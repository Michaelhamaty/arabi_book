#!/usr/bin/env python3
"""Read-only project checks and reading packets. No dependencies or approval actions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
from datetime import date


ROOT = Path(__file__).resolve().parents[1]
STAGES = {
    "planned", "brief_ready", "drafting", "arabizi_review", "revision_needed",
    "translation", "ready_for_author", "accepted",
}
REVIEWED = {"translation", "ready_for_author", "accepted"}
COMPLETE = {"ready_for_author", "accepted"}
NEEDS_ORIGINAL = {"arabizi_review", "revision_needed"} | REVIEWED
REQUIRED = [
    "AGENTS.md", "README.md", "STORY_MASTER.md",
    "development/LANGUAGE_CALIBRATION.md", "planning/ROADMAP.md",
    "memory/CHAPTERS.json", "memory/CURRENT_STATE.md", "memory/STORY_LEDGER.md",
    "memory/DECISIONS.md", "memory/COVERAGE.tsv",
    "prompts/WRITER.md", "prompts/REVIEWER.md", "prompts/TRANSLATOR.md",
    "prompts/ACCEPTANCE.md",
]
ARABIC = re.compile("[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff]")
SCENE = re.compile(r"^##\s+(\d{3,}-S\d{2,})(?=\s|$)", re.MULTILINE)
MARKER = re.compile(r"<!--\s*accepted-through:\s*(none|\d{3,})\s*-->")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text)
                   if not unicodedata.combining(c)).casefold()


def excluded_names(root: Path) -> list[str]:
    """Master owns the exclusion list; do not repeat it in executable config."""
    text = (root / "STORY_MASTER.md").read_text()
    title = "### Excluded personal-name family — editorial enforcement metadata only"
    block = text.split(title, 1)[1].split("\n## ", 1)[0]
    names = re.findall(r"`([A-Za-z]+)`", block)
    if not names:
        raise ValueError("No excluded-name metadata found in master")
    return list(dict.fromkeys(normalized(name) for name in names))


def name_pattern(root: Path) -> re.Pattern:
    return re.compile(r"\b(?:" + "|".join(map(re.escape, excluded_names(root))) + r")\b")


def registry(root: Path) -> dict:
    return json.loads((root / "memory/CHAPTERS.json").read_text())


def local_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("path escapes workspace")
    return path


def review_marker(text: str, field: str, value: str) -> bool:
    return f"<!-- {field}: {value} -->" in text


def check(root: Path) -> list[str]:
    """Return actionable structural errors; do not claim semantic/native validation."""
    errors = []
    for relative in REQUIRED:
        path = root / relative
        if not path.is_file() or not path.read_text().strip():
            errors.append(f"Missing or empty setup record: {relative}")
    if errors:
        return errors
    try:
        data = registry(root)
        excluded = name_pattern(root)
    except (ValueError, KeyError, IndexError) as exc:
        return [f"Invalid setup metadata: {exc}"]
    if data.get("schema_version") != 1 or data.get("story_year") != 2027:
        errors.append("Registry schema/year must be version 1 / 2027")
    chapters = data.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        return errors + ["Registry requires an ordered nonempty chapter list"]
    if not all(isinstance(chapter, dict) for chapter in chapters):
        return errors + ["Each registry chapter must be an object"]
    ids = [chapter.get("id") for chapter in chapters]
    if (any(not isinstance(cid, str) or not re.fullmatch(r"\d{3,}", cid) for cid in ids)
            or len(set(ids)) != len(ids)):
        return errors + ["Chapter IDs must be unique, zero-padded numeric strings"]
    if [int(cid) for cid in ids] != list(range(1, len(ids) + 1)):
        errors.append("Registry chapter IDs must be a sequential list beginning with 001")

    accepted = [c["id"] for c in chapters if c.get("status") == "accepted"]
    if accepted != ids[:len(accepted)]:
        errors.append("Accepted chapters must form a contiguous prefix")
    last = accepted[-1] if accepted else None
    if data.get("last_accepted_chapter") != last:
        errors.append("last_accepted_chapter disagrees with accepted statuses")
    for relative in ["memory/CURRENT_STATE.md", "memory/STORY_LEDGER.md"]:
        match = MARKER.search((root / relative).read_text())
        if not match or match.group(1) != (last or "none"):
            errors.append(f"Accepted-through marker is stale: {relative}")

    known_scenes = set()
    for index, chapter in enumerate(chapters):
        cid = chapter["id"]
        stage = chapter.get("status")
        if stage not in STAGES:
            errors.append(f"{cid}: unknown chapter status")
            continue
        try:
            brief = local_path(root, chapter["brief"])
            if not brief.is_file() or not brief.read_text().strip():
                errors.append(f"{cid}: missing chapter brief")
        except (KeyError, TypeError, ValueError):
            errors.append(f"{cid}: invalid brief path")

        predecessor = ids[index - 1] if index else None
        if stage != "planned":
            if predecessor is not None and predecessor not in accepted:
                errors.append(f"{cid}: preceding chapter is not accepted")
            if chapter.get("based_on_accepted_chapter") != predecessor:
                errors.append(f"{cid}: brief dependency is stale")

        folder = root / "chapters" / cid
        original = folder / "arabizi.md"
        english = folder / "english.md"
        report = folder / "review.md"
        if original.exists() and stage in {"planned", "brief_ready"}:
            errors.append(f"{cid}: manuscript exists but status still says no draft")
        if stage in NEEDS_ORIGINAL and not original.is_file():
            errors.append(f"{cid}: status requires an original")

        original_scenes = []
        for path in [original, english]:
            if not path.is_file():
                continue
            text = path.read_text()
            if not text.strip():
                errors.append(f"{cid}: empty manuscript file {path.name}")
            if excluded.search(normalized(text)):
                errors.append(f"{cid}: excluded personal name in {path.name}")
            if path == original and ARABIC.search(text):
                errors.append(f"{cid}: Arabic-script leakage in original")
            scenes = SCENE.findall(text)
            if not scenes or len(scenes) != len(set(scenes)):
                errors.append(f"{cid}: scene headings missing or duplicated in {path.name}")
            if any(not scene.startswith(cid + "-S") for scene in scenes):
                errors.append(f"{cid}: scene ID belongs to another chapter in {path.name}")
            if path == original:
                original_scenes = scenes
                if known_scenes.intersection(scenes):
                    errors.append(f"{cid}: original scene ID duplicated across chapters")
                known_scenes.update(scenes)
            elif stage in COMPLETE and scenes != original_scenes:
                errors.append(f"{cid}: original/English scene IDs do not align")
        if english.is_file() and not original.is_file():
            errors.append(f"{cid}: English exists without an original")

        if stage in NEEDS_ORIGINAL:
            dates = chapter.get("story_dates")
            if not isinstance(dates, list) or not dates:
                errors.append(f"{cid}: actual story_dates required for review")
            else:
                try:
                    parsed = [date.fromisoformat(value) for value in dates]
                    if any(value.year != 2027 for value in parsed):
                        errors.append(f"{cid}: story date outside 2027")
                    if cid == "001" and any(value >= date(2027, 2, 1) for value in parsed):
                        errors.append("001: departure dates must precede Barcelona arrival")
                except (ValueError, TypeError):
                    errors.append(f"{cid}: invalid story date")
            if not isinstance(chapter.get("locations"), list) or not chapter["locations"]:
                errors.append(f"{cid}: actual locations required for review")
            romantic = chapter.get("contains_romance_or_flirting")
            people = chapter.get("romantic_participants")
            if not isinstance(romantic, bool) or not isinstance(people, list):
                errors.append(f"{cid}: romance metadata must be explicit before review")
            elif bool(people) != romantic:
                errors.append(f"{cid}: romantic participant metadata is inconsistent")
            if cid == "001" and (romantic is not False or people):
                errors.append("001: no pre-Barcelona romantic/flirtation content is allowed")
            if isinstance(people, list):
                for person in people:
                    if (not isinstance(person, dict)
                            or type(person.get("age")) is not int or person["age"] < 20
                            or not person.get("name") or person.get("scene") not in original_scenes):
                        errors.append(f"{cid}: participant needs age 20+, name, and source scene")

        review_text = report.read_text() if report.is_file() else ""
        source_hash = digest(original) if original.is_file() else None
        if stage in REVIEWED:
            if not report.is_file() or not review_text.strip():
                errors.append(f"{cid}: reviewed status requires a substantive review report")
            if not source_hash or chapter.get("reviewed_original_sha256") != source_hash:
                errors.append(f"{cid}: original review is stale or missing")
            if (not source_hash or not review_marker(review_text, "original-sha256", source_hash)
                    or not review_marker(review_text, "original-disposition", "pass")):
                errors.append(f"{cid}: review report does not pass the current original")
            for heading in ["## Scope", "## Findings", "## Resolution", "## New provisional facts"]:
                if heading not in review_text:
                    errors.append(f"{cid}: review report missing {heading}")
        if stage in COMPLETE:
            if not english.is_file():
                errors.append(f"{cid}: complete chapter needs English")
            english_hash = digest(english) if english.is_file() else None
            if not source_hash or chapter.get("translated_from_original_sha256") != source_hash:
                errors.append(f"{cid}: translation is stale or lacks original revision evidence")
            if not english_hash or chapter.get("reviewed_english_sha256") != english_hash:
                errors.append(f"{cid}: English review is stale or missing")
            if (not english_hash or not review_marker(review_text, "english-sha256", english_hash)
                    or not review_marker(review_text, "english-disposition", "pass")):
                errors.append(f"{cid}: review report does not pass the current English")
        acceptance = chapter.get("author_acceptance")
        if stage == "accepted":
            if (not isinstance(acceptance, dict) or not acceptance.get("source")
                    or not acceptance.get("note")):
                errors.append(f"{cid}: actual author acceptance evidence is required")
            if chapter.get("memory_updated") is not True:
                errors.append(f"{cid}: accepted chapter memory transaction is incomplete")
        elif acceptance is not None or chapter.get("memory_updated") is not False:
            errors.append(f"{cid}: unaccepted chapter must not claim acceptance or memory promotion")

    registered = set(ids)
    chapter_root = root / "chapters"
    if chapter_root.is_dir():
        for folder in chapter_root.iterdir():
            if folder.is_dir() and folder.name not in registered:
                errors.append(f"Unregistered chapter directory: {folder.name}")
    export_root = root / "book"
    if export_root.is_dir():
        for path in export_root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".txt", ".html"}:
                if excluded.search(normalized(path.read_text())):
                    errors.append(f"Excluded personal name in book source: {path.relative_to(root)}")

    with (root / "memory/COVERAGE.tsv").open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        expected = ["chapter_id", "scene_id", "situation", "participants", "register",
                    "dialect_voice", "exposure_notes", "source_revision"]
        if reader.fieldnames != expected:
            errors.append("Coverage TSV header does not match the documented schema")
        for row in reader:
            if row["chapter_id"] not in accepted:
                errors.append("Coverage contains exposure from an unaccepted chapter")
            elif row["scene_id"] not in known_scenes:
                errors.append("Coverage references a missing original scene")
    return errors


def packet(root: Path, cid: str, role: str) -> str:
    """Return a current reading list, refusing invalid dependencies or stale inputs."""
    problems = check(root)
    if problems:
        raise ValueError("Project checks failed:\n" + "\n".join(problems))
    data = registry(root)
    chapters = data["chapters"]
    chapter = next((item for item in chapters if item["id"] == cid), None)
    if chapter is None:
        raise ValueError(f"Chapter {cid} is not registered")
    position = chapters.index(chapter)
    predecessor = chapters[position - 1] if position else None
    if role == "writer":
        if chapter["status"] not in {"brief_ready", "drafting", "revision_needed"}:
            raise ValueError("Writer packet requires a ready brief or current writing/revision stage")
        if predecessor and predecessor["status"] != "accepted":
            raise ValueError("Writer packet requires acceptance of the preceding chapter")
        expected = predecessor["id"] if predecessor else None
        if chapter["based_on_accepted_chapter"] != expected:
            raise ValueError("Refresh brief dependency before writing")
    original = root / "chapters" / cid / "arabizi.md"
    if role in {"reviewer", "translator"} and not original.is_file():
        raise ValueError(f"{role.capitalize()} packet needs an actual original draft")
    if role == "translator" and chapter["status"] != "translation":
        raise ValueError("Translator packet requires a passing current original review")

    prompt = {"writer": "WRITER", "reviewer": "REVIEWER", "translator": "TRANSLATOR"}[role]
    inputs = ["AGENTS.md", f"prompts/{prompt}.md", "STORY_MASTER.md",
              "development/LANGUAGE_CALIBRATION.md", "memory/CHAPTERS.json",
              "memory/CURRENT_STATE.md", chapter["brief"]]
    previous = [item for item in chapters[:position] if item["status"] == "accepted"][-2:]
    inputs.extend(f"chapters/{item['id']}/arabizi.md" for item in previous)
    if role != "writer" or original.is_file():
        inputs.append(f"chapters/{cid}/arabizi.md")
    for name in ["review.md", "english.md"]:
        path = root / "chapters" / cid / name
        if path.is_file() and (name != "english.md" or role != "writer"):
            inputs.append(str(path.relative_to(root)))
    lines = [f"# Chapter {cid}: {role} reading packet", "",
             "Read the listed files fully. This is a reading list, not a substitute for them.",
             "Hashes identify current inputs; regenerate this list if any input changes.", ""]
    for number, relative in enumerate(inputs, 1):
        lines.append(f"{number}. {relative}  sha256={digest(root / relative)}")
    lines += ["", "Retrieve relevant older scenes from memory/STORY_LEDGER.md as needed.",
              "Future plans and calibration samples are not accepted events.",
              "The packet does not authorize drafting or provide author acceptance."]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="Validate setup and existing chapter revision metadata")
    packet_parser = commands.add_parser("packet", help="Print a fresh ordered reading list")
    packet_parser.add_argument("chapter")
    packet_parser.add_argument("--role", choices=["writer", "reviewer", "translator"], default="writer")
    hash_parser = commands.add_parser("hash", help="Print SHA-256 of a workspace file")
    hash_parser.add_argument("path")
    args = parser.parse_args()
    try:
        if args.command == "check":
            problems = check(ROOT)
            for problem in problems:
                print(f"ERROR: {problem}", file=sys.stderr)
            if problems:
                return 1
            data = registry(ROOT)
            count = sum(item["status"] == "accepted" for item in data["chapters"])
            print(f"Structural checks passed; {count} accepted chapters.")
            print("Language naturalness, prose quality, and undeclared scene content require human/agent review.")
        elif args.command == "packet":
            print(packet(ROOT, args.chapter, args.role))
        else:
            print(digest(local_path(ROOT, args.path)))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

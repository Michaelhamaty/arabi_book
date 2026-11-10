#!/usr/bin/env python3
"""Read-only project checks, reading packets, and chapter stats. No approval actions."""

from __future__ import annotations

import argparse
import collections
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
    "ready_for_author", "provisionally_accepted", "accepted",
}
SETTLED = {"provisionally_accepted", "accepted"}
REVIEWED = {"ready_for_author"} | SETTLED
NEEDS_ORIGINAL = {"arabizi_review", "revision_needed"} | REVIEWED
ROLES = {
    "planner": "PLANNER",
    "writer": "WRITER",
    "language_reviewer": "LANGUAGE_REVIEWER",
    "story_reviewer": "STORY_REVIEWER",
    "archivist": "ARCHIVIST",
}
REQUIRED = [
    "AGENTS.md", "README.md", "STORY_MASTER.md",
    "development/LANGUAGE_CALIBRATION.md", "development/LEXICON.tsv",
    "planning/ROADMAP.md",
    "memory/CHAPTERS.json", "memory/CURRENT_STATE.md", "memory/STORY_LEDGER.md",
    "memory/DECISIONS.md", "memory/COVERAGE.tsv",
    "prompts/OVERNIGHT.md", "prompts/ACCEPTANCE.md",
] + [f"prompts/{name}.md" for name in ROLES.values()]
ARABIC = re.compile("[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff]")
SCENE = re.compile(r"^##\s+(\d{3,}-S\d{2,})(?=\s|$)", re.MULTILINE)
MARKER = re.compile(r"<!--\s*settled-through:\s*(none|\d{3,})\s*-->")
LABEL = re.compile(r"^(?:>\s*)?\*\*([^*:]+):\*\*", re.MULTILINE)
WORD = re.compile(r"[A-Za-z0-9\u00c0-\u024f]+")


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


def lexicon(root: Path) -> dict[str, str]:
    """Disallowed spelling variant -> preferred form, from development/LEXICON.tsv."""
    with (root / "development/LEXICON.tsv").open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        if rows.fieldnames != ["variant", "preferred", "note"]:
            raise ValueError("LEXICON.tsv header must be variant, preferred, note")
        return {row["variant"].casefold(): row["preferred"] for row in rows if row["variant"]}


def lexicon_hits(text: str, table: dict[str, str]) -> list[str]:
    hits = collections.Counter(word.casefold() for word in WORD.findall(text)
                               if word.casefold() in table)
    return [f"{word}→{table[word]} ×{count}" for word, count in sorted(hits.items())]


def registry(root: Path) -> dict:
    return json.loads((root / "memory/CHAPTERS.json").read_text())


def local_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("path escapes workspace")
    return path


def review_marker(text: str, field: str, value: str) -> bool:
    return f"<!-- {field}: {value} -->" in text


def revising(chapter: dict | None) -> bool:
    """A previously settled chapter that is being deliberately revised."""
    return bool(chapter and chapter.get("acceptance_history"))


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
        spelling = lexicon(root)
    except (ValueError, KeyError, IndexError) as exc:
        return [f"Invalid setup metadata: {exc}"]
    if data.get("schema_version") != 3 or data.get("story_year") != 2027:
        errors.append("Registry schema/year must be version 3 / 2027 (Arabizi only)")
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

    settled = [c["id"] for c in chapters if c.get("status") in SETTLED]
    accepted = [c["id"] for c in chapters if c.get("status") == "accepted"]
    if settled != ids[:len(settled)]:
        errors.append("Settled chapters must form a contiguous prefix")
    if accepted != ids[:len(accepted)]:
        errors.append("Author-accepted chapters must precede provisional ones")
    if data.get("last_settled_chapter") != (settled[-1] if settled else None):
        errors.append("last_settled_chapter disagrees with settled statuses")
    if data.get("last_accepted_chapter") != (accepted[-1] if accepted else None):
        errors.append("last_accepted_chapter disagrees with author-accepted statuses")
    last = settled[-1] if settled else None
    for relative in ["memory/CURRENT_STATE.md", "memory/STORY_LEDGER.md"]:
        match = MARKER.search((root / relative).read_text())
        if not match or match.group(1) != (last or "none"):
            errors.append(f"Settled-through marker is stale: {relative}")

    known_scenes = set()
    hashes = {}
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

        predecessor = chapters[index - 1] if index else None
        if stage != "planned":
            if (predecessor is not None and predecessor.get("status") not in SETTLED
                    and not revising(predecessor)):
                errors.append(f"{cid}: preceding chapter is not settled")
            if chapter.get("based_on_accepted_chapter") != (predecessor["id"] if predecessor else None):
                errors.append(f"{cid}: brief dependency is stale")

        folder = root / "chapters" / cid
        original = folder / "arabizi.md"
        if (folder / "english.md").is_file():
            errors.append(f"{cid}: English edition is disabled; preserve unexpected files for user resolution")
        if any(field in chapter for field in ["translated_from_original_sha256", "reviewed_english_sha256"]):
            errors.append(f"{cid}: obsolete translation fields in Arabizi-only registry")
        report = folder / "review.md"
        if original.exists() and stage in {"planned", "brief_ready"}:
            errors.append(f"{cid}: manuscript exists but status still says no draft")
        if stage in NEEDS_ORIGINAL and not original.is_file():
            errors.append(f"{cid}: status requires an original")

        original_scenes = []
        if original.is_file():
            text = original.read_text()
            if not text.strip():
                errors.append(f"{cid}: empty manuscript file")
            if excluded.search(normalized(text)):
                errors.append(f"{cid}: excluded personal name in manuscript")
            if ARABIC.search(text):
                errors.append(f"{cid}: Arabic-script leakage in original")
            hits = lexicon_hits(text, spelling)
            if hits:
                errors.append(f"{cid}: spelling drift against LEXICON.tsv: " + ", ".join(hits))
            original_scenes = SCENE.findall(text)
            if not original_scenes or len(original_scenes) != len(set(original_scenes)):
                errors.append(f"{cid}: scene headings missing or duplicated")
            if any(not scene.startswith(cid + "-S") for scene in original_scenes):
                errors.append(f"{cid}: scene ID belongs to another chapter")
            if known_scenes.intersection(original_scenes):
                errors.append(f"{cid}: original scene ID duplicated across chapters")
            known_scenes.update(original_scenes)

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
            if not review_text.strip():
                errors.append(f"{cid}: reviewed status requires a substantive review report")
            if not source_hash or chapter.get("reviewed_original_sha256") != source_hash:
                errors.append(f"{cid}: original review is stale or missing")
            if (not source_hash or not review_marker(review_text, "original-sha256", source_hash)
                    or not review_marker(review_text, "original-disposition", "pass")):
                errors.append(f"{cid}: review report does not pass the current original")
            for heading in ["## Scope", "## Findings", "## Resolution", "## New provisional facts"]:
                if heading not in review_text:
                    errors.append(f"{cid}: review report missing {heading}")
            hashes[cid] = source_hash

        acceptance = chapter.get("author_acceptance")
        provisional = chapter.get("provisional_acceptance")
        evidence = lambda item: isinstance(item, dict) and item.get("source") and item.get("note")
        if stage == "accepted":
            if not evidence(acceptance):
                errors.append(f"{cid}: actual author acceptance evidence is required")
        elif acceptance is not None:
            errors.append(f"{cid}: only an accepted chapter may record author acceptance")
        if stage == "provisionally_accepted" and not evidence(provisional):
            errors.append(f"{cid}: provisional acceptance needs the standing user instruction as evidence")
        if stage not in SETTLED and provisional is not None:
            errors.append(f"{cid}: unsettled chapter must not claim provisional acceptance")
        if (stage in SETTLED) != (chapter.get("memory_updated") is True):
            errors.append(f"{cid}: memory_updated must be true exactly for settled chapters")

    chapter_root = root / "chapters"
    if chapter_root.is_dir():
        for folder in chapter_root.iterdir():
            if folder.is_dir() and folder.name not in set(ids):
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
            if row["chapter_id"] not in settled:
                errors.append("Coverage contains exposure from an unsettled chapter")
            elif row["scene_id"] not in known_scenes:
                errors.append("Coverage references a missing original scene")
            elif row["source_revision"] != hashes.get(row["chapter_id"]):
                errors.append(f"Coverage row for {row['scene_id']} cites a stale source revision")
    return errors


def packet(root: Path, cid: str, role: str) -> str:
    """Return a current reading list, refusing invalid dependencies or stale inputs."""
    if role not in ROLES:
        raise ValueError(f"Role must be one of: {', '.join(sorted(ROLES))} (Arabizi only)")
    problems = check(root)
    if problems:
        raise ValueError("Project checks failed:\n" + "\n".join(problems))
    data = registry(root)
    chapters = data["chapters"]
    chapter = next((item for item in chapters if item["id"] == cid), None)
    if chapter is None:
        if role != "planner" or int(cid) != len(chapters) + 1:
            raise ValueError(f"Chapter {cid} is not registered; only the planner may open the next ID")
        position = len(chapters)
    else:
        position = chapters.index(chapter)
    predecessor = chapters[position - 1] if position else None
    original = root / "chapters" / cid / "arabizi.md"
    status = chapter["status"] if chapter else None

    if role in {"planner", "writer"}:
        if predecessor and predecessor["status"] not in SETTLED:
            raise ValueError(f"{role} packet requires the preceding chapter to be settled")
    if role == "planner" and status not in {None, "planned", "brief_ready"}:
        raise ValueError("Planner packet is only for an unwritten chapter")
    if role == "writer":
        if status not in {"brief_ready", "drafting", "revision_needed"}:
            raise ValueError("Writer packet requires a ready brief or current writing/revision stage")
        if chapter["based_on_accepted_chapter"] != (predecessor["id"] if predecessor else None):
            raise ValueError("Refresh brief dependency before writing")
    if role in {"language_reviewer", "story_reviewer"}:
        if not original.is_file():
            raise ValueError("Reviewer packet needs an actual original draft")
        if status not in {"arabizi_review", "revision_needed"}:
            raise ValueError("Reviewer packet requires arabizi_review or revision_needed")
    if role == "archivist" and status != "ready_for_author":
        raise ValueError("Archivist packet requires a chapter that passed review")

    inputs = ["AGENTS.md", f"prompts/{ROLES[role]}.md", "STORY_MASTER.md",
              "development/LANGUAGE_CALIBRATION.md", "development/LEXICON.tsv",
              "memory/CHAPTERS.json", "memory/CURRENT_STATE.md"]
    if role in {"planner", "archivist", "story_reviewer"}:
        inputs += ["memory/STORY_LEDGER.md", "memory/DECISIONS.md"]
    if role in {"planner", "archivist"}:
        inputs += ["planning/ROADMAP.md", "memory/COVERAGE.tsv"]
    if chapter:
        inputs.append(chapter["brief"])
    previous = [item for item in chapters[:position]
                if item["status"] in SETTLED or revising(item)][-2:]
    inputs.extend(f"chapters/{item['id']}/arabizi.md" for item in previous)
    if original.is_file():
        inputs.append(f"chapters/{cid}/arabizi.md")
    report = root / "chapters" / cid / "review.md"
    if report.is_file() and role != "planner":
        inputs.append(f"chapters/{cid}/review.md")
    lines = [f"# Chapter {cid}: {role} reading packet", "",
             "Read the listed files fully. This is a reading list, not a substitute for them.",
             "Hashes identify current inputs; regenerate this list if any input changes.", ""]
    for number, relative in enumerate(inputs, 1):
        lines.append(f"{number}. {relative}  sha256={digest(root / relative)}")
    lines += ["", "Retrieve relevant older scenes through memory/STORY_LEDGER.md as needed.",
              "Future plans and calibration samples are not settled events.",
              "The packet does not authorize drafting or provide author acceptance."]
    return "\n".join(lines)


def stats(root: Path, cid: str) -> str:
    """Reviewer aid: size, speakers, spelling drift, and repeated narration words."""
    original = root / "chapters" / cid / "arabizi.md"
    text = original.read_text()
    speakers = collections.Counter(LABEL.findall(text))
    narration = "\n".join(line for line in text.splitlines()
                          if line.strip() and not line.startswith(("#", "*", ">")))
    stop = {"w", "el", "3al", "3a", "la", "bel", "men", "ma", "kan", "kanet", "howwe",
            "hiye", "shi", "fi", "ba3den", "lal", "ma3", "elli", "fo2", "ta7t", "bass", "hon"}
    words = collections.Counter(word.casefold() for word in WORD.findall(narration)
                                if word.casefold() not in stop and len(word) > 2)
    hits = lexicon_hits(text, lexicon(root))
    lines = [f"Chapter {cid}: {len(WORD.findall(text))} words, "
             f"{sum(speakers.values())} labeled passages, scenes {', '.join(SCENE.findall(text))}",
             "Speakers: " + ", ".join(f"{name} {count}" for name, count in speakers.most_common()),
             "Most repeated narration words: " + ", ".join(f"{w} {c}" for w, c in words.most_common(15)),
             "Spelling drift: " + (", ".join(hits) if hits else "none")]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="Validate setup and existing chapter revision metadata")
    packet_parser = commands.add_parser("packet", help="Print a fresh ordered reading list")
    packet_parser.add_argument("chapter")
    packet_parser.add_argument("--role", choices=sorted(ROLES), default="writer")
    stats_parser = commands.add_parser("stats", help="Print reviewer statistics for a chapter")
    stats_parser.add_argument("chapter")
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
            settled = sum(item["status"] in SETTLED for item in data["chapters"])
            accepted = sum(item["status"] == "accepted" for item in data["chapters"])
            print(f"Structural checks passed; {settled} settled chapters ({accepted} author-ratified).")
            print("Language naturalness, prose quality, and undeclared scene content require human/agent review.")
        elif args.command == "packet":
            print(packet(ROOT, args.chapter, args.role))
        elif args.command == "stats":
            print(stats(ROOT, args.chapter))
        else:
            print(digest(local_path(ROOT, args.path)))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

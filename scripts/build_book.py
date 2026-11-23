#!/usr/bin/env python3
"""Assemble the settled Arabizi chapters into a printable book (HTML + PDF).

    python3 scripts/build_book.py              # settled chapters only
    python3 scripts/build_book.py --include-unsettled

Outputs `book/Bayn-Balad-w-Balad.html` and `book/Bayn-Balad-w-Balad.pdf`.

The chapter sources under `chapters/NNN/arabizi.md` stay authoritative; this
script only typesets them. Editorial metadata (scene IDs, hashes, briefs,
reviews) never reaches the book. Layout: US Letter, double-sided, mirrored
margins, every chapter and part opening on a right-hand page.

Requirements beyond the standard library: `pypdf`, and Node with the
pre-installed `playwright` package and Chromium (used only to render).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
STEM = "Bayn-Balad-w-Balad"
TITLE = "Bayn Balad w Balad"
SETTLED = {"provisionally_accepted", "accepted"}

# Parts follow the itinerary in planning/ROADMAP.md (inclusive chapter ranges).
# Only parts that contain an included chapter are printed.
PARTS = [
    ("001", "001", "San Francisco · Los Angeles"),
    ("002", "019", "Barcelona"),
    ("020", "027", "Lebnen"),
    ("028", "999", "Barcelona, marra tenye"),
]
ROMAN = ["I", "II", "III", "IV", "V", "VI"]

# Page geometry (inches). Inner = binding side.
PAGE_W, PAGE_H = 8.5, 11.0
M_TOP, M_BOTTOM, M_INNER, M_OUTER = 1.0, 1.05, 1.3, 1.0


# --------------------------------------------------------------------------
# Manuscript parsing
# --------------------------------------------------------------------------

@dataclass
class Scene:
    title: str | None
    blocks: list[tuple[str, str]] = field(default_factory=list)  # (kind, text)


@dataclass
class Chapter:
    cid: str
    title: str
    scenes: list[Scene]

    @property
    def number(self) -> int:
        return int(self.cid)


CHAPTER_RE = re.compile(r"^# (\d{3}) — (.+)$")
SCENE_RE = re.compile(r"^## \d{3}-S\d{2} — (.+)$")


def parse_chapter(cid: str, text: str) -> Chapter:
    title = None
    scenes: list[Scene] = []
    para: list[str] = []

    def flush() -> None:
        if not para:
            return
        quoted = all(line.lstrip().startswith(">") for line in para)
        joined = " ".join(re.sub(r"^\s*>?\s*", "", line) if quoted else line.strip()
                          for line in para)
        para.clear()
        if not scenes:
            scenes.append(Scene(None))  # untitled bridge before the first scene
        if quoted:
            scenes[-1].blocks.append(("message", joined.strip()))
        elif re.fullmatch(r"(\*\s*){1,3}", joined):
            scenes[-1].blocks.append(("skip", ""))
        elif re.fullmatch(r"\*[^*].*[^*]\*", joined):
            scenes[-1].blocks.append(("dateline", joined[1:-1]))
        elif joined.startswith("**") and re.match(r"^\*\*[^*]+:\*\*", joined):
            scenes[-1].blocks.append(("speech", joined))
        else:
            scenes[-1].blocks.append(("narration", joined))

    for raw in text.splitlines():
        line = raw.rstrip()
        if m := CHAPTER_RE.match(line):
            flush()
            if m.group(1) != cid:
                raise ValueError(f"{cid}: heading names chapter {m.group(1)}")
            title = m.group(2).strip()
        elif m := SCENE_RE.match(line):
            flush()
            scenes.append(Scene(m.group(1).strip()))
        elif line.startswith("#"):
            raise ValueError(f"{cid}: unexpected heading {line!r}")
        elif not line.strip():
            flush()
        else:
            para.append(line)
    flush()
    if not title or not scenes:
        raise ValueError(f"{cid}: missing chapter title or scenes")
    return Chapter(cid, title, scenes)


def load_chapters(include_unsettled: bool) -> tuple[list[Chapter], list[str]]:
    registry = json.loads((ROOT / "memory/CHAPTERS.json").read_text())
    chapters, notes = [], []
    for entry in registry["chapters"]:
        cid, status = entry["id"], entry["status"]
        path = ROOT / "chapters" / cid / "arabizi.md"
        if not path.exists():
            continue
        data = path.read_bytes()
        if status not in SETTLED:
            if not include_unsettled:
                notes.append(f"skipped {cid} ({status})")
                continue
            notes.append(f"included unsettled {cid} ({status})")
        elif hashlib.sha256(data).hexdigest() != entry.get("reviewed_original_sha256"):
            notes.append(f"WARNING {cid}: text differs from its reviewed hash")
        chapters.append(parse_chapter(cid, data.decode("utf-8")))
    return chapters, notes


# --------------------------------------------------------------------------
# HTML
# --------------------------------------------------------------------------

def smart_quotes(text: str) -> str:
    text = re.sub(r'(^|[\s(\[—–-])"', "\\1“", text)
    text = text.replace('"', "”")
    text = re.sub(r"(^|[\s(\[—–-])'", "\\1‘", text)
    return text.replace("'", "’")


def inline(text: str) -> str:
    out = html.escape(smart_quotes(text), quote=False)
    out = re.sub(r"\*\*([^*]+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\*([^*]+?)\*", r"<em>\1</em>", out)
    if "*" in out:
        raise ValueError(f"Unbalanced emphasis: {text[:80]!r}")
    return out


def labelled(text: str) -> str:
    m = re.match(r"^\*\*([^*]+?:)\*\*\s*(.*)$", text)
    if not m:
        return inline(text)
    return f'<span class="who">{inline(m.group(1))}</span> {inline(m.group(2))}'


def part_for(cid: str) -> int | None:
    for i, (lo, hi, _) in enumerate(PARTS):
        if lo <= cid <= hi:
            return i
    return None


def chapter_html(ch: Chapter) -> str:
    parts = [f'<section class="chapter" id="ch{ch.cid}">',
             '<header class="opener">',
             f'<div class="ch-num">{ch.number}</div>',
             f'<h1 class="ch-title">{inline(ch.title)}</h1>',
             '</header>']
    for i, scene in enumerate(ch.scenes):
        cls = "scene first" if i == 0 else "scene"
        parts.append(f'<div class="{cls}">')
        if i:
            parts.append('<div class="break" aria-hidden="true">*&#8195;*&#8195;*</div>')
        if scene.title:
            parts.append(f'<h2 class="scene-title">{inline(scene.title)}</h2>')
        for kind, text in scene.blocks:
            if kind == "skip":
                parts.append('<div class="skip" aria-hidden="true">*</div>')
            elif kind == "dateline":
                parts.append(f'<p class="dateline">{inline(text)}</p>')
            elif kind == "message":
                parts.append(f'<blockquote class="message"><p>{labelled(text)}</p></blockquote>')
            elif kind == "speech":
                parts.append(f'<p class="speech">{labelled(text)}</p>')
            else:
                parts.append(f"<p>{inline(text)}</p>")
        parts.append("</div>")
    parts.append("</section>")
    return "\n".join(parts)


def css(font_url: str) -> str:
    fonts = "".join(
        f"""@font-face {{ font-family: "Literata"; font-style: {style}; font-weight: {weight};
  src: url("{font_url}/literata-latin-{weight}-{style}.woff2") format("woff2"); }}\n"""
        for weight, style in [(300, "normal"), (400, "normal"), (400, "italic"),
                              (700, "normal"), (700, "italic")])
    return fonts + f"""
@page {{ size: {PAGE_W}in {PAGE_H}in; margin: {M_TOP}in {M_OUTER}in {M_BOTTOM}in {M_INNER}in; }}
@page :left {{ margin-left: {M_OUTER}in; margin-right: {M_INNER}in; }}
html {{ font-family: "Literata", Georgia, serif; font-size: 12pt; line-height: 1.5;
  color: #111; font-variant-numeric: lining-nums; font-kerning: normal;
  font-synthesis: none; }}
body {{ margin: 0; }}
p {{ margin: 0 0 0.42em; text-align: justify; text-justify: inter-word;
  orphans: 2; widows: 2; }}
.who {{ font-weight: 700; }}
p.speech {{ padding-left: 1.4em; text-indent: -1.4em; }}
blockquote.message {{ margin: 0.5em 1.6em 0.75em 1.4em; padding: 0.15em 0 0.15em 0.85em;
  border-left: 1.5pt solid #9a9a9a; break-inside: avoid; }}
blockquote.message p {{ margin: 0; font-size: 0.95em; font-style: italic; text-align: left; }}
blockquote.message .who {{ font-style: normal; }}

/* front matter */
.front {{ page: front; break-after: page; }}
.titlepage {{ height: 8.6in; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center; }}
.titlepage h1 {{ font-weight: 300; font-size: 40pt; line-height: 1.15; margin: 0;
  letter-spacing: 0.01em; }}
.titlepage .rule {{ width: 1.1in; border-top: 0.75pt solid #111; margin: 0.35in 0; }}
.titlepage .sub {{ font-style: italic; font-size: 14pt; }}
.verso {{ height: 8.8in; display: flex; flex-direction: column; justify-content: flex-end;
  font-size: 9.5pt; line-height: 1.6; color: #333; }}
.toc h1 {{ font-weight: 300; font-size: 24pt; text-align: center; margin: 0.6in 0 0.45in; }}
.toc ol {{ list-style: none; margin: 0 0.2in; padding: 0; }}
.toc li {{ margin: 0; }}
.toc a {{ color: inherit; text-decoration: none; display: flex; align-items: baseline; }}
.toc .part a {{ font-variant-caps: all-small-caps; letter-spacing: 0.08em;
  margin: 0.55em 0 0.2em; font-size: 11.5pt; }}
.toc .chap a {{ font-size: 11.5pt; line-height: 1.75; }}
.toc .n {{ width: 2.2em; flex: none; }}
.toc .t {{ flex: none; }}
.toc .dots {{ flex: 1; border-bottom: 1pt dotted #888; margin: 0 0.5em; transform: translateY(-0.25em); }}
.toc .pg {{ flex: none; min-width: 2.2em; text-align: right; }}
.blank {{ page: blank; break-before: page; height: 1px; }}

/* parts */
.part-page {{ page: front; break-before: page; height: 8.4in; display: flex;
  flex-direction: column; justify-content: center; align-items: center; text-align: center; }}
.part-page .roman {{ font-size: 13pt; letter-spacing: 0.3em; margin-bottom: 0.25in; }}
.part-page h1 {{ font-weight: 300; font-size: 30pt; margin: 0; }}

/* chapters */
.chapter {{ break-before: page; }}
.opener {{ padding-top: 1.55in; margin-bottom: 0.5in; text-align: center; }}
.ch-num {{ font-weight: 300; font-size: 44pt; line-height: 1; margin-bottom: 0.2in; }}
.ch-title {{ font-weight: 400; font-style: italic; font-size: 20pt; line-height: 1.25; margin: 0; }}
.scene-title {{ font-weight: 400; font-size: 11pt; font-variant-caps: all-small-caps;
  letter-spacing: 0.1em; text-align: center; margin: 0 0 0.35em; break-after: avoid; }}
.scene.first .scene-title {{ margin-top: 0; }}
.break {{ text-align: center; margin: 1.1em 0 0.9em; letter-spacing: 0.1em; break-after: avoid; }}
.skip {{ text-align: center; margin: 0.7em 0 0.6em; break-after: avoid; }}
.dateline {{ text-align: center; font-style: italic; font-size: 0.92em; color: #333;
  margin: 0 0 1.1em; break-after: avoid; }}
"""


@dataclass
class Layout:
    chapter_pages: dict[str, int] = field(default_factory=dict)   # 1-based physical page
    part_pages: dict[int, int] = field(default_factory=dict)
    first_body_page: int = 0                                       # physical page shown as "1"

    def folio(self, physical: int) -> int:
        return physical - self.first_body_page + 1


def book_html(chapters: list[Chapter], font_url: str, layout: Layout | None,
              blanks_before: set[str], edition: str) -> str:
    folio = (lambda p: str(layout.folio(p))) if layout else (lambda p: "000")
    toc, body = [], []
    current_part = None
    for ch in chapters:
        pi = part_for(ch.cid)
        if pi is not None and pi != current_part:
            current_part = pi
            key = f"part{pi}"
            page = folio(layout.part_pages[pi]) if layout else "000"
            toc.append(f'<li class="part"><a href="#{key}"><span class="t">{inline(PARTS[pi][2])}</span>'
                       f'<span class="dots"></span><span class="pg">{page}</span></a></li>')
            if key in blanks_before:
                body.append('<div class="blank"></div>')
            body.append(f'<section class="part-page" id="{key}"><div class="roman">{ROMAN[pi]}</div>'
                        f'<h1>{inline(PARTS[pi][2])}</h1></section>')
        page = folio(layout.chapter_pages[ch.cid]) if layout else "000"
        toc.append(f'<li class="chap"><a href="#ch{ch.cid}"><span class="n">{ch.number}</span>'
                   f'<span class="t">{inline(ch.title)}</span><span class="dots"></span>'
                   f'<span class="pg">{page}</span></a></li>')
        if f"ch{ch.cid}" in blanks_before:
            body.append('<div class="blank"></div>')
        body.append(chapter_html(ch))

    front = f"""
<section class="front titlepage"><h1>{TITLE}</h1><div class="rule"></div>
<div class="sub">riwaye</div></section>
<section class="front verso"><p>{edition}</p></section>
<section class="front toc"><h1>El fehres</h1><ol>
{chr(10).join(toc)}
</ol></section>
"""
    return f"""<!doctype html>
<html lang="und-Latn"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>{css(font_url)}</style></head>
<body>
{front}
{chr(10).join(body)}
</body></html>
"""


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

RENDER_JS = """
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, preferCSSPageSize: true, printBackground: true });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
"""


def render(html_text: str, work: Path, name: str) -> Path:
    src, out = work / f"{name}.html", work / f"{name}.pdf"
    src.write_text(html_text, encoding="utf-8")
    js = work / "render.js"
    if not js.exists():
        js.write_text(RENDER_JS)
    subprocess.run(["node", str(js), str(src), str(out)], check=True, cwd=work)
    return out


def destinations(pdf: Path) -> dict[str, int]:
    reader = PdfReader(str(pdf))
    return {name.lstrip("/"): reader.get_destination_page_number(dest) + 1
            for name, dest in reader.named_destinations.items()}


def measure(chapters: list[Chapter], dests: dict[str, int]) -> tuple[Layout, set[str]]:
    """From an unpadded render, insert blanks so every part/chapter opens recto."""
    order = []
    seen = set()
    for ch in chapters:
        pi = part_for(ch.cid)
        if pi is not None and pi not in seen:
            seen.add(pi)
            order.append(f"part{pi}")
        order.append(f"ch{ch.cid}")
    shift, blanks, layout = 0, set(), Layout()
    for key in order:
        page = dests[key] + shift
        if page % 2 == 0:
            blanks.add(key)
            shift += 1
            page += 1
        if key.startswith("part"):
            layout.part_pages[int(key[4:])] = page
        else:
            layout.chapter_pages[key[2:]] = page
    layout.first_body_page = dests[order[0]] + (1 if order[0] in blanks else 0)
    return layout, blanks


def overlay_html(layout: Layout, pages: list[dict], font_url: str) -> str:
    cells = []
    for info in pages:
        right = info["n"] % 2 == 1
        inner, outer = M_INNER, M_OUTER
        left_margin = inner if right else outer
        width = PAGE_W - inner - outer
        head = html.escape(info.get("head", ""))
        folio = info.get("folio", "")
        cells.append(
            f'<div class="pg"><div class="head" style="left:{left_margin}in;width:{width}in">{head}</div>'
            f'<div class="folio" style="left:{left_margin}in;width:{width}in">{folio}</div></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{css(font_url).split('@page')[0]}
@page {{ size: {PAGE_W}in {PAGE_H}in; margin: 0; }}
body {{ margin: 0; font-family: "Literata", serif; color: #333; font-variant-numeric: lining-nums; }}
.pg {{ position: relative; width: {PAGE_W}in; height: {PAGE_H}in; break-after: page; overflow: hidden; }}
.head {{ position: absolute; top: 0.55in; text-align: center; font-size: 9pt;
  font-variant-caps: all-small-caps; letter-spacing: 0.12em; }}
.folio {{ position: absolute; bottom: 0.55in; text-align: center; font-size: 9.5pt; }}
</style></head><body>{''.join(cells)}</body></html>"""


def build(include_unsettled: bool, keep_html: bool) -> None:
    chapters, notes = load_chapters(include_unsettled)
    for note in notes:
        print(note)
    if not chapters:
        sys.exit("No chapters to build.")
    numbers = [c.number for c in chapters]
    edition = (f"Nos5a lal 2raye — el fsoul {numbers[0]}–{numbers[-1]}<br>"
               f"{dt.date.today():%d.%m.%Y}")

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        font_url = (BOOK / "fonts").as_uri()

        # Pass 1: measure natural page positions.
        first = render(book_html(chapters, font_url, None, set(), edition), work, "pass1")
        layout, blanks = measure(chapters, destinations(first))

        # Pass 2: padded, with real TOC page numbers; verify positions held.
        final_html = book_html(chapters, font_url, layout, blanks, edition)
        second = render(final_html, work, "pass2")
        got = destinations(second)
        for cid, page in layout.chapter_pages.items():
            if got[f"ch{cid}"] != page or page % 2 != 1:
                sys.exit(f"Layout drift: chapter {cid} expected p{page}, got p{got[f'ch{cid}']}")
        for pi, page in layout.part_pages.items():
            if got[f"part{pi}"] != page:
                sys.exit(f"Layout drift: part {pi} expected p{page}, got p{got[f'part{pi}']}")

        # Running heads and folios.
        reader = PdfReader(str(second))
        openers = {page: cid for cid, page in layout.chapter_pages.items()}
        part_pages = set(layout.part_pages.values())
        titles = {c.cid: c.title for c in chapters}
        starts = sorted((page, cid) for cid, page in layout.chapter_pages.items())
        info = []
        for n in range(1, len(reader.pages) + 1):
            entry = {"n": n}
            text = reader.pages[n - 1].extract_text().strip()
            if n >= layout.first_body_page and text and n not in part_pages:
                entry["folio"] = layout.folio(n)
                if n not in openers:
                    current = [cid for page, cid in starts if page <= n][-1]
                    entry["head"] = titles[current] if n % 2 == 1 else TITLE
            info.append(entry)
        over = PdfReader(str(render(overlay_html(layout, info, font_url), work, "overlay")))

        writer = PdfWriter(clone_from=reader)
        for page, stamp in zip(writer.pages, over.pages):
            page.merge_page(stamp)
            page.compress_content_streams()
        writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
        for pi, page in sorted(layout.part_pages.items(), key=lambda kv: kv[1]):
            parent = writer.add_outline_item(PARTS[pi][2], page - 1)
            for ch in chapters:
                if part_for(ch.cid) == pi:
                    writer.add_outline_item(f"{ch.number}. {ch.title}",
                                            layout.chapter_pages[ch.cid] - 1, parent=parent)
        writer.add_metadata({"/Title": TITLE, "/Subject": "Riwaye", "/Creator": "scripts/build_book.py"})
        writer.page_mode = "/UseOutlines"
        BOOK.mkdir(exist_ok=True)
        pdf_path = BOOK / f"{STEM}.pdf"
        with pdf_path.open("wb") as handle:
            writer.write(handle)
        if keep_html:
            (BOOK / f"{STEM}.html").write_text(
                final_html.replace(font_url, "fonts"), encoding="utf-8")

    words = sum(len(t.split()) for c in chapters for s in c.scenes for _, t in s.blocks)
    print(f"Built {pdf_path.relative_to(ROOT)}: {len(info)} pages, chapters "
          f"{chapters[0].cid}–{chapters[-1].cid}, ~{words:,} words.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--include-unsettled", action="store_true",
                        help="also include drafted chapters that are not yet settled")
    parser.add_argument("--no-html", action="store_true", help="do not keep the HTML edition")
    args = parser.parse_args()
    if not shutil.which("node"):
        sys.exit("Node.js with the playwright package is required to render the PDF.")
    build(args.include_unsettled, not args.no_html)


if __name__ == "__main__":
    main()

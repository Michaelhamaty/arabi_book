"""Checks for the book typesetter's manuscript parsing (no rendering)."""

import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_book", ROOT / "scripts/build_book.py")
build_book = importlib.util.module_from_spec(SPEC)
sys.modules["build_book"] = build_book
SPEC.loader.exec_module(build_book)

SAMPLE = """# 042 — Shi jdid

Bridge bala 3onwan.

> **Rami:** El bab el a5dar.
> W ma tet2a55ar.

## 042-S01 — Awwal

*Barcelona — 1 shbat 2027.*

**Michael:** "Ahla" w 'salam'.

*

Narration *ma3* emphasis.
"""


class BuildBookParsing(unittest.TestCase):
    def test_sample_blocks(self):
        chapter = build_book.parse_chapter("042", SAMPLE)
        self.assertEqual(chapter.title, "Shi jdid")
        bridge, scene = chapter.scenes
        self.assertIsNone(bridge.title)
        self.assertEqual(bridge.blocks[1], ("message", "**Rami:** El bab el a5dar. W ma tet2a55ar."))
        self.assertEqual([kind for kind, _ in scene.blocks],
                         ["dateline", "speech", "skip", "narration"])

    def test_inline_markup(self):
        out = build_book.labelled('**Michael:** "Ahla" w \'salam\'.')
        self.assertEqual(out, '<span class="who">Michael:</span> “Ahla” w ‘salam’.')
        self.assertNotIn("*", build_book.inline("Narration *ma3* emphasis."))

    def test_all_settled_chapters_parse(self):
        chapters, _ = build_book.load_chapters(include_unsettled=False)
        self.assertTrue(chapters)
        for chapter in chapters:
            html = build_book.chapter_html(chapter)
            self.assertNotRegex(html, r"\d{3}-S\d{2}")
            self.assertNotIn("**", html)


if __name__ == "__main__":
    unittest.main()

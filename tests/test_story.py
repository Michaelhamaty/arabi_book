"""Regression checks for revision, dependency, settlement, and spelling safeguards."""

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("story", ROOT / "scripts/story.py")
story = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(story)
EVIDENCE = {"source": "test fixture, not a real approval", "note": "fixture revision"}


class StoryChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        briefs = [chapter["brief"] for chapter in story.registry(ROOT)["chapters"]]
        for name in story.REQUIRED + briefs:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, path)
        # Fixtures describe an empty writing window, independent of live progress.
        data = story.registry(self.root)
        data["last_accepted_chapter"] = None
        data["last_settled_chapter"] = None
        for index, chapter in enumerate(data["chapters"]):
            chapter.pop("acceptance_history", None)
            chapter.update(status="brief_ready" if index == 0 else "planned",
                           based_on_accepted_chapter=None, story_dates=[], locations=[],
                           contains_romance_or_flirting=False if index == 0 else None,
                           romantic_participants=[], reviewed_original_sha256=None,
                           provisional_acceptance=None, author_acceptance=None,
                           memory_updated=False)
        self.write(data)
        for relative in ["memory/CURRENT_STATE.md", "memory/STORY_LEDGER.md"]:
            (self.root / relative).write_text("# Test baseline\n\n<!-- settled-through: none -->\n")
        # The fixture has no settled story, so retain the TSV schema, not live rows.
        coverage = self.root / "memory/COVERAGE.tsv"
        coverage.write_text(coverage.read_text().splitlines()[0] + "\n")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, data):
        (self.root / "memory/CHAPTERS.json").write_text(json.dumps(data))

    def update(self, index=0, **changes):
        data = story.registry(self.root)
        data["chapters"][index].update(changes)
        self.write(data)

    def markers(self, value):
        for relative in ["memory/CURRENT_STATE.md", "memory/STORY_LEDGER.md"]:
            (self.root / relative).write_text(f"# Test\n\n<!-- settled-through: {value} -->\n")

    def draft(self, text="**Michael:** Shu?\n"):
        folder = self.root / "chapters/001"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "arabizi.md").write_text("# Safar\n\n## 001-S01 — El bayt\n\n" + text)
        self.update(status="arabizi_review", story_dates=["2027-01-31"], locations=["Los Angeles"])
        return folder

    def reviewed(self):
        folder = self.draft()
        source_hash = story.digest(folder / "arabizi.md")
        report = (f"<!-- original-sha256: {source_hash} -->\n"
                  "<!-- original-disposition: pass -->\n"
                  "## Scope\nFixture reviewed.\n## Findings\nNone.\n"
                  "## Resolution\nNo changes.\n## New provisional facts\nNone.\n")
        (folder / "review.md").write_text(report)
        self.update(status="ready_for_author", reviewed_original_sha256=source_hash)
        return folder

    def settle(self, status="provisionally_accepted"):
        folder = self.reviewed()
        data = story.registry(self.root)
        evidence = {"author_acceptance": EVIDENCE} if status == "accepted" else {"provisional_acceptance": EVIDENCE}
        data["chapters"][0].update(status=status, memory_updated=True, **evidence)
        data["last_settled_chapter"] = "001"
        data["last_accepted_chapter"] = "001" if status == "accepted" else None
        data["chapters"][1].update(status="brief_ready", based_on_accepted_chapter="001")
        self.write(data)
        self.markers("001")
        return folder

    def errors(self):
        return story.check(self.root)

    def assert_error(self, phrase):
        self.assertTrue(any(phrase in error for error in self.errors()), self.errors())

    def test_initial_setup_is_valid(self):
        self.assertEqual(self.errors(), [])

    def test_first_writer_packet_has_current_sources(self):
        packet = story.packet(self.root, "001", "writer")
        self.assertIn("planning/briefs/001.md", packet)
        self.assertIn("development/LEXICON.tsv", packet)
        self.assertIn("sha256=", packet)

    def test_future_writer_is_refused(self):
        with self.assertRaisesRegex(ValueError, "settled|ready brief"):
            story.packet(self.root, "002", "writer")

    def test_stale_dependency_is_detected(self):
        self.update(1, status="brief_ready")
        self.assert_error("preceding chapter is not settled")

    def test_original_change_invalidates_review(self):
        folder = self.reviewed()
        self.assertEqual(self.errors(), [])
        with (folder / "arabizi.md").open("a") as handle:
            handle.write("\n**Michael:** La2.\n")
        self.assert_error("original review is stale")

    def test_english_manuscript_is_flagged_without_deleting_it(self):
        folder = self.reviewed()
        path = folder / "english.md"
        path.write_text("Unexpected English edition.\n")
        self.assert_error("English edition is disabled")
        self.assertTrue(path.exists())

    def test_acceptance_cannot_be_inferred_from_reviews(self):
        self.reviewed()
        self.update(status="accepted", memory_updated=True)
        self.assert_error("actual author acceptance evidence")

    def test_accepted_revision_unblocks_refreshed_next_brief(self):
        self.settle("accepted")
        self.assertEqual(self.errors(), [])
        packet = story.packet(self.root, "002", "writer")
        self.assertIn("chapters/001/arabizi.md", packet)
        self.assertNotIn("chapters/001/english.md", packet)

    def test_provisional_acceptance_unblocks_next_writer(self):
        self.settle()
        self.assertEqual(self.errors(), [])
        self.assertIn("chapters/001/arabizi.md", story.packet(self.root, "002", "writer"))

    def test_provisional_acceptance_needs_evidence(self):
        self.settle()
        self.update(provisional_acceptance=None)
        self.assert_error("provisional acceptance needs")

    def test_provisional_cannot_claim_author_acceptance_field(self):
        self.settle()
        self.update(author_acceptance=EVIDENCE)
        self.assert_error("only an accepted chapter may record author acceptance")

    def test_last_accepted_must_exclude_provisional(self):
        self.settle()
        data = story.registry(self.root)
        data["last_accepted_chapter"] = "001"
        self.write(data)
        self.assert_error("last_accepted_chapter disagrees")

    def test_revision_batch_allows_successor_review(self):
        self.reviewed()
        self.update(acceptance_history=[{"status": "accepted", "sha256": "old"}])
        self.update(1, status="brief_ready", based_on_accepted_chapter="001")
        self.assertEqual(self.errors(), [])
        with self.assertRaisesRegex(ValueError, "settled"):
            story.packet(self.root, "002", "writer")

    def test_original_revision_packet_contains_only_arabizi(self):
        self.reviewed()
        self.update(status="revision_needed")
        packet = story.packet(self.root, "001", "writer")
        self.assertIn("review.md", packet)
        self.assertNotIn("english.md", packet)

    def test_state_cannot_claim_unsettled_progress(self):
        path = self.root / "memory/CURRENT_STATE.md"
        path.write_text(path.read_text().replace("settled-through: none", "settled-through: 001"))
        self.assert_error("Settled-through marker is stale")

    def test_excluded_name_and_diacritic_variant_detected(self):
        folder = self.draft()
        banned = story.excluded_names(self.root)[0]
        marked = banned[0] + "\u0301" + banned[1:]
        with (folder / "arabizi.md").open("a") as handle:
            handle.write("\n" + marked + "\n")
        self.assert_error("excluded personal name")

    def test_arabic_script_leakage_detected(self):
        folder = self.draft()
        with (folder / "arabizi.md").open("a") as handle:
            handle.write("\n\u0627\n")
        self.assert_error("Arabic-script leakage")

    def test_lexicon_drift_detected(self):
        self.draft("**Michael:** Lama wselt, kont ta3ban.\n")
        self.assert_error("spelling drift")
        self.assertIn("lama→lamma ×1", story.stats(self.root, "001"))

    def test_lexicon_ignores_preferred_forms(self):
        self.draft("**Michael:** Lamma wselt, kent ta3ban, inshalla.\n")
        self.assertEqual(self.errors(), [])

    def test_age_nineteen_is_not_eligible(self):
        self.draft()
        self.update(contains_romance_or_flirting=True,
                    romantic_participants=[{"name": "Example", "age": 19, "scene": "001-S01"}])
        self.assert_error("age 20+")
        self.assert_error("no pre-Barcelona")

    def test_future_dates_rejected(self):
        self.draft()
        self.update(story_dates=["2028-01-01"])
        self.assert_error("outside 2027")

    def test_ready_status_requires_actual_passing_review(self):
        folder = self.reviewed()
        path = folder / "review.md"
        path.write_text(path.read_text().replace("original-disposition: pass", "original-disposition: pending"))
        self.assert_error("does not pass the current original")

    def test_obsolete_translation_fields_rejected(self):
        self.reviewed()
        self.update(translated_from_original_sha256=None)
        self.assert_error("obsolete translation fields")

    def test_unsettled_coverage_rejected(self):
        with (self.root / "memory/COVERAGE.tsv").open("a") as handle:
            handle.write("001\t001-S01\tcoffee\tMichael\tcasual\tDamascene\tfixture\tfixture\n")
        self.assert_error("unsettled chapter")

    def test_coverage_must_cite_reviewed_hash(self):
        folder = self.settle()
        source_hash = story.digest(folder / "arabizi.md")
        with (self.root / "memory/COVERAGE.tsv").open("a") as handle:
            handle.write("001\t001-S01\tcoffee\tMichael\tcasual\tDamascene\tfixture\tstale\n")
        self.assert_error("stale source revision")
        coverage = self.root / "memory/COVERAGE.tsv"
        coverage.write_text(coverage.read_text().replace("\tstale\n", f"\t{source_hash}\n"))
        self.assertEqual(self.errors(), [])

    def test_translator_role_is_disabled(self):
        self.reviewed()
        with self.assertRaisesRegex(ValueError, "Arabizi only"):
            story.packet(self.root, "001", "translator")

    def test_no_packet_claims_review_before_original_exists(self):
        with self.assertRaisesRegex(ValueError, "actual original draft"):
            story.packet(self.root, "001", "language_reviewer")

    def test_planner_may_open_only_next_unregistered_chapter(self):
        self.settle()
        data = story.registry(self.root)
        data["chapters"] = data["chapters"][:1]
        self.write(data)
        self.assertIn("Chapter 002: planner", story.packet(self.root, "002", "planner"))
        with self.assertRaisesRegex(ValueError, "not registered"):
            story.packet(self.root, "003", "planner")

    def test_archivist_requires_passed_review(self):
        self.draft()
        with self.assertRaisesRegex(ValueError, "passed review"):
            story.packet(self.root, "001", "archivist")
        self.reviewed()
        self.assertIn("memory/STORY_LEDGER.md", story.packet(self.root, "001", "archivist"))


if __name__ == "__main__":
    unittest.main()

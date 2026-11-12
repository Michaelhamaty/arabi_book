# Novel development workspace

A dialogue-driven Levantine Arabizi novel, **Bayn Balad w Balad** (working
title): Michael's 2027 in Barcelona, Lebanon, and Barcelona again. The
foundation is [STORY_MASTER.md](STORY_MASTER.md); live progress is in
`memory/CHAPTERS.json`.

## Start here

1. Read `AGENTS.md`, the master, and `memory/CURRENT_STATE.md`.
2. Read `development/LANGUAGE_CALIBRATION.md`: spelling table, voice cards,
   texture palette, and noncanonical samples. `development/LEXICON.tsv` lists
   spelling drift the checker rejects.
   Read `development/EDITORIAL_DIRECTION.md` for what has worked, what must not
   repeat, and the lessons of the 2026-11-11 audit.
3. Read `planning/ROADMAP.md` for the book's shape (about 36 chapters, ending
   New Year's Eve 2027) and the next few chapter nodes.
4. For a long run, follow `prompts/OVERNIGHT.md`.

## Method

**Planner → writer → language reviewer → story reviewer → archivist
(provisional acceptance) → the user's morning ratification.** Each role is a
fresh agent with its own prompt in `prompts/` and a reading packet from
`story.py`. The user wants **no English version**; editorial notes may be English.

The standard since 2026-11-10 (C007): rich, natural texture; distinct
Damascene and Lebanese voices; a pace where every chapter changes something.
Chapters are usually 1,800–3,000 words in one to three scenes.

Every spoken passage begins with `**Name:**`, including when speech resumes
after narration; written messages are attributed blockquotes. When requested,
settled chapters are assembled into a combined manuscript and printable PDF
with the labels kept and editorial metadata removed.

The GitHub repository is `https://github.com/Michaelhamaty/arabi_book.git`.
The original working branch is `codex/book-development`; sessions may work on
their own assigned branch. Commit and push after each increment.

## Files

| Record | Purpose |
| --- | --- |
| `STORY_MASTER.md` | User facts, cast, arcs, language principles, adopted defaults. |
| `development/LANGUAGE_CALIBRATION.md` | Spelling, voice cards, texture palette, samples. |
| `development/LEXICON.tsv` | Rejected spelling variants and preferred forms. |
| `development/EDITORIAL_DIRECTION.md` | What works (001–004 evidence), repetition rules, audit lessons (C010). |
| `planning/ROADMAP.md` | Book shape and future nodes; not evidence of events. |
| `planning/briefs/NNN.md` | One brief per chapter, written by the planner. |
| `memory/CHAPTERS.json` | Status, dependency, review hashes, acceptance evidence. |
| `memory/CURRENT_STATE.md` | Present snapshot of the settled story. |
| `memory/STORY_LEDGER.md` | Per-chapter summaries, commitments, retrievable details. |
| `memory/DECISIONS.md` | Provenance of user decisions and editorial defaults. |
| `memory/COVERAGE.tsv` | Situations and registers already used, per settled scene. |
| `prompts/` | Role prompts, the overnight runbook, and the ratification procedure. |
| `reports/` | Run reports, audits (`2026-11-11-project-audit.md`), and `RUN_STATE.md`. |
| `scripts/story.py` | Read-only checks, packets, stats, hashes. |
| `reports/RUN_STATE.md` | Resume point for an active long run. |
| `.cursor/hooks.json` | Cursor-only stop hook: blocks ending an active run with unsaved work. |

## Commands

```sh
python3 scripts/story.py check
python3 scripts/story.py packet 004 --role planner     # also writer, language_reviewer, story_reviewer, archivist
python3 scripts/story.py stats 003                     # words, speakers, repeated narration words, drift, variant pairs
python3 scripts/story.py hash chapters/003/arabizi.md
python3 -m unittest discover -s tests -v
```

Packets refuse to print when checks fail or when the role's preconditions are
not met (for example, a writer whose predecessor is not settled).

## Statuses

| Status | Meaning |
| --- | --- |
| `planned` | Listed in the registry; no immediate brief yet. |
| `brief_ready` | Brief written from settled state; no manuscript. |
| `drafting` | Writer at work. |
| `arabizi_review` | Draft and metadata ready for the language and story reviewers. |
| `revision_needed` | Story reviewer sent it back with findings. |
| `ready_for_author` | Passed both reviews; current hash recorded with pass markers. |
| `provisionally_accepted` | Settled by the archivist under the user's standing instruction (C007); memory updated; awaiting the user's ratification. |
| `accepted` | The user's own words accepted this exact revision. |

**Settled** means `provisionally_accepted` or `accepted`. Settled chapters form
a prefix of the registry, and author-accepted chapters come first within it.
Memory contains settled chapters only, and both memory Markdown files carry a
`<!-- settled-through: NNN -->` marker matching `last_settled_chapter`.
`last_accepted_chapter` counts author-ratified chapters only.

Registry fields (schema 3): `based_on_accepted_chapter` (settled predecessor
used for the brief), `story_dates` and `locations` (actual drafted values),
`contains_romance_or_flirting` and `romantic_participants` (names, ages 20+,
source scenes), `reviewed_original_sha256`, `provisional_acceptance` and
`author_acceptance` (`{source, note}` objects with real evidence),
`acceptance_history` (earlier acceptances of revised chapters), and
`memory_updated`.

Review files end with markers written only after actual review:

```text
<!-- original-sha256: ACTUAL_64_CHARACTER_HASH -->
<!-- original-disposition: pass -->
```

Any edit to a reviewed original makes the hash stale until it is reviewed
again. Never refresh hashes to hide a stale review.

## Running chapters overnight

Say, for example:

> Develop chapters 004–008 with the overnight workflow in
> `prompts/OVERNIGHT.md`. Use fresh agents for each role, commit and push each
> stage, and leave me a morning report.

In the morning, read `reports/YYYY-MM-DD.md` and the chapters, then reply
"I accept 004–008", "Revise 006: ...", or "Reject 007 because ..."
(`prompts/ACCEPTANCE.md`).

## Where things stand

Chapters 001–014 are provisionally accepted; the user trusts the pipeline and
does not ratify chapter by chapter (C013);
the registry owns status. On 2026-11-11 an audit
([`reports/2026-11-11-project-audit.md`](reports/2026-11-11-project-audit.md))
led to a rewritten Chapter 008, spelling corrections in 004–007 (new hashes),
slimmer records and a re-planned roadmap (DECISIONS C010, S015–S017, P008).
Chapters 009–014 were developed by separate fresh subagents under C011,
C012, C014, C016, C017 and C018 (P009–P014).

Last narrated moment: Sun May 2, 2027 (Pascha), about 3:05 am, on the walk
down from the borrowed Poble-sec church toward the Paral·lel metro. Michael
broke his fast at Abouna Elias's car boot on the pavement and is counted in
for next Sunday (the clock, the candle box with his name). Rami came unasked
from his first full-time grill night, called him `ya 7mar` again and owned
the other half of the loaves; Em Nicola has his arm. Yara's Beirut contract
needs an answer before May 15; `B7ebbik` is still unreturned. See
`memory/CURRENT_STATE.md`.

The user does not ratify chapter by chapter and trusts the pipeline (C013):
settled chapters stay `provisionally_accepted`. Michael studies data
engineering and computer science at UAB; he is Orthodox (Pascha 2027 is
Sun May 2; Great Lent from Mon Mar 15; S018).

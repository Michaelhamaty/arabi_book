# Novel development workspace

The foundation is in [STORY_MASTER.md](STORY_MASTER.md). The project now has a
working development process, a language baseline, an opening roadmap, and three
chapter briefs. Current chapter progress and acceptance are recorded in
`memory/CHAPTERS.json`; use that live record rather than assumptions in older handoffs.

## Start here

1. Read `AGENTS.md`, the master, and `memory/CURRENT_STATE.md`.
2. Read master Section 15 for the adopted editorial defaults and remaining
   research questions. User-confirmed facts remain distinct from working fiction.
3. Read `development/LANGUAGE_CALIBRATION.md`: spelling rules, voice notes, and
   short noncanonical Arabizi sample exchanges.
4. Choose the next requested operation. Do not write chapters merely because
   their briefs exist.

## Method

**Brief → direct Arabizi draft → fresh language/story review → targeted revision
→ author acceptance of the Arabizi → memory update.**

The user wants **no English version**. No translation stage or English companion
is part of production. Editorial instructions can remain in English.

Use GPT-6.1 Sol Extra High for the initial writing/review cycle if available, in
separate sessions with the same reference files. A chapter is the normal unit;
long chapters can be composed by scene within one writing context. There is no
fixed total length or chapter count. Detailed planning rolls forward only a few
chapters at a time.

The user prefers shorter chapters, usually one or two substantial scenes.
The three existing briefs cover only the opening; new briefs are added as the
story advances. Chapter 001's brief snapshots still form one compact departure.
See master Section 6 for a nonbinding illustration of overall scale.

Every spoken passage in the Arabizi must begin with `**Name:**`, including
when speech resumes after narration. Keep individual chapter Markdown sources;
when requested, assemble accepted chapters in order into a combined manuscript
and a printable PDF with contents and page numbers. Preserve the speaker labels
and omit all editorial metadata from the reader's book.

The GitHub repository is `https://github.com/Michaelhamaty/arabi_book.git`. The
user requests a commit and push after each completed increment; see `AGENTS.md`.

## Files with distinct responsibilities

| Record | Purpose |
| --- | --- |
| `STORY_MASTER.md` | Single foundation: user facts, cast, arcs, language principles, architecture, adopted setup defaults. |
| `development/LANGUAGE_CALIBRATION.md` | Spelling contract, voice calibration, noncanonical samples and uncertainty notes. |
| `planning/ROADMAP.md` | Flexible future movements; not evidence of events. |
| `planning/briefs/001.md`–`003.md` | Opening scene purposes, dates, characters, and constraints. |
| `memory/CHAPTERS.json` | Chapter status, dependency, revision hashes, and acceptance evidence. |
| `memory/CURRENT_STATE.md` | Current accepted story state; no speculative developments. |
| `memory/STORY_LEDGER.md` | Chronology and memorable details from accepted chapters. |
| `memory/DECISIONS.md` | Provenance of confirmed choices and delegated editorial defaults. |
| `memory/COVERAGE.tsv` | Conversational exposure actually present in accepted chapters. |
| `prompts/` | Launch instructions for fresh writing, review, and acceptance work. |
| `scripts/story.py` | Read-only structural checking, content hashes, and context-packet reading lists. |

`chapters/NNN/` is created when drafting begins. It contains `arabizi.md` and `review.md`. No blank manuscript or book/export directories
are created in advance. Typesetting, page numbers, and contents generation follow
accepted manuscript material.

## Commands

From the workspace root:

```sh
python3 scripts/story.py check
python3 scripts/story.py packet 001 --role writer
python3 scripts/story.py packet 001 --role reviewer
python3 scripts/story.py hash chapters/001/arabizi.md
python3 -m unittest discover -s tests -v
```

The packet command prints a role instruction and an ordered list of files with
current hashes. It does not copy the master into a second source of truth. The
agent must read those files. Writer packets for future chapters are refused until
the preceding chapter is accepted and the brief's dependency has been refreshed.

## Chapter registry and status

`memory/CHAPTERS.json` is edited deliberately by the responsible agent. The script
does not change statuses or manufacture approvals.

| Status | Required material |
| --- | --- |
| `planned` | An outline/brief, subject to earlier chapters. No manuscript yet. |
| `brief_ready` | Immediate brief prepared; no manuscript yet. |
| `drafting` | Arabizi original in progress. |
| `arabizi_review` | Original and scene/date metadata ready for review. |
| `revision_needed` | Original exists; specific findings require changes. |
| `ready_for_author` | Arabizi passed review; current original hash and substantive report. No English required. |
| `accepted` | Same revision checks, actual user acceptance evidence, and updated memory. |

Schema version **2** is Arabizi-only; the retired `translation` status and its
hash fields are removed. A passing original goes directly to `ready_for_author`.

The registry stores:

- `based_on_accepted_chapter`: last accepted chapter used for the brief/draft;
  `null` for Chapter 001.
- `story_dates` and `locations`: **actual drafted** dates/locations; empty during
  initial planning. Planned dates live in the brief.
- `contains_romance_or_flirting`: reviewer-confirmed boolean before review stages.
- `romantic_participants`: names, ages at interaction, and source scenes when
  that boolean is true. The age metadata supports human reading; it cannot prove
  no undeclared flirtation occurs.
- `reviewed_original_sha256`: source revision that passed original-language review.
- `author_acceptance`: `null` until accepted; then an object with a specific
  `source` (the actual user instruction) and `note` identifying the accepted revision.
- `memory_updated`: true only after the corresponding state, ledger, and coverage
  updates are complete.

Both memory Markdown records contain an `accepted-through` comment that must
match `last_accepted_chapter`. Acceptance must be a contiguous prefix of the
registry. Do not update accepted chapter text without recording the revision and
rechecking everything it affects.

The review file uses these markers, filled only after actual review:

```text
<!-- original-sha256: ACTUAL_64_CHARACTER_HASH -->
<!-- original-disposition: pass -->
```

There are no English/translation markers. Keep the substantive
findings and their resolution in the report; markers alone are not a review.
Review prompts specify the report sections.

## Ready now, and deliberately left open

Chapter 001's departure brief is ready. Close third-person Arabizi narration,
fictional farewell friends, and the first Barcelona housing arrangement are
adopted editorial defaults, all reversible before acceptance. `8 = gh`, `q = q`,
and `2 = glottal stop` are user-confirmed.

Michael's UAB subject is awaiting input. That does not block the departure
chapter. Avoid course titles, department claims, and official calendar dates in
Chapter 003 until supplied or verified. Church denomination, exact addresses,
future 2027 public events, and later romantic outcomes are not setup blockers.

To start the next writing session, use:

> Read AGENTS.md. Run `python3 scripts/story.py packet 001 --role writer` and read
> every input it lists. Draft Chapter 001 in original Arabizi following its brief.
> Stop after the original draft and a concise handoff for fresh review; do not
> create any English version, accept, or promote draft events into memory yet.

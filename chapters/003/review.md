# Chapter 003 — Writer handoff for fresh review

**Not independently reviewed. Writer self-edit only.** No fresh editorial or
native-speaker review has occurred. This report does not pass the original.

## Scope

- Chapter: **003 — Barra el beit**; two scenes, **1,249** whitespace-delimited
  words including headings and speaker labels.
- Writer source SHA-256:
  `396c954b09ea6d44d245f7722aae1900d64308e2cc23fecb2aeb1ec96d788728`.
  This identifies the handed-off draft, not a reviewed revision.
- Stage: **arabizi_review**. `reviewed_original_sha256` and
  `author_acceptance` remain null; `memory_updated` remains false.
- Predecessor: accepted **002**, SHA-256
  `2766f274fbfde210b836380ba82fe10bad53f53abe455f70e12a6795b2dcd210`.
  The user's actual acceptance was recorded before preparing this brief/draft.
  Accepted 001 remains at
  `1bf32f1fb8ea4df2ab289bab2d32ea6500bbc1abc967bc242de6125f93f59407`.
- Read every input in `python3 scripts/story.py packet 003 --role writer`:
  AGENTS.md, prompts/WRITER.md, STORY_MASTER.md,
  development/LANGUAGE_CALIBRATION.md, memory/CHAPTERS.json,
  memory/CURRENT_STATE.md, planning/briefs/003.md, and both accepted originals
  001–002. Also read README.md, memory/STORY_LEDGER.md, memory/DECISIONS.md,
  memory/COVERAGE.tsv, prompts/ACCEPTANCE.md, prompts/REVIEWER.md, and 002's
  actual passing report. The full source was reread after the final self-edits.
- Actual scenes: **003-S01**, February 1, 2027, evening, Michael's Barcelona
  room; **003-S02**, February 2, 2027, morning, unnamed neighborhood streets
  and the fictional café **3al Zawiye**. No named real geography or official
  university particulars are used.

## Findings — writer self-edit, not fresh review

| Scope | Change made during self-edit | Reason |
| --- | --- | --- |
| 003-S01, Michael's arrival account | Used “hiye kanet 3am teshta8el” for Inés's earlier activity; removed an unnecessary reference to a car. | Report the witnessed arrival, without asserting her current progress or supplying an unneeded transport detail. |
| 003-S01, phone viewpoint | Replaced unseen eating/phone movements with the heard plate and Zeina's more distant voice. | Keep narration within Michael's perception. |
| 003-S02, initial order | Removed a repeated coffee-count question and its corrective joke. | Let ordinary service breathe; avoid making every stranger exchange another correction of Michael. |
| 003-S02, café ambition | Replaced a dismissive instruction to finish eating with reciprocal teasing about coffee. | Give Michael room to answer Walid; avoid a proprietor who only teaches lessons. |
| 003-S02, machinery interruption | Simplified the steam wording and removed an unexplained incoming call and an explicit explanation that Michael would not solve the problem. | Show Walid's competing attention through action; let the absence of an offer stand without a moral. |
| Whole original | Corrected a script typo, aligned “finjan” spelling with the earlier narrative, and clarified a service verb. | Preserve the adopted notation and readable rhythm. |

All **93 live spoken passages** have speaker labels: Michael **48**, Zeina
**23**, Walid **22**. Attribution was checked by reading, not by alternating
names. There are no written-message blocks in this chapter. Hassan's completed
call is narrated in summary, with no quotation or invented dialogue assigned to him.

## Resolution and questions for the fresh reviewer

The writer has completed a full self-edit. No passing review markers are present.
Use `prompts/REVIEWER.md` and run
`python3 scripts/story.py packet 003 --role reviewer` in a fresh context.

1. **Language/voice:** check Walid's compressed replies, especially
   “Iza ma3zoum, beshrab w beskot”, “Bte3mela hek ktir?” in Michael's question
   about the machine, and the short farewell “W nharak”. The intended effect is
   ordinary dry Lebanese service banter, not a claim that any phrase is a
   verified regional idiom. Preserve the give-and-take; make targeted changes
   where the actual wording does not carry it naturally.
2. **Pacing and repetition:** assess the two quiet scenes, the brief clothes
   callback, the pauses on the phone, and the café interruption. They should
   feel like a particular evening/morning rather than a series of settling-in
   lessons. The key action is deliberately brief. Do not expand the chapter
   merely to include Karim or the unused campus outline.
3. **Continuity and viewpoint:** check 001-S03/S05 and 002-S01/S02 directly.
   Both parental conversations are **new draft events after rest**: Hassan's
   completed call is explicitly narrated, and Zeina's is enacted. Neither is
   inferred from an arrival message. Check the first café meeting and limit
   machine claims to what is observed or Walid says.

No native speaker or external dialect authority has validated the language.
The absence of a structural error cannot resolve these editorial questions.

## New provisional facts

**Draft evidence only. None of the following has entered accepted memory.**

| Source | Proposed future state/ledger material only if accepted |
| --- | --- |
| 003-S01 | Michael sleeps after 002, wakes in the evening, showers, opens his luggage, and hangs some clothes. He completes a call with Hassan before calling Zeina. The contents of the Hassan conversation are not supplied. |
| 003-S01 | Michael and Zeina have an actual reciprocal phone conversation. He names Rami/Inés and describes arrival help, food, and his first uncertainty in the shared space. She describes an ordinary morning and possible errands. No substantive family biography or new residence fact is added. Their conversation continues as the scene ends; no daily-call schedule is created. |
| 003-S02 | Michael tests the building key while holding the entrance open, then goes out alone. This is a new test, not a claim that 002 tested that key. It does not depict closed-door re-entry. |
| 003-S02 | First visit to **3al Zawiye** and first meeting with **Walid, 47**. The café is a few minutes' walk from the flat according to Michael. He orders coffee with milk and toast with labne/oil, and says he also likes black coffee; this is not an established recurring order. |
| 003-S02 | Michael mentions a possible café of his own someday. They exchange jokes and eventually names. No job, business agreement, private financial disclosure, invitation, regular status, or promise to return is established. |
| 003-S02 | The machine makes a noise; Walid says steam is unavailable while coffee remains possible. He searches a paper for a number. No fault diagnosis, repair call, completed repair, or identified repairer is established. Michael pays and leaves, recognizes the direction home, then continues walking the other way. No next destination is specified. |

Sami's software delivery/tester update and conditional first-week test remain
unestablished; no formal role or payment is added (001-S01). Fares's game/result
and conditional news remain unestablished (001-S02). Inés's photo selection,
submission, client outcome, and the table/food requests are not resolved
(002-S02). Rami's later shifts/return are not supplied. No Karim or wider cast
introduction, UAB subject/course/calendar assertion, or romance/flirting appears.
The false romance flag is the writer's assessment awaiting fresh confirmation.

## Disposition

**Awaiting fresh original-language/story review — arabizi_review.**
No pass, independent review, native validation, or author acceptance is claimed.
Accepted originals 001–002 are unchanged. Accepted state, ledger, coverage, and
foundation facts stop at 002; only production-status notes mention draft 003.
No Chapter 004 or English version was created.

Validation: `python3 scripts/story.py check` passed with **two accepted chapters**;
the Chapter 003 reviewer packet generated successfully; all **19** existing
unit tests passed; `git diff --check` passed. Both accepted source hashes were
verified unchanged. These checks establish structural consistency, not a fresh
language/story review.

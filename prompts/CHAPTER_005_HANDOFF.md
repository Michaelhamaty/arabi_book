# Chapter 005 — coordinator handoff

Work in `/Users/michaelhamaty/Developer/arabic_story_dev`. Develop **Chapter 005
only**, from fresh planning through writing, separate reviews, and provisional
settlement under the standing C007 authorization. Do not continue to 006 or
claim the user personally accepted these revisions.

## Read before launching work

Read `AGENTS.md`, `README.md`, `STORY_MASTER.md`,
`development/EDITORIAL_DIRECTION.md`, `development/LANGUAGE_CALIBRATION.md`,
`development/LEXICON.tsv`, `memory/CHAPTERS.json`, `memory/CURRENT_STATE.md`,
`memory/STORY_LEDGER.md`, `memory/DECISIONS.md`, `planning/ROADMAP.md`,
`prompts/OVERNIGHT.md`, and `reports/RUN_STATE.md`.

Read current Chapters 003–004 and the 004 brief/review in full. The saved editorial
direction contains the comparison of revised 001–003 with their earlier versions;
retrieve older source scenes if a callback depends on their exact wording.

Inspect live files, Git status, branch, and remote first. At preparation, the
branch is `codex/book-development`, settled through 004; all four revised chapters
are provisionally accepted, awaiting ratification. **There is no Chapter 005 brief
or manuscript yet.** The previous run's planner launch failed on a usage limit.
Do not assume this remains current or overwrite work that subsequently appeared.

Run:

```sh
python3 scripts/story.py check
python3 -m unittest discover -s tests -v
python3 scripts/story.py packet 005 --role planner
```

## Editorial direction the user wants preserved

The recent revisions established stronger living vocabulary, genuinely different
voices, situational profanity, and consequences rather than cautious logistics.
The user expressly wants that direction to continue.

- Texture must do social work: affection, sarcasm, irritation, blessing, refusal,
  embarrassment, flirtation, or pressure. No phrase parade, copied sample exchanges,
  slang quota, or requirement that everybody swear.
- Preserve distinct voices, especially Damascene Michael/Rami versus Lebanese
  Walid/Yara and economical Inés. Karim has his own Palestinian-Jordanian profile;
  do not make him a second Jordi, Abu Nabil, or Michael.
- **No conversation reruns.** Check proposed exchanges against 003–004 and the
  coverage tracker. A callback requires new information, stakes, consequence, or
  relationship movement. Don't repeat the café dream/manual offer, dice loss,
  lateness interrogation, nostalgia argument, or the same flirtation/name-bet terms.
- Use meaningful physical detail, not repeated cup/phone/plate choreography.
- Spelling follows calibration and lexicon. Search established forms before adding
  variants; preserve legitimate dialect differences. The checker catches listed
  tokens, not every semantic or phonetic error.
- Arabizi original only, close third-person on Michael; `**Name:**` on every spoken
  passage, repeated after narration. Messages are attributed blockquotes. No Arabic
  script or English version. All nationalities speak Arabic in-world.
- Preserve all master boundaries: 2027, real-family facts, separate parental homes,
  excluded names, and romance/flirting participants age 20+.

The editorial note records concrete before/after evidence and remaining review
uncertainties. Use its principles, not the exact jokes as reusable dialogue.

## Continuity the planner must resolve

- Last scene: Fri Feb 5, shortly before midnight, Camille's flat. No walk home is
  narrated. Use a short transition/time jump if stronger than continuing the dinner.
- **Sami's build arrived Feb 5.** Michael promised to test it `bokra` (Sat Feb 6).
  If jumping to Feb 8 or later, establish whether he tested, postponed, or partly
  attempted it. Don't assume an unshown day means a failure or a completed task.
- Yara refused her number. Their bet is undated and unresolved: whoever Walid
  calls by name first wins; the loser pays and concedes `ma3ak 7a2` in front of him.
  No date, number, exclusivity, or physical relationship is established.
- Walid was told Michael's name at the Feb 2 introduction, but has not used it
  on-page. Michael doesn't know whether he remembers it. Abu Nabil calls him Mars.
- Inés's `akid` point was made once; let consequences/behavior carry it rather
  than another speech about saying yes. Her client still has not paid.
- Jordi's Tue Feb 9 class is an invitation Michael has not accepted. Abu Nabil's
  Fri Feb 12 invitation went unanswered. Andrew has Rami's number and a two-day
  contact rule; no family alarm is established. Keep actual knowledge attributed.
- Working 005 direction: generic early UAB life and **Karim, 24**, in a plausible
  shared train/campus circumstance. Keep the chapter focused; one or two substantial
  scenes can suffice. No named program, professor, official calendar, or legal
  travel/work assertion is invented. The user's program remains unspecified.
- Do not resolve the café machine or identify the tomorrow-man as Marwan.

Refresh the roadmap only where the actual preceding chapter warrants it. Its 005
node is a plan; exact dialogue and outcomes remain the new writer's creative work.
Require a clear end-of-chapter change without scheduling every thread into 005.

## Fresh-role pipeline and checkpoints

Act as coordinator, not the prose writer or reviewer. Use the runtime's actual
available delegation interface; do not assume a tool from another host exists.
Each role is a fresh context with the workspace, chapter ID, role prompt, packet
command, and requirement to read the files itself:

1. **Planner:** `prompts/PLANNER.md`, `packet 005 --role planner`. Read the saved
   editorial direction. Create `planning/briefs/005.md`, register 005 with predecessor
   `004`, and set `brief_ready`. Include a repetition comparison and what changes.
2. **Writer:** `prompts/WRITER.md`, `packet 005 --role writer`. Compose the actual
   `chapters/005/arabizi.md`; write a handoff in `review.md`; fill metadata and set
   `arabizi_review`. Self-editing is not a fresh review.
3. **Language reviewer:** `prompts/LANGUAGE_REVIEWER.md`, corresponding packet.
   Make specific corrections, preserve texture, and document uncertain expressions.
4. **Story reviewer:** `prompts/STORY_REVIEWER.md`, corresponding packet. Check
   the full new text against 003–004, not just the brief. Verify attribution, dates,
   knowledge, novelty, and consequences. Pass the actual final hash only after
   reading it, or return `revision_needed`. Follow the runbook's two-loop cap.
5. **Archivist:** `prompts/ARCHIVIST.md`, corresponding packet, only after both
   reviews pass. Read the source, provisionally settle it under C007, and update
   registry/state/ledger/coverage/durable facts together. Never mark author acceptance.

Run `python3 scripts/story.py stats 005` after drafting and revision, and
`python3 scripts/story.py check` after each stage. Run the unit tests at the
specified checkpoints. Commit and push each completed stage to the tracked GitHub
branch and update `reports/RUN_STATE.md` with the exact next step.

Honor the runbook's previously authorized model fallback **only if the current
runtime actually offers it**, recording the model and required follow-up review.
Never claim an unavailable model/agent ran or bypass a usage limit. If the needed
stage cannot run, preserve completed work, checkpoint the limitation, and stop.

At completion, write the run report with what changed, new promises, hashes,
reviewer fixes, uncertainties, tests, models, and GitHub sync outcome. Stop after
005; the earlier 004–005 range does not authorize 006 here. In the final response,
link the chapter/report and distinguish provisional settlement from user acceptance.

**Do not edit settled Chapters 001–004 during this assignment.** Source spellings
or uncertain idioms flagged in the editorial note are review questions, not
permission to rewrite prior chapters or silently refresh their hashes.

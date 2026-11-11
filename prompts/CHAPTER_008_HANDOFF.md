# Chapter 008 — coordinator handoff

Work in `/Users/michaelhamaty/Developer/arabic_story_dev`. Develop **008 only**
through fresh planning, writing, language review, story review, and provisional
archival settlement under C007. Stop before 009. Do not claim author acceptance.

## Verify the predecessor before starting

Read `AGENTS.md`, `README.md`, `STORY_MASTER.md`, `memory/CURRENT_STATE.md`,
`memory/CHAPTERS.json`, `memory/STORY_LEDGER.md`, `memory/DECISIONS.md`,
`memory/COVERAGE.tsv`, `development/EDITORIAL_DIRECTION.md`,
`development/LANGUAGE_CALIBRATION.md`, `development/LEXICON.tsv`,
`planning/ROADMAP.md`, `prompts/OVERNIGHT.md`, and `reports/RUN_STATE.md`.
Read actual Chapters 006–007, their briefs/reviews, and the completed 007 report
if available. Retrieve 001's Maya/family scenes, 002's Rami scenes, and relevant
005 testing passages before planning callbacks.

Inspect Git status, branch, and remote, and check for an active 007 coordinator.
At handoff preparation, the local branch was `codex/book-development` at
`30fb1dd`: the 007 planner was committed, but the draft/review handoff and registry
changes were still uncommitted at `arabizi_review`. Memory was settled through
006. The user reports 007 done; the files may catch up after this preparation.
**Do not assume reviews or settlement from the user's completion report.**
Do not ratify 007 on their behalf or copy draft events into settled memory.

Run `python3 scripts/story.py check` and inspect the live 007 review hash,
status, memory markers, and completion evidence. Start 008 only once 007 is
actually settled and no other agent owns the active run. If still unfinished,
report the exact pending stage and wait for that coordinator to finish; don't
duplicate its reviews, commit its files, or bypass the predecessor gate.
Preserve all existing edits. If 008 artifacts already exist, resume from the
verified stage rather than overwriting them.

Once ready:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/story.py packet 008 --role planner
```

## Working direction: first bill comes due

Use the early-March roadmap: a video call with **Maya**, whose life matters
independently of Michael's, and a favor for **Rami** collide with the first
Nadine-related deadline. Michael lets someone down in a small, concrete way
and must own the consequence. Choose the actual collision, failure, and response
from the final settled 007 text. Don't predeclare which promise he breaks.
One or two substantial scenes usually suffice; don't pad for a word target.

The draft inspected during preparation contained these **unsettled** commitments.
Recheck every detail against the final reviewed 007; revisions supersede this list:

- Feb 24 afternoon introduction at 3al Zawiye. Nadine returns Walid's tray;
  her company makes workflow programs. Michael volunteers the café before
  asking. Walid refuses a pilot; both Nadine and Michael acknowledge the refusal.
- **Mon Mar 1, 16:00, twenty minutes at the café:** Walid describes one order,
  on the customer side of the bar. He may leave for service. No customer
  names/numbers, recording, extra participant, book access, staff interviews,
  software deployment, or observation permission is granted.
- **Tue Mar 2 before 18:00:** Michael promises the same one-page account to
  both: a copy brought to Walid at the café and an email to Nadine's saved,
  corrected professional address. Beginning-to-end description and at most
  three unanswered questions; no solution/recommendation or owner rewrite duty.
- No interview or note has happened yet in that draft. No payment, employment,
  partnership, personal number exchange, or continuing work role is agreed.

If these survive settlement, show or clearly establish the March 1 conversation
before using its contents in the note. Don't silently assume it occurred, invent
its answers as earlier history, or treat a general example from 007 as the
completed interview. Keep the two delivery obligations distinct: sending an
email doesn't deliver Walid's copy. His limited conversation permission never
becomes consent to a pilot. Any changed arrangement must occur on-page.

Maya is 23, Michael's close, laughing sister. Give her agency and an immediate
interest beyond asking about Barcelona; avoid invented substantive biography
for a real family member. Rami is a generous, profane Damascene flatmate with
kitchen shifts and his own pressures. Earn a specific favor; no earlier favor,
appointment, or knowledge of Nadine is already established. Neither needs to
deliver a lesson about Michael's character. An apology need not erase a cost.

Sami may send a short hurt message if useful, but his preliminary observation
was delivered in 005; only the independent run/full findings remain pending,
undated. Don't portray the whole test as untouched or invent a missed deadline.
Avoid packing every open thread into one chapter.

## Preserve continuity and the editorial direction

- Yara and Michael have mutual numbers and want to talk again; the name bet
  was won, conceded, and paid in 006. No agreed date, exclusivity, or physical
  romantic step was established. Check 007 for any later change.
- Karim's application was submitted, not accepted; campus coffee conditional.
  No automatic connection between his application, Sami's build, and Nadine.
- No invented family alarm, shared parental home, daily call schedule, UAB
  program/timetable, machine repair, or identity for the tomorrow-man.
- Don't repeat the Friday lateness interrogation, `akid` lecture, Yara's
  overcommitment diagnosis, café nostalgia dispute, name contest, technical
  testing exercise, or 007's consent confrontation. The new failure needs
  different stakes and concrete consequences, not another identical scolding.

Follow `development/EDITORIAL_DIRECTION.md`: living idiom, varied vocabulary,
distinct Damascene/Lebanese voices, affection, sarcasm, anger, and situational
profanity. No sanitizing, slang quotas, copied jokes, or everyone sounding alike.
Professional terms can remain natural; no vocabulary lessons. Check recurring
conversations against source text and coverage before drafting.

Compose directly in Arabizi, close third-person on Michael. Prefix every spoken
paragraph `**Name:**`, including resumed speech; attribute written messages.
No English edition or Arabic-script manuscript. All nationalities speak Arabic.
Use calibration/lexicon spellings, `8` for gh, retained `q`, glottal `2`, prefer
`ra7`; preserve legitimate dialect variation. Check grammar, meaning and staging
beyond listed spelling tokens. Keep 2027, family facts, itinerary, excluded-name
rules, and romantic participants aged 20+. Disclose uncertain usage honestly.

## Execute and synchronize

Coordinate with actual available delegation tools. Each role must be a separate
fresh context, receive its prompt and freshly generated `packet 008 --role ROLE`,
and read the sources itself. Begin a new 008 checkpoint while preserving history.

1. Planner: `prompts/PLANNER.md`; brief/registry with predecessor `007`,
   repetition comparison and meaningful change; `brief_ready`.
2. Writer: `prompts/WRITER.md`; `drafting`, then `chapters/008/arabizi.md`,
   review handoff and accurate metadata; `arabizi_review`.
3. Language reviewer: `prompts/LANGUAGE_REVIEWER.md`; preserve voice/texture
   while fixing errors; document unresolved judgments.
4. Story reviewer: `prompts/STORY_REVIEWER.md`; verify chronology, actual
   promises/delivery, permissions, knowledge, novelty, family facts, attribution,
   consequences and staging. Pass actual final SHA-256 and `ready_for_author`,
   or `revision_needed`. Follow the two-loop cap and review changed text.
5. Archivist: `prompts/ARCHIVIST.md`, after both passes; read source and reconcile
   registry, state, ledger, coverage and durable facts as `provisionally_accepted`.
   Only the user grants author acceptance.

Run stats after drafting/revision, structural checks each stage, tests at runbook
checkpoints. Commit and push each completed increment to the tracked project
branch, verifying synchronization; include only intended files. Never overwrite
concurrent edits, invent reviews/model identities, or refresh old hashes to hide
stale review. Use only available authorized fallbacks, recording follow-up needs.
If a required stage cannot run, checkpoint completed work and report the blocker.

Report source hash, reviewer fixes, actual kept/broken promises, remaining
uncertainties, models, checks and GitHub outcome. Link chapter/report and identify
provisional settlement. **Stop after 008; preserve settled Chapters 001–007.**

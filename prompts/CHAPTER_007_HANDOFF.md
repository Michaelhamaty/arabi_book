# Chapter 007 — coordinator handoff

Work in `/Users/michaelhamaty/Developer/arabic_story_dev`. Develop **Chapter 007
only**, through fresh planning, writing, separate language and story reviews,
and archival provisional settlement under C007. Stop before 008. Preserve settled
Chapters 001–006. Do not claim author acceptance.

## Start with evidence

Read `AGENTS.md`, `README.md`, `STORY_MASTER.md`, `memory/CURRENT_STATE.md`,
`memory/CHAPTERS.json`, `memory/STORY_LEDGER.md`, `memory/DECISIONS.md`,
`memory/COVERAGE.tsv`, `development/EDITORIAL_DIRECTION.md`,
`development/LANGUAGE_CALIBRATION.md`, `development/LEXICON.tsv`,
`planning/ROADMAP.md`, `prompts/OVERNIGHT.md`, and `reports/RUN_STATE.md`.
Read Chapters 005–006 and their briefs/reviews fully, the 006 completion report
`reports/2026-11-10-chapter-006.md`, and relevant café passages in 003–004.
Packets are reading lists, not substitutes for source text.

Inspect live Git status, branch, and remote. At preparation, the clean branch is
`codex/book-development` at `1f95078`, settled through 006, with zero current
author-ratified revisions. No 007 brief, manuscript, or registry entry exists.
Chapter 006's reviewed source hash is
`f92137df5527d9ccb118d93eb323ad4f5f7b0e08e78ce46e7d98720510e07c01`.
Verify the live state rather than overwriting subsequent work. The finished
006 run's stop boundary is historical; this assignment authorizes 007 only.

```sh
python3 scripts/story.py check
python3 -m unittest discover -s tests -v
python3 scripts/story.py packet 007 --role planner
```

## Direction for fresh planning

Use the late-February roadmap direction: **Nadine, 42, a Damascene entrepreneur
whose fictional company builds workflow tools for small businesses**, enters
through Walid's network. She wants a pilot café; Michael volunteers 3al Zawiye
before asking its owner and offers help with a bounded discovery task. Walid's
reaction is the turn. These are planning intentions, not established events.
Earn the introduction and the offer in a specific encounter; choose the exact
date, scope, response, and ending from the settled state.

Nadine is precise, curious, selectively warm, sometimes impatient, with her own
company pressures, colleagues, judgment, and humor. She is a professional
connection, not automatically a flirtation because she is an older woman. Avoid
a founder pitch, instant mentorship, résumé interview, or instant hiring.
Give her a concrete reason to listen and something she needs to learn. Michael
can have useful curiosity without becoming a technical expert or café savior.

The dramatic problem is **offering another person's business without consent**.
Let Walid's ownership, practical knowledge, and independent priorities matter.
Do not reduce him to comic resistance to progress, or let Nadine and Michael
treat his café as an available test site. Any permission must actually be given,
with its limits understood; an introduction is not consent to a pilot.

If a discovery task is agreed, make its concrete obligation and timing clear
enough for later follow-through. Distinguish suggestions from commitments and
leave genuinely unsettled scope/payment visibly unsettled. No assumed wages,
contract, partnership, legal work status, software deployment, access to customer
data, or guaranteed availability. A bounded conversation or observation may
precede any implementation. No real company or technical research is needed
unless the scene genuinely depends on it.

The roadmap's 008 consequences are future possibilities. Leave usable threads
without writing 008 now, predeclaring a failure, or crowding this chapter with
every open obligation. Prefer one or two substantial scenes and a meaningful
change. The usual length range is guidance; 006's complete 1,652-word scene was
deliberately retained without padding.

## Continuity and repetition guards

- Last scene ends **Tue Feb 16, 2027, morning**, at 3al Zawiye's door after Yara
  leaves. A late-February jump is available; intervening events are unestablished.
- **The name bet is finished.** Walid called Michael by name while serving;
  Michael won, Yara conceded to him before Walid, and she actually paid. No debt,
  rematch, uncertain recognition, or pending concession remains. Walid now knows
  about the bet, not necessarily the whole dinner story. Abu Nabil's knowledge
  of its outcome is unestablished.
- **Michael and Yara now have mutual numbers** and explicitly want to talk again.
  Her earlier refusal remains history, not current status. The received finger
  photograph completes contact; she says she keeps it for its light. No agreed
  date, exclusivity, physical step, recurring appointment, design service, or
  private love-token meaning is established. Yara knows his café ambition now;
  don't repeat its reveal or their breakfast conversation about quiet company.
- Walid's machine was silent in 006, last shown broken, with no repair established.
  The tomorrow-man is unidentified; do not identify him as Marwan or turn Nadine's
  business into a convenient machine fix.
- Michael already described his café dream in 003 and heard practical costs.
  Don't repeat that lesson, the manual offer, Friday's dice humiliation, nostalgia
  argument, lateness interrogation, or the same overcommitment diagnosis.
- In 005, Sami received one actual preliminary test finding, steps, two screenshots,
  and a first-route caveat. A clean independent run/full findings remain pending,
  undated; no diagnosis or repair was promised. Neither untouched nor finished.
- Karim submitted his own application-exercise answer; outcome unknown. Numbers
  exchanged, coffee conditional and undated. Do not repeat the metrics debate,
  have Michael write another person's solution, or merge Karim's application,
  Sami's build, and Nadine's company without an earned connection.
- Jordi's Feb 9 and Abu Nabil's Feb 12 invitations were not accepted promises;
  no later attendance or failure is established. Inés's client remains unpaid;
  her `akid` remark is spent. Family messages continued, Andrew replied on Feb 6,
  and no alarm is established. Rami's offstage life/knowledge remain unshown.
- UAB program/timetable remain unknown; keep campus references generic. Preserve
  all confirmed family facts, 2027 itinerary, excluded-name rules, and adult
  romance boundaries. Plans and character proposals are never manuscript history.

## Editorial standard

Follow the saved 001–003 revision comparison and 004 examples in
`development/EDITORIAL_DIRECTION.md`. Maintain distinct Damascene and Lebanese
voices, living vocabulary, affection, sarcasm, anger, and situational profanity.
Professional vocabulary belongs naturally in Nadine's speech; don't formalize
her into a textbook or make everyone joke and swear alike. Preserve quieter
intervals and independent purposes as well as conflict.

Compose directly in natural Levantine Arabizi, close third-person on Michael.
Every spoken paragraph needs `**Name:**`, including resumed speech after narration;
attribute written messages separately. No English edition or Arabic-script
manuscript. All nationalities speak Arabic in-world. Use `8` for gh, retained
`q`, glottal `2`, and prefer `ra7`; consult calibration and lexicon for spelling.
Preserve legitimate dialect variation. Check meaning, agreement, address forms,
and physical staging as well as listed tokens. No native verification is claimed.

Require a repetition comparison before drafting. Callbacks must change stakes,
information, or consequences; no copied jokes, phrase quotas, recycled work
exercise, or generic cup/phone choreography. The 006 review's uncertain idioms
are disclosed model judgments, not stock verified expressions to reuse.

## Fresh-role execution and delivery

Act as coordinator using the runtime's actual delegation interface. Start a new
007 checkpoint in `reports/RUN_STATE.md` while retaining historical evidence.
Each role gets the workspace, chapter ID, its prompt, a newly generated packet,
and instructions to read the files itself in a fresh context:

1. **Planner:** `prompts/PLANNER.md`, `packet 007 --role planner`. Create brief
   and registry entry with predecessor `006`, then `brief_ready`. Include novelty,
   chronology, consent/commitment distinctions, and the chapter's meaningful change.
2. **Writer:** `prompts/WRITER.md`, `packet 007 --role writer`. Set `drafting`,
   write `chapters/007/arabizi.md` and the review handoff, then `arabizi_review`.
3. **Language reviewer:** `prompts/LANGUAGE_REVIEWER.md`, corresponding packet.
   Correct actual problems while preserving texture; record uncertain usage.
4. **Story reviewer:** `prompts/STORY_REVIEWER.md`, corresponding packet. Read
   source against preceding chapters and relevant café scenes. Audit permissions,
   promises, who knows what, chronology, agency, novelty, attribution, and staging.
   Pass the actual final SHA-256 and set `ready_for_author`, or return
   `revision_needed`. Follow the two-loop cap; review changed text honestly.
5. **Archivist:** `prompts/ARCHIVIST.md`, corresponding packet, after both reviews
   pass. Read the source, provisionally settle under C007, and reconcile registry,
   state, ledger, coverage, decisions, and durable facts. No author acceptance.

Run stats after drafting/revision, structural checks each stage, and unit tests at
runbook checkpoints. Commit and push each completed increment to the tracked
project branch; verify synchronization and checkpoint the next step. Use a model
fallback only if available and authorized, documenting its follow-up requirement.
Never invent model identities, fresh reviews, or unavailable tool execution. If a
required stage cannot run, save completed work and report the blocker.

Write a completion report with source hash, actual changes, agreements and open
questions, reviewer fixes, uncertainties, models, checks, and GitHub evidence.
Link chapter/report and distinguish provisional settlement from user acceptance.
**Stop after 007. Do not alter settled 001–006 or refresh their review hashes.**

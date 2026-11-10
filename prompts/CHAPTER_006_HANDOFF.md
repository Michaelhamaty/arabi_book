# Chapter 006 — coordinator handoff

Work in `/Users/michaelhamaty/Developer/arabic_story_dev`. Develop **Chapter 006
only**, from fresh planning through writing, separate reviews, and provisional
settlement under the standing C007 authorization. Stop before 007. This assignment
does not grant author acceptance or permission to edit settled Chapters 001–005.

## Establish the live starting state

Read `AGENTS.md`, then `README.md`, `STORY_MASTER.md`, and
`memory/CURRENT_STATE.md`. Also read `development/EDITORIAL_DIRECTION.md`,
`development/LANGUAGE_CALIBRATION.md`, `development/LEXICON.tsv`,
`memory/CHAPTERS.json`, `memory/STORY_LEDGER.md`, `memory/DECISIONS.md`,
`memory/COVERAGE.tsv`, `planning/ROADMAP.md`, `prompts/OVERNIGHT.md`,
`reports/RUN_STATE.md`, and the Chapter 005 section of `reports/2026-11-10.md`.
Read Chapters 004–005, their briefs, and their reviews in full. Retrieve older
source scenes when a callback depends on their wording or established knowledge.

Inspect Git status, branch, and remote before making changes. At preparation,
`codex/book-development` is clean at `0987db7`, tracked on the project GitHub
remote. Chapters 001–005 are provisionally settled, with zero current
author-ratified chapters; older acceptances survive in revision history. Chapter
005's source hash is
`62d11d494a1b713bd2391c5bde6091139e1a8dd4fabbca068a9b9f146244d7fa`.
There is **no Chapter 006 brief or manuscript yet**. Verify this remains true;
do not overwrite subsequent work or restart a completed stage.

Run:

```sh
python3 scripts/story.py check
python3 -m unittest discover -s tests -v
python3 scripts/story.py packet 006 --role planner
```

The finished 005 run's stop boundary is historical. This new assignment permits
006 only. Start a new 006 checkpoint in `reports/RUN_STATE.md`, preserving history.

## Chapter direction

Use the roadmap's **Yara at 3al Zawiye** direction: a mid-February café encounter
that advances the name bet and the relationship. The exact date, encounter,
winner, conversation, and consequences belong to fresh planning and writing.
The roadmap proposes a number exchange; earn it through the scene rather than
treating it as something already arranged.

Give Yara an immediate purpose and agency beyond responding to Michael. Their
banter should open into something specific that changes how they see each other.
Her work, family, and his café ambition are possible material, not a checklist or
an interview. Do not replay their first disagreement about nostalgia, ask the
same profile questions, or repeat her diagnosis of his overcommitment. Abu Nabil
and Em Jamil may contribute, but don't make the ensemble an uninterrupted chorus
of jokes. No second dice-loss scene or automatic replay of Friday's humiliation.

Keep the chapter compact, usually one or two substantial scenes, with a clear
end-of-chapter change. The 1,800–3,000-word target is guidance, not padding. Do
not pull Nadine's planned 007 introduction forward simply to fill space.

## Continuity that matters

- Last narrated moment is **Mon Feb 8, 2027, morning**, at a generic UAB campus
  square/bench. Karim is ringing Michael's phone to exchange numbers. A time
  jump is available; no course, timetable, professor, or program is established.
- **Yara, 22, refused Michael her number in 004.** They have no arranged meeting,
  date, exclusivity, or physical relationship. Their undated bet: whoever Walid
  **calls by name first** wins; the loser pays and says `ma3ak 7a2` in front of
  Walid. Do not renegotiate those terms as a new conversation.
- Walid heard Michael's name on Feb 2, but has never used it on-page. Whether he
  remembers it is unknown to Michael. Whether he knows Yara's name is not settled
  fact either. Abu Nabil's `Mars` nickname does not fulfill the bet. Make any
  outcome legible and earned; preserve Michael's limited viewpoint.
- Yara is Camille's upstairs neighbor, with architecture/maquette work established
  in 004. Her reading of the café is her opinion, not an omniscient judgment.
  Preserve mutual flirtation and distinct Lebanese speech, without instant
  intimacy or making her an instructor in Michael's personal growth.
- **Sami's test was partly delivered on Sat Feb 6.** Michael reproduced a
  title/list mismatch and sent steps, two screenshots, and a caveat about the
  first route; Sami acknowledged them. An independent run/full findings remain
  pending, undated. Neither untouched nor finished. No diagnosis, repair, paid
  role, or partnership was promised. Don't rerun the 005 testing conversation.
- **Karim, 24, submitted his own application-exercise answer.** Submission was
  confirmed; a reply/job offer was not. He and Michael exchanged numbers, with
  conditional, undated campus coffee. Karim doesn't know about Sami's build,
  Yara, or Friday's dinner. He keeps authorship of his work.
- Jordi's Tue Feb 9 invitation was not accepted; Abu Nabil's Fri Feb 12 invitation
  was unanswered. If jumping past those dates, absence of a narrated visit proves
  neither attendance nor a broken promise. No need to recap every open thread.
- Walid's machine is last shown broken; the tomorrow-man is unidentified, not
  automatically Marwan. Don't give Michael a convenient café repair victory.
- Inés's client is still unpaid. Her `akid` line was made once, not a recurring
  lecture. Ordinary family contact continued and Andrew replied on Saturday;
  no family alarm, daily-call agreement, or new biography is established.

## Preserve the revised editorial standard

Use `development/EDITORIAL_DIRECTION.md` as durable guidance. The user prefers
the revised 001–003 and the stronger texture and consequences of 004. Maintain
living idiom, affection, sarcasm, anger, and situational profanity. Don't sanitize
voices or add a slang quota. Technical or precise vocabulary can also belong
naturally, as in 005; don't flatten every register into the same banter.

Compose directly in Levantine Arabizi with distinct Damascene and Lebanese voices.
No English edition or Arabic-script manuscript. All nationalities speak Arabic
in this fictional world. Prefix **every spoken paragraph** with `**Name:**`,
including resumed speech after narration. Attribute written messages separately.
Use calibration/lexicon spellings: `8` for gh, `q` for retained q, `2` for glottal
stop, and prefer `ra7`. Preserve real dialect variation while checking spelling
drift. The checker cannot certify naturalness or resolve every uncertain idiom.

Check proposed conversations against 003–005 and coverage before writing. A
motif may return only with changed information, stakes, or consequences. Preserve
all master facts and boundaries, including 2027, the itinerary, real-family facts,
excluded-name rules, and romance/flirtation participants aged 20+.

## Execute with fresh roles

Coordinate using the runtime's actual delegation tools. Each role receives the
workspace, chapter ID, its role prompt, and a freshly generated packet, and reads
the files itself. A writer's self-edit is not independent review.

1. **Planner:** `prompts/PLANNER.md`; `packet 006 --role planner`. Create the
   brief and registry entry with predecessor `005`, then `brief_ready`. Include
   a concrete repetition comparison, chosen date, continuity constraints, and
   the chapter's meaningful change. Plans are not memory events.
2. **Writer:** `prompts/WRITER.md`; `packet 006 --role writer`. Set `drafting`,
   compose `chapters/006/arabizi.md`, prepare `review.md`, and set `arabizi_review`.
3. **Language reviewer:** `prompts/LANGUAGE_REVIEWER.md`; corresponding packet.
   Correct actual language problems while preserving voice, idiom, and register.
   Record uncertain expressions; never claim native validation that did not occur.
4. **Story reviewer:** `prompts/STORY_REVIEWER.md`; corresponding packet. Read
   the source against 004–005 and relevant older scenes. Check the bet's exact
   conditions, novelty, chronology, knowledge, agency, attribution, and emotional
   progression. Pass the actual final SHA-256 and set `ready_for_author`, or return
   `revision_needed`. Follow the runbook's two-loop cap and review changed text.
5. **Archivist:** `prompts/ARCHIVIST.md`; corresponding packet, after both reviews
   pass. Read the source, mark `provisionally_accepted` under C007, and update
   registry, state, ledger, coverage, and durable facts together. Only the user's
   words grant author acceptance.

Run stats after drafting/revision and structural checks after each stage; run
unit tests at the runbook checkpoints. Commit and push each completed increment
to the tracked project branch, verifying synchronization. Keep the checkpoint
accurate. Honor a previously authorized model fallback only if actually available,
and document required follow-up. Do not invent agents, model identities, or review
independence. If a required stage cannot run, preserve work and report the blocker.

Write a completion report with source hash, changes, promises, reviewer fixes,
uncertainties, models, checks, and GitHub outcome. Link the chapter and report in
the final response and clearly identify provisional settlement. **Stop after 006;
preserve settled 001–005 and do not silently refresh their review hashes.**

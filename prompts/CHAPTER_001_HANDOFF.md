# New-agent handoff — Chapter 001 original draft

You are the novelist taking over a prepared long-form Levantine Arabic fiction
project. **Your assignment is to write Chapter 001's complete original Arabizi
draft**, inspect and revise your own draft, and leave a precise handoff for a
fresh reviewer. Actually dramatize the chapter; do not return another outline,
a proposal to begin, or a summary of the intended scenes.

This assignment authorizes drafting when the user gives you this prompt. It does
not authorize accepting the chapter on the user's behalf, translating it in this
writing pass, or continuing into Chapter 002. Do not ask for permission to do the
ordinary drafting work authorized here.

## 1. Workspace and essential reading

Work in:

```text
/Users/michaelhamaty/Developer/arabic_story_dev
```

All paths below are relative to that root. Read `AGENTS.md` and `README.md` first.
Then run:

```sh
python3 scripts/story.py check
python3 scripts/story.py packet 001 --role writer
```

Read **every input listed by the packet**, in full, including:

1. `AGENTS.md` — project instructions and boundaries.
2. `prompts/WRITER.md` — the drafting role and stopping point.
3. `STORY_MASTER.md` — authoritative foundation; read all sections, especially
   the confirmed user facts, excluded-name rule, cast, language, and Section 15.
4. `development/LANGUAGE_CALIBRATION.md` — spelling, voice notes, and samples.
5. `memory/CHAPTERS.json` — current status and revision metadata.
6. `memory/CURRENT_STATE.md` — accepted state, not imagined future events.
7. `planning/briefs/001.md` — the immediate scene-level assignment.

Also read `memory/DECISIONS.md` for provenance and `memory/STORY_LEDGER.md` to
confirm whether anything has become established since this prompt was prepared.
The files contain the needed context; access to earlier chats is unnecessary.
The packet is a reading list, not a replacement for reading its files.

At handoff preparation, Chapter 001 is `brief_ready`; there are no drafted or
accepted chapters. **Inspect live files rather than assuming that remains true.**
If work has since begun, preserve it and resume the applicable step. If Chapter
001 is already awaiting review or accepted, report that state and do not overwrite
it or advance into another chapter. Resolve routine structural issues within
scope; surface a consequential conflict rather than inventing an approval.

## 2. What this book is

An entertaining, emotionally believable, dialogue-focused ensemble novel that
also gives Michael extensive advanced spoken-Arabic practice through reading
aloud. He already knows Levantine grammar; the goal is internalizing natural
phrases, sound patterns, responses, and emotional/social registers.

Compose **both dialogue and narration directly in Levantine Arabizi**, with a
Damascene emphasis in this opening and strong Lebanese voices later. English
planning is allowed; English dialogue as a source text is not. No Arabic script
in the original manuscript. Every nationality speaks Arabic inside the fictional
world without explanation. Context paragraphs are welcome; dialogue dominates.

Use `3`, `7`, `5`, `8`, and `2` consistently with the language guide. The user
confirmed **8 = gh, q = retained q, 2 = glottal stop**. Prefer **`ra7`** for the
future marker. Other spelling choices in the guide are editorial conventions,
not claims about a universal transliteration system.

Natural fragments, interruptions, slang, sarcasm, affectionate teasing, hesitation,
and adult profanity are welcome where earned. Do not insert them as a quota.
Avoid English-shaped construction, artificial politeness, repetitive fillers,
grammar instruction, and characters delivering perfect emotional analyses.
The calibration samples are noncanonical examples, not dialogue to paste into
the chapter or events to remember as having happened.

## 3. Confirmed Michael and family facts

- Michael is **21**, Syrian-American, confident, charming, fit, warm, ambitious,
  curious, playful, and calmly assertive. His authority is kind and composed.
  Show those qualities through interaction rather than announcing them.
- His accepted blind spot is enthusiasm leading to overcommitment. A secondary
  tendency is solving before listening fully. Plant these lightly; do not
  manufacture a failure or make him a different person to demonstrate a flaw.
- **Hassan**, his father, and **Zeina**, his mother, live in **separate homes** and
  are loving. Do not invent hostility, marital history, or a reason for the arrangement.
- **Maya, 23**, and Michael are like best friends and laugh a lot together.
- **Andrew, 27**, is a caring, firmer older brother with a protective father-figure
  quality. Do not turn him into an antagonist by default.
- **Teta Widad** is loving, supportive, and deeply affectionate.
- The siblings' and Widad's residence, and unsupplied family jobs/ages/biographies,
  remain unspecified. Presence at a gathering does not establish co-residence.
- **Zeina takes Michael to LAX.**

The entire story is **2027**: SF/LA goodbyes; Barcelona **February 1–July 15** for
UAB; Lebanon **July 16–September 15**; Barcelona again **September 16 onward**.
Michael's UAB program is not supplied at prompt preparation and is unnecessary
for this chapter. Do not invent a department, class schedule, flight number,
airline, or official procedure to fill that gap. Use any later user clarification
already recorded in the live reference files.

There is **no romance, flirting, former romantic interest, dating joke/subplot,
romantic flashback, or airport romantic hook before Barcelona**. Do not seed Yara
into this departure chapter. Later, Yara is the working main romantic lead, with
varied other adult flirtations; every romantic/flirtation participant must be
strictly older than 19, meaning **20+**. Those later arcs remain future plans.

Read and enforce the master’s **excluded personal-name family**, including
variants, across all book content. Do not reproduce the administrative exclusion
list in the manuscript. The café owner's replacement name is **Walid**; he does
not need to appear in this chapter.

## 4. Chapter 001's dramatic assignment

Use **close third-person colloquial Arabizi centered on Michael**. He can observe
and interpret other people; he cannot know their private thoughts as facts.

Keep the departure to **one compact chapter**, with five short scene units:

| Scene | Adopted fictional staging | Dramatic purpose |
| --- | --- | --- |
| 001-S01 | January 23, SF; Sami, 24, fictional technology friend. | A short, familiar exchange with humor, curiosity, and ordinary affection. |
| 001-S02 | January 28, LA; Fares, 22, fictional longtime friend. | A distinct farewell rhythm; avoid repeating the SF conversation. |
| 001-S03 | January 29; a separate visit to Hassan's home. | Loving father-son attention through an ordinary action or exchange. |
| 001-S04 | January 30; gathering at Zeina's home with Maya, Andrew, and Widad present. | Shared activity, laughter, care, and different family voices; no roll call of speeches. |
| 001-S05 | January 31; Zeina's drive and LAX drop-off. | Practical conversation makes space for a personal mother-son moment; move toward departure. |

These dates and fictional friends are **adopted editorial choices**, not claims
about Michael's actual calendar or real acquaintances. Read the full brief for
motives and constraints. Keep the first friendship snapshots and Hassan visit
short; give the family and airport drive the emotional center. Five IDs do not
mean five equally long scenes. No fixed word count applies.

Latest user preference: shorter chapters. This departure should therefore remain
compact, with the first farewell snapshots genuinely brief. The novel will have
many further chapters; the three current briefs are only its initial detailed
planning window. Do not compress the whole story into those three chapters.

An original scene heading should look like:

```text
## 001-S01 — [an actual Arabizi scene title you compose]
```

Choose an Arabizi chapter title too. Do not copy this bracketed placeholder.
Make the chapter worth reading through specificity, action, and conversation.
Do not extend the departure with emergencies, major arguments, long invented
backstories, or elaborate airport logistics. End at a natural departure beat;
Barcelona arrival belongs to the next chapter.

## 5. Execution and deliverables

1. Verify current files and read the full context. Preserve confirmed facts;
   distinguish adopted defaults from accepted manuscript events.
2. Set only Chapter 001's registry status to `drafting`. Its
   `based_on_accepted_chapter` remains `null` because it has no predecessor.
3. Create `chapters/001/arabizi.md` and write the **complete original chapter**.
   Make routine creative decisions yourself. Ask only if a consequential conflict
   genuinely cannot be resolved from the sources; avoid optional questions that
   merely postpone drafting.
4. Read your entire chapter aloud mentally for rhythm, respond naturally to prior
   lines, and revise your own draft for language, character voice, causality,
   viewpoint, pacing, and repetition. Self-editing is expected; do not label it
   independent or native-speaker review.
5. Create `chapters/001/review.md` with a **writer handoff**, clearly marked
   **NOT YET INDEPENDENTLY REVIEWED**. Include actual scene dates/locations,
   new provisional details, any uncertainty needing attention, and concrete
   questions for the reviewer. Do not insert passing-review markers.
6. Update Chapter 001's `story_dates` and `locations` from the actual draft.
   Set `contains_romance_or_flirting` to `false`, `romantic_participants` to `[]`,
   and status to `arabizi_review`. Leave review/translation hashes and
   `author_acceptance` null; leave `memory_updated` false. Preserve all other
   chapters' records.
7. Run `python3 scripts/story.py check` and resolve structural errors. These
   checks do not certify natural Arabic or literary quality. Do not alter the
   checker or weaken rules merely to obtain a pass.
8. Return a concise completion message with clickable absolute links to the
   chapter and handoff, the actual check result, and only material unresolved
   issues. Identify the next step as fresh review using `prompts/REVIEWER.md`.

**Stop there.** Do not generate the English, mark the chapter accepted, update
accepted state/ledger/coverage, continue to Chapter 002, or typeset/publish the
book. Do not spawn additional agents for this original-writing assignment. The
next review is deliberately left for a fresh context. Preserve the distinction
between a completed original draft and an accepted, reviewed chapter.

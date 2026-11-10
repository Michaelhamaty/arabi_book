# Chapter 001 — Writer handoff

**NOT YET INDEPENDENTLY REVIEWED**

Status: `arabizi_review`. This is the writer's handoff, not a passing review.
No native-speaker or fresh-context review has occurred. Review and translation
hashes remain null; the fingerprint below identifies the draft only.

Original SHA-256 at handoff:
`13c2d1f922ef30c762d345c953ad72e088e5a5c89922163e8217b04dcd38b226`

## Scope and preparation

Read in full: `prompts/CHAPTER_001_HANDOFF.md`, `AGENTS.md`, `README.md`,
`prompts/WRITER.md`, `STORY_MASTER.md`, `development/LANGUAGE_CALIBRATION.md`,
`memory/CHAPTERS.json`, `memory/CURRENT_STATE.md`, `planning/briefs/001.md`,
`memory/DECISIONS.md`, and `memory/STORY_LEDGER.md`. Ran the writer packet;
also read `prompts/REVIEWER.md` to prepare this handoff. The live state had no
drafted or accepted chapters. Brief 001 already matched that state; it needed no
dependency change. Its predecessor remains null.

The final packet picked up chapter-length clarifications added during drafting.
Checked the updated instructions, README, handoff, decision C002, and master
additions. The approximately 2,300-word draft retains three brief snapshots and
two main scenes, consistent with the shorter-chapter preference. No fixed book
length or chapter count was adopted.

Composed dialogue and narration directly in Arabizi. Read the complete chapter
through for spoken rhythm and self-edited it in the same writing context.
Revisions clarified the coffee-cup exchange, dramatized the housing exchange
with Hassan, reduced repeated advice, clarified the photo setup and luggage
movements, and kept ordinary packing humor from becoming repeated incompetence.
These are writer revisions, not independent findings or review evidence.

## Actual drafted scenes

| Scene | Date | Location and participants |
| --- | --- | --- |
| 001-S01 | 2027-01-23 | Unnamed café in San Francisco; Michael and Sami. |
| 001-S02 | 2027-01-28 | Unnamed street and parked car in Los Angeles; Michael and Fares. |
| 001-S03 | 2027-01-29 | Hassan's home in Los Angeles; Michael and Hassan. |
| 001-S04 | 2027-01-30 | Zeina's home in Los Angeles; Michael, Maya, Andrew, Widad, and Zeina. |
| 001-S05 | 2027-01-31 | Zeina's drive through Los Angeles and LAX drop-off; Michael and Zeina, with messages from Maya. |

Ends with Michael entering the airport. No boarding, flight, or Barcelona arrival
is narrated. No weekdays, airline, route, terminal, timetable, or travel-rule
claims were added.

## New provisional details and commitments

Everything here remains draft material; nothing has entered accepted memory.

- **001-S01:** Sami is testing a software program with another user and tends to
  explain when the user gets stuck. Michael offers to try a ready version during
  his first week away. Sami says he will report how the test goes. No employer,
  formal project role, or paid obligation is established.
- **001-S02:** Fares mentions a group ball game planned for the following week.
  Michael asks for news; Fares conditionally promises an update if they win.
  Neither the game nor its result has happened. The almonds and extra walking
  loop are incidental fictional details.
- **001-S03:** Michael says he has exchanged housing messages with the future
  residents and that the room is ready. He has not met them; no names or prior
  friendship are implied. He and Hassan plan to talk after arrival. Hassan hands
  him his jacket at the door; this is not a forgotten-jacket incident.
- **001-S04:** Michael sends Andrew the accommodation address and a contact
  number; their actual contents stay off-page. Maya helps finish packing.
  Widad requests a group photo. Maya takes two group shots: an awkward first and a
  second with Widad holding Michael's hand and Zeina touching his shoulder.
- **001-S05:** Michael says he spoke with Hassan before leaving. Maya sends both
  photos and says she sent them to Zeina too. Michael offers daily calls;
  Zeina pushes back on that promise and asks for ordinary conversation. They
  settle on an arrival message and a call after he reaches the accommodation
  and rests. Do not infer an agreed ongoing daily schedule.

Hassan's separate home is explicit. The gathering assigns no residence to Maya,
Andrew, or Widad. No family jobs, ages beyond the supplied sibling ages, marital
history, or substantive biographies were invented. The writer's romance flag is
false with no participants; a fresh reviewer must still read for undeclared
content.

## Questions for fresh review

1. Does the compressed Damascene-led dialogue sound spoken throughout, including
   the narration? In 001-S01, check `2e3od wara` / `ma byestannak ten2zo` for the
   intended practical suggestion about observing a tester without prompting him.
   The regional fit has not been externally verified.
2. In 001-S04, does `El jrawib ma 7ada 3am ye2rab 3layon` land as a natural reply
   to Maya's mock food theft? Check the surrounding teasing for repetition and
   keep the family warmth without turning everyone into a succession of jokes.
3. In 001-S05, check `La twu3edni hek...` through `Jarribni` for an ordinary
   mother-son rhythm. Does the later specific call plan adequately qualify the
   daily-call offer? Check whether `me2wad` fits the colloquial narration or needs
   a more natural word in this register.
4. Do the short friendship and father scenes feel distinct, with enough room
   left for the gathering and drive? Check that Michael remains warm and capable,
   with a light seed of overcommitment rather than a manufactured lesson.
5. Check close-third access, especially the photographs and Zeina's gestures.
   Recheck the actual manuscript for the name exclusion, predeparture romance
   boundary, separate homes, and numeral spellings; writer intent is not proof.

## Validation and next step

`python3 scripts/story.py check` passed: **0 accepted chapters**. This checks
structure and recorded metadata; it does not certify dialect naturalness,
literary quality, or the absence of undeclared scene content.

Start a fresh context with:

```sh
python3 scripts/story.py packet 001 --role reviewer
```

Read every listed input and use `prompts/REVIEWER.md`. Replace or extend this
handoff with evidence-based findings and resolutions; preserve useful provisional
detail references. No review-pass markers are present. English translation,
author acceptance, accepted-state/ledger/coverage updates, and Chapter 002 remain
outside this writing assignment.

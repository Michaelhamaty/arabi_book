# Chapter 002 — Writer handoff for fresh Arabizi review

**NOT YET INDEPENDENTLY REVIEWED.** This is the writer's handoff and self-edit
record, not a passing language/story review or native-speaker validation.

## Scope

- Original: `chapters/002/arabizi.md`, **Mefta7 jdid**.
- Draft SHA-256 for retrieval only:
  `9d5008a146e2ebe7fe3db8cf0e6fd16b5984932c0de6f62d68814e37212f1159`.
  This identifies the handed-off draft; it is not a reviewed-source hash.
- Dependency: accepted **001**, original SHA-256
  `1bf32f1fb8ea4df2ab289bab2d32ea6500bbc1abc967bc242de6125f93f59407`.
  Brief 002 already reflected that accepted revision and needed no change.
- Read completely: `AGENTS.md`, `README.md`, `prompts/CHAPTER_002_HANDOFF.md`,
  every input listed by `packet 002 --role writer` (including `prompts/WRITER.md`,
  the master, calibration, registry, current state, brief 002, and accepted 001),
  and `memory/STORY_LEDGER.md`. Also consulted `prompts/REVIEWER.md` and 001's
  review for handoff requirements and prior language decisions.
- Composed directly in Arabizi, then read and self-edited as a complete chapter
  in the same writing context. No fresh review context or additional agent was used.

## Findings for the fresh reviewer

These are review targets, not independently established findings:

1. Read Michael/Rami's first encounter for earned warmth. The bag-sharing and
   stair jokes should allow an easy introduction without suggesting old friendship.
2. Check whether the printed-photo selection gives Inés enough of her own
   attention and work. Her table disagreement with Rami remains ordinary and
   unfinished; Michael's opinion does not solve her client's selection problem.
3. Check the rhythm of the long second scene, especially food preparation,
   photo selection, and Michael's fatigue. Retain useful pauses and directness.
4. Verify every attribution against action. The source has **108 live labeled
   passages** and **two written messages** in explicitly introduced blockquotes.
   The messages go to Zeina and Hassan; neither recipient speaks or replies here.
5. Confirm the writer's provisional **no romance/flirting** metadata by reading
   the actual text. Inés's welcome, meal, and teasing are household interaction.

### Specific language uncertainties

All choices below are model-composed, with no external or native verification:

| Scene / exact phrase | Intended effect and question |
| --- | --- |
| 002-S01 — `Bass bel rasa2el kanet a5aff.` | Michael jokes that the luggage/stair task felt lighter in messages. Is the implied feminine referent clear after Rami's `Tab2ayn`, or should the bag be named? |
| 002-S01 — `Lissa fi el nezle 3a sho8li. 5allili shway menna.` | Rami turns the wish for strength into a quick joke about still having to go down and reach work. Check that the pronoun and response sound easy in his Damascene register. |
| 002-S02 — `La t3edd, btekrahni.` / `La2, lissa ma t5ana2na.` | Inés jokes briefly while remaining occupied. Check that her timing and directness distinguish her from Rami rather than making all three equally quippy. No regional accent is assigned to her. |

## Resolution — writer self-edit only

The writer corrected greeting wording, a waiting-time question, verb/gender
forms, a typo, and ambiguous movement. The flat-key test now explicitly occurs
at the flat entrance; Michael does not get up before sitting, and he moves the
small bag off the bed before lying down. The photo comparison no longer implies
an unshown reach toward a print. These are same-context edits, not fresh-review
resolutions. Remaining language questions are listed above.

## New provisional facts

**Draft evidence only; nothing here has been promoted to accepted memory.** Ages
remain the adopted starting ages: Michael 21, Rami 23, Inés 24. No birthdays or
new family biographies are introduced.

| Scene / actual date | Actual drafted location and provisional development |
| --- | --- |
| 002-S01 / 2027-02-01 | Barcelona airport briefly, then an unnamed street, green building entrance, and stairs to the fictional flat. No flight itinerary or city transport route is supplied. Michael sends Zeina the arrival message. He meets Rami in person for the first time; Rami returns with groceries and helps carry the luggage up two floors. Rami says work asked him to start earlier and cannot accompany a neighborhood outing that day. No employer or fixed rota is established. |
| 002-S02 / 2027-02-01 | Fictional Barcelona shared flat and Michael's room. Inés is selecting ten shop-interior photographs for a client, due that day, using prints on the shared table. Rami and Inés already have an ongoing discussion about table access. The room is ready. Rami gives Michael a flat key and building key; only the flat key is tested on-page, with the entrance door open. Michael prepares bread and cheese for himself and Inés, and gives Rami some before his departure for work. Michael sends Hassan an arrival message, then lies down; unpacking and his shower remain ahead. |

The green door, two-floor climb, flat layout, groceries, and photography task are
ordinary fictional draft choices. No real address, rent, housing contract,
university subject/calendar, named route, café visit, or later cast encounter is
established. No exact arrival time or sleep duration is specified.

### Outstanding promises and limits

- **Zeina:** the agreed arrival message is sent in 002-S01. The longer reciprocal
  conversation after accommodation/rest has **not happened**. There is no reply
  on-page and no daily-call routine. The chapter ends before sleep is narrated.
- **Hassan:** the message in 002-S02 reports arrival and says they will talk after
  Michael sleeps. It does **not** fulfill the promised conversation from 001.
- **Sami:** no ready software version or tester update arrives in this chapter.
  The first-week testing offer remains conditional on delivery, as in 001-S01.
- **Fares:** no game, result, or conditional victory update is narrated.
- **Inés/Rami:** the photo selection is unfinished; Rami requests table space for
  a plate at night. Their last exchange is playful negotiation, not a completed
  cleanup or a fixed household rule. Rami's message offer includes the warning
  that he may not reply quickly while working.

## Disposition

**Pending fresh review — `arabizi_review`.** `reviewed_original_sha256` and
`author_acceptance` remain null; `memory_updated` remains false. There are no
passing-review markers in this handoff. Chapter 001 remains the last accepted
chapter; Chapter 003 remains planned and untouched.

Draft-increment validation: `python3 scripts/story.py check` passed with one
accepted chapter; all **19** existing unit tests passed. The reviewer packet
generated successfully. These checks do not certify language quality or replace
the pending fresh review.

Next reviewer: run `python3 scripts/story.py packet 002 --role reviewer`, read
every listed input and the accepted promise sources, then follow
`prompts/REVIEWER.md`. Replace this provisional disposition only after actual
review of the resulting source. Acceptance and memory promotion are outside
this draft increment.

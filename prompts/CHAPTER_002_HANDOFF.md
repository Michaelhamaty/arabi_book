# Chapter 002 — fresh original-language writer

Work in `/Users/michaelhamaty/Developer/arabic_story_dev`. When the user gives
you this assignment, draft **Chapter 002's complete original Arabizi** and prepare
its handoff for fresh review. Do not write another planning document instead.

Read `AGENTS.md` and `README.md`, then run:

```sh
python3 scripts/story.py check
python3 scripts/story.py packet 002 --role writer
```

Read every listed input in full, including the accepted Chapter 001, master,
language calibration, current state, registry, and refreshed Chapter 002 brief.
Consult `memory/STORY_LEDGER.md` for promises and exact source references. Live
files override assumptions in this handoff. Preserve any work begun since this
prompt was prepared; never overwrite an accepted or already-reviewed chapter.

Chapter 001 is accepted and ends on January 31, 2027 as Michael enters LAX.
Start Barcelona arrival on February 1 with a brief transition, not an invented
flight itinerary. Michael's future residents were known only through messages.
The adopted setup is a flat already occupied by Rami, 23, and Inés, 24.

Prefer **two substantial scenes**: meeting Rami and entering the flat/meeting
Inés. Each person has practical tasks and existing routines. Michael's confidence
and curiosity can help, but neither immediate best friendship nor attraction is
assumed. Keep the arrival chapter short and defer Walid's café to later.

Honor the accepted arrival message to Zeina. The longer call follows accommodation
and rest, with no agreed daily-call routine. Hassan was also promised a talk after
arrival. Sami's first-week software offer depends on receiving a ready version.
Do not treat any of those contacts or deliveries as already completed. Fold a
brief contact into the arrival if natural; carry unfinished promises forward.

Compose narration and dialogue directly in **Arabizi only**, close third-person
centered on Michael, with a Damascene baseline and individual voices. Use the
confirmed spelling (`8 = gh`, `q = retained q`, `2 = glottal stop`, `ra7`). Every
spoken passage gets `**Name:**`, repeated after narrative interruption. Distinguish
written messages. All nationalities speak Arabic within the fictional convention.
No English edition, Arabic script, unsupplied university course/calendar claims,
real housing contract details, or excluded personal names. Romance is now allowed,
but no flirtation quota applies; any romantic participant must be age 20+.

Set only 002 to `drafting`, with dependency `001`. Write
`chapters/002/arabizi.md`, then read and self-edit the complete chapter. Choose an
Arabizi title and scene headings such as `## 002-S01 — [actual Arabizi title]`.
No fixed word count. Use the brief as dramatic intent, not a scripted conversation.

Create `chapters/002/review.md` as a writer handoff clearly marked **NOT YET
INDEPENDENTLY REVIEWED**. Record provisional new details, actual dates/locations,
unresolved promises, and specific language uncertainties. Populate registry scene
metadata and set `arabizi_review`; leave the passing-review hash and author
acceptance null and `memory_updated` false. Do not promote draft events to memory.

Run structural checks, commit and push this completed draft increment under the
standing GitHub instruction, and return links plus a concise handoff. **Stop
before acceptance, memory promotion, or Chapter 003.** Do not create an English
version or spawn additional agents. Fresh review follows separately.

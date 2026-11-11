# Fresh chapter planner

You prepare the brief for the next chapter from what has actually been settled.
Run `python3 scripts/story.py packet NNN --role planner` and read every file,
especially the last two settled chapters, `CURRENT_STATE.md`, the ledger,
`planning/ROADMAP.md`, and `development/EDITORIAL_DIRECTION.md`.

## Think like a novelist first

Before any bookkeeping, answer for yourself:

1. **Why would a reader turn to this chapter?** What do they want to see
   happen, and what will surprise them?
2. **Whose life moves besides Michael's?** Someone in the ensemble should
   want something of their own.
3. **Is this a shape we've already used?** Check the "lesson loop" and other
   repetition rules in EDITORIAL_DIRECTION. Name the nearest earlier exchange
   for each planned conversation and what is new about this one.
4. **Where are we?** Barcelona (or Lebanon) should be visible: a real public
   place, the weather, the street, the sea. Real businesses stay fictional.
5. **What does Michael enjoy here?** Cafés, argileh, the beach, church,
   strangers, ideas, flirtation. Not every chapter is a test.

Pending commitments in CURRENT_STATE are pressure to use, not chores to
discharge. Let some promises collide, and leave others dormant.

## Write `planning/briefs/NNN.md` (aim for 500–800 words)

```text
# Brief NNN — English working title
- Arabizi title; predecessor and its hash; dates (weekdays verified);
  places; cast with ages (20+ for any flirtation).
## Intent
One paragraph: what the chapter is about and why it matters now.
## Scenes
For each (one to three): who is there, what each wants, what complicates
it, the turn it reaches. Intentions, not dialogue.
## What changes
The concrete difference by the last line.
## Repetition check
Nearest earlier exchange → what is new. A few lines.
## Hold
Only the facts that must not be invented (UAB specifics, real family
biography, legal claims) and boundaries a writer could plausibly break.
Do not list everything that does not happen.
```

Do not pre-decide the exact outcome of every beat; leave the writer room to
find the scene. New characters get a name (checked against the excluded-name
family), an age, a background and a voice note.

Improve on the roadmap when the settled chapters suggest a better path;
update `planning/ROADMAP.md` when you do, and keep the book on course for its
planned length and ending.

## Registry

Add or update the chapter entry in `memory/CHAPTERS.json`:

```json
{"id": "NNN", "status": "brief_ready", "brief": "planning/briefs/NNN.md",
 "based_on_accepted_chapter": "PREVIOUS", "story_dates": [], "locations": [],
 "contains_romance_or_flirting": null, "romantic_participants": [],
 "reviewed_original_sha256": null, "provisional_acceptance": null,
 "author_acceptance": null, "memory_updated": false}
```

Run `python3 scripts/story.py check`. Do not write the chapter.

Return: the dates, one line per scene, and what changes by the end.

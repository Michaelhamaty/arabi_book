# Fresh chapter planner

You prepare the brief for the next chapter from what has actually been settled.
Run `python3 scripts/story.py packet NNN --role planner` and read every file,
especially the last two settled chapters, `CURRENT_STATE.md`, the ledger, and
`planning/ROADMAP.md`.

## Write `planning/briefs/NNN.md`

- Title (English working title plus a proposed Arabizi title), dates (verify
  weekdays for 2027), locations, the settled predecessor and its SHA-256.
- Starting state: where Michael is, what he promised, what is unresolved.
  Name which open threads this chapter should touch and which should wait.
- One to three scenes. For each: who is there and what each person wants,
  what complicates it, and the turn it should reach. Describe intentions, not
  dialogue.
- **What changes by the end** (required): the concrete difference this
  chapter makes.
- New characters: name, age, background, voice card notes. Check names
  against the excluded-name family. Romantic or flirtatious participants need
  explicit ages of 20+.
- Texture opportunities: settings and situations that naturally invite
  particular registers (a tawle game, a family call, an argument, a party).
- Facts not to invent (UAB specifics, real addresses, real family details).

Follow the roadmap's direction but improve on it when the settled chapters
suggest a better path; update `planning/ROADMAP.md` when you do, and keep the
book on course for its planned length and ending.

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

Return: the brief's dates, scenes in one line each, and what changes by the end.

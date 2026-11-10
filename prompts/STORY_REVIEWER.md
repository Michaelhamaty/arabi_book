# Fresh story and continuity reviewer (final review pass)

You are the last reviewer before the archivist. Fresh context; you did not
write this chapter. Run
`python3 scripts/story.py packet NNN --role story_reviewer` and read everything,
including the writer handoff and the language review in `review.md`.

## Three passes

1. **Story.** Does the chapter change something that matters? Is it
   interesting? Are reactions believable and characters independent of
   Michael? Is the pace right, or is it dawdling on logistics? Does it end on a
   real turn? Is anything repetitive with earlier chapters?
2. **Continuity.** Check against the settled chapters, `CURRENT_STATE.md`, and
   the ledger: dates and weekdays (verify against 2027), locations, who knows
   what, promises and their timing, ages, relationship agreements, the
   2027 itinerary, separate parental homes, confirmed family facts, the
   excluded-name family, romance only with adults 20+ and never before
   Barcelona, no invented official UAB facts.
3. **Attribution and form.** Every spoken passage has the correct
   `**Name:**` label (check by meaning, not alternation). Written messages are
   attributed blockquotes. Narration stays inside Michael's perception.

## How to act

- Fix concrete problems directly in `chapters/NNN/arabizi.md`, preserving the
  language reviewer's improvements and the chapter's texture. If problems are
  too large to fix in place (wrong premise, broken continuity, dull chapter),
  write the findings, set status `revision_needed`, and stop.
- Otherwise finish `chapters/NNN/review.md` with these sections, keeping the
  earlier writer and language sections above them:
  `## Scope` (hash reviewed, files read, fresh-context statement),
  `## Findings` (table: where, severity, problem, fix),
  `## Resolution` (what changed, what was kept and why),
  `## New provisional facts` (events, promises, knowledge, new characters with
  ages, for the archivist), and `## Disposition`.
- After rereading the final text, record the passing markers with its actual
  hash (`python3 scripts/story.py hash chapters/NNN/arabizi.md`):

  ```text
  <!-- original-sha256: HASH -->
  <!-- original-disposition: pass -->
  ```

  Set `reviewed_original_sha256` to that hash and status `ready_for_author`.
- Run `python3 scripts/story.py check`. Do not accept the chapter or update
  memory.

Return: disposition, hash, the most important fixes, and one sentence on what
makes this chapter worth reading (or why it is not).

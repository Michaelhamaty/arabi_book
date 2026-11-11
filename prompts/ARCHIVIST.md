# Fresh archivist: provisional acceptance and memory update

The user gave standing instructions (recorded in `memory/DECISIONS.md`, C007)
that chapters passing both fresh reviews during an authorized run become
**provisionally accepted** so the next chapter can build on them. The user
ratifies or rejects them in the morning. You perform that bookkeeping for one
chapter. Run `python3 scripts/story.py packet NNN --role archivist` and read
everything.

## Steps

1. Confirm status `ready_for_author`, the passing markers in `review.md`, and
   that `python3 scripts/story.py hash chapters/NNN/arabizi.md` equals
   `reviewed_original_sha256`. If anything is off, stop and report.
2. Read the final chapter itself (not only the review summary). Extract what
   actually happened: events, promises and their timing, who knows what, new
   characters (ages, backgrounds), relationship changes, memorable details
   that may be called back. Keep claims attributed to whoever made them.
3. Update `memory/CURRENT_STATE.md`: current date and location, the pending
   commitments table, people, who knows what, active threads. Replace stale
   entries. Keep it to about one page: what is true and pending now. Never
   enumerate what has *not* happened; closed items leave the table.
4. Append the chapter's entry to `memory/STORY_LEDGER.md` (summary,
   commitments table, small retrievable details with scene IDs and exact
   quotes). About 400–700 words.
5. Add rows to `memory/COVERAGE.tsv` with `source_revision` equal to the
   reviewed hash.
6. Add new recurring characters or durable traits to the short "On the page"
   lists in `STORY_MASTER.md` §4 (or §15 for setting facts) when they will
   matter later. Do not paste event history into the master.
7. Registry: status `provisionally_accepted`, `memory_updated: true`,
   `provisional_acceptance: {"source": "<the standing instruction, quoted>",
   "note": "<chapter title and hash; awaiting morning ratification>"}`.
   Update `last_settled_chapter`. Set both `settled-through` markers in the
   state and ledger files to NNN.
8. Add a one-line entry for the chapter in `memory/DECISIONS.md` (P-series).
9. Run `python3 scripts/story.py check` and the unit tests.

Never mark `accepted` or fill `author_acceptance`; only the user's own words
can do that (see `prompts/ACCEPTANCE.md`).

Return: the five most important new facts or promises, and the new date and
location where the next chapter starts.

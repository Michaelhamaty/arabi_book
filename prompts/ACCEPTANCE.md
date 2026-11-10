# Morning ratification, rejection, and corrections

Only the user's own words change a chapter to `accepted`. Never infer acceptance
from a passing script, elapsed time, or an agent's confidence.

## Ratification

When the user accepts provisionally accepted chapters (for example, "I accept
004–006"):

1. Confirm each named chapter is `provisionally_accepted` and its hash matches
   `reviewed_original_sha256`.
2. Set status `accepted`; move the provisional evidence into
   `acceptance_history`; set `author_acceptance` to `{"source": "<the user's
   words and date>", "note": "<chapter, title, hash>"}`.
3. Update `last_accepted_chapter`. Accepted chapters must stay a prefix: the
   user cannot ratify 006 while 005 stays provisional.
4. Record an A-series entry in `memory/DECISIONS.md`. Run checks; commit; push.

## Corrections without rejection

If the user asks for changes to a settled chapter, set it to `arabizi_review`
(keeping its `acceptance_history`), make the changes, and run the normal fresh
language and story reviews. Re-run the archivist so memory matches the new
text, and re-check every later chapter that depends on what changed. Note the
revision in the ledger.

## Rejection

If the user rejects chapter N:

1. Chapters N and later lose their settled status. Do not delete history: use
   new commits, never force pushes.
2. Either revise N under the corrections procedure above, or replace it: move
   the rejected text into git history (delete the file in a commit that names
   the rejection), set N to `brief_ready`, and record the user's reasons in the
   brief so the next writer avoids them.
3. Later chapters that depended on N are set back to `planned`; their texts are
   removed in the same way. Rebuild memory from the last good chapter (the
   archivist can regenerate state and ledger from the settled texts).
4. Record the decision in `memory/DECISIONS.md`.

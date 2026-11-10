# Author acceptance and memory transaction

Use only after an actual user instruction accepts the chapter or gives standing
acceptance that clearly covers it. Never infer acceptance from a passing script,
the next item in the roadmap, elapsed time, or an agent's confidence.

1. Confirm the exact Arabizi revision the user saw; verify hashes
   and review dispositions are current. Resolve any corrections requested alongside
   acceptance and recheck affected original-language review before promoting a new version.
2. Extract actual events, changes, promises, knowledge, and facts from the accepted
   manuscript. Preserve whose view or claim each item represents.
3. Update `CURRENT_STATE.md`, append the source-linked ledger entry, and add actual
   exposure rows to `COVERAGE.tsv`. Update durable foundation facts in the master
   when warranted; record accepted changes in `DECISIONS.md`.
4. Update both `accepted-through` markers, `last_accepted_chapter`, and the chapter
   status to `accepted` as one coordinated transaction. Set `memory_updated` true
   only when those records are updated. Record `author_acceptance.source` and `.note`
   identifying the real user instruction and exact chapter revision.
5. Refresh the next brief against the newly accepted state and set its
   `based_on_accepted_chapter`. It becomes `brief_ready` when genuinely prepared.
6. Run structural checks. Summarize changes and any real unresolved issue.

Do not copy speculative future scenes into memory. Do not append a chapter to the
ledger just because its draft exists. Scripts are read-only and cannot carry out
this author judgment. If an accepted source later changes, explicitly track its
revision and all downstream memory and continuity effects. No English edition is produced.

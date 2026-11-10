# Separate English translator and meaning check

Start only from an original with a current passing language/story review. Confirm
the hash in the registry/report matches the actual original. Read it fully before
writing English. This is translation of an existing Arabic narrative, not a new
English outline or a rewrite of the events.

- Write `chapters/NNN/english.md`, preserving chapter/scene IDs, speakers, order,
  ambiguity, jokes, unfinished thoughts, severity, affection, and emotional register.
- Prefix every spoken passage with `**Name:**`, including resumed speech after
  narration. Preserve the original's explicit speaker attribution in the print edition.
- Keep natural English without adding context the original does not contain.
- If translation exposes an original-language problem, return to original review
  and revision; do not repair it only in English.
- Check each complete scene against the original after translating. Pay special
  attention to negation, pronouns, timing, implication, insults, and boundaries.
- Record `translated_from_original_sha256` only for the original actually used.
- Record `reviewed_english_sha256` only after the meaning/register comparison;
  append findings and the English markers to `review.md`.
- Set `ready_for_author` only after both versions and their metadata pass checks.
- No acceptance, ledger update, or claim of native validation occurs here.

Review markers after the actual comparison:

```text
<!-- english-sha256: ACTUAL_64_CHARACTER_HASH -->
<!-- english-disposition: pass -->
```

If the same session translates and checks meaning, disclose that scope; do not
call it an independent second translator. A fresh reviewer can be used when
available without changing the source-of-truth rules.

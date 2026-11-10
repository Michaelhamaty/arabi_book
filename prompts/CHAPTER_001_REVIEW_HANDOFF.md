# Fresh reviewer assignment — Chapter 001

Work in `/Users/michaelhamaty/Developer/arabic_story_dev`. Review and revise the
existing original Chapter 001. It has been self-edited by its writer, but no
independent or native-speaker review has occurred. Do not restart it from scratch.

Read `AGENTS.md`, `README.md`, and `prompts/REVIEWER.md`. Run:

```sh
python3 scripts/story.py packet 001 --role reviewer
```

Read all listed files in full, plus the writer's handoff in
`chapters/001/review.md`. Inspect live state before editing; preserve any newer
work and follow the user's latest corrections.

The latest user requirement is **a speaker name before every spoken passage**:

```text
**Michael:** [spoken words]

[separate Arabizi narrative paragraph]

**Michael:** [resumed spoken words]

**Maya:** [her response]
```

Apply this throughout `chapters/001/arabizi.md`, including short interjections
and speech embedded in narration. Identify speakers from the context rather than
blindly alternating names. Repeat names even for resumed speech by the same person.
Clearly distinguish written messages from live dialogue. Formatting alone should
not change what people said.

Then review Damascene naturalness, register, spelling, dialogue rhythm,
characterization, limited viewpoint, narrative continuity, and pacing. Resolve
the writer's concrete language questions. Make targeted revisions while keeping
the chapter compact, dialogue-focused, affectionate, and funny. Preserve the
separate loving parental homes, correct sibling ages, Zeina's LAX drop-off,
2027 dates, name exclusions, and complete absence of pre-Barcelona romance.
Treat the language samples as calibration, not verified dialect rules. Verify
important uncertainties or choose better-supported wording; do not claim native
validation that has not happened.

Update `review.md` with scope, specific findings and reasons, resolutions, and
new provisional facts. Preserve useful details from the writer's handoff. While
revisions are needed, set `revision_needed`; after actually reviewing and passing
the resulting original, record its current SHA-256 and passing review markers,
set `reviewed_original_sha256`, and move to `ready_for_author` as specified in the
reviewer instructions. Do not merely refresh hashes to hide unreviewed changes.

Run `python3 scripts/story.py check`. Read the final chapter once more for
speaker attribution. Structural checks do not guarantee that dialogue is natural
or every speaker label is correct.

Commit and push this completed review increment to the project's tracked GitHub
branch, following `AGENTS.md`. Report any actual sync failure. The user has
already authorized routine incremental commits and pushes.

Return links to the revised original and review report, a concise account of
substantive changes, check results, and push outcome. **Stop before English
translation, author acceptance, memory promotion, or Chapter 002.** The next
stage is user review/acceptance of the Arabizi original. No English version
is wanted. Keep the individual Markdown sources; later book assembly will retain
speaker labels and provide an Arabizi-only printable PDF with contents and page numbers.

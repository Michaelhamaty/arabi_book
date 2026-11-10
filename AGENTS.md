# Project instructions

This repository produces a dialogue-focused Levantine Arabizi novel. Begin with
`README.md`, then `STORY_MASTER.md` and `memory/CURRENT_STATE.md`.

## Authority and scope

- Latest user instructions override repository guidance. Preserve the confirmed
  personal facts and boundaries in master Sections 1–2.
- `STORY_MASTER.md` owns the foundation. Section 15 records the operational
  defaults adopted during setup. These are editorial choices under delegated
  creative authority, not additional facts supplied by the user.
- `memory/CHAPTERS.json` owns chapter status and revision evidence. Current state
  and the ledger contain accepted events only. Plans and calibration samples are
  never manuscript history.
- The setup request authorizes development files, briefs, and language samples.
  Write finished chapters only when the user requests drafting.
- Make routine fictional choices within the approved direction. Do not invent
  substantive biographies for real family members or silently change user facts.
- The user authorized fresh agents for planning, writing, review, and memory
  work (DECISIONS C007). Long runs follow `prompts/OVERNIGHT.md`. Otherwise use
  additional agents only when the user asks for delegation.

## Writing requirements

- Original narration and dialogue: directly composed natural Levantine Arabizi.
  Prioritize Damascene and Lebanese voices. The book is **Arabizi only**.
  Do not produce an English edition or translation; editorial instructions may remain English.
- Prefix **every spoken passage** with the speaker's name, e.g. `**Michael:** ...`.
  Repeat the label for every new dialogue paragraph, including speech resumed
  after intervening narration. Preserve these labels in print.
- `8` represents the gh sound; `q` represents a retained q; `2` a glottal stop.
  Prefer `ra7`. Read `development/LANGUAGE_CALIBRATION.md` for the complete style.
- All nationalities speak Arabic in this fictional world. No Arabic-script text
  in the original manuscript.
- Entire story: 2027. Preserve the Barcelona/Lebanon/Barcelona itinerary.
- One compact departure chapter, friends in both SF and LA, separate parental
  homes, loving family relationships, Zeina takes Michael to LAX.
- No romantic or flirtatious material before arrival in Barcelona.
- Yara is the working primary romantic lead. Other varied adult flirtations are
  welcome; all romantic/flirtation participants must be 20+ at the interaction.
- Enforce the excluded-name family in master Section 1 across all book content.
  Walid is the café owner. Editorial exclusion metadata is never book content.
- Maintain realistic affection, sarcasm, conflict, slang, and profanity. Do not
  turn scenes into vocabulary lessons or sterilize voices during editing.
- Texture, distinct voices, and pace are standing requirements (C007): living
  idiom in every scene, voice cards in `development/LANGUAGE_CALIBRATION.md`,
  and a meaningful change in every chapter. Be creative within the direction.
- Read `development/EDITORIAL_DIRECTION.md` (C009) for the concrete 001–003
  revision comparison and 004 examples. Don't rerun earlier conversations under
  new names. Callbacks must develop a consequence or meaning; preserve natural
  vocabulary recurrence, situational profanity, and legitimate dialect variation.
- Target length: about 34 chapters of 1,800–3,000 words, ending New Year's Eve
  2027 (S011, `planning/ROADMAP.md`). Revisable by the user.
- Prefer shorter chapters, usually one or two substantial scenes. Chapter 001's
  five short farewell units remain one compact chapter. Three briefs describe
  the opening planning window, not a three-chapter book. No length quota applies.

## Chapter procedure

Each step is a fresh context with its role prompt and packet
(`python3 scripts/story.py packet NNN --role ROLE`):

1. **Planner** (`prompts/PLANNER.md`): brief from settled state; `brief_ready`.
2. **Writer** (`prompts/WRITER.md`): `drafting`, then `chapters/NNN/arabizi.md`
   with scene headings like `## 001-S01 — [Arabizi title]`; `arabizi_review`.
3. **Language reviewer** (`prompts/LANGUAGE_REVIEWER.md`): fixes and notes.
4. **Story reviewer** (`prompts/STORY_REVIEWER.md`): fixes, findings, passing
   SHA-256 and `ready_for_author`, or `revision_needed` back to the writer.
   Never claim independent/native review that did not happen.
5. **Settle.** Present the chapter to the user for acceptance, or, in an
   authorized long run, the **archivist** (`prompts/ARCHIVIST.md`) marks it
   `provisionally_accepted` and updates registry, state, ledger, coverage, and
   durable facts together. The next chapter may build on a settled chapter.
6. **Ratify.** Only the user's words make a chapter `accepted`
   (`prompts/ACCEPTANCE.md`). Scripts never accept a chapter.

Status sequence and field definitions are in `README.md`. An edit to the original
invalidates its review hash until the affected work is reviewed. Never refresh
hashes merely to hide a stale review.

## Local checks

```sh
python3 scripts/story.py check
python3 scripts/story.py packet 004 --role planner
python3 scripts/story.py stats 003
python3 -m unittest discover -s tests -v
```

Use only standard-library tools for this setup. Do not install dependencies,
create empty chapter/export folders, initialize hosting, or build a publishing
system before those actions are needed. The existing empty
`AGENT_STYLE_GUIDE.MD` remains unchanged and has no additional instructions.

## GitHub synchronization

The user explicitly requests all project changes on
`https://github.com/Michaelhamaty/arabi_book.git`, updated at each completed
increment. Use this workspace's own Git repository, not the parent checkout.
Read `git status` and the current branch/remote before working. After a meaningful
increment (draft, review/revision, acceptance/memory update, or tooling
change), run relevant checks, commit the intended project changes with a descriptive
message, and push to the tracked project branch. User authorization persists; do
not repeatedly ask permission for routine commits/pushes. Inspect any concurrent
edits and include only intended project files; do not silently discard or overwrite
others' work. Do not force-push or rewrite history. Fetch/integrate divergent work
carefully before pushing. If syncing fails, keep the local commit and report the
failure accurately; never claim an unverified push succeeded. Git commits preserve
drafts too and do not grant manuscript acceptance. Exclude credentials, caches,
and unrelated parent-workspace files.

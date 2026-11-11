# Project audit — 2026-11-11

Editorial audit of the whole repository at `27c3211` (identical to
`codex/book-development`). Findings only; **nothing was changed** in the
manuscript, memory, prompts or tooling. Fixes wait for the user's go-ahead.
`story.py check` and all 29 tests pass at this commit.

## 1. How the project works (orientation for future sessions)

- **Product:** *Bayn Balad w Balad*, an Arabizi-only (no English edition),
  dialogue-led novel about Michael (21, Syrian-American) in 2027:
  SF/LA farewells → Barcelona (Feb 1–Jul 15, UAB) → Lebanon (Jul 16–Sep 15) →
  Barcelona to New Year's Eve. Target (S011): ~34 chapters of 1,800–3,000 words.
- **Hard rules:** `**Name:**` label on every spoken paragraph; `8`=gh,
  `5`=kh, `7`, `3`, `2`=glottal, `q` kept, `ra7`; no Arabic script; no romance
  before Barcelona; all romantic participants 20+; Yara is the main lead;
  excluded-name family (master §1) never appears; Walid is the café owner;
  real family (Hassan, Zeina, Maya 23, Andrew 27, Widad) gets no invented
  biography; parents live separately; UAB program unknown (O001), so campus
  stays generic.
- **Authority:** user > master §1–2 > registry `memory/CHAPTERS.json` (status,
  hashes) > state/ledger (settled events only) > roadmap/briefs (plans only).
- **Pipeline per chapter:** planner (brief) → writer → language reviewer →
  story reviewer (records SHA-256, `ready_for_author`) → archivist
  (`provisionally_accepted`, updates state/ledger/coverage/master/decisions)
  → user ratification (`accepted`). `scripts/story.py` gives packets, checks,
  stats, hashes. Editing a reviewed chapter makes its hash stale until reviewed.
- **Status now:** 001–007 provisionally accepted (P001–P007), none ratified.
  008 *Ba3d el sette* drafted, `arabizi_review`, waiting on the language
  reviewer. `reports/RUN_STATE.md` still says `status: running` for 008.
- **Story so far:** Jan 23 – Mar 2. Farewells (001); arrival, Rami, Inés
  (002); calls home, 3al Zawiye, Walid, Abu Nabil, double booking (003);
  tawle night, Em Jamil, Camille's dinner, Yara and the name bet (004);
  Sami bug test, Karim on the train (005); Walid says Michael's name, Yara
  pays and they exchange numbers (006); Nadine, Michael offers the café
  without asking, Walid refuses a pilot (007); interview, Rami's shelf,
  Maya's call, the page arrives late (008, unreviewed).

## 2. Story and creative problems (highest priority)

1. **The same lesson three times.** 004 (Yara), 007 (Walid) and 008
   (Nadine/Walid) all run: Michael overreaches → is called out → admits it →
   pays a small, restrained cost. EDITORIAL_DIRECTION forbids exactly this
   ("let changed behavior or a fresh cost speak").
2. **Work has turned into paperwork.** 005-S01 is a bug reproduction, 005-S02
   a support-ticket metrics exercise, 007 a pickup-order workflow, 008 a
   one-page memo with at most three questions. The stake in 008 is that a
   colleague is assigned elsewhere for one week. Karim's "political edge"
   became an argument about closed-ticket counts.
3. **Barcelona is invisible.** "Unnamed street", "unnamed train", "generic
   campus square", "unnamed printing shop". No sea, no neighborhood, no
   metro, no Catalan signage. The rule to verify real particulars has been
   read as "avoid them".
4. **Michael's stated loves are missing** after five story weeks: argileh,
   beach, church, gym, Spanish lessons, real politics/philosophy, any
   flirtation besides Yara. Yara appears only in 004 and 006.
5. **The ensemble is frozen.** Rami is offstage 003–007 (he is the
   flatmate); Inés is absent since 004; Camille and Jordi appeared once.
   Flat life, the cheapest source of daily texture, is unused.
6. **Repeated ending cadence.** Chapters close on a still object:
   002 (suitcase stays shut), 007 (`El kerse dall ma7allo`), 008
   (`El saf7a dallet 3al raff`); 006 closes on a shut door.
7. **Chapters are shrinking:** 004 2,996 → 006 1,652 → 007 1,546 words,
   below the 1,800 guide.
8. **Roadmap crunch.** Seven chapters cover Feb 1–Mar 2. Part 2 ends ~016,
   leaving ~8 chapters for 4.5 months that must hold Dalia, a first date,
   Easter/church, a Rami conflict, Inés, Sant Jordi, Salma, Marwan, a Nadine
   fight, Sant Joan, exams and departure. Re-plan or extend.
9. **Reviews check compliance, not drama.** The 007 story review made zero
   edits; its findings table checks scope limits, never whether the scene is
   interesting.

## 3. Language and spelling drift (verified counts)

| Issue | Where | Established form |
| --- | --- | --- |
| `se3a` ×6 | 008 only | `sa3a` (003–007) |
| `tnen` ×11, also in narration | 008 (one in 007) | `tnein`; `tnen` only in Lebanese mouths |
| `mumkin` ×2 | 005 (Sami), 006 | `momken` ×14 |
| Feminine past `-it` in narration: `natarit`, `fatashit`, `mshit` | 006, 007, 008 | `-et` (`de7ket`, `raja3et`, `maddet`) |
| `jughrafia` | 004 (Yara) | `ju8rafia`: breaks the 8 rule (already flagged, never fixed) |
| `akhla2` | 005 (Karim) | `a5la2`: breaks the 5 rule |
| `qarar` | 008 (Nadine's email) | she says `2arrer` in the same chapter |
| `7elwa` | 008 (Michael to Maya) | Damascene `7elwe` |
| `Werrato` (Lebanese) in narration | 006 | narration uses `farja` |
| `Zaa7` | 006 | `za77` (002) |
| Formal MSA cluster: `mo2tar7in`, `enjaz`, `ta2kid el ersal`, `moraja3a` | 005 | colloquial equivalents |

Formula repetition: `Y3tik el 3afye` / `Allah y3afik` in 5 of 8 chapters;
`Tsharrafna` closes 6 introductions; the bet's ritual phrase `ma3ak 7a2`
recurs casually ~10 times, which dilutes its payoff in 006.

The checker cannot see any of these: it matches single banned tokens only,
and the `walla shi` lexicon row can never fire.

## 4. Process and documentation problems

1. **Bloat.** About 80k words of apparatus support about 17k words of novel.
   Briefs are longer than chapters (007 brief 2,619 words for a 1,546-word
   chapter). Review files run 4–5k words. A planner packet starts with the
   14.5k-word master.
2. **Duplication against master §9 ("single ownership").** One fact (Mar 1,
   16:00, twenty minutes, no recording, book stays with Walid…) appears in
   master §4 Walid, §4 Nadine, §15 P007, four places in CURRENT_STATE, the
   ledger, ROADMAP, README, DECISIONS P007, the 008 handoff, brief 008 and
   two reports.
3. **Defensive negation lists** ("no date, exclusivity, kiss, recurring
   meeting, promised design work or guaranteed availability") fill every
   record. Brief 008 has dozens of "no X" clauses and pre-decides the outcome
   ("preferred consequence: both copies arrive late"). This is the likely root
   cause of §2: writers get compliance documents, not dramatic intent.
4. **Stale or contradictory records:**
   - README "Open questions" says no 008 brief or manuscript exists; both do.
   - ROADMAP row 008 says `brief_ready`; it is drafted.
   - Master §1 says "no fixed chapter count … or total word-count target";
     S011 sets ~34 chapters.
   - Master §10 names GPT-6.1. OVERNIGHT relies on Cursor `Task` /
     `generalPurpose`, a Grok fallback and `.cursor/hooks`, none of which run
     in Claude Code.
   - Master §12 says registry "schema version 2"; it is 3.
   - EDITORIAL_DIRECTION still carries a stale "Chapter 005 starting contract".
   - `prompts/CHAPTER_005–008_HANDOFF.md` are spent one-off files; 008's uses
     a local `/Users/...` path.
   - `RUN_STATE.md` says `running`, and every historical run is appended to it.
   - Calibration "Older baselines" duplicates the voice cards. There are no
     cards for Em Jamil, Camille or Jordi. Walid's card ("never stops
     talking") no longer matches how he is written (dry, terse).
   - CURRENT_STATE, meant as a present snapshot, carries old history
     (Feb 3–4, the 32 for the table, the past Feb 9/12 invitations).

## 5. Suggested fix order (pending user approval)

1. Decide 008: revise it against §2 before reviews continue, or re-plan it.
2. Fix the §3 drift in 004–008. Settled chapters need targeted re-review and
   new hashes; record that as a user-authorized correction.
3. Slim the apparatus. The master keeps only foundations. The state becomes a
   true one-page snapshot. Ledger entries go to ~200 words. Briefs become
   short (intent, stakes, required facts, the few real prohibitions).
   Remove the negation boilerplate, archive the handoffs, refresh the stale
   records, and make OVERNIGHT tool-neutral for Claude Code.
4. Re-plan ROADMAP 009–016 for pace, setting, ensemble and Michael's
   interests; consider allowing real public Barcelona places.
5. Extend the lexicon and checker (kh/gh digraphs, variant-pair report, the
   new rows above) and add tests.

Open questions for the user: keep the full five-role pipeline or lighten it;
Michael's UAB program (O001); whether real Barcelona places/events may be named.

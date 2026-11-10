# Chapter 001 — Original-language review

<!-- original-sha256: 1bf32f1fb8ea4df2ab289bab2d32ea6500bbc1abc967bc242de6125f93f59407 -->
<!-- original-disposition: pass -->

## Scope

Reviewed and revised Chapter 001, **Lissa shway**, in a fresh model-review
context relative to its writer. This is an editorial language/story review,
not native-speaker validation or a separate-agent review. The writer's prior
self-edit was not treated as a passing review.

- Input original SHA-256:
  `13c2d1f922ef30c762d345c953ad72e088e5a5c89922163e8217b04dcd38b226`.
- Passed revised original SHA-256:
  `1bf32f1fb8ea4df2ab289bab2d32ea6500bbc1abc967bc242de6125f93f59407`.
- Read completely: `AGENTS.md`, `README.md`,
  `prompts/CHAPTER_001_REVIEW_HANDOFF.md`, `prompts/REVIEWER.md`,
  `STORY_MASTER.md`, `development/LANGUAGE_CALIBRATION.md`,
  `memory/CHAPTERS.json`, `memory/CURRENT_STATE.md`,
  `planning/briefs/001.md`, the original chapter, and the writer's `review.md`.
  Ran the reviewer packet and checked the live branch/worktree before editing.
- Reviewed in story, language, and continuity passes; reread the complete revised
  chapter after the initial structural check, specifically checking attribution.
  Compared the original quoted words with the revised labeled passages to
  distinguish formatting changes from editorial changes.
- No accepted chapters or older accepted source scenes exist. Brief 001's
  predecessor remains null. The accepted-state records remain unchanged.

The writer had already revised the coffee-cup exchange, housing conversation,
photo setup, luggage movements, and repetition in the same writing context.
Those useful revisions were preserved rather than restarting the chapter.

## Findings

Severity describes the problem in the input revision; all findings below are
resolved in the passed revision. Scene IDs and exact input phrases locate them.

| ID | Severity / location | Evidence and reason | Correction applied |
| --- | --- | --- | --- |
| R1 | High; all scenes | Unlabeled quotation paragraphs and speech split by narration fail the explicit speaker requirement. Short turns such as `Maya.` and resumed speech need attribution too. | Added stable `**Name:**` labels to every spoken passage, repeated after narrative interruptions, and kept narration in separate paragraphs. Written messages have author labels inside blockquotes after explicit message narration. |
| R2 | Medium; 001-S01 | `2e3od wara` leaves the position underspecified; `ma byestannak ten2zo` makes the tester exchange depend on an awkward rescue formulation. | Used `2e3od warah` and `La2, bass hek ma byedall yetla33 fik kell ma ye3la2.` The suggestion is now to sit behind the tester so he stops looking to Sami at every obstacle. Sami's hiding joke and uncertain `Momken` remain. |
| R3 | Low; 001-S01 / 001-S05 | `b7kilik` addresses Sami and `e7kilik` addresses Michael, whereas the chapter's adopted masculine address forms use `-lak`. | Changed those two instances to `b7kilak` and `e7kilak`. This is local address consistency, not a claim that Arabizi has one universal vowel spelling. |
| R4 | Low; 001-S04 | `El jrawib ma 7ada 3am ye2rab 3layon` communicates the joke, but generic approaching weakens the connection to Maya reaching toward his food. | Used `El jrawib ma 7ada 3am ymedd ido 3layon.` Kept Maya's dismissive reply and the earlier sock-packing repair. Also changed `El awwal 8assel idak` to the more conversational `8assel idak bel awwal`. |
| R5 | Medium; 001-S04 | `fa talla3 Michael 3al janb` blurs the photograph's appearance with an action; later `Talla3 fiha` could refer to Maya or the photo. `3am ymayyel` is an unclear way to describe the supported phone tilting. | Described Michael as leaning sideways **in the first photo**, named the photo in his later look, and used `3am ymeel`. Made the second timer setup explicit. The candid Andrew picture remains distinct from the two group shots. |
| R6 | Medium; 001-S03 / 001-S04 | The tea reply `Michael 2al eh` is embedded speech. Andrew's photo objections and Maya's zipper instruction are also delivered through narrative summaries. | Rendered the tea offer/reply, Andrew's existing photo objections, and Maya's existing zipper instruction as short labeled turns. These supply direct wording for already narrated exchanges, without adding a new incident. |
| R7 | Low; 001-S05 | The writer queried the rhythm from `La twu3edni hek` through `Jarribni`, and whether `me2wad` fits the surrounding register. `5alli 7alak tousal` and `W law ma 3andak 5abar` are less easy here than the adjacent short replies. | Used `Enta ousal bel salame bel awwal` and `7atta law ma 3andak shi jdid...`; retained `La twu3edni hek`, `Betzha2i`, and `Jarribni`. Replaced `me2wad` with `derkisyon`; lexical support and limits are recorded below. |

## Resolution

All material findings are resolved. Formatting preserved the existing spoken
content except for the identified language edits and the short expansions of
previously summarized exchanges. Removing speech tags required ordinary
sentence punctuation; it did not change the substance of those turns.

### Attribution and written messages

The resulting chapter has **205 live spoken passages** and **two written
messages**, each attributed. Nonverbal action, Michael's unspoken thoughts,
and background calling with no quoted words remain narration.

Checked the assignments against context, including these easy-to-misassign turns:

- **001-S01:** Michael says `Deer balak 3a 7alak`; Sami replies and notices the
  coffee cup. Michael then returns the cup and makes the tester callback. The
  cup actions determine the exchange; simple alternating labels would not.
- **001-S04:** Michael gives both parts of the sock clarification, separated by
  shared laughter. Widad resumes after touching his hand. Zeina gives the
  handwashing instruction; Maya responds to the photo request; Andrew makes
  the photo objections. `Maya.` is Michael addressing his sister.
- **001-S05:** The two blockquotes are Michael writing to Maya and Maya replying,
  not live conversation with Zeina. Zeina says that she also received the photos;
  the writer handoff's attribution of that information to Maya was imprecise.
  Zeina retains her label after the intervening steering-wheel observation.

### Language evidence and limitations

For the steering-wheel word, checked the published entry
[“Wheel”, “Wheels” in Lebanese Arabic, Ithaca Bound Languages](https://www.ithacaboundlanguages.com/wheel-wheels-in-lebanese-arabic/),
which gives `Dreksyon` and examples. The chapter's `derkisyon` is a readable
editorial transliteration of that colloquial loanword. This supports the lexical
choice in a North Levantine register; it does **not** verify a specifically
Damascene pronunciation or certify the surrounding passage.

The tester and sock lines were simplified through model editorial judgment,
not declared verified regional idioms. Calibration samples were treated as
examples, not dialect authority. No native speaker read this revision. No
blocking expression-level uncertainty remains for this editorial pass; native
feedback can still refine rhythm and register later.

### Story, pacing, and continuity retained

- The three short opening snapshots differ: Sami has a software test to run,
  Fares has a game coming up, and Hassan's scene leaves room for quiet attention.
  The gathering and drive retain the chapter's greater emotional weight. The
  five short units remain one compact departure chapter, without a new subplot.
- Michael remains playful and capable. His testing offer, ambitious list,
  quick practical responses, and daily-call offer plant overcommitment lightly;
  nobody gives him a closing lesson. He stays with Hassan and offers ordinary
  help at the gathering. The cup and packing jokes remain affectionate.
- Close third-person stays with Michael: photographs are seen on phones,
  gestures are observable, and his mother's private thoughts are not asserted.
  His pause about what to tell her is unspoken thought, not unlabeled dialogue.
- Dates remain January 23, 28, 29, 30, and 31, **2027**, in SF, LA, and LAX.
  Hassan's home and Zeina's home remain separate. Maya, 23, and Andrew, 27,
  retain their established sibling roles; no new ages or family biographies
  appear. Presence at Zeina's gathering establishes no sibling/Widad residence.
- Zeina drives and drops Michael at LAX. The chapter ends as he enters the
  airport; no flight route, airline, terminal, schedule, university procedure,
  or Barcelona arrival is invented. The later itinerary remains intact.
- Read for undeclared romantic content: there is **no romance or flirting**,
  including no farewell/airport hook. The false flag and empty participant list
  are reviewer-confirmed. No excluded personal names or editorial exclusion
  metadata appear in the manuscript. Original dialogue, narrative, and headings
  remain Arabizi, with the adopted numerals and `ra7`; no Arabic script appears.
- Zeina rejects the blanket daily-call promise. The later arrival message and
  call after settling/resting are the specific agreed plan, **not** a standing
  daily schedule. The modest disagreement stays warm and partly playful.

## New provisional facts

These are draft facts and proposed future memory references only. None has been
promoted to the accepted state, ledger, coverage, or durable biography.

| Scene / date | Provisional details, knowledge, and commitments |
| --- | --- |
| 001-S01 / 2027-01-23 | Unnamed SF café; Michael and fictional Sami, 24. Sami reports a user testing his software the previous day and his own tendency to prompt the user. Michael suggests sitting behind him and offers to test a ready version during his first week away. Sami says he will report how the test goes. No employer, paid role, completed test result, or formal obligation is established. The wrong-cup joke recalls the tester conversation. |
| 001-S02 / 2027-01-28 | Unnamed LA street and parked car; Michael and fictional Fares, 22. Almonds and another walking loop are incidental. Fares mentions a group ball game next week and conditionally promises news if they win. The game and result have not occurred; no particular sport or venue is fixed. |
| 001-S03 / 2027-01-29 | Separate visit to Hassan's LA home. Michael says housing messages have been exchanged and the room is ready; he does not know the residents beyond messages. No names or existing friendship are implied. Michael and Hassan plan to talk after arrival. Hassan hands him his jacket at the door; Michael has not forgotten it. |
| 001-S04 / 2027-01-30 | Gathering at Zeina's LA home with Michael, Maya, Andrew, and Widad. Michael sends Andrew the accommodation address and a contact number, with contents off-page. Maya helps pack. An earlier candid photo of Andrew precedes Widad's requested group photo: Maya takes two timed group shots, the first awkward, the second with Widad holding Michael's hand and Zeina's hand on his shoulder. She finishes packing with Michael. Their presence does not assign residence. |
| 001-S05 / 2027-01-31 | Zeina drives through LA and drops Michael at LAX. Michael says he spoke with Hassan before leaving. Maya sends both group photos to Michael; **Zeina says** she received them too. Michael and Zeina agree on an arrival message and a call after he reaches the accommodation and rests, with reciprocal ordinary conversation rather than a daily-call promise. He enters the airport; boarding and Barcelona arrival remain unnarrated. |

## Disposition

**Pass — original-language editorial review.** The original review source hash
above is unchanged. The reviewed original originally queued a translation stage;
the user's subsequent instruction, **"I dont want an english version"**, retires
that stage. Chapter 001 now moves directly to **`ready_for_author`**.

No English manuscript has been created. Author acceptance remains null and memory
promotion false; Chapters 002 and 003 remain planned. This workflow correction
does not claim another language review or acceptance of the chapter.

At the original review increment, structural checks and 18 regression tests
passed, and the revised chapter was reread for speaker attribution. Structural
checks do not certify dialect quality or infer acceptance. See decision C005 for
the later Arabizi-only workflow migration.

**Next:** present this Arabizi original for the user's reading, corrections, or
acceptance. Do not generate an English version. After actual acceptance, follow
`prompts/ACCEPTANCE.md` to promote events and refresh the next chapter brief.

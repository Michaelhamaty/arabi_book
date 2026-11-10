# Language and voice calibration

Status: active spelling baseline and noncanonical voice samples. The user confirmed
`8 = gh; keep q for q` during setup, with `2` representing a glottal stop. Other
choices below are adopted editorial defaults that can be refined with feedback.
The examples are model-drafted, not native-reviewed or accepted manuscript events.

## Readable Arabizi contract

| Written form | Sound/production choice |
| --- | --- |
| `2` | Glottal stop. Use it when that is the sound in the intended spoken form. |
| `3` | The voiced pharyngeal sound commonly represented by this numeral in Arabizi. |
| `5` | The kh sound. Use this numeral consistently in ordinary Arabic words. |
| `7` | The voiceless pharyngeal h sound. |
| `8` | The gh sound; explicitly confirmed by the user. |
| `q` | A retained q sound; do not automatically convert every written q to a glottal stop. |
| `sh` | The sh sound. |
| `j` | The chosen Latin representation of the relevant j sound; do not introduce a second `zh` spelling mechanically. |
| `h` | Ordinary h, distinct from `7`. |
| `a e i o u` | Readable vowels; use `aa`, `ee`, `oo` where length or clarity helps. Avoid heavy diacritics. |
| Doubled consonants | Preserve meaningful doubling in readable forms, e.g. `baddi`, `kell`. |

This is a production notation, not a claim that every Arabizi writer uses the same
system. Prefer a consistent lexical spelling once established. Do not normalize
away an actual character/dialect difference to satisfy spelling uniformity.

- Future marker: **`ra7`**. Keep it as a separate word; no drift to the rejected prefix.
- Useful default spellings: `shu`, `ya3ni`, `bass`, `baddi`, `ma`, `la2`, `eh`,
  `5alas`, `3anjad`, `wa2et`, `2ahwe`, `ma3ak`, `ma3ik`. Do not insert these as quotas.
- Keep clitics/readability consistent (`ma3ak`, `3annak`, `btesma3ni`), but don't
  invent a rigid universal rule covering all dialectal constructions.
- Use familiar proper-name spellings and established common loanwords as needed;
  a loanword such as `laptop` is not an English-dialogue exception.
- Use normal Latin punctuation, ellipses for hesitation when warranted, and a
  dash for a real interruption. Avoid constantly marking every breath.
- Every spoken passage begins with `**Name:**`; repeat it in each dialogue
  paragraph, even for consecutive passages by the same speaker separated by
  narration. Keep narration separate; unlabeled quotation paragraphs do not
  satisfy the user's format. Preserve this convention in the Arabizi print edition.
- Dialogue labels use stable names. Scene headings use the chapter/scene ID and
  an Arabizi title. Original narration is also Arabizi.
- Do not introduce Arabic-script text into the original. Editorial phonetic
  explanation belongs here or in review notes, outside the reader's flow.

## Spelling table (C006)

For evidence of how the spelling, voice, and texture changes improved 001–003,
and how 004 applied them, read `development/EDITORIAL_DIRECTION.md` (C009).
Its examples are evidence to learn from, not dialogue to reuse in a new chapter.

`story.py check` rejects the variants in `development/LEXICON.tsv`. The table
below is the readable summary; extend both together.

| Use | Not | Notes |
| --- | --- | --- |
| `lamma` | lama | "when" |
| `enno`, `enni`, `ennak`, `ennik`, `enna`, `ennon` | eno | "that" + pronoun |
| `kent`, `kenti` | kont | "I was / you were" |
| `talla3` / `ytalle3` / `talle3!` | tla33, yetla33 | look at; past / present / imperative |
| `de7ek`, `de7ket`, `de7ko`, `yed7ak` | da7ak | laugh |
| `hazz`, `laff`, `8assal` (past) | hezz, leff | `8assel!` is the imperative |
| `inshalla` | inshallah, nshallah | one spelling |
| `wala shi` (nothing) | walla shi | `walla` alone means "or"; `wallah` is the oath |
| `ebri2` (teapot), `berrad` (fridge) | | not interchangeable |
| `jarrar` / `dorj` (drawer) | drawer | no English nouns in narration |
| `telefon`, `laptop`, `bus`, `metro` | telephone | established loans are fine |
| `ma3ik`, `3andik`, `shantik` | ma3ek | feminine "you" ends in `-ik` |
| `wejh`, `wejho`, `wejhak` | wejjak | |
| `jakeit` | jacket | loanword spelled as spoken |
| `leish` (Damascene), `lesh` (Lebanese) | leh | "why" |
| `kerse` is masculine | kerse fadye | `kerse fadi`, `el kerse el kbir` |

Family address: Michael calls his parents `mama` and `baba`. Hassan calls
Michael `baba` and `ya 3ein baba`; Widad says `ya t2berni` and `ya 3omri`.

## Voice cards (S010)

A reader should be able to cover the label and still guess most speakers.

| Speaker | Dialect markers | Individual voice |
| --- | --- | --- |
| Michael (21) | Damascene: `hada/hay/hadol`, `mu`, `iza`, `ya3ni`, `lissa`, `shu`, `halla2`, `ya zalame` with friends | Warm, quick, a joker who deflects with humor, says yes too fast. Precise when he is working. |
| Hassan | Damascene, slower | Few words, tea as a language, teasing without smiling, `baba` to his son. Does not pry; asks one exact question. |
| Zeina | Damascene | Loving, sharp, practical, catches Michael's evasions, turns the question back on him (`w emta btedros?`). |
| Maya (23) | Damascene, fast | Sibling insults as love (`ya 7mar`, `ya 2abaday`), mocks his packing and his face, runs the photos. |
| Andrew (27) | Damascene | Plans and deadlines, dry big-brother lines (`Barcelona mu Moscow`), softens only at the end. |
| Widad (teta) | Damascene, old-fashioned | Blessings and prayers, `ya t2berni`, food as a measure of love, sly humor. |
| Rami (23) | Damascene, compressed | Sarcasm, quick profanity (`yel3an abu...`, `ya 7mar`, `5ara`), kitchen-shift fatigue, generous under the jokes. |
| Inés (24) | Plain, direct, no regional flourishes | Deadpan, crude when annoyed, no endearments, threats as jokes (`bedba7ak`), works too much. |
| Walid (47) | Beiruti Christian: `hayda/hayde/hawde`, `mesh`, `eza`, `ya3ne`, `ba3d` (still), `bonjour`, `merci`, `ya 3ammo`, `ya 3adra` | Dry, nosy, theatrical about his café and his machine, never stops talking, kind by accident. |
| Abu Nabil (~70) | Old Damascene: `walak`, `ya ebni`, `ba2a`, `ya 7aram`, tawle vocabulary (`shesh besh`, `habbyek`, `mars`) | Trash-talking backgammon player, proud, tells stories that may be lies, mocks Walid constantly. |
| Fares (22) | Lebanese-American family: `hayda`, `mesh`, `eza`, `ba2a`, `ya 7ayawan` | Teasing, listens more than he lets on, competitive about his games. |
| Sami (24) | Damascene, SF tech life | Self-mocking founder energy, catastrophizes then laughs, `5arabli bayti`. |
| Yara (22) | Beiruti: `hayda`, `mesh`, `eza`, `ya3ne`, `bta3ref shu`, `5alas`, French/English flecks a Beiruti would use | Tests people, laughs at pretension, serious about her work, can be cutting and tender in the same minute. |
| Dalia (35) | Beiruti, fiery | Open flirtation, direct questions, enjoys making people blush, not interested in long explanations. |
| Nadine (42) | Damascene professional | Exact, impatient with vagueness, rare warmth that counts. |
| Salma (26) | Damascene, measured | Quiet at first, very funny once comfortable, challenges Michael's easy charm. |
| Karim (24) | Palestinian-Jordanian urban speech: `hada`, `mish`, `eish`/`shu`, `ya zalame` | Political edge, argues for fun, loyal. |
| Tarek (26) | Lebanese (regional profile chosen before his first scene) | Civil engineer in Lebanon, hospitable and funny, weighing a job abroad; a mirror for Michael's wish to stay. |
| Camille / other non-Arab characters | Plain, fluent Arabic under the universal convention | Distinguish by personality and subject, not by fake accents. |

These cards are adopted editorial choices (S010), not claims of native
validation. Refine them from settled chapters.

## Texture palette

Use these as a menu that suits the speaker and moment, not a checklist.

- **Greetings and replies:** `ahlan w sahlan` / `ahlan fik`; `saba7 el 5er` /
  `saba7 el nour`; `y3tik el 3afye` / `Allah y3afik`; `sa7tein` /
  `3a 2albak`; `tislam idak` / `w idak`; `ma3 el salame`; `Allah ma3ak`.
- **Oaths and exclamations:** `wallah`, `wallahi`, `w 7yetik`, `ya 7aram`,
  `ya 3adra` (Christian Lebanese), `yi`, `ya allah`, `tfeh`, `ya latif`,
  `ya ribbi`, `shu hal 7aki?`.
- **Love and blessing:** `ya 3omri`, `ya 2albi`, `ya t2berni`, `ya 3ein baba`,
  `Allah y5allik`, `Allah ywaff2ak`, `Allah yer7amo`.
- **Insults and sarcasm:** `ya 7mar`, `ya 7ayawan`, `ya 8abi`, `yel3an abu...`,
  `5ara`, `kezzab`, `ya 2abaday`, `tayyeb ya shater`, `mbayyan`.
- **Fillers and pivots:** `ya3ni` / `ya3ne`, `ba2a`, `5alas`, `yalla`, `tayyeb`,
  `ma32oul?`, `3anjad?`, `walaw`, `ma fi mushkle`.
- **Tawle:** `shesh besh`, `dabsh`, `habbyek`, `mars`, `yalla 2allib`,
  `3am tensok el zahr`.

Expressions should reveal the speaker. A proverb from Abu Nabil lands; the
same proverb from Inés would be strange.

## Older baselines

| Speaker/group | Baseline | What changes with relationship or pressure |
| --- | --- | --- |
| Michael | Damascene; warm, curious, playful, composed. | Brevity and precision professionally; affectionate familiarity with family; less fluent emotional certainty when vulnerable. |
| Nadine | Damascene with clear professional vocabulary. | Precise questions, brief impatience, selective warmth and wit. |
| Yara | Urban Beiruti Lebanese working profile. | Playful testing, professional focus, warmth, caution, tenderness, anger: several registers. |
| Walid / Dalia | Urban Lebanese baselines, distinct age/professional lives. | Walid's dry observation differs from Dalia's overt flirtatious challenge. |
| Salma | Damascene, measured initially. | More animated with trusted people or a subject she knows well. |

## Noncanonical original-language samples

These are independent calibration exchanges, not chapter extracts. Family samples
contain no romance. All flirtation samples are explicitly set **after Barcelona
arrival**, with the adult ages given. Do not add these events or exact lines to
memory automatically. No English reading version is produced.

### A — Family teasing: Michael, 21; Maya, 23

**Maya:** Ya3ni ra7 tsafer w tetzakkarna bass lamma y5rab ma3ak el laptop?

**Michael:** La2, hay el marra ra7 ettesel 2abel ma y5rab.

**Maya:** Eh, hek a7san. N7na kamen 3anna 7ayatna, ya 7mar, mu 3am nestanna telefonak.

**Michael:** Shayfe? Lissa ma safart w ballashti teshta2ili.

**Maya:** La tet7ammas ktir. 3am eshta2 lal hdou2.

### B — Practical boundary: Nadine, 42; Michael, 21

**Nadine:** 2addesh baddak wa2et? Bass la t2elli bokra iza mu ra7 tel7a2.

**Michael:** Iza baddik shi mazbut, lazem a5od wa2ti. Fini eb3atlik el awwal el 5amis.

**Nadine:** Tayyeb. W iza sar ma3ak shi, 7kini 2abel, mu ba3d.

**Michael:** Ma3ik 7a2. Bass lazem nettefe2 men halla2 shu da5el bel sho8ol w shu la2.

### C — Lebanese playfulness: Yara, 22; Michael, 21; Barcelona

**Yara:** Enta dayman hek m2akkad men 7alak?

**Michael:** La2. Bass ma3ik 3am jarrib bayyen hek.

**Yara:** Eh, mbayyan enno 3am tjarreb.

**Michael:** Ya3ni ma zabetet?

**Yara:** Ma 2elet hek. Bass la tet3awwad esma3ak shi 7elo kell marra.

### D — Open flirtation: Dalia, 35; Michael, 21; Barcelona

**Dalia:** Shu, ra7 tdall wa2ef hon walla ra7 te3zemne 3a 2ahwe?

**Michael:** Enti dayman bte5tasre el mawdu3 hek?

**Dalia:** Lamma ykoun el mawdu3 sahl, eh.

**Michael:** Tayyeb, 2ahwe. Bass ba3den dori es2al.

**Dalia:** Es2al. Bass ma bwa3dak jaweb 3a kell shi.

### E — Quiet exchange: Salma, 26; Michael, 21; Barcelona

**Michael:** Iza baddik te23odi la7alik, 2ulili. Ma ra7 ez3al.

**Salma:** La2, mu hek. Bass baddi shway la et3awwad 3al 3alam.

**Michael:** Ma fi 3aj2a. Neshrob el 2ahwe w neshuf.

**Salma:** Tayyeb. Bass enta shaklak ma bteskot ktir.

**Michael:** 7asab ma3 min.

### F — Rough friendship and an actual limit: Rami, 23; Michael, 21; Barcelona

**Rami:** Shu hal 5ara? 2eltellak ma t7ki 3anni w ana mu mawjud.

**Michael:** Ma 7kit shi 3annak. Sa2alni iza ra7 tiji, 2eltello ma ba3ref.

**Rami:** Ana sma3et 8er hek.

**Michael:** Tayyeb, esma3 minni kamen. W iza baddak netfe2 3a shi, netfe2. Bass ma tethemni 2abel ma tesma3ni.

This last sample deliberately leaves disagreement unresolved. It is an example
of intended range, not a scheduled conflict or a rule that both people are right.



## Editorial uncertainty and improvement

- All samples need an ear-based naturalness pass during real review; the city
  labels and spelling consistency do not prove regional authenticity.
- Watch long responses in B/F: they should not become the default way everyone
  explains a boundary. In real scenes, action, interruptions, and shorter replies
  may convey the same intent better.
- The bold/shy contrasts are starting points, not recurring scripts. Dalia can be
  uninterested; Salma can challenge Michael; Yara has much more to say than flirtation.
- The specific profanity and severity should be checked in the intended relationship.
  Keep crude speech where it works instead of adding a fixed number of bad words.
- Add accepted corrections and source scene references here as actual chapter
  voices develop. Do not silently turn sample wording into permanent canon.

Samples were corrected to the C006 spelling baseline on 2026-11-10. They are
still not chapter text: never paste them into the manuscript.

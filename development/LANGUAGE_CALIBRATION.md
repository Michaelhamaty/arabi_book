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
| `sa3a` (hour, clock) | se3a | `sa3to`, `sa3tein` |
| `momken` | mumkin | |
| `tnein` (two) | | Damascene speech and narration; Lebanese speakers may say `tnen` |
| Narration feminine past `-et`: `de7ket`, `raja3et`, `nataret`, `fattashet`, `mashet` | natarit, fatashit, mshit | `-it` is Lebanese; keep it out of Damascene narration |
| `7elwe` | 7elwa | Damascene and Beiruti both end in `-e` |
| `za77` (shifted) | zaa7 | |
| `5` and `8`, never `kh` / `gh` | akhla2, jughrafia | `a5la2`, `ju8rafia`; names (Michael) excepted |
| `farja` (show) in narration | werra | `werra` is Lebanese; fine in Walid's or Yara's mouth |

Family address: Michael calls his parents `mama` and `baba`. Hassan calls
Michael `baba` and `ya 3ein baba`; Widad says `ya t2berni` and `ya 3omri`.

## Voice cards (S010, refreshed under C010)

A reader should be able to cover the label and still guess most speakers.

| Speaker | Dialect markers | Individual voice |
| --- | --- | --- |
| Michael (21) | Damascene: `hada/hay/hadol`, `mu`, `iza`, `ya3ni`, `lissa`, `shu`, `halla2`, `ya zalame` with friends | Warm, quick, a joker who deflects with humor, says yes too fast (`Ana jey`, `akid`). Precise when working. |
| Hassan | Damascene, slower | Few words, tea as a language, teasing without smiling, `baba` to his son. Asks one exact question. |
| Zeina | Damascene | Loving, sharp, practical; catches evasions, turns the question back (`w emta btedros?`). |
| Maya (23) | Damascene, fast | Sibling insults as love (`ya 7mar`, `ya 2abaday`), roasts him by text, has her own mornings. Fast and theatrical in a fight; quotes the parents as law (`Mama 3amle 2anoun`); refuses to be managed (`Ana mu hada.`) (017). |
| Andrew (27) | Damascene | Plans and deadlines, dry big-brother lines (`Barcelona mu Moscow`), softens late. Renames plans to defend them (`Ana mu 3amel 5otta. Ana 3amel 7ajz.`); concedes narrowly (`3an hay bass.`); the worry shows in one plain line (017). |
| Widad (teta) | Damascene, old-fashioned | Blessings and prayers, `ya t2berni`, food as love, sly humor. |
| Rami (23) | Damascene (el Sha8our), compressed | Sarcasm, quick profanity (`yel3an abu…`, `5ara`, `ya 7mar`), kitchen-shift fatigue, neighborhood pride, generous under the jokes. |
| Inés (24) | Plain, direct, no regional flourishes | Deadpan, crude when annoyed or hungry (`Ana mu mo7tarame. Ana ju3ane.`), no endearments, threats as jokes (`bedba7ak`), edits ruthlessly. |
| Walid (47) | Beiruti Christian: `hayda/hayde/hawde`, `mesh`, `eza`, `ya3ne`, `ba3d`, `bonjour`, `merci`, `ya 3ammo`, `ya 3adra`, `tablier` | Theatrical in short bursts, dry, proud, exact about his own café; turns complaints into performances; goes quiet when something lands. Hands a duty over in two words (`Kelmte, w idak.`); one plain line about his name (`Esme mesh fraata b jeibtak.`) (018). |
| Abu Nabil (~70) | Old Damascene (el Midan): `walak`, `ya ebni`, `ba2a`, `ya 7aram`, tawle vocabulary | Trash-talker, invents laws "from my grandfather's days", corrects other people's stories from his corner (`3am sa77e7`). Self-mocking entrances (`Ana 3ajouz walla 3arous?`); tawle insults by comparison (`metl el Swisri`); proud refusals (`Nzelt la7ali, w betla3 la7ali.`) (018). Says a want plainly once, with no law (`Ma baddi 5alles.`); farewells as insults (`W la terja3 Lebnani. Wa7ad b hal ma7all bikaffi.`) (019). |
| Em Jamil (~68) | General Syrian (Homs per Abu Nabil); no invented Homsi phonetics | Very few words; blessings and endearments as weapons (`Allah ysam7o`, `Mars. Sa7tein.`). |
| Fares (22) | Lebanese-American family: `hayda`, `mesh`, `eza`, `ba2a`, `ya 7ayawan` | Teasing, listens more than he lets on, competitive. |
| Sami (24) | Damascene, SF tech life | Self-mocking founder, catastrophizes then laughs, `5arabli bayti`. Under real failure: laughs high from no sleep (`Hay de7ket wa7ad ma nam.`), then owns it flatly (`Hay sharikti`) (017). |
| Yara (22) | Beiruti: `hayda`, `mesh`, `eza`, `ya3ne`, `lesh`, `hniik`, `bta3ref shu`, French flecks (`bref`, `merci`) | Tests people, laughs at pretension, serious about her work, cutting and tender in the same minute. Sets terms as conditionals (`Eza baddak wa3d, ma fi wa3d.`); closes a subject in two words (`Hayde ila.`); hurt and fair in one line (`Ma 7abbet esma3a, w 7abbet enno sme3ta menak.`) (019). |
| Camille (22) | Plain, fluent, exclamatory | `Ya allah!`, `Kezzab!`; hosts by feeding; delighted rather than offended. |
| Jordi (27) | Plain, fluent | Earnest contrarian for pleasure; Catalunya not Spain; `Ma3 el 7a2. Kell marra 3and wa7ad.` |
| Nadine (42) | Damascene professional | Exact, impatient with vagueness; warmth arrives sideways (her mother at the window). Gives a verdict as people, not figures; hands the floor over by name (`Marwan. El 7sab ilak. 7kih enta.`); a one-word conclusion (`Idak.`) (019). |
| Karim (24) | Palestinian-Jordanian urban: `hada`, `mish`, `eish`/`shu`, `3ashan`, `zay`, `ahlein`, `ya zalame`, `2ult`, `shuft`, `kasse`, `sitti`/`sido`, `fi 3amman` | Political edge, argues for fun, sarcastic corporate quoting (reads HR Arabic aloud like airport announcements: `3azizi`, `tamma mal2uh`), loyal; profane with friends (`Kol 5ara`, `ya jaban`); concedes with `Momken` (015). |
| Dalia (35) | Beiruti, fiery: `hayda/hayde`, `ya3ne`, `eza`, `ken`, English flecks (`student`, `ok`) | `7ayete` to everyone, which makes it mean nothing; imperatives and deadlines (`Tlat kelmat.`); turns complaints into guests; flirts openly, then leaves mid-sentence for someone more useful (010). Teases with pretexts and money (`Ya3ne student w byes2al 2addesh.`); one plain name lands harder than any `7ayete`; loud when outplayed (`Hayde 7arakte ana!`) (017). Pays first and in front of a witness (`Enta shahed.`); turns a question back (`Hayda so2alak lal 8arib?`); sets terms in a sentence (`Ana el leile.`) (018). |
| Pilar (59) | Plain Arabic, no regional flourishes | Prices and minutes; asks each regular the follow-up to yesterday; sardonic one-liners (`El forn mzakkar. Hiye la2.`); never asks for help; furious before she is generous (010). |
| Marwan (~50) | Damascene (Bab Touma) polished by fifteen years of Dubai hotels: `hada`, `ya 7abibi` to everyone, `Tante`, `sarli … 3am`, English business flecks (`concept`, `delivery`, `stock`) | Soft voice that never rises; argues in seats, customers, hours and rent; charming and often right; casts himself as the villain with the spreadsheet; laughs from the belly when outplayed; a conclusion, not a compliment (`Halla2 3reft enta ma3 min.`) (011). Counts against his own case and says so; an ultimatum in the same soft voice (`Ya ana wara hal bar, ya ana masari b hal 7et.`) (019). |
| Odette (~76) | Beiruti Maronite: `hayda/hayde`, `mesh`, `ya3ne`, `Mn3ayyed`, `ya 3adra`, `ya 7aram`, French (`chéri`) | Commands as questions (`… mesh hek?`); counts out loud (eggs, years, grandchildren); feeds to win; asks whether women are married; runs the table without raising her voice (011). |
| Abouna Elias (~58) | Educated general Syrian (el Lazi2iyye; no coastal phonetics): `hada`, `ya 3azizi`, `ya 2albi` (to his wife), English tech words borrowed from Michael (`algorithm`, `bug`) | Quick, busy, funny; clocks everything (`3andak tlat da2aye2`); quotes (Augustine) and then mocks himself; deadpan about fasting (`Ana sayem, mu mayyet`); argues, never preaches (011). |
| Em Nicola (old) | General Syrian (el Wadi): `hay`, `mu`, `Idayyi` | Interrogates strangers; short, balanced verdicts (`Hay mu jawab. Hay jawazein.`); takes an arm without asking (011). |
| Salma (26) | Damascene (el Mezze), measured: `mu`, `hay/hada`, `la2enno`, `B shart` | One-word answers to strangers; a single dry line ends an argument; forceful on her subject (sand, coasts); sets conditions (`Kell shart fa7s`); names Michael's charm (`Hay shi byeshte8el. Hada el 3atel.`); laughs rarely and whole (015). |
| Tarek (26) | Lebanese (choose region before his first scene) | Civil engineer, hospitable and funny, weighing a job abroad. |

These cards are adopted editorial choices, not native validation. Refine them
from settled chapters.

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
- **Church (Orthodox, S018):** `el 3id el kbir` (Pascha), `El Masi7 2am!` /
  `7a22an 2am!`, `Abouna`. Use only where a scene earns it.
- **Tawle:** `shesh besh`, `dabsh`, `habbyek`, `mars`, `yalla 2allib`,
  `3am tensok el zahr`.

Expressions should reveal the speaker. A proverb from Abu Nabil lands; the
same proverb from Inés would be strange.

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

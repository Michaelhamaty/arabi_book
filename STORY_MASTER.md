# Levantine Arabic Novel — Master Story and Agent Reference

> Read this file before planning, drafting, reviewing, translating, or updating this project. It is the single reference for the project's accepted requirements, working creative direction, and production architecture. It is editorial material, not part of the reader-facing book.

## 0. Quick orientation and source authority

### What we are making

A substantial, dialogue-focused, contemporary ensemble novel following a fictionalized Michael through San Francisco and Los Angeles goodbyes, study and life in Barcelona, a summer in Lebanon, and a return to Barcelona. The entire story takes place in **2027**. The original narrative is composed directly in natural spoken Levantine Arabic, written in Latin transliteration/Arabizi. The user now explicitly wants **no English version**; the book is Arabizi only.

Michael already understands the rules of spoken Levantine Arabic. The purpose is sustained exposure to real conversational language that he can read aloud and internalize: sounds, idioms, responses, emotional registers, and spontaneous social exchanges. The story must remain engaging on its own merits. Plot and relationships should make the conversations worth reading.

### Source priority

1. The user's latest explicit instructions and corrections.
2. Confirmed user requirements recorded in this file.
3. Accepted creative decisions and accepted manuscript events, each with provenance.
4. Working proposals recorded here or in a chapter brief.
5. Earlier assistant suggestions, which have no independent authority.

If an accepted manuscript contradicts a user-established personal fact, flag the contradiction and propose a correction. Do not silently rewrite the personal fact to fit the manuscript. A new user correction supersedes an older one; update this reference accordingly.

Sources reviewed for this reference:

- ChatGPT conversation **Levantine Dialogue Story Development**, ID `6aed7ac1-d834-83e8-bcad-48dded8b23fd`; both available exchanges were read.
- ChatGPT conversation **Story Development Plan**, ID `6af24245-9ea4-83e8-a01a-6e066332d5f7`; the available exchange was read.
- User attachment **Levantine Arabic Novel — Creative Development and Agent Architecture**.
- The user's subsequent corrections about locations, family, language, predeparture romance, romantic variety, prohibited names, and the year 2027.

This reference is intended to let future agents work without rereading those chats. Retrieve the sources only if a consequential ambiguity cannot be resolved here.

### Status vocabulary

| Status | Meaning | May an agent treat it as an event that happened? |
| --- | --- | --- |
| **CONFIRMED** | An explicit user requirement, fact, or accepted creative direction. | Only if it describes an existing fact; a requirement about a future event is not an occurrence. |
| **WORKING** | A recommended fictional design, cast detail, scene, or future direction. It may evolve during development. | No. |
| **ADOPTED** | An operational or fictional default selected under the user's delegated development authority. It is the current baseline, reversible before acceptance; not a separately user-supplied fact. | No, unless later established in an accepted chapter. |
| **MANUSCRIPT** | An event established in an accepted chapter, with chapter and scene reference. | Yes, subject to later explicit corrections. |
| **OPEN** | A consequential detail not yet established. | No. |
| **RETIRED** | Superseded or rejected material. | No; exclude it from ordinary writing packets. |

An accepted plan and an event that has happened are different things. A character's claim, fear, accusation, lie, interpretation, or joke must retain that attribution in memory.

### Current production state

- This file holds foundations. It does not track chapter progress. Live
  status: `memory/CHAPTERS.json`. Settled story: `memory/CURRENT_STATE.md`
  (snapshot) and `memory/STORY_LEDGER.md` (per chapter).
- Book shape and ending: `planning/ROADMAP.md`. Editorial lessons:
  `development/EDITORIAL_DIRECTION.md`. Latest audit:
  `reports/2026-11-11-project-audit.md`.
- Working title: **Bayn Balad w Balad**, with the English gloss **Between One
  Country and Another**. The title is not finalized.

## 1. Non-negotiable story and language requirements

### Story form

- Follow Michael, a **21-year-old Syrian-American** young man, through the 2027 itinerary in Section 2.
- Use chapters, but impose no fixed chapter count, minimum length, maximum length, or total word-count target. (The user later delegated book length, C008; the adopted working shape is in `planning/ROADMAP.md`.)
- **Latest user preference: shorter chapters.** Use one or two substantial scenes as the usual chapter shape, ending at a useful emotional or social turn. Additional very short scenelets are fine. Divide a long sequence at a natural break rather than stretching every chapter. Preserve the compact departure as one chapter with brief snapshots.
- The novel should be substantial; its length should grow from worthwhile scenes, relationships, and consequences.
- Make dialogue the dominant reading experience. Contextual paragraphs before, between, and after conversations are welcome for setting, action, emotional texture, and transitions.
- Do not turn the book into disconnected language exercises, vocabulary demonstrations, or a sequence of perfectly resolved social problems.
- Let recurring characters have goals, relationships, work, responsibilities, histories, and conflicts independent of Michael.
- Allow humor, affection, ordinary pleasure, and quiet scenes alongside conflict and difficult choices.
- Develop different age dynamics and conversations across genders, cultures, social circles, and professional settings.
- Characters may be unreasonable, mistaken, offensive, contradictory, funny, affectionate, or unable to resolve a disagreement.
- New characters are encouraged when they strengthen the story. Introduce them gradually and give them memorable purposes rather than inflating the cast indiscriminately.

### Language and reading edition

- Compose the **original dialogue and original narrative directly in Levantine Arabizi**. Do not first write English dialogue and translate it.
- Prioritize **Damascene/Syrian and Lebanese** speech. Palestinian and Jordanian variation belongs where a character's background supports it.
- Every character speaks Arabic in this fictional world, regardless of nationality. This convention requires no in-story explanation.
- Use Latin letters and the numerals **`3`, `7`, `5`, `8`, and `2`**, following `development/LANGUAGE_CALIBRATION.md`. The user confirmed **`8 = gh`, `q` for a retained q, and `2` for a glottal stop** during setup. Other spelling choices are editorial defaults, not claims about a universal Arabizi standard.
- Honor the user's explicit preference for **`ra7` rather than `7a`** for the future marker.
- Do not use Arabic script in the original manuscript or its reader-facing headings.
- Preserve contractions, fragments, hesitation, repetition, interruptions, slang, discourse markers, jokes, and conversational compression where natural.
- Sophisticated political, philosophical, emotional, and business conversations should retain their complexity.
- Include offensive remarks, profanity, crude humor, and insults when appropriate to the speaker and situation. Do not sanitize adult life or insert swearing mechanically.
- Cover affectionate, caring, romantic, sarcastic, angry, frustrated, respectful, and confrontational ways of speaking, including phrases that change meaning with delivery and relationship.
- **Do not produce an English version, companion, chapter translation, or parallel-text edition.** This latest user correction supersedes earlier translation plans. English editorial planning/instructions are still allowed.
- After the original Arabizi passes review, present it directly to the user for acceptance.
- **Speaker labels are required before every spoken passage**, using `**Name:** speech` in the Arabizi manuscript and printable book. Repeat the name at every new dialogue paragraph, including when the same person resumes after narration. Put narration in separate paragraphs instead of leaving unlabeled speech embedded in it. Clearly distinguish messages/written quotations from live speech while retaining their author attribution.

### Romance and age rules

- **No romance or flirting subplot before Michael reaches Barcelona.** This includes old romantic interests, romantic flashbacks, farewell romantic tension, airport flirtation, and a romantic hook during the departure sequence.
- Michael has **one main romantic interest**. **Yara** is the current working lead for that role.
- Michael also talks to and flirts with other women of different ages and personalities. The user's specific contrasts include a fiery, very openly flirtatious woman and a shy woman.
- **Every woman involved in flirting, dating, or romantic/sexual interest is strictly older than 19: age 20 or above at the time of the interaction.** Being 19 does not satisfy this requirement. Give recurring romantic/flirtation characters explicit adult ages.
- Other flirtations should have believable variation in initiative, reciprocity, interest, rejection, awkwardness, and emotional significance.
- A woman's shyness does not establish attraction or consent. A very flirtatious manner does not promise a relationship.
- Keep each woman's independent life and choices visible. Not every woman Michael meets becomes romantically available.
- Interest in Yara does not automatically establish an exclusive relationship. Track whether exclusivity has actually been discussed and agreed. Later behavior must reflect whatever promises the characters have made, with consequences if they break them.
- Do not predetermine marriage, a permanent breakup, cheating, a love triangle, or an eventual partner.
- Work, learning, business, politics, friendship, and family remain major parts of Michael's life. Romance is important but does not consume every arc.

### Excluded personal-name family — editorial enforcement metadata only

The user's prohibited base name is **`Gaby`**. Exclude it and similar spelling or phonetic forms, including **`Gabi`, `Gabby`, and `Gabbi`**, from all manuscript, translation, title, dedication, background-signage, and dialogue content. Avoid corresponding longer personal-name forms such as **`Gabriel`, `Gabrielle`, and `Gabriella`** as well. This is a personal-name exclusion, not a ban on arbitrary letter sequences within unrelated words.

The names in this paragraph are administrative matching metadata only and must never be exported into the book. The previously proposed café-owner name is retired. **Use Walid as the replacement café-owner name throughout working story material.** Do not revive an excluded name through a surname, nickname, cameo, passing reference, or fictional business name. If a new proposed name is an obvious near-match, choose a clearly different name without asking the user to adjudicate it.

## 2. Calendar, geography, and established personal facts

### The 2027 itinerary — CONFIRMED

| Story period | Location | Required progression |
| --- | --- | --- |
| Before February 1, 2027 | San Francisco and Los Angeles | Michael says goodbye to friends in both cities and spends time with family. Keep this opening compact. |
| Departure before the Barcelona stay | Los Angeles / LAX | **Zeina takes Michael to LAX** for his departure to Barcelona. Exact flight date, route, and arrival details remain open. |
| February 1–July 15, 2027 | Barcelona | Michael attends **Universitat Autònoma de Barcelona (UAB)** and builds his life in and around the city. |
| July 16–September 15, 2027 | Lebanon | Michael spends the summer in Beirut and other parts of Lebanon, with friendships, study, outings, travel, and adventures. |
| September 16–the remainder of 2027 | Barcelona | Michael returns. The story explores changed relationships, circumstances, and commitments after the summer. |

- Keep all narrated story events within 2027. Characters may discuss earlier experiences, but pre-Barcelona romance remains excluded from the opening.
- Do not attach weekdays to dates until checked against the 2027 calendar.
- The year is fixed; birthdays have not been assigned. Do not invent a birthday or age change merely because the calendar advances.
- Michael's UAB subject/program is awaiting user input; department, official course schedule, neighborhood, exact commute, and employment arrangement remain open. A fictional shared-flat setup with Rami and Inés is adopted in Section 15; it is not a claim about actual housing.
- UAB must not be silently replaced by a different Barcelona university.
- Verify consequential real-world particulars before presenting them as facts: campus procedures, routes, named venues, opening hours, historical/political events, or employment and travel rules.
- Do not convert forecasts or invented future news into factual 2027 history. Any deliberately invented public event must be identified as fictional in editorial records.

### Michael's family — CONFIRMED

| Person | Established relationship and facts | Portrayal constraints |
| --- | --- | --- |
| **Hassan** | Michael's father. He and Zeina live in separate homes. The parents are loving. | Preserve affection; the separate homes do not establish hostility, a legal marital status, or a cause for the arrangement. |
| **Zeina** | Michael's mother. Lives separately from Hassan. Loving. Takes Michael to LAX. | Give the airport departure a natural mother-son center without inventing a family crisis. |
| **Maya, 23** | Michael's sister. They are like best friends and laugh a lot together. | Show shared humor, easy familiarity, affection, and mutual recognition. Do not make her merely an adviser or expositional sibling. |
| **Andrew, 27** | Michael's older brother. Caring, more exacting/protective, and somewhat of a father figure to Michael. | He may ask practical questions or hold Michael accountable. Do not automatically turn this into authoritarian control or antagonism. |
| **Widad** | Michael's teta. Loving, supportive, and endlessly affectionate. | Her love should feel personal and lived-in; avoid generic grandmother speeches or an invented tragedy. |

Important residence distinction: **Hassan and Zeina have separate homes.** The user has not established which household Michael primarily stays in, where Maya or Andrew live, or whether Widad lives with either parent. Being present in a scene does not establish co-residence. A family gathering may bring people together, but it must not imply that both parents share a home.

Still open: the parents' and Widad's ages, their precise speech habits and biographies, sibling occupations, and the identities of actual SF/LA friends. Sami and Fares are adopted fictional farewell friends (Section 15), without presenting their biographies as facts about real acquaintances.

### Michael's established personality, interests, and aspirations

Michael is confident, charming, handsome, physically fit, ambitious, socially curious, playful, kind, and calmly assertive. His intended manner is soft but authoritative: he can set a boundary, negotiate, or disagree while speaking calmly. He smiles and enjoys well-timed jokes. Calm delivery does not mean absence of anger, uncertainty, or emotion.

He enjoys:

- Meeting strangers, asking where people are from, hearing introductions, and asking follow-up questions.
- Forming different social circles and meaningful relationships with men and women of different ages.
- Beaches, cafés, argileh/hookah, spontaneous outings, new places, and becoming a recognized café regular.
- Going to church alone and speaking with people there.
- Technology, research, business, entrepreneurship, companies, and what people are building.
- Political and philosophical conversation, including strong opinions and genuine disagreement.
- Learning, languages, travel, friendship, attraction, flirting, and romance.
- Giving advice to peers, learning from older people, listening to complaints, and understanding consequences.

His aspirations include proficiency in Spanish and Arabic, meaningful work in technology/business, opening a café, travel, possibly living in Lebanon or Syria, and eventually having a family and children. These are interests and aspirations, not promises about the ending.

Spanish learning can be discussed in Arabic. All spoken dialogue still follows the Arabic-only fictional convention; there is no automatic exception for foreign characters or language-learning scenes.

### Accepted growth direction — CONFIRMED

The user accepted **enthusiasm leading to overcommitment** as Michael's principal blind spot. He is capable and interested in people, so he sometimes offers help, makes introductions, accepts invitations, or assumes he can fulfill several obligations at once. Consequences should emerge from specific promises and limited time, not from suddenly making him incompetent.

A secondary accepted direction is his tendency to move toward reassurance or problem-solving before he has listened long enough. Develop this with restraint. His caring and calm assertiveness remain strengths; other characters need not always agree with him or accept his proposed solution.

Possible expressions, still WORKING: a joke goes too far; confidence reads as arrogance to someone; he mistakes ease of conversation for mutual understanding; a professional promise conflicts with a personal one. These are available possibilities, not scheduled events or diagnoses of the real Michael.

## 3. Narrative vision and storytelling method

### The central question — WORKING

**How does Michael build a life that contains his ambitions, his freedom, and people he genuinely cares about?**

The year should explore the difference between first contact and a sustained relationship through actual experiences: becoming familiar somewhere, remembering what someone said, making room for another person's priorities, admitting a mistake, following through, and discovering what he wants to commit to.

### Narrative method — ADOPTED baseline under the setup request

- Close third-person narration centered on Michael, in natural colloquial Arabizi.
- Dialogue carries most scenes; narration supplies concrete setting, movement, pauses, gestures, and selective internal observations.
- Michael cannot directly know another character's private thoughts. Distinguish his interpretations from facts.
- No mandatory dialogue percentage. The earlier 60–80% suggestion was a rough orientation, not a mechanical target.
- Let dialogue breathe. A scene may include digressions, mundane logistics, laughter, interruptions, and topics that develop unexpectedly.
- Distinguish voices through background, relationship, temperament, rhythm, register, and what a person avoids saying. Do not assign everyone a repetitive catchphrase.
- Chapters can contain one sustained conversation or several connected scenes. End at a meaningful turn rather than an arbitrary word limit.
- Permit scenes of enjoyment or intimacy with no hidden crisis. Do not force a major and minor arc advancement into every chapter as a quota.
- Maintain a social world beyond Michael: off-page plans, friendships between supporting characters, work obligations, and absences matter.
- Let the consequences of a conversation survive the scene. An apology need not instantly restore trust; a disagreement need not end a friendship.

### Overall phases — WORKING architecture on the confirmed itinerary

1. **Leaving familiar circles:** SF/LA goodbyes and a loving family departure. One compact chapter is the initial recommendation.
2. **Building a Barcelona life:** accommodation, UAB, routines, friendship, café familiarity, church, work contacts, attraction, and growing commitments.
3. **Barcelona entanglements:** deeper relationships and professional responsibility; accumulated promises begin to compete. This is a movement within the February–July stay, not a separate fixed act boundary.
4. **Lebanon and distance:** local life and adventures alongside family contact and Barcelona relationships altered by absence. Do not automatically transport the entire Barcelona cast to Lebanon.
5. **Returning to Barcelona:** reunions, altered circumstances, work left unfinished, changed expectations, and decisions made with greater knowledge of the people involved.

There is no fixed ending, fixed number of acts, or obligation to resolve every thread. The eventual emotional resolution should grow from the manuscript.

## 4. Character registry

### Registry rules

Family facts and Michael's confirmed profile are in Section 2. The fictional
biographies below are **WORKING**. An "On the page" list records durable
traits and facts established in settled chapters; the event history lives in
the ledger, the present situation in current state. Keep these lists short:
record what a writer needs to stay consistent, not what has *not* happened.

Use first names until a surname matters. Introduce people at a rate readers
can remember. Ages are working starting ages; no birthdays are assigned.

### Michael — main protagonist

- **Age/background:** 21, Syrian-American; family in Los Angeles; friends in
  SF and LA; UAB in 2027 (program open, O001).
- **Wants:** study, Spanish and Arabic, worthwhile work, business, travel,
  deep friendship, romance, a future family, belonging; one day a café.
- **Strengths:** social confidence, curiosity, warmth, composure, initiative.
- **Growth pressure:** overcommitment; solving before listening; misreading
  other people's priorities. The habit is dangerous partly because it often
  *works*.
- **Voice:** Damascene. Playful with peers, affectionate at home, attentive
  with elders, precise when working.
- **Arc:** from abundant opportunity toward chosen commitments, without losing
  spontaneity or ambition.
- **On the page:** calls his parents `mama`/`baba`. Café nickname from Abu
  Nabil: `Mars` / `el Amerkani` / `ebn el zahr`. Says `Ana jey` and `akid`
  too easily (003–004, 008).

### Rami — core Barcelona friend

- **Age/background:** 23, Damascene, from el Sha8our (008). Shares the flat
  with Inés (about two years before Michael arrives).
- **Goal:** finishing studies while working irregular restaurant kitchen
  shifts; wants stability while performing carelessness.
- **Personality:** funny, loyal, sarcastic, impulsive; jokes when exposed.
- **Voice:** compressed Damascene, quick profanity (`yel3an abu…`, `5ara`,
  `ya 7mar`), generous under it.
- **On the page:** may not answer for hours on shift. Owns the yellow cheese.
  Bought a used four-shelf unit for his room (008). Owes Michael a dinner
  from the restaurant for the carry (Wed Mar 3, 008). Knows Tarek through an
  older friendship (working; not yet on the page).
- **Do not predetermine:** financial emergency, trauma, betrayal, or a failed
  romance as backstory.

### Yara — principal romantic interest

- **Age/background:** 22, Lebanese (urban Beiruti), architecture student in
  Barcelona building a portfolio and seeking paid experience. A placement may
  take her elsewhere; nothing is decided.
- **Personality:** perceptive, funny, independent, direct; affectionate when
  comfortable; serious about her work.
- **Voice:** Beiruti (`hayda`, `mesh`, `eza`, `ya3ne`, `lesh`, `hniik`),
  French flecks (`bref`, `merci`, `maquette`), can be cutting and tender in
  the same minute.
- **On the page:** lives one floor above Camille. Reads rooms like a designer
  (Walid's window chair is "design, not nostalgia", 004). Lost the name bet
  and paid, conceding `Ma3ak 7a2` before Walid (006). Likes working among
  people without being asked what she is doing (006). Kept the photo with
  Michael's finger in it "for the light". Mutual numbers since Feb 16. First
  invitation: dawn photographs at Barceloneta, Sat Mar 6, 7:30 (008).
- **Relationship stage:** mutual attraction; no date yet held, no exclusivity
  discussed. Track any agreement explicitly when it happens.
- **Avoid:** treating her as a prize; jealousy as her only conflict; career
  plans that exist only to test Michael.

### Walid — café owner

- **Age/background:** 47 (looks forties), Lebanese Christian, owns the
  fictional café **3al Zawiye** in Gràcia (S015).
- **Goal:** keep a viable business whose identity matters to him.
- **Personality:** hospitable, theatrical, observant, proud, impatient, dry;
  kind by accident. Experience doesn't make every opinion correct.
- **Voice:** Beiruti (`hayda/hayde/hawde`, `mesh`, `eza`, `ya3ne`, `ba3d`),
  `bonjour`, `merci`, `ya 3ammo` to everyone, `ya 3adra`.
- **On the page:** the espresso machine is older than Michael, unreliable, and
  its mention is banned. An unidentified supplier keeps promising "tomorrow".
  Green cardboard gift boxes with a sticker (`2ahwe. Akel. Tawle.`).
  Empty-hands rule for visits. First called Michael by name on Feb 16 (006).
  Refused Nadine's pilot after Michael offered the café without asking (007);
  gave one twenty-minute account instead (008). Takes phone orders on paper on
  a nail, changes in red, and is the only one near the phone (008). Keeps a
  brown book bound with rubber bands under the bar; Michael's page is now in
  it. Partner **Marwan** wants apps, delivery and screens; Walid refuses
  (named in 008).

### Nadine — technology/business connection

- **Age/background:** 42, Damascene entrepreneur; small unnamed fictional
  company making workflow tools for small businesses.
- **Personality:** precise, curious, selectively warm, impatient with
  vagueness, mischievous at times.
- **Voice:** Damascene with professional vocabulary inside colloquial speech.
- **On the page:** met through Walid while returning his serving tray (007).
  Her parents ran a sweets shop in el Midan; her mother took orders from the
  upstairs window ("Abu Fadi wants the kenafe at seven"); her mother is alive
  (008). Assigned a colleague to the small-business version after Michael's
  page arrived early. Offered Michael paid discovery work: three businesses
  (bakery, florist, phone repair), 8 h/week for six weeks, subject to his
  papers. She asked him to think; he said yes at once (008).
- **Boundary:** professional first; her age/gender do not make her a romantic
  possibility. Legal work arrangements stay unsettled until a scene needs them
  and they are checked.

### Karim — core friend with intellectual and practical stakes

- **Age/background:** 24, Palestinian-Jordanian; studies and works; wants
  better work.
- **Personality:** funny, loyal, politically engaged, stubborn about admitting
  misunderstandings; argues for fun.
- **Voice:** Palestinian-Jordanian urban (`mish`, `eish`, `3ashan`, `zay`,
  `ahlein`), sarcastic corporate quoting.
- **On the page:** met Michael on the train to UAB (Feb 8, 005); they argued
  about whether counting closed requests protects workers or hides customers.
  He submitted his own application answer (outcome unknown). Numbers
  exchanged; he promised the coffee is on him.
- **Next:** give him a real political or philosophical fight with personal
  stakes; not another metrics debate. Don't make him speak for a whole people.

### Inés — flatmate

- **Age/background:** 24, Spanish, freelance photographer.
- **Personality:** direct, deadpan, private, crude when annoyed or hungry,
  generous on her own terms; works too much.
- **Voice:** plain Arabic under the convention; no endearments; threats as
  jokes (`bedba7ak`).
- **On the page:** hates cucumber. Nobody steps on her camera bag. The shared
  table is her workspace; she gave Michael the corner (008). Said once, at
  Camille's door, `Akid ya3ni akid` (004). Her ten-photo client paid on Mar 2
  after a message she sharpened (008). Her printer has only glossy photo
  paper. Friend of Camille.
- **Romance:** no predetermined interest in Michael.

### Tarek — Lebanon friend (not yet on the page)

- 26, Lebanese civil engineer, Rami's old friend; weighing a job abroad while
  Michael dreams of staying. Hospitable, funny, tired of being a visitor's
  guide. Choose his town and regional voice before his first scene.

### Dalia — openly flirtatious (not yet on the page)

- **35**, Lebanese, events/hospitality professional in Barcelona. Fiery,
  assured, quick, openly flirtatious when she feels like it, sharp when
  pushed, sometimes simply uninterested. Meets Michael through the café or
  business network. Not a test of his feelings for Yara; no predetermined
  affair.

### Salma — reserved at first (not yet on the page)

- **26**, Damascene postgraduate researcher in the UAB orbit. Measured with
  strangers, dryly funny with friends, forceful on her subject; calls
  Michael's charm what it is. Interest must emerge from reciprocal behavior;
  a friendship that stays a friendship is fine.

### Supporting tier

- **Abu Nabil (~70):** Damascene, from el Midan (008). Tawle regular in the
  café's corner for ten years, "here every day". Trash-talks, invents café
  laws on the spot ("from my grandfather's days"), carries his own dice. Beat
  Michael by mars (003); lost to him (004). Never calls him by name. Hears
  everything from the corner and corrects other people's stories (008).
- **Em Jamil (about 68):** from Homs per Abu Nabil; Friday regular, the best
  player in the café, very few words, blessings as weapons (`Allah ysam7o`,
  `Mars. Sa7tein.`). Not grandmotherly toward Michael.
- **Camille, 22:** French exchange student; short red hair; hosts by feeding
  (her grandmother's blanquette); exclamatory (`Ya allah!`, `Kezzab!`).
- **Jordi, 27:** Catalan; beard and glasses; teaches Catalan to adults on
  Tuesday evenings; contrarian for pleasure (`Ma3 el 7a2. Kell marra 3and
  wa7ad.`); corrects "Spain" to "Catalunya".
- **Marwan, 50:** Walid's business partner; wants apps, delivery and screens.
  Named in 008, not yet on the page. A reasonable person, not a
  predetermined villain.
- **Abouna Elias, about 58:** priest in a Barcelona church community; warm,
  intellectual, funny, busy. Denomination and parish open.
- **Sami, 24 (SF):** founder; Michael tested his build once and owes a clean
  independent run. **Fares, 22 (LA):** Lebanese-family friend; news of his
  team's game only if they win.
- **Others:** café staff and regulars, classmates, employers, church people,
  gym friends, shopkeepers, Lebanese friends. Any woman in a flirtation must
  be 20+ with an explicit age.

## 5. Relationships and long-running narrative threads

All incidents in this section are **WORKING possibilities**, not events that have occurred. Build from the actual manuscript rather than forcing every possibility to happen.

### A. Work, competence, and ambition

An introduction to Nadine may become bounded project work. Michael enjoys learning about the company and demonstrating competence. Specific expectations concerning delivery, payment, credit, communication, and availability create stakes. His study schedule, social life, and July departure eventually require choices.

Leave the exact technical project open until it can be chosen for both plausibility and interesting conversation. Do not invent legal work eligibility or institutional permission. The arc can include negotiating scope, asking questions, admitting uncertainty, explaining a technical problem clearly, evaluating risk, or giving/receiving criticism.

### B. The café and the imagined future

Michael wants the staff to know his name and order. Let that recognition develop over repeated visits. Walid's business introduces ownership, customers, costs, staff, partnership, identity, and family obligations. Michael's wish to open a café gains specificity through experience.

A partner disagreement is available as a sustained subplot. Michael may offer something useful, misunderstand a constraint, or discover that access to someone's business comes with responsibilities. He does not become the automatic technological savior of an established local business.

### C. Friendship, loyalty, and discretion

Early practical favors and shared pleasure create trust. Later, two friends may need incompatible things or share information Michael cannot freely pass along. Overcommitment can damage reliability; discretion can be mistaken for distance. Preserve humor, routine, and ordinary kindness even during friction.

The specific secret, conflict, or breach should not be selected before the relationships support it. Reconciliation may be partial and take time. Some friends can remain friends despite unresolved differences.

### D. Yara and other adult connections

Yara is the principal romantic focus. Develop mutual interest through actual encounters, humor, attention, attraction, follow-up, vulnerability, and choices. Let both receive and give compliments and ask questions. Their independent ambitions may affect timing and expectations.

Michael's other flirtations provide genuinely different exchanges: bold reciprocal teasing, a quiet compliment, playful refusal, uncertain interest, easy conversation with an older woman, or a friendly encounter that never turns romantic. Use Dalia and Salma when their full characters strengthen the scene, and allow additional women to enter naturally.

Track the actual relationship stage and agreements. Main-interest status does not make every other woman a jealousy device. Do not manufacture an exclusivity violation merely to create drama. If a character does break a promise, preserve the other person's point of view and the consequence.

### E. Belonging, family, and life choices

Calls and messages sustain family ties across the year. Maya's shared humor, Andrew's practical care, Hassan and Zeina's affection, and Widad's support should recur in different circumstances without each call repeating the same emotional beat.

Lebanon brings Michael's imagined future into contact with other people's actual goals and responsibilities. Tarek may be considering leaving while Michael dreams of staying. Neither perspective is automatically superior. Family, faith, work, language, freedom, future children, and responsibility can become personally grounded conversations.

### F. Politics, philosophy, faith, and ideas in daily life

Conversations may concern Lebanon, Syria, Palestine, Jordan, the US, Europe, immigration, political systems, religion, ethics, technology, AI, business, wealth, happiness, love, family, and success. Characters should have differing perspectives, levels of knowledge, and stakes.

Let a discussion emerge from something: a practical decision, an event, a remark over food, a job opportunity, a family experience, or a casual question. Casual conversation can also become sophisticated without a crisis. Not every discussion should end in consensus or a polished moral.

Specific real-world assertions need checking when consequential. A character may hold an incorrect belief; distinguish that characterization from narration presenting the belief as established fact.

### G. Absence and return

Lebanon does not suspend Barcelona. Work, friendships, and Yara's life continue off-page. Calls, delayed replies, kept or missed promises, and changed expectations can carry distance without obligating constant conflict.

On returning to Barcelona, familiar places and people may feel different. Allow reunion, pleasure, awkwardness, practical work, and new understanding. Do not predetermine that everything deteriorates during the absence.

## 6. Planning depth

- The opening (001–003) is written; its original scene intentions survive in
  `planning/briefs/001–003.md` and Git history.
- Adopted book shape (S011, revised in S017): about **36 chapters of
  1,800–3,000 words**, ending New Year's Eve 2027. `planning/ROADMAP.md`
  owns the plan and may change.
- Keep an overall emotional direction and broad arcs. Plan the next two or
  three chapters in useful detail; keep distant chapters as possibilities.
- Reader-facing chapter and scene titles are Arabizi; English working titles
  stay in briefs.

## 7. Conversational exposure map

This is a behind-the-scenes coverage specification, not a syllabus or chapter order. Track meaningful instances in accepted chapters. Natural recurrence across different relationships is valuable; do not mark a topic complete because it appeared once.

| Area | Desired exposure |
| --- | --- |
| Introductions and curiosity | Names, origins, work/study, follow-up questions, asking someone to explain more, exchanging contact details, remembering prior details. |
| Friendship and group dynamics | Jokes, sarcasm, storytelling, interruptions, inside jokes, affectionate insults, gossip, invitations, planning, changing plans, teasing, defending someone, embarrassment. |
| Romance and flirting | Bold, gentle, shy, playful, direct, and indirect approaches; giving/receiving compliments; varying responses; asking for a number; interest, refusal, ambiguity, attraction, rejection. All participants 20+. |
| Emotional intimacy | Care, affection, vulnerability, listening, reassurance, asking difficult questions, expressing needs, future expectations, jealousy, tenderness, disappointment. |
| Conflict and repair | Calm boundaries, saying no, harsh disagreement, angry language, misunderstandings, unfair treatment, accusations, accepting criticism, apologies, negotiation, reconciliation, unresolved tension. |
| Family and generations | Affection, practical concern, respect, teasing across ages, protective advice, sibling closeness, different forms of support, independence, future plans. |
| Politics and philosophy | Defending and questioning opinions, uncertainty, nuance, persuasion, disagreement, happiness, ethics, success, responsibility, country-specific perspectives, religion, immigration, technology and AI. |
| Business and work | Professional introductions, company questions, technical explanations, project scope, interviews, salary/payment negotiation, deadlines, risks, ownership, customers, staff, partnership, consequences, advice. |
| Ordinary life | Cafés, restaurants, beaches, gym, church, argileh lounges, shopping, transport, shared housing, getting lost, asking for help, errands, boredom, spontaneous encounters. |
| Lebanon and travel | Beirut and other places, local social circles, trips, beaches, hikes, mountains, waterfalls, plans changing, hospitality, visitor/local expectations, uncertainty, adventure. |
| Personal aspirations | Travel, Arabic/Spanish proficiency, café ownership, worthwhile work, living in Lebanon/Syria, love, marriage/family/children as future possibilities. |
| Register and expressive range | Warmth, respect, affection, care, sarcasm, anger, irritation, crude joking, profanity, offensive remarks, softness, authority, hesitation, irony, serious confrontation. |

Michael must receive as well as produce these forms of language. Other people ask questions, initiate flirting, complain, negotiate, give advice, tell stories, refuse, misunderstand, and challenge him.

## 8. Arabizi and dialect production guide

### Composition process

1. Plan in English using circumstances, intentions, tensions, relevant facts, and possible movement.
2. Compose the original scene directly in colloquial Levantine Arabizi, including narrative paragraphs.
3. Review Arabic quality, character voice, dramatic effectiveness, and continuity.
4. Revise the specific issues that matter; preserve successful spontaneous prose.
5. Present the reviewed Arabizi directly for author acceptance. No English version is produced.
6. Recheck affected review and memory references after any later source changes.

Scene briefs should not contain an English script disguised as planning. Describe what people want and what complicates the encounter. Let the writer find what they would actually say.

### Transliteration baseline and unresolved conventions

| Item | Current rule |
| --- | --- |
| Script | Latin Arabizi only in original narrative, dialogue, and reader-facing original headings. |
| Numerals | Use `3`, `7`, `5`, `8`, `2` according to the calibration guide; `8 = gh` is user-confirmed. |
| Future marker | Prefer `ra7`; do not drift into the alternative prefix the user rejected. |
| Exact numeral mappings | `8 = gh`, `q = retained q`, `2 = glottal stop` confirmed in the user's setup reply. Remaining production conventions are specified in the calibration guide. |
| Vowels, doubled consonants, apostrophes, word joins | Adopted readable defaults are in the calibration guide; these are editorial choices, not a universal standard. |
| Dialectal pronunciation | Preserve meaningful character differences rather than mechanically normalizing everyone into one spelling. |
| Proper names and foreign terms | Use established Latin spellings where appropriate. A proper noun or common loanword is not permission for paragraphs of English dialogue. |
| Foreign-national characters | Full Arabic dialogue under the fictional convention, with no required accent explanation. |

The user specifically praised the earlier Arabizi argument-repair sample as matching the desired direction. It is a tonal reference, not a scene to reuse or evidence that its characters/events are canon. Build a small approved set of actual voice samples during calibration; do not copy the same expressions into every chapter.

### Voice records

For each recurring speaker, eventually retain a compact voice card covering:

- Geographic/family language background and any established influences.
- Typical sentence rhythm, speed, directness, humor, and register changes.
- How the person speaks with close friends, family, strangers, and professional contacts.
- How affection, embarrassment, anger, uncertainty, and vulnerability alter their speech.
- A few accepted anchor lines from their actual manuscript scenes, with references.
- Specific corrections already accepted, with reasons and sources where useful.

Shared religion does not make Lebanese characters speak identically. Age, region, education, temperament, setting, and relationships matter. Do not reduce Damascene/Lebanese speech to adding a few discourse markers to translated English.

### Review for naturalness

- Check clause order, information emphasis, omitted material, idiom, rhythm, conversational repair, and whether a response fits the preceding line.
- Watch for translated English collocations, unnecessary formality, generic agreement, excessive names/vocatives, polished speeches, and repetitive fillers.
- Keep incomplete sentences when they work. Do not mistake colloquial compression for an error merely because formal grammar would differ.
- Do not ban normal recurring expressions to satisfy a novelty quota. Look for stale exchange structures, repeated jokes, and identical emotional beats.
- Corrections should specify the line, issue, proposed replacement, and reason. A reviewer should not rewrite a lively chapter wholesale to demonstrate editorial activity.
- Reasoning should support causal coherence and language selection without making every character sound as if they have already analyzed their emotions perfectly.

### Profanity, insults, and sensitive expressions

Preserve the user's requested range. Track intended severity, relationship, delivery, and consequences: affectionate teasing, coarse humor, irritation, humiliation, and serious hostility are not interchangeable. Do not automatically censor the original.

If a reader aid is useful, put register/severity notes in a separate reference section, not inside the conversation. The story should not pause to explain every idiom.

### Uncertainty and external verification

- A model's training data does not guarantee authentic Damascene or Lebanese usage.
- Keep a short language-uncertainty list in the relevant chapter review or calibration notes: expression, intended meaning, speaker/register, uncertainty, proposed verification.
- Check consequential uncertainties against appropriate native usage, credible dialect resources, or native-speaker feedback when available. Record whether something is user-preferred, model-proposed, source-supported, or native-reviewed.
- Native Damascene and Lebanese review of representative passages is recommended, particularly for regional idioms, register, and offensive expressions. Do not claim such review has occurred until it has.
- An uncertain expression may be replaced with a well-supported natural alternative. Do not fabricate a rule to avoid admitting uncertainty.

### Publication-language rule — CONFIRMED, supersedes translation plans

The user explicitly does not want an English version. Produce and review only the
Arabizi manuscript, retaining speaker names before every spoken passage. English
may be used for editorial plans, review findings, instructions, and user conversation;
it is not a second reading edition. Do not create chapter translations, matching
English files, or translation-review work. Optional later aids require a new user
request; they are not part of the current production process.

## 9. File structure and ownership

### Design principle

**This file remains the single foundation reference.** Avoid copying its complete contents into multiple competing bibles, character registries, and style guides. Future chapter artifacts and changing story state belong in small purpose-specific files. Split the master only if scale creates a demonstrable problem, with an explicit migration and clear ownership of every fact.

The repository's structure (files appear only when the workflow needs them):

```text
arabi_book/
  AGENTS.md / README.md           # Instructions and orientation
  STORY_MASTER.md                 # This file: foundations, cast, language, workflow
  AGENT_STYLE_GUIDE.MD            # Existing empty file; no authority
  memory/
    CHAPTERS.json                 # Status, dependency, review hashes, acceptance evidence
    CURRENT_STATE.md              # One-page snapshot of the settled present
    STORY_LEDGER.md               # Per settled chapter: summary, commitments, callbacks
    DECISIONS.md                  # Provenance of user decisions and editorial defaults
    COVERAGE.tsv                  # Exposure already present, per settled scene
  planning/
    ROADMAP.md                    # Book shape and future movements (plans only)
    briefs/NNN.md                 # One short brief per chapter
  development/
    EDITORIAL_DIRECTION.md        # What has worked and what must not repeat
    LANGUAGE_CALIBRATION.md       # Spelling, voice cards, texture palette, samples
    LEXICON.tsv                   # Spelling variants the checker rejects
  prompts/                        # Role prompts, long-run runbook, ratification
  chapters/NNN/arabizi.md         # Manuscript
  chapters/NNN/review.md          # Review record with pass markers
  reports/                        # Run reports, audits, RUN_STATE.md
  scripts/story.py                # Checks, packets, stats, hashes
  tests/test_story.py             # Regression tests for the checks
```

`book/` (contents, layout, exports) and `development/PROPOSALS.md` are
created only when needed.

Do not create empty scaffolding merely to make the tree look complete. Introduce a file when the workflow first needs its content. Keep the existing empty style-guide file untouched until there is a reason to adopt or retire it; it is not an instruction source just because its filename resembles one.

### Single ownership of information

| Information | Owning record |
| --- | --- |
| User requirements, confirmed personal facts, accepted foundational cast/voice details | This master reference. |
| Chapter status, dependency, revision evidence, and acceptance metadata | `memory/CHAPTERS.json`; script checks it against actual files. |
| Actual chapter text | The chapter's `arabizi.md`; no English version. |
| Current emotional relationships, outstanding commitments, present location, who knows what | `memory/CURRENT_STATE.md`, derived from accepted chapters. |
| Chronology, compact historical changes, source-linked memorable details | `memory/STORY_LEDGER.md`. |
| Reason for an accepted creative/factual change | `memory/DECISIONS.md`; update the owning fact, do not leave the decision log as the only correction. |
| Intended future plot movements | `planning/ROADMAP.md` and the immediate brief. |
| Unaccepted alternatives | `development/PROPOSALS.md`. |
| Accepted conversational exposure | `memory/COVERAGE.tsv`. |
| Local editorial issues and reviewed source revision | The chapter's `review.md`. |
| Contents and page numbers | Generated book artifacts, never manually authoritative story records. |

Do not maintain a second standalone timeline or relationship bible that competes with the ledger and current state. Add specialized indexes only when retrieval actually needs them.

### Stable identifiers

- Chapters: zero-padded IDs such as `001`, `002`, `003`; these are labels, not a planned limit.
- Scenes: `001-S01`, `001-S02`, etc. If a scene splits before acceptance, update references deliberately.
- Threads: short IDs such as `work-opportunity`, `cafe-future`, `michael-yara`, `rami-trust`; assign only as useful.
- Canonical facts and callbacks should point to a chapter/scene, with a short exact excerpt when wording matters.
- A page number is a reading convenience, not a durable source identifier; pagination changes during typesetting.

## 10. Long-running agent workflow

### Model and role arrangement

- Any capable model may fill a role. The project has run under Codex/GPT,
  Claude and a Grok fallback. Record the model honestly in the run state; do
  not require a particular model, tool, or orchestrator.
- Use one continuing editorial conversation for the user's taste and
  decisions, with fresh role contexts supplied from the repository.
- Separate contexts reduce self-rationalization but are not native-speaker
  verification. When one agent performs several roles, say so in the review.
- The user authorized fresh agents for writing and review (C007). The
  coordinator loop is in `prompts/OVERNIGHT.md`. Never draft dependent
  chapters in parallel against stale state.

### Practical division of work

| Mechanism | Responsibilities |
| --- | --- |
| Stable project instructions | Read order, source priority, original-language rule, age/name boundaries, mutation/acceptance process. |
| Master reference | Durable personal facts, creative foundations, cast, language approach, architecture. |
| Structured state and ledger | Current relationships, information asymmetry, dates, promises, established events, callbacks. |
| Reasoning/writing sessions | Dramatic causality, psychology, pacing, natural dialogue, idiom, creative decisions, targeted revision. |
| Deterministic scripts | IDs, scene pairing, missing sections, excluded-name matching, script leakage, stale revision warnings, contents and pagination. |
| User and native feedback | Personal recognition, taste, accepted creative direction, and real dialect/register judgments. |

Scripts cannot establish emotional truth or native-sounding dialogue. Model review cannot establish that every factual claim is true.

### Before writing a chapter

The planner or coordinator prepares a **compact chapter packet** containing:

1. This master reference, or its explicitly maintained essential reading sections if the document later becomes unwieldy.
2. Current accepted state and unresolved commitments.
3. The chapter brief with relevant dates, characters, scene purposes, and constraints.
4. The previous one or two accepted chapters, including relevant voice context.
5. Specific older scene excerpts when a callback, secret, promise, or exact phrase matters.
6. Relevant accepted decisions or language corrections not yet reflected in the master; resolve that lag promptly.

Do not feed the entire manuscript by default. Do not replace necessary exact evidence with an unreliable summary merely to keep context small. Retrieve what a scene actually depends on.

### Chapter brief contents

A brief is short (aim for 500–800 words) and gives the writer dramatic intent,
not a compliance checklist. Format: `prompts/PLANNER.md`. It states:

- Dates (weekdays verified), places, cast with ages, the settled predecessor.
- What each person wants and what complicates it; the turn each scene reaches.
- **What changes by the end.**
- The nearest earlier exchange for each planned conversation, and what is new.
- A short **Hold** list: only the facts that must not be invented or the
  boundaries a writer could plausibly break. Do not list everything that
  does not happen.

Briefs describe intentions, never scripted dialogue, and leave the writer room
to discover the scene.

### Drafting unit

Use a full chapter as the default writing assignment. If a chapter is unusually long or complex, compose it scene by scene in the same writing context and then read/revise the chapter as a whole. Do not split every ordinary scene among separate writers and lose the accumulating emotional rhythm.

### Review and acceptance cycle

1. **Plan** (fresh planner): brief from settled state.
2. **Draft** (fresh writer): original Arabizi to the texture/voice/pace standard.
3. **Language review** (fresh): naturalness, voice cards, texture, spelling.
4. **Story review** (fresh): story value, continuity, attribution; records the
   passing SHA-256 and sets `ready_for_author`, or `revision_needed` (at most two
   revision loops).
5. **Settle**: in an authorized long run, the archivist sets
   `provisionally_accepted` and updates memory; otherwise the user accepts
   directly. Either way, only the user's words make a chapter `accepted`.
6. **Ratify** in the morning (`prompts/ACCEPTANCE.md`): accept, correct, or reject.

Scripts never approve a chapter. Unsettled drafts and proposed futures never
enter event memory.

## 11. Memory records and contamination prevention

### Current-state contents

Keep a concise, source-linked record of:

- Last accepted chapter and current story date/location.
- Current activities and practical circumstances.
- Each active character's immediate goal and unresolved pressure.
- Directional relationship state: Michael toward Yara and Yara toward Michael can differ.
- Promises, debts, invitations, deadlines, boundaries, and explicit relationship agreements.
- Knowledge: who knows a fact, who suspects it, who has been told something false, and who has not been informed.
- Active threads and their last meaningful changes.
- Next-scene starting conditions; proposed future outcomes belong in the roadmap.

Do not rewrite the full character registry into every state update. Do not infer a hidden emotion as fact unless the text supports it; label inference and perspective.

Keep the snapshot to roughly one page (about 1,500 words). Record what is true
and pending; do not enumerate what has not happened. History belongs in the ledger.

### Ledger entry design

Use a compact record for each accepted chapter:

```text
Chapter: [ID and accepted revision]
Story dates/locations: [established, with any deliberate uncertainty]
Changed circumstances: [causal summary rather than every conversation]
Relationship changes: [direction, agreement, tension, source scene]
Promises/knowledge: [who said or learned what; who does not know]
Open threads: [thread IDs and latest state]
Memorable details/callbacks: [specific detail + source scene]
New durable facts: [facts to incorporate into the master if foundational]
```

An ordinary entry may be roughly 150–250 words plus a few indexed details, but completeness of a consequential change matters more than an exact cap. Do not summarize every line or preserve every discarded option.

### Retaining small meaningful details

- Record a private joke, object, order preference, unfinished promise, or unusual phrase when it may plausibly matter later.
- Give the detail a source scene and search-friendly tag; include exact wording when essential.
- Keep dormant details in the ledger/index rather than every writer packet.
- Retrieve a small relevant set when planning a return, reunion, or callback.
- Do not make every incidental object into a future plot obligation.

### Decision record design

Each accepted change should identify the decision, status, source/user message or chapter, reason if given, what it supersedes, and which owning records were updated. A character's opinion is not an authorial decision about reality.

### Coverage record design

Suggested TSV columns:

```text
chapter_id  scene_id  situation  participants  register  dialect_voice  exposure_notes  source_revision
```

Record meaningful exposure already present in accepted scenes. Repeated situations may be useful when age, relationship, stakes, or register changes. Use the tracker to notice broad omissions and stale repetitions, not to demand a vocabulary checklist in every chapter.

### Contamination rules

- Do not promote a proposal by repeatedly summarizing it as fact.
- Do not make the latest draft automatically canonical.
- Do not read retired alternatives into the next writer's packet.
- Keep future romance outcomes, imagined betrayals, possible moves, and tentative backstories out of current-state facts.
- Preserve the difference between observable behavior, narration, a character's belief, and an editorial hypothesis.
- Do not create an English version or let editorial paraphrases silently create new events or intentions.
- Approved additions to real family biographies require user provenance; fictional people can gain ordinary details through accepted chapters.
- If canonical records disagree, resolve the source conflict and update the owning record. Do not let two contradictory versions persist.
- Never claim manuscript progress, review, research, user acceptance, or native verification that has not occurred.

## 12. Book layout and deterministic checks

### Arabizi reading edition

- The user wants separate chapter Markdown files during development and eventual
  assembly into one printable **Arabizi-only** book.
- Build an ordered combined manuscript and print-ready PDF when requested, with
  a table of contents, page numbers, coherent typography, and speaker labels retained.
- The chapter sources remain authoritative. Generated page numbers are not stable
  scene identifiers; retain chapter/scene IDs for editorial references.
- Do not include English translations, a companion edition, inline glosses, review
  notes, hashes, briefs, registry records, or exclusion metadata in the book.
- Use the appropriate document/PDF workflow when actual typesetting is requested.
  No book export is part of the current workflow correction.

### Useful deterministic checks

- Chapter/scene IDs are unique and original headings contain no Arabic-script leakage.
- A reviewed chapter has substantive passing evidence for its current original hash.
- `ready_for_author` and `accepted` require only the reviewed original, not English.
- Acceptance requires real user evidence and a coordinated accepted-memory update.
- Excluded names, 2027 itinerary, departure boundaries, and age metadata remain checked.
- Check actual speaker attribution and naturalness by reading; scripts cannot prove them.
- The retired translation stage/fields are rejected (registry schema version 3).
- Unexpected English manuscript files are flagged for resolution, never silently deleted.
- Contents and page numbers will be generated from accepted Arabizi material.

## 13. Initial decision register

| Decision | Status | Source/interpretation |
| --- | --- | --- |
| Dialogue-focused fiction for advanced conversational immersion and reading aloud | CONFIRMED | Original user discussions and attached brief. |
| Direct Levantine Arabizi composition; no English version | CONFIRMED, supersedes earlier translation request | Latest user correction: "I dont want an english version". |
| Damascene and Lebanese emphasis; other Levantine variation when justified | CONFIRMED | Repeated user instructions. |
| `ra7` preference | CONFIRMED | Attached user brief. |
| All nationalities speak Arabic within the story | CONFIRMED | Original user discussion and attached brief. |
| Realistic emotional range, slang, offensive language, and profanity | CONFIRMED | Repeated user instructions. |
| Friends in SF and LA; compact departure; Zeina takes Michael to LAX | CONFIRMED | User correction after initial context review. |
| No pre-Barcelona romance/flirting | CONFIRMED | User correction; preserve strictly. |
| 2027, including the Barcelona–Lebanon–Barcelona dates | CONFIRMED | Attached itinerary plus latest year correction. |
| Hassan and Zeina have separate loving households | CONFIRMED | Latest user family correction; no further marital/residence facts inferred. |
| Maya 23, close and humorous; Andrew 27, caring older-brother/father-figure quality; Widad deeply affectionate/supportive | CONFIRMED | Latest user family correction. |
| Overcommitment as principal blind spot; sometimes solving before listening | CONFIRMED | User accepted the proposed growth direction. |
| One main romantic interest, plus varied flirtation with women strictly older than 19 | CONFIRMED | Latest user romantic-direction correction. |
| Excluded personal-name family and café-owner replacement | CONFIRMED exclusion / WORKING replacement | Exclusion is user-directed; Walid is the new editorial choice. |
| Yara as the main lead; Dalia and Salma as contrasting adult connections | WORKING implementation | Implements the user's requested romantic structure; identities/outcomes can develop. |
| Close third-person Arabizi narration | ADOPTED | Selected as the development baseline under the setup request; not a separately supplied user fact. |
| One master foundation reference plus small state/chapter artifacts | ADOPTED and operational | Initial reference created first; subsequent setup request authorizes active supporting records. |
| GPT-6.1 High/Extra High throughout, fresh writing and review contexts | User preference / WORKING process | Attached brief preference; pilot can refine effort/session choices. |
| `8 = gh`, `q = retained q`, `2 = glottal stop` | CONFIRMED | User's answer during operational setup. |
| Finished chapters or fixed ending | NOT REQUESTED IN SETUP / OPEN | Current task prepares development; it does not ask for full manuscript generation or a fixed ending. |

## 14. Open decisions and next-use instructions

### Still open

- Michael's UAB program (O001). Campus scenes stay generic until answered.
- Church denomination and parish, before a specific rite or named church.
- Exact addresses, rent and contract terms, only if a scene depends on them.
- Lawful work arrangements for Michael, before paid work starts on the page.
- Real 2027 public events: verify, or mark invented events as fiction.

### Leave open until the story earns a choice

- Romantic outcome, exclusivity timing, which flirtations become meaningful.
- Distant chapter sequence and exact chapter count.
- Which Barcelona characters travel to Lebanon, if any.
- The business project's outcome, the café partnership, Michael's career.
- The final meaning of home and whether any relocation happens.
- Final title, export format, optional learning supplements.

### Instructions to the next agent

1. Read Sections 0–2 first and preserve every confirmed fact.
2. Determine what the user is asking for: development, a brief, a chapter, a
   review, or a memory update.
3. Read the relevant sections, the current state, and the editorial direction.
4. Keep confirmed facts, working plans and settled events distinct.
5. Make ordinary authorized choices without asking.
6. Report what actually changed. Never claim a plan has happened.

**Guiding principle:** write an absorbing social world Michael wants to return
to, with the depth, humor, friction, affection, and variety of conversation
that sustained real relationships create.

## 15. Operational baseline adopted during development

**ADOPTED** means selected under the user's delegated creative authority; it
is not a user-supplied fact and the user may revise it.

### Choices in force

- **Narration:** close third-person colloquial Arabizi on Michael, Damascene
  baseline (feminine past in `-et`, `hada/hay`, `mu`, `iza`).
- **Voices:** Damascene for Michael, his family, Rami, Abu Nabil, Nadine,
  Salma. Beiruti for Walid, Yara, Dalia, and Lebanese-family Fares. Karim
  Palestinian-Jordanian. Inés, Camille and Jordi speak plain Arabic. Voice
  cards: `development/LANGUAGE_CALIBRATION.md`.
- **Spelling:** `8 = gh`, `q = retained q`, `2 = glottal stop` are confirmed;
  the rest is in the calibration guide and lexicon.
- **Departure (001):** Jan 23 SF, Jan 28 LA friend, Jan 29 Hassan, Jan 30
  family at Zeina's, Jan 31 Zeina to LAX. Arrival Feb 1.
- **Home and café (S015):** a fictional shared flat with Rami and Inés, two
  floors up behind a green door, in **Gràcia**. The fictional café **3al
  Zawiye** is a few minutes' walk away. Real public places (squares, streets,
  beaches, transport lines, landmarks) may be named when certain; real
  businesses, addresses and people are not used.
- **Business:** Nadine's company is fictional and unnamed. Marwan (50) is
  Walid's partner.
- **Writing unit:** one chapter. Memory holds settled chapters only.

### Texture, voice, and pace standard (C007, C009, C010)

The user judged early drafts thin in texture, alike in voice and too cautious
in pace, and asked for that standard to continue: every chapter changes
something that matters, speakers carry their voice cards, and idiom, sarcasm
and profanity belong where the characters would use them. The revised
001–003 are the user's reference for the desired vocabulary and range
(C009). The 2026-11-11 audit (C010) adds: no lesson loops (the same
overreach-confession-cost shape), work threads with human stakes rather than
paperwork, a visible city, and an ensemble that moves. See
`development/EDITORIAL_DIRECTION.md`.

### Durable fictional details

Event-by-event details live in the ledger. The facts writers most often need:

- Hassan calls Michael `baba` / `ya 3ein baba`; Widad says `ya t2berni`,
  `ya 3omri`. Andrew has Michael's address and Rami's number; two days of
  silence and he "knows whom to call" (001).
- The shop next to the flat painted its door the same green (002). Michael's
  room faces a neighbor's laundry line. A tiny balcony by the kitchen (008).
- 3al Zawiye: green sign, glass door, `2ahwe. Akel. Tawle.`; smells of coffee
  and za3tar; window chair sees door and corner and gets morning sun; Friday
  evenings fill with old men and boards; Abu Nabil's invented laws (`el
  5asran byedfa3`, `el rab7an ma byer7al`).
- Michael's first order: man2oushe za3tar and coffee with milk, seven and a
  half.

### Remaining decisions and their deadlines

| Detail | When needed | Current handling |
| --- | --- | --- |
| Michael's UAB subject/program | Before course-specific campus scenes | Question sent to user (O001). Generic campus scenes only. |
| Official UAB calendar/procedures | Before naming such an event | Verify from an official source. |
| Housing address, rent, contract | Only if a scene depends on them | Keep unspecified. |
| Michael's work eligibility | Before paid work begins on the page | Nadine raised it in 008; settle with care, verify rules, or keep offstage. |
| Family ages/jobs/residence | Only if material to a scene | Avoid incidental assertions. |
| Church denomination and parish | Before specific rites or a named church | Generic Christian context, or ask. |
| Specific regional expressions | During language review | Flag or verify; no fabricated certainty. |
| 2027 public events | Before presenting one as fact | Research, or record as fiction. |
| Romantic agreements | When the relationship develops | Track explicit promises only. |

### Incremental GitHub delivery — CONFIRMED

The user supplied `https://github.com/Michaelhamaty/arabi_book.git` and requested
all project changes there, updated at each completed increment. Keep the book in
its own repository in this workspace; preserve the unrelated parent checkout.
Commit and push completed drafts, review/revision passes,
acceptance/memory updates, and tooling/documentation changes after appropriate
checks. Follow the current tracked branch, avoid force pushes, preserve concurrent
work, and report sync failures instead of implying success. Publishing a draft
to the Git repository is not author acceptance of its story events. See
`AGENTS.md` for the operational rule.

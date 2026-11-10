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

- Phase: Chapters 001–002 accepted; Chapter 003 brief refreshed for the authorized draft. Live progress is owned by the registry and memory records.
- Accepted progress is owned by `memory/CHAPTERS.json` and the corresponding accepted-only state and ledger. The original setup had no chapters; that historical checkpoint is not current progress.
- The user has now authorized sorting out the remaining details and creating the working development setup, beyond the original single-reference task.
- This setup request does not itself request finished chapters or a complete novel. Prepare the next authorized draft without treating plans or samples as events.
- The core personal facts and requirements below are confirmed. Fictional supporting-character biographies, scene designs, and future plot outcomes remain working proposals unless specifically marked otherwise.
- Working title: **Bayn Balad w Balad**, with the English gloss **Between One Country and Another**. The title is not finalized.

## 1. Non-negotiable story and language requirements

### Story form

- Follow Michael, a **21-year-old Syrian-American** young man, through the 2027 itinerary in Section 2.
- Use chapters, but impose no fixed chapter count, minimum length, maximum length, or total word-count target.
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

Chapters 001–002 are accepted. The SF/LA farewells and Zeina's LAX drop-off,
Barcelona arrival, and first in-person meetings with flatmates Rami and Inés are
established manuscript events; retrieve source-linked details from
`memory/STORY_LEDGER.md`. Arrival messages are not completed parental
conversations. No café visit has occurred. Unused supporting biographies and
future meetings remain proposals. The broader character designs retain their
stated status except where accepted source text establishes a fact.

Family facts and Michael's confirmed profile are established in Section 2. The fictional supporting biographies in this section are **WORKING**, not accounts of real people and not manuscript history. Retain accepted details, but revise provisional details when doing so strengthens the story and does not contradict user requirements.

Use first names until a surname matters. Avoid overloading the opening with introductions. Ages below are working starting ages; track them consistently if dates or birthdays are later assigned.

### Michael — main protagonist

- **Age/background:** 21, Syrian-American; home/family ties in Los Angeles and friends in both SF and LA; UAB in 2027.
- **Independent wants:** study, language proficiency, worthwhile work, business learning, travel, deep friendship, romance, future family, and a sense of belonging.
- **Strengths:** social confidence, curiosity, warmth, composure, initiative, and willingness to engage with different people.
- **Growth pressure:** overcommitment; sometimes solving before listening; occasional misreading of another person's priorities.
- **Voice:** Damascene baseline. Playful with peers, affectionate at home, attentive with older people, clear in professional settings. Preserve continuity between registers.
- **Long-term arc:** moving from abundant opportunity toward chosen commitments without losing spontaneity or ambition.
- **Romantic design:** one primary interest, currently Yara; other adult flirtations with different personalities and ages. Relationship promises must be tracked rather than assumed.

### Rami — core Barcelona friend

- **Age/background:** 23, Syrian/Damascene, living in Barcelona. Adopted setup: he and Inés already occupy the shared flat Michael joins; exact address and contract details are open.
- **Circumstances/goal:** finishing studies while working irregular shifts; wants more stability but enjoys appearing spontaneous and unconcerned.
- **Personality:** funny, loyal, sarcastic, sometimes impulsive. A serious moment can become a joke when he feels exposed.
- **Relationships:** likely an early connection for Michael; potential friendship with Inés independent of Michael; knows Tarek through an older friendship.
- **Voice:** distinctly Damascene, quick and compressed among peers; rougher joking when the relationship supports it; capable of speaking seriously without a sudden personality change.
- **Narrative possibilities:** practical generosity, teasing about attraction, money/time disagreements, a problem he shares with another friend first, or an occasion when Michael's well-meant intervention is unwelcome.
- **Do not predetermine:** a financial emergency, family trauma, betrayal, or a failed past relationship as established backstory.

### Yara — principal romantic interest

- **Age/background:** 22, Lebanese, studying architecture in Barcelona.
- **Goal/circumstances:** building a strong portfolio and seeking paid professional experience. A placement may take her elsewhere; nothing has been decided.
- **Personality:** perceptive, funny, affectionate when comfortable, independent, and capable of direct disagreement. Caution is situational, not her only trait.
- **Relationships:** Michael's main romantic focus. She must have friends, professional relationships, and family concerns that exist independently of him.
- **Voice:** adopted urban Beiruti Lebanese background; warmth, wit, guardedness, annoyance, and tenderness vary with trust and circumstances. Check uncertain regional expressions rather than treating the label as native verification.
- **Potential arc:** mutual attraction develops into real knowledge of each other, including differing expectations, vulnerability, boundaries, time pressures, and future plans.
- **Open outcomes:** when they become close, whether/when they become exclusive, whether she travels during summer, and the eventual relationship outcome.
- **Avoid:** treating her as a prize, making jealousy her sole source of conflict, or having her career plans exist merely to test Michael.

### Walid — recurring café owner

- **Age/background:** 47, Lebanese Christian, owns the fictional café **3al Zawiye** in Barcelona. The name is an adopted editorial choice; exact location remains open.
- **Independent goal:** maintain a viable business and a place whose identity matters to him while handling staff, family responsibilities, and business decisions.
- **Personality:** hospitable, observant, proud, occasionally impatient; dry humor and selective storytelling. Experience does not make every opinion correct.
- **Relationships:** initially a proprietor Michael encounters; familiarity and trust grow over repeated visits. He has relationships with staff, regulars, and possible partners beyond Michael.
- **Voice:** Lebanese, with generational and professional register changes. Do not make every exchange a proverb or lesson.
- **Working subplot:** a partner wants changes Walid believes would damage the café's identity. Michael's interest in cafés invites conversation and perhaps involvement, but does not entitle him to fix the business.
- **Potential development:** mutual respect complicated by unsolicited suggestions, differing appetites for risk, or Michael's romanticized ideas about ownership.

### Nadine — technology/business connection

- **Age/background:** 42, Syrian/Damascene entrepreneur in Barcelona.
- **Independent goal:** develop a small technology company and make sound choices about growth, clients, and partnerships.
- **Personality:** precise, curious, warm selectively, sometimes impatient, capable of mischievous humor and uncertainty.
- **Relationships:** a potential professional connection for Michael; project work could emerge only after a credible introduction and conversation. She has her own colleagues and competing commitments.
- **Voice:** Damascene with clear professional vocabulary; changes register naturally without turning into formal textbook Arabic.
- **Working subplot:** a bounded technical/business assignment raises questions of scope, payment, credit, availability, and follow-through alongside Michael's UAB work and summer departure.
- **Boundary:** her age and gender do not automatically make her a flirtation or romantic possibility. Her initial function is professional, with space for a fuller human relationship.

### Karim — core friend with intellectual and practical stakes

- **Age/background:** 24, Palestinian-Jordanian, studying and working in Barcelona. Specific family/region history remains open.
- **Independent goal:** establish a viable career while balancing practical constraints and strongly held values.
- **Personality:** funny, loyal, politically engaged, sometimes stubborn about admitting a misunderstanding; capable of easy friendship as well as forceful argument.
- **Relationships:** Michael can meet him through UAB; he should develop friendships outside their debates.
- **Voice:** a coherent Palestinian-Jordanian profile based on a defined background, not an arbitrary regional mixture.
- **Potential arc:** situations in which his practical choices complicate an argument he once made confidently; friendship that survives disagreement; occasionally being tired of others expecting him to speak for an entire people.
- **Avoid:** assigning all political conversation to him, equating nationality with one ideology, or making anger his only register.

### Inés — core Barcelona friend and social connection

- **Age/background:** 24, Spanish, freelance photographer in Barcelona; exact home region is open.
- **Independent goal:** establish reliable paid work and protect time for her own projects.
- **Personality:** energetic socially, surprisingly private in some matters, direct about work being undervalued; generous on her own terms.
- **Relationships:** adopted flatmate with Rami before Michael arrives; connection to Camille; relationships in a local social/artistic circle independent of Michael. The prior resident relationship does not itself imply romance.
- **Voice:** Arabic under the book's universal convention. Distinguish her through directness, timing, topic choices, and temperament, not a fabricated foreign accent or broken speech.
- **Potential arc:** an enthusiastic business suggestion clashes with the realities of freelance creative labor; friendship grows through practical trust and shared experiences.
- **Romantic status:** no predetermined interest in Michael. She is not automatically a romantic option because she is a young woman in the cast.

### Tarek — substantial Lebanon friend

- **Age/background:** 26, Lebanese, civil engineer, based in Lebanon; exact town/background to be settled when his scenes are planned.
- **Independent goal:** weigh opportunities abroad against local relationships and responsibilities.
- **Personality:** hospitable, funny, spontaneous when available, impatient with assumptions that he can always act as a visitor's guide.
- **Relationships:** old friend of Rami, potential close friend of Michael; has his own longstanding local circle.
- **Voice:** a consistent Lebanese regional/personal profile chosen before drafting; do not infer it from religion or a town stereotype.
- **Potential arc:** closeness and disagreement with Michael about staying, leaving, opportunity, responsibility, and daily life; adventures alongside work and family obligations.
- **Avoid:** making him a tour guide, a representative of all Lebanese opinion, or an automatic source of hardship exposition.

### Dalia — openly flirtatious recurring woman

- **Status:** new WORKING proposal to implement the user's requested personality and age range.
- **Age/background:** **35**, Lebanese, based in Barcelona, independent events/hospitality professional.
- **Independent goal:** build repeat business, negotiate fair terms, and protect her professional reputation and autonomy.
- **Personality:** fiery, socially assured, openly flirtatious, quick-witted, and capable of pushing back sharply. She also has moods and situations in which she is quiet or uninterested.
- **Connection:** Michael can meet her at an event through the wider café/business network after his arrival. Do not introduce her solely as a test of his attraction to Yara.
- **Voice:** Lebanese, quick challenges and playful directness when welcome, with a distinct professional register.
- **Possible dynamic:** she initiates some teasing; Michael must understand the difference between mutual play, a boundary, and a serious invitation. Both have agency.
- **Open:** degree of involvement, recurrence, and whether there is anything beyond flirtation. No predetermined conquest or affair.

### Salma — shy at first, with a fuller private personality

- **Status:** new WORKING proposal to implement the user's requested contrast.
- **Age/background:** **26**, Syrian/Damascene, a postgraduate researcher in the UAB orbit; exact field open.
- **Independent goal:** finish a demanding piece of work and decide her next academic/professional step.
- **Personality:** reserved with unfamiliar people, observant, dryly funny with friends, and unexpectedly forceful about subjects she knows well.
- **Connection:** a university or mutual-friend encounter after Michael's arrival. She may enjoy his company without immediately expressing it; interest must emerge through actual reciprocal behavior.
- **Voice:** initially more measured and less interruptive; fuller, faster, and more playful in trusted company. Avoid making shyness sound like childishness.
- **Possible dynamic:** understated compliments, gentle teasing, misunderstandings about reserve, or a friendship that stays a friendship.
- **Open:** whether any flirtation becomes mutual and how she relates to Yara or other cast members. Do not invent a rivalry automatically.

### Supporting tier and future encounters

- **Camille, 22:** French exchange student, social and spontaneous; potential friend of Inés and part of an international circle. Speaks Arabic within the fictional convention. Her interests, romance outlook, and degree of involvement remain working details, not a promise of a romance with Michael.
- **Abouna Elias, approximately 58:** priest in the Barcelona church community; warm, intellectually engaged, humorous at times, with actual community responsibilities. Precise denomination and parish remain open. He can disagree with Michael and discuss ordinary matters as well as faith.
- **SF/LA friends:** adopted fictional friends **Sami, 24**, a technology peer in SF, and **Fares, 22**, a socially playful longtime LA friend. They are not asserted to be real acquaintances. Their short farewells reveal different relationships without launching a long pre-Barcelona subplot.
- **Other women:** additional adult women in their twenties, thirties, forties, or older may enter naturally. Explicitly establish age 20+ before any flirtation or romantic interest; there is no age-group quota.
- **Other ordinary and occasional characters:** family friends, café staff and regulars, university peers, employers, church acquaintances, gym friends, people at the beach, shopkeepers, and Lebanese friends/family connections.

An occasional character need not become permanent. A minor encounter may matter much later if a believable connection develops. Introduce people at a rate readers can remember and give recurring people recognizably independent lives.

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

## 6. Opening roadmap and scene design

### Planning depth

- The three existing briefs are the initial detailed planning window, **not the total planned book**. The full 2027 geographical and emotional roadmap remains much broader.
- A nonbinding scale illustration is **40–60 shorter chapters averaging around 2,000 original Arabizi words**, or roughly **80,000–120,000 original words**, with no English edition. This is orientation for the user's length question, not an approved quota, minimum, maximum, or fixed chapter count. Let meaningful scenes and complete coverage determine the eventual size.
- Keep an overall emotional direction and broad arcs.
- Maintain a flexible near-term roadmap.
- Plan the next **two or three chapters** in useful detail; revisit as the manuscript develops.
- Distant chapters should remain possibilities or broad movements.
- Do not create a rigid whole-book scene schedule or force a fixed chapter count.

### Tentative opening chapters — WORKING

| Chapter | Focus | Intended movement |
| --- | --- | --- |
| **001 — Leaving** | SF and LA goodbyes, loving family contact across the correct households, Zeina's LAX drop-off. | Show existing relationships efficiently, then depart. Absolutely no romantic material. |
| **002 — First Address** | Arrival, accommodation, Rami, Inés, first neighborhood impressions. | Michael enters routines and relationships that already exist. |
| **003 — Finding a Routine** | UAB, an initial connection with Karim, another café visit, contact with home. | Establish different registers and early continuity without instant deep friendship. |
| **004 — An Invitation** | A social gathering or ordinary invitation expands the circle. | A natural first encounter with Yara is possible. Introduction order remains flexible. |
| **005 — Something Concrete** | A professional introduction or small assignment acquires expectations. | Give ambition a specific stake alongside study and social commitments. |
| **006 — Becoming Familiar** | Repeated encounters gain shared history, jokes, attraction, and expectations. | Build the social world through recurrence; combine or reorder these nodes if needed. |

These English labels are editorial working titles. Reader-facing chapter titles must be composed in Arabizi without English reader-facing equivalents.

### Chapter 001: detailed scene intentions

The operational brief `planning/briefs/001.md` separates the two city snapshots and the two parental-home visits into five short scene units. That is the current scene-ID assignment; the following grouped notes preserve dramatic purposes rather than an additional competing outline.

**Overall purpose:** establish what Michael is leaving and how he relates to loved ones, then reach the departure promptly. This can be a compact chapter containing a few short sequences; do not expand the opening to give every person a speech.

**Friendship farewells — brief scenes 001-S01 and 001-S02.**

- Use short, distinct farewell encounters, with transitions as needed; do not imply both cities are one location.
- Participants: Michael, fictional SF friend Sami, and fictional LA friend Fares in separate encounters (profiles in Section 15).
- Dynamics: familiar jokes, interruptions, future plans, practical questions, affection that need not become sentimental.
- Purpose: show different existing friendships through behavior and conversational rhythm.
- Boundaries: no women introduced as romantic prospects, no old-flame hook, no predeparture dating discussion used as a subplot.
- Continuity note: assign real subscene IDs if the two city encounters need separate scene references.

**Family visits — brief scenes 001-S03 and 001-S04.**

- Participants across appropriate visits or a deliberately arranged gathering: Hassan, Zeina, Maya, Andrew, Widad, Michael.
- Dynamics: Maya and Michael laugh easily; Andrew's care has a firmer practical edge; both parents remain loving; Widad offers support and affection.
- Purpose: establish family voices through preparations, teasing, attention, and small personal moments.
- Residence rule: a visit or gathering does not imply co-residence. Preserve Hassan and Zeina's separate homes. Do not decide sibling/Widad residence through incidental wording.
- Flexibility: a brief separate visit or conversation with Hassan may be clearer than assembling everyone at one table. Choose the least cumbersome natural arrangement.

**001-S05 — Zeina takes Michael to LAX.**

- Participants: Zeina and Michael; other travel staff only as necessary.
- Dynamics: practical travel conversation can open into one personal mother-son moment.
- Purpose: center the transition emotionally and conclude the departure movement.
- Boundaries: no airport flirtation, invented emergency, gratuitous conflict, or elaborate flight-procedure exposition.
- Open facts: flight details, exact dates, and whether the chapter ends before boarding or at another natural departure beat.

### Chapter 002: detailed scene intentions

**002-S01 — Arrival and connection with Rami.**

- Establish a plausible prior arrangement for meeting or accommodation; do not assume they are lifelong friends.
- Travel fatigue and logistics give Rami's humor and Michael's personality something concrete to work against.
- A small practical task can reveal generosity, mismatched assumptions, or boundaries.
- Settle the date and housing premise in the brief, consistent with the February 1 start.

**002-S02 — Entering the flat or immediate social environment.**

- Participants: Michael, Rami, and Inés if the shared-housing proposal is retained.
- Dynamics: existing routines, practical expectations, and an invitation Michael may be too tired to accept.
- Purpose: make clear that the other residents have lives and relationships already underway.
- Avoid: instant intimacy, a forced domestic argument, or everyone explaining their entire biography.

**002-S03 — First neighborhood outing.**

- Participants: Michael and Rami, encountering Walid in the café if location/timing supports it.
- Purpose: plant a place that can become familiar. A first pleasant interaction does not mean the owner already treats Michael as family.
- Dialogue can begin with ordinary service and drift naturally; no mandatory philosophy lesson on the first visit.
- Romance is now allowed geographically, but no requirement forces a romantic introduction into this chapter.

### Chapter 003: detailed scene intentions

**003-S01 — UAB and a first connection with Karim.**

- Use a plausible academic or campus circumstance after confirming Michael's program/schedule.
- Purpose: introduce university life through an actual shared task, question, or experience.
- Let curiosity and humor build a connection without assuming immediate loyalty.

**003-S02 — A conversation continues.**

- A walk, meal, journey, or coffee gives Michael and Karim time to talk.
- An actual topic of interest reveals points of agreement and disagreement, with room for digression.
- Purpose: show intellectual energy alongside personality; no compulsory explosive political argument.
- An additional café encounter may begin recognition but should not accelerate familiarity unnaturally.

**003-S03 — Contact with home.**

- Choose a family member for a specific reason; do not cycle mechanically through the whole family.
- Michael's spoken account of his new life may differ slightly from what the reader has seen, without making him automatically deceptive.
- Purpose: preserve old relationships and show what he wants to share, minimize, or understand aloud.

### Opening revision freedom

Combine or split scenes if pacing improves. If a stronger first Barcelona scene emerges, revise the roadmap rather than forcing an outdated brief. Keep the short departure, confirmed family portrayal, dates, language rules, age limits, and predeparture romance boundary intact.

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

The initial reference-only task created this master. The later setup request creates the active instructions, memory records, briefs, calibration, prompts, and structural tools. The following is the designed structure; `chapters/` and `book/` remain deferred until content actually needs them:

```text
arabic_story_dev/
  STORY_MASTER.md                 # This file: requirements, cast, architecture, language, workflow
  AGENTS.md                       # Active concise instructions and reading order
  README.md                       # Start commands, status fields, and practical launch instructions
  AGENT_STYLE_GUIDE.MD             # Existing empty file; unchanged; no established authority/content

  memory/
    CHAPTERS.json                 # Status, dependency, revision hashes, acceptance evidence
    CURRENT_STATE.md               # Present accepted story state, relationships, knowledge, active threads
    STORY_LEDGER.md                # Compact accepted chapter records, dates, callbacks, source references
    DECISIONS.md                   # Dated accepted changes and reasons; amendments update master/state
    COVERAGE.tsv                  # Exposure already present, referenced to accepted scenes

  planning/
    ROADMAP.md                     # Flexible future movements; always marked as plans
    briefs/
      001.md                       # Detailed next-chapter packet, not a finished script

  development/
    PROPOSALS.md                   # Future alternatives file when actual alternatives need storage
    LANGUAGE_CALIBRATION.md        # Adopted spelling, voice notes, noncanonical samples, uncertainty

  prompts/
    WRITER.md                      # Fresh original-language writing assignment
    REVIEWER.md                    # Language/story/continuity review and evidence
    ACCEPTANCE.md                  # User acceptance and memory-update transaction

  chapters/
    001/
      arabizi.md                   # Original manuscript
      review.md                    # Editorial findings, fixes, uncertainties, proposed memory changes

  book/
    CONTENTS.md                    # Generated from accepted chapters
    layout/                       # Typography/build templates
    exports/                      # Generated reading editions and reference supplements

  scripts/
    story.py                      # Read-only structural checks, hashes, and input lists
    build_book.py                 # Future contents/pagination/export builder, when useful

  tests/
    test_story.py                 # Structural checks and stale-review/dependency regression cases
```

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

### Recommended model and role arrangement

- User preference: **GPT-6.1 at High or Extra High throughout**, with Extra High for initial creative development.
- Start the foundation and pilot chapter with GPT-6.1 Sol Extra High if that setting is available in the user's session. Assess output quality instead of assuming higher effort guarantees better dialogue.
- Do not require Astra, a different model family, an unavailable tool, an API key, or a custom orchestrator to proceed with ordinary chapter work.
- Earlier Astra-planner/Sol-writer advice is a superseded architecture preference, not a project requirement.
- Use one continuing editorial conversation for user taste and high-level decisions, with fresh chapter-writing and review contexts supplied from the repository.
- Roles can be separate sessions using the same model. Separate contexts reduce local rationalization but do not constitute independent native-speaker verification.
- Parallel agents, when explicitly used, should handle bounded independent research/review tasks. Do not draft dependent future chapters in parallel against stale state. Do not spawn agents simply because this document describes possible roles.

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

Each brief should state:

- Chapter ID, working title, status, dates, locations, and starting state.
- Relevant character ages and current relationship/knowledge state.
- Emotional/social purpose and independent goals of participating characters.
- Scene intentions and causal links, allowing useful discoveries during composition.
- Prior commitments, references, and facts the chapter must respect.
- Available future possibilities clearly marked as possibilities.
- Conversational opportunities, only where the situation supports them.
- Unresolved research/language questions and the facts that must not be invented.
- A flexible stopping point, not a mandatory word count or scripted conversation.

### Drafting unit

Use a full chapter as the default writing assignment. If a chapter is unusually long or complex, compose it scene by scene in the same writing context and then read/revise the chapter as a whole. Do not split every ordinary scene among separate writers and lose the accumulating emotional rhythm.

### Review and acceptance cycle

1. **Plan:** prepare the immediate brief from accepted state.
2. **Draft:** compose the original Arabizi directly. New fictional details remain provisional.
3. **Review:** use a fresh context to check naturalness, voice, story, continuity,
   speaker labels, dates, personal facts, age/name constraints, and factual uncertainty.
4. **Revise:** resolve concrete findings and read the resulting original. Record its
   actual SHA-256 and passing review evidence only after that review occurs.
5. **Present:** set `ready_for_author` and give the user the Arabizi chapter.
   There is no translation stage, English file, or English-review requirement.
6. **Accept:** actual user acceptance promotes that exact revision; scripts never approve it.
7. **Update:** synchronize accepted state, ledger, coverage, registry, and durable facts.
8. **Continue:** refresh the next brief from what actually happened, then draft sequentially.

Use one lightweight author checkpoint per chapter unless the user changes the
cadence. Routine fictional decisions do not require repeated permission requests.
Unaccepted drafts and proposed future outcomes never enter accepted-event memory.

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
- The retired translation stage/fields are rejected by registry schema version 2.
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

### Settle before full drafting when relevant

- Numeral mapping is now confirmed and the remaining spelling baseline adopted in `development/LANGUAGE_CALIBRATION.md`; assess voice quality during actual review.
- Close third-person narration is adopted as the initial development choice.
- Fictional farewell friends and household staging are chosen in Section 15 and brief 001; do not invent additional real family biographies.
- A fictional shared-flat arrangement and limited pre-arrival contact with Rami are adopted in Section 15.
- Michael's UAB program and relevant schedule before specific campus scenes.
- Exact recurring-character language backgrounds before making regional speech claims.
- The first three briefs specify their limited cast; later character introductions remain responsive to the manuscript.
- Any substantive details about real family members that an opening scene would otherwise have to invent.

These are targeted development questions, not a request for the user to redesign the novel. Make useful recommendations, avoid repeating settled requirements, and leave inconsequential details to ordinary fictional composition.

### Leave open until the story earns a choice

- Eventual romantic outcome, relationship exclusivity timing, and which flirtations become meaningful.
- Distant chapter sequence and chapter count.
- Which Barcelona characters travel to Lebanon, if any.
- The exact business project, café partnership outcome, and eventual career choice.
- The final meaning of home/belonging and whether any long-term relocation happens.
- Final title, export format, audio, exercises, and other optional learning supplements.

### Instructions to the next agent

1. Read Sections 0–2 first and preserve every confirmed correction.
2. Determine whether the user is requesting development, a brief, a chapter, review, or a memory update. Do not start manuscript generation merely because this reference exists.
3. Read the relevant cast, arcs, language, and workflow sections. Find the latest accepted state if any chapters now exist.
4. Distinguish confirmed facts, working plans, and accepted events in both prose and updates.
5. Work toward the requested deliverable without requesting approval for ordinary authorized choices.
6. Keep foundation changes in this file, manuscript evidence in chapters, current state in memory, and speculative ideas in development.
7. Report what actually changed and any consequential unresolved point. Never claim a proposal has already happened in the story.

**Guiding principle:** write an absorbing social world Michael wants to return to, with the depth, humor, friction, affection, and variety of conversation that sustained real relationships create.

## 15. Operational baseline adopted during development setup

The user requested that final details and the working method be sorted out so
development can begin cleanly. This section records the resulting editorial
choices. **ADOPTED** means selected under that delegated creative authority; it
does not mean the user separately supplied the detail or that it has happened in
the story. The user may revise these choices. Confirmed facts above retain priority.

### Choices settled now

- **Narration:** close third-person colloquial Arabizi centered on Michael.
- **Primary voices:** Michael, Rami, Nadine, and Salma have Damascene baselines;
  Yara's working profile is urban Beiruti Lebanese. Walid and Dalia retain urban
  Lebanese baselines with individual age/professional differences. Avoid unsupported
  microregional rules. Karim's Palestinian-Jordanian profile is not a license to
  mix regional forms randomly. Voices are drafted and reviewed, not declared authentic
  solely because a city label was assigned.
- **Spelling:** `8 = gh`, `q = retained q`, `2 = glottal stop` are user-confirmed.
  Other conventions, examples, and their editorial status are in the calibration guide.
- **Departure:** one compact chapter. Provisional scene dates are January 23 (SF),
  January 28 (LA friend), January 29 (Hassan visit), January 30 (family gathering at
  Zeina's home), and January 31 (Zeina's LAX drop-off). These are fictional planning
  dates within the confirmed itinerary, not records of actual flights. February 1
  is the arrival premise. Exact routes and times are not invented.
- **Opening friends:** Sami, 24, is a fictional SF technology peer; Fares, 22, is
  a fictional longstanding LA friend with a socially playful style. They provide
  two distinct short exchanges. Do not assert they are real acquaintances or add
  significant real-life history to Michael through them.
- **Household staging:** Hassan receives a separate short visit. At the family
  gathering, Maya, Andrew, and Widad are present/visiting; their actual residence is
  left unspecified. Zeina drives Michael to LAX. Separate parental homes remain clear.
- **First Barcelona home:** a fictional shared flat already occupied by Rami and
  Inés, which Michael joins through a practical pre-arrival arrangement. Prior contact
  consists of accommodation messages, not an established friendship. Address,
  neighborhood, rent, and legal contract terms are not needed for the first scenes.
- **Café:** Walid's fictional establishment is called **3al Zawiye**. Treat it as
  invented, not a recommendation or claim about a real business. The exact address
  stays unspecified. A potential partner **Marwan, 50**, is reserved for a later
  business subplot; introduce him only when useful. He can have a reasonable view
  of the business and is not predetermined to be an antagonist.
- **Cast pacing:** Rami/Inés/Walid in the first Barcelona movement; Karim next;
  Yara potentially through Camille at an ordinary later gathering. Nadine, Salma,
  and Dalia enter when their own circumstances fit. No all-cast first-week reunion.
- **Business direction:** Nadine's fictional company develops practical workflow
  tools for small businesses. A first conversation may lead to a bounded discovery
  or project opportunity. Exact deliverables, payment, and lawful work arrangements
  remain to be settled before those facts matter; no automatic paid job is promised.
- **Writing unit:** one chapter, with scene-by-scene composition inside the same
  context if needed. Use fresh writing and review sessions with the same references.
- **Memory:** no chapter events enter current state or the ledger until author
  acceptance. Registry hashes protect against accidentally reusing a review or
  review of an older original. No translation is produced. The scripts never accept chapters.

### First development cycle

1. Use the prepared short noncanonical voice samples to understand the spelling
   baseline and desired register contrasts. Feedback is welcome; these examples
   are neither manuscript nor native-speaker-validated rules.
2. When drafting is requested, run the Chapter 001 writer packet and read all its
   inputs. Compose the original only, then hand it to fresh review.
3. Review naturalness, voice, pacing, factual continuity, and boundaries; make
   concrete revisions and record the reviewed source hash.
4. Present the reviewed Arabizi chapter directly to the user; no English version.
5. Record actual acceptance and update the memory transaction. Only then refresh
   Chapter 002's brief and write it from current accepted state.

The practical commands and registry schema are in `README.md`; role-specific
launch prompts live in `prompts/`. Do not create another full workflow bible.

### Remaining decisions and their deadlines

| Detail | When needed | Current handling |
| --- | --- | --- |
| Michael's UAB subject/program | Before course-specific campus scenes | Question sent to user. The departure chapter is unblocked; a general campus visit need not invent courses. |
| Exact official UAB calendar/procedures | Before naming such an event | Verify from an appropriate official source; do not equate arrival date with a class start. |
| Housing address, rent, contract | Only if a scene truly depends on them | Keep unspecified or choose a clearly fictional setting without unsupported legal claims. |
| Family ages/jobs/residence not supplied | Only if material to a scene | Avoid incidental assertions; ordinary actions and dialogue can use established relationships. |
| Church denomination and parish | Before describing specific rites or a named church | Use generic Christian social context if sufficient; ask only when the detail matters. |
| Highly specific regional expressions | During language review | Flag or verify; don't fabricate certainty. |
| Future political/news events in 2027 | Before presenting a concrete event as factual | Research if knowable at drafting time; record invented events as fiction. |
| Later romantic agreements and outcomes | When the actual relationship develops | Keep open; track explicit promises rather than assuming them. |

There is no requirement to settle every distant plot choice before Chapter 001.
The setup is intended to make careful writing possible, not to keep adding planning
layers indefinitely.

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

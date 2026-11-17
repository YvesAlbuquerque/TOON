# T.O.O.N. — The Office Of Nonsense — Design Direction

**Decision date:** 2026-11-09  
**Expanded:** 2026-11-13  
**Status:** Accepted direction; Documented  
**Former project names:** InkTime / Ink Through Time  
**Implementation status:** Do not infer implementation from this document. See code, tests, Issues, branch state, builds, and playable evidence.

## Product statement

**T.O.O.N. — The Office Of Nonsense** is a historical creative-studio management game about building one eccentric company across more than a century of changing media.

The player begins with a tiny office around 1900, hires generations of creative professionals, develops persistent fictional properties, manages money and production, and adapts as the studio expands across four supported production types: **comic strips, comics, 2D animation, and 3D animation**.

The studio is the long-lived protagonist. Productions, employees, relationships, technologies, facilities, and IPs change around it.

T.O.O.N. is not a professional animation-authoring application and is not defined by AI generation. It is a management simulation about keeping creative nonsense alive long enough to ship it.

## Naming decision

The owner selected **T.O.O.N. — The Office Of Nonsense** as the current game name.

The acronym and expansion are intentional:

- **T.O.O.N.** evokes cartoon media;
- **The Office** represents organization, departments, deadlines, budgets, contracts, and responsibility;
- **Of Nonsense** represents creative risk, exaggeration, humour, invention, and the unreliable personalities that make the work.

The central creative tension is:

> **Office gives nonsense structure. Nonsense keeps the office worth running.**

The name remains **Accepted direction, not commercially cleared**. Existing collision risk must remain explicit until proper clearance.

## Player dream

> Start with a room, a few strange people and a handful of ideas. Build T.O.O.N. across generations of media, survive the people and technologies that transform it, and leave behind a studio history that belongs to your campaign.

The player should want to say:

- “this is **my studio**”;
- “these are **my people**”;
- “we made **that**”;
- “that character has existed here for eighty years”;
- “this employee changed the company”;
- “this disaster became part of our history.”

## Principal pillar

### Doing — managing creative chaos

The primary play is choosing how to allocate people, money, time, creative freedom, technology, and organizational attention under uncertainty.

### Emotional payoff — attachment and legacy

The player should become attached to:

- the studio as an institution;
- recurring professionals;
- their relationships and careers;
- persistent IPs and characters;
- memorable productions;
- the visible history accumulated across decades.

## Creative and systemic references

T.O.O.N. draws from several references, but they are **directional influences rather than feature-parity targets**. The project should borrow useful principles, simplify aggressively where production reality requires it, and preserve its own identity.

### The Movies

**The Movies** is the strongest overall reference for the fantasy of running a creative entertainment studio whose people, facilities, productions and history remain visible in the world.

It is also an intentionally **utopian reference** for T.O.O.N.: reproducing its breadth with a much smaller team and development budget would be an unrealistic scope target.

Use it primarily to inform:

- the studio as a physical, evolving place;
- attachment to recurring staff;
- visible production activity;
- the relationship between facilities, people and output;
- the pleasure of seeing the studio's history accumulate;
- completed productions as something the player can actually watch or revisit.

Do not use it as a requirement to match every simulation layer, production system or content volume.

### TOON tabletop RPG

The **TOON** role-playing game is a thematic and systemic reference because its cartoon logic, terminology, abilities and treatment of absurd characters overlap with the space T.O.O.N. wants to explore.

Useful inspiration includes:

- cartoon-world logic taken seriously by the rules;
- unusual abilities and character traits;
- absurd consequences that remain mechanically meaningful;
- a vocabulary that can help identify useful design concepts.

This is inspiration, not a licence to copy distinctive protected text, rules expression, characters or presentation. T.O.O.N. should adapt useful ideas into its own terminology and systems where appropriate.

### Dispatch

**Dispatch** is a reference for character relationships and for presenting a cast whose personalities, conflicts and interpersonal history matter to management decisions.

It is also useful as a reference for a **very lightweight representation of a city and activities outside the primary workplace**. T.O.O.N. can learn from that abstraction while developing a richer model where outside-life events, geography and employee autonomy justify it.

### Management games

Management games broadly are reference material for:

- readable cause and effect;
- resource and staffing tradeoffs;
- growth through capacity rather than arbitrary progression;
- legible worker state;
- long-term planning;
- allowing simulation stories to emerge from management decisions.

T.O.O.N. should take patterns selectively rather than inheriting genre conventions automatically.

### Evil Genius

**Evil Genius** is a recurring reference for this style of game, particularly for:

- a physical base whose layout is part of management;
- workers visibly inhabiting and using the space;
- facilities creating operational capacity;
- readable autonomous behaviour;
- systemic comedy emerging from serious simulation rules;
- the pleasure of watching an organization function, malfunction and develop character.

The relevant lesson is the coupling of **space + people + systems + personality**, not copying its specific base-building structure or theme.

### Reference discipline

When a reference conflicts with T.O.O.N.'s production constraints or core identity, prefer the smallest system that preserves the intended player experience.

The question should be:

> **What useful experience are we borrowing?**

rather than:

> **How do we reproduce the referenced game?**

## Soul rule

> **Every production and every person can change the office that made them.**

Consequences should persist in some combination of:

- studio finances and facilities;
- professional happiness, careers, relationships, absences, departures, or legacy;
- IP history, canon, audience recognition, and adaptation opportunities;
- technology and workflow choices;
- reputation and future opportunities;
- the studio archive.

## World opening, starting location and language

A new campaign should begin by presenting the world before presenting the studio.

The preferred opening direction is an interactive **globe/world view** around the campaign start date, from which the player chooses where T.O.O.N. begins.

**G-09 owner decision (2026-11-16, option A, stylized):** the campaign opens with a **stylized interactive world map or globe** and the player selects a **country**, not a city. The first studio is then established in an **implicit or game-defined starting locality** associated with the selected country; there is **no mandatory city-selection step** or full city-level simulation in the base opening flow.

`Stylized world view -> select country -> first studio`

The visual art direction of the map/globe, geographic abstractions and starter-country catalogue remain later art/content decisions. **Owner correction (2026-11-16) supersedes any earlier economic/geographic interpretation of G-09:** the selected country is **only a source for language defaults and country-relevant historical/cultural events/context**. It is **not** an economic modifier, territory, foreign-market unlock, travel destination, branch-management system or country-based expansion progression. The map is stylized, not a world-simulation feature. Event facts require sourced, reviewable data.

### Starting location

The starting **country** supplies (1) the studio/world language default, which can inform the default production language, and (2) relevant, sourced country-specific historical/cultural events and narrative context. The interface language remains independently configurable. **Country choice does not itself alter salaries, rent, talent availability, markets, technology, distribution reach, contracts or opportunities, nor does it unlock geographic expansion.** Any economic/market consequences arising from independently designed historical events must be explicitly authored and evidenced as event mechanics, **not inferred automatically from a national label**. There is no required city selection or city simulation.

### Language layers

Separate language into at least three concepts:

1. **Interface language** — menus, settings, tutorials and accessibility text.
2. **Studio/world language** — what professionals normally speak in the chosen location.
3. **Production language** — the language in which a particular work is created/released.

Starting location should set sensible defaults for studio/world and production language.

It may also suggest the interface language at first launch, but **the player must be able to change UI language independently**.

This allows examples such as:

- UI in Portuguese, studio in Tokyo, characters primarily speaking Japanese;
- UI in English, studio in Rio de Janeiro, productions primarily in Portuguese;
- a multilingual studio later creating a production in a language different from its home market.

### Dialogue and accessibility

Character dialogue can be voiced/spoken in the studio/world language while subtitles remain in the selected interface/subtitle language.

Where runtime voice generation is used, voice language/accent is part of the character/presentation layer and must remain separable from UI localization.

Do not make understanding the game's management systems depend on the player personally speaking the studio language.

### Productions and localization

A production should record its original language.

Later systems may support:

- subtitles;
- translation;
- dubbing;
- localized editions;
- multilingual staff;
- foreign distribution;
- remakes/adaptations for other markets.

These are expansion candidates, not first-slice requirements.

### Geographic scope boundary (G-09 owner correction)

**There is no gameplay system for international expansion based on starting country.** Do not add moving headquarters, overseas branches, multinational office management, geographic progression or automatic country-specific business modifiers as a consequence of the country picker. The game remains focused on its single studio; country selection is a **language and event-context input only**. Any unrelated later publishing/localization feature must earn a separate design decision, rather than being inferred from the start-of-campaign map.

## Campaign and time

The target campaign spans approximately **1900–2030**. This is about 130 years of studio history, not 120; exact start/end dates and technology availability remain tunable design data rather than historical-simulation claims.

### Simulation clock and working day

T.O.O.N. should use a **continuous management-simulation clock** rather than advancing only when the player submits an action or ends a turn.

Accepted direction:

- time advances on its own during normal studio play;
- the player can manually accelerate simulation speed;
- when nobody is actively working, the game automatically fast-forwards through low-value downtime until the next meaningful work period/event;
- automatic fast-forward must stop before a relevant event, the next meaningful work period or player-required intervention, rather than skipping it;
- opening the main `Esc` menu pauses simulation;
- entering construction/build mode pauses simulation;
- pop-ups that require reading or a player choice, including Decision Events, pause simulation while presented;
- leaving/closing the game never advances campaign time in the background.

The goal is to preserve a living continuous studio without making the player wait through empty nights/weekends or lose time while making deliberate management/build decisions.

The visible studio day should matter.

Professionals can:

- arrive for work;
- perform assigned work;
- move through the studio;
- talk and socialize;
- eat/rest/use amenities;
- react to colleagues and the environment;
- leave at the end of their working day;
- arrive late, leave early or be absent when simulation state causes it.

T.O.O.N. should **not** become a full domestic-life simulation. Off-site life is represented primarily through state and events rather than a fully simulated city/home.

Nights, weekends and other low-interaction periods may be compressed, accelerated or skipped where that improves campaign pacing. The exact time scale and work calendar remain tuning parameters. T.O.O.N. does not need a separate multi-shift/shift-roster management system; normal working hours, overtime, lateness and absence are sufficient unless later validation proves otherwise.

This creates a useful distinction:

`visible workplace simulation -> compressed off-site life -> persistent consequences back at work`

### Campaign-length target

The target for a first complete campaign is approximately **40 hours to the 2030 retrospective/end-state**.

This is a design target, not a guaranteed runtime claim. Validation must measure actual player pace once representative systems and generated productions exist.

At 1900–2030, a 40-hour campaign implies an average of roughly **3.25 in-game years per real-time hour**, but pacing should not be uniform. Early text/illustration/strip eras may move through time faster, while later productions can consume more real-time attention as teams, media and outputs become more complex.

The 40-hour budget includes more than management UI. It includes the player's time spent:

- running the studio;
- hiring, negotiating with and responding to professionals;
- making production and technology decisions;
- shaping/reviewing creative work;
- reading, viewing or watching completed T.O.O.N. productions;
- inspecting archive/history consequences;
- dealing with systemic events and relationships.

The campaign should feel like an evolving history of creative production, not a fixed linear tech tree.

### Media evolution

T.O.O.N.'s four accepted production types are **comic strip, comic, 2D animation and 3D animation**. Their historical workflows can incorporate text/humour writing, illustration, storyboards, silent/sound/colour techniques, television-era distribution, digital tools and realtime technology without making those separate top-level production types.

New technologies do not automatically invalidate older production types. New capabilities expand the studio's options.

A 1970s T.O.O.N. may still publish comics. A 2020s T.O.O.N. may deliberately retain hand-drawn 2D while another department produces 3D work.

### Technology choice

Technology should create strategic choices, not passive unlock bonuses.

Early adoption may bring:

- high cost;
- training burden;
- workflow instability;
- competitive advantage;
- new creative possibilities.

Late adoption may bring:

- lower risk;
- lower cost;
- lost opportunities;
- staff frustration;
- audience or market lag.

## Historical context: global and local timelines

T.O.O.N. should treat real history as an active **context layer** around the player's fictional studio.

The campaign should maintain two coupled historical timelines:

1. **Global timeline** — major international events, technology shifts, economic cycles, media/market changes, wars, crises, cultural movements, communication/distribution changes, and other broadly relevant context.
2. **Local timeline** — country/region-specific events, market conditions, cultural movements, regulation, local technology/media adoption, labour conditions, economic shocks, and other context relevant to the chosen studio location.

The studio's own fictional history forms a third layer:

3. **Studio timeline** — hires, departures, relationships, productions, failures, successes, IP history, expansions, scandals, awards, technical transitions and other campaign-specific events.

The player should be able to understand these layers together:

`global history + local history + studio history -> creative context and market context`

### Historical events as structured context

Historical data should be represented as structured, sourced entries rather than free-form flavour text.

A historical-context entry may include:

- stable identifier;
- date or date range;
- geographic scope;
- event/category tags;
- factual summary;
- affected market/media domains;
- possible social/economic/technology pressures;
- source/provenance;
- confidence/review state;
- whether the effect is factual, inferred, or game-design interpretation.

Do not encode controversial interpretation as objective historical fact.

Where an event's gameplay effect is a design inference, keep the distinction explicit.

### Creative context

When a production is conceived or developed, the current historical slice can be exposed to the creative process.

Relevant inputs may include:

- current year/era;
- global events;
- local events;
- market conditions;
- available media/technology;
- cultural movements;
- studio location/language;
- existing studio/IP history;
- professionals assigned to the production;
- their relationships, beliefs, experiences and current states;
- prior audience response.

For runtime AI-assisted production, provide a **bounded, relevant context package**, not an unfiltered dump of the entire historical database.

Historical context can influence:

- themes;
- tone;
- subject matter;
- humour;
- character concerns;
- visual language;
- medium choice;
- production constraints;
- what employees propose or reject.

The player should retain creative agency. Historical context informs possibilities; it does not force one "correct" work.

### Effects on professionals

Real events may affect professionals through their personal context.

Possible consequences include:

- morale/stress;
- creative energy;
- attendance;
- finances;
- safety;
- political/social pressure;
- family obligations;
- migration;
- military/civic obligations where historically appropriate;
- access to materials/equipment;
- changes in audience or professional opportunity.

Effects should depend on the character and location rather than applying identical global penalties to everyone.

A global event may be background noise to one employee and life-changing to another.

### Market and audience reception

Historical context should participate in reception without becoming a deterministic lookup table.

A production's result should use a **hybrid evaluation model**. The simulation process matters, but the finished generated work also matters.

Conceptually:

`production process/state -> generated artifact`

`generated artifact -> local artifact evaluation`

`process evidence + artifact evidence + audience/market context + distribution + uncertainty -> reception/commercial result`

The production process contributes evidence such as:

- crew skill and suitability;
- time and schedule pressure;
- fatigue/conflict/production disruption;
- technology and facilities;
- creative direction;
- budget and scope;
- iteration/rework opportunities.

The **artifact itself** must also be evaluated. Where technically feasible, local specialist or multimodal models should inspect the actual finished text, strip, comic, image, audio, animation or other produced work and return bounded, game-owned evaluation dimensions.

Candidate artifact dimensions include:

- coherence/readability;
- technical defects;
- visual/audio/narrative consistency;
- fidelity to the production brief and IP anchors;
- recognizability/continuity of persistent characters;
- pacing/composition/craft signals appropriate to the medium;
- distinctiveness/novelty where it can be assessed meaningfully;
- likely appeal to the target audience/context.

Do not collapse artistic value into one supposedly objective AI taste score. Artifact evaluation should provide structured evidence with uncertainty, not an unquestionable verdict.

A production's result may therefore conceptually depend on a combination such as:

`process quality + artifact evaluation + audience fit + historical context + market conditions + medium/technology + studio reputation + distribution + novelty/timing + uncertainty`

Examples of context-sensitive reception:

- a theme becomes unusually resonant because of current events;
- a comedy arrives at the wrong cultural moment;
- a new medium benefits from novelty but reaches a smaller audience;
- economic hardship reduces spending while increasing demand for inexpensive entertainment;
- a local cultural movement creates an audience for work previously considered niche;
- a production created before a major event is received very differently if released afterward.

Do not reduce this to hidden arbitrary bonuses. The player should receive legible signals about why the market reacted as it did.

The artifact evaluation should also be legible enough to explain why the finished work mattered. For example, a production can be well managed but produce an inconsistent final short, or survive a chaotic production and still result in an unusually strong work.

Management decisions should influence the generated artifact itself where possible, not merely add or subtract score afterward. Production state can affect available iterations, generation constraints, references, quality settings, continuity context or other bounded inputs to the local generation pipeline.

The local evaluator must not directly set revenue or mutate authoritative state. It returns structured evidence; game-owned reception rules combine that evidence with simulation and market context.

Because local model judgments can vary, important artifact evaluation should use stable prompts/schemas, bounded dimensions and validation. Where practical, calibration, multiple evaluators or repeated/ensemble scoring may be tested for higher-impact decisions. Exact evaluator architecture remains **Planned** until validated.

### History is backdrop, not predestination

The canonical historical timeline should remain stable unless the game explicitly adopts an alternate-history system in the future.

T.O.O.N. should generally answer:

> "What did your fictional studio do while real history was happening?"

rather than:

> "Can your cartoon studio rewrite world history?"

The studio can become culturally important inside the fictional campaign without casually replacing real historical causality.

### Historical tone and sensitivity

Real history can include war, persecution, disaster, political repression, economic collapse, discrimination and other serious events.

T.O.O.N. should not convert human suffering into a simplistic opportunity modifier such as `+20% comedy demand`.

For sensitive events:

- distinguish factual context from game-design interpretation;
- model concrete pressures before abstract market bonuses;
- consider asymmetric effects on professionals, audiences, materials, distribution and safety;
- avoid jokes whose only premise is the suffering of real victims;
- keep systemic comedy focused primarily on the fictional studio/cast rather than trivializing real tragedy;
- provide content/tone controls where historical material materially benefits from them;
- use reviewable sourced summaries rather than sensationalized AI-generated history.

Historical context can still create meaningful creative tension, irony and market change, but the simulation should remain legible about what is factual and what is an authored model.

### Historical research boundary

Because the campaign uses real countries, dates, markets and events, historical content requires a sourced data pipeline.

Do not let AI invent historical facts at runtime.

AI may synthesize from approved historical context, but factual entries should come from curated/reviewed data with provenance.

## Core systemic model

T.O.O.N. is built around five coupled systems:

### Studio

- cash and recurring costs;
- facilities;
- departments;
- equipment;
- reputation;
- archive;
- opportunities;
- long-term identity.

### People

- skills and roles;
- career progression;
- happiness/morale;
- creative energy;
- discipline;
- wildness/experimentation;
- relationships;
- demands and bargaining power;
- absences and outside-life consequences;
- aging/longevity rules;
- legacy.

### Productions

- medium;
- scope;
- schedule;
- budget;
- crew;
- creative direction;
- production pressures;
- quality;
- release result;
- persistent consequences.

### IPs

- identity;
- characters;
- premise/tone;
- canon where useful;
- adaptation history;
- audience recognition;
- ownership/credit history;
- media transformations over time.

### Time

- eras;
- changing production methods;
- new professional disciplines;
- cultural/market pressures;
- staff aging or non-aging;
- retirements and generations;
- long-term studio memory.

These systems must interact. A production decision should be able to affect people, money, future IP options, and studio history.

## Core loop

Long-term target:

`Choose opportunities -> develop/continue an IP -> assemble a crew -> manage people, money and technology -> solve creative/production conflicts -> release -> absorb consequences -> evolve studio/cast/IP -> advance into new opportunities and media`

The game should produce stories through simulation rather than requiring scripted narrative for every campaign event.

## Studio economy

The economy should create clear management tradeoffs without turning T.O.O.N. into a detailed accounting simulator.

The core player-facing financial model should emphasize:

- **cash on hand**;
- **recurring studio burn**;
- **money/time committed to active productions**;
- a readable estimate of **runway** at the current burn rate.

Do not require the player to manage accounting minutiae such as individual consumables, invoice ledgers or tax-line bookkeeping unless a later proof demonstrates clear gameplay value.

### Main revenue paths

Use three broad revenue families:

1. **Contract work** — an outside client pays the studio to make something. Under **G-13**, the client owns the IP created for its commissioned work; the studio receives the agreed delivery payment, not ongoing ownership or automatic IP/catalogue exploitation rights. This provides more predictable income but less creative freedom and no studio-owned long-tail value from that commission.
2. **Original productions** — the studio funds its own work. This creates greater financial risk but can produce valuable persistent IP, stronger upside and long-term studio identity.
3. **Catalogue/IP revenue** — previously released work can continue generating value through mechanisms appropriate to the era, such as republication, syndication, distribution, licensing, adaptation or later equivalents.

The systemic distinction should remain stable even as the historical presentation changes. A commissioned strip, television job or later digital contract can all belong to the same broad contract-work model without requiring a completely different economy for every decade.

A central economic tension should be:

`predictable contract work <-> risky original production <-> long-tail catalogue value`

### G-14 — Hybrid revenue for studio-owned original productions

**Owner accepted option C (2026-11-16):** releasing a **studio-owned original work** may generate **initial commercial revenue at publication** and **subsequent catalogue revenue over time**. Both are grounded in the work's reception, audience, medium, distribution and historical context, using **game-owned simulation/accounting rules**. An original can earn little or nothing, recoup its costs, or become a long-running success. Neither immediate profitability nor continuing revenue is guaranteed, and the timing/rates/decay of later earnings are **balancing and validation parameters**, not approved fixed numbers.

- **Publication boundary:** no initial or catalogue revenue accrues before the player's explicit G-08 release. On release, process any initial commercial result **once**, independently of ongoing catalogue income thereafter; save/reload must not duplicate release proceeds or historical ticks.
- **Recurring value:** published studio-owned originals can produce subsequent income as simulation time passes; actual revenue may fluctuate or fall to zero depending on the game-owned reception/distribution model. Do not equate permanent archive storage with permanent positive income.
- **No mandatory sales minigame:** ordinary publication can participate in this hybrid model without requiring the player to negotiate distribution for every production. Optional later publishing/marketing infrastructure under G-08 remains unapproved in its exact mechanics.
- **Ownership separation:** client-owned commissioned IP remains excluded from studio-owned release/catalogue earnings under G-13; G-11 contract delivery payment continues separately. For employee-originated studio productions, the existing originator's **5% participation on revenue from that production and its direct catalogue revenue** remains applicable; do not multiply it across unrelated works using the same IP.

### How productions originate

A production can begin from three sources that converge into the same production pipeline:

1. **Player initiative** — the player starts an original production, choosing the production type and using an existing IP or creating a new one.
2. **External contract** — an outside client offers a bounded job that the player can accept or reject.
3. **Internal proposal** — one employee proposes a specific creative project based on their interests, experiences, relationships, IP context or current historical/cultural context.

**G-03 accepted concept-authoring boundary (2026-11-16):** all three origins converge on a **concept form**, but they arrive with different editable fields:

- **External client/agent proposal:** concept and terms arrive partially populated. The player may review them and edit only fields explicitly negotiable/editable under that proposal; mandatory client requirements and **client ownership under G-13** remain fixed. **Every external contract concerns IP that does not belong to the studio; existing studio-owned IPs are ineligible for this proposal origin.** Accepting/rejecting the offer remains separate from editing its allowed creative fields.
- **Internal employee proposal:** the originating employee provides a partially populated concept. The player may keep or edit the fields the proposal exposes before approving it as a production. The employee still retains the established single-originator credit and participation rules when the proposal is accepted.
- **Player-originated proposal:** the player may fill a concept from scratch, accept contextual default/pre-filled values and edit them, or ask the game/local creative system to fill suitable fields automatically. Auto-fill is **optional**, never a requirement to type every field.

Concept field schema and editable/locked masks depend on origin and offer constraints; the player must see which fields can be changed. Do not let a cosmetic edit implicitly rewrite an accepted external contract or confuse employee originator credit.

**After the concept is accepted**, it becomes the persistent physical production object and must be taken to the **first creative station: scriptwriting**. Creative generation/automatic filling does not mean the player relinquishes control of where the production physically goes next.

Internal proposals have **exactly one originator**. Do not model co-originated internal pitches in the base system.

If an internal proposal is accepted and becomes a production:

- the originator receives persistent creator/proposer credit;
- the originator receives a fixed **5% of the revenue received by the studio from that production**;
- the percentage is a tunable design value, not a historical/legal claim;
- the participation continues even if that employee later leaves the studio;
- the participation applies to that specific production and its direct catalogue revenue, not automatically to every future production using the same IP;
- studio ownership of the IP remains separate from the employee's credit and revenue participation.

This rule is intentionally fixed rather than negotiated per employee so internal proposals remain easy to understand.

### External contract terms

External contracts should remain compact and legible. A contract can define:

- client;
- production type;
- brief;
- mandatory requirements;
- deadline;
- guaranteed payment;
- **client ownership of commissioned IP (G-13; fixed, not a negotiable right transfer)**;
- optional bonuses;
- contractual **lateness penalties** where explicitly defined (subject to G-05); **quality, brief compliance and mandatory-content shortfalls after delivery affect studio reputation and future offers, not acceptance, rejection or withheld/reduced guaranteed payment** (G-12). Early project abandonment follows the global G-06 cancellation formula, not a contract-by-contract negotiated cancellation percentage.

The base interaction is an offer that can be **accepted or rejected**. Advanced clause-by-clause negotiation is not required for the core system.

### G-13 — Client ownership of commissioned works

**Owner accepted option A (2026-11-16), clarified by owner:** **every external contract is exclusively about IP not owned by the studio**. The commissioned IP belongs to the **client**, not to the player's studio. The contract pays for delivery under G-11; after delivery the studio cannot independently commission sequels, remakes, adaptations or reuse the commissioned characters/property as its own IP. Do not introduce negotiable split ownership, automatic licensing, revenue shares or studio catalogue royalties for such commissions. This is a **gameplay ownership rule**, not a claim about real-world copyright law.

- **Archive is not ownership:** the completed work remains visible in the studio's immutable published history with its credits, delivered artifact and client-owner attribution. Historical display and review do **not** imply rights to commercially exploit the client's IP.
- **Studio-owned original work remains separate:** player-original and eligible employee-originated studio productions follow their own IP/participation rules; G-13 does not remove the accepted employee-originator 5% rule for qualifying internal proposals.
- **Hard origin boundary:** external offers **never** reference, reuse, adapt, license, buy or transfer IP already owned by the studio. Such offers are **invalid and must not be generated or accepted**, rather than postponed as a future contract type. Player/employee-original studio IP remains on its separate studio-owned production path. An external offer may contain client-provided IP or commission new client-owned IP; in neither case does it belong to the studio.
- **Do not infer continuing studio income:** commissioned work does not generate studio-owned catalogue/licensing/adaptation income merely because it is in the published catalogue. Any hypothetical future licensing/participation exception requires a separate owner decision.



**G-12 accepted (owner correction 2026-11-16): delivery is final.** There is no post-delivery client acceptance/rejection stage, rework request, approval gate or non-payment/quality-based reduction for a delivered work. At player-authorized publication/delivery (G-08/G-11), the guaranteed contract payment becomes due under the existing payment rule. **Quality, creative execution and how well the work meets the brief** inform the studio's **reputation**, which in turn directly affects both the **value and frequency of future external contract offers**. Do not create a client veto of a published work, or make subjective AI scores authoritative for money. This does **not** silently repeal already accepted explicit contract-deadline penalties (G-05); lateness remains a separate rule.

`delivered artifact + production/brief evidence -> global studio reputation + relevant production-type reputation -> future contract offer value and frequency`

### G-15 — Hybrid studio and production-type reputation

**Owner accepted option C (2026-11-17):** track **one global studio reputation** and **one production-type reputation for each of the four accepted types**: comic strip, comic, 2D animation and 3D animation. The studio's overall standing and its specific track record in the relevant production type **both influence the value and frequency of future external contract offers**. Strong results in one type can help the studio enter another through its global reputation, without automatically awarding equal competence/reputation in an unfamiliar type. Poor work can likewise have persistent consequences in the relevant specialization and the studio's general standing.

- **No permanent specialization lock:** a studio may enter new production types when other existing gameplay requirements allow it; an inexperienced type does not inherit a fully established specialist reputation merely from global fame.
- **Reputation follows authored outcomes:** at delivery/release, game-owned evaluation of relevant evidence may update global and corresponding type-specific reputation, without creating a client approval/rejection stage or altering G-11's guaranteed delivery payment for quality reasons (G-12).
- **One legible system:** present global and four type-specific reputations as facets of the studio, not separate departments or independently micromanaged reputation subsystems. Starting values, aggregation/transfer weights, change magnitude, decay, offer-frequency/value response and UI details require **balancing and validation**; do not invent numeric multipliers.
- **Ownership independent:** commissioned work remains client-owned under G-13; its delivery performance may still inform studio reputation. Studio-owned original work follows G-14 for revenue, independently of the reputation model.


Game-owned rules determine reputation and future offer generation from bounded, provenance-aware evidence, using **G-15's global plus production-type reputation**. AI may dramatize reactions or provide evaluation evidence, but cannot directly change cash or authoritatively reject delivery. The exact reputation coefficients, memory/decay and offer-response curves require later balancing/validation.

### G-11 — External contract payment on delivery

**Accepted owner choice (2026-11-16): option B, payment at delivery.** Accepting a client contract **does not deposit any money** into studio cash. There are **no upfront advances or milestone/instalment payments** in the base external-contract payment flow. The player finances all ongoing studio and production costs until the commissioned work reaches **player-authorized release and contract delivery**, at which point the game-owned finance system posts the **guaranteed contract payment once**, subject only to separately accepted explicit financial terms such as **lateness penalties** (G-05). **Quality, brief compliance and creative merit do not gate, reduce, reject or delay this guaranteed payment**; G-12 routes those outcomes through studio reputation and subsequent contract-offer value/frequency instead. Do not invent client approval, post-delivery rework or AI-authoritative financial vetoes.

- **Ready is not delivered:** completed work may wait unpublished at the G-08 physical publishing endpoint. Waiting creates no contract income and does not suspend its contractual deadline.
- **Abandoned work is unpaid:** under G-06, trashing an unreleased contracted project forfeits its delivery payment and posts the **global X% guaranteed-payment cancellation fee**; there are no client advances to refund or offset under G-11.
- **No cash-flow shortcut:** a prospective guaranteed payment is shown as expected future income, **not current cash** or a realized receivable to spend before delivery. Persist the delivery/settlement state and prevent duplicate credit or penalties after save/reload. Exact payment amounts and previously accepted explicit deadline-penalty coefficients remain balancing/contract data; reputation and future offers follow G-12.

### G-06 — Abandoning an accepted external contract

**Accepted owner design (2026-11-16):** the player may **abandon an already accepted external contract by trashing its unreleased production project**. This is allowed at any pre-release production stage; there is no requirement to finish the contracted work. Trashing an original/self-funded unreleased project only destroys that project without reimbursing spent money; abandoning a **contracted** unreleased project additionally triggers the cancellation settlement below.

- **Fixed global cancellation formula:** the cancellation charge is **X% of the contract's guaranteed payment**, independent of the production's elapsed time, stage, progress or client. **X is a global balancing parameter**, not a variable contract clause or a presently accepted numerical rate.
- **Consequences:** project data/drafts/artifacts are deleted permanently, committed money already spent is **not refunded**, the accepted external contract is **terminated**, the cancellation charge is booked once to studio finances, and **no future payments for completing that abandoned contract** are owed. Do not double-charge sunk costs as a new deletion fee or invent retroactive refunds.
- **Player confirmation:** before destructive trash, clearly display that the contract will end, the **new cancellation charge**, non-refundable already-spent costs and the loss of remaining contracted payment. Declining this confirmation leaves the project and contract intact.
- **State integrity:** persist the cancellation's financial/contract consequences even though the unreleased project is deleted. Save/reload and queued generation must not resurrect the project or duplicate the cancellation charge. There is no separate cancelled-project archive entry or post-publication trash path.

**G-11 eliminates advances and partial client payments from the base contract flow.** Therefore G-06 abandonment creates **only** the fixed-percentage cancellation fee and forfeits the unpaid delivery settlement; do not invent refunds, deposits, offsets or a second cancellation-fee model.

### Main cost families

Keep costs concentrated in categories the player can understand and act on:

- salaries and employment-related costs;
- studio space and recurring operating costs;
- production-specific expenses;
- facilities/equipment;
- technology adoption/upgrades;
- selected discretionary spending such as recruitment, expansion, training or promotion where those systems exist.

Production budgets should remain compact. Prefer:

`crew time + specific production expenses + required facilities/technology`

over a large accounting breakdown with many low-value line items.

### Production spending authority and schedule slippage

**Accepted owner rule (2026-11-16): after the player commits to a production's current budget, automatic work, failed internal attempts and automatic technical AI recovery do not recalculate or increase that production's cost.** Those attempts can extend the estimated/actual production schedule. **Only an explicit player request for a new creative version/rework at an eligible stage triggers a new calculation of that work's production cost**; communicate the cost consequence to the player. This keeps incremental creative spending under player direction and does not create a pay-per-inference fee.

This rule applies to **production-specific budgeting and version generation**, not an automatic freeze of all studio finances. Existing recurring studio operating costs, salaries, other player-authorized financial commitments and cash/runway continue to obey their established game rules as simulation time advances. Do not book an additional production fee merely because a background generator retried. Any contractually specified lateness penalty is a **separate existing contract obligation**, not a hidden regeneration charge. **G-05 below** defines a bounded technical-delay grace against such deadlines; this does not freeze the simulation or guarantee that every resulting late delivery is penalty-free.

Conceptually:

`automatic internal failure/retry -> possible production delay; production budget unchanged`

`player requests new version (while version slots remain) -> recalculate/communicate new production cost + schedule consequence`

### G-05 — Bounded contract-deadline grace for technical AI failures

**Accepted owner choice (2026-11-16): option C, partial compensation.** If an accepted external contract's production is delayed by **verified technical generation failures or automatic technical retries**, it may receive **limited, capped grace** for evaluating that contract's deadline and lateness penalty. This is neither a permanently suspended contract clock nor an unconditional deadline extension: once the bounded allowance is exhausted, further lateness is treated under the contract's normal terms. The precise allowance, accumulation and cap are **balance/implementation parameters**, not yet fixed.

- Only **game-owned evidence of technical generation delay** qualifies. Do not classify poor artistic quality, an ordinary creative revision, player-requested new version, staffing/management decisions, missing equipment or ordinary production slippage as an AI technical failure eligible for grace. Do not double-count overlapping delay intervals.
- The **world clock, studio operating burn, salaries, financing instalments and other unrelated obligations continue**. Grace affects only the relevant **contract deadline/late-penalty assessment**, not production-budget accounting or the actual passage of time.
- Show the contract's base deadline and any applied/remaining technical allowance clearly enough for the player to distinguish ordinary lateness from protected technical delay. Preserve the allowance and its causal evidence across save/reload; do not regrant it when a failed job is retried or a save is loaded.
- Ordinary contract penalties remain possible after grace is exhausted. No new technical-failure production charge or creative-version consumption is implied; G-02 remains the source of those rules.

### Financial pressure and failure

The player should be able to understand financial danger before it becomes terminal. The UI should expose a clear burn-rate/runway signal such as an estimate of how long the current cash position can sustain current recurring costs.

### G-04 — Financial distress, repayable financing and forced studio sale

**Accepted owner design (2026-11-16; revised by owner after original zero-debt/no-new-loan interpretation):** do **not** introduce a broad bankruptcy-rescue menu (asset-liquidation options, mandatory restructuring packages, repeated financing negotiations, etc.). Financial danger should emerge through the normal contract market and employee agency. The studio may have **one active emergency financing at a time**: first eligible crisis offers financing, a second threshold breach while it remains unpaid forces sale, and **full repayment restores eligibility for a future financing offer**. This supersedes the earlier permanent one-rescue-per-campaign limit.

- **Distressed market:** as the studio runs into financial difficulty, **third-party project offers become more frequent**, but generally offer **more oppressive commercial terms** (e.g., lower pay for the work or harsher requirements). Their frequency and severity should scale with financial distress and use the existing proposal/contract flow, not a separate emergency-project minigame. The player still chooses whether to accept each offer.
- **Unpaid staff:** when the studio fails to pay employees, affected professionals may, depending on personality, relationship, circumstances and their own financial pressures, **consider taking home a studio decorative object, miss work, or accept another studio's job offer**. These are **possible** authored/simulation outcomes, not automatic universal punishments or a new direct player action menu. The stolen/removed prop is a physical workplace consequence; absence and departures affect workforce/production state. Preserve coherent object and staff persistence. Unpaid obligations are not silently erased.
- **Eligible negative-cash threshold event — rescue plus repayment obligation:** when the studio **does not have an outstanding emergency financing** and crosses the configurable negative cash threshold, present the rescue offer. If accepted, it **settles pre-existing financial debt and overdue obligations (including unpaid salaries)** and leaves a **positive operating cash reserve**. The amount is calculated from the actual deficit/obligations **plus a tunable extra cash buffer**, without double-counting items already reflected in authoritative cash/liability accounting. **The old liabilities are cleared, but the accepted rescue itself creates a new, separately tracked repayable financing obligation**. Do not label the studio as globally debt-free while this financing remains outstanding; do not silently reinstate the discharged old debts. **Repayment method accepted (owner, 2026-11-16): scheduled instalments are charged automatically to studio finances**, with no manual payment or early-payoff action in the base game. The payment schedule and outstanding balance must be visible so the player can anticipate cash-flow pressure. The instalment amount, frequency, duration and interest (if any) are **not yet specified**; those parameters are deferred for tuning and implementation. The repayable obligation and full-payment eligibility reset remain accepted.
- **Repayment resets the insolvency cycle:** when the active rescue obligation is **fully paid**, the game clears its outstanding-financing status and **resets the terminal-risk/eligibility condition**. A subsequent independent downward threshold crossing is again treated as a **first eligible insolvency**, offering financing, not immediate game over. **Partial repayment does not reset the condition.** The game must persist active-financing identity, remaining balance, repayment completion and the crisis cycle across save/reload.
- **Second negative-cash threshold event while financing is unpaid:** after rescue and recovery above the threshold, if the studio **crosses the same threshold downward again while the rescue has an outstanding balance**, the company is **forcibly sold and the campaign ends**, without another financing offer. This is a distinct crossing, **not** a counter that increases every tick/day within one continuous deficit. If financing was **fully repaid before that crossing**, the insolvency cycle has reset and the next crossing is again eligible for a rescue, instead of forcing sale.
- **Game-over epilogue:** on forced sale, show a studio retrospective plus bounded, coherent **what-happened-next** outcomes for relevant **IPs, employees and competitors**. These follow from saved game history and game-authored/procedural outcome rules; local AI may dramatize them but does not independently invent authoritative changes. The epilogue is a narrative payoff, not a continuing post-sale player management mode.

**G-04 final decision on insolvency choice (accepted by owner 2026-11-16):** on the **first eligible downward crossing** of the negative-cash threshold **without an active unpaid rescue**, **pause the simulation immediately** and open a **mandatory financing Decision Event** with exactly two outcomes:

1. **Accept financing:** settle old debts and overdue obligations, grant the calculated positive operating buffer and create the separate repayable emergency-financing obligation. The crisis is resolved and the simulation may resume; the player does not remain trapped in an indefinitely negative-cash state.
2. **Decline financing:** the studio is **compulsorily sold immediately** and the campaign terminates in the established retrospective and epilogue. Make the irreversible consequence unambiguous before confirmation; do not allow simulation time to advance behind this decision.

While the decision is open, do not process further financial ticks, repeatedly fire the threshold event or offer a different bailout. A **second independent threshold crossing while the previous rescue has not been fully repaid** instead proceeds directly to forced sale/game over, with **no** financing choice. If that rescue was **fully repaid**, the insolvency cycle is reset and the **next separate crossing** is again eligible for the same pause-and-decide event. Saving/reloading at a pending choice must not lose or duplicate the event or consume eligibility. Exact cash threshold, repayment mechanics, buffer sizing and event presentation remain tuning/implementation work, not additional design votes.

Financial health warnings, cash, burn rate, obligations and runway remain legible before the threshold. Normal production and contract choices remain possible while the studio can operate. **The rescue's positive cash buffer funds continued operation, but it does not erase the history of missed payments or reverse employee absences, departures, damaged relationships, missing props or other already-applied consequences.** Routine salaries, studio burn and newly incurred contractual obligations still apply after the rescue; an otherwise unviable operation can spend through the reserve and fall into financial trouble again. A forced sale here is a **game-design terminal event**, not a historically accurate statement about bankruptcy, creditor law, employment law or corporate acquisitions.

**Automatic repayment and insufficient cash (owner accepted 2026-11-16):** each scheduled instalment is **charged in full on its due date even when the studio has insufficient available cash**. The cash balance may become negative; the scheduled charge reduces the outstanding financing balance accordingly. There is **no separate skipped/missed-payment state**, default surcharge, late-payment fine, extra penalty, dedicated delinquency event, manual repayment or prepayment action. The resulting cash position is handled through the **existing negative-cash threshold/insolvency rules**: if the charged instalment causes a distinct downward threshold crossing while the rescue remains unpaid, that crossing triggers forced sale/game over. If the scheduled charge pays the financing **fully**, the rescue eligibility resets upon complete settlement, and the post-charge cash position is evaluated consistently with that settled balance; do not classify a fully settled loan as still outstanding. Persist the payment and trigger transition atomically to avoid double posting after save/reload. The repayment amount, frequency, duration and interest (if any) remain tunable and unvalidated.

**G-04 insolvency decision gap closed:** declining the mandatory first-eligible financing offer **ends the game immediately** by forced sale. Accepting applies the rescue in the paused event before normal simulation resumes; there is no indefinite continuous-below-threshold waiting state, no extra countdown and no repeated financing offers during the same crisis. The threshold must trigger once per distinct crossing, and the event/rescue state must persist across save/reload. The negative threshold, re-arming/hysteresis implementation, repayment terms, offer weighting, employee probabilities and epilogue content remain tunable and unvalidated.

Exact credit, bankruptcy, employment and legal rules must be sourced for the relevant era/location before being presented as historical fact.

## Studio space, facilities and workplace culture

The studio is a physical system that grows with the company.

The player should be able to expand the workplace over time by acquiring space, building rooms/departments, and buying objects that affect both production capability and the people who work there.

Studio purchases fall into several broad categories.

### Production infrastructure

These directly enable or improve work:

- writing desks and editorial equipment;
- drawing/inking stations;
- cameras and animation equipment;
- sound/recording spaces;
- projection/review rooms;
- computers/workstations;
- render infrastructure;
- storage/archive capacity;
- specialist department rooms.

Production infrastructure should primarily affect what the studio can make, how efficiently it can make it, and what workflows become possible.

### Shared workplace amenities

These improve the lived experience of the office:

- break rooms;
- kitchen/coffee;
- lounge/rest spaces;
- better lighting;
- climate control;
- quiet rooms;
- music/radio;
- recreational objects;
- comfortable furniture.

These should influence morale, recovery, social interaction, concentration, or conflict rather than acting as universal flat bonuses.

### Professional-facing props and personalisation

Professionals may react differently to objects and spaces.

Examples:

- an artist may value reference shelves, plants, natural light, or a large drawing table;
- a writer may prefer privacy, books, a typewriter, cigarettes in an era where appropriate, or a chaotic shared room;
- an anxious prey character may dislike being seated beside a hunter;
- an immortal veteran may insist on keeping an obsolete desk or tool for decades;
- a technically minded employee may become happier when new equipment arrives;
- a nostalgic character may prefer older tools even after better technology exists.

A prop should ideally answer at least one of:

- does this help someone work;
- does this help someone recover;
- does this change social behaviour;
- does this express studio identity/history;
- does this satisfy or annoy a specific professional.

Avoid reducing every prop to generic `+X Creativity` or `+Y Happiness`.

### Culture and identity

Decoration can make the studio feel like **this campaign's T.O.O.N.** rather than a generic office.

Potential sources include:

- posters from old productions;
- framed strips/comic covers;
- awards;
- employee portraits;
- props from films;
- old equipment retained after replacement;
- memorials;
- joke signs and bureaucratic notices;
- department-specific decoration;
- souvenirs from failed/successful productions.

Historical objects can carry both emotional and mechanical value.

For example, preserving the original 1900 writing desk in a 2030 headquarters may:

- improve morale for nostalgic veterans;
- reinforce studio identity;
- irritate a modern producer who wants the space;
- become part of the archive/museum;
- trigger stories or memories tied to old productions.

### Space and adjacency

Room layout may influence the simulation where it creates meaningful decisions.

Possible effects include:

- shorter collaboration distance;
- concentration/noise;
- cross-department contact;
- social friction;
- exposure to predators/hunters;
- access to equipment;
- crowding;
- privacy;
- visibility/status of offices.

Do not make the player micromanage furniture placement purely for optimization unless the placement creates readable, interesting tradeoffs.

### Professional preferences

Professionals may have lightweight environmental preferences such as:

- likes quiet;
- likes crowds;
- wants natural light;
- hates clutter;
- loves clutter;
- prefers old technology;
- wants cutting-edge equipment;
- needs privacy;
- enjoys social spaces;
- wants prestige/status;
- strongly values a specific personal object.

These preferences should combine with personality, role, relationships, era and current state.

The same object may make one employee happier and another less productive.

### Growth over time

Studio expansion should be visible across the campaign.

A possible progression:

`one room -> shared office -> specialist rooms -> multi-department studio -> expanded lot/building -> modern production campus`

Growth should follow needs created by people, media and production scale rather than existing only as a linear upgrade tree.

## Studio professionals

Studio professionals are recurring characters, not interchangeable worker resources.

A professional may include:

- stable identity;
- visual/species/archetype identity;
- role/discipline;
- skills and strengths;
- happiness/morale;
- creative energy;
- discipline;
- wildness/experimentation;
- ambitions;
- salary/credit expectations;
- work history;
- relationships;
- life outside the studio;
- longevity/aging model;
- current assignment/state.

Depth should come from readable behaviour and history, not hundreds of opaque attributes.

### Employment, workstations and studio capacity

T.O.O.N. should use **permanent employees only** as the player-managed workforce. Do not add a parallel temporary-worker, contractor or freelancer staffing layer to the core management model.

Hiring capacity comes from the physical studio rather than an abstract global employee cap.

A new employee can be hired only when the studio has an available **compatible workstation/capacity slot** for that role. Examples include:

- an illustrator/drawing desk supporting one artist;
- a specialist workstation supporting a compatible production role;
- a mocap room providing several distinct compatible positions;
- another room or production facility exposing one or more role-specific capacity slots.

The principle is:

`built productive capacity -> available compatible position -> employee can be hired`

The game should not impose an unrelated rule such as “maximum 25 employees” when the studio itself can express the constraint.

Workstations represent productive capacity, not permanent ownership by one employee. The player may reassign compatible employees as production priorities change.

Removing a workstation **does not automatically fire an employee**. Employment and productive capacity are separate states. If the studio temporarily has more employees than compatible positions:

- affected employees remain employed and continue receiving salary;
- the game clearly identifies the capacity shortfall;
- employees may still socialize, rest and perform appropriate non-station activities;
- their normal role productivity is reduced or blocked;
- prolonged inability to work can affect morale, relationships or generate management pressure;
- the player can solve the problem by rebuilding/reassigning capacity or explicitly dismissing an employee.

Because construction/build mode pauses simulation, the player may reorganize workstations freely while building. Capacity and assignments are reconciled when returning to live simulation.

### Dismissal and voluntary departure

Ending employment should remain mechanically simple even when its consequences are meaningful.

For a player-initiated dismissal, the core interaction is:

`select employee -> Dismiss -> confirm`

There is no mandatory negotiation minigame, notice-period simulation or playable handover phase. Once confirmed, the professional leaves the active workforce immediately.

Any legally or historically appropriate notice, severance, contractual obligation or equivalent cost should be represented through **abstracted economic/rule consequences appropriate to the era and location**, rather than requiring the employee to remain physically simulated for a notice period. Exact legal/historical rules require sourced data before becoming canonical mechanics.

Dismissal can still create persistent consequences such as:

- salary/severance or other economic cost where applicable;
- morale changes among colleagues;
- relationship changes toward management or the dismissed professional;
- subjective memories and grudges;
- reputation effects where later systems support them;
- disruption to productions/responsibilities;
- later return, re-hire or rival-studio opportunities.

The severity should depend on context. Dismissing a respected veteran with strong relationships should not feel equivalent to dismissing a recently hired, socially isolated professional.

Professionals may also **resign autonomously**. Plausible causes include compensation, lack of recognition, conflict, burnout, blocked career goals, outside-life changes or an external opportunity.

Some impending resignations may escalate into a Decision Event when player authority could plausibly change the outcome. Others may occur directly when the underlying situation is sufficiently established and no meaningful management decision remains.

Departure does not erase the person from history. Former employees can remain in character memory, production credits, relationships, archive/history and future recruitment/re-encounter systems.

### Recruitment channels across eras

Hiring should not come from one timeless global candidate list. **How the studio discovers candidates evolves across the campaign**, and early recruitment should feel much more constrained than modern recruitment.

Accepted directional channels include:

- **Walk-in applications** — especially early in the campaign, a potential employee may physically arrive at the studio to leave a résumé/application. This is a relatively rare event, so the player may have very few candidates to choose from.
- **Employee referrals** — an existing professional may occasionally recommend someone from their network. Referrals are also relatively rare and can carry useful social context because the recommendation comes through a known employee.
- **Newspaper job advertisements** — as the studio grows, the player can actively place a job advertisement. The advertisement increases the flow of applicants who then appear/contact the studio. This can become especially relevant during the animation-industry growth periods, but its availability should not imply that newspaper employment ads historically began only then.
- **Modern digital professional network** — in later eras, the studio gains access to a computer-based recruitment interface analogous to a professional network such as LinkedIn. This allows active searching/browsing of a larger candidate pool rather than waiting for applicants to arrive physically.

The progression should broadly move from:

`scarce inbound opportunities -> referrals -> active mass recruitment -> searchable digital talent market`

These channels change **discovery and access**, not the permanent-employment rule. A discovered candidate can still only be hired when the studio has compatible productive capacity.

Candidate information should remain **evidence-based and incomplete**, not a perfect readout of hidden simulation values.

Before hiring, the player may see information such as:

- role/discipline and claimed experience;
- work history;
- portfolio or representative prior work where appropriate;
- salary/credit expectations;
- education/training where relevant;
- who referred them, if anyone;
- references or endorsements where the channel supports them;
- broad qualitative impressions rather than exact hidden numbers.

Different recruitment channels provide different evidence and should also have distinct **presentation hints**:

- **Employee referral** — the recommending professional may offer a short subjective comment about the candidate. The comment may mix useful information with bias, friendship, humour or concern. For example, a referrer might effectively say that a friend has a serious personal vice but is an exceptional artist.
- **Walk-in applicant** — the candidate can physically wait at the studio entrance. While waiting, comic-style thoughts can provide flavour or ambiguous foreshadowing, and clicking the candidate can trigger a short spoken line. These are not interviews and do not unlock additional probing.
- **Newspaper applicant** — the application can remain comparatively document-driven, with résumé/portfolio evidence and limited personal context.
- **Modern professional network** — the profile exposes a broader work history, skills, credits and connections, but testimonials/endorsements are intentionally **over-positive and exaggerated**. A mediocre candidate may still have praise equivalent to “the greatest artist alive; only a fool would pass.” This makes endorsements entertaining but lowers their evidentiary confidence.

Thoughts, comments and testimonials are **signals, not omniscient truth**. They may be sincere, evasive, biased, self-promotional, mistaken or deliberately comic. If a hint relates to an actual hidden trait, the game controls what can be surfaced; the generative model must not invent a new canonical secret merely to make a funny line.

Some attributes should remain uncertain until the person actually works in the studio. Examples include:

- real reliability under pressure;
- interpersonal compatibility;
- hidden ambitions or insecurities;
- true tolerance for overtime or chaos;
- unusual habits and outside-life complications;
- whether apparent skill translates into the studio's actual workflows;
- private or secret traits the studio has no reason to know.

Where useful, the UI can communicate **confidence** rather than false precision: `Unknown`, `Limited evidence`, `Promising`, `Well established`, or similar qualitative signals.

A referral or strong portfolio can improve confidence in a claim without making that claim infallible. Characters and documents can themselves be biased, outdated, incomplete or self-promotional.

The goal is for hiring to contain informed uncertainty:

`available evidence + recruitment channel + studio knowledge -> hiring judgment -> later discovery through employment`

There is **no separate interview mechanic** in the core hiring flow. The player does not question candidates, run a branching dialogue scene, perform a recruitment minigame, or spend another interaction step to reveal hidden attributes.

A candidate may still speak a short ambient/click line, think visibly where the presentation supports it, or be described by a referrer. Those are flavourful hiring cues, not an interview system and not a way to exhaustively inspect the candidate.

Once a candidate is available, the core decision is simply:

`Hire / Do not hire`

Any uncertainty that remains after reviewing the available evidence is resolved only through later employment, observable work, behaviour, relationships and history.

Do not turn uncertainty into arbitrary hidden punishment. Important discoveries should emerge through observable work, behaviour, relationships and history.

The modern professional-network presentation should use an original in-world identity rather than requiring the real LinkedIn brand.

### Working, idle and blocked states

A professional who is not currently producing should not simply freeze.

At minimum, distinguish:

- **Working** — actively performing meaningful productive work;
- **Available / Idle** — able to work but currently has no relevant assigned task;
- **Blocked** — has work to do but cannot proceed because of a missing workstation, unavailable equipment, dependency, required collaborator, material or similar constraint.

Idle time is an **autonomous character-expression state**, not a command queue controlled by the player.

When Available/Idle, a professional chooses what to do according to personality, current emotional state, ambitions, discipline, relationships, interests, outside-life hooks and the opportunities available in the studio.

Possible idle behaviours include:

- study, practise or experiment and slowly develop a skill;
- socialize, gossip, flirt, mentor or seek company;
- encourage or entertain colleagues;
- rest or simply enjoy studio amenities;
- become bored, insecure, lonely, frustrated or depressed by prolonged lack of meaningful work;
- pursue hobbies or personal projects;
- play jokes or pranks on colleagues;
- engage with off-site responsibilities or secret activities, including vigilante behaviour where appropriate;
- observe colleagues or productions and form new opinions, interests or ambitions.

These are examples of behavioural families, not a fixed list that every character can choose from.

The same idle duration should therefore have different consequences for different professionals. A disciplined, ambitious employee might study; a social character might strengthen relationships; an insecure employee may interpret prolonged idleness as evidence that the studio no longer needs them.

There is **no universal idle-time threshold** after which a professional becomes unhappy or insecure. Idle tolerance and interpretation should depend on context such as:

- personality and ambition;
- confidence and perceived job security;
- salary and expectations;
- recent workload and burnout/recovery needs;
- recent production involvement and recognition;
- relationships and social belonging;
- whether the employee is using the time in a personally meaningful way;
- how long the pattern has persisted relative to that character's expectations.

A period that feels like welcome recovery to one professional may feel like neglect or impending redundancy to another.

The player **does not directly order idle behaviours** such as `Study`, `Socialize` or `Prank X` as the normal management model. The player influences them indirectly through hiring, assignments, environment, amenities, policies, relationships, management conversations and the amount/type of unassigned time.

Idle activity may create bounded social, recovery, personal-development or outside-life consequences, but should not become a reliable source of major production progress for free.

An Available/Idle professional may also **leave the studio during working hours on their own initiative** when their personality, interests or outside-life hooks make that plausible. This can represent ordinary personal errands, hobbies, relationships, vigilante activity, criminal activity, or other authored character-specific behaviour.

Leaving the studio is a real simulation consequence, not cosmetic flavour:

- the professional becomes temporarily unavailable for newly assigned work or spontaneous collaboration;
- the player does not directly order the off-site activity as part of normal idle control;
- there is no separate recall/call-back mechanic; the professional remains unavailable until they return naturally;
- the character may later return with altered energy, morale, injury, relationship state, knowledge or another relevant consequence;
- repeated or risky off-site behaviour can create future management pressure or Decision Events;
- legibility matters: the player should be able to tell that the employee is away and, where appropriate, understand the known reason without automatically revealing secret information the studio has not learned.

Blocked behaviour should be biased differently from ordinary idleness. A professional who has assigned work but cannot proceed is more likely to wait, seek another route, complain, help elsewhere where appropriate, or accumulate frustration around the cause of the block.

The distinction must be legible to the player: “nothing assigned” and “cannot do assigned work” are different management problems.

## Character ontology and lifespan

T.O.O.N. intentionally allows different kinds of beings to coexist in one workplace.

Appearance/species and lifespan are separate concepts.

A character may visually be a:

- human;
- anthropomorphic animal;
- creature/monster;
- living object;
- other authored cartoon archetype.

Separately, the character has an **existence/longevity model**.

Candidate longevity models include:

### Mortal

Ages broadly like a human. Can grow older, retire, and die.

### Long-lived

Ages, but on a slower or non-human timescale.

### Cartoon-static

Can remain visually and biologically at roughly the same apparent age for decades or centuries unless a specific event changes them.

A grumpy elderly cartoon hired in 1930 may still be the same grumpy elderly cartoon in 2030.

### Conditional / rule-bound

Longevity follows a character-specific rule rather than ordinary biology. Examples might include magical, mechanical, cursed, resurrecting, or other cartoon-logical conditions.

The game should not require every employee to share one biological model.

This creates meaningful long-term cast structures:

- mortal employees create generations, succession, retirement, mentorship, and loss;
- immortal/static cartoons create institutional memory, ancient grudges, recurring mentorship, and comic continuity;
- mixed teams create relationships that can span radically different lifetimes.

Immortality must not imply immunity from all consequences. An immortal character may still:

- quit;
- be fired;
- be imprisoned;
- disappear;
- be injured;
- become unavailable;
- change profession;
- fall out with the studio;
- leave for a rival;
- return decades later.

## Management model and autonomous social simulation

The player represents the **management authority of the studio**, not a diegetic character and not a puppeteer controlling individual workers like playable Sims.

There is no player avatar, player-character aging, founder succession, heir system, management-character replacement or death mechanic required to explain the 1900–2030 campaign. The player's management authority persists across the full campaign without needing an in-world biological explanation.

Professionals may still refer to management, ownership or "the boss" where useful for dialogue and event framing, but those references do not imply a separately simulated player character.

The management layer should primarily let the player set context and constraints such as:

- role/discipline;
- production assignment and crew;
- priorities;
- schedule/budget pressure;
- compensation, credit and promotion;
- workspace/facility conditions;
- policies;
- direct management conversations;
- responses to important situations.

Professionals then execute and socialize with meaningful autonomy.

### Multiple productions, priorities and workload

A professional may contribute to **more than one production at the same time**, but this does not multiply their available time.

The player should manage responsibilities and priorities rather than manually allocating percentages such as `35% Project A / 65% Project B`.

The intended model is:

`assigned responsibilities + production priorities + deadlines/context -> autonomous work selection -> finite time actually spent`

When the same professional is important to several productions:

- they switch between compatible responsibilities according to current priority and context;
- simultaneous demand can delay one or more productions;
- excessive context switching can reduce effective productivity;
- long uninterrupted or repeated high-pressure work can accumulate fatigue and longer-term stress;
- the professional may autonomously pause, rest or stop working when their state makes continuing unreasonable;
- sustained overload may eventually create complaints, mistakes, absence, management pressure or Decision Events.

This makes staffing pressure a consequence of finite people rather than an abstract allocation spreadsheet.

### Autonomous social behaviour

Professionals should initiate ordinary social interactions without explicit player commands.

They may:

- chat;
- joke;
- argue;
- flirt where appropriate;
- mentor;
- complain;
- reconcile;
- gossip;
- react to recent work/events;
- build or damage relationships over time.

The player influences the conditions under which relationships develop, but does not normally issue commands such as `Talk to X` or `Befriend Y`.

### Conversation presentation

Ordinary workplace conversation should primarily appear as **short comic-style speech bubbles**, not fully voiced dialogue.

Sound can support reactions, emotion and readability without requiring every generated line to be voiced.

The studio is allowed to have more social life than the player can observe. A player who is looking elsewhere may miss ordinary conversations. This is intentional: routine social simulation is ambient life, not mandatory information.

Important state changes must remain legible through behaviour, relationship UI, warnings and later consequences even when the player did not read every line.

### AI-generated conversation and autonomous action selection

Runtime AI can generate dialogue and help choose bounded autonomous actions so behaviour reflects:

- character identity and personality;
- current relationships;
- recent events;
- production responsibilities and priorities;
- historical/cultural context where relevant;
- current internal state;
- fuzzy interpretations of that state;
- the concrete actions that are currently valid.

The authoritative state remains game-owned. Internal values may be continuous, while a fuzzy layer derives overlapping qualitative memberships such as `low`, `medium`, `high`, `exhausted`, `restless`, `confident` or `socially needy` where useful.

The game should assemble a bounded decision context containing:

- relevant state values and fuzzy interpretations;
- only the history/context needed for the current decision;
- valid targets;
- an allow-list of possible action tags with stable game-owned identifiers;
- any constraints needed to keep the choice legal.

Conceptually:

`authoritative state -> fuzzy interpretation -> bounded context + allowed action tags -> AI choice + dialogue/thought -> validation -> game executes action -> authoritative state update`

The model may return:

- one allowed **action tag**;
- optional speech;
- optional thought/internal reaction;
- bounded presentation metadata where useful.

The exact serialization format can be XML-like tags, JSON or another structured schema, but the contract must remain game-owned and machine-validated. Do not rely on parsing unrestricted prose to decide gameplay.

For example, the context might allow actions equivalent to `ContinueWork`, `TakeBreak`, `ChatWith(EmployeeId)`, `Study(SkillId)` or `LeaveStudioForPersonalActivity`. The model can choose among the valid tags and dramatize the choice; it cannot invent an unrestricted gameplay verb.

Before execution, the game validates:

- the action identifier is on the allow-list;
- referenced targets still exist and remain valid;
- current preconditions still permit the action;
- requested parameters remain within authored bounds.

Invalid, malformed or stale output is rejected and falls back to a deterministic or weighted game-owned choice.

The language model must **not directly mutate authoritative gameplay attributes**. Speech and thoughts are presentation unless accompanied by a separately valid structured action/outcome tag.

An interaction can therefore resolve through a bounded path such as:

`context + allowed actions -> generated tag/dialogue -> validation -> structured interaction outcome -> deterministic simulation update`

Candidate social outcomes include:

- bonding;
- disagreement;
- insult;
- support;
- mentorship;
- flirtation;
- intimidation;
- reconciliation;
- creative inspiration;
- tension increase.

The simulation owns the permitted magnitude and final change to relationships, fatigue, stress, morale, creative energy or other state.

A deterministic/weighted fallback must remain possible when the runtime character model is unavailable, overloaded or returns unusable output.

**Accepted G-02 character-response rule (2026-11-15):** if character inference takes too long or fails, the simulation promptly chooses an eligible, game-authored **action, speech line, thought or reaction** instead of leaving that character waiting. A broad, localized library of authored lines/reactions should be indexed by action intent, personality, emotional state, relationship, historical context and situation; availability/weights/repetition control belong to game-owned selection, not unrestricted text parsing. A late AI answer cannot override a fallback action already executed or mutate now-stale state. Authored responses may also be used proactively when an AI call would add little value. The exact timeout, library size and weighting are implementation/tuning decisions, not evidence of a currently built content catalogue.

### Character memory and subjective interpretation

Long-term character memory belongs to the **game simulation**, not to hidden conversational state inside the generative model.

T.O.O.N. should distinguish between:

1. **Canonical event history** — game-owned facts about what actually happened.
2. **Character memory/belief** — what a particular professional remembers, believes or feels about those events.

A character memory may reference a canonical event while storing a subjective interpretation. Two professionals can therefore remember the same incident differently, and either interpretation may be incomplete, biased or factually wrong without rewriting the underlying studio history.

A compact memory entry may contain:

- source event/reference where applicable;
- remembered summary;
- involved people, production, IP or place;
- subjective interpretation;
- emotional valence/sentiment;
- importance/salience;
- confidence or certainty;
- whether the memory/knowledge is private, shared or secret;
- timestamps/reinforcement metadata where useful.

Do not preserve every spoken line as permanent memory. Routine dialogue can remain ephemeral. Promote only meaningful events, discoveries, conflicts, achievements, promises, betrayals, relationships, production experiences and other context that can materially affect later behaviour.

Recent short-term context and durable long-term memory should be separate. A character can remember a significant event from decades ago without requiring the model to receive decades of transcript history.

Before a local generative cognition call, the game retrieves only memories relevant to the current situation:

`authoritative state + personality + relationships + relevant memories/beliefs + recent context + allowed actions -> local model`

Relevance can consider participants, production/IP, topic, recency, salience, emotional strength and current goals.

The generative model may use those memories to choose or dramatize behaviour, but it does not own the memory database and cannot silently rewrite canonical history. Any newly formed or changed memory must pass through game-owned rules.

This enables:

- grudges and loyalties that survive years;
- conflicting recollections of one event;
- pride or resentment around old productions;
- secrets known only to some characters;
- mistaken beliefs with real social consequences;
- later reconciliation or reinterpretation without changing what objectively happened.

### Local background character AI and cadence

The generative model used for **routine character cognition, bounded action choice, short dialogue and thoughts** should be **local and embedded with the game**, rather than requiring a remote service for ordinary studio behaviour.

This local character-AI layer is distinct from heavier generation used to create production artifacts such as images, audio or animation. **Those heavier runtime generators must also execute locally.** T.O.O.N. should not require paid remote inference APIs for normal gameplay or for creating player-facing production artifacts.

The distinction is therefore about workload and orchestration, not network location:

- character cognition uses smaller, frequent, latency-sensitive local inference;
- production generation may use larger local models, longer-running jobs and explicit queues;
- heavy generation may pause, throttle or schedule work according to available hardware without blocking the main simulation;
- exact quality tiers, model packs and hardware requirements remain subject to profiling.

Model selection should be **capability-oriented rather than hard-coded around one architecture**. T.O.O.N. may use:

- several small, specialized local models tuned for narrow game tasks;
- a small number of broader multimodal models;
- or one larger local model capable of serving several capabilities.

Prefer the smallest model architecture that meets quality, latency and consistency requirements on the target hardware. A larger unified model is acceptable when it materially simplifies orchestration or improves cross-task coherence without making the hardware/runtime budget unacceptable.

The game owns capability contracts such as character cognition, dialogue, image generation, voice/audio generation or animation generation. Concrete models are replaceable implementations behind those contracts.

The intended runtime pattern is **event-driven plus periodic background cognition**:

- fuzzy/game-owned simulation handles trivial continuous behaviour without model calls;
- meaningful state changes can request a generative decision immediately;
- a background scheduler periodically selects an eligible character/context for a bounded generative decision even when no major event has fired;
- the initial tuning target is that, during active live simulation with eligible characters, the character-AI system should not go much longer than roughly **two real-time minutes** without a generative consideration;
- this is a **system-level cadence**, not a requirement to call the model once per employee every two minutes;
- the cadence may be tuned after profiling and playtesting.

A scheduled consideration does not need to create a visible event. The valid result may be to continue working, take a break, think something privately, initiate a conversation, study, socialize, leave the studio, or perform another currently allowed action.

The scheduler should avoid synchronized bursts. Character eligibility, urgency, time since last meaningful generative decision, relationships, current workload and recent repetition can influence who receives the next cognition slot.

Local inference must run asynchronously so model execution does not block the game thread. If the world changes before a result returns, the same validation rules apply: stale or invalid actions are discarded or resolved through fallback behaviour.

No periodic generation is required while the game is closed, loading, or paused for menus/build mode. The cadence applies to active simulation, not wall-clock background progression.

The exact embedded model, quantization, inference backend, hardware floor and final cadence remain **Planned** until Unreal profiling proves acceptable memory, latency, thermals and frame-time impact.

### Preventive management

The player may prevent a later crisis by noticing context early and using normal management tools.

Examples:

- extend a deadline;
- reduce workload;
- change crew composition;
- grant leave;
- improve working conditions;
- adjust compensation or credit;
- change responsibilities;
- initiate a management conversation.

There is no abstract `Prevent Decision Event` button. Prevention emerges because the underlying causes changed.

### Decision Events

Routine interactions remain autonomous until a situation requires **player-level studio management authority**.

A Decision Event is a game-authored or game-authored-template situation that:

- is triggered by legible simulation state;
- represents a crisis, conflict or consequential production/people decision requiring owner intervention;
- auto-pauses the simulation when formally presented;
- presents meaningful structured choices;
- has authored consequence boundaries;
- may use AI for contextual dialogue/flavour without giving AI authority over the rule outcome.

The preferred technical/content model is a **small library of parameterized event archetypes** rather than hundreds of bespoke events.

Examples include:

- serious creative disagreement;
- demand for credit or promotion;
- threat to resign;
- relationship conflict disrupting production;
- dangerous predator/prey escalation;
- request for creative control;
- production crisis caused by an outside-life event;
- ethical or commercial dispute;
- external offer affecting a key professional.

The simulation detects eligibility; the authored event definition owns roles, allowed choices and consequence bounds; AI contextualizes/dramatizes the event; the player chooses; deterministic game rules apply the result.

### Escalation and warning

Many Decision Events should emerge through an observable escalation:

`ordinary interaction -> developing problem -> attention warning -> Decision Event`

A discreet **attention marker** such as `!` can appear over the relevant professional or area when something potentially important is developing.

The marker means “something worth watching may be happening,” not “click now or lose the event.”

The player may investigate and use normal management actions before the crisis escalates.

If the situation ultimately requires owner authority, the game pauses and presents the Decision Event even if the player was looking elsewhere.

Some events are naturally sudden and may skip the warning stage.

This creates two complementary narrative layers:

`emergent autonomous social life + authored consequential decision points`

### Owner-initiated management conversations

The player may directly initiate a management conversation with an employee.

These are **structured management actions**, not free-form roleplay and not direct control of the professional.

Candidate intents include:

- listen to concerns;
- praise;
- give feedback;
- warn/reprimand;
- discuss workload;
- negotiate expectations;
- discuss career development;
- address a relationship or production problem.

The player chooses the **intent**, not the exact wording.

Runtime AI may dramatize the conversation within that intent, but the allowed outcomes and state changes remain game-owned.

**Free-text player dialogue is not part of the intended interaction model.** The player selects structured management intents rather than writing the conversation line by line.

## Relationships

Relationships are directional and should affect production.

### Relationship visibility

Use a **hybrid visibility model**:

- precise multi-dimensional values may exist internally for simulation;
- the player sees a small number of legible high-level relationship bars rather than raw numerical spreadsheets;
- qualitative sentiments/tags communicate important nuance;
- a relationship history explains the main causes of the current state.

Initial high-level visible bars should prioritize concepts such as:

- **Bond/Affection**;
- **Trust**.

Do not require displaying exact `72/100` values by default.

Overlay qualitative sentiments such as:

- friendship;
- rivalry;
- resentment;
- attraction;
- fear;
- mentorship;
- admiration;
- envy;
- professional respect;
- distrust.

This allows relationships that are intentionally contradictory, for example:

`high bond + low trust + rivalry + admiration`

The UI should expose causal history so the player can understand changes, for example:

- Trust decreased — took credit for their work;
- Bond increased — completed a difficult production together;
- Rivalry emerged — both want creative control over the same IP;
- Admiration increased — witnessed exceptional work.

Because relationships are directional, what A feels about B may differ substantially from what B feels about A.

The player should be able to infer relationship state from behaviour/conversation, while the relationship UI provides enough explicit information to make consequential events feel earned rather than arbitrary.

Potential relationship dimensions include:

- affection;
- trust;
- tension;
- rivalry;
- attraction where appropriate;
- fear.

A->B need not equal B->A.

Relationships can influence:

- collaboration quality;
- creative risk;
- rework;
- morale;
- willingness to accept assignments;
- demands for separation or partnership;
- resignations;
- conflicts;
- mentorship;
- romance;
- long-term loyalty.

Species/archetype may create **initial tendencies or pressures**, but it does not determine personality.

A cat and mouse may begin with a predatory/prey tension. They may later become the studio's greatest creative partnership.

A hunter may be extraordinarily talented while making multiple anthropomorphic employees uncomfortable or afraid.

## Office vs Nonsense in people

Creative value should not collapse into one stat.

Useful conceptual axes include:

- **Morale** — miserable to happy;
- **Creative Energy** — exhausted to inspired;
- **Wildness** — conservative to experimental;
- **Discipline** — chaotic to reliable.

Operational state can also include more transient or pressure-oriented values such as:

- **Fatigue** — short-term physical/mental tiredness accumulated through sustained activity and insufficient recovery;
- **Stress / Burnout pressure** — longer-term strain created by repeated overload, conflict, deadlines, insecurity or other persistent pressure.

Do not automatically expose every internal value as a precise player-facing meter. The simulation may retain continuous values while presentation uses behaviour, qualitative labels, bars or other readable signals appropriate to the context.

### Fuzzy state interpretation

Character decisions should not depend on brittle thresholds such as `Fatigue > 70 => TakeBreak`.

Use fuzzy-style interpretation so overlapping states can coexist. A professional may be somewhat tired, highly motivated and moderately stressed at the same time.

Personality and context modify how these states influence behaviour. For example:

- a highly disciplined employee may continue working at a fatigue level where another person takes a break;
- an anxious employee may react strongly to moderate workload uncertainty;
- a social employee may respond to low morale by seeking company;
- an ambitious employee may temporarily tolerate stress when a personally important production approaches release;
- a severely exhausted character can still decide that continuing is unreasonable and stop on their own.

These fuzzy interpretations are useful inputs to both deterministic behaviour and the bounded AI action-selection contract.

### Fatigue, recovery and burnout

Time spent working continuously should matter.

Fatigue can accumulate from factors such as:

- long uninterrupted work;
- overtime;
- repeated high-pressure production demand;
- insufficient rest;
- illness/injury;
- demanding outside-life activity.

Ordinary rest, breaks, meals, going home and suitable amenities can reduce short-term fatigue.

Repeated excessive load can create a slower-moving stress/burnout condition that should not disappear because the employee drank coffee or took one short break. Recovery may require sustained lower pressure, meaningful rest, leave, changed responsibilities or resolution of underlying problems.

Professionals can **take breaks or stop working autonomously**. The player manages workload, priorities, deadlines, facilities and conditions; the player does not normally issue minute-by-minute rest commands.

Examples:

- high Wildness + high Discipline = rare creative powerhouse;
- high Wildness + low Discipline = brilliant but dangerous to schedule;
- low Wildness + high Discipline = dependable production specialist;
- low Wildness + low Discipline = organizational problem.

Player choices can shift these states over time.

Repeatedly rejecting a creator's ideas may make them less experimental, more resentful, or more likely to leave. Giving creative freedom may produce exceptional work or uncontrolled scope.

## Employee agency

Employees can make demands and choices.

Potential demands include:

- raises;
- promotions;
- credit;
- different roles;
- time off;
- more creative control;
- less overtime;
- refusal to work with someone;
- access to a desired IP or production;
- recognition for creating a character/property.

Talented employees should gain bargaining power.

Employees can:

- refuse;
- resign;
- leave for competitors;
- return later;
- retire;
- become unavailable mid-production.

The player's job is not to own people. It is to keep a functioning studio despite their agency.

## Competitor studios

Competition should use a **small set of persistent, legible rival studios** rather than fully simulating many equivalent companies.

At the **start of the campaign around 1900**, T.O.O.N. should begin with **one active rival studio**. This is a world-state/campaign-start decision, not a restriction on the first implementation proof.

As the market matures, the number of relevant rivals can grow organically. A useful long-term target is a small handful of active competitors — typically around **3–5 relevant rivals**, with **4** as a reasonable default target when the market is mature enough. The system should remain bounded enough that individual competitors stay memorable.

A competitor can retain abstract state such as:

- identity and creative focus;
- reputation;
- financial strength;
- notable professionals;
- known IPs;
- preferred production types;
- relationships with T.O.O.N.;
- important historical events.

Competitors may arise from the wider world or emerge from the campaign, including former T.O.O.N. professionals who leave and later found their own studio.

Competitors can also **fail and leave the active market**. Bankruptcy is one important path, alongside acquisition/merger, prolonged loss of relevance, or a strategic shift outside the game's supported production space.

A competitor leaving the market should not erase its history. Its former employees, IPs, relationships and notable events can remain in the campaign record and may create future opportunities.

Competitor exits should also create room for new rivals to emerge later, keeping the market dynamic without continuously increasing the active-rival count.

Competition should be expressed through concrete consequences such as:

- competing for talent;
- making offers to T.O.O.N. employees;
- competing for contracts/opportunities;
- releasing work into the same audience window;
- gaining or losing reputation;
- collaboration, rivalry, merger, decline or closure.

Competitor productions are **not simulated through T.O.O.N.'s production pipeline** and do not require generated production artifacts.

Only their relevant outcomes are simulated and persisted, for example:

`competitor production result -> reception/commercial outcome -> reputation/market/talent/opportunity effects`

The game may surface metadata or descriptive summaries of a rival release when needed for context, but should not generate full scripts, storyboards, comics, animations or other production artifacts for competitors.

This keeps AI/runtime cost focused on the player's studio while preserving a believable competitive world.

Competition should not be strictly zero-sum. Two studios can both succeed; rivalry primarily changes attention, opportunities, talent access, distribution pressure and reputation context.

### Personal finances and creative upside

Professionals can have an abstracted personal financial state that affects behaviour without requiring household-accounting simulation.

Relevant influences may include:

- salary and bonuses;
- revenue participation from accepted internal proposals;
- debt or high recurring obligations;
- outside income;
- accumulated savings/wealth.

Personal finances can influence thoughts, demands and outside-work choices. Financial pressure may increase the importance of salary, stability or extra work. Financial success can increase independence, reduce tolerance for poor treatment, enable retirement, fund personal projects or make it plausible for a talented professional to leave and found a competing studio.

These effects should be character- and context-dependent rather than deterministic thresholds.

## Life outside the studio

Characters have an off-screen life that can affect work without requiring a fully simulated city.

Examples include:

- family obligations;
- hobbies;
- second jobs;
- gambling/debt;
- political or union activity;
- criminal activity;
- secret heroism;
- secret villainy;
- relationships outside work;
- illness or injury;
- fame outside the studio.

These can produce readable events and absences.

A worker may arrive exhausted because they act as a hero at night. Their best friend at work may secretly be a villain whom they later arrest, creating an absence in the middle of production.

The simulation should preserve causal signals before severe consequences rather than using arbitrary destructive random events.

## Cartoon logic, predation and violence

Cartoon-world archetypes may create unusual workplace problems:

- predator/prey instincts;
- hunters working beside anthropomorphic animals;
- slapstick violence;
- absurd injuries;
- rivalry escalating into physical conflict;
- imprisonment or disappearance;
- relationships that become dangerous.

The tone should support cartoon exaggeration without making every conflict consequence-free.

Permanent death is not a universal rule because different character ontologies exist. Severe outcomes must follow the character's own existence model and should be causally legible where gameplay investment is at stake.

## Systemic comedy

Humour should emerge from simulation rules, character ontology, workplace pressures, and long-term consequences rather than relying mainly on disconnected scripted jokes.

Examples:

- a brilliant talking cricket may be fully mortal and have a naturally short lifespan, creating an absurd but strategically serious hiring decision;
- an apparently elderly cartoon may remain the same age for a century and become the office's permanent grumpy veteran;
- a mortal prodigy may have only a brief career while an immortal mediocre employee survives multiple generations;
- a predator/prey relationship can begin as a familiar cartoon gag and develop into friendship, fear, rivalry, mentorship, or catastrophe;
- a night-time hero may repeatedly arrive exhausted, while their best friend at work is secretly the villain responsible;
- a character may survive slapstick disasters that would kill a mortal colleague because their existence model follows different rules.

The joke should usually have a **gameplay consequence**.

A short-lived genius, for example, can force the player to decide whether to:

- hire them despite limited long-term availability;
- rush a production around their remaining career;
- pair them with an apprentice to preserve knowledge;
- pay a premium because their talent is rare;
- accept the risk that an unfinished production loses a critical contributor.

This principle keeps T.O.O.N.'s nonsense legible and consequential:

> **The world can be absurd, but the simulation should take its absurdity seriously.**

Avoid direct copies of protected cartoon characters. Familiar archetypes may be referenced structurally, but characters, names, designs, biographies, and specific jokes should be original.

## Careers and generations

Mortal and aging professionals can move through career stages such as:

`Recruit -> Junior -> Experienced -> Veteran -> Legend -> Retired`

Immortal/static cartoons may instead accumulate:

- expertise;
- influence;
- grudges;
- mentorship lineages;
- institutional status;
- outdated habits;
- resistance or enthusiasm toward new media.

A studio can therefore contain both generations of mortal workers and century-long cartoon veterans.

## Supported production types

The current game-design scope is intentionally limited to **four production types**:

1. **Comic strip**;
2. **Comic**;
3. **2D animation**;
4. **3D animation**.

These are the production families T.O.O.N. should support across the campaign. **The accepted first playable production is one 3–4-panel comic strip (owner-confirmed 2026-11-15).** That is a vertical-slice scope choice, not a separate comic-only architecture or a reduction of the four-type game design. Historical technologies, workflows and presentation can evolve inside those families, but text-only works, standalone illustration/editorial pieces, live-action production, television as a separate production type, realtime/game production and other media are outside the current scope unless explicitly reconsidered later.

The four types should share a common conceptual backbone while allowing medium-specific stages:

`concept -> script/structure -> design/art direction -> storyboard/layout -> production -> finishing -> review -> release`

Not every medium requires every stage, and some stages can split into medium-specific technical substeps. Those technical substeps exist primarily to drive people, facilities, equipment, time, cost and production problems; they should not automatically become separate player-facing minigames.

**G-03 accepted authoring boundary (2026-11-16):** the only direct player editable/authorable creative content is (1) the **concept form** (subject to proposal field restrictions), (2) the **script** at the scriptwriting stage, and (3) the **art-direction input/references** at the art-direction stage (including uploaded images/reference materials). **Storyboard/layout and every later technical/finishing/review production stage have no player free-text editor or direct creative-content authoring**. Each stage still permits a player-requested new version, subject to the three-version limit. The player operates the physical production workflow rather than a full comic/animation authoring tool.

The medium-neutral conceptual stages remain applicable to the four finished production types, with medium-specific internal technical steps handled by the studio; they do not expand the set of direct editable stages.

## Production as a physical workflow object

A production should exist as a persistent **physical/workflow object** inside the studio rather than only as an abstract row in a management screen.

The production should have a **strong physical representation** whose appearance changes with:

- historical period;
- production medium/type;
- current pipeline stage.

A comic production, a cel-animation production and a later 3D production should not share one timeless generic prop. Their physical representation should communicate what kind of work they are and where they currently are in the process.

**G-03 accepted physical routing rule (2026-11-16):** after a stage produces its result, the physical production object becomes available again to the player. The player **moves/places that object at the correct next workstation/station** to start the next applicable stage; the studio does **not** silently auto-route it between stations just because content generation completed. An incorrect/incompatible station or an unavailable capacity slot must not secretly advance the production. Player movement between stations is a **management action** and does not count as manually writing/editing creative content.

Concept approval creates the first physical object to route to **scriptwriting**. At scriptwriting, leaving the script alone lets the responsible worker/local AI produce a short script automatically; the player may instead edit the script. After completion, the script/material returns as the production object, ready to be routed to **art direction**. There, generation is automatic unless the player edits/supplies art-direction material (for example image uploads and references). After art direction, subsequent relevant stages run their professional/AI creative or technical work automatically when the player places the object at their matching station. The player may inspect outputs and request versions but cannot type or upload bespoke content into later stages.

The physical representation can evolve from paper folders, boards, reels, cels, tapes, drives, digital work packages or other era/medium-appropriate forms without requiring literal handling simulation for every technology. The exact drag/drop or station-interaction UI is a later UX proof; **player-controlled station routing itself is an accepted game rule**.

The production object owns or references:

- current pipeline stage;
- responsible professionals;
- IP/brief;
- current approved creative inputs;
- generated/intermediate artifacts;
- version/provenance history;
- costs/time spent;
- blockers and pending approvals;
- final released artifact.

This creates a visible relationship between **place + people + production state**.

### G-08 — Physical release and evolving publishing facilities

**Owner-selected direction (2026-11-16, alternative D):** the last step of production/release has a **physical publishing station**. At the start of the campaign, a simple **publishing desk** is sufficient to launch any of the four supported production types. When creative work is finished, its persistent physical project/object can **wait unpublished** until the player chooses to bring it to the publishing station; completion does **not** automatically release it. Waiting does not create catalogue revenue or remove accepted external contract deadlines. The player remains the sole authority for the final publication decision; the published work then enters the existing separate, non-deletable catalogue.

As the studio grows and historical technology changes, the owner can **optionally develop more specialized publishing facilities/capabilities**, potentially for holding unpublished works, promotion and distribution. These are opportunities for improved reach, throughput or convenience, **not mandatory additional stations or a locked multi-building release pipeline**. A simple publishing desk must remain a viable basic release path. Specific facility taxonomy, staffing, upgrade costs, queues, limits, promotional effects and era unlocks remain **Proposed / balance and validation work**, not approved implemented mechanics. Do not invent an unconditional promotion bonus.

### G-18 — Autonomous studio-wide production logistics

**Owner accepted option D (2026-11-17):** as a later progression capability, hired **Production Assistants (Assistentes de Produção)** automatically observe **all eligible studio projects**, identify which physical production objects can advance, and carry them between compatible workstations. This is **studio-wide delegation**, not per-move instructions, per-project assignment, or station-only responsibility. Assistants consume simulated worker time and finite capacity; additional staff can expand transport capacity. **A direct manual move remains the fastest individual transport**, but requires player attention. This decision does not replace **manual player-controlled handoffs in the first vertical slice**.

- An assistant can advance a project only when its current stage has a valid committed/default selection and a compatible available next station; G-07 irreversible stage finality, the three-successful-version limit and blocked/failed-stage handling still apply.
- Assistants **cannot** request paid creative alternatives, make player-owned creative/management decisions, trash projects, silently override a player choice, or authorize final publication. Finished work waits for the player's explicit G-08 release action at the physical publishing desk.
- Assistant time/capacity, congestion and station availability constrain throughput; do not assume unlimited instantaneous movement, parallel carriage by a single worker, or extra creative automation.
- **Still unresolved:** player override/pause controls, tie-breaking/fairness, exception presentation, hire/unlock costs and tuning. G-19 resolves which factors drive the choice, but not their numerical weighting. These are not validated Unreal runtime mechanics.

#### G-19 — Three-factor assistant transport choice

**Owner accepted option B with clarification (2026-11-17):** when two or more productions are ready for transport, **the Production Assistant** determines which production to carry first based on a combined evaluation of **the distance from that assistant to each waiting physical production object**, **how soon each production's deadline expires**, and **the assistant's personal relationship with the professional who most recently worked on that production** (its previous station's professional). This is not a relationship with the destination station's professional. Neither deadline nor affinity is an unconditional override: **all three factors contribute to the choice**. This selection occurs for each assistant with transport capacity; only hired Production Assistants undertake automated transport, while the player's manual handoffs remain separate.

The game owns the deterministic, explainable scheduler and derives affinity from persisted professional relationships. Do not infer that the assistant's relationship automatically changes the production's quality or that the assistant can make creative decisions. Eligibility, compatible available stations, G-07 stage finality and final player-authorized publication remain binding. **Still open for balancing/validation:** the three weights and normalization (including distance and time units), G-20 class priority and no-deadline handling, tie-breaking and G-21 reservation/coordination semantics. **Accepted direction / Documented**, not implemented or validated.

#### G-20 — External contracts before original productions in assistant transport

**Owner accepted option C (2026-11-17):** automated Production Assistants always prefer **eligible external-contract productions** to **studio-owned original productions** awaiting transport. When at least one contract production is ready for an eligible pickup, original productions wait. Only when there is no eligible contract transport to serve does an assistant pick an original. This is a **strict ordering between the two production classes**, not a claim that deadline urgency alone dominates the three G-19 factors *within* the contract queue.

Within the eligible class, G-19 remains in force: assistants compare their own physical distance to each object, deadline urgency where applicable, and their relationship with the **last professional who worked on that project**. For original projects without an external deadline, the deadline component must be neutral/not applicable, not a fictitious contractual deadline or progressive aging. Do not introduce an implicit starvation-prevention promotion that contradicts the accepted external-first rule; project starvation under sustained contract backlog is an explicit balancing/playtest risk. Blocked or incompatible contract projects are **not eligible waiting transport jobs** and therefore cannot freeze original-project movement. Player manual carrying remains a separate action; stage compatibility, G-07 finality and G-08 release authorization are unchanged.

**Accepted direction / Documented**, not implemented or validated. Exact prioritization coefficients, tie-breaking and the G-21 exclusive reservation implementation remain engineering/balancing work.

This is **Accepted direction / Documented**, not implemented or validated.

#### G-21 — Exclusive automatic reservation for concurrent assistants

**Owner accepted option B (2026-11-17):** when multiple Production Assistants are available, **each assistant reserves an eligible production transport job before travelling to pick up its physical project**. A reserved production is removed from other assistants' candidate sets; the remaining assistants choose from other unreserved eligible projects, respecting **G-20's strict external-contract-before-original class** and **G-19's per-assistant combined distance, deadline and relationship-with-last-worker scoring**. This is neither a race to an already claimed object nor a central planner reassigning everyone's work.

- A project must have **at most one active assistant transport reservation**, with atomic acquisition when several assistants decide simultaneously. An assistant cannot carry multiple projects at once. Reserve only when project/stage eligibility and destination compatibility hold.
- Reservation is not a creative approval, project ownership transfer or stage commit. Successful arrival/handoff alone may commit G-07 stage advancement under existing rules, with final publication still player-authorized.
- Never duplicate transport, consume stage versions twice, or let stale reservations cause double-commit after save/reload. Cancelled/trashed/ineligible projects cannot remain valid work assignments.
- **G-22 resolves interruption behavior:** a transport interruption releases the assistant's exclusive reservation automatically. G-23 resolves manual player takeover; exceptional ineligible/deleted jobs still require safe implementation semantics; reservation atomicity and save persistence require validation.

**Accepted direction / Documented**; no Unreal scheduler, tests or runtime behaviour verified.

#### G-22 — Automatic release of interrupted assistant transport

**Owner accepted option B (2026-11-17):** when a Production Assistant is interrupted or becomes unable to continue transporting a project, the transport reservation is **automatically released**. If pickup has not occurred, the production object stays at its prior pickup location; if already picked up, it remains **physically at the location where the interruption happened**. The project becomes eligible for a fresh G-21 reservation by an available assistant, subject to G-20 class priority, G-19 per-assistant factors and compatible downstream workstations.

Interruption alone does **not** cancel or trash the production, alter its creative result, charge another creative-generation expense, consume a creative version or commit/close a production stage. Its physical object must remain reachable and recoverable; saving/reopening must neither resurrect an obsolete reservation nor duplicate pickups/commits. An unrelated ineligibility, deletion or completed handoff still requires normal game-owned guards. **G-23 resolves immediate manual takeover** of a reserved or in-transit object. Exact interruption reasons, placement collision resolution, recovery timing and tests are implementation/validation work. **Accepted direction / Documented**, not implemented or Unreal-validated.

#### G-23 — Immediate player priority over automated transport

**Owner accepted option B (2026-11-17):** the player may **manually pick up any eligible physical production project**, even when it is reserved by, or already being carried by, a Production Assistant. If the assistant has only reserved the job or is travelling to pickup, the player's pickup automatically cancels that reservation. If the assistant already carries the object, manual pickup **atomically interrupts the assistant and transfers that same physical object to the player**. No extra mandatory confirmation dialog is shown. The assistant is free to select another unreserved eligible job using G-20 then G-19 and acquire a G-21 reservation.

Manual takeover must never create duplicate object instances/carriers, duplicate G-07 stage advancement, stale carried state after save/reload, unapproved creative changes, or an implicit G-08 final release. No creative-version slot or production-generation charge is consumed simply by taking over. Manual transport remains the fastest individual handoff. Specific animation, reachability, collision, and moment-of-transfer arbitration are **implementation/UX validation** rather than further owner choices. **Accepted direction / Documented**, not implemented or validated.

#### G-24 — Historically evolving professionalization unlocks assistants

**Owner accepted option C (2026-11-17), with the explicit interpretation that Production Assistants are not a newly invented modern technology:** the capability to **hire Production Assistants** becomes available as the studio progresses through historical changes in **organization and increasingly structured production processes**. This represents the studio's professionalization and greater capacity to delegate physical handoffs, rather than requiring a specific hardware invention or implying that such workers did not exist in earlier eras.

- Preserve the first vertical slice's fully manual routing proof. At a later progression milestone, **optional hiring** of an assistant becomes available; the role should not be granted automatically or made a mandatory gate for production/release.
- Once hired, assistants obey G-18 through G-23, including external-contract-first selection, individual distance/deadline/relationship choice, exclusive reservation, interruption release, and instant manual player takeover.
- **Still to balance/validate:** the concrete historical/organizational milestone, how the game communicates it, cost/wages, availability, staffing progression and its effect on player workload. No fixed date, technology tree item, staff-count threshold or manual-production count is implied by option C.

**Accepted direction / Documented**, not implemented or Unreal-validated.

#### G-25 — Transport and operational production organization

**Owner accepted option B (2026-11-17):** the **Production Assistant (Assistente de Produção)** is responsible for **physically transporting production objects and organizing the operational production workflow**. Beyond G-18–G-24 logistics, the assistant can **organize and monitor production queues, track stage/project progress and communicate blockers to the player**. This gives the recurring professional operational value and a readable presence in the studio without turning the role into an all-purpose manager or creative director.

- Queue organization and transport selection must obey G-20's contract-first precedence, G-19's combined proximity/deadline/last-worker relationship factors and G-21's exclusive reservations. Assistants must not secretly reorder work by a contradictory separate policy.
- Progress monitoring and blocker reporting are **observations/information**, not authority to initiate paid creative versions, change creative outcomes, override player decisions, reassign/hire/fire staff, accept contracts, trash productions or approve G-08 publication. Stalled projects still require the appropriate player decision or station/resource to proceed.
- The assistant may surface actionable warnings about station unavailability, halted production or queue congestion, but exact interface, update frequency and presentation remain implementation/UX work. Avoid assuming AI generative autonomy or a new management system.
- The role remains an optional later progression hire (G-24); the first playable slice's player-routed handoffs remain unchanged. Costs, worker capacity and pacing need validation.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-26 — Marketing department and multiple publicity options

**Owner accepted direction (2026-11-17):** later in the studio's historical/media progression, the player may establish a **Marketing Department** that enables **multiple ways to publicize individual productions**, using *The Movies* as a gameplay reference for having differentiated **promotion modalities**, whose specific investment intensity is controlled under G-27. **There is no Marketing Department while the studio is only producing comic strips**; the capability becomes available **after** that strip-only phase. The precise unlock milestone is not yet fixed and must not be silently equated to a particular year, workforce threshold or specific technology.

- Promotion options belong to the established department; do not add an early strip-era standalone promotional purchase button or require a marketing department to publish.
- Once established, differentiated promotion modalities should respect historical availability and marketing capability; G-27 defines choosing a modality plus investment intensity rather than buying many separate action items. Exact modality catalogue, spending balance, timing and period variants remain to be decided. The inspiration from *The Movies* does not authorize copying protected content or claiming an exact reconstruction of its mechanics.
- Keep G-08's simple player-authorized publication desk viable without marketing. G-14's reception-sensitive original launch and catalogue earnings remain possible without a mandatory campaign. Marketing may influence reach and audience response but **does not guarantee revenue or substitute for game-owned reception**.
- Do not force marketing/advertising into the first strip vertical slice; this is a later studio-development mechanic, with historical appropriateness, staffing and playtest proof still outstanding.

**Accepted direction / Documented**; no Unreal implementation or balanced commercial effects verified.

#### G-27 — One promotion modality with adjustable investment intensity

**Owner accepted option A (2026-11-17):** with a functioning G-26 Marketing Department, the player may choose a **publicity/promotion modality** for a production and set **how much to invest** in it. Greater spend raises the **potential audience reach**, without making awareness, reception or revenue certain. The decision is deliberately simpler than assembling several individual advertising actions into a combined campaign; do not treat G-26's different promotional *options* as an obligation to purchase or schedule multiple actions independently.

- The selected modality determines the kind of outreach; investment intensity/amount controls its potential scale. Era-appropriate options and operational constraints are to be specified, but no particular medium, cost tier, spend formula or action list is approved yet.
- Marketing requires the later-unlocked department (G-26) and remains optional for G-08 player-authorized publication. Reception and any initial/catalogue earnings remain owned by G-14's broader game simulation, not a guaranteed reward for spending.
- **G-28 resolves the campaign decision point:** before publication, with effects both before and after release. Duration, repeatability, stacking, costs and measurable outcomes remain open for design/balancing.

**Accepted direction / Documented**, not implemented or Unreal-validated.

#### G-28 — Pre-publication marketing decision with pre- and post-release effects

**Owner accepted direction (2026-11-17):** the player chooses a G-27 **promotion modality and investment intensity before publishing a production**, with the resulting campaign able to have **effects before release** (such as anticipation/awareness) **and after release** (such as subsequent reach and audience discovery). This is **one up-front decision with effects across the release boundary**, not a model requiring a second player marketing purchase/decision after publication and not an always-on discretionary advertising budget.

- The G-26 Marketing Department is required for the optional campaign; a work can still be released through the G-08 player-authorized physical publishing desk without marketing.
- Before actual player-authorized release, any marketing consequences may affect pre-release awareness/expectations, but **must not post publication revenue, put the unreleased work in the catalogue, or treat a promised release as completed**. Post-release effects begin only upon real release and follow game-owned reception/G-14 economy constraints.
- Campaign decisions, spending and effects need persistent game-owned records to avoid duplicated debits or outcomes across save/reload. Exact launch lead time, duration/decay, repeatability, stacking, G-29 cancellation consequences and remaining balance details require validation; lead-time, duration/decay, repeatability and stacking remain **unresolved**, not silently decided here.

**Accepted direction / Documented**, not implemented or Unreal-validated.

#### G-29 — Cancelled promoted production: sunk cost and public disappointment

**Owner accepted option B (2026-11-17):** when the player **trashes an unreleased production** that was marketed under G-26–G-28, all **already spent promotional money stays spent**, with **no refund or transfer to another project**. In addition, cancellation **may reduce studio reputation according to the actual public expectation generated by the campaign**. Weak or nonexistent awareness may create little or no damage; heavily promoted work may create a larger disappointment. Do not impose a uniform reputation penalty irrespective of audience awareness.

- Use game-owned evidence of pre-release exposure/anticipation to determine impact on **G-15 global and relevant production-type reputation**. A cancellation is not a release or delivery and must not trigger post-release campaign effects, reception income or a published catalogue entry.
- G-06's **single contract cancellation charge** still applies independently if the discarded production belonged to an accepted external contract. Do not replace that fee with marketing effects or invent another fixed contract fee. Studio cash and marketing expense postings persist as economic history, while the unreleased production-owned draft artifacts are permanently deleted under existing trash rules.
- Persist cancellation reputation consequences and charge posting exactly once through save/reload. Exact publicity-to-reputation curve, timing and UI are balancing/validation, not claims of implementation.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-30 — Physical placement gates marketing decisions

**Owner clarification (2026-11-17):** **marketing decisions occur only when the production object is physically placed in the Marketing Department**. This applies to the G-27 initial choice of modality and investment intensity: there is **no remote/global marketing decision panel** that can operate on an absent production. After Marketing **finishes executing the campaign and releases the physical object**, its G-28 pre-release and later post-release effects can continue as the object moves to the G-08 publication desk.

The Marketing Department is an **optional physical workflow visit** available after G-26 progression, not a mandatory gate for publishing all works and not a new creative stage that reopens G-07-closed production steps. Player authority over marketing decisions and G-08 final release remains intact. **Owner accepted option A (2026-11-17): once the player confirms the chosen marketing modality and investment at the department, the campaign is immutable for that production.** The player cannot increase/decrease budget, switch modality, add another campaign, or reset the decision by bringing the project back. An unexpected delay does not reopen marketing; G-29 governs cancellation before release. Record the single commitment and charges idempotently across save/reload. Transport eligibility/routing through the department and how physical occupancy is presented remain to be validated without inventing new approvals.

**Accepted direction / Documented** for the physical decision gate and fixed campaign. No Unreal runtime evidence.

#### G-31 — Marketing eligibility only for completed, unpublished productions

**Owner accepted option A (2026-11-17):** a production may enter the G-26 Marketing Department for its G-27/G-30 publicity commitment **only when all required creative/production stages are complete and the physical production object is still unpublished**. Marketing is an optional step **between completed production and G-08 player-authorized publication**, not an early-development publicity option and not a mandatory passage for every release. No marketing selection for incomplete concepts, scripts or intermediate production objects; already-published catalogue works cannot start a new campaign under this rule.

After finishing production, the player can take the completed object directly to publishing or first route it physically to marketing and commit its one fixed modality/investment choice. The marketing desk does not edit the creative artifact, consume creative-version slots, reopen a G-07 stage, or itself release the work. G-28 campaign effects may build anticipation while the completed work remains unpublished, but post-release effects and G-14 publication income only begin following actual G-08 release. G-29 still applies if the marketed, unreleased work is subsequently trashed.

**Accepted direction / Documented**, not implemented or validated in Unreal. G-32 establishes that execution consumes finite marketing staff capacity over time; its detailed pacing remains to be validated.

#### G-32 — Marketing campaigns consume professional work time

**Owner accepted option B (2026-11-17):** after the player physically places a **completed, unpublished** production in the G-26 Marketing Department and commits its one fixed G-27/G-30 promotion modality and investment, marketing professionals **execute that campaign over simulation time**. Campaign delivery is not an immediate full-effect purchase: the work takes time and uses the department's **finite professional capacity**.

- Marketing professionals must participate in the general autonomous staffing/workload model: they have finite time, may be busy/unavailable, and concurrent campaigns compete for capacity. Do not invent unlimited instantaneous throughput or assume a dedicated worker becomes permanently bound to a single project.
- **Owner correction (2026-11-17), overriding the earlier G-32 interpretation:** both the decision **and execution** occupy the production's **single physical object** at the Marketing workstation. As with every other active production stage, while Marketing is processing it, the player **cannot interact with, collect, move, trash, or publish the object**. When the work completes, the object is released back into the world as an interactable physical production item; it can then be carried to G-08's publication desk. **There is no path to publish before Marketing finishes.**
- Pre-release publicity can create awareness while the work remains unreleased, while post-release influence can occur only after actual G-08 publication (G-28). Staff effort and campaign state must persist without double-spending, duplicate work or duplicate reputation/revenue outcomes. Cancelled unreleased productions still obey G-29; no completed-release state may be fabricated by marketing.
- The **campaign definition remains immutable**: employee work may progress through its fixed plan but cannot autonomously increase spending, switch promotional modality or solicit another approval to extend it. Exact execution duration, capacity allocation, efficiency, pacing and how staffing interruptions affect work remain unbalanced and unvalidated. The proposed G-33 scenario of publishing an in-progress marketing job is invalidated by the same physical processing rule used at other workstations.

**Accepted direction / Documented**, not Unreal implemented or validated.

#### G-33 — Gradual loss of pre-release anticipation after marketing completes

**Owner accepted option B (2026-11-17):** once the G-32 Marketing Department **finishes campaign execution**, returns the completed work's **single physical object** to interaction, and the player chooses to wait before G-08 publication, the **pre-release audience expectation/anticipation accumulated by that campaign decreases gradually with elapsed waiting time**. Publishing sooner after marketing completion tends to preserve more of the pre-launch attention.

- The decay begins from the completed marketing work's return-to-interaction/publication-ready point while the production remains **unpublished**. A production still being actively processed at Marketing is unavailable for player transport/publication; this G-33 does **not** reopen the invalid scenario of publishing before Marketing finishes.
- Use smooth/progressive decay rather than an abrupt all-or-nothing expiry deadline. The precise simulation-time curve, floor and sensitivity to delay remain **unapproved balance parameters**, not a fixed example percentage or promised duration.
- The campaign's G-27 modality and committed spending remain immutable (G-30), and waiting neither creates a refund nor retroactively cancels all post-release effects. G-28 still permits influence following real publication, but its realized launch anticipation is lower after a long delay. G-29 governs any pre-release trash consequences using already accrued public exposure/expectation, not a fabricated release.
- Store campaign-completion time, subsequent waiting duration, and release boundary in game-owned state to avoid duplicated outcomes or invalid save/reload transitions. Inform players that waiting weakens pre-launch expectation without requiring an extra manual decision.

**Accepted direction / Documented**, not implemented, playtested or validated in Unreal.

#### G-34 — Marketing modality affinity by audience, historical era and media type

**Owner accepted a combined rule (2026-11-17), rather than any single exclusive option:** each G-27 promotional modality has **affinity with particular audience segments**, while its effectiveness and suitability **vary by the historical period and the media type of the finished production**. Era and medium are interacting contextual variables, not substitutes for audience affinity. A modality that suits one audience and medium in one decade need not perform equally in another; there should be no universally optimal promotional option.

- For a given finished work, game-owned marketing/reception rules consider **selected modality × audience affinity × historical context × media type × committed investment**. Additional constraints can govern whether a modality is historically available at all, consistently with G-26. Do not infer that newer channels always outperform older ones, or add an unrelated bespoke marketing system for every medium.
- Preserve G-30: one physically initiated, immutable campaign; G-31 requires finished/unpublished production; G-32 holds the object while staff execute the campaign; G-33 gradually reduces remaining pre-launch anticipation if the completed campaign is followed by publication delay.
- Modality selection should be legible to the player through grounded signals of likely audience fit and period/media suitability, without revealing guaranteed ROI. G-14 reception and revenue remain uncertain and game-owned, not a direct deterministic reward from spending.
- **Not yet decided:** the audience-segment taxonomy, concrete modality catalogue, era/media affinity data, interaction weights and presentation. These require explicit balancing/content validation and should not be stated as implemented.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-35 — Professional audience estimates and optional pre-campaign research

**Owner accepted B + D (2026-11-17):** Marketing professionals **provide uncertain evaluations and recommendations** about audience affinity and suitable G-34 publicity modalities for a completed unpublished production. Relevant experience can improve the reliability of these estimates; character expertise is **not** an omniscient forecast of sales or guaranteed reception. Before the one-time G-27/G-30 campaign decision, the player can **optionally request audience/market research**, spending simulation time and departmental resources to improve the understanding of audiences and likely modality fit.

- Use the established G-34 dimensions: audience segments, historical period and production media type. Convey estimates and uncertainty clearly rather than exact guaranteed revenue or hidden-perfect effectiveness scores.
- Research is **separate from committing a promotional campaign**: it can refine advice before the irreversible G-30 choice; once a campaign is confirmed, research must not secretly reselect the modality, revise the investment or create an additional campaign. Research is optional, not a new mandatory prerequisite for publication or marketing.
- Preserve G-31/G-32 physical workflow. With a completed, unpublished physical production at the Marketing Department, any active research processing **occupies the single production object until that work completes**, just as other workstation processes do. While research is running it cannot be picked up, transported, published or interacted with. Once processing finishes the production becomes available for the player's next authorized step; the exact selection UI and whether the next marketing action begins immediately are implementation/UX details.
- Research consumes **finite staff time and resources**, may have cost, and can reduce uncertainty but **does not eliminate it**. Prior evidence and research outputs must be represented as game-owned provenance/observations, never guaranteed commercial outcomes supplied by AI. Specific costs, research designs, accuracy curves and repeatability remain **unresolved design/balancing**; G-36 establishes that knowledge can be reused across productions but loses relevance as conditions change.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-36 — Reusable but time-sensitive institutional market knowledge

**Owner accepted option C (2026-11-17):** the Marketing Department **accumulates reusable institutional knowledge** from G-35 audience/market research. Information gathered for one production may improve later audience-fit estimates and publicity advice for relevant productions, instead of forcing the player to start from zero each time. However, **audience preferences, historical conditions and media markets change**: older evidence may become less relevant/reliable rather than remaining permanently correct.

- Maintain research findings as **studio-owned observations with provenance and contextual scope**, such as audience segment, observed historical period, media type, modality and evidence age. Their applicability is conditional: similar productions and audiences can benefit, but findings are not automatically universal across unrelated media or markets.
- Model diminishing confidence/weight of stale research as contexts diverge and time passes, **without deleting the historical record just because its predictive value fades**. Subsequent relevant research can update or contradict earlier conclusions; staff must communicate uncertainty rather than presenting accumulated lore as objective truth.
- **Knowledge belongs to the studio institution**, not exclusively to one professional: an employee departure does not delete the archive. G-35 employee experience still affects the quality of interpretation and recommendations; institutional memory does not replace skill.
- Retain the G-35 optional physical research step with finite Marketing staff capacity and completed/unpublished production object held during active work (G-31/G-32). Reusing knowledge does not force a paid research step for every work and cannot retroactively revise the immutable G-30 campaign, bypass G-08 publication or guarantee G-14 revenue.
- Exact knowledge schema, aggregation, similarity/context weighting, aging/decay curve, and retention are **unresolved design/engineering/validation**; G-37 explicitly rules out automatic institutional learning from campaign or launch outcomes, not automatic or proven AI memory.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-37 — Formal research is the only source of institutional marketing learning

**Owner accepted option A (2026-11-17):** **only explicit formal G-35 market/audience research updates the reusable institutional marketing knowledge established by G-36**. The studio may retain and display actual promotion, release, reception and revenue results as **commercial history**, but merely observing a successful or failed campaign **does not automatically update audience affinity findings, recalibrate modality effectiveness, or improve later estimates through institutional learning**.

- Separate **historical performance records** from **formal research evidence** in game-owned state. Historic outcomes may be inspected as context by the player or staff, but this does not create an automatic research finding, postmortem analysis or hidden model-training loop. Do not claim that poor predictions self-correct without a research action.
- Professional experience can still influence the uncertain judgment and recommendations of staff (G-35), but that is not an exception permitting automatic writes into the **institutional research knowledge base**. Keep provenance so the game can distinguish research-supported findings from anecdotal or historical observations.
- To update institutional knowledge, the player must elect research via the Marketing Department, incurring finite time/resources and respecting the G-31/G-32 physical object occupancy. Findings remain contextual and subject to G-36 relevance decay; the campaign choice remains immutable once confirmed (G-30).
- G-38 resolves formal research scope as an integrated audience-and-modality study; exact cost, confidence updates, presentation of historical results and archive implementation require design/balancing and validation; this direction does **not** establish a new automatic analytical workflow.

**Accepted direction / Documented**, not Unreal-implemented or validated.

#### G-38 — Integrated research of audience and promotion suitability

**Owner accepted option C (2026-11-17):** when the player optionally commissions formal research at Marketing for a **completed, unpublished production**, the department conducts **one integrated investigation** into both **(a) which audience segments are likely to respond to that production** and **(b) which currently available promotion modalities are best suited to reaching those segments**. The joint analysis accounts for G-34's media-type and historical-period context. This is not a compulsory pair of separately ordered studies, nor a new player-directed menu of unrelated research questions.

- Professional recommendations remain **fallible assessments with uncertainty** (G-35), not deterministic revenue or reception forecasts. Research should improve the information behind the later G-27 choice without selecting or committing that campaign for the player.
- The integrated research is performed as **finite Marketing work** on the **single physical production object**, which is unavailable for interaction, movement, trash or publication while the process runs (G-31/G-32). When research completes, its report becomes available for the player's optional next action; the subsequent campaign is still physically chosen at Marketing, fixed once committed (G-30).
- Research findings contribute **context-scoped, reusable, aging institutional knowledge** (G-36), and **only formal research may update that knowledge** (G-37). Commercial outcomes remain historical performance evidence, never an automatic retraining loop.
- G-39 establishes three discrete research-depth tiers; their precise costs, durations and confidence improvements, remain design/balancing questions; G-40 disallows repeating research on the same production. The two-part scope must not be interpreted as inherently perfect market visibility.

**Accepted direction / Documented**, not implemented, tested or validated in Unreal.

#### G-39 — Three preset depths of integrated marketing research

**Owner accepted option C (2026-11-17):** when optionally commissioning G-38 integrated research on the finished, unpublished production physically placed at Marketing, the player chooses one of **three predefined research-depth tiers**: **Basic (básica), In-depth (aprofundada), Extensive (extensiva)**. These are alternative levels of the **same integrated audience-and-promotional-modality study**, not three different research topics and not a continuously adjustable research budget.

- **Basic:** lower expected cost and work time; less detailed, more uncertain insight into audiences and suitable available modalities.
- **In-depth:** intermediate effort, potential detail and reliability.
- **Extensive:** higher cost and departmental time demand; potentially the richest and most reliable of the three, but it must **not eliminate uncertainty** or guarantee a successful campaign.
- Research occupies the **single completed/unpublished physical object** during the entire selected work process (G-31/G-32/G-35). The object becomes interactable only on completion. Deeper tiers consume more finite staff capacity and other resources; no instant report or remote purchase.
- Results contribute evidence to the reusable, contextual, aging research archive (G-36), updated only through formal research (G-37). Subsequent G-27 campaign selection and intensity stay a separate one-time, immutable decision under G-30; research does not choose for the player.
- **Not yet decided:** numerical costs/times, precise tier-specific evidence gains, access limitations as Marketing develops, while G-40 establishes that each production may be formally researched only once, with no upgrade/repetition afterward. Those quantities need explicit balancing/design validation, not invented fixed thresholds.

**Accepted direction / Documented**, not implemented or Unreal-validated.

#### G-40 — One optional research job per production

**Owner accepted option A (2026-11-17):** each production may receive **no more than one formal integrated G-38 market research job**. If research is chosen, the player must select **one** of the three G-39 levels (Basic, In-depth, Extensive) before beginning. Once the research has been conducted, the production **cannot be researched again**, including repeating the same tier or paying to upgrade to a deeper tier. This is a per-production limit, not a global limit on the studio's research activities.

- Research remains **optional**, so skipping it does not block campaign selection or G-08 publication; if selected, it requires the **completed, unpublished physical object** at Marketing and consumes finite staff time and resources while that object is unavailable until processing finishes (G-31/G-32/G-35).
- The single research report can inform the subsequent **player-owned, immutable G-27/G-30 campaign choice**, but cannot force a particular modality or guarantee reception. Once the report exists, no further research action for that same production should appear in the normal player workflow.
- Research findings contribute to the **reusable studio-wide archive** (G-36/G-37), and earlier research on other productions may inform advice. Reusable knowledge does **not** permit a second formal job on an already researched production.
- Persist research-used state across scene changes/save/reload so that revisiting the physical department cannot restart the study, duplicate costs, or create multiple reports. Handling aborted/failed work without unintended consumption remains a specific implementation/recovery decision, not permission for routine repeat research.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-41 — Combined effect of research depth and professional competence

**Owner accepted option C (2026-11-17):** the usefulness and quality of an optional G-38 integrated market-research report depend on **both** the chosen G-39 research tier (**Basic, In-depth, Extensive**) **and** the competence/experience of the Marketing professionals performing it. Both dimensions can improve the report's **detail and reliability** in evaluating relevant audiences and suitable promotional modalities, within G-34 historical/media context.

- **Neither factor substitutes fully for the other:** a deep study by inexperienced staff is not guaranteed to outperform a basic study by skilled specialists, nor vice versa; meaningful results follow both inputs, and no universal ranking across all combinations is preapproved.
- Do not interpret this as a skill-level gate that locks Extensive research, nor a model in which the research tier alone determines quality while staff only change processing time. Professional expertise remains important to making uncertain assessments under G-35.
- Preserve **uncertainty** in all output; extensive research conducted by experts does not guarantee commercial success, predict revenue perfectly, or determine the player's eventual G-27/G-30 fixed campaign. The single study limit (G-40) still holds even when the result is disappointing.
- Execution consumes finite staff time/resources and **occupies the completed, unpublished production's physical object** until the research process completes (G-31/G-32). Findings alone enrich the contextual, aging institutional archive (G-36/G-37), not actual promotion outcomes automatically.
- **Open balancing/engineering:** which professional attributes count, their weights, how a team contributes, the influence of tier on depth vs reliability, the effect on processing time, and presentation of uncertainty. These are not accepted formulae or validated Unreal behavior.

**Accepted direction / Documented**, not implemented or validated in Unreal.

#### G-42 — Formal research affects decisions, not campaign mechanics directly

**Owner accepted option A (2026-11-17):** formal integrated Marketing research is an **information-gathering investment**, not a direct campaign-effectiveness upgrade. A G-35/G-38 research report helps the player understand likely audience segments and suitable G-34 promotional modalities and judge uncertainty before confirming the one G-27/G-30 campaign, **but the existence, depth or accuracy of a research report does not by itself alter promotional reach, campaign efficacy, expected commercial outcomes or the distribution/variance of results**.

- Two otherwise equivalent completed productions receiving the **same modality and intensity** under equivalent historical/media/audience conditions, professional execution, time and release timing should use the **same campaign outcome rules** whether one commissioned research and the other did not. Research may influence the outcome **indirectly only by changing what the player decides to do** (or through ordinary time/resource opportunity costs), not by hidden modifiers, extra audience targeting bonuses, automatic variance reduction or guaranteed return.
- G-39 tier selection and G-41 professional competence can improve the **reliability and depth of advice**, not the direct mechanical quality of marketing work. Once the player confirms the modality/investment, G-30 immutability continues to apply; research cannot auto-optimize or rewrite that commitment.
- Retain research as **optional**, one formal study per production (G-40), consuming finite staff time/resources and holding the physical completed unpublished production during work (G-31/G-32). Findings enter contextual, aging institutional knowledge only via formal studies (G-36/G-37), but knowledge does not silently boost a campaign when not used for decision-making.
- Quantitative uncertainty, research quality and outcome rules still require balancing and validation. **Do not introduce a compulsory research tax to attain maximum campaign performance.**

**Accepted direction / Documented**, not implemented or validated in Unreal.

### Project trash and deletion

**Accepted owner rule (2026-11-16; explicitly supersedes the 2026-11-15 rule allowing deletion after release):** the player can send an **unreleased / in-production project** to the trash at any stage, permanently deleting that project and its project-owned draft artifacts and versions. **Money already spent is not refunded**; the studio's realized cash, expenses, relationships, history of consequences and prior contractual obligations are not rolled back.

**Release is the deletion boundary.** A finished unreleased project may wait for G-08's physical publishing action; merely becoming ready does not trigger catalogue publication. After the player explicitly authorizes release, the project leaves the active-production workflow and becomes a **published work in a separate published/catalogue menu**. The **trash/delete action is unavailable for published works**; published records, final artifacts, credits/lineage and catalogue/history references persist across save/reload. Catalogue/IP revenue and adaptation rights apply only where the studio actually owns the relevant IP; **G-13 commissioned works remain in the historical catalogue but client-owned**. Contract settlement and other historical records persist without post-release deletion exceptions. Simply finishing a stage or artifact does **not** release it; the player must authorize publication.

When an **unreleased** project is trashed, remove its production state and project-owned draft versions/artifacts/references. **G-06** applies the fixed global cancellation settlement when that unreleased project belongs to an **accepted external contract**; original projects have no contract cancellation charge. Stop in-flight generation where practical, reject late responses, and prevent the deleted draft from being recreated by queued work or save/reload. Do not preserve a recoverable cancelled-project archive record by default, and do not assume a restore feature. Preserve independent IPs, professionals, other productions and already-applied financial/social effects; reconcile cross-entity references without restoring the trashed production.

The UI should make unreleased-project trash irreversible and its **no-refund** consequence clear, and show the G-06 cancellation fee before confirming the deletion of a contracted project. After release, present the work only through the published catalogue/history rather than as an active trashable project. Exact interaction controls are deferred to UX validation.

### Optional human-in-the-loop creation

Creative **content authorship** by the player is optional. Once the player has supplied/accepted a concept, the game can generate all subsequent creative-stage results without the player typing, drawing or uploading content. **Physical transport to the next compatible station remains a player action**, not an optional authoring mode.

For the accepted G-03 interaction model, direct player content intervention is limited to:

1. **Concept** — inspect/complete/edit allowed fields of an external, employee or player-originated idea; optionally use game-provided prefill/auto-fill.
2. **Scriptwriting** — normally the worker/local AI automatically creates the short script; the player may edit the script if desired.
3. **Art direction** — normally the worker/local AI generates the art-direction result; the player may edit/provide relevant art-direction material, particularly uploaded image/reference inputs.

All later stages—including storyboard/layout, medium-specific production, finishing and technical review—**do not expose direct player text entry, upload or creative authoring**. Their work happens at the station, driven by crew, game simulation and local AI/procedural generation. The player still controls placement of the physical object, may review the result, may request another version, and retains final release authority.

Each stage has an **automatic content path** and an optional **player-requested new-version path**, but these are not separate universal Auto/Assisted/Manual modes. The three-version limit applies at **every applicable generating stage**, even those without any manual editor.

A stage's first valid result can be the default approved output if the player leaves it untouched; requesting or selecting another version is optional. **Moving the resulting physical object to the next correct station is the handoff/advance action**: it uses the chosen/default version and discards all other versions in the current stage. Thus automatic stage content completion never implies automatic physical routing or player-free final release.

### Version limit and selection

**Accepted owner rule (2026-11-15): up to three generated versions in total per creative stage.** Each successfully produced alternative is the result of requesting a **new version** for that stage. The limit is **not** merely three candidates held concurrently: once the third version has been generated, requesting another version/rework for that stage becomes **unavailable**. Discarding a version does not refund a generation slot or unlock a fourth attempt. Each new stage has its own allowance of up to three versions.

The player views **one version at a time**. A small indicator should communicate other available versions and allow navigation/selection. Exact controls and visual language are deferred to a later UX/UI pass.

**Automatic creative results** provide a valid default stage output without mandatory player inspection or manual editing. If the player requests alternatives, their selected version advances; otherwise, **physically routing the object to the next valid workstation** accepts the current/default version. This handoff discards the other versions. Even a late technical stage without a manual editor supports the same bounded new-version action. Final public release always remains under player authority.

The player may:

- request another version only while fewer than three successful versions have been generated **in that stage**;
- inspect previously generated versions one at a time;
- select any available version to advance the production;
- move an **unreleased project** to trash at any time before publication, permanently deleting it with **no reimbursement of spent money**; after player-authorized release, the work lives in the separate **published catalogue** and is **not deletable**.

**G-07 — Irreversible production-stage advancement (owner accepted 2026-11-16; option A):** once the player physically moves the project to the **next compatible workstation**, the previous stage is **closed permanently for that production**. The selected/default version becomes its approved output and **all other versions from the closed stage are discarded**. The player **cannot return to earlier stages, regenerate an earlier stage, or reopen its creative-version allowance**, even if a later stage exposes a flaw in the earlier result. The player may inspect and request up to three total successful versions **only at the current stage before advancing**. A failed/incompatible handoff does not close the stage. No rollback/revision loop is part of the base game. If the player dislikes the committed outcome, their choices are to continue from the current stage or trash the unreleased project under existing rules; final release still requires explicit authorization. Preserve closed-stage state and selected inputs across save/reload so a late AI response or UI navigation cannot reopen a committed stage.

### Runtime generation failure and creative-result boundary (G-02)

**Accepted owner direction (2026-11-15): production AI technical failures receive a bounded number of automatic recovery attempts.** This is distinct from short character cognition/dialogue fallback and does **not** permit substituting generic pre-authored media for a failed finished production.

- **Technical failure:** unavailable or crashed model, timeout, out-of-memory condition, corrupted/unreadable output, interrupted work or a result that cannot be presented/consumed at all. Retry/recover automatically within a **bounded technical attempt/time budget**; use queued/asynchronous execution and reject stale results. No technical-failure attempt without a usable deliverable consumes one of the stage's **three generated-version slots**, recalculates the production budget or charges extra production costs. Automatic recovery may extend the stage's schedule.
- **Completed creative result:** an artifact the player can actually read/view/watch as the intended production type, even if it is artistically imperfect, odd, uneven, off-brief or shorter than the target length. It counts as **one of the three versions**. A strip with one or two panels can still function as a strip; do **not** reject it just because a target says three or four. Apply the same flexible, function-first standard to comics and 2D/3D animation.
- **Creative feedback, not artistic veto:** an evaluator may surface uncertain evidence about continuity, readability, craft or intent, and the game may connect those observations to authored production/professional outcomes. It must not turn subjective quality, a fixed panel count, or an aesthetic-score threshold into an automatic technical rejection or effectively grant unlimited free versions. Do not claim a specific professional *caused* a model defect without game-owned causal evidence.
- **Diegetic presentation:** an unsuccessful technical attempt may be represented by an era/medium-appropriate action (e.g., a cartoonist crumpling a sheet and starting again). This visual is a presentation of the technical retry, not proof of staff incompetence, and must not invent fatigue, reputation, morale or cash penalties merely because the local model failed. Its game-visible process consequence may be **time dilation**, not an automatic budget revision.
- **Persistent failure:** after the bounded recovery policy is exhausted, keep the stage and game-owned production state intact, indicate an actionable technical blocker, and provide an explicit safe recovery path when possible. Do not loop forever, silently skip the stage, publish a fabricated artifact, or consume creative-version slots for missing outputs. The whole project can still be trashed at any time.

Retry count, deadlines/backoff, classification thresholds, technical job lifecycle, persistence while blocked, and actual local-model/Unreal feasibility remain **Planned** until measured. Technical retry is **not** player-requested creative rework; the approved three-version maximum remains unchanged.

**Player-requested new versions are different from automatic retries.** Only clicking/requesting a **new creative version** can trigger a recalculation of that production's version/rework cost (within the existing three-successful-version limit). The player should see the cost/schedule consequences in the production interface. These requests can consume time and game-owned effort and affect other appropriate simulation states, but **automatic technical/creative recovery within the same requested version never silently creates an extra spending decision**. Exact cost coefficients remain tuning parameters. The project's regular budget is not recalculated each time a worker discards an unsuccessful attempt.

Player-authored or uploaded material becomes part of the production's real creative input and therefore can affect downstream generation and final artifact evaluation. It is not merely cosmetic metadata.

Player intervention is treated as an **external creative contribution**, not as work performed by a particular in-studio professional.

For example, if the player supplies a script at a stage that supports script intervention:

- that script advances as the approved external input for the next stage;
- the studio's scriptwriter does not retroactively receive authorship or work credit for producing it;
- the scriptwriter does not need to “improve” it merely because they exist on staff;
- later pipeline stages can still transform, adapt, reinterpret or degrade/improve the result through their own professionals, simulation state and local AI generation.

The same rule applies to uploaded character references, art-direction images or other player-provided creative inputs.

This preserves a clean distinction:

`player/external creative input -> accepted production material -> later studio pipeline transforms it`

Human-in-the-loop should therefore bypass or replace only the specific creative contribution supplied at that stage, not the downstream production process as a whole.

### Provenance

The production should retain enough provenance to distinguish, where relevant:

- automatically generated content;
- player-authored text;
- player-uploaded reference/input;
- selected generated version;
- regeneration/rework history;
- professionals and tools/models involved;
- final approved artifact lineage.

Provenance supports continuity, debugging, archive/history and export/share metadata. It should not require preserving every discarded intermediate artifact forever.

## Production scale and output length

T.O.O.N. should favor **small complete works** rather than attempting real-world production lengths.

The goal is that a player can finish many works across one campaign, actually consume them, remember them, compare adaptations, and optionally share favorites.

Target output scales are intentionally compact and remain subject to prototype validation. They are **design targets, not hard technical validation limits**: shorter output is acceptable when it still works as the intended medium (for example, a readable one- or two-panel strip). The first controlled playable fixture still targets a complete 3–4-panel strip:

| Medium | Initial target scale |
| --- | --- |
| Comic strip | **3–4 panels** (target, not a validity minimum) |
| Comic | **1–4 pages** |
| 2D animation | roughly 30–120 seconds |
| 3D animation | roughly 30–120 seconds |

These are **content-length targets**, not fixed in-game production-time rules.

A two-minute 3D short can require far more staff, equipment, cost and in-game calendar time than a two-minute 2D short. Production complexity should scale through:

- number and specialization of professionals;
- technology/equipment;
- pipeline stages;
- iteration/rework;
- relationships/conflicts;
- budget;
- schedule;
- creative ambition.

The player should not need to produce a feature-length film to feel that T.O.O.N. has entered a film/3D era. A compact, polished production can represent a much larger industrial capability while remaining practical to generate, watch and archive.

Production forms may later have rare exceptions beyond these normal targets, but long runtime should not become the default progression reward.

## Sharing productions

Completed productions should be designed as **shareable artifacts**.

The preferred first architecture is export-first rather than hard-wiring the game to individual social-network APIs.

A released work may produce a share package containing, where relevant:

- the final image/comic/video/text artifact;
- title and IP;
- studio year/era;
- selected credits;
- optional T.O.O.N. branding;
- a compact generated caption/description;
- a thumbnail/poster/card;
- provenance needed by the game to reconnect the shared artifact to the campaign.

The player should explicitly choose what is shared. Do not automatically upload productions or expose private save data.

Possible later platform-specific sharing integrations should remain adapters around a game-owned export/share contract so changing third-party APIs do not own the production system.

Social sharing can reinforce the fantasy: a player is not merely posting a procedural asset; they are showing **what their studio made**.

A useful share might communicate:

> title + year + medium + key credits + one memorable production fact

For example, the game could surface that a short was directed by a century-old immortal veteran, written by a short-lived cricket genius, or completed after the lead animator was arrested.

## Produced works as playable rewards

T.O.O.N. productions are not only abstract score cards.

Where technically and economically feasible, the player should be able to **consume the work the studio produced**:

- read dialogue, captions and other text within comic strips and comics;
- read finished strips and comics;
- review storyboards or animatics as **intermediate workflow artifacts**, not independent release types;
- watch compact finished 2D animation shorts;
- watch compact finished 3D animation shorts.

These outputs may be created through combinations of player direction, simulation, authored templates, procedural systems and runtime AI behind T.O.O.N.-owned contracts.

Watching/reading the work counts as part of the intended campaign experience and therefore part of the approximate 40-hour target.

The production itself is a reward, evidence of the studio's history, and feedback on prior player choices. It should preserve enough provenance to answer questions such as:

- which IP was used;
- which professionals contributed;
- what major creative/production choices shaped it;
- what media/technology was available;
- how the audience/reputation/economy responded;
- how later adaptations descend from it.

Consumption should be skippable/revisitable where practical. A player who wants to watch everything should be rewarded with context and attachment rather than punished with mandatory unskippable runtime.

## IP continuity across media

One persistent property may evolve through multiple media.

Example pattern:

`comic strip -> comic -> 2D animation -> 3D animation`

The adaptation history should remain visible. The studio archive should show how a property changed across decades and which professionals shaped each version.

A later adaptation should ideally make the lineage perceptible: the player should be able to compare a 1910s comic strip version of an IP with its later comic, 2D animation and eventual 3D animation incarnations.

### G-16 — Evolving IP continuity across productions

**Owner accepted option C (2026-11-17):** studio-owned IP retains a **persistent, recognizable identity** while successive productions and cross-media adaptations can introduce changes. **Some changes may become lasting continuity for future works; others are local to the specific production/adaptation** and must not silently rewrite the shared IP identity. This is neither an immutable canon that forbids development nor an unrelated reboot at every release, and it does **not** require a manual player approval prompt for every new incidental detail.

- Maintain **game-owned shared IP/character identity and continuity evidence**, distinguished from **production/adaptation-local variants** (for example a period costume or medium-specific presentation). A later work can inherit established shared anchors while deliberately differing in its local version.
- **Local AI proposals and generated media are evidence, not authority to rewrite canon.** G-17 locates continuity selection at the **start of the next production**: the game provides prior published works and their recorded context to the local AI, while the game-owned concept/continuity rules control what the new production inherits. Do not automatically promote every generated detail to an immutable global fact; exact context selection, compression and conflict resolution remain **design/validation work**.
- Preserve the **lineage and provenance** of shared changes and local variants so the player can inspect how the IP evolved over years, productions and media. Published works remain immutable catalogue entries; later continuity changes do not rewrite earlier released artifacts.
- Apply this to **studio-owned IP**. Client-owned commissioned works remain historical delivered artifacts but are not available for studio-controlled continuations or adaptations under G-13. Honor G-07's irreversible closed production stages; G-16 does not reopen them.

### G-17 — Previous published works guide the next production

**Owner accepted option D (2026-11-17), with clarification:** **do not hold a post-publication canon approval step.** When beginning a **new production using an existing studio-owned IP**, the game supplies **its previous published productions as creative/continuity input to the local AI**. The model should use the actual previous works, in their historical/production sequence, to **build a coherent continuation**, instead of generating an unrelated restart or treating every prior generated detail as an authoritative permanent global rule. The player directs the new production through the existing G-03 concept, script and art-direction surfaces; reusing or developing earlier ideas happens there, not through an extra mandatory approval workflow.

- **Evidence-based context:** the game owns the IP identity, previous published artifacts, order, medium, approved creative direction and provenance. The next-generation input should use available earlier **works themselves**, accompanied by bounded factual continuity/identity context and necessary adaptation-local distinctions; summaries or selection may be needed to fit local inference limits, but must remain traceable to the published source rather than invented memory.
- **Sequential continuation without forced global canon:** using earlier releases as context does not mean that **every change becomes universally binding** in every future medium or version. In the next production, previously introduced elements can be continued, revised or left as adaptation-local developments under the current player-directed concept and game-owned consistency constraints. There is **no separate per-detail canon approval screen** after publishing.
- **Bounded authority:** local AI may propose a continuation using those inputs but **does not alter game-owned source works, shared identity or locked gameplay facts**. The new work becomes part of the published IP history only when the player authorizes its release under G-08; unpublished, failed or trashed drafts are not previous *published* works for the next project.
- **No new media or rights path:** G-17 applies only to studio-owned IP. An external client-owned work is not a source of studio-controlled sequel/adaptation under G-13. The existing four finished production media remain unchanged.

**Implementation validation:** check chronological continuity of two or more published works across media, context truncation/selection when the historical corpus exceeds the local model's limits, stable character identity, adaptation-local differences and correct exclusion of unreleased/cancelled artifacts. The exact context-packing, retrieval, representation and conflict strategy are **not yet implemented or validated**.

## Cross-media identity consistency

Persistent IP only works if the player can recognize the same property and characters across decades and media.

Each important IP/character should therefore have a game-owned continuity package that can be consumed by manual tools, procedural systems and runtime AI adapters.

Useful identity evidence may include:

- stable character/IP identifiers;
- canonical names and relationships;
- premise/tone;
- visual anchors and silhouette traits;
- approved reference images where available;
- voice/language traits where relevant;
- recurring props/symbols;
- canon facts and adaptation constraints;
- deliberate changes introduced by a specific adaptation.

The goal is **continuity with evolution (G-16/G-17)**, not pixel-identical reproduction. The next production's local AI must receive prior **published production context** under game-owned control; shared identity and adaptation-local variants remain distinct. Generated details never independently rewrite authoritative persistent identity.

A 1910 illustration and a 2025 3D adaptation should be allowed to look different while remaining recognizably descended from the same property.

When runtime AI generates media, provider-specific prompt tricks, seeds or model settings may assist consistency, but they must not become the canonical identity source. The canonical identity belongs to T.O.O.N.-owned data and approved artifacts.

## Historical archive and endgame

The archive is a major campaign payoff.

By 2030, the player should be able to inspect the history they created:

- first published work;
- first successful character;
- major failures;
- hits;
- **published works** kept permanently in the published catalogue/archive after player-authorized release (unreleased projects that were trashed never become published works);
- important employees;
- founders and retirees;
- century-old immortal staff;
- famous partnerships and feuds;
- technology transitions;
- different versions of the same IP;
- awards/reputation milestones where implemented;
- disastrous reboots;
- legendary productions.

The archive should make the campaign feel authored by the player's decisions.

### Financial game-over retrospective

When G-04's **second distinct negative-cash threshold** forces a sale, the campaign ends with a condensed studio retrospective followed by **what happened next** for meaningful IPs, professionals and rivals. Possible endings should refer to actual persistent context (ownership, reputations, relationships, active competitors, surviving IPs) rather than inventing a full off-screen simulation. The narrative may be illustrated/dramatized with local AI behind bounded game-owned contracts.

This closing view is available even when the studio ends before the planned 2030 historical campaign endpoint. A **trashed unreleased project** is not secretly restored to the playable archive or rewritten as a released work merely to fill an epilogue. **Published projects remain in the historical catalogue** and can appear in the retrospective. Independent IPs, people and other saved history still supply material.

## Art direction

The studio world should visually evolve with time while preserving T.O.O.N.'s authored identity.

Useful principles:

- strong silhouettes;
- expressive posing;
- macro-shape clarity;
- animation-aware movement;
- era-sensitive clothes, props, equipment and spaces;
- visible studio growth;
- old objects and rooms retained as historical traces;
- a mixture of institutional office language and cartoon absurdity.

Classic-cartoon structure can inform posing and graphic design without copying protected studio/character identities.

## Authorship and AI

Production intent, accepted generated artifacts and persistent consequences should converge on game-owned production data.

Runtime AI may be used heavily for text, image, audio, animation or other media generation. Provider/runtime choices remain implementation adapters and must not own:

- the game-domain model;
- studio progression;
- employee agency;
- historical truth;
- final release authority;
- irreversible canon/production decisions.

The player should retain meaningful creative direction and release authority. Where the workflow exposes intermediate proposals, they should be inspectable/accept-reject-editable.

Provider independence does **not** require a feature-complete manual authoring tool for every medium. Core simulation and persistence should be testable through deterministic fixtures/fallbacks even when representative final media normally uses AI generation.

## Persistence

Persistent state should support stable identifiers and version migration.

Long-term persistence must be able to represent at least:

- studio history;
- employees and their existence models;
- relationships;
- IPs and adaptation history;
- productions/releases;
- technology/media state;
- durable consequences.

Legacy `InkTime` saves/artifacts are migration evidence rather than a shipped compatibility promise. Preserve representative fixtures or extract useful data where valuable, but do not make full Unity-save compatibility a blocker for the Unreal game without explicit need.

## First validation slice

The first slice should not attempt 130 years.

It should prove the characteristic interaction among studio, people, production, and persistent consequence. **The first playable production is a complete 3–4-panel comic strip**, using a medium-neutral Production core and a narrow strip-specific output path. Completion, reception and save/reopen remain unvalidated until exercised.

Minimum target:

1. one small studio;
2. 3–4 recurring professionals with distinct traits;
3. at least two meaningful relationships;
4. one IP;
5. one complete **3–4-panel comic strip production**;
6. one assignment decision;
7. one people/production conflict;
8. one player response with tradeoffs;
9. release;
10. one persistent studio/professional/IP consequence;
11. save/reopen;
12. one visual signal of historical continuity.

A second bounded prototype should later test one media/era transition.

## Explicit non-goals for the first slice

Do not require:

- a full 1900–2030 campaign;
- every historical medium;
- a complete animation DCC;
- deep city simulation;
- complete family simulation;
- hundreds of relationship variables;
- feature-film production depth;
- large autonomous AI pipelines;
- unproven Loomlight Game Studio / Loomlight Collective integrations;
- production readiness.

## Engine and production strategy

T.O.O.N. is now intended to be built in **Unreal Engine**.

This is an accepted project direction, not an implementation claim. The current repository still contains a Unity-based scaffold until an Unreal project is bootstrapped and validated.

The Unreal project is also an explicit professional-development artifact: it should demonstrate practical engine competence through real game requirements rather than résumé-driven feature accumulation.

Development is intentionally **AI-heavy**. AI may be used extensively for code, content, research, tests, debugging, tooling, documentation, balancing and visual exploration.

Keep two boundaries explicit:

- **development-time AI** accelerates making the game;
- **runtime/player-facing AI** is a game feature and remains behind game-owned contracts.

AI acceleration must not erase technical ownership. Important systems should remain understandable, debuggable, maintainable and supported by actual compile/run/test/profile evidence.

See [Unreal + AI development strategy](unreal-ai-development-strategy.md).

## Relationship to Polite Goblin and Loomlight

T.O.O.N. is an independent game.

- **YFramework** owns shared terminology, naming/routing, doctrine, The Y Framework methodology, and status vocabulary.
- **Loomlight Flux** owns reusable Unity framework implementation but is legacy migration context for T.O.O.N.; the target game implementation is Unreal-owned.
- **Loomlight Game Studio** may orchestrate production work around T.O.O.N.; it does not own this game's design/runtime.
- **Loomlight Collective** is the selected internal display-name direction for the existing Loomlight Nexus product; participation is optional and cannot be inferred from T.O.O.N.'s AI features. This reference does **not** establish integration, trademark clearance, or permission for a public product launch.

## Validation questions

- Does the player feel they are running a living studio rather than filling production forms?
- Do people create meaningful production opportunities and problems?
- Can employees feel memorable without becoming unpredictable noise?
- Are serious outcomes causally readable?
- Does mixed mortality/immortality create interesting long-term stories?
- Does a new medium change staffing, equipment and production decisions rather than only adding a bonus?
- Can old media remain strategically relevant?
- Does one IP feel meaningfully transformed when adapted across eras?
- Does the studio visibly accumulate history?
- Does core simulation, persistence and reception remain coherent if a runtime AI provider is unavailable, replaced or degraded, even if generated-media fidelity temporarily falls back?

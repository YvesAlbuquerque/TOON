# T.O.O.N. — The Office Of Nonsense — Development Roadmap

**Rebased:** 2026-11-13  
**Design dependency:** [T.O.O.N. Design Direction](design.md)  
**Roadmap status:** Planned  
**Former project names:** InkTime / Ink Through Time

This roadmap preserves validated/recovered technical work while rebasing future game work around the accepted historical living-studio direction.

## Sequencing principles

- Preserve evidence already earned; do not pretend the repository started over.
- Treat the studio as the long-lived protagonist.
- Do not expand historical comic-specific architecture merely because scaffold code exists.
- Re-evaluate useful legacy calendar, employee, economy, equipment, and era concepts against the new design instead of automatically discarding them.
- Keep persistent IP and save compatibility where useful.
- Treat professionals as recurring agents with careers, relationships, demands, outside lives, and explicit longevity models.
- New media expand the studio's options; they do not automatically obsolete old media.
- Validate one characteristic studio/people/production interaction before attempting a full 1900–2030 campaign.
- Preserve Unity serialization/GUID/`.meta` evidence until migration intentionally removes it; do not confuse preservation with continued Unity development.
- Treat Unreal bootstrap as a separate proof before porting broad gameplay.
- Never claim implementation or validation from documentation alone.

For an evidence-based reconciliation of **already accepted design**, the resolved candidate-selection and G-02 failure rules, and separate Unreal/AI validation work, see the [pre-production design coherence audit](preproduction-design-review.md). An implementation proof does not reopen settled design decisions.

## Phase 0 — Recovered technical baseline

### 0.1 Reproducible Unity baseline — completed evidence

Issue #2 / associated merged work established the current Unity baseline and documented historical limitations.

### 0.2 Loomlight Flux audit — completed evidence

Issue #3 / PR #25 documented the host/framework boundary.

### 0.3 Scoped Flux host upgrade — completed historical evidence

Issue #4 / PR #26 validated the bounded Unity/Flux host upgrade at the recorded Flux pin. This remains historical migration evidence; it does not define the target Unreal architecture.

### 0.4 Unreal bootstrap — planned

Unreal Engine is now the accepted target engine. Before porting broad gameplay, prove:

- a clean Unreal project bootstrap;
- exact engine version recorded after validation;
- reproducible open/build instructions;
- one T.O.O.N.-owned C++ module;
- one serializable studio state;
- one simple relationship/production decision;
- visible consequence;
- save/reload;
- standalone/package evidence where practical for the milestone.

Do not claim the migration complete because a `.uproject` exists.

See `docs/unreal-ai-development-strategy.md`.

## Phase 1 — Creative identity and representative proof

### 1.1 Accepted concept

Accepted direction now includes:

- **T.O.O.N. — The Office Of Nonsense** as current project/public name;
- studio/company fantasy as the primary frame;
- campaign target approximately 1900–2030;
- media evolution through **comic strips, comics, 2D animation and 3D animation**, while text, illustration and digital/realtime techniques remain internal production methods rather than additional top-level types;
- persistent IPs that can cross media;
- recurring professionals with agency, relationships and outside lives;
- mixed character longevity, including mortal, long-lived, cartoon-static and rule-bound existence models;
- management of people, productions, studio/economy and technology as coupled systems;
- historical archive/legacy as a major campaign payoff.

Commercial/legal name clearance remains unresolved and separate.

### 1.2 Representative visual target

Minimum visual target:

- one small early-era T.O.O.N. office;
- 3–4 distinct professionals;
- at least one immortal/static cartoon and one mortal character;
- visible relationship tension or affinity;
- one active production;
- a production board/decision surface;
- institutional **Office** language plus visible **Nonsense**;
- one retained historical object/trace suggesting future continuity.

**Exit evidence:** owner-reviewed visual/interactive artifact with recorded corrections.

### 1.3 World-start and language proof

Prototype the campaign opening as a bounded world/location selection.

Minimum proof:

- world/globe presentation;
- choose one of a small validated set of starting locations;
- starting location supplies a default studio/world language;
- one production inherits a default production language;
- interface/subtitle language remains independently selectable;
- character dialogue can display/voice in the studio language while management UI stays understandable in the player's UI language.

Do not require a complete historical world simulation.

Any location-specific economic, cultural, technology or legal modifiers must be backed by researched data before being treated as factual gameplay rules.

## Phase 2 — Unreal domain foundation

All new target implementation in this phase is Unreal-owned. Port concepts, not Unity architecture by default.

Professional evidence should emerge naturally from game requirements: C++ ownership, Unreal reflection/serialization, data-driven authoring, Blueprint boundaries, save/persistence, UI, profiling and debugging where relevant.

AI may accelerate implementation heavily, but generated code/assets are not validation evidence.

### 2.1 Continuous simulation clock and working-day proof

Prove a bounded management clock before long-era simulation.

Minimum behaviour:

- simulation time advances continuously at normal speed;
- at least one player-selected accelerated speed exists;
- when nobody is actively working, low-value downtime automatically fast-forwards toward the next meaningful work period/event;
- fast-forward returns to normal speed before a relevant event, the next meaningful work period or a required player decision;
- opening the main `Esc` menu pauses simulation;
- construction/build mode pauses simulation;
- a Decision Event or other choice/read pop-up pauses simulation while presented;
- a professional visibly arrives, works/socializes/rests and leaves;
- off-site time is compressed/abstracted rather than fully simulated;
- no real-world/background progression occurs while the game is closed;
- no separate multi-shift/shift-roster management system is required for the initial model; working hours, overtime, lateness and absence are sufficient.

Validate pacing before selecting final day length, fast-forward threshold or speed multipliers.

### 2.2 Autonomous social interaction proof

Prove one ordinary social interaction that does not require a direct player command.

Minimum path:

`simulation chooses interaction -> speech-bubble dialogue -> bounded AI output or deterministic fixture -> structured outcome -> game-owned state change`

Requirements:

- ordinary conversation is presented primarily through comic-style speech bubbles;
- reaction/emotion audio may support the interaction without fully voiced generated dialogue;
- the interaction may occur outside the player's camera and be missed;
- AI/provider output cannot directly write relationship or morale values;
- the game owns allowed outcomes and magnitude;
- one relationship change is legible through high-level Bond/Affection and Trust indicators, qualitative sentiments and causal history;
- the underlying simulation can retain precise directional values without displaying raw numbers by default;
- deterministic fixtures remain available for tests/provider-unavailable cases.

The autonomous-interaction proof should also exercise the bounded AI action contract:

`authoritative state -> fuzzy interpretation -> allowed action tags -> AI choice/dialogue/thought -> validation -> game-owned execution`

Requirements:

- current state values and fuzzy interpretations can be supplied as bounded context;
- the game supplies an explicit allow-list of valid action identifiers/tags and valid targets;
- AI output selects from that allow-list rather than inventing unrestricted gameplay verbs;
- optional speech/thought can accompany the action without directly changing simulation state;
- malformed, stale or disallowed tags are rejected;
- a deterministic/weighted fallback can choose an action without the generative model;
- when inference is slow or unavailable, a **contextually selected game-authored action, dialogue, thought or reaction** from an indexed/localized library prevents characters from waiting indefinitely;
- a late model result must not override an already executed authored fallback action; measure latency thresholds and repeated-line frequency;
- only game-owned execution mutates authoritative state.

The first runtime character-AI proof should also validate **local embedded background inference**:

- routine character cognition uses a locally packaged model/runtime and does not require a network service;
- inference is asynchronous and does not block the game thread;
- event-triggered decisions can be requested immediately;
- a background scheduler can request periodic bounded cognition during active live simulation;
- use roughly **two real-time minutes** as the initial maximum quiet interval for the system when at least one eligible character exists;
- the interval applies to the whole character-AI scheduler, not separately to every employee;
- paused/build/menu/closed-game time does not require periodic calls;
- stale results are rejected if state or targets changed while inference was running;
- profile latency, memory, CPU/GPU/NPU usage and frame-time impact before treating the cadence or model choice as validated.

Runtime AI validation must also preserve the broader rule that **all player-facing generative inference is local**. Before generated production artifacts are considered validated:

- prove at least one representative heavy generation path without a remote inference API;
- run it asynchronously or through a local job queue so it does not block the game thread;
- record generation latency, memory/VRAM use, storage/model footprint and failure behaviour;
- automatically retry **technical** production-generation failures a bounded number of times; exhausted retry budgets create a legible, recoverable blocker rather than a soft lock or fictitious output;
- a failed technical attempt with **no usable delivered artifact** consumes **none** of a stage's three creative-version slots; each completed creative result consumes exactly one, regardless of perceived artistic quality;
- preserve media-specific expressive freedom: a functioning one-/two-panel strip is valid even though **3–4 panels** is the first-slice target; apply the same principle across the four media rather than treating target lengths or evaluator taste scores as hard errors;
- express failed technical attempts through appropriate professional/workstation animations where useful without automatically assigning gameplay penalties or blame to employees for model instability;
- keep character-cognition inference and heavyweight production generation as separate workload classes even though both are local;
- compare at least one small-specialist route against a broader/larger-model route for a representative capability before freezing the runtime architecture;
- measure not only output quality but latency, RAM/VRAM, install size, throughput, cross-task consistency and orchestration complexity;
- keep model identity/configuration behind game-owned capability routing so later model replacement does not require rewriting gameplay rules;
- do not claim a minimum hardware specification until representative models have been profiled.

### 2.3 Decision Event escalation proof

Prove one parameterized Decision Event archetype driven by emergent simulation state.

Minimum path:

`ordinary social/production state -> escalating condition -> optional ! attention marker -> owner-required threshold -> auto-pause -> structured choice -> deterministic consequence`

Requirements:

- the event exists because studio-owner authority is required;
- the player may act preventively through normal management before escalation;
- no abstract “prevent event” action exists;
- warning state is observable for an escalating event;
- sudden events may bypass warning when appropriate;
- event roles/options/consequence bounds are authored;
- AI may contextualize dialogue but cannot invent rule consequences;
- the event is presented even if the player was observing another area.

### 2.4 Owner-initiated management conversation proof

Prove one direct conversation initiated by the studio owner with an employee.

The player selects a structured intent such as:

- listen;
- praise;
- feedback;
- warn;
- workload discussion;
- expectations/career discussion.

Requirements:

- no unrestricted free-text dialogue input;
- AI may dramatize the selected intent;
- outcomes remain bounded and game-owned;
- the result can affect a relevant professional/relationship state;
- the interaction reads as management rather than direct Sim-style puppeteering.

## Phase 3 — Persistent studio and people foundation

### 3.1 Revalidate persistent IP foundation

The merged minimum IP model remains directionally useful. Revalidate it against:

- cross-media adaptation history;
- persistent characters/properties;
- production/release history;
- long campaign timescale.

### 3.2 Minimal Professional model

Implement the smallest serializable professional model needed for the proof:

- stable identity;
- role/discipline;
- visual/species/archetype identity reference;
- compact skill representation;
- morale;
- creative energy;
- discipline;
- wildness/experimentation;
- current assignment/state;
- salary/credit expectations where gameplay requires them;
- longevity/existence model;
- career/history hooks;
- permanent-employment state;
- compatible workstation/capacity assignment;
- legible activity state: Working, Available/Idle or Blocked;
- short-term fatigue;
- longer-term stress/burnout pressure where needed for the proof;
- multiple production responsibilities/priorities without manual percentage allocation.

The workforce model for this proof assumes **permanent employees only**.

Hiring must require compatible physical capacity rather than an unrelated global headcount cap. Removing capacity must not automatically dismiss an already-hired employee; instead, the affected professional remains employed and can become Blocked until the player restores/reassigns capacity or explicitly changes employment.

The first professional-state proof should also demonstrate that **Available/Idle is personality-driven rather than player-commanded**:

- at least two professionals should choose different idle behaviours under comparable free time;
- idle choice should consider personality/state/context rather than pure random selection;
- the player influences idle behaviour through conditions rather than issuing direct `Study` / `Socialize` / similar orders;
- at least one idle behaviour should create a small persistent consequence such as skill growth, relationship change, morale change or an outside-life hook;
- prolonged idle time may be interpreted negatively by some personalities;
- there is no universal timer for negative idle consequences; tolerance should vary with personality, ambition, perceived job security, recent workload, recognition, relationships and whether the employee finds the time meaningful;
- at least one idle behaviour may take the professional physically off-site, making them temporarily unavailable and able to return with a bounded consequence;
- no separate recall/call-back mechanic is required; the professional returns naturally;
- off-site idle activity is autonomously chosen rather than directly ordered by the player;
- the UI should distinguish “away” from ordinary in-studio Idle without automatically exposing unknown secret motives;
- Blocked behaviour should remain distinguishable from ordinary Idle behaviour.

The same proof should exercise **workload and autonomous recovery**:

- one professional can hold responsibilities in more than one production;
- priorities rather than manual time percentages guide which responsibility receives attention;
- sustained work increases short-term fatigue;
- repeated excessive pressure can contribute to longer-term stress/burnout;
- a professional can autonomously take a break or stop working;
- recovery reduces fatigue without unrealistically erasing longer-term burnout pressure.

### 3.3 Character memory proof

Prove the smallest persistent memory model needed to support local character cognition without preserving full conversation transcripts.

Minimum proof:

- one canonical game-owned event is recorded;
- two professionals form different subjective memories/interpretations of that same event;
- at least one memory is incomplete, biased or otherwise not identical to canonical fact;
- memory entries can retain salience, sentiment, confidence and privacy/knowledge scope where needed;
- a later character-AI decision retrieves only relevant memories rather than the full historical record;
- the retrieved memory materially influences an allowed action, dialogue line, thought or relationship outcome;
- canonical event history remains unchanged by subjective recollection;
- memory survives save/reload.

### 3.4 Minimal Relationship model

Prove a directional relationship representation with only the dimensions needed for the first slice.

Candidate internal dimensions:

- affection/bond;
- trust;
- tension;
- rivalry;
- fear;
- attraction where appropriate.

The first player-facing proof should use a **hybrid visibility model**:

- a small number of readable high-level bars such as Bond and Trust;
- at least one qualitative sentiment/tag;
- a short causal history explaining why the state changed;
- no requirement to expose exact raw numeric values;
- directional asymmetry visible for A->B vs B->A where it creates a meaningful difference.

The proof must show one relationship affecting a production decision or outcome and let the player understand the causal path.

### 3.5 Outside-life hooks

Implement a bounded event source for off-screen life without simulating a full city.

First proof should support one outside-life condition affecting attendance, energy, relationship or production state.

### 3.6 Versioned persistence

Define Unreal-owned versioned persistence for current T.O.O.N. domain state.

Legacy `InkTime` data is migration source evidence, not an automatic compatibility requirement. Preserve a representative fixture or extraction path only if it materially helps recover useful authored/state data.

**Exit evidence:** current Unreal save/reload survives schema-relevant changes; any claimed legacy import is exercised explicitly.

## Phase 4 — First production-management proof

### 4.1 Shared production model

The production system should support the four accepted production types: **comic strip, comic, 2D animation and 3D animation**.

**Accepted first playable target (owner-confirmed 2026-11-15): one complete 3–4-panel comic strip.** This remains the fixed validation-fixture target; a separately generated strip with fewer panels is still a valid creative result when it functions as a strip, not an automatic technical failure. Build the smallest strip-specific output path on a medium-neutral Production domain; do not hard-code the shared domain exclusively around strips. Other production types remain in design scope but are not required as validated output paths in the first vertical slice.

The first production proof must treat the production as a **persistent physical workflow object**. On completion of each stage, the object returns to the player; **the player places it at the next compatible station** to begin the next stage. The studio may automatically generate creative contents but **must not silently transport or advance the project to another workstation**. An incompatible/unavailable workstation blocks the handoff without losing the project. The accepted first route is `concept accepted -> physical project object -> scriptwriting station -> art-direction station -> later medium-specific stations -> review/release`.

The minimum production representation should support:

- medium/type;
- IP reference;
- crew;
- schedule;
- budget;
- creative/quality state;
- release/result;
- persistent consequences;
- current pipeline stage;
- approved creative inputs;
- intermediate artifact references;
- provenance/version metadata.

Human-in-the-loop proof requirements:

- concept form can originate from (a) a partially filled external/client proposal with offer-specific editable/locked fields, (b) a partially filled one-originator employee pitch, or (c) a player-created concept with optional prefill/AI auto-fill and editing;
- accepting the concept creates the physical project object for the **scriptwriting workstation**;
- in scriptwriting, the game can produce a short script automatically; **only here** may the player optionally edit the script;
- in art direction, generation is automatic unless the player optionally edits/supplies **art-direction references**, including image uploads;
- **concept, scriptwriting and art direction are the only stages with direct player content editing/authoring**; storyboard/layout and every later stage have **no player free-text entry or bespoke creative input upload**;
- all generating stages can complete their contents without player-authored creative inputs; the player still **physically routes** the completed project object to the next station;
- regeneration/new-version selection is available **at every generating stage**, including those without direct editing, within the established three-successful-version limit;
- there is no mandatory universal three-mode Auto/Assisted/Manual system;
- each creative stage that generates alternatives permits **at most three successfully generated versions in total**, not a regenerable pool of three concurrent slots;
- versions are reviewed one at a time, with a lightweight indication of the others; exact UX/UI is deferred;
- after the **third** generated version, further rework/new-version requests in that stage are **disabled**, even if earlier versions are discarded;
- the initial output may be the default chosen version when the player does not intervene; otherwise they may select an existing generated version; the **player's physical routing to the next station** accepts the chosen/default version and discards the rest;
- **G-07: progressing to the next compatible station permanently closes the previous stage**; the chosen/default result becomes committed, all other versions are discarded, and the player **cannot return, regenerate or revise an earlier stage**. Versions remain available only at the current stage before moving forward; incompatible/failed routing never commits the stage;
- **only an explicit player request for a new version** (within the three-version allowance) triggers recalculation/communication of incremental production/rework cost; internal failed work or automatic AI retry may extend the deadline **without recalculating the production budget**;
- player-provided input becomes part of downstream production context and can affect the actual generated artifact;
- player-authored/uploaded input is treated as an external creative contribution rather than work performed by a specific employee;
- intervention replaces only that contribution/stage input; later professionals and AI continue to transform the production normally;
- the physical production representation changes according to era, medium and pipeline stage; each completed stage returns the object for **player-initiated placement** at the correct following station, with appropriate state validation;
- provenance records whether relevant inputs were automatic, player-authored/uploaded or selected from generated alternatives;
- **before release only**, the player may send an in-production project to **trash**, deleting its project-owned draft data/versions/artifacts; **spent money is never refunded**. **G-06:** trashing a project under an already accepted external contract also terminates the contract and charges a **single global X% of its guaranteed payment**, independent of elapsed time/progress/client; X awaits balance, and the player must see the fee before confirmation;
- project trash is destructive, not a soft-cancel/archive state: remove unreleased project-owned references and prevent in-flight/late AI results from recreating it; no restore feature is implied;
- **after explicit player-authorized release**, the project leaves active production and becomes a **published work in a separate published/catalogue menu**; it cannot be moved to trash or deleted, and its durable artifact/credits/history survives save/reload;
- studio recurring burn continues as time passes, but internal generation recovery must not itself book a new production expense; **G-05 accepts capped/partial grace for verified AI technical delays against contract deadline penalties**, not a paused world clock or unlimited waiver. Normal lateness penalties still apply beyond the allowance and for ordinary production delays;
- independent IP/professionals, other productions and already-applied studio/contract effects are not deleted or retroactively undone; released works remain in the published catalogue with normal income/contract consequences, so there is **no post-release deletion case** to model.

Detailed media-specific structures should be adapters or submodels introduced only when required. Do not require full manual DCC authoring for every medium; deterministic fixtures can prove the core production contract while runtime AI supplies representative media where appropriate.

Pipeline-direction proof should preserve a shared conceptual backbone:

`concept -> script/structure -> design/art direction -> storyboard/layout -> production -> finishing -> review -> release`

Not every production type requires every stage. Medium-specific technical substeps should drive staffing, facilities, equipment, time, cost and production risk without automatically becoming player-facing minigames. **Direct content editing is limited to concept, script and art-direction material;** physical station routing and capped player-requested regeneration apply throughout the production pipeline.

### 4.2 One people/production conflict

Implement one causally legible production problem driven by people.

Examples:

- creative disagreement;
- predatory/prey tension;
- demand for credit;
- salary dispute;
- exhaustion from outside life;
- refusal to work with another employee;
- highly talented but unreliable employee;
- sudden absence.

### 4.3 Player tradeoff

The player must receive at least two materially different responses that trade among:

- schedule;
- money;
- morale;
- creative potential;
- relationship state;
- risk of departure;
- production quality.

### 4.4 Release and durable consequence

Completing the production should alter at least one of:

- studio state;
- professional state;
- relationship state;
- IP history;
- future opportunity.

Save/reopen must preserve it.

## Phase 5 — Historical time and generations

### 5.1 Calendar/era reinterpretation

Audit the legacy calendar/era scaffold.

Do not restore old fixed-era behaviour blindly. Keep only patterns that support the new campaign.

The calendar must eventually support:

- long-form year progression;
- era/media availability;
- staff aging where applicable;
- retirement/death where applicable;
- immortality/static-age models;
- historical archive timestamps.

### 5.2 Career progression

Prove bounded career progression such as:

`Recruit -> Junior -> Experienced -> Veteran -> Legend -> Retired`

Not every character uses every stage. Immortal/static cartoons may accumulate influence and history without aging normally.

### 5.3 Mortality and longevity

Implement existence rules as explicit data/behaviour, not species hard-coding.

Minimum models to prove:

- Mortal;
- Cartoon-static.

Later candidates:

- Long-lived;
- Conditional/rule-bound.

### 5.4 Succession and institutional memory

Demonstrate one long-term consequence in which:

- one employee leaves/retires/dies; and/or
- one immortal/static employee persists;

and the studio retains their influence through history, relationships, IP credit, mentorship or archive evidence.

### 5.5 Historical-context data proof

Before attempting a full historical database, implement a small sourced context set for one location and one bounded period.

The proof should include:

- at least one global timeline entry;
- at least one local/country timeline entry;
- explicit date/geographic scope;
- source/provenance metadata;
- separation between factual data and game-design interpretation;
- one professional state affected by context;
- one production prompt/context package affected by context;
- one reception result that explains how historical/market context contributed.

Runtime AI must consume only approved structured context for historical facts. Do not permit unsourced historical invention to become simulation state.

### 5.6 Reception model proof

Prototype a legible **hybrid reception model** in which both the production process and the finished artifact matter.

Candidate inputs:

- production-process evidence such as crew, time pressure, technology, facilities, conflict and direction;
- structured evaluation of the actual generated artifact;
- audience/market fit;
- historical context;
- medium and available technology;
- studio reputation;
- distribution/reach;
- novelty/timing;
- uncertainty.

Artifact-evaluation proof requirements:

- evaluate at least one representative generated work using a local model;
- return bounded structured dimensions rather than unrestricted prose as authoritative gameplay data;
- assess the actual artifact, not only the parameters used to generate it;
- include at least one medium-appropriate craft/coherence signal and one brief/IP-consistency signal;
- keep evaluator output as evidence; only game-owned reception rules determine final state/revenue;
- demonstrate that two artifacts produced under similar simulation parameters can receive meaningfully different artifact evidence;
- demonstrate that strong process parameters do not guarantee a strong artifact score, and vice versa;
- expose a human-readable explanation of how process evidence, artifact evidence and market context contributed;
- test evaluator repeatability/variance before treating any scoring method as validated.

Do not treat a single AI aesthetic score as objective artistic truth.

## Phase 6 — Media evolution

### 6.1 First media transition

Do not attempt all four production families at once.

Prototype one transition within the accepted scope, for example:

`comic strip -> comic`

or:

`comic -> 2D animation`

The transition should require at least one meaningful change in:

- staffing;
- equipment/facility;
- cost;
- workflow;
- opportunity;
- creative possibility.

### 6.2 Technology adoption choice

Prove one early-vs-late adoption tradeoff.

New technology should carry advantages and costs rather than a flat upgrade.

### 6.3 Cross-media IP adaptation

Adapt one persistent IP into a second medium and preserve the relationship between versions.

**Exit evidence:** archive/history can show both works as part of one property lineage.

### 6.4 Cross-media identity consistency proof

Before broad adaptation support, prove that one persistent IP/character remains recognizably continuous across two media.

The proof should preserve:

- stable IP/character identifiers;
- canonical visual/narrative anchors;
- explicit adaptation changes;
- provenance/reference artifacts used by runtime generation;
- player-readable lineage in the archive.

Do not treat provider-specific seeds/prompts as the canonical identity source.

### 6.5 Compact production-output validation


Before scaling content generation, validate representative output sizes.

Initial released-work targets for the **four accepted production types**:

- comic strip: **3–4 panels** (target, not a strict minimum for a functioning strip);
- comic: **1–4 pages**;
- 2D animation: roughly 30–120 seconds;
- 3D animation: roughly 30–120 seconds.

Text, illustration and animatics can still be production-stage materials or intermediate reviews. They are not independent released production types in the current scope. Targets for length, panels and duration are **not** hard technical gates: a shorter coherent result may be a valid version, while subjective quality concerns belong in creative evaluation. Only genuinely unreadable, missing, corrupt or unplayable outputs trigger technical recovery.

Measure separately:

- player consumption time;
- runtime generation time/cost;
- in-game production time;
- archive/storage footprint;
- quality consistency;
- whether the work feels complete enough to remember/share.

Do not equate content duration with in-game production complexity.

### 6.6 Shareable production artifact

Prototype a provider-neutral export/share contract for at least one completed work.

The first proof should support:

- final artifact export;
- title/year/credits metadata;
- thumbnail/poster/share card where relevant;
- optional generated caption;
- explicit player approval before export/share;
- no private save-state leakage.

Direct posting to specific social networks is optional and should come later behind adapters rather than becoming a core dependency.

## Phase 7 — Studio economy and organization

### 7.1 Economy

Prototype a compact studio economy that supports production and people choices without becoming a spreadsheet-only game.

The core proof should expose:

- cash on hand;
- recurring studio burn;
- committed production spending/time;
- a readable runway estimate.

Revenue should initially distinguish three families:

- predictable **contract work**;
- riskier **original productions** with greater IP/upside potential;
- **catalogue/IP revenue** from previously released work.

Costs should remain concentrated in:

- salaries/employment costs;
- studio/operating costs;
- production-specific expenses;
- facilities/equipment;
- technology adoption;
- selected discretionary spending such as recruitment, expansion, training or promotion.

Requirements:

- at least one choice should force a tradeoff between a safer contract and spending capacity on an original production;
- production budgeting should remain compact rather than decomposing into low-value accounting line items;
- the UI should make burn rate/runway legible without requiring the player to calculate it manually;
- historical media/business changes may alter presentation and parameters without requiring a wholly separate economy each era;
- G-04 distress emerges through existing systems: **more frequent external project proposals with worse/stricter commercial terms**, rather than a special insolvency negotiation UI;
- when salaries are unpaid, **some** workers may take a decorative prop home, miss shifts or move to a competitor, using character-dependent simulation and preserving object/employee state;
- when the studio crosses an adjustable **negative cash threshold without an active rescue financing**, offer emergency financing: accepting it **clears pre-existing debts/overdue pay**, adds a calculated **positive cash buffer** without double counting, and **creates a separately tracked repayable financing obligation**; do not equate cleared old debts with zero total liabilities while financing is outstanding;
- only **full repayment** of the active emergency financing resets the insolvency/game-over cycle and makes a **future** rescue offer available on the next separate threshold breach; **partial** repayment is insufficient. **instalments are automatically charged in full on their schedule, even with insufficient cash** (negative cash is allowed; no manual repayment, early payoff, missed-instalment state or special default penalty); the existing insolvency threshold handles any resulting negative balance. Instalment size, frequency, duration, interest and cash-buffer parameters remain open;
- a **second distinct** downward threshold crossing while the rescue **remains unpaid** triggers forced company sale/game over. If the rescue was fully repaid, the cycle has reset and a new first threshold breach can offer financing again; remaining below the threshold in one episode does not create repeated breach events; previous social/property consequences and future normal expenses remain;
- game over presents an **archive-based retrospective** and game-owned coherent *what happened next* for meaningful IPs, employees and competing studios;
- on a **first eligible threshold crossing** with no unpaid financing, **pause simulation and present a mandatory two-outcome Decision Event**: **accept** applies debt/arrears settlement, positive operating buffer and new repayable rescue before resuming; **decline** immediately forces company sale and game over. No continuous-under-threshold waiting, automatic countdown, extra rescue menu or repeated event ticks;
- on a **second distinct crossing while the rescue is still unpaid**, force sale/game over immediately without another financing offer; once the rescue is fully paid, a later independent crossing again gets the mandatory offer;
- the economic/behavioural parameters, threshold/offer values and epilogue logic require tuning and Unreal proof before promotion to Validated;
- any claimed credit, bankruptcy, employment or legal rule must be sourced for the relevant era/location before becoming a historical fact;
- catalogue/IP value should persist across time and later connect to the release/reception/distribution model;
- support the three production origins: player initiative, external contract and single-originator internal proposal;
- an accepted internal proposal gives its one originator persistent credit and a fixed **5%** of studio revenue from that production;
- internal-proposal participation continues after the employee leaves but does not automatically propagate to future productions in the same IP;
- external contracts use a compact term set: client, production type, brief, mandatory requirements, deadline, guaranteed payment, ownership/rights, optional studio participation and bonuses; **G-06 cancellation uses one globally configured percentage of guaranteed payment**, not per-client cancellation clauses; other contract penalties remain distinct;
- contract outcomes are determined by game-owned rules rather than free-form AI judgment;
- G-05: contract lateness assessment applies a **bounded technical-delay grace** only for game-verified AI technical failures/retries; preserve the base deadline, allowance, causal evidence and final penalty result across save/reload. The grace cap/measurement and coefficients remain balancing details. Staff, resource, player-requested revision and ordinary production delays do not consume or qualify for technical grace;
- model an abstract personal-finance state sufficient for revenue participation, financial pressure, wealth and resulting employee-agency consequences.


### 7.2 Departments, facilities and physical growth

Grow from one-room office toward specialized rooms, departments and larger premises only after the first production proof works.

Facilities should change what the studio can do, not exist as decorative unlocks.

Productive facilities/workstations also define **workforce capacity**. A room may expose one or more role-compatible positions. Hiring requires an available compatible position, while removing a position creates a capacity shortfall rather than an automatic firing.

The studio-growth proof should eventually distinguish:

- production infrastructure;
- shared amenities;
- professional-facing props/personalisation;
- archive/history objects;
- pure visual decoration.

At least one non-production object should affect a professional differently based on their preferences/state rather than providing a universal flat bonus.

### 7.3 Recruitment channels across eras

Prototype recruitment as an evolving access system rather than a timeless candidate browser.

The bounded proof should establish at least two distinct channels with different availability/flow, while the long-term direction includes:

- rare walk-in applications at the studio;
- rare employee referrals;
- paid newspaper job advertisements that increase applicant flow;
- a later computer-based professional-network interface with a broader searchable candidate pool.

Requirements:

- early recruitment can genuinely leave the player with very few options;
- employee referrals retain who made the recommendation;
- active advertising increases candidate discovery rather than creating employees from nothing;
- recruitment availability remains separate from workstation/capacity requirements;
- the digital-era network uses a fictional in-world identity rather than requiring a real LinkedIn integration;
- candidate channels must not expose perfect hidden character stats by default;
- pre-hire information should come from evidence such as résumé, portfolio, work history, referral provenance, references/endorsements and compensation expectations;
- different channels should expose different amounts/types of evidence;
- referrals can include a short subjective recommendation/comment from the referring employee;
- walk-in applicants can wait visibly at the studio, show a short comic-style thought, and say a brief line when clicked;
- these walk-in thoughts/lines are hints and flavour, not authoritative disclosure of hidden stats or an interview mechanic;
- modern professional-network testimonials should be consistently positive/exaggerated enough that they carry lower evidentiary confidence than structured work-history data;
- at least one important professional attribute should remain uncertain until after hiring;
- the UI should express uncertainty/confidence qualitatively rather than showing false exact values;
- later discovery of a hidden/uncertain trait should be causally observable through work or behaviour rather than feeling like an arbitrary penalty;
- no interview screen, branching candidate dialogue, recruitment minigame or extra pre-hire probing step is required;
- after reviewing available evidence and flavour cues, the player decision is simply Hire / Do not hire;
- historical unlock timing should be treated as game progression and researched context, not as a claim that the underlying real-world medium did not previously exist.

### 7.4 Workplace environment and preferences

Prototype lightweight environmental preferences before building a large furnishing simulation.

The first proof should test a small set such as:

- quiet vs social space;
- old vs new technology preference;
- clutter tolerance;
- privacy/status preference;
- one specific personal object/amenity.

Validate whether environmental choices produce readable effects on morale, recovery, creativity, concentration, or relationships without forcing excessive furniture micromanagement.

### 7.5 Competitor studios

Prototype a lightweight persistent competitor model.

Requirements:

- begin a campaign around 1900 with **one active competitor**;
- allow the relevant competitor count to grow organically as the market matures;
- target roughly **3–5 active relevant competitors** in a mature market, with around **4** as a normal design target;
- keep the active-competitor count small enough that rivals remain memorable;
- competitors retain abstract identity, reputation, financial strength, notable talent, IP/focus and relationship state;
- former employees can plausibly found new competitor studios;
- competitors can affect talent, contracts, audience attention, reputation and opportunities;
- rival productions are **not run through the player production pipeline**;
- rival productions do **not** require generated artifacts;
- only outcomes relevant to the world are simulated/persisted, such as release result, reception, commercial success/failure and resulting market/reputation effects;
- descriptive metadata may be generated for presentation, but not full production content;
- competition is not assumed to be strictly zero-sum;
- competitors can fail, including through bankruptcy;
- competitor exits preserve historical consequences rather than deleting the studio from campaign history;
- a failed/merged/irrelevant competitor can free an active-rival slot for a new studio to emerge later.

### 7.6 Employee bargaining, dismissal and agency

Introduce:

- raises;
- promotions;
- credit;
- role requests;
- refusals;
- resignations;
- player-initiated dismissal;
- return/re-hire opportunities.

The studio should have to retain talent rather than simply own it.

Dismissal proof requirements:

- dismissal is a simple player action with confirmation rather than a negotiation/minigame;
- once confirmed, the professional leaves the active workforce immediately;
- notice/severance/legal obligations, where modeled, are abstracted as era/location-appropriate economic or rule consequences rather than a playable notice period;
- exact legal/historical obligations are not invented without sourced data;
- dismissal can affect colleagues, relationships, memories, production continuity and future opportunities;
- the former employee remains part of persistent studio history.

Voluntary-departure proof requirements:

- at least one professional can decide to resign from simulation state rather than only through scripted story;
- causes are legible enough for the player to understand why the departure pressure exists;
- an impending resignation may become a Decision Event when there is a meaningful management choice;
- departure can also proceed directly when intervention would add no meaningful decision;
- re-hire or later re-encounter remains possible where appropriate.

## Phase 8 — Presentation and historical continuity

### 8.1 Evolving studio world

Validate visible studio transformation across at least two time periods.

### 8.2 Character presentation

Validate:

- strong silhouettes;
- profession;
- personality;
- relationship promise;
- longevity distinction;
- era-sensitive presentation without flattening identity.

### 8.3 Institutional history

Use:

- boards;
- posters;
- awards;
- photographs/portraits;
- archived productions;
- retired equipment;
- renamed rooms;
- memorials or preserved desks;
- employee credits;

to make past decisions visible in the present.

## Phase 9 — Integrated vertical-slice validation

Required workflow:

`Open studio -> recurring crew -> one relationship pressure -> one IP -> one production -> assignment/tradeoff -> release -> durable consequence -> save/reopen`

The first integrated slice does **not** need to span the full campaign. It must complete one **3–4-panel comic strip** as a player-consumable finished work; proving this does **not** validate comics, 2D animation or 3D animation.

Record:

- Unreal Engine/editor version;
- exact branch/commit;
- setup;
- commands/tests actually run;
- representative visual evidence;
- save/reload result;
- known failures and limitations.

Only exercised scope may move to **Validated**.

## Campaign-length validation

The accepted design target is approximately **40 hours for a complete 1900–2030 campaign**, including time spent managing the studio and consuming completed productions.

Do not tune pacing from calendar math alone. The current conceptual average is about **3.25 in-game years per real-time hour**, but the real validation target is experiential:

- early eras should establish the studio without dragging;
- media transitions should feel meaningful;
- people/relationship stories need time to develop;
- later productions may justify more player attention;
- watching/reading produced work counts toward campaign time;
- optional archive review can extend beyond the core target.

Once a representative production pipeline exists, measure:

- real time per in-game decade;
- real time per production type;
- management time vs production-review/consumption time;
- skip/revisit behaviour;
- frequency of meaningful people events;
- whether 40 hours produces enough generational and media change to feel like a century-scale history.

## Phase 10 — Historical campaign proof

After the vertical slice is stable, prove a bounded multi-era campaign containing:

- at least one technology/media transition;
- at least one mortal career transition;
- at least one persistent immortal/static employee;
- one IP adapted across media;
- visible archive/history accumulation;
- at least one produced work the player can actually read/view/watch;
- measured real-time pacing for management plus production consumption.

Only then should the project expand toward a full 1900–2030 campaign.

**G-07 stage-finality proof (later, game-owned):** complete one production with a selected/default stage result, move it to the next station, attempt to return to or regenerate the closed stage, and confirm the action is unavailable. Validate that remaining current-stage alternatives are discarded on successful handoff, wrong/incompatible routing does not close the current stage, save/reopen preserves closed-stage state, and stale local-AI results cannot reopen it. Do not imply runtime validation from this documented rule.

**G-06 contract-abandonment proof (later, game-owned):** trash an unreleased original versus a contracted project at early/late stages. Check nonrefundable sunk costs, exactly one cancellation charge equal to configured X% of guaranteed contract payment, clear pre-deletion confirmation, terminated contractual future payment, no surviving project/archive entry, retained independent studio/IP/crew history, no late AI resurrection, and no duplicate settlement after save/reload. The actual percentage X remains balancing work.

**G-05 contract-deadline proof (later, game-owned):** compare a normal late delivery, technical retries within the grace cap, technical retries beyond that cap, and mixed-cause delay. Verify the bounded allowance changes only contract lateness/penalty assessment, not the simulation clock, salaries, loan instalments, production cost or the three-version counter; repeated events and save/reload must not duplicate credited delay. Exact caps and weights require balancing evidence.

**Endgame G-04 proof (later, game-owned):** exercise two distinct negative-cash crossings **while rescue is unpaid**, full repayment resetting rescue eligibility, a **subsequent eligible rescue offer**, distress-weighted contract offers, conditional unpaid-staff behaviours, forced sale and retrospective/future epilogue. Validate old debt/salary arrears clearance and positive calculated cash buffer **plus the new repayable financing balance**; automatic scheduled instalment posting **with insufficient cash**, visible remaining balance and projected payments, correct repayment/zero-balance transition; no reset for partial repayment; no duplicate charge on reload or special missed-payment penalty; test insolvency threshold crossing caused by a charge, including the final-instalment zero-balance edge case; no repeated trigger in one continuous negative period; save/reopen of financing balance and cycle; and early ending before 2030. Prove accept/decline transitions, **paused simulation with no financial ticks while the Decision Event is pending**, direct sale on decline, no duplicate triggers within continuous negative cash, full-payment eligibility reset and save/reload of a pending offer before the terminal flow can be marked Validated.

## Deferred until proofs earn expansion

- every historical medium;
- deep city simulation;
- complete family simulation;
- hundreds of relationship variables;
- large fandom/community systems;
- feature-film-scale production depth;
- complete animation DCC functionality;
- large autonomous AI pipelines;
- unproven Loomlight Game Studio / Loomlight Collective integrations (internal display-name direction; public-use clearance remains pending);
- aggressive technical identifier renames without migration evidence.

## Technical rename work

The public name is accepted and the GitHub repository route is now `YvesAlbuquerque/TOON`. Remaining compatibility-sensitive identifiers require a bounded migration:

- `Assets/InkThroughTime/` path;
- `InkThroughTime.*` namespaces and asmdefs;
- `InkGameRoot`, `InkSaveService`, and other legacy type names;
- `InkTime` save/artifact directories;
- old local skill names/paths;
- serialized references and downstream docs.

Do not claim these migrated until the Unreal replacement path is exercised and any retained compatibility/data migration is tested. Unity compile evidence remains historical evidence, not Unreal validation.

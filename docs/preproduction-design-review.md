# T.O.O.N. — Pre-production design coherence and readiness review

**Review date:** 2026-11-15  
**Status:** **Proposed** review and validation plan; **not** an Accepted direction change or a production-readiness claim.  
**Owner:** T.O.O.N. game repository.  
**Canonical sources:** [Design direction](design.md), [roadmap](roadmap.md), [Unreal/AI strategy](unreal-ai-development-strategy.md), [creative direction #28](https://github.com/YvesAlbuquerque/TOON/issues/28), [integrated proof #16](https://github.com/YvesAlbuquerque/TOON/issues/16).

## Verdict and distinction between gates

**Current verdict: design direction Documented; not yet validated or approved for broad production.** Unreal bootstrap is Planned; runtime AI, production generation, reception, pacing and the representative art target lack validated game evidence.

Separate three gates:

1. **Coherent design for a bounded proof:** the first production, decision, consequences, failure handling and acceptance tests are specified without contradictory scope.
2. **Ready for bounded Unreal implementation:** an owner-reviewed representative target and a sufficiently small, inspectable vertical-slice contract exist. The Unreal project itself need not be built to approve starting the proof.
3. **Ready to scale production:** the actual Unreal end-to-end proof, representative generated media, on-device resource/cost/latency measurements, save/reload and player-comprehension evidence exist. This gate is **not met** by documentation, mocked generation, or a standalone model demo.

The first gate is not permission to claim the third. Do not label T.O.O.N. `Validated`, `MVP-ready` or `Production-ready` merely because this review or a design PR merges.

## Confirmed boundaries — do not re-open without an explicit owner decision

- Four supported production types only: **comic strip, comic, 2D animation, 3D animation**. Text writing, illustration, storyboard/animatic, television-era presentation, digital authoring and realtime technology can appear as **techniques, stages or historical context**, but not a fifth type.
- Player is persistent **management authority**, not a diegetic founder/avatar; staff are persistent characters with agency. The physical studio and archives carry continuity.
- Production core: `IP -> Production -> Medium -> Crew -> Stages -> Release -> Reception -> Legacy`.
- Player-managed employees are permanent; compatible built workstations gate hiring; shortage blocks work but does not automatically dismiss employees.
- Studio time is continuous during active management, with pausing and low-value downtime compression; the 1900–2030 / ~40-hour campaign is a **target**, not established balance.
- Player-authored creative contributions are optional, external inputs. At most three candidate versions exist at an alternative-generating stage, and only one advances. Release remains player-authorized.
- All runtime/player-facing generative inference is local; model choice and target hardware are not validated. Game-owned structured state, validation and deterministic fallbacks remain authoritative.

## Contradictions and drift identified

| ID | Severity | Finding | Resolution / remaining boundary |
| --- | --- | --- | --- |
| C-01 | Correctable documentation drift | Earlier descriptive passages called text-only, stand-alone illustration, animatics or realtime works separate finished production types after the accepted four-type restriction. | Reword affected current README/design/roadmap descriptions. Retain these only as *internal stages, techniques or contextual examples* where appropriate. Historical PRs and comments are not retroactively rewritten. |
| C-02 | High — unresolved proof scope | The design allows four production families but does not pick **one specific initial release artifact** for the vertical slice. A medium-neutral domain alone cannot prove a readable production loop. | **Proposed:** first playable proof releases a **3–4-panel comic strip**. Keep the production domain medium-neutral, with the strip format as the first thin adapter; do not commit to this choice as Accepted until owner review. |
| C-03 | High — capability gap | 30–120-second 2D/3D animation generated locally, coherently, reproducibly and affordably on target player hardware is an ambition, not demonstrated feasibility. | Treat local animation as a separate **feasibility gate** before promising the full four-type shipped experience. Static fixture/strip proof does not validate animation. |
| C-04 | High — feedback causality | Hybrid reception requires inspection of the actual artifact, but model output can be unstable, biased, absent, or incoherent with player choices. | Define a game-owned evidence contract, evaluation-unavailable path and repeatability tests. No evaluator may set cash, reputation or canon directly. |
| C-05 | High — first-loop design | The roadmap lists domain systems but not a single testable event and decision with predictable costs/relationships and player-visible explanations. | Use the proposed bounded play scenario below and a consequence ledger. Review before implementation. |
| C-06 | High — pacing | 130 historical years in ~40 real hours, real-time office days, multi-stage production, optional artifact viewing and slow local inference can compete for player attention. | Gate with measured time-per-production, meaningful decisions per hour, skipped downtime, work generation waiting, and a multi-era time-compression experiment. Do not prescribe a fixed sim-time conversion before testing. |
| C-07 | Medium — start-world promise | Globe/location/language scope, historic cost data and global+local events could require an unbounded authored/researched world. | Begin with a **small sourced location set** and one bounded historical period. Keep UI language independent from studio/production languages. Defer unsupported local modifiers rather than inventing facts. |
| C-08 | High — representative target | Physical production objects, characters, office art language and UI attention cues have no owner-reviewed representative visual proof. | Exit via one early-era office mock/prototype showing four distinct staff, active strip workflow, warning, decision surface and one persistent historical trace. |
| C-09 | High — release/export | Uploaded/generated assets, credits, continuity, disk storage, rights and sharing require operational policies and tests. | Prove artifact ownership/provenance and private-by-default **local export** for one work. Clear licensing, safety, retention and platform requirements before broader release. |
| C-10 | High — workflow authority | "Automatic production completion" could be misread as automatic **public release**, even though the player retains release authority. | Explicitly separate **automatic stage completion** from player-authorized **release**; a production can wait in a review-ready state without losing artifacts or advancing its canon. |
| C-11 | Medium — candidate exhaustion | "At most three candidate versions" and regeneration at the limit leave no specified path if all three outputs are rejected. | **Proposed:** cap **active candidates** at three; permit a bounded, paid replacement of an unselected candidate, or explicitly allow stage rework/cancellation. Decide whether the cap is concurrent or lifetime before implementation. |
| C-12 | High — simulation/inference timing | Continuous time, accelerated time and asynchronous local generation can produce stale briefs, overshot deadlines or a simulation that waits indefinitely on inference. | Define snapshot/versioned job inputs, valid waiting/timeout/cancel paths, stale-result rejection and an auto-fast-forward stop when a production becomes reviewable or requires authority. Record game-time cost separately from wall-clock model delay. |

## Proposed first playable proof: one office, one consequential strip

This **is a recommendation for owner review**, not canon or an implemented plan.

**Setup:** one small early-era studio, three to four named professionals with at least two directional relationships; one persistent IP; one commissioned or original 3–4-panel comic-strip production; one limited compatible workstation bottleneck. The first pass uses **one** production and may reuse authored fixture images/text to isolate the simulation from unfinished inference technology.

**Player-visible loop:**

1. Open the studio. Staff move/work socially; available capacity, cash/runway, production stage and a relationship signal are legible.
2. Review the IP, compact brief and crew; choose an assignment or a priority. Production advances through visibly different stage representations rather than only a progress bar.
3. A specific **authored and causally prepared** tension emerges, e.g. one skilled but tired contributor clashes with the deadline and another professional who feels overlooked. The player sees an earlier warning and its evidence.
4. Present two or three choices with explicit tradeoffs, such as **delay/reduce pressure** (calendar+burn tradeoff, relationship relief) vs **push deadline** (short-term schedule advantage, increased fatigue/trust risk). Never predefine that one is universally correct; consequences depend on state and are game-owned.
5. Complete a readable 3–4-panel strip. At least one player choice must alter a visible production or outcome detail rather than only changing an invisible score. A fixture can establish deterministic causality; a later local-model run must prove generative causality separately.
6. Player reviews and explicitly authorizes release. Reception gives a legible breakdown of production/process evidence, artifact evidence when present, market/context and uncertainty.
7. Save/reopen. The released artifact, IP release history, relationship/state change, cash consequence and archive entry remain consistent. The player can later re-open the strip and understand why the event occurred.

**Minimum proof artifacts:** event trigger and warning state, option/precondition list, before/after authoritative state snapshots, work/artifact references, release and evaluation evidence, save version, reproduced load, UI screenshots or short capture, exact Unreal build/test identifiers. Do not claim any of this ran until it has.

### Evaluation and failure policy — proposed test contract

- A local evaluator receives the *actual* finished artifact plus bounded brief/continuity context and returns a versioned typed record: dimensions (e.g. readability, panel continuity, IP/brief fidelity), confidence, diagnostics and evaluator provenance. This is **evidence**, not authoritative reception.
- The simulation combines that evidence with game-owned process and market inputs, records the reasons, and decides outcome. Identical stored evidence and state must reproduce the same resulting reception, independent of model randomness.
- When evaluation is unavailable, timed out or malformed, record the absence. Apply a clearly signalled deterministic fallback/limited-confidence reception path; never silently invent a positive artifact judgment.
- Measure repeated evaluation of **unchanged** artifacts and sensitivity to deliberately altered panels/continuity. If variance dwarfs the difference between comparable artifacts, do **not** use those dimensions as consequential scores.
- Heavy generation cannot freeze office frames; explicit queued/cancelled/failed states and retry bounds are necessary. Generated-media fidelity may degrade, but save/release/history must remain coherent.

## Owner decisions to close before broad production

| Decision | Proposed default | Evidence to accept |
| --- | --- | --- |
| D-01: First slice's primary release artifact | Comic strip, 3–4 panels | Owner confirms it demonstrates the player dream, not just a comic editor |
| D-02: Player attention and intervention budget | One meaningful assignment, one optional creative input, one consequential Decision Event, one release approval | Short paper/interactive walkthrough is comprehensible without reading design docs; player influence has visible causal effect |
| D-03: Local generation minimum for first proof | Game-owned deterministic fixture for systems proof, then separate local strip-generation/inspection proof | Compare representative locally generated strip on agreed hardware against coherence, waiting, failure and storage criteria |
| D-04: Animation commitment | Keep 2D/3D in the accepted **design scope**, not in the first validated production slice | On-device sample measuring consistent characters, motion, audio if applicable, generation time, VRAM/RAM, storage, restart/recovery and share/export quality |
| D-05: Historical and language pilot | One researched era/location (plus one contrasting location only if it changes the decision) | Source-linked global+local context and language layers correctly survive production and reception |
| D-06: Minimum visual identity | One small office and 3–4 recurring cast silhouettes, with production stations/era-specific props and readable event signals | Owner-reviewed representative target with corrective feedback recorded |
| D-07: Economy + reception | A bounded contract-vs-original choice later; first slice only needs one explicit cost/benefit tradeoff and a readable reception consequence | No inscrutable bankruptcy or arbitrary reception spike; deterministic replay and player explanation |
| D-08: Tempo of 130-year campaign | Keep the ~40h target provisional and compress uninteresting time | Timed multi-era prototype measuring decade progression, production count, decision density and work consumption |
| D-09: Candidate-cap meaning | Three **concurrent** alternatives; replacing an unselected candidate incurs bounded rework cost | Test rejection of all three, replacement, cancel, provenance and cost; never allow unbounded free retries |
| D-10: Automatic completion vs release | Stages may run automatically; final release always requires explicit player authority | Auto-run reaches review-ready, waits safely, and remains persistent after save/reopen |
| D-11: Clock vs asynchronous model work | Treat local inference as a versioned pending job; clock and work cost are game-owned, not wall-clock model latency | Accelerate/pause/save/load/timeout/cancel and stale-return tests; no soft lock or unexpected skipped choice |

## Exit checklist and evidence requirements

**Before starting the bounded vertical-slice implementation:**

- [ ] Owner resolves D-01, D-02, D-06, D-09 and D-10; confirms representative creative direction and does not mistake doc acceptance for visual validation.
- [ ] The initial production state machine, two real decision options and their player-visible consequences are specified.
- [ ] Fixed-fixture artifact and evaluator-absent paths are defined so game logic is testable without waiting for an external model.
- [ ] The first proof's out-of-scope list is enforced (no full globe/world simulation, four complete media authoring pipelines, feature-length output, large NPC population, automatic social posting).
- [ ] First prototype acceptance evidence is assigned to [#16](https://github.com/YvesAlbuquerque/TOON/issues/16) and the design decision to [#28](https://github.com/YvesAlbuquerque/TOON/issues/28).

**Before scaling to broad production:**

- [ ] Unreal baseline compiled/opened with exact version and reproducible instructions.
- [ ] One full playable loop was observed; one consequential staff/production decision was understood by a tester.
- [ ] State, provenance, release and archive survive save/reopen.
- [ ] At least one actual **local model** path has measured generation + inspection, structured failures, memory/latency/storage and frame-time impact on a defined hardware target.
- [ ] One second production/media transition demonstrates why new people, facilities or technology matter; campaign pacing has measured evidence.
- [ ] The owner-reviewed art target and public-name/legal clearance have explicit recorded outcomes before commercial claims.

## Explicit unresolved risks

Hardware profiles, local generation quality/latency, 2D/3D sequence coherence, model licensing, content rights, uploaded-input handling, historical research cost, export privacy, economy balance, simulation pacing, candidate-version exhaustion, asynchronous-work timing, UI usability and market-name clearance are **Unknown / Planned**, not solved by this review.

**Recommendation:** use this as an evidence-driven gate and merge only the factual terminology fixes without silently treating D-01–D-11 as accepted design. Owner review of those choices should precede implementation scope expansion.

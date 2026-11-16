# T.O.O.N. — Pre-production design coherence audit

**Reviewed:** 2026-11-15  
**Status:** **Documented audit** of the current accepted design, with limited **Proposed** implementation clarifications. **Not** evidence of a validated game or production readiness.  
**Authority:** [T.O.O.N. design](design.md), [roadmap](roadmap.md), [Unreal and AI strategy](unreal-ai-development-strategy.md), [creative-direction issue #28](https://github.com/YvesAlbuquerque/TOON/issues/28), [integrated-proof issue #16](https://github.com/YvesAlbuquerque/TOON/issues/16).

## Audit rule: do not ask to re-decide accepted design

A design gap exists only when the owning source lacks a necessary rule or contains incompatible rules. An **unimplemented** or **unvalidated** accepted rule is *engineering work or a validation gate*, **not** a fresh owner design question. Historical/legacy files and superseded PR text do not override the current design. Before escalating any question, search the current design, roadmap, relevant issues and merged PRs; record the conflicting passages and the consequential alternatives.

## Confirmed decisions — resolved, not open questions

| Topic | Accepted/current rule | Evidence location |
| --- | --- | --- |
| Project fantasy | Historical living creative studio, roughly 1900–2030; the studio/people/IP/archive accumulate history | [Design](design.md), [#28](https://github.com/YvesAlbuquerque/TOON/issues/28) |
| Production types | **Exactly four**: comic strip, comic, 2D animation, 3D animation; storyboards, text, standalone illustrations and animatics are not extra independent release types | [Design — Supported production types](design.md#supported-production-types) |
| **First playable artifact** | **One complete 3–4-panel comic strip**; explicitly confirmed by owner **2026-11-15**. Other three types remain in game-wide design scope | [Design — First validation slice](design.md#first-validation-slice), [#28](https://github.com/YvesAlbuquerque/TOON/issues/28) |
| Core domain | Medium-neutral `IP -> Production -> Medium -> Crew -> Stages -> Release -> Reception -> Legacy` | [README](../README.md), [Design](design.md) |
| **G-03 — Concept and stage authorship** | Three concept origins with editable/locked fields; direct editing only for **concept, script and art-direction references**. All later stages auto-generate contents; new-version request (max three) is available at all stages | [Design — Authoring](design.md#optional-human-in-the-loop-creation), [Design — Proposal origins](design.md#how-productions-originate) |
| Physical workflow handoff | Accepted concept creates a physical object; scriptwriting is first. After each stage, player places the object at the **correct next workstation**; automatic content generation is not automatic stage routing | [Design — Physical production](design.md#production-as-a-physical-workflow-object) |
| Management | Player manages assignments, priorities, money, workplace and consequential Decision Events, **not** individual idle actions or free-form conversations | [Design — Management model](design.md#management-model-and-autonomous-social-simulation) |
| Release authority | Automatically completing creative stages **does not** bypass player authority over final release | [Design — Authorship and AI](design.md#authorship-and-ai), [roadmap](roadmap.md) |
| Alternatives | **At most three total successfully generated versions per stage**; each new version uses one slot, further rework disabled after the third; one chosen version advances and all others are discarded | [Design — Version limit](design.md#version-limit-and-selection) |
| Project deletion | The player can move the **entire project** to trash **at any time**, including after release; delete project-owned data/artifacts/archive entry, not a reversible cancellation record | [Design — Project trash](design.md#project-trash-and-deletion) |
| Workforce | Permanent player-managed employees, hiring gated by compatible built capacity; no instant dismissal when a workstation is removed | [Design — Employment](design.md#employment-workstations-and-studio-capacity) |
| Economy and reception | Cash/burn/runway; contract, original, catalogue revenue; reception considers process, **actual artifact**, audience/market, distribution and uncertainty; local evaluator returns evidence, not direct authoritative revenue | [Design — Studio economy](design.md#studio-economy), [historical context and reception](design.md#market-and-audience-reception) |
| Runtime AI | All player-facing generative inference **local**; bounded game-owned state/actions and provenance; async execution/queues, stale-result checks and deterministic fallback where applicable | [Design](design.md#local-background-character-ai-and-cadence), [Unreal and AI strategy](unreal-ai-development-strategy.md) |
| **G-02 — Production AI technical failure** | Bounded automatic recovery only for **technical failure**; absent/unusable results spend **neither a creative slot nor an extra production charge**. They may delay delivery. Imperfect but consumable results count as versions; no automated aesthetic veto | [Design — G-02](design.md#runtime-generation-failure-and-creative-result-boundary-g-02) |
| Production spending authority | **Only explicit player requests for new creative versions recalculate the production/rework cost**. Automatic failed attempts may extend schedule, not the production budget; unrelated recurring studio burn continues with time | [Design — Production spending](design.md#production-spending-authority-and-schedule-slippage) |
| Character AI latency fallback | If cognition/speech/thought is late or unavailable, choose a contextual **game-authored action, line, thought or reaction**; stale AI output cannot supersede the committed fallback | [Design — Autonomous action](design.md#ai-generated-conversation-and-autonomous-action-selection) |
| Time and campaign | Continuous active-simulation clock, configurable acceleration and appropriate pausing/skipping; **~40h** full-campaign target awaits playtesting | [Design — Campaign and time](design.md#campaign-and-time) |
| Scope of technical work | Unreal target **Accepted direction**, bootstrap **Planned**; Unity/Flux remains legacy scaffold evidence, not current game behaviour | [README](../README.md), [roadmap](roadmap.md) |

## Reconciliation performed in this PR

1. **Resolved documentation contradiction:** current high-level descriptions formerly implied text-only, illustration, animatics or realtime were additional production types. Align current README, design and roadmap to the **four** accepted types.
2. **Resolved initial-format omission:** record the owner's **accepted 3–4-panel comic strip first proof** in canonical design and roadmap without making Production comic-specific.
3. **Clarified automatic content versus physical stage progression:** a valid generated result can be the default selected version when the player does not intervene. **G-03 (owner, 2026-11-16) supersedes any implied automatic transfer between stations**: the player physically moves the production object to the next compatible workstation, advancing the chosen/default version and discarding the others. Final release remains separately player-authorized.
4. **Previous false positives withdrawn:** the original audit treated creative-participation budget, final release approval, reception/economy, local AI fallback and the ~40-hour campaign target as fresh owner decisions. They are already accepted design rules or validation work; **do not ask the owner to approve them again**.

## G-03 resolved — bounded authoring and player-routed stations (owner, 2026-11-16)

External client proposals arrive partially completed with proposal-specific locked/editable fields. Employee proposals arrive partially completed with existing single-originator credit preserved. Player-initiated concepts may be empty, prefilled or optionally AI-assisted and remain editable. **The three direct content-edit surfaces are concept, scriptwriting and art direction (including reference-image upload).** No player text or bespoke reference upload is required or exposed at storyboard/layout or later stages.

After concept acceptance, the player physically routes the production object into scriptwriting, then art direction and each relevant medium-specific station. **Stage content may generate automatically; station handoff does not.** Each stage permits a player-requested new version under the **three total successful versions** rule. The player can leave the default version untouched, then route the object to the next correct station; routing discards the unchosen versions. Final release remains a separate owner-approved action.

**Engineering validation still missing:** station compatibility, generated-result return/handoff, direct-edit access only at three surfaces, masks for client proposal fields, stage-version cap in later technical stages, input provenance, save/reload across handoffs, and confirmation that wrong-station placement never advances. This is **Documented / Accepted direction**, not implemented Unreal behaviour.

## E-01 resolved — three versions and project trash (owner, 2026-11-15)

The earlier ambiguity is **closed as a design decision**. Each successful request for a new version is one of **at most three total generated versions in that stage**. When the third exists, the new-version/rework action is disabled; discarding an earlier candidate does not create a new slot. Choosing a version advances it and **discards all others**. With no approved candidate, the player may still pick one of the existing versions or move the **entire project** to trash. There is no automatic advancement of a rejected version after player intervention.

**Trash means deletion, not cancelled-project archival**: the player can select any project at any time, including after release, and remove its project-owned data, versions, local artifacts and archive entry. This explicitly **supersedes** the earlier 'cancel active production, preserve cancellation record, published work cannot be removed' interpretation. See [the owning design](design.md#project-trash-and-deletion).

**Engineering verification, not another design vote:** test 0/1/2/3 versions, disable after third, all unselected candidates erased on advance, automatic stage selection, trash before/after release, save/reopen without orphaned project references, and late asynchronous result rejection. G-02 now accepts bounded automatic technical retries without spending creative versions; exact retry budget, failures, latency and recovery UI remain unvalidated engineering/tuning work.

**Narrow remaining post-release specification:** the rules have not yet defined what happens to future catalogue revenue, contract liabilities and externally distributed works when an *already released* project is deleted. Do not invent cancellation refunds, third-party recalls or retroactive reversal of studio/people state. Only escalate these outcomes when production/economy design reaches that case.

## Engineering / production-feasibility evidence gaps — NOT undecided design

These are outstanding proofs attached to current roadmap/issues, not re-opened conceptual decisions:

| Evidence still missing | Existing direction | How to close |
| --- | --- | --- |
| Representative visual identity | Early-era studio, diverse recurring cast, legible relationships, physical production object and warning/decision surfaces | Owner-reviewed target plus recorded corrections: [#28](https://github.com/YvesAlbuquerque/TOON/issues/28) |
| Unreal end-to-end loop | One studio, 3–4 professionals, two relationships, one IP, one strip, meaningful decision, release, durable consequence, save/reopen | Compile and exercise the integrated proof: [#16](https://github.com/YvesAlbuquerque/TOON/issues/16) |
| Local generative strip + artifact evaluation | Local models behind game-owned contracts, bounded evidence and graceful fallback | Measure actual panel coherence, IP continuity, evaluator repeatability, latency/RAM/VRAM/storage, queued/failure behaviour; compare deterministic fixture separately |
| Local 2D/3D animated output | Remains inside the **accepted design scope**, but initial strip proof does not validate it | Separate on-device sequence/character consistency and duration/compute/licensing feasibility before promising release-quality animated production |
| Historical content and languages | Sourced global/local context; interface language independent of studio/production languages | Small researched starting location/time dataset and working language-layer proof |
| Economy, era progression and pacing | Three revenue families, legible financial pressure, 1900–2030 / ~40h target | Player-tested decision comprehension, meaningful choices per hour, time spent generating/consuming productions and multi-era transition measurement |
| Export and commercial clearance | Export-first, explicit player approval, persist attribution/provenance | Rights/licensing, content/privacy/storage and actual export tests; separately verify the current T.O.O.N. name-collision risk |

**Do not confuse them:** *Documented* is not *Implemented*; a deterministic fixture is not local-model media validation; a playable strip is not proof of 2D/3D animation or a 40-hour campaign; release-name clearance is not implied by engine milestones.

## First vertical-slice proof — acceptance scenario, not a new owner decision

Use the accepted small-scope roadmap as a concrete validation fixture:

1. One early-era studio with 3–4 recurring professionals, distinct responsibilities, an IP, relationships and workstations; cash/runway and stage are legible.
2. A persistent production enters a **3–4-panel strip** pipeline with automatic creative steps, while one optional authoring/selection point remains available.
3. A causally visible staffing/relationship pressure generates a consequential management Decision Event with at least two different costs or outcomes.
4. A chosen response changes persistent state **and** something visibly connected to the finished strip or its process/credits.
5. The studio completes a readable artifact; final **release requires player approval**; reception records the evidence and explains its most consequential causes.
6. Save/reopen preserves production, released artifact, credits/lineage, relevant relationship/economy consequences and archive history.
7. A separate local-model experiment tests actual generated outputs; if unavailable, a deterministic fixture proves only the game-owned logic and failure path.

This scenario is a **test plan**, not an approval for exact character bios, script, art direction, cost coefficients, generation stack or release claims.

## Question and completion discipline

- **Do not ask again** about optional creative content editing restricted to concept/script/art direction, physical player-controlled station handoffs, concept source-specific editable field masks, three **total** generated versions per stage, trash deletion at any time, chosen-version advancement/discarding others, release authority, four production types, the initial **3–4-panel target (not a hard validity condition)**, bounded technical recovery vs creative imperfections, **player-only creative-regeneration cost recalculation**, local-only runtime AI, economy families, or the provisional campaign target unless new contradictory owner evidence emerges.
- Escalate only an **unresolved consequential design choice** with explicit links to the incompatible/missing canonical rule. Use a narrow recommendation and alternatives, not a general questionnaire.
- Prefer closing engineering unknowns through benchmarks, artifacts, tests and playtests; preserve all unverified status as **Planned** / **Unknown**.
- This documentation review does **not** establish a validated Unreal build or production readiness.

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
| Creative participation | **Optional**; a stage can complete automatically or use bounded player-authored/selective input; no universal Auto/Assisted/Manual mode | [Design — Optional human-in-the-loop creation](design.md#optional-human-in-the-loop-creation) |
| Management | Player manages assignments, priorities, money, workplace and consequential Decision Events, **not** individual idle actions or free-form conversations | [Design — Management model](design.md#management-model-and-autonomous-social-simulation) |
| Release authority | Automatically completing creative stages **does not** bypass player authority over final release | [Design — Authorship and AI](design.md#authorship-and-ai), [roadmap](roadmap.md) |
| Alternatives | **At most three concurrent candidate versions** per stage; one approved version advances; rework consumes simulation resources; discarded work need not be archived permanently | [Design — Version limit](design.md#version-limit-and-selection) |
| Workforce | Permanent player-managed employees, hiring gated by compatible built capacity; no instant dismissal when a workstation is removed | [Design — Employment](design.md#employment-workstations-and-studio-capacity) |
| Economy and reception | Cash/burn/runway; contract, original, catalogue revenue; reception considers process, **actual artifact**, audience/market, distribution and uncertainty; local evaluator returns evidence, not direct authoritative revenue | [Design — Studio economy](design.md#studio-economy), [historical context and reception](design.md#market-and-audience-reception) |
| Runtime AI | All player-facing generative inference **local**; bounded game-owned state/actions and provenance; async execution/queues, stale-result checks and deterministic fallback where applicable | [Design](design.md#local-background-character-ai-and-cadence), [Unreal and AI strategy](unreal-ai-development-strategy.md) |
| Time and campaign | Continuous active-simulation clock, configurable acceleration and appropriate pausing/skipping; **~40h** full-campaign target awaits playtesting | [Design — Campaign and time](design.md#campaign-and-time) |
| Scope of technical work | Unreal target **Accepted direction**, bootstrap **Planned**; Unity/Flux remains legacy scaffold evidence, not current game behaviour | [README](../README.md), [roadmap](roadmap.md) |

## Reconciliation performed in this PR

1. **Resolved documentation contradiction:** current high-level descriptions formerly implied text-only, illustration, animatics or realtime were additional production types. Align current README, design and roadmap to the **four** accepted types.
2. **Resolved initial-format omission:** record the owner's **accepted 3–4-panel comic strip first proof** in canonical design and roadmap without making Production comic-specific.
3. **Clarified automatic stage selection:** automatic creative completion does not demand manual selection of an alternative. If the player intervenes, they select the approved candidate; otherwise a **game-owned automatic selection rule** advances a valid result. This implements the already accepted optional-intervention rule and does **not** permit automatic public release.
4. **Previous false positives withdrawn:** the original audit treated creative-participation budget, final release approval, reception/economy, local AI fallback and the ~40-hour campaign target as fresh owner decisions. They are already accepted design rules or validation work; **do not ask the owner to approve them again**.

## Narrow remaining design specification issue

### E-01 — All available candidate versions rejected

**Real edge-case ambiguity:** A creative stage may hold up to three candidate versions. The docs specify selection, a simultaneous cap and bounded regeneration cost, but do not define the interaction when the player rejects **every** currently available candidate without selecting one. This matters for completion, UI and resource accounting.

**Proposed minimal implementation behaviour (not yet accepted):** the stage does **not** silently advance a rejected candidate. The player can (a) select an existing candidate, (b) explicitly cancel/rework the production as allowed by production state, or (c) spend bounded time/budget/effort to discard one candidate and generate a replacement while never exceeding **three concurrent** candidates. Cancellation/rework and generation failure paths must be legible and persist safely.

**Validation:** write a small state-machine test for 0/1/2/3 candidates, accepting, rejecting all, replacement cost, cancel, save/reload and generation timeout. Escalate to owner **only if** experience-level alternatives genuinely diverge after this engineering test; do not open a broad design questionnaire.

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

- **Do not ask again** about optional creative participation, three concurrent candidates, release authority, four production types, initial strip length, local-only runtime AI, economy families, or the provisional campaign target unless new contradictory owner evidence emerges.
- Escalate only an **unresolved consequential design choice** with explicit links to the incompatible/missing canonical rule. Use a narrow recommendation and alternatives, not a general questionnaire.
- Prefer closing engineering unknowns through benchmarks, artifacts, tests and playtests; preserve all unverified status as **Planned** / **Unknown**.
- This documentation review does **not** establish a validated Unreal build or production readiness.

# T.O.O.N. — Repository knowledge and work index

**Purpose:** help humans and AI assistants find the **right owning evidence** quickly without reopening settled decisions or mistaking the Unity scaffold for the Unreal game. This is a **navigation page, not a second design specification**.

## Start here

| Need | Authoritative entry point | Interpretation |
| --- | --- | --- |
| Project identity and current confidence | [Root README](../README.md) | Current state, accepted direction, status and next proof |
| Game rules and accepted direction | [Design](design.md) | Canonical T.O.O.N.-specific game design |
| Ordered implementation / validation work | [Roadmap](roadmap.md) and [open GitHub issues](https://github.com/YvesAlbuquerque/TOON/issues) | Plans, not proof of completed code or gameplay |
| Already settled vs actually missing | [Design coherence audit](preproduction-design-review.md) | Cross-check accepted rules **before asking design questions** |
| Unreal target and AI boundaries | [Unreal + AI strategy](unreal-ai-development-strategy.md) | Accepted target; Unreal bootstrap still Planned until exercised |
| Agent behaviour and validation rules | [AGENTS.md](../AGENTS.md), [AI pipeline](../.agents/AI_PIPELINE.md) | Instructions, not implementation evidence |
| Third-party software and licensing context | [Third-party notices](../Docs/THIRD_PARTY.md) | Review licensing separately before redistribution |
| Which files to read for a specific task | [Agent task routing](#agent-task-routing) below | Minimize context; use owning sources rather than loading all docs |

## Design: topic index

The **single owning design document** is [`docs/design.md`](design.md). Use these section links; do not maintain competing summaries as additional authority.

- **Player, time and world:** [player dream](design.md#player-dream), [location and language](design.md#world-opening-starting-location-and-language), [campaign and time](design.md#campaign-and-time), [historical context](design.md#historical-context-global-and-local-timelines).
- **Management and people:** [core loop](design.md#core-loop), [studio economy](design.md#studio-economy), [studio space](design.md#studio-space-facilities-and-workplace-culture), [professionals](design.md#studio-professionals), [autonomy and management](design.md#management-model-and-autonomous-social-simulation), [relationships](design.md#relationships), [employee agency](design.md#employee-agency).
- **Production and creative output:** [four production types](design.md#supported-production-types), [origin of productions](design.md#how-productions-originate), [physical production workflow](design.md#production-as-a-physical-workflow-object), [G-03 authorship](design.md#optional-human-in-the-loop-creation), [three-version limit](design.md#version-limit-and-selection), [G-02 technical failure](design.md#runtime-generation-failure-and-creative-result-boundary-g-02), [pre-release trash and permanent publication](design.md#project-trash-and-deletion), [produced works](design.md#produced-works-as-playable-rewards).
- **Economy and consequences:** [contract terms](design.md#external-contract-terms), [production cost authority](design.md#production-spending-authority-and-schedule-slippage), [G-04 financing and insolvency](design.md#g-04--financial-distress-repayable-financing-and-forced-studio-sale), [historical reception](design.md#market-and-audience-reception), [catalogue income](design.md#main-revenue-paths), [archive and endgame](design.md#historical-archive-and-endgame).
- **Identity and continuity:** [IP continuity](design.md#ip-continuity-across-media), [cross-media identity](design.md#cross-media-identity-consistency), [character ontology and lifespan](design.md#character-ontology-and-lifespan), [competitor studios](design.md#competitor-studios).
- **Proof and visual direction:** [art direction](design.md#art-direction), [first validation slice](design.md#first-validation-slice), [first-slice non-goals](design.md#explicit-non-goals-for-the-first-slice), [persistence](design.md#persistence).

**Already accepted:** the first playable production is a **3–4-panel comic strip**. The full game design still supports **comic strip, comic, 2D animation and 3D animation**. This does not imply a compiled Unreal project or functioning local generator.

## Retrospective methodology adoption

- [Retrospective Concept reconciliation — stages 00–10 and Gate A–D candidate package](concept-retrospective-reconciliation.md) — indexed concept/proposal, historical pivot, Soul/experience synthesis, proposed hypotheses, audience gaps and explicit owner review conditions; **not** a passed Gate D.
- [YFramework stages 00–16 evidence/equivalence matrix](yframework-retrospective-adoption-00-16.md) — bounded retrospective adoption audit, Gate A–H status, missing proof and Unreal validation handoff (issue [#101](https://github.com/YvesAlbuquerque/TOON/issues/101)); **does not replace the canonical design** or assert gate passage.

- [Audience and market snapshot (November 2026)](audience-market-snapshot-2026-11.md) — sourced comparables, player segments, community concerns, AI/Steam caveats, positioning hypotheses and proposed primary validation. Secondary research only; **not** market validation or Gate D approval.

## Agent task routing

**Read the smallest relevant slice**, not the entire ~120 KB design and ~50 KB roadmap on every turn. Start with this index, then the **owning design heading**, the **matching roadmap phase/issue**, and only the **implementation files/tests** relevant to a behaviour claim. The index routes to evidence; it does not supersede that evidence.

| Task / question | Minimum useful evidence set | What not to infer |
| --- | --- | --- |
| Is this game rule already decided? | [Design by topic](#design-topic-index) → [design coherence audit](preproduction-design-review.md) → relevant merged PR/issue if conflicting | A missing Unreal feature does not create a new design vote |
| Change production stages, versions, deletion or release | [Physical workflow](design.md#production-as-a-physical-workflow-object), [trash/publication](design.md#project-trash-and-deletion), [version limit](design.md#version-limit-and-selection), [Phase 4](roadmap.md#phase-4--first-production-management-proof), [#9](https://github.com/YvesAlbuquerque/TOON/issues/9) | Historic comic/Unity flow is not the current authority |
| Change financing, costs, employee consequences or contracts | [Studio economy](design.md#studio-economy), [G-04](design.md#g-04--financial-distress-repayable-financing-and-forced-studio-sale), [Phase 7](roadmap.md#phase-7--studio-economy-and-organization) | Documented scenarios are not tested economy systems |
| Plan/implement Unreal first slice | [Unreal strategy](unreal-ai-development-strategy.md), [Phase 0.4](roadmap.md#04-unreal-bootstrap--planned), [#16](https://github.com/YvesAlbuquerque/TOON/issues/16), [vertical-slice skill](../.agents/skills/toon-vertical-slice/SKILL.md) | Unity scaffold does not establish Unreal readiness |
| Review AI providers, failures or evaluation | [G-02](design.md#runtime-generation-failure-and-creative-result-boundary-g-02), [authorship/AI](design.md#authorship-and-ai), [AI pipeline](../.agents/AI_PIPELINE.md), [#10](https://github.com/YvesAlbuquerque/TOON/issues/10) | Fixture output is not measured local-model quality |
| Inspect old code, packages or compatibility | [Historical evidence](#historical-documents-not-current-requirements), [Flux audit](flux-migration-audit.md), [legacy technical identifiers](../AGENTS.md#legacy-technical-identifiers) | Never alter Unity assets, .meta files or submodule pins as index cleanup |

When documenting a new accepted decision, **edit the owning design paragraph**, then update relevant roadmap acceptance evidence/issue. Change this index **only when a navigational entry or authority boundary changes**; do not copy complete mechanics here.

## Implementation and evidence routes

| Area | Start with | Status boundary |
| --- | --- | --- |
| Unreal bootstrap / first playable loop | [Roadmap — Phase 0.4](roadmap.md#04-unreal-bootstrap--planned), [integrated proof #16](https://github.com/YvesAlbuquerque/TOON/issues/16) | **Planned** until an Unreal project is opened, built and exercised |
| Professional and relationship domain | [Roadmap — Phase 3](roadmap.md#phase-3--persistent-studio-and-people-foundation), [#6](https://github.com/YvesAlbuquerque/TOON/issues/6) | Documented / Planned; not validated Unreal behaviour |
| IP, production and outputs | [#5](https://github.com/YvesAlbuquerque/TOON/issues/5), [#8](https://github.com/YvesAlbuquerque/TOON/issues/8), [#12](https://github.com/YvesAlbuquerque/TOON/issues/12) | Preserve medium-neutral core and stage-specific output |
| AI and reception | [Unreal + AI strategy](unreal-ai-development-strategy.md), [#10](https://github.com/YvesAlbuquerque/TOON/issues/10), [#13](https://github.com/YvesAlbuquerque/TOON/issues/13) | Runtime generation/evaluation requires real on-device measurement |
| Historical Unity scaffold | [Static baseline audit](baseline-static-audit.md), [Unity validation](baseline-unity-validation.md), [Flux migration audit](flux-migration-audit.md), [Flux upgrade validation](flux-upgrade-validation.md) | **Historical evidence**, not present Unreal gameplay |
| Migration/identifier compatibility | [Legacy identifiers in AGENTS](../AGENTS.md#legacy-technical-identifiers), [#31](https://github.com/YvesAlbuquerque/TOON/issues/31) | Do not bulk-rename or remove serialised assets before explicit migration validation |
| Current creative visual review | [Creative direction #28](https://github.com/YvesAlbuquerque/TOON/issues/28) | Owner-reviewed target still requires recorded visual evidence |

### Historical documents, not current requirements

The uppercase **[`Docs/`](../Docs/GDD.md)** directory contains old Ink Through Time documents: [GDD](../Docs/GDD.md), [GTDD](../Docs/GTDD.md), [architecture](../Docs/ARCHITECTURE.md) and [implementation plan](../Docs/IMPLEMENTATION_PLAN.md). They are **explicitly superseded** and intentionally kept for tracing the checked-in Unity scaffold. Do not use old checklists or 1980–2030 three-panel assumptions as a renewed game backlog.

The original `Assets/`, `ProjectSettings/`, `Packages/`, `Plugin/`, `.gitmodules` and `Assets/YJackCore` gitlink are retained **legacy source/migration evidence**. **Quick legacy code paths:** `Assets/InkThroughTime/Scripts/Domain/` (state), `Application/` (services/flow), `Infrastructure/AI/` (provider adapters), `Infrastructure/Persistence/` (historical saves), `Presentation/` (Unity UI), and `Tests/` (historical test sources); these are *not* the target Unreal code map. Neither their size nor their existence is a justification for automatic deletion or for porting obsolete code. Third-party binaries and licence obligations require dedicated review before any cleanup.

## Repository upkeep rules

1. **One authority per claim:** rules in design, implementation in owning source/tests, roadmap/issues for work, YFramework for shared company doctrine. Do not copy accepted rules into another pseudo-GDD.
2. **No fabricated gaps:** compare existing accepted decisions and merged PRs before proposing a new owner choice. Classify unresolved behaviour vs engineering specification vs validation evidence.
3. **Safe edits:** use short PRs into `develop`; keep Unity `.meta`/serialization intact; never rewrite history or remove vendor binaries in a cosmetic cleanup.
4. **Documentation links:** run `python tools/check_docs.py` before merging a documentation PR. The [docs integrity workflow](../.github/workflows/docs-integrity.yml) checks Markdown links on GitHub. It does **not** test Unreal, Unity or runtime AI.
5. **Evidence on exit:** record exact branch/commit and actual compile, test, visual, inference, pacing and save/load proof. A design/doc merge is **Documented**, not `Validated`.

For implementation-specific AI assistance, see the local [vertical-slice skill](../.agents/skills/toon-vertical-slice/SKILL.md). Historical Unity/Flux skills are migration-only.

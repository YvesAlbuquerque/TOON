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

## Design: topic index

The **single owning design document** is [`docs/design.md`](design.md). Use these section links; do not maintain competing summaries as additional authority.

- **Player, time and world:** [player dream](design.md#player-dream), [location and language](design.md#world-opening-starting-location-and-language), [campaign and time](design.md#campaign-and-time), [historical context](design.md#historical-context-global-and-local-timelines).
- **Management and people:** [core loop](design.md#core-loop), [studio economy](design.md#studio-economy), [studio space](design.md#studio-space-facilities-and-workplace-culture), [professionals](design.md#studio-professionals), [autonomy and management](design.md#management-model-and-autonomous-social-simulation), [relationships](design.md#relationships), [employee agency](design.md#employee-agency).
- **Production and creative output:** [four production types](design.md#supported-production-types), [physical production workflow](design.md#production-as-a-physical-workflow-object), [optional creative intervention](design.md#optional-human-in-the-loop-creation), [alternative selection](design.md#version-limit-and-selection), [produced works](design.md#produced-works-as-playable-rewards), [IP continuity](design.md#ip-continuity-across-media), [reception](design.md#historical-context-global-and-local-timelines).
- **Proof and visual direction:** [art direction](design.md#art-direction), [first validation slice](design.md#first-validation-slice), [first-slice non-goals](design.md#explicit-non-goals-for-the-first-slice), [persistence](design.md#persistence).

**Already accepted:** the first playable production is a **3–4-panel comic strip**. The full game design still supports **comic strip, comic, 2D animation and 3D animation**. This does not imply a compiled Unreal project or functioning local generator.

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

The original `Assets/`, `ProjectSettings/`, `Packages/`, `Plugin/`, `.gitmodules` and `Assets/YJackCore` gitlink are retained **legacy source/migration evidence**. Neither their size nor their existence is a justification for automatic deletion or for porting obsolete code. Third-party binaries and licence obligations require dedicated review before any cleanup.

## Repository upkeep rules

1. **One authority per claim:** rules in design, implementation in owning source/tests, roadmap/issues for work, YFramework for shared company doctrine. Do not copy accepted rules into another pseudo-GDD.
2. **No fabricated gaps:** compare existing accepted decisions and merged PRs before proposing a new owner choice. Classify unresolved behaviour vs engineering specification vs validation evidence.
3. **Safe edits:** use short PRs into `develop`; keep Unity `.meta`/serialization intact; never rewrite history or remove vendor binaries in a cosmetic cleanup.
4. **Documentation links:** run `python tools/check_docs.py` before merging a documentation PR. The [docs integrity workflow](../.github/workflows/docs-integrity.yml) checks Markdown links on GitHub. It does **not** test Unreal, Unity or runtime AI.
5. **Evidence on exit:** record exact branch/commit and actual compile, test, visual, inference, pacing and save/load proof. A design/doc merge is **Documented**, not `Validated`.

For implementation-specific AI assistance, see the local [vertical-slice skill](../.agents/skills/toon-vertical-slice/SKILL.md). Historical Unity/Flux skills are migration-only.

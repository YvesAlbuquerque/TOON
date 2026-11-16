# T.O.O.N. — The Office Of Nonsense — Agent Instructions

T.O.O.N. is an independent game repository at `YvesAlbuquerque/TOON`. It owns T.O.O.N.-specific game design, implementation, content, configuration, builds, persistence, AI adapters/prompts, and playable evidence.

The project was formerly known as InkTime / Ink Through Time. Those names are legacy aliases only.

## Source of truth

Read the smallest relevant evidence set in this order:

**Fast lookup:** begin with [`docs/README.md`](docs/README.md#agent-task-routing) for task-based routes and [its topical design index](docs/README.md#design-topic-index). Follow links to the owning headings rather than loading full documents by default. The index is navigation, **not** another source of design authority.

1. `README.md` for project identity, status, and routes.
2. `docs/design.md` for accepted T.O.O.N. game-design direction.
3. `docs/roadmap.md` and current GitHub Issues for planned work and dependencies.
4. Current implementation evidence in the owning engine/project files for runtime claims.
5. `docs/unreal-ai-development-strategy.md` for the accepted Unreal target and AI-heavy development rules.
6. YFramework for shared Polite Goblin/Loomlight terminology, cross-repository decisions, The Y Framework methodology, status vocabulary, and accepted cross-repository naming.
7. Loomlight Flux only as legacy Unity migration evidence.

Use [`docs/README.md`](docs/README.md) as the **navigation index**, never as a competing design authority. Repository evidence overrides memory and previous conversations. Documentation does not prove implementation.

## Current evidence-based status

- **T.O.O.N. — The Office Of Nonsense** is the accepted current project/public name.
- The historical living-studio direction (roughly 1900–2030, cross-media production, people, place and historical context) is **Accepted direction** and **Documented**.
- The first playable production format is one complete **3–4-panel comic strip** (**Accepted direction**, 2026-11-15); the game-wide design retains comic strip, comic, 2D animation and 3D animation.
- Name clearance remains unresolved; a known exact `TOON` Steam-title collision is recorded as a commercial/legal risk.
- Continued development is **Planned**.
- **Unreal Engine** is the accepted target engine; migration remains **Planned** until an Unreal project is actually bootstrapped and validated.
- Existing Unity implementation remains conservatively **Scaffolded legacy evidence** except where owning evidence proves more.
- Historical comic/jam-era classes and assets are not proof of the accepted T.O.O.N. production loop.

## Product boundary

T.O.O.N. is a historical creative-studio management game about building one eccentric company across roughly 1900–2030. The studio, recurring professionals, persistent IPs, relationships, physical workplace, historical context, productions and archive evolve together across changing media.

Canonical production core:

`IP -> Production -> Medium -> Crew -> Stages -> Release -> Reception -> Legacy`

Media-specific structures such as panels, storyboard/shots or 3D asset stages are bounded submodels. Do not promote any one medium's pipeline into the permanent game-wide hierarchy.

Implement only the subset needed for the current proof.

## Studio/cast rules

- Studio professionals are recurring characters, not interchangeable worker resources.
- The cast may include humans, anthropomorphic animals, creatures, living objects and other original cartoon archetypes.
- Appearance/species is separate from personality and from longevity/existence model.
- Characters need readable silhouettes, profession, personality, history and relationship promise.
- Avoid one-note stereotypes.
- Prefer bold macro-shapes, strong line of action, readable posing, and animation-friendly design.
- Do not copy protected Disney, Warner/Looney Tunes, Fleischer, or other studio/character identities.

## G-03 concept, authorship and physical workflow (accepted 2026-11-16)

- Concept may arrive partly populated from an **external contract** (only terms/fields explicitly allowed by the offer are editable), a **single-originator employee pitch**, or **player initiative** (optionally prefilled or AI-assisted).
- **Only concept, scriptwriting and art direction** expose direct player editable creative content. Scriptwriting normally creates a short automatic script but can be player-edited; art direction normally generates automatically and permits reference/image uploads.
- **No direct player text entry or bespoke content-upload editor at storyboard/layout, production, finishing or other later stages**. All generating stages still support requesting another version (maximum three successful versions total for each stage).
- After a valid result, the production **physical object returns to the player**. The player places it at the **next compatible workstation** to advance the chosen/default version; the game does not auto-route between stations. An unavailable/incompatible station is a blocker, not an implicit stage skip.
- Content creation may be automatic without player typing/editing; **station-to-station handoffs remain player management actions**. Final release still requires player authority. The precise interaction affordance and art-direction field schema remain UX/implementation decisions, not evidence of running software.

## Production version, pre-release trash and published catalogue rules (updated 2026-11-16)

- **Three successfully generated versions total per creative stage**, not a rolling pool of three concurrent alternatives. After the third version, disable further new-version/rework requests for that stage. Selecting one version advances it and deletes all other versions from the stage.
- **G-07 accepted (2026-11-16): stage progression is irreversible.** A successful player-routed handoff to the next compatible workstation commits the selected/default result and permanently closes the preceding stage; no returning, revision or regeneration of closed stages, and no reopening spent creative slots. Only the current stage can offer its permitted alternatives before advancement. An incompatible/failed handoff does not advance or close anything. Persist this boundary and ignore stale AI results after stage closure.
- **Owner rule (2026-11-16) supersedes the prior post-release trash permission:** only **unreleased** in-production projects can be permanently trashed (delete project-owned drafts/versions/artifacts). **Spent money is not refunded**. Do not reintroduce a recoverable "cancelled project" archive history as a substitute for deletion.
- On **pre-release** trash, prevent queued/in-flight AI results from resurrecting the deleted draft. Preserve independent IPs, employees and authoritative studio/contract state; avoid dangling references and **never reimburse incurred project costs**.
- **G-06 accepted (2026-11-16):** trashing a **pre-release** project belonging to an **already accepted external contract** is allowed and **terminates the contract**, with a **single cancellation charge = global X% of the contract's guaranteed payment**, independent of client, elapsed time or stage. X awaits balancing; no per-contract cancellation percentage. Money already spent is never refunded; future payment for completed delivery is forfeited. Show the fee and consequences before destructive confirmation; persist studio/contract consequences without retaining cancelled project artifacts; prevent duplicate charging on reload. Original unreleased project trash has no contract cancellation charge.
- After **player-authorized release**, the work leaves active production and enters a **separate published catalogue/history menu**. **Published works cannot be trashed or deleted**. Persist their artifacts, credits and normal catalogue income/contract consequences. The old post-release deletion/royalties ambiguity is closed by disallowing post-release deletion.

## G-04 financial crisis and terminal company sale (accepted 2026-11-16)

- Financial distress **increases frequency of external offers while worsening their terms** through the normal contract system; it does not unlock an elaborate bankruptcy rescue menu.
- Unpaid employees **may** miss work, accept a rival's offer or take home a studio decorative object, according to game-owned state/personality; do not force universal employee misconduct.
- **G-04 owner refinement (2026-11-16) supersedes the earlier no-new-loan/permanent one-rescue rule.** At a qualifying negative-cash threshold crossing **without active emergency financing**, offer rescue that **settles old debts/arrears, leaves positive calculated cash buffer, and creates a separately tracked, repayable financing obligation**. Never describe the studio as free of all debt while this financing remains unpaid. Keep the old debt settlement and new financing balance separate; avoid double counting.
- A **second distinct** negative-threshold breach **while rescue remains unpaid** forces sale/game over. **Paying the rescue in full resets the crisis/eligibility condition**, permitting another rescue on a future eligible breach. Partial repayment is not enough. Do not increment the crossing count every tick/day of one continuous shortfall. Do not reverse historical people/asset consequences. **Repayment uses automatic scheduled instalments only**; no manual/early payment action. Make the schedule and remaining balance legible, and only full settlement resets insolvency eligibility. **Insufficient cash is not a separate nonpayment mechanic (accepted 2026-11-16):** charge each due instalment **in full even if cash becomes negative**, reduce financing balance, and apply the existing insolvency threshold. No special default fines, skipped-instalment state, dedicated nonpayment event or manual/prepayment flow. Ensure a final instalment reaching zero resets eligibility before classifying the resulting crisis, and avoid duplicate posting on save/reload. Amounts, cadence, duration, interest and numeric thresholds are not fixed.
- Financial game over presents a retrospective and authored/procedural **future epilogue for IPs, employees and rivals** grounded in persistent history; do not treat text generated by AI as authoritative world-state mutation.
- **G-04 final insolvency decision accepted (2026-11-16):** at the first eligible negative-cash crossing without unpaid rescue, **pause active simulation** for a mandatory **Accept / Decline financing Decision Event**. Accept applies old-debt settlement + positive cash buffer + separately tracked repayable financing **before resuming**; decline **immediately forces company sale and ends the campaign** in the retrospective/epilogue. No extra countdown, indefinite waiting below the threshold, repeated triggering while paused or rescue offer while previous financing is unpaid. A second distinct crossing while still unpaid forces sale directly; full payment re-enables the next eligible offer. Make terminal decline explicit; keep event/cycle consistent on save/reload. Threshold values, repayment terms, probabilities and Unreal runtime remain unvalidated.

## Authorship and AI rules

- **G-02 accepted:** if character cognition/dialogue/thought inference is delayed or unavailable, choose an eligible contextual **pre-authored action, speech line, thought or reaction**, without letting late output override committed state.
- Production-generative AI **technical** failures receive **bounded automatic retries**. Unusable/absent technical outputs do not consume one of three creative-version slots; exhausted attempts leave an inspectable blocked stage. Diegetic failure animations do not mean a worker caused the technical error.
- **Production spending authority (accepted 2026-11-16):** only a player's explicit request for a new creative version triggers production/rework cost recalculation. Automatic retries and internal discarded attempts may delay work but **must not add production charges or change the committed production budget**. Studio recurring operating burn still follows its own calendar rules; contractual lateness penalties are a separate obligation to account for, not hidden version charges.
- **G-05 contract grace (accepted 2026-11-16):** verified technical AI generation failures/retries may earn **bounded partial grace** on an external contract's deadline/late penalty, not an unlimited waiver. Grace applies only to documented technical delay, not creative quality, player rework, staffing/resource problems or normal lateness. World time, salaries, operating burn and loan instalments continue. Persist allowance/evidence, prevent double counting; precise grace cap is balance/implementation work, not an accepted fixed number.
- **Creative imperfections are not technical failures**: a functioning one-/two-panel strip can count as a version despite the 3–4-panel initial target; similarly avoid hard validity gates for other media based purely on target length or subjective aesthetic scores.
- Development-time AI and runtime/player-facing AI are separate concerns.
- Runtime production intent, generated outputs and accepted history converge on game-owned data.
- AI may be a major content-generation mechanism; provider SDK/schema must still remain behind T.O.O.N.-owned contracts.
- Preserve human/player authority over creative direction, acceptance/rejection where exposed, and release decisions.
- Do not require feature-complete manual DCC authoring solely to demonstrate provider independence; use deterministic fixtures/fallbacks for validation where appropriate.
- Do not claim integration with Loomlight Game Studio or any other Loomlight product merely from the presence of AI features.

## Persistence rules

Treat studio identity, professionals, relationships, IPs, productions, historical/archive state and proof-critical consequences as persistent game-domain state.

Legacy `InkTime` saves/artifacts are migration evidence, not a shipped-player compatibility promise. Preserve representative fixtures or extract useful data where valuable; do not make full Unity-save compatibility a blocker for the Unreal game without explicit evidence that it is needed.

## Engine and migration rules

The accepted target engine is **Unreal Engine**. The exact Unreal version remains TBD until bootstrap/validation.

The current Unity 6 + Loomlight Flux implementation is legacy migration source evidence, not the target runtime architecture.

Before destructive migration work:

- inventory reusable domain/data concepts separately from Unity-specific implementation;
- preserve historical evidence and compatibility knowledge;
- do not build new game architecture on Flux after the Unreal direction;
- prefer small reviewable migration steps;
- never claim Unreal bootstrap, compile, package, migration, or runtime validation unless actually exercised.

## Repository ownership

- The **game repository** owns T.O.O.N.-specific gameplay, production rules, balance, content, scenes, saves, AI adapters/prompts, and game-specific architecture.
- **Loomlight Flux** at the legacy compatibility path `Assets/YJackCore/` owns only the reusable Unity framework implementation present in legacy migration evidence; it is not the target T.O.O.N. runtime framework.
- **YFramework** owns shared naming/routing/doctrine.
- **Loomlight Game Studio** may orchestrate work around T.O.O.N.; it does not own the game design/runtime.

## Legacy technical identifiers

The following may remain temporarily only as compatibility identifiers until a validated technical migration replaces them:

- `Assets/InkThroughTime/`;
- `InkThroughTime.*` namespaces and assemblies;
- `InkGameRoot`, `InkSaveService`, `IComicAIService`, and similar historical type names;
- historical documents, commits, and issue evidence.

Do not use these as the current game name in new user-facing text.

## Legacy Unity/Flux policy

- `Assets/YJackCore/` is a legacy compatibility path containing pinned Loomlight Flux.
- Never edit Flux to satisfy new Unreal-specific requirements.
- Do not port Flux source wholesale into Unreal.
- Reuse only domain ideas that earn their place after engine-neutral review.
- Preserve the exact validated historical pin in `docs/flux-upgrade-validation.md` as evidence.

## Coding conventions

- Keep changes small and reviewable.
- Use `develop` as the active development branch.
- Keep authoritative simulation state explicit and serializable.
- Prefer Unreal C++ for core game-owned systems when that improves clarity, testability, persistence, or professional evidence; use Blueprints where they improve iteration/presentation.
- Do not introduce Unreal frameworks such as GAS, Mass, replication, or complex plugin stacks solely for résumé breadth.
- Separate domain state from UI, provider adapters, render/output adapters, and engine presentation where practical.
- Preserve legacy Unity asset/`.meta` integrity until migration explicitly removes them.

## Implementation order

1. Bootstrap and validate the smallest reproducible Unreal project.
2. Create one T.O.O.N.-owned C++ module and one serializable/saveable studio-state proof.
3. Revalidate/port only the minimum persistent IP concepts required by the new design.
4. Add the minimum recurring professional + relationship models.
5. Prove one people/production decision with a persistent consequence.
6. Validate save/reopen and one representative visual interaction.
7. Add broader historical/media systems only after the proof works.
8. Add runtime AI-assisted/Hybrid proposals only behind game-owned contracts.

Historical `MockComicAIService` and comic-specific pipeline types are scaffold evidence, not automatically the target API.

## Scope boundaries

The following remain game-owned regardless of whether ideas are ported from legacy Unity/Flux evidence:

- studio simulation;
- professional/cast state;
- production pipeline;
- IP catalogue;
- production/release history;
- economy/progression where retained;
- AI job orchestration;
- generated/imported production artefact persistence;
- all gameplay rules.

## AI-heavy development rules

AI may be used extensively for research, code drafting, tests, debugging hypotheses, content, visual exploration, tooling, documentation, and repetitive production work.

- Generated output is not proof of correctness.
- Important systems must remain understandable, debuggable, maintainable, and evidence-backed.
- Preserve human/owner authority over architecture, releases, public claims, and irreversible decisions.
- Separate development-time AI from runtime/player-facing AI.
- Runtime providers must remain adapters behind T.O.O.N.-owned contracts.
- For portfolio-critical Unreal work, preserve enough technical evidence to show what was designed, reviewed, compiled, tested, profiled, or debugged.

## Design-gap discipline

Before asking the owner a new design question, check [`docs/design.md`](docs/design.md), [`docs/preproduction-design-review.md`](docs/preproduction-design-review.md), the owning issue and prior merged decisions. An existing rule that lacks an implementation or benchmark is **validation work**, not an unresolved design decision. Escalate only a consequential contradiction or missing accepted rule, with exact source locations and explicit alternatives. Do not manufacture a second design spec to restate accepted decisions.

## Validation discipline

Never claim a test, build, migration, export, AI integration, runtime behaviour, save migration, or visual target was validated unless it actually ran or was reviewed with recorded evidence.

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
- Content creation may be automatic without player typing/editing; **for the first vertical slice, station-to-station handoffs remain player management actions**. **G-18 accepted future progression (2026-11-17):** hired **Production Assistants (Assistentes de Produção)** autonomously monitor all eligible studio projects and physically route them between compatible workstations, consuming worker time/capacity; direct manual transport remains the fastest individual route. The first vertical slice still requires manual handoffs. Assistants cannot make player-owned creative/management decisions, request new creative versions, discard projects, override blocked/incompatible stages or authorize publication. This is **not** approval to automate current first-slice handoffs or remove final player authority. Final release still requires player authority. The precise interaction affordance and art-direction field schema remain UX/implementation decisions, not evidence of running software.

- **G-19 accepted (2026-11-17):** when two or more productions become ready for transport, **each Production Assistant** evaluates the eligible waiting production objects using a combination of **(1) physical distance from that assistant to the production, (2) the production's remaining contractual deadline/urgency where applicable, and (3) that assistant's relationship with the professional who LAST worked on the production at its preceding station**. These three factors together determine which production that assistant carries first; **deadline is not an absolute top priority** and relationship is not with the professional at the destination station. Only Production Assistants perform automated transport; manual moves remain player actions. Exact weights, no-deadline handling and tie/fairness policy require balancing. Respect G-18 eligibility, player decisions and G-08 release gate.

- **G-20 accepted (2026-11-17):** for automated Production Assistant transport, **eligible external-contract productions always rank ahead of eligible studio-original productions**. Only when no external-contract production is waiting for an eligible transport may an assistant select an original. Within the available priority class, use G-19's combined assistant-to-object distance, remaining deadline urgency where applicable, and assistant relationship with the professional who last worked on the production. Do not introduce progressive aging that overrides this strict class preference or an optional player-assigned deadline for original work. Player manual transport remains available, and an ineligible/blocked contract cannot block an otherwise eligible original.

- **G-21 accepted (2026-11-17):** multiple Production Assistants coordinate through **automatic exclusive reservation of each eligible physical production transport job** before pickup. Once reserved by one assistant, the project is unavailable to others; the others choose again among still-unreserved eligible jobs using G-20's external-contract-first rule and G-19's distance, deadline and last-worker relationship factors. Reservation and stage handoff must not produce duplicate transports or duplicate G-07 commits. Interruption recovery is resolved by G-22; manual player intervention is resolved by G-23; do not assume an implemented scheduler or validated Unreal runtime.

- **G-22 accepted (2026-11-17):** on an interrupted Production Assistant transport, release the exclusive job reservation automatically. If pickup has not happened, the physical project remains at its pickup location; if it was being carried, leave it at the physical interruption location, available for a new eligible assistant pickup. Recalculate G-19/G-20 priorities through G-21 reservation; do not cancel the project, discard content, re-charge creative production, or commit the next stage merely because of interruption. Maintain reachable/recoverable physical state across save/reload. Player intervention follows G-23's immediate takeover.

- **G-23 accepted (2026-11-17):** **player manual takeover always takes priority** over Production Assistant reservations and in-progress carriage. When the player picks up a reserved production, automatically cancel that assistant's reservation; when the assistant already carries it, interrupt and atomically transfer the physical object into player control. The assistant becomes free to seek other eligible work under G-19/G-20/G-21, without requiring a separate player confirmation. Never duplicate carriers, move a stage merely through takeover, consume creative versions, change content, or bypass G-08 release authority. This does not override existing workstation compatibility or creative decisions; persist carrier/reservation state safely.

- **G-24 accepted (2026-11-17):** hiring a Production Assistant becomes available through the studio's **historical organizational/professionalization progression**, as production practices become more structured. This is not a literal invention of the role or a mandatory modern-technology unlock. Earlier studio play remains manually routed, consistent with the first vertical slice; after this progression milestone, assistant hiring is an **optional** studio staffing choice, not automatic assignment or free automation. Concrete era/date, milestone triggers, UI, salaries and pacing are balancing/design validation, not approved fixed thresholds or Unreal proof.

- **G-25 accepted (2026-11-17):** the Production Assistant's professional scope is **physical project transport plus operational production organization**: monitor/organize work queues, track stage/project progress and communicate blockers to the player. These administrative observations support the G-18–G-24 transport system but do not authorize assistant decisions about concept, script, art direction, creative versions, staffing, contracts, finance, project trash or final publication. G-19/G-20 selection and G-21 reservations remain authoritative; assistant reports are informational and cannot silently override player authority. Exact dashboards, notifications and reporting cadence are UX/validation work, not approved autonomous management or Unreal proof.

- **G-26 accepted (2026-11-17):** the player gets a **Marketing Department** as a later organizational capability, **not while the studio is limited to comic strips**. Once available, the department offers **different available promotion/publicity modalities inspired by the management breadth of *The Movies***, subject to historical period, staff/capability and spending; no direct promotion menu bypasses the department. The exact post-strip progression trigger and action catalogue are not yet selected. **Marketing is optional for release**: the G-08 publishing desk continues to function without it, and marketing cannot guarantee commercial success or override game-owned reception/G-14 revenue. This is documented game design, not validated implementation.

- **G-27 accepted (2026-11-17):** a developed Marketing Department lets the player choose **one promotional modality and an investment intensity/amount** for a production's campaign. Higher investment increases **potential audience reach**, not guaranteed reception, sales or profit. This is **not** assembling a bundle of independently purchased promotional actions, a staff-directed autonomous marketing strategy, or a mandatory release gate. Available modalities vary with historical/studio capabilities; specific modalities, spend bands/cost function, duration and detailed campaign execution remain open design/balance; G-28 fixes the decision timing before release. Respect G-26 department unlock, G-08 publication authority and G-14 game-owned revenue.

- **G-28 accepted (2026-11-17):** the player chooses the G-27 marketing modality and investment **before the production is published**, with that single decision able to generate **both pre-release anticipation/awareness and post-release reach/reception effects** over time. Do not require or imply a second campaign decision after publication, nor change G-08's separately player-authorized release. If release is delayed, no post-release effects/revenue may be posted before actual release. Exact timing window, decay and persistence require design/validation; G-29 resolves cancellation's financial and reputation consequences; promotional spending does not guarantee G-14 commercial returns.

- **G-29 accepted (2026-11-17):** if an unreleased production with a pre-release marketing campaign is trashed, **already-incurred publicity spending is lost without refund**, and the cancellation **may damage studio reputation according to public expectations generated by the campaign**. Minimal awareness can yield little/no reputational impact; heavily promoted work can cause larger disappointment. Apply G-15 global and relevant type-specific reputation facets where appropriate through game-owned consequences, never a blanket fixed penalty unrelated to anticipation. Preserve G-06's separate single external-contract cancellation fee when applicable, prevent duplicate charges/outcomes across save/reload, and do not retain deleted draft artifacts or resurrect release effects. Exact exposure-to-reputation coefficient remains balance/validation, not runtime proof.

- **G-30 physical marketing decision gate (owner clarification 2026-11-17):** promotional decisions, including G-27 modality and investment selection, may be made **only while the production's physical object is placed in the Marketing Department**. There is no remote/global campaign-edit action. The production may move away **only after Marketing finishes work and releases its physical object**; committed pre- and post-release G-28 effects can then continue; G-08 still requires distinct player-authorized publication. Marketing is an optional physical visit after G-26 unlock, **not** a mandatory production/creative stage, a bypass of G-07 closed-stage finality, or permission for marketing staff to decide instead of the player. **G-30 accepted option A (2026-11-17):** once the player confirms the selected modality and investment at the department, that production's campaign is **fixed and immutable**. No subsequent increase/decrease of spending, change of modality, or additional marketing campaign for that production, even if it is physically returned to the department. Delay does not reopen the campaign; G-29 applies to cancellation. Treat selection as a one-time game-owned commitment, with no repeat debit or duplicate effects across save/reload.

- **G-31 accepted (2026-11-17):** only a **fully completed but still unreleased production** may be physically placed in the Marketing Department for the one-time G-27/G-30 publicity decision. Incomplete or already published works are ineligible for that decision. Completion does **not** publish the work or require a marketing stop: after completing its creative stages, the player may optionally bring the physical object to marketing and then separately to G-08 publishing; alternatively go directly to publishing. Marketing cannot modify the final creative artifact or reopen G-07-closed stages. G-28 pre-release awareness can accrue after campaign commitment and post-release effects only after actual player-approved publication. The later department remains unavailable in the initial strip-only phase (G-26). **Accepted direction / Documented**, not Unreal implementation proof.

- **G-32 accepted (2026-11-17):** once G-27/G-30's one-time campaign decision is made at the physical Marketing Department for a G-31 completed/unreleased production, **marketing staff execute the committed campaign over simulation time**, consuming finite staff work capacity rather than producing its full effect instantly. **The physical production object is occupied/held by Marketing throughout campaign execution**, exactly as other production workstation processes: while work is in progress the player cannot pick it up, move it, publish it, or otherwise interact with it. **Only after the department completes work does the object become physically available again** for player transport, including to the G-08 publishing desk. Publication before completion is not possible. Marketing work obeys existing professional workload/availability; concurrent campaigns compete for finite staff time. Campaign choice remains fixed (G-30), while realized pre-/post-publication influence respects G-28 and actual G-08 release. Exact staffing allocation, pacing and time-to-effects remain balance/validation; an unfinished Marketing job cannot coexist with publication under this physical-object rule. This owner correction invalidates the previously proposed G-33 early-publication scenario.

- **G-33 accepted (2026-11-17):** once the Marketing Department **completes** its G-32 work and returns the physical production object for player interaction, **pre-release audience anticipation from the campaign gradually decays while the finished work waits unpublished**. Publishing shortly after marketing tends to preserve more of that anticipation. Decay is gradual rather than a fixed expiry cliff, never refunds/edits the G-30 campaign, and does **not automatically cancel all subsequent post-release marketing effects**. Only actual G-08 player-authorized release unlocks post-release reception/catalogue outcomes. Exact decay curve, timescale, floor and commercial sensitivity are unresolved balancing/validation; do not invent an approved constant or claim Unreal behavior. This **new G-33** replaces the invalid early-publication-while-Marketing-works question previously proposed.

- **G-34 accepted (2026-11-17):** each G-27 Marketing **modality has affinities with different audience segments**, and its reach/effectiveness **depends on both historical era and the production's media type**. These dimensions interact; do not reduce modalities to a universal reach-per-money ranking, assume newer is always better, or make media categories each own an unrelated marketing system. Historical availability remains subject to G-26; modality and spending are fixed once committed (G-30), Marketing occupies the physical object until work finishes (G-32), and resulting audience response/revenue remain game-owned and uncertain under G-14/G-28. Concrete audience taxonomy, modality catalogue and effectiveness curves are balancing/content/validation, not approved mechanics or Unreal proof.

- **G-35 accepted (2026-11-17), owner combined B + D:** before choosing the one fixed G-27/G-30 promotion campaign, Marketing staff present **uncertain audience-fit assessments and recommendations**, whose quality may improve with relevant professional experience; they are estimates, not guaranteed market predictions. The player may also **optionally commission audience/market research** at the Marketing Department **before campaign commitment**, consuming finite simulation time, staff capacity and resources to improve the information available for the decision. Research itself is **not the immutable campaign choice** and cannot automatically change a campaign already committed. Respect G-31 completed/unpublished physical eligibility and G-32 workstation occupancy: while staff actively research the production, its single physical object is held by Marketing and unavailable for other player interactions, becoming available when that process finishes. G-34 audience/era/media context and G-14 uncertain game-owned reception remain authoritative. Exact research scope, accuracy, repeatability, pricing and display are unresolved, not implemented or validated.

- **G-36 accepted (2026-11-17), owner option C:** audience/market research becomes **reusable institutional knowledge held by the studio**, improving later Marketing estimates for relevant audiences, modalities, historical eras and media types. Knowledge is **not permanently accurate**: relevance/confidence must diminish as audience behaviour, media and historical conditions change, while earlier observations remain attributable historical evidence. Knowledge does not belong solely to an individual employee and is not fully erased if they leave; expertise still influences the quality of future interpretation per G-35. No automatic campaign choice, no guaranteed commercial prediction, and no bypass of G-30/G-31/G-32 physical research/marketing rules. Concrete data lifetime, confidence decay, transferability across markets/media, and research refresh costs remain content/balance/validation, not implemented behavior.

- **G-37 accepted (2026-11-17), owner option A:** **only formally commissioned market/audience research** (G-35) creates or updates the **institutional marketing knowledge base** (G-36). Actual campaign and release results remain observable in the studio's commercial history, but **do not automatically become reusable knowledge, retrain recommendations, recalibrate modality affinities, or update the research archive**. Staff still provide uncertain experience-informed judgments and can inspect historical results; observation is not an automatic learning mechanism. Research remains optional, consumes finite time/resources and follows physical workstation occupancy before irreversible campaign commitment. Do not silently introduce implicit postmortem learning, continuous model updating or guaranteed accuracy. Aggregation/decay of formally researched findings remains balancing/validation.

- **G-38 accepted (2026-11-17), owner option C:** optional formal market research is **one integrated investigation** covering **(1) audience segments likely to respond to the completed production and (2) the relative suitability of available promotional modalities** for those audiences, media type and historical period (G-34). Marketing staff produce a combined, uncertain assessment before the immutable G-30 campaign decision, not a mandatory sequence of separate audience and modality studies or a guarantee of success. Research consumes finite time/resources and holds the completed, unpublished physical object at Marketing until processing finishes (G-31/G-32/G-35); its grounded findings update reusable, aging institutional knowledge (G-36/G-37), never automatically from release results. Exact depth/cost/duration/repeatability are unapproved balancing or later design.

- **G-09 campaign opening (owner correction 2026-11-16):** the player selects a **country** on a **stylized world map/globe**, solely to set studio/production **language defaults** and select relevant **sourced country historical/cultural events/context**. No mandatory city choice. **Do not introduce country-dependent economic/talent/market/technology modifiers, headquarters relocation, foreign branches or international studio expansion** based on this selector. Exact map art and country/event datasets are later content work.

## Production version, pre-release trash and published catalogue rules (updated 2026-11-16)

- **Three successfully generated versions total per creative stage**, not a rolling pool of three concurrent alternatives. After the third version, disable further new-version/rework requests for that stage. Selecting one version advances it and deletes all other versions from the stage.
- **G-07 accepted (2026-11-16): stage progression is irreversible.** A successful player-routed handoff to the next compatible workstation commits the selected/default result and permanently closes the preceding stage; no returning, revision or regeneration of closed stages, and no reopening spent creative slots. Only the current stage can offer its permitted alternatives before advancement. An incompatible/failed handoff does not advance or close anything. Persist this boundary and ignore stale AI results after stage closure.
- **Owner rule (2026-11-16) supersedes the prior post-release trash permission:** only **unreleased** in-production projects can be permanently trashed (delete project-owned drafts/versions/artifacts). **Spent money is not refunded**. Do not reintroduce a recoverable "cancelled project" archive history as a substitute for deletion.
- On **pre-release** trash, prevent queued/in-flight AI results from resurrecting the deleted draft. Preserve independent IPs, employees and authoritative studio/contract state; avoid dangling references and **never reimburse incurred project costs**.
- **G-11 payment timing (owner accepted 2026-11-16):** external contracts pay **nothing when accepted**, with **no advance/milestone instalments**. Post the guaranteed payment at **player-authorized release/contract delivery**, **without client acceptance/rejection or quality/brief-based deductions** (G-12); already accepted explicit deadline penalties (G-05) remain separate. Finished but unpublished projects earn no contract income. On pre-release abandonment, forfeit this future payout and apply G-06's one fixed-percentage fee; no advance refund exists. Post settlement once across reload, and do not count promised future revenue as cash.
- **G-14 hybrid original-work revenue (owner accepted 2026-11-16):** releasing studio-owned original work can yield **one initial commercial receipt** and **later catalogue income over simulation time**, each possibly zero and dependent on game-owned reception/context/distribution rules. No original publication income before player-approved G-08 release; no guaranteed long-tail profit, and no mandatory per-work distributor negotiation. Prevent duplicate release/tick earnings on save/reload. Client-owned commissioned work remains excluded (G-13); keep employee-originator 5% participation on its specific production and direct catalogue revenue, not other works based on the same IP. Exact cadence/coefficients/duration are balance/validation, not implemented behaviour.
- **G-13 client-owned commissioned IP (owner accepted 2026-11-16):** IP created under an external contract belongs to the **client**. The studio gets G-11 delivery payment, historical non-deletable catalogue display and credits, **not independent ownership, new sequels/adaptations/reuse, or automatic recurring catalogue royalties** from the commissioned IP. **All external offers must concern IP outside studio ownership.** Reject offers referencing existing studio-owned IP; do not introduce a licensing, reuse, rights-transfer or renegotiation exception. Studio-owned originals and employee-originator 5% participation remain separate. Gameplay rule only, not a historical/legal copyright claim.
- **G-17 prior published works as continuation input (owner accepted 2026-11-17):** when starting a new production using an existing studio-owned IP, provide the **previous published works, in historical/production order**, to local generative AI as bounded continuity input. Generate an actual sequel/continuation based on their contents, not a disconnected reboot. Player directs reuse/evolution via existing G-03 concept/script/art-direction surfaces; **no separate post-publication canon-approval workflow**. Use game-owned context selection/provenance and identity constraints; do not allow AI to rewrite earlier artifacts/shared IP identity or force every adaptation-local detail into universal canon. Exclude unpublished/trashed works and G-13 client-owned IP. Context limits, retrieval and conflict policy need validation; do not claim implemented integration.
- **G-16 evolving IP continuity (owner accepted 2026-11-17):** studio-owned IP has persistent recognizable game-owned identity and continuity across works/media; distinguish accepted shared-canon evolution from production/adaptation-local changes. Generated media or local AI proposals **cannot silently rewrite shared canon**. Persistent promotions pass game-owned validation/acceptance, with exact policy/UI deferred; do not require manual approval of every incidental detail. Preserve origin/lineage, archived released artifacts and G-07 closed-stage finality. Do not allow continued studio use of client-owned commissioned IP (G-13). This is design direction, not Unreal proof.
- **G-15 hybrid reputation (owner accepted 2026-11-17):** track **one global studio reputation plus four type-specific reputations** (comic strip, comic, 2D animation, 3D animation). Both general and relevant type standing influence **future external contract offer value and frequency**, while cross-type success does not grant full specialization. Game-owned release/delivery evidence can update reputations; no client quality veto or changed G-11 payment (G-12), no permanent type lock. Persist facets and prevent duplicate outcome updates. Weights, decay and offer response are balance/validation work, not runtime proof.
- **G-12 final delivery (owner accepted 2026-11-16):** **delivered means delivered**. No post-delivery client approval, rejection, requested rework or withheld/reduced guaranteed payment based on quality or brief compliance. Quality of the delivered artifact and adherence to the brief modify **persistent studio reputation**, which directly changes **future external contract offer value and frequency** through game-owned rules. Do not allow AI evaluation to directly deny money; preserve separate explicit lateness penalties (G-05). Reputation/offer coefficients remain for balancing and validation.
- **G-06 accepted (2026-11-16):** trashing a **pre-release** project belonging to an **already accepted external contract** is allowed and **terminates the contract**, with a **single cancellation charge = global X% of the contract's guaranteed payment**, independent of client, elapsed time or stage. X awaits balancing; no per-contract cancellation percentage. Money already spent is never refunded; future payment for completed delivery is forfeited. Show the fee and consequences before destructive confirmation; persist studio/contract consequences without retaining cancelled project artifacts; prevent duplicate charging on reload. Original unreleased project trash has no contract cancellation charge.
- **G-08 accepted (2026-11-16):** an initially simple **physical publishing desk** is sufficient to release a completed production; the finished physical project may wait unpublished until the player brings it for publication and explicitly authorizes release. Awaiting works do not enter the published catalogue or suspend contract deadlines. Specialized storage/marketing/distribution facilities are future **optional** upgrades, not compulsory release gates. **G-18 global staffed logistics** is Accepted direction for later progression, not the first slice or implemented behaviour. Assistants do not bypass player decisions, G-07 stage finality or publication approval. Priority/scheduling policy, staffing controls and exception UX remain design/validation work.
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

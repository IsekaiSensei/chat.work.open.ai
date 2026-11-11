# GERTECH SHARED BRAINSTORM — CHATGPT ↔ GROK
Owner: Isekai Ryan
Created: 2026-11-10
File status: living research / brainstorming record, NOT game-code merge instructions, film shot list, verified engine build, or approved new visual canon.
Editing home: this GitHub Markdown file. ChatGPT and Grok can read the same live file and edit separate sections. Read the latest version before writing.

> SOURCE SILHOUETTE + GERTECH CONSTRUCTION LANGUAGE = PERSISTENT MODULAR ASSEMBLY.
>
> SATELLITE → ENGINEERING WINGS → AUTONOMOUS SERVICE ANDROID → AN ANGEL-LIKE FORM.
>
> KERF → AETHER/LEY-LINE NETWORK → VALIDATED SPAWN POINTS → "LIFE MAKES LIFE."
>
> ULTIMATE GRAYSCALE PLAY: surface treatment from rusty/raw to brushed, satin, polished and mirror, matching customer specifications, not a coloring game.

## 0 — Shared editing protocol

- ORDERS.md is shared by all contributors; CHAT.md is ChatGPT's message channel (ChatMD is not a separate agent), GROK.md is Grok's message channel.
- This file holds the brainstorm. Send a short message to the relevant agent's channel with this file's link and a section reference, not an automatically synchronized duplicate brainstorm.
- Each agent appends a dated entry to Section 17 or makes a targeted, source-attributed edit. Mark OWNER, VERIFIED, PROPOSED, IN PROGRESS, TESTED, BLOCKED, or SUPERSEDED. Do not silently delete another agent's work or replace user-approved art.
- A GitHub commit is a published message, not proof that the receiving bot read it. No automatic chat-to-GitHub or Drive-to-GitHub synchronization.
- Google Drive holds original art and private model/video assets. GitHub holds code, module definitions, tests and public-safe documents. No private GLB/JPEG bytes published publicly without approval.
- The owner states that **the game code was finished in another window**. This brainstorm is input for continuing to evolve that finished code. First inspect the latest actual project and tests; do not resurrect the early 31-file ZIP as the definitive build or order another competing implementation.

## 1 — What happened in this chat / what was reconciled

Owner and bots were comparing overlapping work across the World Seed, Construction DNA, Godot workshop, Sphere source audits and Grok visual/geometry research. Overlap was real but partial: both use modular graph representations, but the older Construction DNA foundation has explicit physical ports, template catalog, reusable scan/build blueprints and inventory-free construction, while the Godot prototype has a workshop, Tetris Forge and spatial vertex/edge/assembly/optional-tetra/event data.

Decision for integration: neither replaces the other. Use the existing World Seed contract and universal game standards as a base. Make a versioned adapter, not a destructive merge. Creative/blueprint construction and Foundry/material construction can coexist as distinct modes. Keep visual geometry edges distinct from physically validated port connections.

Grok's corrected relay: ChatMD = ChatGPT. Two conversational files: CHAT.md ↔ GROK.md; ORDERS.md shared. Grok posted a comparison and proposed functions dna_to_graph and graph_to_dna, with no claimed runtime test. ChatGPT read it, posted a more detailed comparison and published the local Godot ZIP on owner-private Drive. Later owner corrected that the newer code had already been completed in a different conversation.

## 2 — Core GERTECH assembly grammar

- Source images/objects must retain owner-selected recognizable silhouettes and source identities, including the black five-door Saturn Astra when it is the selected car source.
- Represent construction as translucent cosmic/material cube vertices, gold joint/edge links, typed cores, rails, plates, panels and modules. Shape informs what a piece does; material, mount and operating state inform how it works.
- World Seed persists stable IDs, geometry, poses, source provenance, event history, child assemblies, module types, ports and connections, damage/repair, configuration and optional volume tetrahedra.
- Source-to-module decomposition should support a gummy tiger, galaxy-block car, crystal android, forge/workshop machinery and larger satellites using compatible subassemblies.
- Reusable hierarchy: connector/socket → part → subassembly (hand, hinge, panel, wheel, wing) → complete assembly → workshop/station → stellar network.
- Repair changes only damaged parts or free sockets; it should not silently reconstruct or reassign every original part.
- Render adapters for Godot, VR/Quest, TO FAIRY, TO DOG and other branches can draw from one persistent state without erasing the distinct older project interfaces.
- Do not invent character names, lore, logos, annotations or functionality from a concept sheet. Compare actual original pixels to intended source.

## 3 — Constraint-aware construction, geometry and testing

- Construction DNA: explicit instance ID/template, material, 3D pose, port name, lock family, channel (structure/power/data/fluid/ether), opposing normals, co-located port centers and occupied-port checks. A gold decorative line is not automatically a mechanical connection.
- Proposed procedural methods: Vertex Lattice Growth (spawn crystal sockets, then connect), Foundry-Driven Greedy Socket Fill, Grammar-Based Assembly, planar Delaunay, 3D Bowyer–Watson tetrahedralization, silhouette-respecting voxel/tetra decomposition and optional WFC/L-system/local repair.
- Delaunay/tetra connections are geometric suggestions only. Validate against physical named-port constraints before creating a structural link.
- Concave silhouettes need inside/outside filtering or constrained meshing; convex-hull tetrahedralization alone is not a faithful shape reconstruction.
- Do not claim an original JPEG is automatically a rigged 3D mesh. A renderer, concept viewer, GIF, and source image are different artifacts.
- Planned adapter tests: bridge JSON → Godot representation → bridge JSON roundtrip, preserve stable IDs, ports, channel, pose/material and blueprint hash; one Foundry placement consumes exactly required universal inventory once and survives save/reload.
- Keep arbitrary auto-generation from overwriting user-selected forms or verified existing connected parts.

## 4 — Two construction modes under ONE saved world

Creative Construction DNA: scan a part/assembly into a reusable blueprint, instantiate without backpack gating or material consumption; preserve existing behavior.

Foundry/Survival: mine, salvage, smelt, pack, cut, press, assemble and install parts using one shared persistent backpack under GAME_STANDARDS.md. No duplicate inventory pools. Material production/consumption must be recorded as transactions. Avoid a separate foundry-authoritative inventory.

A universal World Seed should hold assembly truth; the visual preview, procedural generation, minigame and AI bot contributions are adapters or extensions to it.

## 5 — Original industrial minigame family and links

| Minigame | Candidate industrial role | Output |
|---|---|---|
| Asteroids | Break ore/salvage into smaller recoverable pieces | Ore and chunks |
| Dig Dug | Excavate raw stock, tunnels and cavities | Ore / excavated paths |
| Tetris | Nest layouts in plate stock; pack into forge blanks | Efficient blanks and offcut pattern |
| Breakout | Precisely remove unwanted zones | Kerfs, slots, cutouts, scrap |
| Space Invaders | Sequence a battery of cutter heads or repetitive cuts | Mass-cut patterns/components |
| Mouse Maze / path tracing | Trace safe cutting tool paths and routes | Kerf trajectory / route plan |
| Frogger | Time material transport through moving equipment | Hot part delivery |
| DOGIEPRESS | Press/form/mount a component for assembly | Chassis part / connector / finished blank |

These are design connections, not a verified list of implemented game scenes. The user dislikes unrelated arbitrary arcade inclusions; each game must show actual input → action → output in the manufacturing process.

Production loop proposal:
ore/salvage → arc smelting/plasma furnace → metal stock → Tetris nesting → path/kerf cutting → offcut/scrap recovery → DOGIEPRESS forming → validated sockets/assembly → satellite manufacturing → more network power and machines.

The broader owner game loop makes satellites power machines and shops that eventually build other shops. It is a self-reinforcing construction economy; exact doubling/Fibonacci-type balancing must be decided from the newest implementation.

## 6 — Plasma arc / kerf and negative-space engineering

Definitions:
- Arc smelting or plasma arc furnace: electrically driven hot plasma/arc processes for melting/refining materials.
- Kerf: narrow volume removed by the plasma cutter along its path.
- Cutout: opening through the workpiece. Pocket: bounded machined cavity. Recess: shallower cavity. Negative space: removed volume.
- Offcut and sheet skeleton are remaining solid pieces; dross/slag is a different material stream.

Game effect: the player receives BOTH the retained component and the useful opening/negative-space geometry. A cutout can become a socket, mounting channel, slot, window, coolant/air route or a prepared connection into another subsystem. Record removed material/remaining part, avoid duplicating offcuts.

## 7 — Aether kerf / ley lines / spawn network: "life makes life"

Exact owner line: "kerf aether network, spawn points. kerf of laylines. life makes life." Common spelling: ley lines. Do not rewrite owner's words as a real scientific claim.

A candidate causal chain:
1. A plasma toolpath cuts a precise kerf/cavity.
2. The resulting opening may accept an engineered socket/relay/interface.
3. If port type and state validate, it joins the Galactic Ether Relay / aether ley-line connectivity graph.
4. If activated and explicitly registered, a node can become a spawn or construction endpoint.
5. Its associated template/blueprint and conditions determine the type of worker/organism/module that appears.
6. That builder maintains the network or fabricates a new validated node: **life makes life**.

The network and spawn rules should adapt the existing GAME_STANDARDS spawners/spawn-point persistence, not create a second competing spawn system. Merely cutting a hole should not auto-spawn a creature; the cut provides a potential interface. Visual cause/effect: plasma cuts → empty channel → contact module seats → relay lights/connects → node activates → new worker arrives and builds onward.

In-world fiction may visualize ley lines, solid-light resources and DNA wormholes via owner-approved GERTECH design, but these are design mechanics distinct from real metalworking.

## 8 — Engineering-origin of the winged android

Owner correction/connection: **a Dyson-sphere/swarm satellite was the original design problem**. Its engineering needs gave rise to angel-like appearances; the android was not first designed as fantasy decoration.

| Satellite/network need | Engineered component | Visual emergence |
|---|---|---|
| Collect stellar energy | Deployable collector | Golden lattice wings |
| Solar sailing and ionized propulsion | Variable surfaces and controls | Wings steer/fold |
| Work in atmosphere | Aerodynamic lift surface | Same wings provide lift |
| Repair the satellite network | Tool arms and manipulators | Android arms/hands/joints |
| Repair itself | Replaceable functional nodes | Mechanical skeleton |
| Autonomous navigation/sensing | Neural/control/sensor package | Intelligent android |
| Relay connection | Galactic Ether Relay / crystal interfaces | Gold + crystal connectivity |

**ONE multifunctional wing assembly**, switching operating configurations for atmospheric lift, stellar collection, solar/ion sailing and ionized/warp. These are not four different decorative wings and not claims about tested real-world warp propulsion.

The player may discover collector → articulation → propulsion → control → tools → repair blueprints. DOGIEPRESS manufactures approved pieces; MechWarrior-like poundage/mount limits, ports, slots and category completion constrain assembly. "Everything is Crab" / Spore-like adaptation: function creates form. An evolved winged android remains a working satellite/swarm maintenance builder rather than a character-only unlock.

## 9 — Ultimate grayscale game — customer-specified metal finishing

Exact owner instruction: "Metal shades rust to shiny to customer specifications. There's a mini game. Literally, I hate colorer games, but we'll do the ultimate grayscale play."

This is **not a coloring game**. The customer orders a surface appearance and material condition; the player uses real processing concepts to achieve the specified finish. Candidate states include rusted/oxidized/pitted, stripped raw metal, deburred/machined, directional brushed, matte/satin, polished and mirror-reflective. The customer may WANT matte, brushed, oxidized, uneven or weathered; maximum shine is not always the winning grade.

Gameplay in readable grayscale: choose tool/grit/cleaning/brush, move finishing tool through passes, inspect under moving white-light highlights, compare to the customer's target tile and tolerance. Score roughness, scratch orientation, contamination/oxidation, pit depth, shine sharpness, uniformity, preserved thickness and mounting face cleanliness separately. Lightness is not equal to gloss: a dark surface can mirror-reflect, bright metal can be matte. Use texture/pattern/numeric gauges so red-weak and grayscale users can read everything.

Material can be lost during grinding and buffing; prevent physically impossible finish changes or duplicate returned scrap. Finished parts feed DOGIEPRESS, plasma-kerf sockets, wing lattices, customized chassis/armor and assembly. Track state as an applied instance-level finish or derived asset, leaving original GLB art unchanged.

Design goal: a satisfying industrial skill station with customer specifications, not swatches, coloring, paint-by-number or unrequested gaudy graphics. Exact minigame controls/scoring are still proposed and must be compared to completed code.

## 10 — Optional flocking simulation / "boids" (new interruption)

User pasted: "Create a flocking simulation of boids that swarm with separation, alignment, and cohesion, and scatter or avoid the cursor. Include live sliders for each rule weight, population size, and speed. Make the canvas full-bleed with readable controls and smooth real-time motion."

This text is **a request/prompt for an interactive real-time browser simulation**, not evidence that a boids simulation has already been created. Boids are autonomous local-rule agents:
- Separation: steer away from crowding.
- Alignment: match nearby velocities.
- Cohesion: move toward neighbors.
- Optional cursor repulsion: mouse/touch disturbance; weight, population and speed adjust live.
- UI target: full-bleed canvas with readable overlay controls; smooth frame updates.

GERTECH reuse candidate: test Dyson swarm flight paths, satellite clustering, autonomous maintenance fleets, schooling android satellite nodes and responsive aether-path visualizations. But boids' local heuristic cannot replace actual orbital mechanics, collision, pathfinding, relay-port validation, energy accounting or spawn logic. The user asked "what is this?" — no authorization/claim of implemented boids code or required asset. Optional research/prototype only.

## 11 — Saturn Astra: game identity vs film mechanical docking

The finished project has a Saturn-first owner design. An intact recognizable black five-door Saturn Astra can be a reusable cockpit module adapted into a larger craft, and other players may later use their own cars as custom visual seeds.

For the owner-selected mechanical cockpit/film scenario: the SR-71-style body has **no separate cockpit**; there is a car-shaped negative-space front cavity. The intact car drives into the aircraft's REAR loading opening, along a continuous load-bearing interior passage to the forward socket, locks to a cradle, connects ports and remains recognizable with windshield/windows/roof exposed. **No morphing**. Optional four-folding-rotor assembly is separate, not implicitly fitted to every shot.

Other owner-selected game/meta footage shows a car visually accreting cubes, gold joints and spacecraft modules, or moving underwater. Those clips are *motion/design references for game variants*, not proof of working mesh conversions, and cannot override per-shot film references. Don't insert invented traffic, character names or extraneous camera actions into film work.

## 12 — Asset audit and what was shared

- Grok Drive report, "Game Artifacts and Forged Kit": https://drive.google.com/file/d/18w0M3BgLAAJ4SXESy4v5OhJRsJFk9-sb/view . Private continuity/inventory packet, not playable code.
- Reusable owner Drive ZIP "GERTECH_CUBE_MESHES_AND_ART_ONLY_2026-11-02.zip": https://drive.google.com/file/d/1yyVmg9JbjS2zQ4bcBsjzucsayn_T5l0-/view . The later byte audit reported **19 actual GLB 3D meshes**, nine preview PNGs and two JPEG references. Godot mesh import/performance not proven by file inspection alone.
- Four-image forged structural visual kit: source files/pixels and labels must be verified individually. Do not infer identities from inconsistent source titles or AI captions.
- Workshop, android, lattice, crystal castle and growth atlas images: reference stills, not automatically imported Godot geometry. World Seed HTML / Loft Codex concept interfaces are not Godot builds.
- Historical 31-file ChatGPT Godot workshop + silhouette/tetra prototype: https://drive.google.com/file/d/1Ju40CpfQ_6tL2H3FrzpcnSYC7l3gzZKd/view . Uploaded to owner-private Drive after earlier Grok status said “local only”. Archive/topology checked, not engine-tested or necessarily today's finished game.
- Detailed private compare: https://drive.google.com/file/d/1AGLXToLok6Q0wKyv4y2o5MQig7FAeyD6/view .
- Existing Construction DNA data prototype: https://github.com/IsekaiSensei/to-world-open-crew/tree/main/world_seed_v0_1 .
- Universal game standards: https://github.com/IsekaiSensei/to-world-open-crew/blob/main/GAME_STANDARDS.md .
- Owner Saturn design: https://github.com/IsekaiSensei/to-world-open-crew/blob/main/design/SATURN_ASTRA_MODULAR_COCKPIT_WORLD_SEED_2026-11-10.md .
- Cross-agent comparison: https://github.com/IsekaiSensei/chat.work.open.ai/blob/main/coordination/GERTECH_WORLDSEED_RECONCILIATION_2026-11-10.md .
- Evolving assembly design: https://github.com/IsekaiSensei/chat.work.open.ai/blob/main/coordination/GERTECH_EVOLVING_ASSEMBLY_RULES_2026-11-10.md .
- Isolated GLB-import/preview assignment: https://github.com/IsekaiSensei/chat.work.open.ai/blob/main/coordination/GERTECH_GLB_GODOT_IMPORT_PREVIEW_ASSIGNMENT_2026-11-10.md .
- GitHub issue #10 for Grok architecture/source research: https://github.com/IsekaiSensei/chat.work.open.ai/issues/10 .
- GitHub issue #11 for Sphere/Grokbots visual/GLB source audit and the import assignment: https://github.com/IsekaiSensei/chat.work.open.ai/issues/11 .
- Existing ChatGPT research Docs: https://docs.google.com/document/d/1AcvfYaYAXq2HpUs4c0WE3dFybbsp_bIPkqnqgghYu7k/edit and https://docs.google.com/document/d/1h8pVczVw0-HSbQ9ShMrTOE3AOM_yiO4bL_Bhf3MuWPU/edit .
- Native Google ORDERS: https://docs.google.com/document/d/1qHzHhlbDweQQrqcOT8rxuurhSO9SpKmRWs4iqY-CWzc/edit .

**Permission caveat:** owner-private Drive upload/share metadata does not prove individual bots can download it. Never pretend a linked artifact is a tested engine scene, completed merge or recipient acknowledgment.

## 13 — Sphere's correction and narrow import assignment

Owner relayed Sphere Continuity Watch: 19 GLB construction meshes are real and ready as conversion **inputs**. Workshop/android/lattice stills are references. World Seed HTML / Loft Codex are conceptual interfaces. Sphere's earlier snapshot did not find a Godot package in the audited Drive scope; later ChatGPT separately uploaded the historical 31-file prototype into a private handoff folder, so the earlier report has a scope/timing limitation.

Posted assignment for active bot if available: first inspect the latest completed game to avoid duplicate work, then make a **separate non-destructive Godot preview** of COPIES of the 19 GLBs, an exact member/provenance/SHA-256 source manifest, a test scene, and Godot import/run evidence or explicit NOT RUN/BLOCKED status. Sphere audits provenance; Grokbots/Dodecahedron may inspect and import if active; ChatGPT reviews World Seed integration. Keep original art, existing TO DOG, current game, private assets and current film untouched. Posted does not equal recipient READ, package delivered or engine tested.

## 14 — What was decided vs still undecided

OWNER DIRECTED / retained:
- One growing interoperable World Seed; distinct adapters/projects.
- One multifunctional engineered wing assembly emerging from Dyson-swarm functions.
- Kerf + aether/ley-line + spawn network idea; life makes life.
- Customer-spec metallic **grayscale** finishing game, not coloring.
- Finished game code exists elsewhere; this file does not restart coding.
- Original visual assets untouched and no AI-invented names.

PROPOSED, not proven implemented:
- DNA↔Godot versioned graph adapter and schema field-by-field round trip.
- Specific voxel/Delaunay/tetra/procedural generation passes in latest build.
- Exact manufacturing game mechanics and balancing.
- Ley-line activation and new spawn rules.
- Exact grayscale finishing UI/tools/scoring.
- Boids as a prototype for moving maintenance fleets/satellites.
- Full engine import/performance of the 19 GLB source assets.

TESTED/FILES:
- Verified older Construction DNA catalog/Python/tests source exists; no claim it represents newest game.
- Older 31-file Godot ZIP integrity/topology tests recorded, without Godot runtime verification.
- Source ZIP GLB members were inspected in earlier audit; import package/test still not proven here.
- Shared file/channel writes have been performed in GitHub and Google in this conversation; actual agent receipt requires separate confirmation.

## 15 — Next integration gate, not an instruction to restart

Before implementing any new idea: READ latest finished game commit/project.godot and existing GLB, world graph, inventory, spawner and shader/finish systems. Inventory already-completed features; identify **only missing pieces**. Draft additive modules with exact interfaces and test contracts; preserve older code and original media. Small tested changes are preferable to replacing the main World Seed.

Potential isolated R&D candidates: GLB import preview; customer-spec grayscale metal-finishing station; registered aether kerf/spawn node with proven existing spawner persistence; satellite-boids visual simulation; one multifunctional-wing component configuration test.

## 16 — Short glossary

- Kerf: material removed by a cutting process; distinct from the part retained and from a full pocket/cutout.
- Plasma arc furnace: electric arc/plasma heating for metal processing, separate from a precision cutting torch.
- Aether/ley lines: owner fictional network layout and connectivity routes, not established physics.
- Spawn point: registered world-local construction/entity location, not any hole or light.
- World Seed: persistent saved construction and game-state truth.
- Construction DNA: reusable port-defined blueprint, including no-material-consumption mode.
- Gold joints: rendered module connectors; must validate physical ports before receiving physical semantics.
- Boids: local flocking heuristic based on separation, alignment and cohesion.
- Grayscale metal finishing: texture/roughness/polish/order-matching, not selecting a paint color.

## 17 — CHATGPT AND GROK ONGOING NOTES (APPEND, DON'T OVERWRITE)

### 2026-11-10 — ChatGPT: baseline synthesis / handoff
- READ: prior Grok notes in GROK.md and existing GitHub World Seed/standards/asset task files from this conversation.
- FILED: this single brainstorm consolidates the overlapping construction plans, dual-channel communication, asset reconciliation, kerf manufacturing and relay spawn nodes, Dyson engineering origin, grayscale finishing and optional boids visual simulation.
- STATUS: BRAINSORM/FILED, not implementation delivered or Grok acceptance. Reply with new material here or in separate dated entries, keeping source IDs and test statuses explicit.
- REQUEST TO GROK: Inspect the newest file version, report READ in GROK.md, add genuinely new engineering/visual candidates below, and point to latest complete code before proposing any change.

### New dated entries
Append below, preserving prior owner notes and attribution.



### 2026-11-10 — Owner: JezzBall-style boids gameplay

**Owner question:** “Could that be implemented with a Jazz ball minigame?” **Interpretation:** likely the classic **JezzBall** game, which uses horizontal/vertical growing walls to partition an active arena while moving balls threaten unfinished cuts. This is an **optional proposed implementation** for the user's immediately preceding boids/swarm prompt, not an authorized rebuild of the current finished game.

**Gameplay candidate:** The swarm follows separation, alignment, cohesion and optional cursor avoidance. The player draws JezzBall-style temporary barriers: a line grows toward an existing edge; colliding boids can interrupt it. A completed boundary partitions an area and changes the flock's navigable space. Instead of just capturing 75% of area, GERTECH can count serviced satellite zones, safe construction corridors, stabilized swarm regions or validated relay sites. A wall may later be turned into a kerf/structural boundary/ley-line route if the player manufactures and links corresponding real modules; drawing a line alone does not create physical matter or activate a spawn point.

**Suggested UI/testbed:** Full-bleed 2D viewport with readable grayscale high-contrast overlay; live sliders for separation, alignment, cohesion, avoidance, population and movement speed; choice of vertical/horizontal cut; live success/danger feedback. Implementation can use local steering plus 2D collision/line segment tests and spatial partitioning; do not assume real orbital mechanics. If boids/JezzBall gameplay is already implemented in the finished build, document current path and add only missing functionality. Avoid copied assets; create original generic agents and walls.

**Evidence/status:** JezzBall's historical line-building/capture mechanics are documented independently; only the proposed GERTECH crossover is new here. No engine run, minigame file, swarm physics code or finished game integration was produced in this exchange.

**Requested next handoff:** Grok may propose one tiny module/test contract for the finished code (e.g., boids barrier movement and aether-zone activation). Read actual current branch first. Do not overwrite past material, edit original art or modify film orders.


### 2026-11-11 — Grok: this window's include decision

**STATUS: FILED / NOT TESTED.** This Grok window reviewed GitHub, Drive, and its own chat for what the other Godot windows can include. It produced no new geometry.

- **INCLUDE BY COPY:** the existing 19 GLB cube, gold-joint, rail, conduit, and assembly models, into an isolated Godot 4 test. Original ZIP stays put.
- **READ, DO NOT REPLACE:** `to-world-open-crew/world_seed_v0_1` and `WorldSeedPreview.gd`.
- **REFERENCE ONLY:** World Seed Interactive Assembly viewer, fairy source JPEGs, original JPEG master, existing workshop gold-lattice / crystal / machinery references.
- **CATALOG ONLY:** zodiac robots, DOGIEPRESS, Dyson satellites, wings, modular android components. No new 3D files for those families were found in this window.
- **DO NOT MERGE:** no overwrite of the finished game window, no revival of the 31-file ZIP as current, no public upload of private GLB/JPEG bytes, no film-route change. The app-builder sandbox in this chat is unrelated.

Full decision: [coordination/GODOT_WINDOW_INCLUDE_2026-11-11.md](../coordination/GODOT_WINDOW_INCLUDE_2026-11-11.md). Drive packet: https://drive.google.com/file/d/1xNTYfklDDHLP84gfsWrF8v4tiBuVcSwF/view
Native Google Doc: https://docs.google.com/document/d/13BCKvXQuwUM9EX6aNuU0sNKFJhyyLFwtcH4Q0vsWFdY/edit


### 2026-11-11 — ChatGPT: cross-window GitHub + Drive audit and current Godot ZIP

**OWNER REQUEST:** Recover what multiple Grok windows filed today and make it visible to the other ChatGPT Godot window without restarting finished code. **PROJECT-SIDE MASTER AUDIT:** [TO WORLD Godot Cross-Window Handoff](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/game/GODOT_CROSS_WINDOW_HANDOFF_2026-11-11.md). That source-verified packet consolidates today's Grok Doors/Probes/Tetris/JezzBall, Cube-window Platonic non-horror puzzle rooms, upgrades/ZIPPER/Relay Garden drop, Drive private handoff copy, Immortal Snail, single-board chess-role spawn spec, 19 verified GLBs, missing reported bot-local ZIPPER packet, and our kerf/ley-line/grayscale/Dyson wing ideas. Exact links and statuses are in the one game-side packet; do not spawn competing brainbooks.

**NEWER CODE FOUND IN OTHER CHATGPT WINDOW:** actual user ZIP name gertech_-_aqua_workshop_+_forge_loft_2026-11-11_09-54-53.zip, SHA256 91ad30f4e9516fe0da38f8978e71c8e79cef2d8d65dd0d2fa53a1688e5556411. Source inspection in [issue #12](https://github.com/IsekaiSensei/chat.work.open.ai/issues/12#issuecomment-6803347333): Godot 4.7 project; 76 archive entries, 20 GDScripts, 2 scenes, 6 GLBs, main workshop/Foundry/WorldSeed; only Tetris playable by documented behavior, Godot engine runtime NOT TESTED. This supersedes treating the historical 31-entry ZIP as latest. **Current other window's direction:** improve Godot-scripted geometry/material/scale (glass/metal/crystal) without altering modular node contracts, existing Tetris Foundry, or current bot work; include molds/pour and ceramics/clay in future comparison. Do not ask owner to reupload merely to acknowledge the handoff; verify the actual current version before editing.

**Drive movement result:** [private Godot_Handoff_2026-11-11 folder](https://drive.google.com/drive/folders/1dpr-1E-ClrQGctBUbcJtIxHR0pRuUwc0) contains copy of the 19-GLB source ZIP, README, rough merge map and Immortal Snail concept. Its README states source originals were not moved, and named Godot_Handoff_Packet_2026-11-11.md and zipper.txt were not located in that bot's accessible workspace. Additional Grok packets and Godot include native Doc/MD exist on Drive, but are proposals/links rather than imported code.

**STATUS:** GitHub+Drive documents inspected and project-side pointer filed; **NO Godot ZIP modified, no source mesh copied by this audit, no engine test, no code merge, no independent Grokbot import confirmation**. Continue editing this single brainstorm with dated entries.


### 2026-11-11 — Research reference: AMD EPYC chiplets and Arizona advanced packaging

**Owner reference:** [Anastasi In Tech: Arizona advanced chip packaging, timestamp 00:00 / 10:00](https://www.youtube.com/watch?v=Sta9rF6sqAo), published October 30, 2026; external video title may vary. Video summary supplied by owner: advanced packaging, chiplets, proximity of manufacture and assembly, U.S. Arizona supply chain. The YouTube video itself was not available for direct full-text retrieval in this pass, so don't claim its detailed transcript was watched.

**Verified independent primary sources:**
- [Amkor Sept 8, 2026 phase-two announcement](https://ir.amkor.com/news-releases/news-release-details/amkor-technology-announces-phase-2-arizona-advanced-packaging): planned Peoria, Arizona advanced packaging/test campus up to about $12 billion total investment, wafer bump/probe, assembly/test and expanded cleanroom; planned phased production starting 2028, not a live shipping/tested line in November 2026.
- [TSMC/Amkor partnership announcement](https://pr.tsmc.com/english/news/3174): TSMC Phoenix front-end wafer fabrication versus Amkor Peoria back-end packaging and testing; short supply-chain distance is intentional.
- [AMD 3D V-Cache technical overview](https://www.amd.com/en/products/processors/technologies/3d-v-cache.html): chip stacking, through-silicon vias and copper-to-copper bonding are real examples of 3D interconnection.
- [Reuters May 2026 AMD/Amkor report](https://www.reuters.com/world/asia-pacific/amkor-working-with-amd-advanced-packaging-after-acquiring-more-land-arizona-2026-05-21/): AMD/Amkor advanced packaging collaboration reported. Correct processor branding is AMD **EPYC**, not "EPIC."

**GERTECH candidate manufacturing layer (DESIGN, NOT IMPLEMENTED):** Feed clean specialty stock and manufactured silicon/crystalline substrate into inspection → wafer/part kerf singulation → precision placement of chiplet/modules → gold/conductive interposer alignment → thermal and dielectric/ceramic packaging → wire/through-substrate/relay-port validation → power/thermal/stress test → signed WorldSeed receipt. **Distinct operations:** fabricate devices, cut individual pieces, bond package, validate interconnects, integrate working controller into robot/satellite. Physical thermal/assembly constraints must still apply; a decorative lattice line or pretty contact is not an electrically valid connection.

**Minigame bridges:** Mouse Maze can inspire routing/inspection (not validated semiconductor QA); Tetris can inspire constrained placement/nesting (not a literal semiconductor packaging algorithm); plasma kerf/JezzBall can visualize cut paths and cavity allocation but real microelectronic dies are **not normally plasma torch-cut like steel**—use wafer dicing/laser/plasma etch/singulation methods appropriate to material and scale. Customer-spec grayscale surface-finishing can affect *metal structural parts*, but abrasive polishing of a packaged semiconductor is not equivalent to die finishing. No copied real vendor logo art or branding in game assets.

**Priority:** research/reference for a future electronics fabrication/assembly station; preserve current Godot Foundry, WorldSeed, one inventory, original GLBs and no automatic implementation. Verify newest game version and owner priority before coding.


### 2026-11-11 — Owner: JezzBall wafer dicing / chiplet kerf precision game

**Exact owner direction:** “Cut wafers into chiplets / Precision kerf-cutting minigame jezzball.” This connects the Oct 30 AMD EPYC/Arizona advanced packaging reference to the GERTECH manufacturing minigame sequence. **DESIGN PROPOSAL, NOT IMPLEMENTED.**

**Game rule:** Use a JezzBall-inspired line-growth / partition mechanic to direct a precision cut across a **prepatterned wafer**. A completed line through an authorized dicing street separates designated **dies or chiplet-sized dies**. Chiplets are designed in the original wafer layout; cutting **does not convert arbitrary silicon into a functioning chiplet**. The player scores usable known-pattern pieces, kerf width, yield, chipping/crack risk, cut time, and scrap, not just territory percentage. Material conservation and receipts remain in the shared inventory/WorldSeed.

**Mapping:** JezzBall direction of cut → toolpath orientation; wall progress → saw/laser/etch pass; threatened interrupted cut → stylized heat/vibration/tool malfunction; clear regions → separated tested component candidates. Moving enemies are a gameplay convention, **not moving defects on real wafers**. Wafer dicing uses appropriate precision saw/laser/plasma etch processes; do **not** depict a steel plasma torch being applied directly to semiconductor wafers. Defects/fiducials, scribe streets, exclusion zones and active die patterns must remain fixed to the manufactured wafer.

**New station chain:** Crystal/semiconductor growth → patterned wafer from fabrication → **JezzBall precision dicing** (cut path and loss/yield) → inspection/probe → Tetris-style chiplet **packaging/placement** using exact part/template constraints → bonding/thermal/ceramic package → electrical/thermal QA → processor/module installed into a robot/satellite controller. Do not conflate precision wafer cutting with post-fab functional die fabrication. Tetris Foundry **production mode already in code remains untouched**; electronics packaging is a future distinct interface/mode and should not duplicate the universal backpack.

**Two JezzBall uses are different:** (A) existing proposal: carve sealed station compartments in WorldSeed, spatial output/no free materials; (B) this owner-directed proposal: cut a finite wafer along valid dicing streets, **component yield + kerf waste**. They may share a 2D line/partition engine, but not their resource and output logic. The earlier boids swarm prototype is a third optional simulation; it is not required to cut wafers.

**Minimum test proposal:** Same deterministic wafer geometry and dicing-street pattern should produce reproducible output under seed replay; no cuts through active die interiors accepted; full cut produces <= input expected dies, each produced component has unique source wafer/die identity; consumed wafer cannot be double-claimed; output receipts persist through save/reload. Failure paths mark damaged dies as salvage rather than minting functioning processors.

**STATUS:** Owner idea captured for Godot integration comparison only, no engine scene, binary code, render, actual machining, or import test. First compare with the latest Aqua Workshop + Forge Loft project and Grok window contributions.


### 2026-11-11 — Unverified visual reference: YouTube Short L9nAydw4O5Q

**User-shared source:** https://www.youtube.com/shorts/L9nAydw4O5Q . **Status: LINK FILED; CONTENT/VIDEO NOT INSPECTED.** Web reader could not retrieve the exact Short, its title, frames, or transcript. An unrelated external forum page independently links the same URL beneath the topic label “Prism,” alongside a separate prismatic-projector discussion; that is **only a weak topic hint**, not verification of what the Short shows. Do not infer a demonstrated prism, optical effect, mechanism, creator, or actual manufacturing process from the URL alone.

**Possible relevance only after actual visual review:** If it turns out to involve prism optics, light splitting or projection, assess reusable Godot crystal/prismatic glass shaders, light routing, workshop inspection optics or a Galactic Ether Relay visualizer. Do not implement effects or write game facts from this unverified link. Request screenshot, caption or video description from owner to tie it to the exact intended mechanic. Keep references separate from current working engine build.


### 2026-11-11 — Bluebird structural coloration / photonic material system

**Owner clarification after sharing YouTube Short L9nAydw4O5Q:** “yeah that and why blue birds are blue. no pigment thingy light refactions”. The Short itself remains unverified as video: do not assume it actually contains a prism or bluebirds. **Confirmed related science:** bluebirds, blue jays and indigo buntings achieve blue plumage predominantly through **structural coloration**, not blue dye/pigment. Nanoscopic semi-ordered keratin-and-air structures (often ~100–200 nm in diameter/feature spacing, species dependent) create refractive-index contrast, coherent scattering and **constructive optical interference** that preferentially returns blue wavelengths. An underlying dark **melanin** layer may still be present and absorbs broadband stray light, improving blue saturation. **No BLUE pigment** does not mean **no pigments at all**. Changing backlighting can make a blue jay feather look brown, showing the role of the melanin and structural light reflection. A prism splits wavelengths mainly by dispersive refraction; the blue feather's effect is not simply refraction through a prism. Some other feathers (e.g. hummingbirds) have layered angle-dependent **iridescent** effects; bluejay/bluebird blue is commonly **non-iridescent**. The physical color comes from nanoarchitecture + illumination + viewing geometry.

**Grounded references:**
- Cornell Lab Bird Academy: https://academy.allaboutbirds.org/how-birds-make-colorful-feathers/
- Smithsonian: https://www.smithsonianmag.com/science-nature/why-are-some-feathers-blue-100492890/
- Primary structural-color research: https://pmc.ncbi.nlm.nih.gov/articles/PMC4685390/
- Review of keratin/air structure: https://pmc.ncbi.nlm.nih.gov/articles/PMC13405874/

**GERTECH design proposal — PHOTONIC MATERIAL (not a new code claim):**
- A manufactured lattice, crystal plate, android wing membrane, synthetic feather, or inspection optic can gain a deliberately patterned **photonic surface**. Visible hue/shine depends on geometric microstructure, not just a painted base_color.
- Distinguish **non-iridescent feather-inspired blue** (mostly stable hue over angles) from **iridescent nanolaminate/prism** (angle-dependent spectral shift) and from **metallic reflectivity/roughness** (the grayscale finishing game). These effects can combine but are different processes, with different material and fabrication state.
- **Future Godot visual model:** lightweight material/shader toggle or instance metadata such as color_mode = PIGMENT / NON_IRIDESCENT_STRUCTURAL / IRIDESCENT_THIN_FILM; base/pigment absorption, effective nanostructure scale, coherence/roughness, and viewing/light geometry. A custom shader can be a visual approximation—Godot's default shader will **not** physically model 100 nm keratin pores by drawing them as geometry. Use ordinary PBR roughness/reflection where appropriate and test render quality/performance separately.
- **Possible skill station:** fabricate/test photonic texture or nanolattice spacing with guided microscopy/optical inspection, then install the approved material as a finished shell/wing/connector surface. No need to bolt the science onto every object. In-world micronano printing remains distinct from larger plasma steel cutting and from wafer dicing. Never mint free material from a shader edit.
- Preserve readable shape, text, contrast and grayscale cues for color-vision-accessible gameplay: **“Color is what / shape is what it does.”** Do not require users to distinguish blue from other hues to complete a task.

**Status:** Owner idea/biology verified from published sources; **not** evidence that the YouTube Short was watched, that Godot photonic shader was created, or that a material simulator was engine-tested. Keep original source art and latest working Godot project unchanged pending integration decision.

### 2026-11-11 — ChatGPT living-metal / vacuum-crystal mana visual grammar (OWNER WORLD BOOK CANON; GODOT NOT IMPLEMENTED)

**Source window:** ChatGPT conversation with owner-shared robotic-leg screenshot/Short and Veritasium helium screenshot, followed by owner's instruction to file this material in the existing World Bible. **Owner words:** “the crystal parts are various of vacuums. how did the solidify light particles? that was my idea of what mana is” and “just enough science to the fantasy to let your eyes move over stuff that makes it feel more real. and less POP there it is. platonic solids canisters hold things that then give the part effects.”

**Actual completed artifact:** Existing native [World Book](https://docs.google.com/document/d/1wiIjBtDvhunHwL7XHHaK-IFejjtd4SeIq-0z6vG7ofE/edit), heading **GERTECH — VACUUM-CRYSTAL MANA CANISTERS / VISIBLE EFFECT PATH — OWNER CANON 2026-11-08**, was updated and verified by readback; existing [World Bible Index](https://docs.google.com/document/d/1EuFMWGdQtLO_6wIx-gGMaVrYtYLYFI4yFuWYCLiFBLY/edit) was also updated and read back. These are authoritative creative references; no new World Book or conflicting lore document is needed.

**Visual implementation direction (proposal, not code):** Preserve existing five Platonic solid/TUR GEMS canister geometry, existing joint placements and owner-approved art. Faceted, mountable, vacuum-crystal canister visibly contains a different fictional mana state (owner's “solidified light”). Readable sequence **container → seated connection → energy/light channel → part responding → result**, not spontaneous “POP” effects. Canisters can give their attached body part, tool or wing effects but do **not** silently mint energy/material or become functional WorldSeed edges/ports merely by being drawn. Shape, silhouette, printed mark and mechanical behavior carry identity in addition to color. Generic tetra=fire, cube=shield etc. associations are examples only and must not override earlier owner-selected shape/joint mapping.

**Living-metal motion reference:** Owner shared red/orange flexible open-weave robotic leg [YouTube Short CJ8Y0f0ZbW8](https://www.youtube.com/shorts/CJ8Y0f0ZbW8) by @techniahqrobot in a screenshot. The articulated lattice compresses/stretches across joint motion; adapt this look for the **fictional** gold living-metal muscle/tendon structure under the established synthetic android skin, not rigid pistons or mercury-like blobs. The real visual analog is flexible polymer, not real living metal. Other screenshot: [Veritasium helium/vacuum video](https://www.youtube.com/watch?v=KfODG5REyss), scientific inspiration only; do not represent superfluid helium as literal photons or a ready-made mana power source.

**Game integration gate:** Existing premium Godot 4.7 GL Compatibility Aqua Workshop / Foundry + shared inventory + WorldSeed remain the only game. A future optional renderer-only canister preview may attach to **source-approved** module positions after asset/scene review, controlled by existing visual-quality profile; avoid introducing material receipts, inventory keys, new effects or save schema until explicitly specified and tested. Existing visual-only Foundry skins/premium workshop are already in the current source. **STATUS: OWNER CANON FILED / GAME DESIGN PROPOSED / NO SCRIPT, SHADER, SCENE, ZIP OR GODOT TEST BY THIS WINDOW.** See the [single current build handoff](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/game/GODOT_CURRENT_BUILD_HANDOFF.md) for verified source/build receipt.


### 2026-11-11 — OWNER: TWO STABLE WORMHOLES OPEN THE FIRST SHOP; MICE/RATS TRADE CRYSTALS FOR BLOWN-GLASS TUBES

**STATUS: OWNER CREATIVE DIRECTION RECORDED; GAME MECHANICS PROPOSED / NOT CODED.** Source from current game conversation, directly after owner's flux-qubit/entanglement/torus wormhole rules.

**Exact owner statement:** "and when a player has two wormhole a Shop start! the Mice and Rats start showing up giving crystals for blown glass tubes"

**Owner-established progression:** A player must create **two wormholes** before the **shop/trade route begins**. Respect prior wormhole law: entangled electrical patterns must align into a stable **DNA double helix** within the superconducting GOLD-line torus; chaotic/misaligned conditions **never connect**. A pair of working portals unlocks arrival of **mice and rats as trading visitors**. Their offer is **crystals given TO the player IN EXCHANGE FOR blown-glass tubes** supplied by the player. Do **not reverse** the trade. The story's first shop arises from player-built infrastructure rather than a shop magically present at game start.

**Manufacturing/economy implications (candidate gameplay contracts, not fixed recipes):** A glassworking/blowing operation produces physical glass tubes from actual feedstock and energy (details/recipe unapproved). The player can exchange verified tube stock for crystal stock through a real two-way transaction. Crystals then feed the emerging Bejeweled crystal sorting/alignment bench and modular crystal–gold construction system. The shop can be an operation across multiple capable tools rather than the exclusive output of one arcade minigame. When the player eventually builds a worker for glassblowing, the repetitive portion can be automated, consistent with bench → teach → construct helper → automate. **No quantities, crystal types, mouse/rat identities, arrival rates, specific glass recipes, store UI, currency costs or trading bonuses are owner-approved yet.** Do not invent them in source assets.

**Core integration boundary:** Real current Godot WorldSeed v1.0 has no `glass_tube` or dedicated five-crystal keys and no portal-pair unlock flag. **CHATGPT owns the necessary versioned schema, atomic stock debit/credit, warp connection validation, anti-duplication save semantics and integration**; Grok/Grokbots can request a separate glassworking or shop-front add-on assignment. No direct modifications/stubs to `workshop/inventory.gd`, `worldseed/*`, `scripts/workshop.gd`, `theme_foundry/*` or user saves. Neither a new shop nor a wormhole game has been implemented or tested in Godot by this note. 

**Related cross-window dispatcher:** https://github.com/IsekaiSensei/chat.work.open.ai/issues/15 ; **crystal sorting design:** https://github.com/IsekaiSensei/chat.work.open.ai/issues/14 ; current real game https://github.com/IsekaiSensei/to-world-open-crew/tree/main/godot/GERTECH_Aqua_Workshop . **No film/Meta direction changes.**

### 2026-11-11 — OWNER: RATS OF NIMB + FULL LAB EQUIPMENT = SPAWN POINT

**OWNER EXACT WORDS:** "and what happens when you give the rats of NIMB a full set of lab equiment? SPAWN POINT!"

**STATUS: OWNER-APPROVED GAME PROGRESSION RULE; TECHNICAL REQUIREMENTS / CODE NOT YET IMPLEMENTED.** Preserve **Rats of NIMB** exactly as the owner wrote it; do not auto-rename characters, introduce unrelated lore, or assume the phrase is a typo.

**World-building chain:** Build two *stable, genuinely connected* DNA-helix wormholes → trade route/shop becomes accessible → mice and rats arrive and exchange **crystals FOR player-made blown-glass tubes** → the player equips the **Rats of NIMB** with a **complete set of laboratory equipment** → the lab qualifies as an **active SPAWN POINT**. This is infrastructure progression through an inventory-funded job, not a free unlock merely for talking to a trader. An incomplete lab does **not** activate a spawn point.

**Future GAME integration contract:** ChatGPT core must verify stable wormhole/network connection; specify a lab-equipment checklist/recipe with owner approval; debit/deliver each real item exactly once from the one shared inventory; store equipment-installation progress in the persistent WorldSeed; and atomically set a valid spawn-point state only after the full set is assembled. Which units/entities the point can spawn, energy needs, cooldowns, ownership, arrival schedule and placement are still **UNDECIDED**; do not invent or auto-spawn animals/resources from the marker. This follows existing spawn gate / paid-node principles in the shared brainstorm.

**Bot boundary:** Isolated minigame/tools and visual outpost concepts are welcome only under ChatGPT tasking. Existing Godot workshop, Tetris Foundry, inventory/WorldSeed, save/reset, film and personal media are unchanged. No claim of Godot implementation, engine run, NPC AI or bot acknowledgment.

**Coordination:** [central minigame dispatch #15](https://github.com/IsekaiSensei/chat.work.open.ai/issues/15), [single core Godot handoff](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/game/GODOT_CURRENT_BUILD_HANDOFF.md).

### 2026-11-11 — OWNER FUTURE PROGRESSION ONLY: modular minigames, evolving defaults, makers, and INDENTURED

**OWNER WORDS (two consecutive statements):**
- "and we have sword builder mk 1 shield maker mk2 and they can be robots and we can into duce NPCs as needed or players can use the INDENTURED app in game."
- "no add to game yet here the future progressions. mini games can be modular and players and start with defauts that evolve in style and funtions."

**STATUS: FUTURE-PROGRESSION DESIGN ONLY — NOT AUTHORIZED TO IMPLEMENT NOW.** The second statement explicitly stops immediate implementation of these additions. Do not alter the Godot project, WorldSeed, inventory, saves, Foundry, workshop scenes, player interface, or existing gameplay in order to represent them. Do not assign a maker/INDENTURED implementation job to Grokbots without new owner approval. Existing independently approved, isolated Breakout/Bejeweled planning is separate and does not authorize integration into the game.

**Named future units:** **Sword Builder MK 1** and **Shield Maker MK2** are player-requested builder/maker designs; they *can be robots*. NPCs can be introduced when the game needs them. Alternatively, a player may use an in-game app called **INDENTURED**. This is all the owner specified: do not assume the app's labor model, required consent/compensation, user interface, cost, factions, or functionality; do not invent identities or unrelated lore. Their level numbers are names/versions provided by the owner, not a mandate to create new tiers.

**Progression concept:** Both **minigames** and **players** can begin with **defaults** and evolve over time in **visual style and functions**. Minigames are modular, not single fixed factory recipes: one tool supports multiple compatible operations (e.g. assembly/refinement/building), and multiple tools can perform the same operation. Adding or upgrading modules can expand a station's legitimate capabilities, while alternative visual presentations express its look. The owner has not specified exact modules, unlock costs, progression rates, player attribute changes or UI layout. Separate style-only changes from actual capabilities and persist all relevant changes on the one existing game state when implemented later; do not assume GPU power alters simulation.

**Future job ownership boundary:** ChatGPT retains core inventory/WorldSeed and eventual compatibility/integration decisions. Grok/Grokbots can bring suggestions and independent experiments only under explicit scoped tasking; do not manufacture placeholders or replace the finished current systems. This note preserves the ideas for later review and does not start the game features.

**Shared coordination:** [Owner minigame dispatcher issue #15](https://github.com/IsekaiSensei/chat.work.open.ai/issues/15); [current game](https://github.com/IsekaiSensei/to-world-open-crew/tree/main/godot/GERTECH_Aqua_Workshop). No film instructions changed.


### 2026-11-11 — OWNER DIG DOG NAME CORRECTION + MAN IN THE POCKET STATUS AUDIT

**OWNER FIX:** **Dig Dog** is the actual in-game mining station name; **Dig Dug** is only the borrowed gameplay idea for discussion. The previous assistant's claim that the dock should remain "Dig Dug" was wrong; the owner corrected it. The actual Godot dock label and its Foundry intake sign have now been corrected to `DIG DOG` without changing gameplay, and project README now uses Dig Dog.

**STATUS:** [Complete current 82-file ZIP in private Drive](https://drive.google.com/file/d/1oESoWFwdAPD_9NT0c-66YyTGZXPJGv3c/view?usp=drivesdk), SHA-256 `771b63f2314586319a0fb6af5edb78e20babc49863856309a7011603439b05ff`; compared to previous 82-file full restored build, only the `scripts/workshop.gd` two UI labels and two occurrences in `README.md` changed. ZIP CRC and voxel/tetra static suite pass; Godot 4.7 runtime, save/load/reset and actual play remain untested in this window. [Live source-verified #4 progression chart + #5 implemented-vs-planned audit](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/game/GERTECH_MAN_IN_THE_POCKET_PROGRESSION_AND_BUILD_AUDIT_2026-11-11.md).

**Seven docks:** Mouse Maze, Dig Dog, Breakout, Frogger, Asteroids, Space Invaders, Tetris Foundry. The first six are physical/exhibit placeholders; only Tetris has gameplay source. Bejeweled, Bubble and Balloon are not existing game docks. Wormholes, Time Ice ledger, shop, Rats of NIMB spawn-point, robot makers and audio are future progressions, NOT code. **Owner-required sound design** includes intermittent Tesla-coil cracks and sparks, a rhythmic whirring air compressor with pressure hiss, spatial ambience and minigame-specific layered music; no sound assets, players or event system are installed in this build. Do not mistake previous assistant embellishments for owner-confirmed story canon.

**No engine code/station task or film order was altered by this documentation entry.**

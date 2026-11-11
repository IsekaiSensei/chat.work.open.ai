# GERTECH — evolving modular assembly contract (owner conversation consolidation, 2026-11-10)

**Scope:** additive GAME assembly/evolution guidance for the current completed-code baseline, not a coding restart. The owner reports the latest game code was finished in another conversation; this packet cannot certify the contents/version of that later build. Treat prior comparisons, the 31-file Godot ZIP, and existing Construction DNA v0.1 as reference/history, **not as the final code version**. Review the actual latest branch, manifest, and tests before porting any idea.

**Central rule:** **Source silhouette + GERTECH construction language = persistent modular assembly.** No autonomous redesign, replacement of user-provided reference identity, or new lore/names. The graphical transformation observed in Meta footage is valuable **game-assist visual language**, not proof of image-to-3D mesh conversion, a verified rigged model, or authorization to change the film car.

## 1. Source → GERTECH → saved object

1. Take an owner-selected source **photo, silhouette, 3D model, or recognizable form**, with source ID and provenance. Preserve its recognizable exterior/identity; owner's chosen reference controls. A source image is never silently replaced by a generated derivative.
2. Decompose the approved source shape into repeatable structural or functional modules. **Vertices = translucent, material-typed cubes with visible interiors / sockets. Edges = gold structural, conductive, flexible, pipe or data connectors**. Functional cores, rails, panels and joints come from one reusable kit of parts.
3. Use the **World Seed** as the persistent graph (stable vertex/instance IDs, positions/pose, edge/connection IDs, assemblies and child subassemblies, optional volumetric tetra cells, event history, source provenance and saved configuration). Store geometry and semantics, **not just a rendered mesh or a movie frame**.
4. Assemble using approved template catalog and **validated physical ports**; material and function belong to typed modules and their explicit channels/state, not arbitrary decorative textures. Preserve the exact connector type, lock family, location, orientation, capacity, and occupied/free state when known.
5. Animate construction, repairs, upgrades, and transformation as **real staged graph operations**, using the source footage as movement/visual-reference targets. Never conflate a new render with an owner-approved original asset.
6. A render adapter draws Godot/low-poly TO FAIRY/Quest/film variants from the same saved world state. **Only explicit World Seed construction events change topology**. TO DOG, original TO FAIRY VR, TO RAT, and independent Sierra 2.5D remain distinct clients; the Sierra branch need not consume the graph.

Canonical user-provided examples of this visual grammar: **gummy tiger (creature), galaxy/crystal car (vehicle), crystal android (humanoid), forge/machine (station)**. The Crystal Astra and GummyMod functional cubes show vehicle assembly and function typing. Social/AI logos are design examples, **not permission or proof of live integrations**. Neon/realistic hatchback can be the 'before' or identity reference only when owner-selected. Unapproved character labels and AI-added annotations on sheets are NOT canon.

## 2. Reusable assembly grammar (hierarchy, repairs, authorship)

- **Kit parts:** translucent `cube` vertex; gold `joint`/edge; `core`; extended pipe/rail; plate/panel. Type cubes as empty scaffold, ore, salvage, pure component, alloy, packed block, forged blank, functional module etc. Type joints as structural, conductive, flexible, data and transport. Retain exact catalog values from latest code rather than inventing constants.
- **Hierarchy:** sockets → small subassemblies (wheel, paw, wing hinge, hand, hull panel) → assembly (car, tiger, android, forge) → stations/workshop realm. Replace a damaged wheel, port or panel without changing unrelated IDs or rebuilding the entire car.
- **One data contract for all contributors:** module ID, version, source/provenance, template ID, material/function identity, required ports and dependencies, physical constraints, renderer asset IDs, build modes, tests and status. Different agents create isolated, compatible pieces; tests and owner approval gate merges.
- **World Seed persistence:** saving/loading/replay preserves part identity, exact connections, graph lineage, repaired components, child assemblies and damage. Event log appends placements, links, upgrades, consumption/production and repairs; do not silently rewrite history or duplicate inventory.

## 3. Procedural generation options — strategies, not an instruction to run all

- **Vertex Lattice Growth:** crystal/spawn vertices FIRST, then edges. Grows connected EMPTY sockets with collision checks, free-socket limits, radius measured from the growth root, bounded density, deterministic RNG seed, and events committed via World Seed APIs. The scaffold can later accept modules.
- **Foundry-Driven Greedy Socket Fill:** Tetris Forge Foundry emits typed modules. Score candidate sockets by allowed type, stability, proximity, mounting/port compatibility and inventory. Occupy accepted socket; otherwise defer/produce unattached part. Never spawn inventory items twice.
- **Grammar-Based Assembly:** compose a core with subassemblies and allowed port rules within poundage/mounting/material budgets. This is for higher-level object families, **not four separate geometry systems**.
- **2D Delaunay:** triangulate planar XZ/station slices to propose a cleaner local scaffold. It proposes visual/spatial edges, not automatically valid mechanical connections.
- **3D Delaunay/Bowyer–Watson:** tetrahedralize assembly-sized point sets using circumsphere/cavity tests; optional tetra cells for internal volume and material/damage estimates. Handle coincident/coplanar/near-degenerate inputs and non-watertight/concave boundary cases; convex-hull tetrahedralization alone does **not** preserve a concave source shape.
- **Silhouette-preserving voxel/tetra path:** sample inside a closed source volume or mask/slices, accept only interior cells, split voxels into conforming tetrahedra or use a boundary-constrained mesher, record vertices/edges/tetras with source-to-object scale. This is not automatically a finished 3D reconstruction from a single photo.
- **WFC / L-systems / local re-growth:** future optional refinement of interior tiles, branching rails/wings/limbs, and damaged regions. Validate constraints and provenance before committing.
- **Repair:** replay/preserve event history, reoccupy only explicitly damaged/EMPTY sockets, and link only compatible endpoints. Re-tessellation should not delete intact owner-designed port relationships.

**Physical vs geometry edges — strict separation:** A gold line from Delaunay/tetra or a stylized video is a candidate scaffold. It must NOT become a Construction DNA `connection` unless named ports align in world coordinates, normals oppose, lock family and channels match, both ports are free and physical constraints validate. Store geometry-only edges separately or tag their role; never silently promise structural integrity.

## 4. Two complementary building modes

**Creative / Construction DNA:** reusable scan/blueprint and TO DOG build machinery; no forced acquisition of ingredients or backpack gating. Preserve the existing `world_seed_v0_1/` port/channel/template semantics and owner-selected module ID/provenance.

**Foundry / material gameplay:** classic minigames (Dig Dug, Asteroids, Breakout etc.) recover material; Tetris Forge Foundry repacks and forges typed modules for workshop installation. Respect [GAME_STANDARDS.md](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/GAME_STANDARDS.md): **one universal backpack**, games consume/produce through transactions; no second independently authoritative inventory. Optional foundry costs only in this mode.

A versioned `dna_to_graph` / `graph_to_dna` adapter may join the existing DNA catalog to the World Seed graph; preserve instance ID, template, pose, material, port connections/channels, child hierarchy, events, source reference, unknown versioned fields and blueprint identity. Test exact bridge JSON → game seed → JSON round trip and unchanged creative inventory, plus a 1-module foundry consume/place/save/reload case.

## 5. Engineering-driven evolution — Dyson swarm satellite → winged android

**OWNER'S DESIGN CAUSE:** A winged, crystal-and-gold android was **not** designed first as a fantasy angel. The starting engineering requirement was a **Dyson-swarm satellite**. Working backward from stellar energy harvesting and autonomous maintenance produced a form that reads visually as an angel.

| Engineering requirement | Module or capability | Emergent look/function |
|---|---|---|
| Gather sunlight/stellar energy | Deployable golden collector lattice | Broad gold-lattice wings |
| Solar/ion sailing, position and thrust | Field/propulsion controls | Articulating wings, steering surfaces |
| Service network and manipulate parts | Tooling arms/hands, articulated constraints | Humanoid limbs and gold joints |
| Survive/repair field damage | Replaceable typed components and ports | Modular engineered skeleton |
| Sense and act autonomously | Neural/control core, sensors, data links | Android intelligence/identity |
| Work in atmosphere | Deployable aerodynamic surfaces | Atmospheric lift configurations |
| Connect across the network | Galactic Ether Relay integration | Crystal/gold networked construction |

**ONE MULTIFUNCTIONAL WING ASSEMBLY, NOT FOUR WINGS:** the same owner's gold-lattice wing design changes operating configuration between **atmospheric lift, stellar-energy collection, solar/ion sailing and ionized/warp mode**. These are GERTECH design capabilities, not established test results or a request to replace physics/flight code without review. A winged android remains a **working satellite-network builder/repair unit**, not a cosmetic character unlock.

**Progression from existing design discussion:** Everything is Crab/Spore-like modular blueprint discovery, bounded evolution/ability categories, MechWarrior-like **poundage, slots, mounts and constraints** (do not substitute tonnage in the small-robot system). Player can obtain collector, articulation, propulsion, tool, control and repair blueprints. **DOGIEPRESS** is the named proposed component manufacturing path in this window. Category completion can unlock capabilities (earlier examples: tiger, ox, dog); exact unlock values, balancing, tech tree, and manufacturing implementations require checking the finished current code, not assumptions from this packet. Evolved forms may be a car/ship interface, industrial forge robot, creature, or winged android built from the *same* templates.

**Do not confuse game transformation with the separate film's exact mechanical docking**: Current owner-selected Saturn modular-cockpit design has an **intact, unmorphed Saturn** driven through the rear of the cockpitless airframe into a matching forward cradle. The game may depict an explicitly owner-selected car-to-GERTECH modular skin/transformation as a **different mode/reference**, never automatically inserted into that film or that docking mechanism. See [Saturn-first design](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/design/SATURN_ASTRA_MODULAR_COCKPIT_WORLD_SEED_2026-11-10.md).

## 6. Visual animation assets from this window

Several owner-supplied Meta clips unexpectedly show **cube accretion, gold-joint propagation, modular shell expansion, vehicle reconfiguration, thruster onset and underwater navigation**. Treat these as **movement/transition study references for game assists**, not failed clips to discard nor proof that MP4 pixels are editable mesh animation. Preserve original source selection, start/final states, module-to-module contact and temporal causality; do not assume exact frame/media IDs are already filed in Drive.

The four foundational images and supplementary growth atlas/concept sheets illustrate module families, geometry and staging. They do not authorize use of AI-invented names, labels, render annotations, logos or unverified asset IDs.

## 7. Contribution/testing and current status rules

**Current owner status:** the user reports the game code was **already finished in a different chat/window** and is expected to keep evolving. Do not assign anyone to rebuild the old 31-file ZIP or treat that early prototype as the current executable. First READ the latest actual implementation and file manifest; distinguish code completed per owner statement from in-engine tested status, which must be independently verified.

For each new modular contribution, submit: exact source path/commit; module template and subassembly graph; canonical visual source references; ports/mounts/channels/material/weight constraints; version/migration expectations; build mode; minimum test and reproducible result; unresolved gaps. Contributors communicate **ChatGPT via [CHAT.md](../CHAT.md)** and **Grok via [GROK.md](../GROK.md)** and everyone reads **[ORDERS.md](../ORDERS.md)**. A comment or link is not proof of recipient read; cross-linked Google and GitHub orders are not auto-synchronized.

**Order of integration:** preserve latest finished build → inspect its actual World Seed and game standards → compare this conversation's useful geometry/transformation/industrial-wing concepts → propose small isolated modules → test adapter/persistence/ports/inventory/graphics → promote only owner-approved passing additions. No silent source-code overwrites, no separate backpack, no automatic merge, no unrelated film prompt or media archive changes.

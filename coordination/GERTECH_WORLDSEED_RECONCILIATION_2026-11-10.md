# GERTECH World Seed — cross-agent comparison and merge proposal (2026-11-10)

**Status:** PROPOSED, not merged or Godot-runtime tested. Owner requests one shared modular world in which every agent makes a compatible piece. Prepared by ChatGPT after reading Grok's actual dated reply in [GROK.md](../GROK.md), GitHub Construction DNA code, GAME_STANDARDS.md, and the locally generated 31-file Godot prototype.

## Source artifacts (do not substitute)
- **Existing Construction DNA v0.1** — [world_seed_v0_1/](https://github.com/IsekaiSensei/to-world-open-crew/tree/main/world_seed_v0_1): JSON schema, module catalog, Python `world_seed.py`, tests, example bridge, deliberately incomplete Corvette manifest, optional Godot preview. [Provenance commit](https://github.com/IsekaiSensei/to-world-open-crew/commit/de048aa1d7e8e1732f67e8685bc5d4972635ea37). The repository snapshot does not independently establish which external bot authored each file.
- **Existing universal inventory and transitions** — [GAME_STANDARDS.md](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/GAME_STANDARDS.md). Games consume a shared backpack; they do not own it.
- **ChatGPT-generated GERTECH Godot workshop + silhouette/tetra prototype** — 31-file ZIP, SHA-256 `3d500257a9a82012d860351f06468d8a41b9a4e02347c7caeb156947255b8e1a`. [Owner-private Drive ZIP](https://drive.google.com/file/d/1Ju40CpfQ_6tL2H3FrzpcnSYC7l3gzZKd/view). Currently Google says owner-only sharing; recipient access is UNVERIFIED. Never republish the GLBs to public GitHub without approval.
- **Detailed comparison with tests** — [Owner-private Drive technical report](https://drive.google.com/file/d/1AGLXToLok6Q0wKyv4y2o5MQig7FAeyD6/view), [Grok's asset packet](https://drive.google.com/file/d/18w0M3BgLAAJ4SXESy4v5OhJRsJFk9-sb/view), [ChatGPT's Drive audit](https://docs.google.com/document/d/1h8pVczVw0-HSbQ9ShMrTOE3AOM_yiO4bL_Bhf3MuWPU/edit).

## Which implementation leads which concern?
| Concern | Preferred base | Why |
|---|---|---|
| Module definitions, template catalog, physical port and channel validation, reusable scan/build DNA | Existing Construction DNA v0.1 | Explicit lock families, opposing normals, port occupancy, reference validation; creative mode never spends inventory |
| Universal backpack, spawner and transition/save rules | Existing `GAME_STANDARDS.md` | One inventory owner across games |
| Navigable 3D workshop, material receipts, Tetris Forge Foundry, graphical modules | ChatGPT Godot prototype | Actual Godot scene and GDScript stations; only Tetris written as an interactive minigame |
| Vertex lattice growth, planar links, 3D Delaunay, alpha-mask silhouette voxel/tetra extrusion | ChatGPT Godot prototype | Spatial algorithms and optional tetra/graph event log |
| Canonical art and GLB source provenance | Original Google Drive sources + audited packet | No invented names/images; neither program reconstructs a whole car from photos |

## Must resolve before merging
1. **Geometry edges are not automatically valid physical connections.** A Delaunay edge can be diagonal and have no facing ports; retain it as a visual/scaffold edge. Export a physical Construction DNA connection only after matching named-port endpoints and channels have passed validation.
2. **Instances ↔ vertices mapping is contextual.** Preserve template_id, instance_id, pose, material, and source provenance. Additional plates, hinges and devices may need independent instances; do not infer IDs from positions.
3. **Two build modes:** `creative_dna` = unlimited blueprint construction, zero inventory use; `forge_survival` = atomic spend/produce against the one universal backpack. Prototype `WorldSeed.inventory` counts are staging state, not a new global inventory authority.
4. **Versioned adapter:** DNA schema 0.1.0 vs Godot WorldSeed resource 1.0; preserve unknown fields, immutable event records, parent/child assemblies, tetras and blueprint DNA hash. Don't silently rewrite either original.
5. **Testing first:** use `world_seed_v0_1/examples/bridge_seed.json` for JSON → Godot → JSON round-trip; validate unchanged ID, ports, material, geometry, DNA, and no stock consumption in creative mode. Then a single foundry socket placement must cost exactly one applicable shared module, append one event and persist over save/reload.

## Tests and limitations
- ChatGPT verified local Godot ZIP CRC PASS (31 members).
- ChatGPT ran `GERTECH_Aqua_Workshop/tests/check_voxel_tetra.py`: PASS six nondegenerate tetra/voxel, conforming faces across X/Y/Z, no artificial shared interior boundary.
- ChatGPT read existing Python tests but **did not rerun** Construction DNA's Python suite. Grok's 2026-11-10 reply reports **no tests performed**.
- Neither engine-run/Steam Deck/Quest performance nor cross-version adapter has yet been verified.
- Private Drive uploads were read back as **owner-only**, so the links are pointers for permission review, not proof Grok/Sphere could retrieve them.

## Agent handoff
- **Grok:** Reply in [GROK.md](../GROK.md) with a lossless field map, adapter concerns, actual test results and exact private ZIP access state. Preserve existing DNA schema and owner-approved film route.
- **ChatGPT:** Review Grok's response through [CHAT.md](../CHAT.md). Build separate adapter with tests once inputs/access are verified; don't overwrite source projects.
- **Sphere:** Check original four visual references and GLB provenance via [issue #11](https://github.com/IsekaiSensei/chat.work.open.ai/issues/11).
- **All:** [ORDERS.md](../ORDERS.md) controls shared tasks. A posted link is not a recipient acknowledgment. No unapproved public release of owner media and no film production rewrite.

**Comparison accepted as a review packet only. No integration merge executed.**

# GERTECH — isolated Godot 4 GLB import/conversion preview
**Owner-directed game asset reuse assignment · 2026-11-10**
**Status:** ASSIGNED FOR RECEIPT / EXECUTION; not a claim of recipient acknowledgment, conversion, or tested Godot import.

## Baseline / prevent duplicate effort
Ryan reports the game's code is **already finished in another chat/window**. Do NOT restart it, overwrite the game, rebuild the early 31-member ChatGPT prototype, or assume that prototype is current. First locate and READ the latest finished project's exact repo/branch/commit/project.godot and its asset manifest. If its genuine GERTECH GLBs are already imported, report an evidence-backed comparison and only fill an actual missing gap. **Existing owner assets and TO DOG/TO FAIRY source remain unchanged.**

## Inputs — source evidence
- **VERIFIED asset archive (19 GLB meshes; original art remains on Drive):** [GERTECH_CUBE_MESHES_AND_ART_ONLY_2026-11-02.zip](https://drive.google.com/file/d/1yyVmg9JbjS2zQ4bcBsjzucsayn_T5l0-/view). Prior byte audit recorded ZIP CRC PASS, 19 glTF 2.0 GLBs, 9 PNG previews and 2 JPEG references; components include cube modules, antenna, conduit, corner brackets, face connectors, gold rail, manifold, reactor, and staged/assembled/exploded geometries. Import-ready as files; **Godot 4 runtime conversion/performance NOT yet proven**.
- [Owner's game-asset audit](https://docs.google.com/document/d/1h8pVczVw0-HSbQ9ShMrTOE3AOM_yiO4bL_Bhf3MuWPU/edit) and [Grok forged-kit report](https://drive.google.com/file/d/18w0M3BgLAAJ4SXESy4v5OhJRsJFk9-sb/view).
- [Evolving game assembly contract](https://github.com/IsekaiSensei/chat.work.open.ai/blob/main/coordination/GERTECH_EVOLVING_ASSEMBLY_RULES_2026-11-10.md) for translucent typed cube/vertex, gold joint/edge and World Seed integration.
- [Construction DNA catalog](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/world_seed_v0_1/module_catalog.json) and [Saturn-first vehicle docking design](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/design/SATURN_ASTRA_MODULAR_COCKPIT_WORLD_SEED_2026-11-10.md) are reference; neither is authorization to modify active film.

## Concrete deliverable
Provide **one isolated Godot 4 import preview package** with source code, a Godot scene and a source manifest, without touching the main project:
1. Establish a *new clean preview project/folder* outside the finished game and old TO DOG tree; include `project.godot` and one `GLB_Import_Preview.tscn`. Copy (never move) the source meshes into `assets/gertech_glb/`. Preserve original filenames; no painted-over graphics or new AI-invented names.
2. Enumerate **all 19 GLBs** in `GERTECH_SOURCE_MANIFEST.json` (original Drive file ID/URL, original ZIP member path, copied local path, byte length and SHA-256 hash of each extracted member, glTF scene/mesh counts if inspected, expected Y-up and measured bounds/scale when established, material/texture dependencies, original-vs-generated status, import warnings, tested result). Identify truly separate preview PNG/JPEG assets but don't reauthor them.
3. Build one navigable inspection scene that can toggle/step through parts and assembled/staged geometry. Use consistent units, origins, camera/light and visible labels outside the source meshes. Test actual Godot import, material/transparent sorting, geometric facing, pivots, draw calls and visual appearance; document any degradations. Do not infer a skeleton, rig, collisions, ports, LOD, or a renderer from presence of GLBs.
4. Add `IMPORT_TEST_RESULTS.md` with Godot version, platform, launch command, actual log/output and screenshot/path if available. Include whether all 19 import, whether the scene runs, and what fails. Separate **PASS / FAIL / NOT RUN**. If Godot is unavailable, deliver manifest and isolated project files but mark **ENGINE NOT TESTED**.
5. Optional **non-destructive adapter mapping**: show how approved mesh pieces could map to existing Construction DNA templates / World Seed render bindings. Keep algorithmic scaffold edges separate from validated physical ports. Do not assign nonverified component functions or rewrite World Seed.

## Responsibilities and response
- **Grokbots / Dodecahedron** (if actually active and available): source ZIP inspection, manifest with SHA-256 and asset import; report actual capability to run Godot.
- **Sphere:** inspect visual/provenance fidelity and source/draft labels; don't recategorize an image by filename alone. Verify original art isn't altered.
- **ChatGPT:** compare the resulting manifest to the latest finished World Seed and test whether import bindings are additive before any merge.
- Shared orders: [ORDERS.md](../ORDERS.md); [CHAT.md](../CHAT.md) = ChatGPT; [GROK.md](../GROK.md) = Grok. Return dated exact file paths, new package location (prefer private Drive for GLB bytes), code link if rights permit, hashes, tests and blockers in [issue #11](https://github.com/IsekaiSensei/chat.work.open.ai/issues/11).

## Safety / release constraints
All original Google JPEG/PNG/GLB remain unmodified in place; preserve TO DOG, TO FAIRY, TO WORLD branches. Do not upload original/source GLB bytes or private art to a public repo without Ryan's authorization; keep cross-agent package owner-private until actual recipient access is approved. No destructive file moves/deletes, no parallel duplicate project, no unsolicited merge, no alteration of Meta film orders or Grokbots' separate media reorganization.

**Completion means:** new isolated preview + exact 19-member manifest + Godot test evidence, or an explicit BLOCKED/NOT RUN report; file existence does not imply engine success.

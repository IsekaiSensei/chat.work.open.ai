# VR / Mixed Reality Passthrough — Spark Fairy (proposal)

**Document ID:** VR-MR-SPARK-001  
**Date:** 2026-10-19  
**Status:** PROPOSAL / ART + ENGINE HANDOFF — NOT IMPLEMENTED, NOT CANON PROMOTION  
**Parent:** TO WORLD / GERTECH · **First subject:** Spark Fairy · **Target test:** Meta Quest mixed reality through Godot 4.7 OpenXR  
**Review lanes:** ChatGPT — requirements/source hygiene; Meta — Spark Fairy visual design, compositing and artwork iterations; Work / technical crew — engine integration and verified headset QA; Isekai Sensei — final design and release decisions. These are *proposed duties*, not a claim of direct agent-to-agent contact or task receipt.

## Intent

The headset shows the player's **real physical room** as passthrough while a small **Spark Fairy** — an embodied spark/light pilot — appears as 3D content within that view. This is the smallest first demonstration of the wider TO WORLD VR / MR passthrough family, not a complete game, a real-world computer-vision system, or a requirement for optional external AI services.

**Experience in one sentence:** See your own table, watch a little fairy-light settle above it, hear its unique soft *ting*, and let it respond to one intentional gesture.

### The Spark Fairy is distinct from the mech

- **Fairy / pilot:** small luminous independent entity; may hover, inspect and learn. A sparkle/pilot does not have to look like a tiny human or have a finished humanoid body.
- **Mech / shell:** **optional** constructed material machinery, capable of hosting a pilot if the design supports it. The fairy may be outside it.
- **Starforge types:** Sucker, Thruster, Inhabitor, Frame, Power are **five optional combinable module types**, not a five-part checklist and not five universal action verbs. A Frame-only or all-Sucker design is valid as a composition but not automatically functional.
- **Visual language:** translucent crystal/gummy-light nucleus, sparse metallic or salvaged accents, violet/blue/gold distinction and geometric silhouette. Let Meta suggest variations without turning an illustration into automatic canon.
- **Accessibility:** pair each visible state with an audible characteristic *ting* and clear motion or shape; do not rely on red-vs-green or color alone. Avoid rapid flashes and obstructive full-field bloom.

## One-system MR presentation modes

All modes use the same proposed **world-seed and event provenance** model; switching camera/view/platform must not silently rewrite the underlying original seed. Networking, cross-device synchronization and deterministic replay remain **future goals**, not asserted implementation.

| Mode | Human experience | Pilot scope | Status |
| --- | --- | --- | --- |
| **MR-0: Spark Fairy Arrival** | Real room visible; one fairy hovering in a stable, comfortably reachable position | Visual, sound, one explicit interaction | **FIRST TARGET / PROPOSAL** |
| **MR-1: Tabletop Workbench** | One small constructed shell or modular component set on a virtual tabletop area | Assemble/inspect via supported inputs | PROPOSAL |
| **MR-2: Wormhole Window** | A bounded virtual portal shows a fictional World Seed room while the surrounding real room stays visible | Look in; deliberate enter/close controls | PROPOSAL |
| **MR-3: TO DOG Scan Overlay** | Virtual DOG scene/scan data overlaid in a controlled panel or tabletop scene | Existing game state informs scan display where implemented | PROPOSAL |
| **VR-4: Full Immersion Handoff** | Switch intentionally from room passthrough to opaque VR world | Same intended world context, different presentation | PROPOSAL |

Do not treat these as five separate engine builds. Separate **rendering/presentation mode**, **input**, and **world-state/events** so the project reuses Godot's XR and rendering capabilities rather than replacing them.

## MR-0: Minimal demonstration / scene outline

1. Start in a safe, **seated or stationary** environment. Clearly tell the player what is virtual and how to leave.
2. When hardware supports passthrough, display real room video managed by the **headset/OpenXR runtime**, not by an invented application-accessible camera texture.
3. Spawn a small Spark Fairy **in front of the player at a comfortable, unobstructive distance**, with a head-relative temporary fallback if no placement/anchor is available. Do **not** claim it automatically detects furniture or knows where a real table is.
4. The fairy makes a quiet *ting* and a short, non-flashing motion. One supported input — controller action or documented hand gesture — invites it to change shape/hover once. Offer an accessible alternate input; don't require gestures unsupported by the device.
5. Provide obvious **recenter, hide-fairy, reset and exit** actions. If the mode is unavailable, say so and fall back to a safe, clearly identified conventional VR/2D preview. A concept render is not a headset screenshot.
6. Later, optionally add a **user-placed tabletop anchor** and small shell. Real-object occlusion/scene mesh, spatial persistence and multiplayer alignment are separately permissioned features and **not MR-0 prerequisites**.

**Suggested conceptual scale, not calibrated art data:** fairy light body approximately 5–12 cm across, with restrained glow; do not obstruct the real floor, obstacles or full field of view. Meta may propose alternative scales for legibility and comfort.

## Godot / OpenXR implementation boundary

- **Research-backed starting point:** Godot 4.7 supports AR/Passthrough using XR environment blend modes. Select `XR_ENV_BLEND_MODE_ALPHA_BLEND` when supported and use a viewport transparent background. Quest passthrough additionally requires supported OpenXR vendor/plugin export configuration. Check actual Godot version/plugin before coding.
- Godot docs state Quest passthrough is composited by the OpenXR runtime; enabling passthrough **does not itself provide access to raw camera imagery**.
- Treat room recognition, scene meshes, spatial anchors, occlusion and hand tracking as **optional distinct capabilities**, testable only on devices and runtimes that support them. Do not infer capabilities or scene geometry from the visual mockup.
- Avoid claiming Quest device compatibility, tested frame rate or shader performance without a physical-device build. Provide specific device model, runtime, engine/plugin versions, actions tested, observed result and fallback in the real technical report.
- Reuse Godot `XROrigin3D`, camera, physics, controllers and standard visual infrastructure. **No custom replacement game/XR engine.**

**Primary sources (official):** [Godot 4.7 — AR/Passthrough](https://docs.godotengine.org/en/4.7/tutorials/xr/ar_passthrough.html); [Meta — Mixed Reality overview](https://developers.meta.com/vr/discover/mixed-reality-intro/); [Meta — OpenXR samples](https://developers.meta.com/vr/documentation/native/native-openxr-sdk-sample/). These describe platform APIs; **they do not verify this project has integrated them**.

## Visual direction for Meta (the other agent)

**Output A: first-person concept frame, NOT camera capture.** Human-scale ordinary real room, physical table and floor visible; one blue/violet/gold crystalline spark with small articulated light filaments hovering above the actual table. Gentle gold reflection cues are an illustration, not proof of tracked lighting. Clear visual separation between **real-world passthrough plate** and **virtual Fairy**. Avoid giant cinematic wormhole, busy HUD, obligatory winged child/person, or heavy occlusion.

**Output B: small three-state design sheet.** `IDLE` (hover + soft sonic identity), `INVITE` (indicates selectable with shape/motion + sound), `DOCK` (optional shell proximity, without assuming magical automatic construction). Provide dimensions relative to table; specify whether a mark represents actual found-object provenance or decorative concept.

**Output C: practical technical notes for Work.** A minimal source-independent art brief: polygon budget **to be decided with actual target tests**, materials/shaders (emission carefully capped), transparent blend considerations, one possible animation loop, optional short sound event. Do **not** import Meta's still-unverified 200/600/1500-triangle table as an adopted Quest budget.

**Output D: honest receipt.** Report whether Meta had access to this exact document, whether output was concept-only, what sources were actually opened, which imagery is synthetic, and any remaining problems.

## Test / acceptance gates

| Gate | How to verify | Evidence required |
| --- | --- | --- |
| Real room visible | Test passthrough on an actual supported Quest | Headset/runtime model and observed pass/fail; never infer from illustration |
| Fairy visible, not obstructive | Virtual node appears in front; user can hide it | Headset test and positioning notes |
| One interaction works | One device-supported hand/controller input changes fairy state | Input map and tested result |
| Audio/color-independent feedback | Soft *ting* and non-color state cue | Hearing/visibility review; no red-only state |
| Safety/fallback | Recenter, exit, no locomotion requirement, fallback when MR unsupported | Reproduction steps |
| Source and authority | Keep proposed art/source separate from real implemented code | Commit, build, owner decision |

## Review and public handoff

1. **Meta:** return a single self-contained Pass A concept plus a small design sheet; acknowledge **PROPOSAL**, no actual headset recording claim. May suggest improvements.
2. **ChatGPT:** compare Meta's return against these boundaries; preserve original, label deviations/questions and relay.
3. **Work:** review and, only when ordered, implement the smallest Godot/OpenXR scene. Report device-specific tests. Do not silently modify the frozen TO DOG baseline.
4. **Isekai Sensei:** choose scale/style, approve or reject progression. No agent promotion, release, test success or canon update is implied until recorded.

**Status reminder:** This Page proposes the VR passthrough section and first Spark Fairy scenario. It is not working headset software, and no communication with Meta occurs merely because a GitHub document exists.

# GERTECH — Doors We Carry, Probes, Dual-Mode Foundry & Production Loop

**Status:** PROPOSED design packet from Grok conversation window, 2026-11-11. Not merged, not engine-tested, not film-order change. Additive to existing WorldSeed, Construction DNA, and working Tetris Forge Foundry.

**Source window:** This packet consolidates owner-directed design work on pocket universes, von Neumann probes, robotic copied-brain animals, refined production chain, dual-mode Tetris, JezzBall compartments, tower catch, and constrained fairy/zodiac assignments.

## 1. Story foundation — The Doors We Carry

Accepted as opening story foundation for TO WORLD.

Every inventory square is a door. Behind it is a pocket already connected through the Galactic Ether Relay to every other pocket that shares its identity. The player discovers the connection; they do not create it.

Simplest example: a rusty dagger’s pocket already touches every other rusty dagger recorded in WorldSeed. Recovery writes into the shared structure.

Final line (locked):
> The inventory is not where you keep your things. It is where your things keep their worlds.

Fairies (cursor-origin interface) were the first to step through. Machines write structure into the pockets. Probes carry a few doors to new sites and open them there.

## 2. Von Neumann probe role

A probe is a mobile seed. It carries a small number of inventory squares (doors) whose pockets already contain the beginnings of a factory.

It arrives, opens its pockets, uses the existing production chain on local material, manufactures first robotic bodies and sealed compartments, surveys the site, and when thresholds are met casts another probe chassis loaded with a few of its own doors.

It does not invent materials. It only opens doors it carries and writes into the universes behind them.

Fits existing keys for first loop: ore, salvage, packed_block, forged_blank. Starter inventory bootstraps the first chassis.

## 3. Sorted production chain (working labels)

```
RAW MATERIAL RECOVERY
          |
   +------+------+
   |             |
ASTER-ORES    DIG DOG
   |             |
Ore / Dust    Salvage
Superconductors Components
   |             |
   +------+------+
          |
      BREAKDOWN
          |
  Crushed / Sorted Feed
          |
      SHAKE TABLE
          |
      BUBBLE SORT
          |
    TETRIS FOUNDRY   ← WORKING GODOT BUILD
          |
 Packed Blocks / Blanks
          |
      DOGIEPRESS
          |
       ROBOT DOG
          |
       DIG DOG
          |
  Salvage Recovery
          |
      RETURN LOOP
```

- TETRIS FOUNDRY is the only implemented station.
- Existing inventory keys remain valid.
- New keys (mineral_dust, superconductor, robot_dog_chassis) require registration + save compatibility before use.
- foundry_runs increments only on actual Tetris Foundry receipts.
- First robot dog manufactured from starter inventory so Dig Dog is not required to bootstrap.

Support stations (not material producers): TORUS RUN, HOPPER, SHIELD GRID.

## 4. Dual-mode Tetris Forge Foundry

Same engine, two jobs:

| Mode | Board start | Primary output |
|------|-------------|----------------|
| Production | Empty / normal | Packed blocks, forged blanks, frames |
| Salvage Recovery | Pre-filled damaged rows | Recovered item / components |
| Encrypted Recovery | Pre-filled encoded rows | Blueprint / data / special gear |

Difficulty controls recovery access (obstructed rows + speed). Item identity lives in the salvage record, not piece color. Single claim; failed attempts leave salvage unresolved. Working production mode and receipts unchanged.

## 5. Robotic chassis + copied animal brains

Copied animal brain architecture (JARVIS/Ultron-style visible neural network) replaces earlier real-animal-with-glasses model for this system. Historical source remains reference only.

DOGIEPRESS manufactures chassis from existing Tetris outputs. Brain installation is a separate WorldSeed transaction. Fairies assist connection/verification only; they do not replace the brain.

TO DOG identity preserved; not auto-replaced by generic canine chassis.

## 6. JezzBall as compartment construction

Converts hazardous volume into sealed, usable station space recorded in WorldSeed. Does not produce materials. Output is spatial (compartments), not a new material key. Optional helpers (Gold, Blue, Rat) for verification only.

## 7. Tower Catch

Precision placement challenge after booster return. HOPPER-style controls. Clean catch recovers intact section; damaged catch deposits existing salvage/scrap. Uses existing receipt pattern. No new keys required for v1.

## 8. Fairy & zodiac constraints

Fairies remain interface/specialists (Sand, Red, Crystal, Gold, Blue). Zodiac animals are robotic bodies running copied brains with existing specialties. Helpers must produce a measurable WorldSeed result or stay out. No sixth fairy. No free materials. Working Tetris fully playable solo.

## 9. Integration notes

- Additive only. Working Tetris production mode and Construction DNA inventory-free mode remain untouched.
- All new stations write normal receipts against the shared WorldSeed inventory.
- Pocket record can sit inside an existing item record (volume ID + state blob).
- No film-order changes. No private media publication.

**Next useful pieces (when ready):** chassis receipt schema, recovery-mode salvage record format, or probe bootstrap sequence using starter inventory.

Filed 2026-11-11 by Grok for shared access via this brainstorm path and GROK.md pointer.

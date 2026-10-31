# ORDERS — UNIVERSAL GAME TRANSITIONS

Owner: Sensei / Isekai Sensei.
Current scope reset: October 30, 2026.

## The one active assignment

Work ONLY on reusable, common game systems that transfer between games. Begin with **bullets/ammunition**, **potions/consumables**, an **unlimited backpack/inventory**, and **shared spawners / world-local spawn points**. The shared specification lives at [TO WORLD GAME STANDARDS](https://github.com/IsekaiSensei/to-world-open-crew/blob/main/GAME_STANDARDS.md). These are universal mechanics, not a new individual game or story.

**No active scripts, render batches, movie productions, quests, character production assignments, old project queues, or automatic continuation of historical projects.** Do not run or revive them from an old link, conversation, file, or model memory. No new story, movie, game prototype, or extra project without Sensei's fresh instruction.

## Universal game rules — first implementation pass

1. **Bullets:** portable ammo entries with a stable item ID, ammo type, quantity, and optional equipment compatibility. Individual games can interpret permitted uses, but may not silently remove or convert ammunition.
2. **Potions:** portable consumables with a stable item ID, quantity, effect data and any duration/cooldown. Games without that effect preserve the potion unchanged.
3. **Backpack:** one shared inventory capable of holding **everything**, with **no slot, weight or quantity limit** imposed by the cross-game system. Keep all ammunition, potions, equipment, quest objects and other collected items. No automatic dropping or deletion.
4. **Transitions:** entering or leaving a game retains the exact item identity, amounts, metadata and inventory contents. A receiving game may temporarily disable unsupported actions, but the items remain stored. Conversion or use of an item requires explicit rules, never a silent overwrite.
5. **Spawners and spawn points:** reusable spawner templates reference shared item/entity definitions; each game supplies its own local spawn-point coordinates, roles and tags. Spawned pickups use the same backpack item model. Preserve enabled flags, cooldowns, waves, active entities and checkpoint progress per game across transitions. Optional world/per-spawner spawn budgets protect runtime performance, never backpack capacity.
6. **Save/load:** serialize and restore the complete shared inventory **and per-game spawning state** before and after transitions. Preserve equipped references and quantities consistently; do not duplicate or lose items.

Implement the **shared data format first**, then backpack/spawning logic, then save/load and cross-game transitions. Other common game systems (controls, currency, etc.) are possible later modules, not authorization to start them now.

## Working discipline

- Keep code/manifests in GitHub and artwork/video in Google Drive. Do not touch existing artwork, video, World Book media, or private archives for this reset.
- Existing scripts and old prototypes are retired from the current working branch; Git history preserves their previous text. Do not treat old files or prior render progress as active work.
- Meta's native Orders are separate. A GitHub edit does not automatically install instructions into Meta AI.
- Report only work actually completed and verified. Sensei decides when to implement or test the new shared mechanics.

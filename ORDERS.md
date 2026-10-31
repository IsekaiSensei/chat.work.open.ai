# ORDERS — UNIVERSAL GAME TRANSITIONS

Owner: Sensei / Isekai Sensei.
Current scope reset: October 30, 2026.

## HARD STOP — SOURCE PRESERVATION / SECTIONING IS NOT REWRITING (OWNER CORRECTION, 2026-10-30)

**This rule applies to ALL scripts, musical scores, stories, game specifications, video/dialogue archives, and other owner-created source material. It overrides any assistant preference to improve, rewrite, modernize, summarize, re-sequence or expand a source when the owner asks only to organize, section, batch, extract, index, or upload it. The owner does not need to repeat this warning.**

**ONE MASTER IS AUTHORITATIVE.** Before sectioning, fetch and read the exact existing source, note its file ID/path, version and available SHA/hash, and treat it as READ-ONLY. Never replace it with a generated approximation, an old chat recollection, another script version, or a newly invented 'master'. Do not silently promote a previous rewrite to canonical source. When the exact master cannot be found or read, STOP and report that blocker; do not reconstruct it.

**SECTION = COPY, NOT COMPOSE.** A section/batch is only a contiguous, non-overlapping selection of existing ordered source rows, with their complete **verbatim** dialogue/lyrics, speaker, punctuation, verse breaks, stage action, music cues, scene order, identity and continuity instructions. No rewriting Shakespeare, inventing dialogue, embellishing tech actions, replacing songs, changing the cast, relocating scenes, or shortening/truncating lines. Do not impose a desired number of clips on the dialogue; source beats determine count. A request to *section* does not authorize a *rewrite*.

**INDEX AND BATCH SAFELY.** Use one stable master manifest/table (spreadsheet if appropriate): immutable `source_clip_id`, exact source text, character, action, music/scene cue, and derived `batch_id`/render status. The same source row belongs to EXACTLY ONE production section. Batch labels are views of the master, never a new script. No overlapping ranges, dropped rows, duplicated rows, regenerated chapters or replays of already-completed segments. Numbering remains stable; if the owner expressly requests resetting display numbers to 001, retain the original `source_clip_id` in the mapping and do not move, omit, repeat or rewrite source content.

**BEFORE ANY EXPORT/RENDER HANDOFF, FAIL-CLOSED CHECK:**
1. Read back both the original master and the extracted section(s); compare every selected source ID, exact text (including Shakespeare lyric/verse punctuation), speaker, action, scene and order against the master.
2. Compare the full section index against the full master: each selected row appears exactly once, sections do not overlap, earlier completed clips are not recycled as a continuation, and no selected row is missing. If source already contains intentional repeated words/lines, preserve them only at their ORIGINAL source IDs. A repeated source ID is a failure.
3. Preserve a coherent song/scene across clip boundaries: same musical phrase and rhythm, character, camera, environment and action; the 10-second segment length is a render container, **not a new scene or new song**.
4. For this Metal the Musical workflow, use the owner-ordered **10 clips per batch** (last batch may be shorter). Never silently switch to one-at-a-time or create a different batch length.
5. If ANY comparison fails, do not export, send to renderer, or announce 'ready'. State the exact mismatch and source IDs. Do not fix it by writing another master.
6. Keep rendered, pending, rejected and unknown status distinct; a file on Drive or instructions on GitHub are NOT proof Meta rendered it. Never ask for a second GO when the owner already ordered execution. Report tool access limitations factually.

**RECURRENCE EVIDENCE — WHY THIS EXISTS:** Metal the Musical had at least FOUR overlapping/competing script variants (169 clips 171–339; 207 beats 171–377; 227 beats 171–397; restarted 157 clips 001–157). Verified comparison found **all 157 dialogue entries in restarted clips 001–157 repeated at 241–397** of the 227-beat version. Additional failures were invented 'Shakespeare-inspired' lyrics in place of original words and one-at-a-time prompts contrary to ten-clip batching. THESE ARE KNOWN DEFECTS, NOT TEMPLATES. Do not use the flawed versions as authority. Preserve originals/history; no new renders or replacements are authorized by this audit.

**Owner override:** Explicit instructions to *rewrite*, *adapt*, *renumber* or *change* specific content may authorize only those named changes. Keep the original intact, record exact changed source IDs and the before/after difference, and never infer permission to change unrelated sections.

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

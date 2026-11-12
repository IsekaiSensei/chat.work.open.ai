# SPAWN POINT GENERATOR — SINGLE BOARD PLACEMENT RULES
Creator: Isekai Ryan
Status: GAMEPLAY SYSTEM SPECIFICATION — not rendered, not implemented, not a Shotcut editing instruction.
Scope: One AI decision window, one active board, one resource ledger. No second strategist per unit.

## PURPOSE
Print the board, then place robots according to WHAT EACH POSITION IS FOR and WHAT ACTUALLY ARRIVED. Bosses are high-value strategic units. Ordinary respawns carry simple, repeatable instructions. The queen is not placed at the gate.

**Basic law:** a spawn point is a location; it does not manufacture, transport or supply a unit. Every spawn must be authorized by available material, a completed route, a valid position and a completed timing rule. The board can change when the player changes the network.

## SINGLE WINDOW INPUT — READ ONLY VERIFIED CURRENT STATE
- BOARD: the 8 × 8 logical placement grid (or a correspondingly mapped grid in a game room); terrain occupancy, accessible cells, walls, gates, sightlines and traversable routes.
- OBJECTIVES: what must be defended, delivered, captured or repaired. Distinguish a win condition from a unit.
- NODES: generator, receiving depot, storage, fabrication, staging, spawn points and destinations; each has identity and status.
- MATERIAL: on-hand quantity, reserved stock, parts in transit, losses and completed receipts. In transit is not available for spawning.
- PRODUCTION: recipes, processing time, energy cost, manufacturing capacity and ready units by role.
- MOVEMENT: actual connected routes, capacity, transit time, interruptions and delivery confirmation.
- UNITS: active, queued, damaged, destroyed, returned and available; role and current square.
- TIME: simulation tick, cooldowns, travel/assembly deadlines and next evaluation.
- PLAYER CHANGES: destroyed bridge, captured node, consumed stock, opened path, defeated guard, diverted shipment.

## PIECE TYPES — ROLES, NOT SIX INDEPENDENT AIs
| Chess name | Game function | Decision level | Placement priority |
| --- | --- | --- | --- |
| PAWN | Basic guard, laborer or ordinary respawn | Fixed local instructions | Screen appropriate routes, work assigned task; cheap to replace only when material is available |
| KNIGHT | Mobile interception and flanking | Route-following with limited local reaction | Reach alternate lanes, cover exposed crossings |
| BISHOP | Specialized line/range support | Fixed domain or line-of-sight rules | Protect long approaches or specialized infrastructure |
| ROOK | Heavy positional defense | Hold assigned protected position | Cover depots, generators, bridges or critical corridors |
| QUEEN | Adaptive boss / high-value mobile reserve | Strategy directed by the single window | Keep available to answer decisive threats, never default to the gate |
| KING | Critical objective, command asset or failure condition | Protected state, not automatically a combat boss | Place according to actual objective and defensible access, not as arbitrary final boss |

The board uses chess as a DEPLOYMENT METAPHOR. These units are not required to move according to the official rules of chess unless the owner explicitly selects literal chess behavior. The player's map may render as a room; all placement still uses one logical board.

## EXACT PROCESS (ONE WINDOW, ONE EVALUATION PASS)
01 — RECEIVE: Confirm deliveries posted to the ledger. Do not count shipments that have merely been requested or dispatched.
02 — MAP: Read the existing board, gates, terrain, occupied cells, usable routes and positions controlling the actual objectives.
03 — COUNT: Calculate ready-to-place units from completed fabrication, energy, materials and role-specific limits. Keep reserves distinct from deployed stock.
04 — ASSIGN: Give each ready unit a piece role and simple task based on the current objective and available resources.
05 — PLACE: Choose legal empty positions, satisfying reachability, purpose and protection before spectacle. Do not spawn on an occupied square, behind an impossible route or inside an unavailable zone.
06 — VERIFY: Check that the selected unit exists, its cost has been paid or reserved exactly once, its route is valid and its spawn cooldown has elapsed.
07 — COMMIT: Atomically mark supply as consumed/reserved, mark position occupied, update unit state and record the placement. Failed validation changes nothing.
08 — OPERATE: Ordinary units run their assigned simple behavior. The single AI window controls board-level strategy rather than individually improvising every pawn's thoughts.
09 — DETECT: Read actual losses, delayed deliveries, captured routes, damaged infrastructure and changed objectives. Do not silently heal or restock.
10 — REPLACE / REPOSITION: Evaluate needs, travel and resource arrivals before respawning. Deploy a reserve or change placement only if it is physically, economically and temporally possible.
11 — PERSIST: Record the new state for the next evaluation. The board never resets because the player entered a different room.

## PLACEMENT ORDER (NOT A FIXED FORMATION)
A. Identify critical objective and vulnerable production/supply nodes.
B. Defend essential infrastructure before adding disposable gate guards.
C. Cover practical approaches with low-cost units whose behaviors are sufficient for that approach.
D. Reserve movement corridors for interceptors and reinforcement deliveries.
E. Keep high-value specialists where their coverage matters, not where they look impressive.
F. Keep the queen behind an appropriate defensive layer or in a useful reserve position with a viable route to emerging threats. **Never default queen to the entrance.**
G. Protect the king/objective as required by the actual win/loss condition; avoid positioning that blocks its own supplies.
H. If a role cannot be paid for, delivered, or placed legally, leave its slot empty and record the shortage. Never fill it by inventing a unit.

## SPAWN / REINFORCEMENT TRANSACTION
PRECONDITION: spawn_point ENABLED; cell FREE; route REACHABLE; required item READY or fabrication FINISHED; ledger AVAILABLE; production ENERGY AVAILABLE; cooldown COMPLETE.
EXECUTION: reserve role-specific cost → route/deliver if required → confirm arrival → place one unit → consume exactly once → log source, destination and tick.
FAILURE: no unit appears; produce an explicit reason (BLOCKED, STOCK_OUT, IN_TRANSIT, NO_POWER, COOLDOWN, NO_RECIPE, POSITION_OCCUPIED).
DESTROYED UNIT: counts as an actual loss. A replacement is NOT a free respawn; rebuild or draw from an already available reserve, then fulfill transit and cooldown.
ROUTE DISRUPTED: units already on the board remain until defeated or moved; undelivered reinforcement stays pending or fails and cannot teleport past the failure.
REOPENED ROUTE: pending shipments can resume only after route state and elapsed transit are reverified.

## SAMPLE SINGLE-BOARD DECISION (ILLUSTRATIVE; NOT A LOCKED MAP)
A player disables the north supply route while the boss queen is still in reserve. Existing pawns continue carrying their simple local orders. The next AI board evaluation sees fewer confirmed arrivals and no valid north-side reinforcement path. It stops new north spawns, protects the remaining generator with already-present units, and reassigns the queen only if she can actually travel along an open route. It does not conjure guards at the gate or reset the board.

## INVARIANTS / TESTS
- No unit spawns unless its actual resource and transit requirements were satisfied.
- No unit spawns in a blocked, occupied, unreachable or disabled position.
- A queen/boss is never default gate furniture; any deployment there requires a separately justified strategic reason.
- Two units never consume the same stock receipt.
- No material goes negative. Reserve stock is unavailable to another deployment.
- Time includes fabrication, travel and cooldown; no instant movement unless an existing game mechanic explicitly supplies and pays for it.
- Re-evaluation uses the current state, not a hidden fresh board.
- Local robot behavior is simpler than the single central placement decision.
- A changed route produces a detectable, causally consistent change in what can be deployed.
- Logs let the player/developer trace WHY a unit appeared: origin → processing → delivery → placement.

## SEPARATION OF CONCERNS
This file defines **game placement and logistics**. Its home is GitHub manifests, not the Shotcut jigsaw edit map. The Shotcut file controls visual/audio composition of existing footage only and must not be used as the authority for spawn decisions. Do not add production or art instructions here.

No renderer execution, Godot implementation, repository-wide ORDERS rewrite or placement simulation has been performed by this specification.

# LEGACY-ONLY — FIXED TEN-SECOND CELL COMPILER

This tool is a historical data compiler with hardcoded `CLIP_MS = 10_000`. It does **not** support the owner's current flexible-duration 5–15-second production and MUST NOT be the default generator for new work. The 90-clip format was never intended to be a universal rule. Existing outputs and source material remain valid records. CLI now requires an explicit `--legacy-fixed-10s` flag for intentional old-plan regeneration. No new variable-duration compiler is claimed to exist here; use the current production plan in [ORDERS](../../ORDERS.md) instead. No action is authorized by reading this file.

---

# Production data tool

Current production method: [ORDERS.md](../../ORDERS.md). The canonical [screenplay](../CONVERSATION_SCREENPLAY.txt) contains sung source dialogue; [shot lists](../../production-sheets/CONVERSATION_SHOT_LIST.md) carry camera instructions; [dailies](../../production-sheets/DAILIES.md) record actual outputs. This tool's timing/source flags describe data completeness and do not authorize production holds over drift or consistency. Source speakers remain the singers; do not assign a new performer identity.

# TO WORLD — Production Cell Compiler (non-destructive)

**Use:** approved original visual reference + approved exact dialogue + explicit timing source → ten-second production *data*. Nothing is rendered or edited. There is no implied Meta GO.

## Truth boundary

- `visual_references` are links to existing owner-original images; never manufactured local paths or generated-clip stills.
- `turns[].text` is copied literally, including punctuation and whitespace. The compiler does not generate dialogue or deduce a speaker or silent listener. **To check it against the original transcript rather than merely against itself, use `--source-text original.txt` and add each turn's `source_span` character offsets.**
- Optional `the_tale`, `the_fable`, `the_journey`, `time_to_frame`, and `frame_state` copy approved existing scene context **verbatim**. Any provided values require `story_context_source`; no new story context is generated.
- `frame_ref` connects the current turn to a specific approved visual. An original image's bounding box **does not** independently verify an object's identity or role.
- `speaker_status: VERIFIED` requires a `speaker_source`; `status: VERIFIED` for a visual requires `approval_source`. These are **declared provenance**. The compiler does not independently read or authenticate that external source.
- `silent_listener_ids: []` with `listener_status: UNVERIFIED` means **not provided**. If the source explicitly proves no one listens, set `listener_status: VERIFIED_NONE` and provide a source. Approved present-but-silent characters use `VERIFIED` and a source. Clips with unverified listener context are flagged; unrelated clips are unaffected.
- All clip containers are `10,000 ms`; a ten-second container **does not guarantee spoken text fits**.
- Keep estimated timing and unresolved source metadata labeled as such; these labels are not Ryan's QC verdict or an instruction to stop an otherwise authorized run.
- This data tool does not change the current source selection or completed footage.

## Input JSON fields

```json
{
  "project_id": "the real owner-approved project ID",
  "visual_references": [
    {
      "reference_id": "reference name from approved index",
      "original_image_uri": "the actual verified existing Drive/original reference link",
      "panel_id": "approved panel identifier, if applicable",
      "status": "UNVERIFIED",
      "approval_source": null
    }
  ],
  "turns": [
    {
      "turn_id": "original spoken turn identifier",
      "text": "exact source dialogue goes here",
      "speaker_id": "speaker identity established in source",
      "speaker_status": "UNVERIFIED",
      "speaker_source": null,
      "silent_listener_ids": [],
      "listener_status": "UNVERIFIED",
      "listener_source": null,
      "frame_ref": "reference name from approved index"
    }
  ]
}
```

This is a **structural illustration only**, not a production source. The actual distributed [`input_template.json`](input_template.json) includes **no fictional dialogue or image paths**.

## Estimated draft (never render-verified)

```bash
python3 production_cell_compiler.py --legacy-fixed-10s owner_input.json --mode draft --wps 2.5 --out review_only
```

The operator must explicitly set WPS; the compiler never assumes one. This divides *verbatim* text at deterministic word boundaries in draft time windows. Punctuation, spaces, repetition and capitalization are retained character-for-character. The tool marks timing estimates `HOLD` in its data output. This is a timing label, not an automated production veto; record actual delivered performance separately.

## Time-aligned mode (source-evidence declared, not cryptographically verified)

For each speaking turn, add `timed_units` covering the full `turn.text` sequentially:

```json
"timed_units": [
  {
    "char_start": 0,
    "char_end": 12,
    "start_ms": 0,
    "end_ms": 4000,
    "timing_evidence": "identifier of the real approved audio/cue evidence"
  }
]
```

Offsets refer to Python Unicode string positions, not bytes. The units must cover every character without gaps, and actual time codes must refer to one consistent **absolute** film timeline. Use only with real evidence; values shown are schema illustrations, **not a claim about a real clip**.

```bash
python3 production_cell_compiler.py --legacy-fixed-10s owner_input.json --mode timed --out checked_cells
```

If a timing unit crosses a ten-second boundary, the affected clip is `HOLD` and the program does **not** pretend to know a valid split inside the unit. Add an approved subdivision from actual audio/owner cues instead. Other clips continue. Passing the timing source through does not authenticate the sound or prove a render is ready.

## Outputs

- `cells.json`: exact source substrings, speakers, silent listeners, original image refs, local and absolute timing, issues.
- `cells.csv`: spreadsheet-compatible view with continuous ten-second rows, optional existing Tale/Fable/Journey/Time-to-Frame/state, and continuation character offsets.
- `verification.json`: SHA-256 of every original dialogue turn, exact copy check, flagged cells, known limitations.

CSV is a **view**, not a replacement for the JSON, because a ten-second window may contain multiple speaking turns. The JSON keeps each turn distinct rather than merging speaker identities.

## Guarantees and non-guarantees

The script checks **exact character preservation** and declared structure; it doesn't generate any original content. It **cannot** prove that a referenced JPEG is approved, that someone in a picture has a specific function, that a performer spoke at the declared speed, or that Meta produced a finished MP4. Those require actual source inspection and performance/render evidence. It cannot make creative hallucination impossible in downstream models, so use data validation and source review instead of relying on a negative prompt alone.

## Original-file verification (strongly recommended before any Meta use)

The compiler's default preservation proof only establishes that it reassembled the provided JSON's dialogue without loss. It **cannot prove the JSON itself was copied faithfully**. To establish that, export the actual authorized source dialogue to a UTF-8 text file, and add a `source_span` to each turn: `{"start_char": 123, "end_char": 180}`. The indices must select that turn's exact text in the source file (Python Unicode characters, starting at zero). Run:

```bash
python3 production_cell_compiler.py --legacy-fixed-10s owner_input.json --source-text original.txt --mode draft --wps 2.5 --out review_only
```

If even one original character differs, execution stops **without writing outputs**. The source text file is read-only, and this proof still does not authenticate the source file's own authority.

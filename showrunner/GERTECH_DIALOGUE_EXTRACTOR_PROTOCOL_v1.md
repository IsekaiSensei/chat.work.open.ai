# GERTECH Dialogue Extractor — Working Protocol v1

## Purpose

Mine original conversations, logs, scripts, and source records for exact dialogue, exchanges, narrative beats, and important distinctions. Preserve the source before any adaptation for film.

## Non-negotiable extraction rules

1. **Extract first; interpret later.** Do not summarize source dialogue or rewrite it to sound neater.
2. **Preserve exact wording and order.** Retain punctuation, repetitions, interruptions, corrections, and speaker turns when they matter. Never silently splice separate statements into one quote.
3. **Keep attribution intact.** Record the actual source speaker separately from any proposed on-screen performer. A line written by ChatGPT is not automatically a Ryan or Gemini line.
4. **Keep status distinctions.** Mark statements as direct statements, documented decisions, proposals, inferences, unresolved questions, or historical notes. Do not promote a proposal or an assistant suggestion into canon.
5. **No invented dialogue.** When a scene needs a line that is absent from the source, leave the dialogue blank and mark the gap. A new connective line can only be drafted in a later, clearly labeled creative-writing pass.
6. **Preserve meaningful variants.** If a phrase was corrected, retain the original and the corrected form with provenance. Do not overwrite the source.
7. **Keep source pointers.** Every extracted item needs a filename plus page, line, message, timestamp, or another recoverable location. If no locator exists, say so.

## Four-stage workflow

### Stage 1 — Raw sweep

Process one source file or a bounded chunk at a time. Extract every distinct line, exchange, argument, correction, and narrative beat that carries a specific point. Keep the original order. No scene formatting and no summarization at this stage.

Raw extraction fields:
- Source file and source date
- Message/turn, page, line, or timestamp
- Actual source speaker
- Exact quotation or exchange
- Context immediately before/after when necessary to preserve meaning
- Initial status label (decision, proposal, inference, open question, historical)

### Stage 2 — Distinction filter

Compare the raw extracts against each other and identify the most consequential distinctions. Quote the source wording exactly. Explain why a distinction matters only in a separate editorial note. Preserve contradictions as contradictions until the owner resolves them.

Examples of distinction categories:
- proposal versus appointment
- blueprint versus fabricated machine
- fabricated machine versus self-replicating system
- delivery versus construction
- one continuing identity versus multiple independent instances
- historical role versus current role
- concept image versus finished asset
- storyboard versus generated video versus edited/published film

These are categories, not substitute quotations. Use only wording supported by the source.

### Stage 3 — Ten-second scene formatting

Create scenes from the selected extracts only after the distinction review. Each target scene is 10 seconds. A 20–25 word line is only a rough planning estimate; actual duration depends on delivery speed, pauses, and performance. The recorded/measured audio duration is the final timing check.

- Do not cut a sentence in half.
- Split only at a natural sentence or dialogue-beat boundary.
- Keep exchanges intact when the reply is essential to the meaning.
- If the exact quote will not fit naturally, preserve it in the extraction register and mark it for multiple scenes rather than shortening it.
- Each 10-second render must still be a complete, independently satisfying cinematic short. A sequence of scenes may form a larger story, but no scene should depend on an instruction to stitch an unfinished action together later.

Scene fields:
- Scene ID
- Source pointer
- Actual source speaker
- Proposed on-screen speaker (only if adaptation is authorized)
- Verbatim dialogue
- Word count and measured duration
- Visual context from approved references
- Physical action/prop visible on screen
- Camera/action
- Distinction and status labels

### Stage 4 — Visual assembly

Use approved visual references and preserve character, material, prop, lighting, and camera continuity. A filename or written description does not prove an image was inspected. Candidate or uninspected images remain marked as such. Never claim a concept image is a model, rig, scene, generated clip, edited film, or published post.

## Output discipline

Maintain separate records for:
1. Raw extraction
2. Distinction register
3. Scene breakdown / storyboard
4. Generation prompts
5. Generated clip receipts
6. Edited film receipts
7. Publication receipts

Do not replace the raw transcript with a condensed script. Do not delete the source after extraction. The extraction register is an index back to the original, not a replacement for it.

## Default statuses

- `RAW EXTRACTION`
- `DISTINCTION REVIEWED`
- `STORYBOARD`
- `READY FOR GENERATION`
- `GENERATED — RECEIPT REQUIRED`
- `EDITED — PLAYBACK REQUIRED`
- `PUBLISHED — LINK REQUIRED`

A written prompt, scene description, or shot list is not evidence that a video was generated.

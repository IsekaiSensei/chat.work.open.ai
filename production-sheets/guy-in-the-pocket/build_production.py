#!/usr/bin/env python3
"""Build the complete verbatim Guy in the Pocket production from retained source and shot plans."""
from pathlib import Path
import json, re, hashlib
ROOT = Path(__file__).resolve().parent
SOURCE = (ROOT / "source/ESSAY_VERBATIM.txt").read_text().rstrip("\n")
speech = json.loads((ROOT / "segmentation.json").read_text())
plans = json.loads((ROOT / "scene_plans.json").read_text())
silent = json.loads((ROOT / "silent_plans.json").read_text())
links = json.loads((ROOT / "publish_links.json").read_text()) if (ROOT / "publish_links.json").exists() else {}
OUT = ROOT / "delivery"
OUT.mkdir(exist_ok=True)
VOICE = "ISEKAI RYAN — his one consistent natural speaking voice"
characters = {
 "RYAN": "Isekai Ryan, the source-matched chief craftsman: his actual face, long gray-brown hair and full gray beard, using the working body and clothes of the selected supplied workshop page",
 "RYAN_M": "the mechanical in-pocket version of Isekai Ryan, with his same recognizable face and hair/beard geometry; use the supplied mechanical treatment, already embodied inside this limited pocket",
 "ASSISTANT": "the source-matched adult brunette android assistant: her established face, wavy brown hair, bright white glazed porcelain, gold details and living blue mana, in the supplied task-appropriate outfit",
 "HANDS": "the same outside adult customer, framed as gloved hands/forearms and source-matched working clothes; no new customer face",
 "TELLER_HANDS": "the service-side adult worker's gloved hands; no new teller face",
 "CUSTOMER": "the same fully clothed adult service customer, source-matched and shown only to the extent needed for the assigned service"
}
worlds = {
 "POCKET": "Inside Ryan's persistent zero-G ether pocket dimension. Its actual quantum workshop and table are inside the space opened by the MAIN paired DNA wormhole. Small paired-helix openings beside objects are local transfers in that network.",
 "PLAYER": "At the outside customer's source-matched inventory/service access. Any interior seen beyond its paired DNA aperture is Ryan's actual pocket dimension, with the persistent quantum workshop inside; a local object transfer is distinct from the main dimensional entrance.",
 "LIMITED": "Inside a particular incomplete, bounded pocket dimension reached through the established DNA wormhole. This limited pocket supports Ryan's already mechanical in-pocket embodiment; do not apply its limitation to every other world or pocket.",
 "BANK": "At the source-matched service counter, staging the ordinary bank-teller capsule analogy within the supplied setting. Customer and service worker remain at their own receiving ledges; the actual GERTECH version receives at the quantum table inside the DNA-opened pocket dimension."
}
reference_policy = """STANDARD VISUAL REFERENCE SET 01–10
Ryan's current standard pages 01–10, supplied directly to Meta, are the working references for this production. Keep their original numbering and use the pictured subject identified in each clip's REFERENCE field. Page numbers 01–10 are reference-page identifiers; CLIP 001–090 are film identifiers. They are not the retired Shakespeare actor numbers 01–30 or an older nine-slot inventory of source art.
Ryan's actual face and its angles on the supplied pages govern his likeness in every appearance. Use the same chosen assistant and the same actual quantum workbench. Reference pages are inputs for moving cinematic films, never a slideshow of the page.
Select the relevant pictured setting/character/prop within that current set. Do not assign guessed page numbers, invent reference URLs, request all references again, or substitute old Shakespeare cast blocks. The owner is supplying the visual references to the renderer.
Preserve any existing zipper detail only where it is already present in the selected source or existing owner footage. Its mention in the narration is never a command to draw a new zipper.
"""
contract = """THE GUY IN THE POCKET — COMPLETE META PRODUCTION
Isekai Ryan | Owner-directed switch, November 7, 2026

Every ten-second render is a complete, independently satisfying cinematic short film.

ACTIVE SOURCE: the essay body pasted by Ryan in the switch instruction, verbatim and in its original order. This source is narrower than the longer earlier essay file; it is not silently replaced with that earlier edition.
90 actual films, exactly 10.0 seconds each: 84 spoken-narration films and six intentionally nonvocal films. Nine batches of ten. Planned full duration 15:00.
Clip numbering begins at CLIP 001; BATCH 01 contains CLIPS 001–010. Global IDs continue through CLIP 090; never restart the global counter for a later batch.
The source link/title, copied separator and final filing sentence about META.md are retained in source/OWNER_QUOTED_SOURCE.txt as source metadata. They are not narration or extra words in the film.

PERFORMANCE: Ryan speaks the essay as a clear, warm explanation in his own consistent natural voice. This production does not inherit Shakespeare singing, rap, cast dialogue or lyrical fillers. Other visible people are silent. Spoken narration may be offscreen while the physical noun and work occupy the image. If Ryan speaks visibly on camera, only his mouth performs that exact narration.
Each narrated segment contains 6–21 words. Speech-window estimates use about 140 words/minute and are planning estimates, not measured rendered audio. Every shot remains 10.0 seconds; give its physical action a clear starting condition, purposeful movement and visible result. Short lines leave time to observe the work. No words may be cut, rewritten, reordered, duplicated or filled with ad-libs.
Nonvocal entries have no narration, singing, rap, recitative, humming, dialogue or whispered filler. Restrained instrumental music and environment/action sound may remain. Empty views contain no visible people of any kind.
Use the standard fields in every entry: META FRAME, REFERENCE, TIMING, PERFORMANCE / AUDIO, RYAN narration or NO VOCALS, and BACKGROUND / CAMERA. Only the narration text is performed; these field labels and instructions are not spoken.

WORLD: The DNA wormhole opens the actual pocket dimension in which Ryan, his persistent quantum table and the crew operate. The small object-transfer seam is part of that network. The outside player, the pocket location and the access mechanism are distinct.
SHOW THE NOUN: a concrete spoken object, person, place or action is visibly represented during its phrase. Demonstrate physical receipt, actual work and actual return. Use generic inventory controls, not copied commercial artwork.
TRACK THE OBJECT: T1 is the original source-matched short-handled pick with a triangular head notch and one loose retaining pin. Its original pin is reseated, the same T1 returns and its inventory updates after receipt. T1 stays repaired thereafter. T2, near the end, is a clearly different incoming damaged tool with a different head silhouette, representing the next request.
A repair remains a repair. The separate gem-and-shaft request is assembly. No new factory is built for a service call.
A mechanical Ryan is already embodied inside the particular limited pocket; the script invents no conversion procedure, injury, death or universal ban on organic life. The organic customer outside remains unchanged.
The approved gear-driven body and living porcelain body both remain in the world. Porcelain repairs by gold emerging, ceramic regrowing, then gold withdrawing inside. Do not substitute a permanently gold-filled wound for this dynamic healing.
NO NEW ZIPPERS. Existing zipper imagery remains the owner's literal pocket joke. Use the established paired DNA access for new portal actions.
No montage of generic robot presentation, new lyrics, title-card lecture, reference-sheet slideshow, production-instruction voiceover or edit/stitching instructions is part of a render prompt.

PRESERVATION AND PROGRESS: Shakespeare is complete for Ryan's current production, by his declaration; preserve every existing screenplay, clip, render, image, receipt and daily. This is not a new render-count verification of all old footage. Later Shakespeare acts are dormant unless Ryan returns to them. The current job is this essay short.
The new dailies start as SCRIPTED / NO NEW RENDER RECEIVED IN THIS AUTHORING PASS. Authoring ninety frames is not a claim that ninety videos already exist.
The existing assignment carries across batches. Read the complete selected entry, then execute the next unperformed clip in order when Ryan runs the production. Do not insert a new approval loop between authorized clips or batches. A source lookup or 'check your orders' does not restart a completed batch.
The director handles assembly of the returned films. Each individual prompt contains only its own complete ten-second action.
"""
def norm(t): return " ".join(t.split())
assert norm(SOURCE) == norm(" ".join(c["text"] for c in speech)), "Source mismatch"
assert len(speech) == len(plans) == 84
assert all(len(c["text"].split()) <= 21 for c in speech)
for i, p in enumerate(plans, 1): assert p["speech_id"] == i
allclips=[]
silent_map={p["after_speech"]:p for p in silent}
def add_silent(k):
 if k in silent_map:
  p=dict(silent_map[k]);p.update(narration=None,source_speech=None,source_paragraph=None);allclips.append(p)
add_silent(0)
for i,(c,p) in enumerate(zip(speech,plans),1):
 d=dict(p);d.update(narration=c["text"],source_speech=i,source_paragraph=c["paragraph"]);allclips.append(d);add_silent(i)
assert len(allclips)==90
for n,c in enumerate(allclips,1):
 c["clip"]=n;c["batch"]=(n-1)//10+1;c["duration_seconds"]=10.0
 c["voice_seconds_estimate"]=round(len(c["narration"].split())*60/140,2) if c["narration"] else 0.0
 c["planned_speech_start"]=0.4 if c["narration"] else None
 c["planned_speech_end"]=round(0.4+c["voice_seconds_estimate"],2) if c["narration"] else None
 assert not c["narration"] or c["planned_speech_end"]<=9.4
def render_clip(c):
 cast="; ".join(characters[k] for k in c["cast"]) if c["cast"] else "NONE — an intentionally unoccupied view; no human, robot or marble person visible"
 frame=f"CLIP {c['clip']:03d} — 10.0 SECONDS\n"
 frame+=f"SOURCE: ESSAY paragraph {c['source_paragraph']:02d}, narration unit {c['source_speech']:03d}.\n" if c["narration"] else f"SOURCE: NONVOCAL — {c['title']}. No essay words assigned.\n"
 frame+=f"META FRAME — SELF-CONTAINED: 16:9 landscape cinematic moving film. LOCATION / WORLD: {worlds[c['world']]} CAST PRESENT: {cast}. VOICE: {VOICE if c['narration'] else 'NONE'}. A complete action is shown within this ten-second film.\n"
 frame+=f"REFERENCE — FORCE FIRST MODEL: Use Ryan's current standard pages 01–10 as supplied; select their pictured {c['reference_subject']}. Preserve the exact source faces, working bodies, material roles, props and set geometry. Create no new zipper.\n"
 if c["narration"]:
  frame+=f"TIMING: exactly 0.0–10.0 seconds. Narration starts about 0.4s; estimated finish {c['planned_speech_end']:.2f}s at natural 140 wpm. Use the remaining time for the assigned action and a settled result. Do not extend the film or alter the words.\n"
  frame+="PERFORMANCE / AUDIO: Ryan's clear, warm SPOKEN NARRATION; no singing or additional voices. Keep action sound and restrained instrumental underscoring below the words. The assistant/customer stays silent.\n"
  frame+="RYAN (NARRATION — VERBATIM):\n"+c["narration"]+"\n"
 else:
  frame+="TIMING: exactly 0.0–10.0 seconds. Let the complete scenic or physical action occupy the interval and settle naturally.\nPERFORMANCE / AUDIO: NO VOCALS. Only the actual environment/action sounds and restrained instrumental score; no invented spoken or sung text.\nNO VOCALS.\n"
 frame+="BACKGROUND / CAMERA: "+c["action"]+" CAMERA: "+c["camera"]+"\n"
 return frame
cliptexts=[render_clip(c) for c in allclips]
(OUT/"REFERENCE_POLICY.txt").write_text(reference_policy)
(OUT/"NARRATION_VERBATIM.txt").write_text(SOURCE+"\n")
words=[]
for c in allclips:
 words.append(f"CLIP {c['clip']:03d}\n"+("RYAN (spoken narration)\n"+c["narration"] if c["narration"] else "[NO VOCALS]"))
(OUT/"SCREENPLAY_WORDS_ONLY.txt").write_text("THE GUY IN THE POCKET — WORDS ONLY\n\n"+"\n\n".join(words)+"\n")
master=contract+"\n"+reference_policy+"\nBATCH INDEX\n"
for b in range(1,10):
 first=(b-1)*10+1;last=b*10
 master+=f"BATCH {b:02d} / CLIPS {first:03d}–{last:03d}: "+links.get(f"batch_{b:02d}",f"BATCH_{b:02d}_CLIPS_{first:03d}-{last:03d}.txt")+"\n"
master+="\nALL NINETY COMPLETE META FRAMES\n\n"+"\n".join(cliptexts)
(OUT/"THE_GUY_IN_THE_POCKET_META_MASTER.txt").write_text(master)
for b in range(1,10):
 first=(b-1)*10+1;last=b*10
 text=f"THE GUY IN THE POCKET — BATCH {b:02d} OF 09 — CLIPS {first:03d}–{last:03d}\n\n"
 text+="Every ten-second render is a complete, independently satisfying cinematic short film.\n"
 text+="Exactly ten films in this batch, each 10.0 seconds. Ryan's essay narration is verbatim, in order, spoken in one consistent voice. Explicit NO VOCALS entries are intentional films, not missing narration. Use the owner's current supplied standard reference pages 01–10; select each entry's pictured subjects. Only narration is performed. No new zippers or inherited Shakespeare lyrics.\n"
 if links.get("master"):text+="FULL MASTER: "+links["master"]+"\n"
 text+="\n"+"\n".join(cliptexts[first-1:last])
 text+=f"\nEND OF BATCH {b:02d} — COMPLETE THROUGH CLIP {last:03d}.\n"
 if b<9:text+=f"NEXT: BATCH {b+1:02d} / CLIPS {last+1:03d}–{last+10:03d}: "+links.get(f"batch_{b+1:02d}",f"BATCH_{b+1:02d}_CLIPS_{last+1:03d}-{last+10:03d}.txt")+"\n"
 else:text+="END OF THE COMPLETE SHORT. No further essay words or Shakespeare continuation are queued by this script.\n"
 text+="Resume the existing authorized assignment at the next undelivered clip; do not reset the counter or add an approval loop.\n"
 (OUT/f"BATCH_{b:02d}_CLIPS_{first:03d}-{last:03d}.txt").write_text(text)
ledger="# THE GUY IN THE POCKET — DAILIES\n\nPlanned: 90 ten-second films / nine batches / 15:00. Scripted entries are not rendered videos. Record actual returned files, actual duration and Ryan's verdict here. All previous Shakespeare dailies remain in their original files.\n\n| Clip | Batch | Words | Planned seconds | Status | Actual returned file | Actual seconds | Ryan verdict |\n|---|---|---|---|---|---|---|---|\n"
for c in allclips:
 ledger+=f"| {c['clip']:03d} | {c['batch']:02d} | {len(c['narration'].split()) if c['narration'] else 0} | 10.0 | SCRIPTED | — | — | — |\n"
(OUT/"DAILIES.md").write_text(ledger)
manifest={
"title":"The Guy in the Pocket","source":"Ryan's pasted essay body, November 7, 2026",
"source_sha256":hashlib.sha256(SOURCE.encode()).hexdigest(),"source_word_count":len(SOURCE.split()),
"clip_count":len(allclips),"narrated_clips":84,"nonvocal_clips":6,"batches":9,"seconds_per_clip":10,"planned_duration_seconds":900,
"narration_word_order_verified":norm(SOURCE)==norm(" ".join(c["narration"] for c in allclips if c["narration"])),
"voice_timing_status":"planning estimates; rendered audio not yet measured",
"reference_set":"owner-supplied standard pages 01–10; no guessed numeric subject mapping",
"nonperformed_metadata":"copied source title/link, separator and final META.md filing sentence retained in source/OWNER_QUOTED_SOURCE.txt",
"clips":allclips,"published_links":links}
(OUT/"PRODUCTION_MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
validation={"verbatim_word_order":manifest["narration_word_order_verified"],"source_words":len(SOURCE.split()),"total_clip_words":sum(len(c["narration"].split()) for c in allclips if c["narration"]),"max_words_per_clip":max(len(c["narration"].split()) for c in allclips if c["narration"]),"all_clips_exactly_ten_seconds":all(c["duration_seconds"]==10 for c in allclips),"every_batch_exactly_ten_clips":all(sum(c["batch"]==b for c in allclips)==10 for b in range(1,10)),"all_standard_frame_fields_present":all(all(k in t for k in ["META FRAME","REFERENCE","TIMING","PERFORMANCE / AUDIO","BACKGROUND / CAMERA"]) for t in cliptexts),"all_narration_estimates_within_ten_seconds":all(c["planned_speech_end"] is None or c["planned_speech_end"]<=9.4 for c in allclips),"no_extra_narration_in_nonvocal_clips":all(c["narration"] is None for c in allclips if c["source_speech"] is None),"missing_rendered_videos_falsely_claimed":False}
assert all(v for k,v in validation.items() if isinstance(v,bool) and k!="missing_rendered_videos_falsely_claimed")
(OUT/"VALIDATION.json").write_text(json.dumps(validation,indent=2)+"\n")
print(json.dumps({"clips":90,"batches":9,"runtime":"15:00","narration_words":len(SOURCE.split()),"validation":validation},indent=2))

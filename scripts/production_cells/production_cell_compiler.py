#!/usr/bin/env python3
"""Non-destructive TO WORLD 10-second dialogue-to-reference cell compiler.

Reads owner-provided JSON. Produces cells.csv, cells.json, verification.json.
Never edits inputs, never renders, never loads image bytes, never invents dialogue.
Python standard library only.
"""
import argparse
import csv
import hashlib
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

CLIP_MS = 10_000
WORD_RE = re.compile(r"\S+", re.UNICODE)
ALLOWED_MODES = {"draft", "timed"}


def fatal(message):
    raise ValueError(message)


def required_str(obj, key, context):
    val = obj.get(key)
    if not isinstance(val, str) or not val:
        fatal(f"{context}.{key} must be a nonempty string")
    return val


def read_config(filename):
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        fatal("Input root must be an object")
    return data


def validate(data, mode, wps):
    required_str(data, "project_id", "root")
    if not isinstance(data.get("visual_references"), list):
        fatal("visual_references must be a list (may be empty)")
    refs = {}
    for idx, r in enumerate(data["visual_references"]):
        ctx = f"visual_references[{idx}]"
        rid = required_str(r, "reference_id", ctx)
        if rid in refs: fatal(f"Duplicate reference ID {rid}")
        required_str(r, "original_image_uri", ctx)  # actual source, NOT fabricated example ID
        if r.get("status", "UNVERIFIED") not in {"VERIFIED", "UNVERIFIED"}:
            fatal(f"{ctx}.status must be VERIFIED or UNVERIFIED")
        if r.get("status") == "VERIFIED" and not r.get("approval_source"):
            fatal(f"{ctx} claims VERIFIED without approval_source")
        refs[rid] = r

    turns = data.get("turns")
    if not isinstance(turns, list): fatal("turns must be a list")
    ids = set()
    for i, turn in enumerate(turns):
        ctx = f"turns[{i}]"
        tid = required_str(turn, "turn_id", ctx)
        if tid in ids: fatal(f"Duplicate turn_id {tid}")
        ids.add(tid)
        if not isinstance(turn.get("text"), str): fatal(f"{ctx}.text must be an exact UTF-8 string")
        required_str(turn, "speaker_id", ctx)
        if not isinstance(turn.get("silent_listener_ids", []), list) or not all(isinstance(s,str) and s for s in turn.get("silent_listener_ids", [])):
            fatal(f"{ctx}.silent_listener_ids must be an array of approved character IDs")
        # There can be no inferred silent listener: unknown is [] and reported as NOT PROVIDED.
        if len(set(turn.get("silent_listener_ids", []))) != len(turn.get("silent_listener_ids", [])):
            fatal(f"{ctx}: duplicate listener")
        if turn["speaker_id"] in turn.get("silent_listener_ids", []):
            fatal(f"{ctx}: same character listed as speaking and silent")
        rid = required_str(turn, "frame_ref", ctx)
        if rid not in refs: fatal(f"{ctx}.frame_ref {rid} absent from visual_references")
        if turn.get("speaker_status", "UNVERIFIED") not in {"VERIFIED", "UNVERIFIED"}:
            fatal(f"{ctx}.speaker_status invalid")
        if turn.get("speaker_status") == "VERIFIED" and not turn.get("speaker_source"):
            fatal(f"{ctx} marks speaker VERIFIED without speaker_source")
        ls = turn.get("listener_status", "UNVERIFIED")
        if ls not in {"VERIFIED", "VERIFIED_NONE", "UNVERIFIED"}:
            fatal(f"{ctx}.listener_status must be VERIFIED, VERIFIED_NONE or UNVERIFIED")
        if ls == "VERIFIED" and not turn.get("silent_listener_ids"):
            fatal(f"{ctx} claims verified listeners but lists none")
        if ls == "VERIFIED_NONE" and turn.get("silent_listener_ids"):
            fatal(f"{ctx} claims no listeners but lists some")
        if ls.startswith("VERIFIED") and not turn.get("listener_source"):
            fatal(f"{ctx} claims listener status verified without listener_source")
        if turn.get("silent_listener_ids") and not turn.get("listener_source"):
            fatal(f"{ctx} lists silent listeners without a listener_source")
        context_keys=("the_tale", "the_fable", "the_journey", "time_to_frame", "frame_state")
        provided=[key for key in context_keys if turn.get(key) is not None]
        for key in provided:
            if not isinstance(turn[key], str): fatal(f"{ctx}.{key} must be a string")
        if provided and not turn.get("story_context_source"):
            fatal(f"{ctx}: story context present but story_context_source absent")
        if mode == "timed":
            units = turn.get("timed_units")
            if not isinstance(units, list): fatal(f"{ctx}.timed_units required in timed mode")
            if turn["text"] and not units: fatal(f"{ctx}.timed_units empty for nonempty text")
            end = 0
            for j, unit in enumerate(units):
                ux=f"{ctx}.timed_units[{j}]"
                for key in ("char_start", "char_end", "start_ms", "end_ms"):
                    if type(unit.get(key)) is not int or unit[key]<0: fatal(f"{ux}.{key} needs nonnegative integer")
                if unit["char_start"] != end or unit["char_end"] <= end:
                    fatal(f"{ux} does not cover original text sequentially at exact boundaries")
                if unit["end_ms"] <= unit["start_ms"]:
                    fatal(f"{ux} timestamp invalid")
                if j and unit["start_ms"] < units[j-1]["end_ms"]:
                    fatal(f"{ux} overlaps previous audio time")
                if not unit.get("timing_evidence"):
                    fatal(f"{ux} lacks time-aligned audio/cue evidence")
                end=unit["char_end"]
            if end != len(turn["text"]):
                fatal(f"{ctx}: units do not cover ALL original characters ({end}/{len(turn['text'])})")
    if mode == "timed":
        # Dialogue turns must stay in the owner's original order on the absolute timeline.
        prev_end = -1
        for turn in turns:
            for unit in turn.get("timed_units", []):
                if unit["start_ms"] < prev_end:
                    fatal("Timed units reorder/overlap source dialogue across turns")
                prev_end = unit["end_ms"]
    if mode == "draft" and (wps is None or not math.isfinite(wps) or wps <= 0):
        fatal("draft mode requires explicitly provided --wps (positive number); not verified timing")
    return refs


def draft_units(turns, wps):
    # Timing is only an estimate; it is never cleared for rendering.
    duration = 1000.0 / wps
    clock = 0.0
    all_units = []
    for turn in turns:
        source_text = turn["text"]
        matches = list(WORD_RE.finditer(source_text))
        last_end = 0
        if not matches:
            if source_text:
                # Whitespace-only text preserved, with no fabricated spoken duration.
                all_units.append({"turn_id": turn["turn_id"], "char_start":0,
                    "char_end":len(source_text), "start_ms":int(clock),"end_ms":int(clock),
                    "text":source_text, "timing_status":"ESTIMATED"})
            continue
        for j, match in enumerate(matches):
            # Include all preceding whitespace with each word so slices reconstruct exactly.
            start=last_end
            end=match.end()
            if j == len(matches)-1:
                end=len(source_text)
            last_end=end
            clip_end=(math.floor(clock / CLIP_MS)+1)*CLIP_MS
            if clock+duration > clip_end+1e-7:
                clock = float(clip_end)
            start_ms=int(round(clock))
            clock+=duration
            end_ms=int(round(clock))
            if end_ms > (start_ms // CLIP_MS +1)*CLIP_MS:
                # Precision guard: hold this unit, never assert precise placement.
                status="ESTIMATED_BOUNDARY_CONFLICT"
            else:
                status="ESTIMATED"
            all_units.append({"turn_id":turn["turn_id"],"char_start":start,"char_end":end,
                "start_ms":start_ms,"end_ms":end_ms,"text":source_text[start:end],
                "timing_status":status})
    return all_units


def timed_units(turns):
    all_units=[]
    for turn in turns:
        for u in turn.get("timed_units", []):
            all_units.append({"turn_id":turn["turn_id"],"char_start":u["char_start"],
                "char_end":u["char_end"],"start_ms":u["start_ms"],"end_ms":u["end_ms"],
                "text":turn["text"][u["char_start"]:u["char_end"]],
                "timing_evidence":u["timing_evidence"],"timing_status":"TIMED_EVIDENCE_DECLARED"})
    all_units.sort(key=lambda x:(x["start_ms"], x["end_ms"]))
    return all_units


def check_against_source_text(data, source_path):
    """Optional real-source check: every turn must equal an exact source span.

    No whitespace or punctuation normalization is performed.
    """
    if source_path is None:
        return {"original_document_checked":False,
                "original_document_match":None,
                "original_document_sha256":None}
    raw=Path(source_path).read_text(encoding="utf-8-sig")
    for turn in data["turns"]:
        pos=turn.get("source_span")
        if not isinstance(pos,dict):
            fatal(f"{turn['turn_id']} has no source_span; cannot verify original")
        a=pos.get("start_char");b=pos.get("end_char")
        if type(a) is not int or type(b) is not int or not (0<=a<=b<=len(raw)):
            fatal(f"{turn['turn_id']} has invalid source_span")
        if raw[a:b]!=turn["text"]:
            fatal(f"{turn['turn_id']} does not EXACTLY match source document at given offsets")
    return {"original_document_checked":True,"original_document_match":True,
            "original_document_sha256":hashlib.sha256(raw.encode("utf-8")).hexdigest()}


def compile_cells(data, mode, wps, source_path=None):
    refs=validate(data,mode,wps)
    original_check=check_against_source_text(data,source_path)
    turns={t["turn_id"]:t for t in data["turns"]}
    units=draft_units(data["turns"],wps) if mode=="draft" else timed_units(data["turns"])
    buckets=defaultdict(list)
    for unit in units:
        clip_no=unit["start_ms"]//CLIP_MS
        buckets[clip_no].append(unit)
    last_end_ms=max((u["end_ms"] for u in units), default=0)
    n_clips=max(max(buckets.keys(), default=-1)+1,math.ceil(last_end_ms/CLIP_MS))
    cells=[]
    per_turn=defaultdict(list)
    previous_frame_refs=[]
    boundary_carry=[]
    for clip_no in range(n_clips):
        start=clip_no*CLIP_MS; stop=start+CLIP_MS
        bu=buckets[clip_no]
        current_frame_refs=list(dict.fromkeys(turns[u["turn_id"]]["frame_ref"] for u in bu))
        frame_refs=current_frame_refs or previous_frame_refs
        if current_frame_refs: previous_frame_refs=current_frame_refs
        problems=["CARRYOVER_TIMING_UNRESOLVED:"+tid for tid in boundary_carry]
        boundary_carry=[]
        if mode=="draft": problems.append("TIMING_ESTIMATE_NOT_RENDER_VERIFIED")
        if len(frame_refs)>1: problems.append("MULTIPLE_FRAME_REFERENCES_REQUIRE_APPROVED_TRANSITION")
        for rid in frame_refs:
            if refs[rid].get("status", "UNVERIFIED")!="VERIFIED":
                problems.append("VISUAL_REFERENCE_UNVERIFIED:"+rid)
        segments=[]
        for u in bu:
            turn=turns[u["turn_id"]]
            if u["end_ms"]>stop:
                problems.append("SPEECH_UNIT_CROSSES_10S_BOUNDARY:"+u["turn_id"])
                boundary_carry.append(u["turn_id"])
            if turn.get("speaker_status","UNVERIFIED")!="VERIFIED":
                problems.append("SPEAKER_UNVERIFIED:"+turn["turn_id"])
            if turn.get("listener_status", "UNVERIFIED") == "UNVERIFIED":
                problems.append("SILENT_LISTENER_STATUS_UNVERIFIED:"+turn["turn_id"])
            segments.append({
                "turn_id":u["turn_id"],"speaker_id":turn["speaker_id"],
                "silent_listener_ids":turn.get("silent_listener_ids", []),
                "frame_ref":turn["frame_ref"],
                "start_char":u["char_start"],"end_char":u["char_end"],
                "dialogue_verbatim":u["text"],
                "local_start_ms":u["start_ms"]-start,
                "local_end_ms":u["end_ms"]-start,
                "time_status":u["timing_status"],
                "the_tale":turn.get("the_tale", ""),
                "the_fable":turn.get("the_fable", ""),
                "the_journey":turn.get("the_journey", ""),
                "time_to_frame":turn.get("time_to_frame", ""),
                "frame_state":turn.get("frame_state", ""),
                "story_context_source":turn.get("story_context_source", "")})
            per_turn[u["turn_id"]].append(u)
        # Combine adjacent units of one turn without altering a single character.
        compact=[]
        for seg in segments:
            if (compact and compact[-1]["turn_id"] == seg["turn_id"]
                and compact[-1]["end_char"] == seg["start_char"]
                and compact[-1]["local_end_ms"] <= seg["local_start_ms"]):
                previous=compact[-1]
                previous["dialogue_verbatim"] += seg["dialogue_verbatim"]
                previous["end_char"] = seg["end_char"]
                previous["local_end_ms"] = seg["local_end_ms"]
            else:
                compact.append(seg)
        segments=compact
        # Undeclared silent listeners are a metadata gap, not presumed absent.
        cell={"clip_id":f"CELL-{clip_no+1:04d}","absolute_start_ms":start,
            "absolute_end_ms":stop,"duration_ms":CLIP_MS,
            "frame_refs":frame_refs,"dialogue_segments":segments,
            "verification_status":"HOLD" if problems else "SOURCE_DECLARED_REVIEW",
            "issues":sorted(set(problems)),
            "source_project":data["project_id"]}
        cells.append(cell)
    failures=[]
    # Exact UTF-8 codepoint preservation of every turn, including punctuation and whitespace.
    for turn in data["turns"]:
        tid=turn["turn_id"]
        fragments=per_turn[tid]
        fragments.sort(key=lambda x:x["char_start"])
        merged="".join(x["text"] for x in fragments)
        if merged != turn["text"]:
            failures.append({"turn_id":tid,"reason":"VERBATIM_TEXT_MISMATCH_OR_MISSING"})
        for idx,frag in enumerate(fragments):
            if idx==0 and frag["char_start"]!=0:
                failures.append({"turn_id":tid,"reason":"MISSING_PREFIX"})
            if idx and frag["char_start"]!=fragments[idx-1]["char_end"]:
                failures.append({"turn_id":tid,"reason":"GAP_OR_DUPLICATE_OFFSETS"})
        if fragments and fragments[-1]["char_end"]!=len(turn["text"]):
            failures.append({"turn_id":tid,"reason":"MISSING_SUFFIX"})
        if not fragments and turn["text"]:
            failures.append({"turn_id":tid,"reason":"NO_UNITS_FOR_NONEMPTY_TURN"})
    if failures: fatal("Preservation check failed: "+json.dumps(failures,ensure_ascii=False))
    # All source words are present in order; only verified source text appears in dialogue_segments.
    source_integrity={t["turn_id"]:hashlib.sha256(t["text"].encode("utf-8")).hexdigest() for t in data["turns"]}
    report={"project_id":data["project_id"],"mode":mode,"fixed_clip_duration_ms":CLIP_MS,
        "timing_verified_by_compiler":False,
        "timing_notice":"Audio/cue timestamps are passed through, not independently authenticated" if mode=="timed" else "Estimated timing; never use as an exact render guarantee",
        "verbatim_character_preservation":True,"turn_sha256":source_integrity,
        "original_images_modified":False,"total_source_turns":len(turns),
        "total_cells":len(cells),"hold_cells":[c["clip_id"] for c in cells if c["issues"]],
        "no_creative_generation":True,
        **original_check,
        "caveat":"This verifier checks exact source copying and formal constraints, not semantic truth or actual image/audio authenticity."}
    return cells,report


def write_outputs(cells, report, directory):
    directory=Path(directory); directory.mkdir(parents=True,exist_ok=True)
    with open(directory/"cells.json","w",encoding="utf-8",newline="") as f:
        json.dump(cells,f,ensure_ascii=False,indent=2)
        f.write("\n")
    cols=["clip_id","absolute_start_ms","absolute_end_ms","duration_ms","frame_refs",
        "speaker_ids","silent_listener_ids","the_tale","the_fable","the_journey",
        "time_to_frame","frame_state","dialogue_verbatim","continuation",
        "verification_status","issues"]
    with open(directory/"cells.csv","w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=cols)
        writer.writeheader()
        for i,c in enumerate(cells):
            segs=c["dialogue_segments"]
            # Multiple speakers in a clip are recorded as separate segments in cells.json.
            continuation=""
            if i+1 <len(cells):
                subsequent=cells[i+1]["dialogue_segments"]
                if segs and subsequent and segs[-1]["turn_id"] == subsequent[0]["turn_id"]:
                    continuation=f"{segs[-1]['turn_id']}@char={segs[-1]['end_char']}"
            writer.writerow({"clip_id":c["clip_id"],"absolute_start_ms":c["absolute_start_ms"],
                "absolute_end_ms":c["absolute_end_ms"],"duration_ms":c["duration_ms"],
                "frame_refs":" | ".join(c["frame_refs"]),
                "speaker_ids":" | ".join(s["speaker_id"] for s in segs),
                "silent_listener_ids":" | ".join(",".join(s["silent_listener_ids"]) for s in segs),
                "the_tale":" | ".join(dict.fromkeys(s.get("the_tale", "") for s in segs if s.get("the_tale"))),
                "the_fable":" | ".join(dict.fromkeys(s.get("the_fable", "") for s in segs if s.get("the_fable"))),
                "the_journey":" | ".join(dict.fromkeys(s.get("the_journey", "") for s in segs if s.get("the_journey"))),
                "time_to_frame":" | ".join(dict.fromkeys(s.get("time_to_frame", "") for s in segs if s.get("time_to_frame"))),
                "frame_state":" | ".join(dict.fromkeys(s.get("frame_state", "") for s in segs if s.get("frame_state"))),
                "dialogue_verbatim":"".join(s["dialogue_verbatim"] for s in segs),
                "continuation":continuation,"verification_status":c["verification_status"],
                "issues":" | ".join(c["issues"])})
    with open(directory/"verification.json","w",encoding="utf-8",newline="") as f:
        json.dump(report,f,ensure_ascii=False,indent=2); f.write("\n")


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",help="Owner-source JSON (untouched)")
    parser.add_argument("--mode",choices=sorted(ALLOWED_MODES),required=True,
                        help="draft requires explicitly chosen WPS; timed requires evidence-aligned units")
    parser.add_argument("--wps",type=float,default=None,help="Words/sec for DRAFT ONLY; a nonauthoritative estimate")
    parser.add_argument("--out",required=True,help="New output folder")
    parser.add_argument("--source-text",default=None,
                        help="Real original UTF-8 transcript. If supplied, require exact source_span offsets for every turn.")
    args=parser.parse_args(argv)
    if args.mode!="draft" and args.wps is not None:
        parser.error("--wps is only valid in draft mode")
    try:
        data=read_config(args.input)
        cells,report=compile_cells(data,args.mode,args.wps,args.source_text)
        write_outputs(cells,report,args.out)
    except (ValueError,OSError,json.JSONDecodeError) as e:
        parser.exit(2,"ERROR — NOTHING GENERATED: "+str(e)+"\n")
    print(json.dumps({"output_folder":args.out,"cells":len(cells),
        "hold_cells":len(report["hold_cells"]),"timing_verified":False,
        "verbatim_preserved":report["verbatim_character_preservation"],
        "original_document_checked":report["original_document_checked"]},ensure_ascii=False))
    return 0

if __name__=="__main__":
    sys.exit(main())

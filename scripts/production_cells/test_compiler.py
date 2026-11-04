"""Self-contained synthetic tests, NOT production dialogue or visual canon."""
import copy
import unittest
from production_cell_compiler import compile_cells


def fixture():
    return {
        "project_id": "TEST_FIXTURE_NOT_CANON",
        "visual_references": [
            {"reference_id":"TEST_IMAGE","original_image_uri":"test://synthetic-only",
             "status":"VERIFIED","approval_source":"test synthetic fixture"}
        ],
        "turns": [{
            "turn_id":"T1", "speaker_id":"S1", "speaker_status":"VERIFIED",
            "speaker_source":"synthetic test fixture", "silent_listener_ids":[],
            "listener_status":"VERIFIED_NONE", "listener_source":"synthetic test fixture",
            "frame_ref":"TEST_IMAGE", "text":""
        }]
    }


class TestCompiler(unittest.TestCase):
    def test_verbatim_with_whitespace_unicode_repetitions_and_continuation(self):
        x=fixture()
        x["turns"][0]["text"]="  hello,   hello!  Élève 😊 — "*15+" Done.\n"
        cells, report=compile_cells(x,"draft",2.5)
        compiled="".join(seg["dialogue_verbatim"] for c in cells for seg in c["dialogue_segments"])
        self.assertEqual(compiled,x["turns"][0]["text"])
        self.assertGreater(len(cells),1)
        self.assertTrue(all(c["duration_ms"]==10000 for c in cells))
        self.assertTrue(all(c["verification_status"]=="HOLD" for c in cells))
        self.assertTrue(report["verbatim_character_preservation"])

    def test_multi_speaker_same_clip_separate_segments(self):
        x=fixture()
        x["turns"][0]["text"]="First. "
        second=copy.deepcopy(x["turns"][0]);second.update({"turn_id":"T2","speaker_id":"S2","text":"Second. "})
        x["turns"].append(second)
        cells,_=compile_cells(x,"draft",3)
        self.assertEqual(len(cells),1)
        self.assertEqual([s["speaker_id"] for s in cells[0]["dialogue_segments"]],["S1","S2"])

    def test_missing_reference_holds_only_affected_clip(self):
        x=fixture()
        x["visual_references"].append({"reference_id":"TEST_UNVERIFIED","original_image_uri":"test://synthetic-two","status":"UNVERIFIED"})
        x["turns"][0]["text"]="First. "*25
        second=copy.deepcopy(x["turns"][0]);second.update({"turn_id":"T2","text":"Second.","frame_ref":"TEST_UNVERIFIED"})
        x["turns"].append(second)
        cells,_=compile_cells(x,"draft",2.5)
        self.assertTrue(any("VISUAL_REFERENCE_UNVERIFIED:TEST_UNVERIFIED" in c["issues"] for c in cells))
        self.assertFalse(any("VISUAL_REFERENCE_UNVERIFIED:TEST_UNVERIFIED" in c["issues"] for c in cells if "TEST_UNVERIFIED" not in c["frame_refs"]))

    def test_timed_exact_coverage_and_no_reordering(self):
        x=fixture(); x["turns"][0]["text"]="Example test."
        x["turns"][0]["timed_units"]=[{"char_start":0,"char_end":13,"start_ms":1000,"end_ms":2500,"timing_evidence":"synthetic test cue"}]
        cells, report=compile_cells(x,"timed",None)
        self.assertEqual(cells[0]["verification_status"],"SOURCE_DECLARED_REVIEW")
        self.assertFalse(report["timing_verified_by_compiler"])
        self.assertEqual(cells[0]["dialogue_segments"][0]["dialogue_verbatim"],"Example test.")

    def test_cross_boundary_holds_no_guess(self):
        x=fixture(); x["turns"][0]["text"]="Span"
        x["turns"][0]["timed_units"]=[{"char_start":0,"char_end":4,"start_ms":9900,"end_ms":10100,"timing_evidence":"synthetic test cue"}]
        cells,_=compile_cells(x,"timed",None)
        self.assertTrue(any("CROSSES_10S_BOUNDARY" in issue for issue in cells[0]["issues"]))

    def test_timed_turn_order_must_be_consistent(self):
        x=fixture(); x["turns"][0]["text"]="A"
        x["turns"][0]["timed_units"]=[{"char_start":0,"char_end":1,"start_ms":5000,"end_ms":6000,"timing_evidence":"test"}]
        second=copy.deepcopy(x["turns"][0]);second.update({"turn_id":"T2","text":"B","timed_units":[{"char_start":0,"char_end":1,"start_ms":1000,"end_ms":2000,"timing_evidence":"test"}]})
        x["turns"].append(second)
        with self.assertRaises(ValueError):compile_cells(x,"timed",None)

if __name__=="__main__":unittest.main()

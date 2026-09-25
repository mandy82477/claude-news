"""Tests for scripts/ingest_gate.py — ingest 內容閘。

守的是：閘清單取自 run_tests.GATES（不另抄）、只挑內容類、新閘 check_log_handoffs
已登記進 GATES，且閘清單裡每支腳本都存在。
"""
import unittest

from tests._helpers import SCRIPTS_DIR, load_script_module

ig = load_script_module("ingest_gate")
rt = load_script_module("run_tests")


class TestSelection(unittest.TestCase):
    def test_selected_gates_are_content_subset_of_run_tests(self):
        names = [n for n, _ in ig.selected_gates(rt.GATES)]
        gate_names = [n for n, _ in rt.GATES]
        self.assertEqual(sorted(names), sorted(ig.CONTENT_GATES))
        for n in names:
            self.assertIn(n, gate_names, f"{n} 必須登記在 run_tests.GATES，ingest_gate 不另抄閘定義")
        self.assertEqual(names, [n for n in gate_names if n in ig.CONTENT_GATES], "順序照 GATES")

    def test_non_content_gates_excluded(self):
        names = {n for n, _ in ig.selected_gates(rt.GATES)}
        for n in ("check_rules.py", "check_arch_docs.py", "check_css_overrides.py", "check_workflow_paths.py"):
            self.assertNotIn(n, names)

    def test_every_content_gate_script_exists(self):
        for n in ig.CONTENT_GATES:
            self.assertTrue((SCRIPTS_DIR / n).exists(), n)

    def test_unregistered_content_gate_still_runs_last(self):
        picked = ig.selected_gates([("check_rules.py", "x"), ("check_feature_radar.py", "radar")])
        self.assertEqual(picked[0], ("check_feature_radar.py", "radar"))
        self.assertEqual(len(picked), len(ig.CONTENT_GATES))


if __name__ == "__main__":
    unittest.main()

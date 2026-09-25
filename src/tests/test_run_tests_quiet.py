"""run_tests.py 安靜模式（2026-09-24）：閘綠只印最後一行、閘紅印全文。

背景：run_tests.py 一次 2,000 多行輸出被 agent 整包讀進 context（Phase C 收尾 agent
單日 162k token）。安靜模式只影響「印多少」，不影響判定：失敗清單「  FAIL: …」與
各閘紅時的完整輸出必須原樣保留，gate_web_build.py 與 check_tests_on_stop.py 靠它們。
"""
import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "scripts" / "run_tests.py"


def _load():
    spec = importlib.util.spec_from_file_location("run_tests_mod", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestSummarize(unittest.TestCase):
    def setUp(self):
        self.mod = _load()

    def test_green_quiet_prints_only_last_line_with_script_name(self):
        out = self.mod.summarize("check_x.py", "line1\n\n狀態：✅ 通過\n\n", "", 0, verbose=False)
        self.assertEqual(out, "[check_x.py] 狀態：✅ 通過\n")

    def test_red_prints_full_output_even_when_quiet(self):
        """閘紅時消費端要看得到 FAIL／❌ 行——安靜模式不得吞掉。"""
        out = self.mod.summarize("check_x.py", "❌ 2 個阻斷級問題\n  FAIL: a\n狀態：❌\n", "warn\n", 1, verbose=False)
        self.assertIn("❌ 2 個阻斷級問題", out)
        self.assertIn("  FAIL: a", out)
        self.assertIn("warn", out)

    def test_verbose_prints_full_output_when_green(self):
        out = self.mod.summarize("check_x.py", "line1\n狀態：✅ 通過\n", "", 0, verbose=True)
        self.assertIn("line1", out)
        self.assertIn("狀態：✅ 通過", out)

    def test_green_quiet_with_empty_output(self):
        out = self.mod.summarize("check_x.py", "", "", 0, verbose=False)
        self.assertEqual(out, "[check_x.py] （無輸出）\n")

    def test_gate_list_scripts_exist(self):
        """GATES 登記的每支腳本都要存在——少一支等於那道閘靜默消失。"""
        for script, _ in self.mod.GATES:
            self.assertTrue((REPO_ROOT / "scripts" / script).exists(), script)


if __name__ == "__main__":
    unittest.main()

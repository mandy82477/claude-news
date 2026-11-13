"""Windows 預設主控台 cp950 下，腳本印 emoji 不可當掉（共用模組 scripts/console_safe.py）。

根因（2026-11-14 實測）：scan_expiring_deadlines.py 在 cp950 stdout 印「🟠 即將到期」拋
UnicodeEncodeError，每日 pipeline Step 3 的截止日複查本機靜默跳過。11-08 build_web 已修同類，
但修法只做在 build_web 內；同樣缺陷散在 40 餘支腳本。修法：抽 console_safe.make_console_safe()，
各腳本入口呼叫。

釘的情境：子程序以 PYTHONUTF8=0、PYTHONIOENCODING=cp950 跑「真實腳本入口」（複製到暫存根目錄，
夾具 wiki 含到期截止日），必須 exit 0 且不出現 UnicodeEncodeError。
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests._helpers import SCRIPTS_DIR


def _cp950_env():
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONUTF8", "PYTHONIOENCODING")}
    env.update({"PYTHONUTF8": "0", "PYTHONIOENCODING": "cp950"})
    return env


def _import_console_safe():
    sys.path.insert(0, str(SCRIPTS_DIR))
    try:
        import console_safe
        return console_safe
    finally:
        sys.path.remove(str(SCRIPTS_DIR))


class TestConsoleSafeModule(unittest.TestCase):
    def test_replaces_unencodable_instead_of_raising(self):
        cs = _import_console_safe()
        old = sys.stdout
        try:
            sys.stdout = io.TextIOWrapper(io.BytesIO(), encoding="cp950", errors="strict")
            with self.assertRaises(UnicodeEncodeError):
                print("🟠", flush=True)
            sys.stdout = stream = io.TextIOWrapper(io.BytesIO(), encoding="cp950", errors="strict")
            cs.make_console_safe()
            print("🟠 ≥ ok 中文")
            stream.flush()
            out = stream.buffer.getvalue().decode("cp950")
        finally:
            sys.stdout = old
        self.assertIn("ok 中文", out)
        self.assertIn("?", out)

    def test_stream_without_reconfigure_is_left_alone(self):
        cs = _import_console_safe()
        old = sys.stdout
        sys.stdout = io.StringIO()
        try:
            cs.make_console_safe()  # StringIO 沒有 reconfigure，不可拋
        finally:
            sys.stdout = old


class TestScanExpiringDeadlinesUnderCp950(unittest.TestCase):
    def test_emoji_report_does_not_crash(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "scripts").mkdir()
            (root / "wiki").mkdir()
            for n in ("scan_expiring_deadlines.py", "console_safe.py"):
                shutil.copy(SCRIPTS_DIR / n, root / "scripts" / n)
            (root / "wiki" / "feature-radar.md").write_text(
                "| **2026-11-12** | 測試事件 | 到期後 | 決定 |\n", encoding="utf-8")
            r = subprocess.run([sys.executable, str(root / "scripts" / "scan_expiring_deadlines.py"),
                                "--today", "2026-11-10"],
                               env=_cp950_env(), capture_output=True, cwd=d)
            err = r.stderr.decode("cp950", errors="replace")
            out = r.stdout.decode("cp950", errors="replace")
            self.assertNotIn("UnicodeEncodeError", err)
            self.assertEqual(r.returncode, 0, err[-600:])
            self.assertIn("即將到期", out)


if __name__ == "__main__":
    unittest.main()

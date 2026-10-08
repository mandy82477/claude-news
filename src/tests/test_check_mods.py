"""`scripts/check_mods.py`：何時跳過、何時真的驗。

跳過條件寫錯的兩種後果都不能接受：該驗時跳過＝mod 壞了沒人知道；不該驗時驗＝雲端或舊版
本機因環境差異紅燈，擋住 web build。
"""
import contextlib
import importlib.util
import io
import os
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("check_mods", REPO / "scripts" / "check_mods.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def quiet_main():
    with contextlib.redirect_stdout(io.StringIO()):
        return mod.main()


class TestCheckMods(unittest.TestCase):
    def test_version_parse(self):
        self.assertEqual(mod.version_of("2.1.278 (Claude Code)"), (2, 1, 278))
        self.assertLess(mod.version_of("2.1.278 (Claude Code)"), mod.MIN_VERSION)
        self.assertGreaterEqual(mod.version_of("2.1.288 (Claude Code)"), mod.MIN_VERSION)
        self.assertIsNone(mod.version_of("garbage"))

    def test_cloud_skips_without_running_claude(self):
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": "true"}), \
                mock.patch.object(mod, "_run", side_effect=AssertionError("不該執行 claude")):
            self.assertEqual(quiet_main(), 0)

    def test_old_version_skips(self):
        fake = mock.Mock(stdout="2.1.278 (Claude Code)", stderr="", returncode=0)
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": ""}), \
                mock.patch.object(mod.shutil, "which", return_value="claude"), \
                mock.patch.object(mod, "_run", return_value=fake) as run:
            self.assertEqual(quiet_main(), 0)
            self.assertEqual(run.call_count, 1)  # 只問了版本

    def test_new_version_runs_validate_and_test_and_fails_on_red(self):
        calls = []

        def fake_run(args, cwd=None):
            calls.append(args[1:3])
            if args[1] == "--version":
                return mock.Mock(stdout="2.1.290 (Claude Code)", stderr="", returncode=0)
            if args[1:3] == ["plugin", "test"]:
                return mock.Mock(stdout="1 fail", stderr="", returncode=1)
            return mock.Mock(stdout="ok", stderr="", returncode=0)

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": ""}), \
                mock.patch.object(mod.shutil, "which", return_value="claude"), \
                mock.patch.object(mod, "_run", side_effect=fake_run):
            self.assertEqual(quiet_main(), 1)
        self.assertIn(["plugin", "validate"], calls)
        self.assertIn(["plugin", "test"], calls)

    def test_turned_off_is_reported_as_skipped_not_passed(self):
        """2026-10-03：開關關著時舊版最後一行仍印「全過」，run_tests 安靜模式只印最後一行，跳過被說成通過。"""
        def fake_run(args, cwd=None):
            if args[1] == "--version":
                return mock.Mock(stdout="2.1.288 (Claude Code)", stderr="", returncode=0)
            if args[1:3] == ["plugin", "test"]:
                return mock.Mock(stdout="claude plugin test: hooks modules are turned off in this process", stderr="", returncode=1)
            return mock.Mock(stdout="ok", stderr="", returncode=0)

        buf = io.StringIO()
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": ""}),                 mock.patch.object(mod.shutil, "which", return_value="claude"),                 mock.patch.object(mod, "_run", side_effect=fake_run),                 contextlib.redirect_stdout(buf):
            self.assertEqual(mod.main(), 0)
        last = [ln for ln in buf.getvalue().splitlines() if ln.strip()][-1]
        self.assertIn("跳過", last)
        self.assertNotIn("全過", last)


if __name__ == "__main__":
    unittest.main()


    def test_runner_death_is_retried_but_real_failure_is_not(self):
        """執行器「ended without a report」重試至多 2 次；有 report 的紅燈一次就報。"""
        def make(responses):
            seq = iter(responses)
            def fake_run(args, cwd=None):
                if args[1] == "--version":
                    return mock.Mock(stdout="2.1.290 (Claude Code)", stderr="", returncode=0)
                if args[1:3] == ["plugin", "test"]:
                    return next(seq)
                return mock.Mock(stdout="ok", stderr="", returncode=0)
            return fake_run
        died = mock.Mock(stdout="(fail) the file did not load\n  its run ended without a report (exit code 9)", stderr="", returncode=1)
        ok = mock.Mock(stdout="5 pass\n0 fail", stderr="", returncode=0)
        real = mock.Mock(stdout="(fail) x\n  AssertionError", stderr="", returncode=1)
        n = len(list(mod.MODS.glob("*")))
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": ""}),                 mock.patch.object(mod.shutil, "which", return_value="claude"),                 mock.patch.object(mod, "_run", side_effect=make([died, ok] * n)):
            self.assertEqual(quiet_main(), 0)
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": ""}),                 mock.patch.object(mod.shutil, "which", return_value="claude"),                 mock.patch.object(mod, "_run", side_effect=make([died, died, died] * n)):
            self.assertEqual(quiet_main(), 1)
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_REMOTE": ""}),                 mock.patch.object(mod.shutil, "which", return_value="claude"),                 mock.patch.object(mod, "_run", side_effect=make([real, ok, ok] * n)) as run:
            self.assertEqual(quiet_main(), 1)
            self.assertEqual(sum(1 for c in run.call_args_list if c.args[0][1:3] == ["plugin", "test"]), n)

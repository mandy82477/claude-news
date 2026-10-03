"""`.claude/settings.json` 的 hook 指令在「跑測試的這台機器」上真的會擋。

為什麼要實際執行指令字串（2026-10-03）：hook 寫成 `python …`，雲端 runbook 規定
`PYTHON=python3`。雲端若沒有 `python`，hook 以 127 結束——PreToolUse 只有 exit 2 算擋，
其他非零都是「hook 出錯、照常放行」，等於靜默失效，而且沒人看得到。
本機反過來：`python3` 是 Microsoft Store 的假檔（exit 126）。所以指令改成
「先找 python、沒有才用 python3」的啟動式。

雲端每班都跑 `python3 scripts/run_tests.py`，本檔因此是「hook 在雲端擋得住」的
唯一機械證據：它用 bash 執行 settings.json 裡原樣的指令字串，看 exit code。
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SETTINGS = REPO / ".claude" / "settings.json"
LAUNCH = 'P=python; command -v python >/dev/null 2>&1 || P=python3; "$P" '


def _bash() -> str | None:
    """找 Claude Code 會用的那個 bash。Windows 上 PATH 裡的 bash.exe 可能是 WSL，不能用。"""
    if os.name != "nt":
        return shutil.which("bash")
    git = shutil.which("git")
    if not git:
        return None
    for up in Path(git).resolve().parents:
        cand = up / "bin" / "bash.exe"
        if cand.is_file():
            return str(cand)
    return None


def _hooks():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    for event, groups in data["hooks"].items():
        for g in groups:
            for h in g["hooks"]:
                yield event, g.get("matcher", ""), h["command"]


def _run(command: str, payload: dict, env_path: str | None = None) -> int:
    env = dict(os.environ, CLAUDE_PROJECT_DIR=str(REPO))
    if env_path is not None:
        env["PATH"] = env_path
    proc = subprocess.run(
        [_bash(), "-c", command], input=json.dumps(payload), capture_output=True,
        text=True, encoding="utf-8", env=env, cwd=str(REPO), timeout=60,
    )
    return proc.returncode


class TestSettingsShape(unittest.TestCase):
    def test_python_hooks_use_launcher(self):
        """裸 `python "…"` 在只有 python3 的環境會靜默失效。"""
        for event, matcher, cmd in _hooks():
            if ".py" in cmd:
                with self.subTest(event=event, cmd=cmd[-60:]):
                    self.assertTrue(cmd.startswith(LAUNCH), cmd)

    def test_referenced_hook_files_exist(self):
        for _, _, cmd in _hooks():
            if "$CLAUDE_PROJECT_DIR/" in cmd:
                rel = cmd.split("$CLAUDE_PROJECT_DIR/", 1)[1].split('"', 1)[0]
                with self.subTest(rel=rel):
                    self.assertTrue((REPO / rel).is_file())

    def test_shell_guards_cover_bash_and_powershell(self):
        groups = [m for e, m, c in _hooks() if e == "PreToolUse" and "block_" in c]
        self.assertTrue(groups)
        for m in groups:
            self.assertEqual(set(m.split("|")), {"Bash", "PowerShell"})


@unittest.skipIf(_bash() is None, "找不到 bash（Windows 需 Git for Windows）")
class TestHooksBlockForReal(unittest.TestCase):
    CASES = [
        ("block_claude_print.py", "claude -p hi", 2),
        ("block_claude_print.py", "claude --version", 0),
        ("block_git_add_all.py", "git add ./", 2),
        ("block_git_add_all.py", "git add wiki/", 0),
        ("block_destructive_git.py", "git stash", 2),
        ("block_destructive_git.py", "git push origin HEAD:master", 2),
        ("block_destructive_git.py", "git pull --rebase origin master", 0),
    ]

    def _cmd_for(self, script):
        for e, m, c in _hooks():
            if e == "PreToolUse" and script in c:
                return c
        self.fail(f"settings.json 沒掛 {script}")

    def test_settings_commands_exit_codes(self):
        for script, shell_cmd, want in self.CASES:
            with self.subTest(script=script, cmd=shell_cmd):
                payload = {"tool_name": "Bash", "tool_input": {"command": shell_cmd}, "cwd": str(REPO)}
                self.assertEqual(_run(self._cmd_for(script), payload), want)

    @unittest.skipIf(os.name == "nt", "Windows 無法只靠 PATH 造出「只有 python3」的環境")
    def test_launcher_falls_back_to_python3(self):
        """PATH 上只有 python3（雲端 Linux 的常見形狀）時，hook 仍要擋得住。"""
        with tempfile.TemporaryDirectory() as d:
            os.symlink(sys.executable, os.path.join(d, "python3"))
            payload = {"tool_name": "Bash", "tool_input": {"command": "claude -p hi"}}
            rc = _run(self._cmd_for("block_claude_print.py"), payload, env_path=d)
            self.assertEqual(rc, 2)


if __name__ == "__main__":
    unittest.main()

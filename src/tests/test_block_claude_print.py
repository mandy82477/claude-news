"""`.claude/hooks/block_claude_print.py`：`claude -p` 的命中／不命中。

CLAUDE.md「`claude -p` 任何情境一律禁止」在 2026-10-03 之前只有文字。本檔守兩邊：
各種包裝寫法都擋得到；只在字串裡提到、或 claude 的其他子指令不被誤擋。
"""
import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent.parent / ".claude" / "hooks" / "block_claude_print.py"
_spec = importlib.util.spec_from_file_location("block_claude_print", HOOK)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class TestBlockClaudePrint(unittest.TestCase):
    def test_blocks_wrapped_forms(self):
        for cmd in (
            "claude -p hi",
            "claude --print 'summarize'",
            "claude --print=json",
            "echo x | claude -p",
            "cd src && claude -p 'x' > out.txt",
            "npx @anthropic-ai/claude-code -p hi",
            "npx @anthropic-ai/claude-code@latest --print hi",
            '& "D:/tools/bin/claude.exe" -p hi',
            'bash -c "claude -p hi"',
            "powershell -Command \"claude -p 'x'\"",
            "out=$(claude -p hi)",
        ):
            with self.subTest(cmd=cmd):
                self.assertTrue(mod.is_claude_print(cmd))

    def test_allows_mentions_and_other_subcommands(self):
        for cmd in (
            "claude --version",
            "claude plugin validate -p .",
            "claude mcp list",
            "echo '別用 claude -p'",
            "grep -rn 'claude -p' src",
            "git commit -m 'block claude -p in hooks'",
            "python scripts/claude_report.py -p",
        ):
            with self.subTest(cmd=cmd):
                self.assertFalse(mod.is_claude_print(cmd))

    def test_main_exit_codes(self):
        def run(payload):
            old = sys.stdin, sys.stderr
            sys.stdin, sys.stderr = io.StringIO(json.dumps(payload)), io.StringIO()
            try:
                return mod.main()
            finally:
                sys.stdin, sys.stderr = old

        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": "claude -p x"}}), 2)
        self.assertEqual(run({"tool_name": "PowerShell", "tool_input": {"command": "claude -p x"}}), 2)
        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": "claude --help"}}), 0)
        self.assertEqual(run({"tool_name": "Read", "tool_input": {"command": "claude -p x"}}), 0)


if __name__ == "__main__":
    unittest.main()

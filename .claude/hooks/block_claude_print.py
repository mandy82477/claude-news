"""
PreToolUse hook: 擋下 `claude -p`／`claude --print`（非互動呼叫 Claude）。

為什麼：本專案沒有 `ANTHROPIC_API_KEY`，唯一合法的 LLM 路徑是 Claude session 直接執行
（CLAUDE.md「環境限制」）。`claude -p` 在無 key 環境下要嘛失敗、要嘛改走訂閱額度
在背景燒——兩種都不是使用者要的。2026-10-03 盤點：這條禁令在 hooks 與 scripts 內
沒有任何機械看守，只靠文字。

行為：tool_name 為 Bash／PowerShell 且指令裡有一段的程式是 `claude`（含 `claude.exe`、
`npx @anthropic-ai/claude-code`），引數帶 `-p`／`--print` → stderr 說明、exit 2。
解析錯誤一律放行（fail-open）。

不命中：`claude --version`、`claude plugin validate`、`claude mcp list`、只在字串裡提到的
字面（`echo "別用 claude -p"`、`grep 'claude -p'`、commit 訊息）。
程式碼裡呼叫 `claude -p` 的靜態掃描是另一道：`scripts/check_no_llm_calls.py`。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmdparse import basename, iter_commands  # noqa: E402

try:
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

TOOLS = {"Bash", "PowerShell"}
CLAUDE_BINS = {"claude", "claude.exe", "claude.cmd", "claude.ps1"}
NPX_PKGS = ("@anthropic-ai/claude-code",)
# 這些子指令自己有 `-p` 之類的旗標，不是 print 模式
SUBCOMMANDS = {"plugin", "plugins", "mcp", "config", "update", "doctor", "install",
               "migrate-installer", "setup-token", "auth", "agents", "upgrade"}

REASON = (
    "🚫 擋下 `claude -p`／`claude --print`。\n"
    "本專案沒有 ANTHROPIC_API_KEY，任何情境（command、skill、script、子程序、間接觸發）"
    "都不得以非互動方式呼叫 Claude；LLM 工作只能由當前 Claude session 直接做，"
    "要平行就用 Agent tool 派子 agent。\n"
    "規則：CLAUDE.md「環境限制」。"
)


def _claude_args(toks: list[str]) -> list[str] | None:
    prog = basename(toks[0])
    if prog in CLAUDE_BINS:
        return toks[1:]
    if prog in ("npx", "npx.cmd", "bunx", "pnpx"):
        for i, t in enumerate(toks[1:], start=1):
            if any(t == p or t.startswith(p + "@") for p in NPX_PKGS):
                return toks[i + 1:]
    return None


def is_claude_print(command: str) -> bool:
    for toks in iter_commands(command):
        args = _claude_args(toks)
        if args is None:
            continue
        first_pos = next((a for a in args if not a.startswith("-")), None)
        if first_pos in SUBCOMMANDS and args.index(first_pos) == 0:
            continue
        for a in args:
            if a in ("-p", "--print") or a.startswith("--print="):
                return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not isinstance(command, str) or not is_claude_print(command):
        return 0
    sys.stderr.write(REASON + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())

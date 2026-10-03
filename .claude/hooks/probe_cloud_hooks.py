"""
PreToolUse 被動探針（暫時）：證明雲端 session 真的會執行專案的 settings hook。

為什麼（2026-10-03，使用者選被動探針）：官方文件只說雲端讀得到 `.claude/settings.json`，
沒說會不會跑裡面的 hook。規則精簡（docs/hook-rule-slimming-2026-10-03.md）以「雲端也擋得住」
為前提，缺這個證據就一條都不能刪。

行為：`CLAUDE_CODE_REMOTE=true`（雲端，探針證據見 docs/cloud-runbooks/probe-workflow-tool-2026-09-13.md）
時，每個 session 第一次 Bash／PowerShell 呼叫前 append 一行到 `src/logs/task_scheduler.log`：
    [cloud hooks-probe ACTIVE <UTC>] settings hooks 在雲端執行（session <id 前 8 碼>）
雲端 routine 開跑時本來就會 commit 並 push 這個檔，所以下一班一過就能在 origin 看到。
恆 exit 0，任何錯誤都吞掉——探針不可影響流程。本機不寫。

格式刻意以 `[cloud ` 開頭：`scripts/daily_health_check.py` 判斷班次是否斷掉，是看 STARTED 行之後、
下一個 `[cloud` 行之前有沒有內容。本行寫在 PreToolUse（指令執行前），一定落在新班 STARTED 行
**之前**；若不以 `[cloud ` 開頭，會被算進上一班的區塊，讓一個中途死掉的上一班看起來有結果。
解析成 routine `hooks-probe`、狀態 `ACTIVE`，孤兒判定只看 STARTED，不受影響。

拿到證據後移除本檔與 settings.json 的掛載（見對照表文末）。
"""
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    try:
        if os.environ.get("CLAUDE_CODE_REMOTE", "").lower() != "true":
            return 0
        payload = json.load(sys.stdin)
        if payload.get("tool_name") not in ("Bash", "PowerShell"):
            return 0
        sid = str(payload.get("session_id") or "unknown")
        marker = Path(tempfile.gettempdir()) / f"claude-news-hooks-probe-{sid}"
        if marker.exists():
            return 0
        root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".")
        log = root / "src" / "logs" / "task_scheduler.log"
        if not log.is_file():
            return 0
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        text = log.read_text(encoding="utf-8", errors="replace")
        sep = "" if text.endswith("\n") or not text else "\n"
        with open(log, "a", encoding="utf-8", newline="\n") as f:
            f.write(f"{sep}[cloud hooks-probe ACTIVE {stamp}] settings hooks 在雲端執行（session {sid[:8]}）\n")
        marker.write_text(stamp, encoding="utf-8")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())

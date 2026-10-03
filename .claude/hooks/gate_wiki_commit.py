"""
PreToolUse hook（H9）: 內容閘紅時，不准把 wiki/ commit 進 master。

使用者 2026-10-03 裁決：閘紅就不 commit wiki，取代原本「閘紅照樣 commit、只跳過 web build」。
以前內容閘（scripts/ingest_gate.py）是主編自律在 ingest 收尾跑；紅了照樣 commit 的話，
紅燈內容就進了 master，修的人變成下一班。

行為：Bash／PowerShell 指令裡有 `git commit`，且
    1. 目前分支是 master／main 或 detached HEAD（雲端起跑形狀），且
    2. 這次 commit 會納入 wiki/ 底下的檔（已 staged，或同一行指令裡 `git add` 點名的路徑）
→ 跑 `scripts/ingest_gate.py`（約 3 秒）；exit 非 0 → stderr 印閘的摘要與處方、exit 2。

出口（刻意留的）：commit 到別的分支不擋——修不好時照 web-publish Step 3 停泊到
`cloud-daily-<日期>-unmerged`，成果不隨雲端容器消失，看門狗（daily_health_check.py）會提醒救回。

fail-open：閘本身跑不起來（缺檔、逾時、例外）→ 放行，不可把收尾卡死。
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmdparse import iter_git  # noqa: E402

try:
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

TOOLS = {"Bash", "PowerShell"}
PROTECTED = {"master", "main", "HEAD"}


def _root(payload: dict) -> Path | None:
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    if env and Path(env).is_dir():
        return Path(env)
    cwd = payload.get("cwd")
    return Path(cwd) if cwd and Path(cwd).is_dir() else None


def _git(root: Path, *args: str) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout if out.returncode == 0 else None


def _is_wiki(path: str) -> bool:
    p = path.replace("\\", "/").rstrip("/")
    while p.startswith("./"):
        p = p[2:]
    return p == "wiki" or p.startswith("wiki/") or "/wiki/" in p or p.endswith("/wiki")


def touches_wiki(command: str, staged: list[str]) -> bool:
    """已 staged 的檔，加上同一行指令裡 `git add` 點名的路徑（add 還沒執行，staged 看不到）。"""
    paths = list(staged)
    for g in iter_git(command):
        if g.sub in ("add", "stage"):
            paths += g.positionals()
    return any(_is_wiki(p) for p in paths)


def has_commit(command: str) -> bool:
    return any(g.sub == "commit" for g in iter_git(command))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not isinstance(command, str) or not has_commit(command):
        return 0
    root = _root(payload)
    if root is None:
        return 0
    branch = (_git(root, "rev-parse", "--abbrev-ref", "HEAD") or "").strip()
    if branch not in PROTECTED:
        return 0
    staged = (_git(root, "diff", "--cached", "--name-only") or "").splitlines()
    if not touches_wiki(command, staged):
        return 0
    gate = root / "scripts" / "ingest_gate.py"
    if not gate.is_file():
        return 0
    # 子程序 stdout 是 pipe：Windows 上 Python 預設用 cp950 編碼，閘一印 emoji 就 UnicodeEncodeError
    # 以 exit 1 結束——綠燈被誤判成紅燈。強制 UTF-8。
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    try:
        proc = subprocess.run([sys.executable, str(gate)], cwd=str(root), capture_output=True,
                              text=True, encoding="utf-8", errors="replace", timeout=50, env=env)
    except (OSError, subprocess.TimeoutExpired):
        return 0
    if proc.returncode == 0:
        return 0
    red = [ln for ln in proc.stdout.splitlines() if re.search(r"❌|FAIL|紅", ln)][:8]
    sys.stderr.write(
        "🚫 內容閘（scripts/ingest_gate.py）紅，不可把 wiki/ commit 進 master。\n"
        + "\n".join("  " + ln.strip() for ln in red) + "\n"
        "處方：跑 `python scripts/ingest_gate.py` 看全文，修失敗訊息指名的內容後重試；"
        "修不好照 .claude/skills/web-publish/SKILL.md Step 3 停泊到 `cloud-daily-<日期>-unmerged` 分支再 commit。"
        "不可改閘腳本或基線讓它變綠。\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())

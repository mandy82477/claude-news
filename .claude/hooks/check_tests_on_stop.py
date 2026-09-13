"""
Stop hook: 收工前檢查「程式改動是否測試綠」（開發完工定義第 1 條的機械化）。

規則來源：.claude/rules/dev-done.md。姊妹 hook check_rules_on_stop.py 看規則檔，
本檔看程式檔。

行為：
- git status --porcelain 取未 commit 檔案，只留 src/、scripts/、.claude/hooks/
  （排除 src/logs/ 與 data 快取 json）
- 沒有這類改動 → 放行
- 記號檔 .claude/.last-tests-ok（scripts/run_tests.py 全綠時寫入）比所有髒檔都新
  → 放行（測試已在改動後跑過）
- 否則實跑 python scripts/run_tests.py；exit 0 → 放行，否則輸出
  {"decision": "block", "reason": "..."} 附最後幾行輸出
- stdin JSON 的 stop_hook_active 為 true → 無條件放行（防無限迴圈）
- 任何錯誤或逾時 → 放行（Stop hook 壞掉不可把使用者卡死）
"""
import io
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HOOK_DIR = Path(__file__).resolve().parent
REPO_ROOT = HOOK_DIR.parent.parent
MARKER = REPO_ROOT / ".claude" / ".last-tests-ok"
RUN_TESTS = REPO_ROOT / "scripts" / "run_tests.py"

WATCH_PREFIXES = ("src/", "scripts/", ".claude/hooks/")
IGNORE_SUBSTRINGS = ("src/logs/", "gathered_items.json", "emitted_items.json", "seen_urls.json", "__pycache__")


def dirty_code_files() -> list[Path]:
    proc = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=REPO_ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=10,
    )
    files = []
    for line in proc.stdout.splitlines():
        if len(line) < 4:
            continue
        rel = line[3:].strip().split(" -> ")[-1].strip('"').replace("\\", "/")
        if not rel.startswith(WATCH_PREFIXES):
            continue
        if any(s in rel for s in IGNORE_SUBSTRINGS):
            continue
        files.append(REPO_ROOT / rel)
    return files


def tests_already_green(files: list[Path]) -> bool:
    if not MARKER.exists():
        return False
    marker_mtime = MARKER.stat().st_mtime
    for f in files:
        if f.exists() and f.stat().st_mtime > marker_mtime:
            return False
    return True


def main() -> int:
    try:
        try:
            data = json.load(sys.stdin)
        except (json.JSONDecodeError, OSError):
            data = {}
        if data.get("stop_hook_active"):
            return 0

        files = dirty_code_files()
        if not files or tests_already_green(files):
            return 0

        env = dict(os.environ, PYTHONUTF8="1")
        proc = subprocess.run(
            [sys.executable, str(RUN_TESTS)],
            cwd=REPO_ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=150, env=env,
        )
        if proc.returncode == 0:
            return 0
        lines = ((proc.stdout or "") + "\n" + (proc.stderr or "")).strip().splitlines()
        hits = [ln for ln in lines if ln.startswith(("FAIL", "ERROR", "❌", "Traceback")) or "FAILED" in ln]
        tail = "\n".join((hits or lines)[-12:])
        reason = (
            f"程式檔有未 commit 改動（{len(files)} 個）且 scripts/run_tests.py 未通過"
            f"（開發完工定義第 1 條，見 .claude/rules/dev-done.md）。修到綠再收工。\n"
            f"最後輸出：\n{tail}"
        )
        print(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())

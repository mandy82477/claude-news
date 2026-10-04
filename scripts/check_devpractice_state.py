# -*- coding: utf-8 -*-
"""check_devpractice_state.py — 最近一次 ingest 的 commit 之後，開發實務的狀態檔有沒有跟著進 git。

開發實務記者靠 `data/devpractice_state.json` 記「上次看到哪個 commit」與「候選處理到第幾行」。
這個檔每輪 ingest 都會被改（`devpractice_diff.py mark`），但它是 data 檔，收尾 commit 漏帶時
沒有任何東西會紅——下一輪就拿舊基準線重撿一遍，或雲端與本機各走各的。

檢查：找最近一個「在 wiki/log.md 新增 `## YYYY-MM-DD Ingest` 標題」的 commit，
從它（含）到 HEAD 之間必須有 commit 動過狀態檔。生效日之前的 ingest 不查。
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = "data/devpractice_state.json"
LOG = "wiki/log.md"
ENFORCE_FROM = "2026-10-05"
HEADING = r"^## [0-9]{4}-[0-9]{2}-[0-9]{2} Ingest"
_DATE = re.compile(r"^\+## (\d{4}-\d{2}-\d{2}) Ingest", re.MULTILINE)


def _git(*args: str, cwd: Path = ROOT) -> str:
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def latest_ingest_commit(cwd: Path = ROOT) -> tuple[str, str] | None:
    """回傳 (sha, 該 commit 新增的最新 ingest 日期)；找不到回 None。"""
    sha = _git("log", "-1", "--format=%H", "-G", HEADING, "--", LOG, cwd=cwd).strip()
    if not sha:
        return None
    dates = _DATE.findall(_git("show", "--format=", "--unified=0", sha, "--", LOG, cwd=cwd))
    return (sha, max(dates)) if dates else None


def check(cwd: Path = ROOT, enforce_from: str = ENFORCE_FROM) -> tuple[bool, str]:
    found = latest_ingest_commit(cwd)
    if found is None:
        return True, "找不到 ingest commit，略過"
    sha, date = found
    if date < enforce_from:
        return True, f"最近一次 ingest（{date}）早於生效日 {enforce_from}，不查"
    touched = _git("log", "--format=%h", f"{sha}^..HEAD", "--", STATE, cwd=cwd).split()
    if touched:
        return True, f"{date} ingest（{sha[:8]}）之後狀態檔已進 git（{touched[0]}）"
    return False, (f"{date} ingest（{sha[:8]}）之後沒有任何 commit 動過 {STATE}——"
                   "開發實務的基準線沒跟著收尾 commit 進去；把該檔與 data/devpractice-candidates.jsonl 補 commit")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ok, msg = check()
    print(("OK: " if ok else "FAIL: ") + "check_devpractice_state — " + msg)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""pipeline_lock.py — 每日 pipeline 的跨機互斥鎖（本機 /news-pipeline 與雲端 routine 共用）。

**為什麼需要：** `Step 0b：冪等閘` 只在開跑那一刻看「日報存不存在」。本機跑到一半時雲端班次
開跑（或反過來），兩邊都看到「還沒有」，各做一份日報與 wiki，後推的撞衝突、wiki 重複條目
要人工挑。兩台機器之間唯一共用的是 GitHub 遠端，所以鎖就放在遠端。

**機制：** 遠端分支 `pipeline-lock`，每次搶鎖／放鎖都是一筆空樹 commit，訊息記狀態：

    HELD <token> <holder> <target_date> <UTC 時間>
    RELEASED <token> <holder> <target_date> <UTC 時間>

搶鎖＝在目前的 tip 上接一筆 HELD 再一般推送（不 force）。兩邊同時搶時，後推的那邊不是
快轉、被 git 拒絕——git 的快轉檢查就是 compare-and-swap，不需要任何 force 或刪分支
（專案 hook 也禁止那些）。這個分支不是 master，推它不會觸發網站部署。

**逾時：** HELD 超過 3 小時（`STALE_HOURS`，與 news-console 的死班判準同值；一輪
pipeline 最壞約 2 小時）視為持有者已死，可以接手——崩潰沒放鎖最多卡 3 小時。

**防重做：** `--require-absent news/<日期>.md` 在搶到鎖後再看一次 origin/master：
別人可能在你過了冪等閘、搶到鎖之前剛做完並推上去。存在就放鎖並回 4（等同冪等中止）。

**權杖：** 搶到時把 token 寫進本 clone 的 `.git/pipeline-lock-token`（不進版控），
release 只放自己持有的鎖；鎖已被別人接手（逾時）時只清權杖不動遠端。

exit：0 取得（或無法驗證的 WARN 放行）｜1 別人持有中／搶輸｜4 日報已在 origin（應中止）
release／status 恆為 0。

用法：
    python scripts/pipeline_lock.py acquire --date 2026-10-08 [--require-absent news/2026-10-08.md]
    python scripts/pipeline_lock.py release
    python scripts/pipeline_lock.py status
"""
from __future__ import annotations

import argparse
import io
import os
import platform
import subprocess
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRANCH = "pipeline-lock"
REMOTE_REF = f"refs/remotes/origin/{BRANCH}"
STALE_HOURS = 3
REPO = Path(__file__).resolve().parent.parent


def _git(repo: Path, *args: str, stdin: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], input=stdin, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=60)


def _now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _iso(t: datetime) -> str:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def default_holder() -> str:
    where = "cloud" if os.environ.get("CLAUDE_CODE_REMOTE") == "true" else "local"
    return f"{where}@{platform.node() or 'unknown'}".replace(" ", "_")


def parse(message: str) -> dict | None:
    """鎖 commit 訊息 → {state, token, holder, date, at}；不是鎖訊息回 None。"""
    parts = message.strip().split()
    if len(parts) != 5 or parts[0] not in ("HELD", "RELEASED"):
        return None
    try:
        at = datetime.strptime(parts[4], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return {"state": parts[0], "token": parts[1], "holder": parts[2], "date": parts[3], "at": at}


def _token_file(repo: Path) -> Path:
    gd = _git(repo, "rev-parse", "--git-dir").stdout.strip()
    p = Path(gd)
    return (p if p.is_absolute() else repo / p) / "pipeline-lock-token"


def _fetch(repo: Path) -> tuple[str | None, str | None]:
    """抓遠端鎖分支。回 (tip, error)；分支不存在回 (None, None)。"""
    r = _git(repo, "fetch", "--quiet", "origin", f"+refs/heads/{BRANCH}:{REMOTE_REF}")
    if r.returncode != 0:
        err = (r.stderr or "").lower()
        if "couldn't find remote ref" in err or "could not find remote ref" in err:
            _git(repo, "update-ref", "-d", REMOTE_REF)
            return None, None
        return None, (r.stderr or "").strip()[:200] or f"git fetch exit {r.returncode}"
    tip = _git(repo, "rev-parse", "--verify", "--quiet", REMOTE_REF).stdout.strip()
    return (tip or None), None


def _state(repo: Path, tip: str | None) -> dict | None:
    if not tip:
        return None
    return parse(_git(repo, "log", "-1", "--format=%B", tip).stdout)


def _push_child(repo: Path, parent: str | None, message: str) -> tuple[str, str | None]:
    """在 parent（None＝新分支）上接一筆空樹 commit 並一般推送。
    回 ("ok"|"rejected"|"error", 新 sha 或錯誤訊息)。"""
    tree = _git(repo, "mktree", stdin="").stdout.strip()
    args = ["commit-tree", tree, "-m", message] + (["-p", parent] if parent else [])
    c = _git(repo, *args)
    if c.returncode != 0:
        return "error", (c.stderr or "").strip()[:200]
    sha = c.stdout.strip()
    p = _git(repo, "push", "--quiet", "origin", f"{sha}:refs/heads/{BRANCH}")
    if p.returncode == 0:
        _git(repo, "update-ref", REMOTE_REF, sha)
        return "ok", sha
    err = (p.stderr or "").lower()
    if "rejected" in err or "non-fast-forward" in err or "fetch first" in err:
        return "rejected", None
    return "error", (p.stderr or "").strip()[:200]


def _describe(st: dict, now: datetime) -> str:
    mins = int((now - st["at"]).total_seconds() // 60)
    return f"{st['holder']}（{st['date']}，{mins} 分鐘前開始）"


def acquire(repo: Path, date: str, holder: str | None = None, require_absent: str | None = None,
            now: datetime | None = None) -> int:
    now = now or _now()
    holder = (holder or default_holder()).replace(" ", "_")
    tip, err = _fetch(repo)
    if err:
        print(f"⚠️ pipeline 鎖：無法讀取遠端（{err}），無法驗證互斥，放行")
        return 0
    st = _state(repo, tip)
    tf = _token_file(repo)
    # 不做「本 clone 已持有就重入」：同一個 clone 上可能同時開兩個本機 session，共用權杖檔，
    # 重入會讓它們一起跑。自己上一輪崩潰留下的鎖，用 release 清掉或等逾時。
    if st and st["state"] == "HELD":
        if now - st["at"] < timedelta(hours=STALE_HOURS):
            hint = "；若是本 clone 上一輪崩潰留下的，跑 `pipeline_lock.py release` 清掉" if tf.exists() else ""
            print(f"🔒 pipeline 鎖：{_describe(st, now)} 持有中，本次中止（ABORTED: pipeline lock held by {st['holder']}）{hint}")
            return 1
        print(f"⚠️ pipeline 鎖：{_describe(st, now)} 逾 {STALE_HOURS} 小時未放，視為已死、接手")
    token = uuid.uuid4().hex[:12]
    status, info = _push_child(repo, tip, f"HELD {token} {holder} {date} {_iso(now)}")
    if status == "rejected":
        tip2, _ = _fetch(repo)
        st2 = _state(repo, tip2)
        who = _describe(st2, now) if st2 else "另一個執行者"
        print(f"🔒 pipeline 鎖：搶輸，{who} 剛取得，本次中止（ABORTED: pipeline lock held by {st2['holder'] if st2 else 'other'}）")
        return 1
    if status == "error":
        print(f"⚠️ pipeline 鎖：推送鎖失敗（{info}），無法驗證互斥，放行")
        return 0
    tf.write_text(f"{token} {holder} {date}\n", encoding="utf-8")
    print(f"✅ pipeline 鎖：已取得（{holder}，{date}）")
    if require_absent:
        _git(repo, "fetch", "--quiet", "origin", "master")
        if _git(repo, "cat-file", "-e", f"origin/master:{require_absent}").returncode == 0:
            print(f"⏹️ pipeline 鎖：{require_absent} 已在 origin/master（別的執行者剛做完），放鎖並中止（ABORTED: digest already exists）")
            release(repo, now=now)
            return 4
    return 0


def release(repo: Path, now: datetime | None = None) -> int:
    now = now or _now()
    tf = _token_file(repo)
    if not tf.exists():
        print("ℹ️ pipeline 鎖：本 clone 未持有，略過")
        return 0
    token, holder, date = (tf.read_text(encoding="utf-8").split() + ["?", "?", "?"])[:3]
    tip, err = _fetch(repo)
    if err:
        print(f"⚠️ pipeline 鎖：無法讀取遠端（{err}），鎖會在 {STALE_HOURS} 小時後逾時")
        return 0
    st = _state(repo, tip)
    if not st or st["state"] != "HELD" or st["token"] != token:
        print("ℹ️ pipeline 鎖：遠端的鎖已不是本 clone 持有（已放或已被接手），只清本機權杖")
        tf.unlink(missing_ok=True)
        return 0
    status, info = _push_child(repo, tip, f"RELEASED {token} {holder} {date} {_iso(now)}")
    if status == "ok":
        tf.unlink(missing_ok=True)
        print(f"🔓 pipeline 鎖：已放（{holder}，{date}）")
    else:
        print(f"⚠️ pipeline 鎖：放鎖推送失敗（{info or status}），鎖會在 {STALE_HOURS} 小時後逾時")
    return 0


def status(repo: Path, now: datetime | None = None) -> int:
    now = now or _now()
    tip, err = _fetch(repo)
    if err:
        print(f"⚠️ 無法讀取遠端（{err}）")
        return 0
    st = _state(repo, tip)
    if not st:
        print("🔓 無鎖")
    elif st["state"] == "RELEASED":
        print(f"🔓 空閒（上一輪：{st['holder']}，{st['date']}）")
    else:
        stale = now - st["at"] >= timedelta(hours=STALE_HOURS)
        print(f"🔒 {_describe(st, now)} 持有中" + ("（已逾時，可接手）" if stale else ""))
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="每日 pipeline 跨機互斥鎖")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("acquire")
    a.add_argument("--date", required=True)
    a.add_argument("--holder")
    a.add_argument("--require-absent")
    sub.add_parser("release")
    sub.add_parser("status")
    ns = ap.parse_args(argv)
    if ns.cmd == "acquire":
        return acquire(REPO, ns.date, ns.holder, ns.require_absent)
    if ns.cmd == "release":
        return release(REPO)
    return status(REPO)


if __name__ == "__main__":
    sys.exit(main())

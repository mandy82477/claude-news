#!/usr/bin/env python3
"""ingest_gate.py — wiki ingest 彙整後、宣告完成前的內容閘（主編自己跑、自己修）。

全套閘原本要到 Phase C web build（`scripts/gate_web_build.py`）才跑；那時主編已
收工，紅燈由修復迴圈的另一個執行者事後補。內容類的紅多半出在主編自己剛寫的檔
（feature-radar、index、log），在 ingest 當輪就擋下，修的人就是寫的人。

只跑內容類閘：閘定義（腳本名、標籤）與安靜模式的輸出規則一律取自
`scripts/run_tests.py` 的 GATES 與 summarize()，本檔只挑名字，不另抄一份。
另外印出存量基線／白名單檔相對 HEAD 的變動行數——把命中收進基線或白名單也能讓
閘轉綠，那種綠要在 commit 訊息交代理由。

用法：
    python scripts/ingest_gate.py --date 2026-09-25   # --date 只傳給 check_log_handoffs
    python scripts/ingest_gate.py --verbose           # 每道閘印全文

exit 0 全綠｜1 有閘紅
"""
from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
DATA = REPO_ROOT / "data"

# 內容類閘：吃 wiki/ 與 data/ 的當日寫入；執行順序照 run_tests.GATES
CONTENT_GATES = (
    "check_wiki_freshness.py",
    "check_feature_radar.py",
    "check_pending_markers.py",
    "check_hierarchy.py",
    "check_reader_language.py",
    "check_cell_limits.py",
    "check_tools_page.py",
    "check_log_handoffs.py",
)
DATED_GATES = {"check_log_handoffs.py"}  # 接受 --date 的閘
BASELINE_GLOBS = ("*baseline*.json", "*-allow.json")


def _load_run_tests():
    spec = importlib.util.spec_from_file_location("_run_tests_for_ingest_gate", SCRIPTS / "run_tests.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def selected_gates(gates: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """從 run_tests.GATES 挑出內容類，保留其順序與標籤；GATES 沒登記的內容閘排在最後。"""
    picked = [(name, label) for name, label in gates if name in CONTENT_GATES]
    known = {name for name, _ in picked}
    picked += [(name, name) for name in CONTENT_GATES if name not in known]
    return picked


def baseline_changes() -> list[tuple[str, int, int]]:
    """回傳 [(相對路徑, +行, -行)]：基線／白名單檔相對 HEAD 的變動（含未追蹤新檔）。"""
    files = sorted({p for g in BASELINE_GLOBS for p in DATA.glob(g)})
    if not files:
        return []
    rels = [p.relative_to(REPO_ROOT).as_posix() for p in files]
    out: list[tuple[str, int, int]] = []
    proc = subprocess.run(["git", "-C", str(REPO_ROOT), "diff", "--numstat", "HEAD", "--", *rels],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) == 3:
            add, rem, path = parts
            out.append((path, int(add) if add.isdigit() else 0, int(rem) if rem.isdigit() else 0))
    untracked = subprocess.run(["git", "-C", str(REPO_ROOT), "ls-files", "--others", "--exclude-standard", "--", *rels],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
    for path in untracked.stdout.splitlines():
        n = len((REPO_ROOT / path).read_text(encoding="utf-8", errors="replace").splitlines())
        out.append((path, n, 0))
    return [row for row in out if row[1] or row[2]]


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="wiki ingest 內容閘：彙整後、宣告完成前跑")
    ap.add_argument("--date", help="TARGET_DATE，傳給 check_log_handoffs")
    ap.add_argument("--verbose", "-v", action="store_true", help="每道閘印全文")
    a = ap.parse_args(argv)

    rt = _load_run_tests()
    red: list[str] = []
    for script, label in selected_gates(rt.GATES):
        path = SCRIPTS / script
        if not path.exists():
            print(f"WARN: {path} 不存在，跳過{label}")
            continue
        cmd = [sys.executable, str(path)]
        if a.date and script in DATED_GATES:
            cmd += ["--date", a.date]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        sys.stdout.write(rt.summarize(script, proc.stdout, proc.stderr, proc.returncode, a.verbose))
        if proc.returncode != 0:
            red.append(script)

    changes = baseline_changes()
    if changes:
        print("\n⚠️⚠️ 基線／白名單有變動，commit 訊息必須寫出理由（收進基線或白名單也會讓閘轉綠）：")
        for path, add, rem in changes:
            print(f"  {path}  +{add} -{rem}")
    else:
        print("基線／白名單：相對 HEAD 無變動")

    if red:
        print(f"❌ ingest_gate：{len(red)} 道內容閘紅（{'、'.join(red)}）——主編同輪修到綠才可進步驟 5")
        return 1
    print(f"✅ ingest_gate：{len(selected_gates(rt.GATES))} 道內容閘全綠")
    return 0


if __name__ == "__main__":
    sys.exit(main())

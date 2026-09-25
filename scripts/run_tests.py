#!/usr/bin/env python3
"""
run_tests.py — 執行 src/tests/ 下所有確定性單元測試（unittest discover）。

只用標準庫，不依賴 pytest 或任何第三方套件。

用法：
    python scripts/run_tests.py            # 安靜模式（預設）：每道閘只印最後一行，紅了才印全文
    python scripts/run_tests.py --verbose  # 舊行為：unittest 逐案例印、每道閘印完整報告

行為：
    全部通過 → exit 0
    任何失敗／錯誤 → 印出失敗案例清單，exit 1

為什麼預設安靜（2026-09-24）：本腳本一次輸出 2,000 多行（857 個測試逐案例一行、
check_rules 報告 680 行、各閘存量 WARN 清單），任何 agent 把它整包讀進 context 就是
50–60k token；今天 Phase C 收尾 agent 為此花了 162k。閘的消費端只需要 exit code 與
最後一行（cloud runbook 心跳、web-publish 摘要都是抄最後一行），失敗時才需要全文。
失敗清單格式「  FAIL: …」／「  ERROR: …」與各閘紅時的完整輸出維持不變——
scripts/gate_web_build.py 與 .claude/hooks/check_tests_on_stop.py 靠它們判定。

供 .claude/skills/web-publish/SKILL.md Step 4（建置 Web Reader）前置檢查呼叫：
測試失敗時視同 Step 4 失敗，跳過 web build 與 web commit。

跑完 unittest 後，依序執行下列機械閘（任一失敗都讓本腳本整體 exit 1）：
check_rules（規則一致性）、check_arch_docs（架構文件漂移）、check_weekly_ledger
（週報預告帳本）、check_wiki_freshness（新鮮度宣稱 × 歸因）、check_feature_radar
（radar 索引對帳）、check_pending_markers（懸置標記語法）、check_tools_page（決策表契約）、
check_hierarchy（子故事階層）、check_workflow_paths（GH Actions 指名路徑）、
check_reader_language（讀者語言閘）、check_cell_limits（字元上限閘）、check_skill_refs
（skill 指路完整性）、check_css_overrides（CSS 靜默覆寫）。
"""
import argparse
import io
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
SCRIPTS = REPO_ROOT / "scripts"
LAST_TESTS_OK = REPO_ROOT / ".claude" / ".last-tests-ok"

# (腳本檔名, 缺檔時的 WARN 說明) —— 執行順序即列表順序
GATES: list[tuple[str, str]] = [
    ("check_rules.py", "規則一致性檢查"),
    ("check_arch_docs.py", "架構文件漂移檢查"),
    ("check_weekly_ledger.py", "週報帳本檢查"),
    ("check_wiki_freshness.py", "wiki 新鮮度檢查"),
    ("check_feature_radar.py", "feature-radar 對帳"),
    ("check_pending_markers.py", "懸置標記語法檢查"),
    ("check_tools_page.py", "tools 決策表契約檢查"),
    ("check_hierarchy.py", "階層契約檢查"),
    ("check_workflow_paths.py", "workflow 路徑檢查"),
    ("check_reader_language.py", "讀者語言閘"),
    ("check_cell_limits.py", "字元上限機械閘"),
    ("check_skill_refs.py", "skill 指路完整性閘"),
    ("check_css_overrides.py", "CSS 覆寫閘"),
]


def summarize(name: str, stdout: str, stderr: str, returncode: int, verbose: bool) -> str:
    """決定一道閘要印什麼。

    verbose 或閘紅（returncode != 0）→ 原樣印全文（stdout＋stderr），消費端靠全文裡的
    FAIL／❌ 行判定；閘綠且安靜 → 只印「[腳本名] 最後一個非空行」。
    """
    if verbose or returncode != 0:
        out = "\n" + (stdout or "") + "\n"
        if stderr:
            out += stderr + "\n"
        return out
    lines = [ln for ln in (stdout or "").splitlines() if ln.strip()]
    last = lines[-1] if lines else "（無輸出）"
    return f"[{name}] {last}\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="跑全部單元測試與機械閘；預設安靜，--verbose 印全文")
    ap.add_argument("--verbose", "-v", action="store_true", help="unittest 逐案例印、每道閘印完整報告（舊行為）")
    args = ap.parse_args(argv)
    verbose = args.verbose

    # Windows 預設 console/file 編碼常是 cp950，日報與 wiki fixture 含大量中文
    # 與 emoji，非 UTF-8 環境下讀檔／print 會壞掉，故此處手動包一層 UTF-8 stream，
    # 不依賴 PYTHONUTF8 環境變數（設定它對已啟動的直譯器 stdout 編碼無效）。
    if hasattr(sys.stdout, "buffer"):
        stream = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    else:
        stream = sys.stdout

    if str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(SRC_DIR / "tests"), pattern="test_*.py", top_level_dir=str(SRC_DIR))

    # 安靜模式 verbosity=0：只有失敗才印 traceback；verbose 才逐案例印一行
    runner = unittest.TextTestRunner(stream=stream, verbosity=2 if verbose else 0)
    result = runner.run(suite)

    unit_ok = result.wasSuccessful()
    if unit_ok:
        stream.write(f"\nOK: {result.testsRun} 個測試案例全數通過\n")
    else:
        stream.write(f"\nFAILED: {len(result.failures)} 個失敗、{len(result.errors)} 個錯誤（共 {result.testsRun} 個案例）\n")
        for test, _ in result.failures:
            stream.write(f"  FAIL: {test}\n")
        for test, _ in result.errors:
            stream.write(f"  ERROR: {test}\n")
    stream.flush()

    gates_ok = True
    for script, label in GATES:
        path = SCRIPTS / script
        if not path.exists():
            stream.write(f"\nWARN: {path} 不存在，跳過{label}\n")
            stream.flush()
            continue
        proc = subprocess.run(
            [sys.executable, str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        stream.write(summarize(script, proc.stdout, proc.stderr, proc.returncode, verbose))
        stream.flush()
        if proc.returncode != 0:
            gates_ok = False

    all_ok = unit_ok and gates_ok
    if all_ok:
        # 全綠記號：.claude/hooks/check_tests_on_stop.py 用 mtime 比對，
        # 髒檔都比它舊就不必在每次 Stop 重跑整套測試（見 .claude/rules/dev-done.md）
        try:
            LAST_TESTS_OK.write_text("ok\n", encoding="utf-8")
        except OSError:
            pass
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

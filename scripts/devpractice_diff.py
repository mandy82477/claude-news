# -*- coding: utf-8 -*-
"""devpractice 記者的沉澱訊號源：上次看過之後，wiki 新增了什麼。

設計依據（2026-09-02 使用者裁決）：
- devpractice 不靠其他記者標 tag（跨記者耦合＝已知失效模式：主線 tag 規則明寫
  「漏填等於該節點不存在」）。他自己在各記者沉澱完之後 git diff 撿料，
  「什麼算 coding 相關」的判斷權單一歸他。
- 基準線不是「今天的 commit」——補跑、雲端／本機交錯、漏一天都會漏看。
  改記狀態檔（上次看到的 commit sha），每次 diff <上次sha>..HEAD，看完更新 sha。
  漏跑三天，下次自動補齊三天的量。
- 狀態檔與候選帳本都在 data/ 且必須隨 pipeline push——雲端與本機共用同一條基準線，
  不 commit 的話兩邊各自為政，基準線就斷了。

用法：
    python scripts/devpractice_diff.py show   # 印出上次以來 wiki/ 的新增行（依檔案分組）
    python scripts/devpractice_diff.py mark   # 把基準線推進到目前 HEAD
    python scripts/devpractice_diff.py pending  # 列出還沒寫進手冊的候選（不看日期，看游標）
    python scripts/devpractice_diff.py consume  # 把游標推到帳本尾端（處理完才跑）

失敗模式處理：
- 狀態檔缺失／sha 已不在歷史中（rebase、force push）→ 退回「48 小時前的 commit」
  當基準線（用 rev-list --before，不用 reflog——雲端 fresh clone 的 reflog 是空的）。
- 淺 clone（雲端容器）且 sha 不在本地 → 先 git fetch --shallow-since／--deepen 補歷史；
  補不到才退到 48 小時前或「本 clone 最舊 commit」，並印警告（show 輸出第二行）。
- diff 為空 → 印「無新增」，exit 0（無料是正常結果，不是錯誤）。
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATE = ROOT / "data" / "devpractice_state.json"
# log.md 是編輯部日誌、index.md 是路由層——都不是新聞內容，撿了只會混入雜訊
# coding-workflow-guide 是本記者自己寫的頁——不排除的話，今天寫進去的明天會被自己再撿一次
EXCLUDE = ("wiki/log.md", "wiki/index.md", "wiki/topics/coding-workflow-guide.md")
LEDGER = ROOT / "data" / "devpractice-candidates.jsonl"
MAX_LINES_PER_FILE = 120  # 單檔新增行上限，防單頁大改版灌爆輸出


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )


def _fallback_sha():
    r = _git("rev-list", "-1", "--before=48 hours ago", "HEAD")
    return r.stdout.strip() or None


def _is_shallow() -> bool:
    return _git("rev-parse", "--is-shallow-repository").stdout.strip() == "true"


def _oldest_sha():
    """本 clone 可見歷史的最舊 commit（淺 clone 的邊界 commit）。"""
    r = _git("rev-list", "--max-parents=0", "HEAD")
    lines = r.stdout.split()
    return lines[-1] if lines else None


def _has_commit(sha) -> bool:
    return bool(sha) and _git("cat-file", "-e", f"{sha}^{{commit}}").returncode == 0


def _deepen_for(sha, updated) -> bool:
    """淺 clone 裡狀態檔的 sha 不在本地時，先補歷史再放棄（不靜默換基準）。
    先 --shallow-since（狀態檔 updated 往前推 2 天，必含該 sha），不行再 --deepen。"""
    attempts = []
    try:
        dt = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        since = int(dt.timestamp()) - 2 * 86400
        attempts.append(["fetch", "-q", f"--shallow-since={since}", "origin"])
    except (TypeError, ValueError):
        pass
    attempts.append(["fetch", "-q", "--deepen=200", "origin"])
    for args in attempts:
        try:
            _git(*args)
        except OSError:
            return False
        if _has_commit(sha):
            return True
    return False


def _base_sha():
    """基準 sha 與來源。順序：
    1. 狀態檔 sha 在本 clone → "state"
    2. 淺 clone 且不在 → 嘗試補歷史取回 → "state-fetched"
    3. 非淺 clone（rebase／force push）→ 48 小時前 → "fallback-48h"
    4. 淺 clone 補不到 → 48 小時前（若有）否則本 clone 最舊 commit → "fallback-shallow-48h"／"fallback-shallow-oldest"
    非 "state" 系的來源，show() 一律印警告，讓雲端 log 看得出基準被降級。"""
    sha, updated = None, None
    if STATE.exists():
        try:
            data = json.loads(STATE.read_text(encoding="utf-8"))
            sha, updated = data.get("last_sha"), data.get("updated")
        except (json.JSONDecodeError, OSError, AttributeError):
            sha = None
    if _has_commit(sha):
        return sha, "state"
    shallow = _is_shallow()
    if sha and shallow and _deepen_for(sha, updated):
        return sha, "state-fetched"
    fb = _fallback_sha()
    if not shallow:
        return fb, "fallback-48h"
    if fb:
        return fb, "fallback-shallow-48h"
    return _oldest_sha(), "fallback-shallow-oldest"


def show():
    sha, origin = _base_sha()
    if not sha:
        print("⚠️ 找不到基準 commit（repo 太新？），無法 diff")
        return 1
    head = _git("rev-parse", "HEAD").stdout.strip()
    print(f"基準線：{sha[:10]}（{origin}）→ HEAD {head[:10]}")
    if origin not in ("state", "state-fetched"):
        print(f"⚠️ 基準線被降級（{origin}）：狀態檔記的 commit 不在本 clone 且補不到；"
              "基準線之前、狀態檔 sha 之後的 wiki 新增可能漏撈（不會重撈）。"
              "雲端請改用較深的 clone。")
    if sha == head:
        print("無新增（基準線已是 HEAD）")
        return 0
    r = _git("diff", f"{sha}..HEAD", "--unified=0", "--", "wiki/")
    if r.returncode != 0:
        print(f"⚠️ git diff 失敗：{r.stderr.strip()}")
        return 1
    current, buf, total = None, [], 0

    def flush():
        nonlocal buf
        if current and buf:
            shown = buf[:MAX_LINES_PER_FILE]
            print(f"\n## {current}（新增 {len(buf)} 行"
                  + (f"，只列前 {MAX_LINES_PER_FILE}" if len(buf) > MAX_LINES_PER_FILE else "")
                  + "）")
            for line in shown:
                print(line)
        buf = []

    for line in r.stdout.splitlines():
        if line.startswith("+++ b/"):
            flush()
            path = line[6:]
            # repo root 在 CLAUDE_NEWS 上一層，diff 標頭路徑帶 CLAUDE_NEWS/ 前綴——用 endswith 比對
            current = None if any(path.endswith(e) for e in EXCLUDE) else path
        elif line.startswith("+") and not line.startswith("+++") and current:
            text = line[1:].rstrip()
            if text.strip():
                buf.append(text)
                total += 1
    flush()
    if total == 0:
        print("無新增（wiki/ 內容無變化）")
    else:
        print(f"\n合計新增 {total} 行（不含 log.md／index.md）")
    return 0


def mark():
    head = _git("rev-parse", "HEAD").stdout.strip()
    if not head:
        print("⚠️ 取不到 HEAD")
        return 1
    STATE.parent.mkdir(parents=True, exist_ok=True)
    state = _load_state()
    state["last_sha"] = head
    state["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _save_state(state)
    print(f"基準線已推進：{head[:10]}")
    return 0


def _load_state() -> dict:
    if STATE.exists():
        try:
            data = json.loads(STATE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _ledger_lines() -> list[str]:
    if not LEDGER.exists():
        return []
    return [ln for ln in LEDGER.read_text(encoding="utf-8").splitlines() if ln.strip()]


def pending():
    """帳本裡游標之後的候選。游標記的是「已處理到第幾行」，不是日期——
    哪一週沒跑，下次照樣從上次停下的地方讀，不會落在七天窗外。"""
    lines = _ledger_lines()
    done = int(_load_state().get("consumed_lines") or 0)
    if done > len(lines):  # 帳本被截短（不該發生）→ 全部重讀，寧可重看不可漏看
        done = 0
    rest = lines[done:]
    print(f"候選帳本 {len(lines)} 行，已處理 {done} 行，待處理 {len(rest)} 行")
    for ln in rest:
        print(ln)
    return 0


def consume():
    n = len(_ledger_lines())
    state = _load_state()
    state["consumed_lines"] = n
    state["consumed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _save_state(state)
    print(f"候選游標已推到第 {n} 行")
    return 0


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    cmd = sys.argv[1] if len(sys.argv) > 1 else "show"
    if cmd == "show":
        return show()
    if cmd == "mark":
        return mark()
    if cmd == "pending":
        return pending()
    if cmd == "consume":
        return consume()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())

"""
PreToolUse hook: 擋下把「別的 session 宣告中的路徑」加進 commit。

死因（2026-09-13）：兩個 interactive session 共用同一個工作樹。其中一個被交代
「都 commit 和 push」，它跑 `git status` 看到滿滿的 `wiki/` 與 `weekly/`，合理地
判斷那是自己這輪的成果，就一起 add 了——實際上那是另一個 session 正在分兩步修
字元上限、還沒收尾的半成品。當天量測：兩個 session 的 commit 檔案集**重疊為零**，
它們本來就在做不相干的事；碰撞不是內容碰撞，是 **staging 碰撞**。

根因：`git add` 的粒度是路徑，所有權的粒度是「哪個 session 寫的」。兩者對不起來，
而人只看得到前者。`block_git_add_all.py` 擋的是 `-A`／`.`，指名路徑則一路放行——
今天這次正是指名路徑進來的。

做法：讓所有權變成機器讀得到的東西。session 進入寫入階段前宣告路徑前綴，
本 hook 在 `git add`／`git commit` 前算出 staged 路徑，落在「**別的、還活著的**
session 宣告範圍」內就擋下並指名是誰。

宣告檔：`.claude/tree-claims/<session_id>.json`（gitignore）
    {"session": "<id>", "paths": ["wiki/", "weekly/"], "note": "自由文字"}
心跳＝檔案 mtime。逾 `STALE_MINUTES` 視為過期，自動失效——**hook 壞掉或宣告沒清乾淨，
都不可以把樹卡死**，所以失效方向一律是「放行」。

刻意不解的問題（誠實標明射程）：
- 不防兩個 session 同時「編輯」同一個檔（lost update）。那要靠 worktree 隔離，
  本 hook 只管 staging。
- 沒宣告＝沒保護，但也不會誤擋。
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# 用 reconfigure 而不是 `sys.stderr = io.TextIOWrapper(sys.stderr.buffer, …)`：
# 後者每被 import 一次就多包一層，第一層被 GC 時會關掉底層 buffer。
# 實測：本檔與 block_git_add_all.py 同時被測試套件 import，全套 723 個案例
# 掛掉 54 個（logging handler 指向已關閉的 stream），單跑卻是綠的。
try:
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

TOOLS = {"Bash", "PowerShell"}
STALE_MINUTES = 90

# `git add` 或 `git commit`（含 -C <path> 之類的前置旗標）位於指令起點。
GIT_STAGE_RE = re.compile(
    r"(?:^|[;&|\n(`]|\bthen\b|\bdo\b)\s*"
    r"\bgit\b(?:\s+-[-\w]+(?:=\S+)?|\s+-C\s+\S+)*\s+(?:add|commit)\b"
)


def _norm(path: str) -> str:
    """統一成 repo 相對、正斜線、無 `./` 前綴的形式。

    不可用 `lstrip("./")`——那是字元集合去除，會把 `.claude/hooks/` 的開頭那個點
    一起吃掉變成 `claude/hooks/`，任何以點開頭的路徑都會被切錯。
    """
    p = str(path).replace("\\", "/")
    while p.startswith("./"):
        p = p[2:]
    return p


def _repo_root() -> Path | None:
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    if env and Path(env).is_dir():
        return Path(env)
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except Exception:
        pass
    return None


def _touched_paths(root: Path, command: str) -> list[str]:
    """這次 commit 會納入哪些檔案。

    `git add <路徑>` 尚未執行，所以除了已 staged 的內容之外，還要把這條指令
    點名的路徑一起算進來——否則 `git add wiki/ && git commit` 會在 add 當下
    看到空的 staged 清單而放行。
    """
    paths: set[str] = set()
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            cwd=str(root), capture_output=True, text=True, timeout=10,
        )
        if out.returncode == 0:
            paths |= {p.strip() for p in out.stdout.splitlines() if p.strip()}
    except Exception:
        pass
    for m in re.finditer(r"\bgit\b(?:\s+-[-\w]+(?:=\S+)?|\s+-C\s+\S+)*\s+add\b([^;&|\n)`]*)", command):
        for tok in m.group(1).split():
            if tok.startswith("-"):
                continue
            paths.add(_norm(tok.strip("'\"")))
    return sorted(p for p in paths if p)


def _live_foreign_claims(root: Path, my_session: str) -> list[dict]:
    d = root / ".claude" / "tree-claims"
    if not d.is_dir():
        return []
    cutoff = time.time() - STALE_MINUTES * 60
    out = []
    for f in sorted(d.glob("*.json")):
        try:
            if f.stat().st_mtime < cutoff:
                continue
            claim = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue  # 壞掉的宣告當作不存在，不卡人
        sid = str(claim.get("session") or f.stem)
        # 檔名與 session 欄任一對上就算自己的——寫宣告的人不見得知道自己的
        # session_id（那是 UUID，不是顯示名），兩條路都認可以少一個把自己
        # 鎖在門外的方式。真的鎖到了，擋下訊息會把 id 印給你。
        if my_session and my_session in (sid, f.stem):
            continue
        paths = [_norm(p) for p in (claim.get("paths") or [])]
        if paths:
            out.append({"session": sid, "paths": paths, "note": claim.get("note") or ""})
    return out


def _conflicts(touched: list[str], claims: list[dict]) -> list[tuple[str, str, str]]:
    hits = []
    for path in touched:
        for c in claims:
            for claimed in c["paths"]:
                if path == claimed.rstrip("/") or path.startswith(claimed.rstrip("/") + "/"):
                    hits.append((path, c["session"], c["note"]))
                    break
            else:
                continue
            break
    return hits


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not isinstance(command, str) or not GIT_STAGE_RE.search(command):
        return 0

    root = _repo_root()
    if root is None:
        return 0
    my_session = str(payload.get("session_id") or "")
    claims = _live_foreign_claims(root, my_session)
    if not claims:
        return 0
    hits = _conflicts(_touched_paths(root, command), claims)
    if not hits:
        return 0

    by_session: dict[str, list[str]] = {}
    notes: dict[str, str] = {}
    for path, sid, note in hits:
        by_session.setdefault(sid, []).append(path)
        if note:
            notes[sid] = note
    lines = ["🚫 這次 commit 會掃到別的 session 正在動的檔案，已擋下。"]
    for sid, paths in by_session.items():
        head = f"  · session {sid}"
        if notes.get(sid):
            head += f"（{notes[sid]}）"
        lines.append(head + " 宣告中：")
        for p in sorted(set(paths))[:12]:
            lines.append(f"      {p}")
        extra = len(set(paths)) - 12
        if extra > 0:
            lines.append(f"      …另 {extra} 個")
    lines.append(
        "修法：只 add 你自己這一輪真的動過的路徑。若確認對方已收工，"
        "刪掉 .claude/tree-claims/<session>.json 再重試（宣告逾 "
        f"{STALE_MINUTES} 分鐘無心跳會自動失效）。"
    )
    lines.append(
        f"若這些其實是你自己的檔案，代表宣告檔的 id 對不上——你這個 session 的 id 是 "
        f"`{my_session or '（未提供）'}`，把 .claude/tree-claims/ 下那份宣告的檔名或 "
        f"session 欄改成它即可。"
    )
    lines.append("立法依據：2026-09-13 兩個 session 共用工作樹，指名路徑 add 掃走對方半成品。")
    sys.stderr.write("\n".join(lines) + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())

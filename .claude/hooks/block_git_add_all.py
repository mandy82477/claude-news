"""
PreToolUse hook: 擋下 `git add -A` / `git add --all` / `git add .`。

為什麼要用 hook 而不是只寫在規則裡：這條規則必須**每次都發生**，而規則文字只在
agent 剛好記得時生效。2026-08-29 一個訊息為「fix: 目標日期取自耐久的 gathered_archive」
的 commit 掃走了同時間另一份工作的四個 wiki 檔——當事 session 不是不知道規則，
是沒想到自己正在違反它。

行為：
- 讀 stdin JSON；tool_name 為 Bash／PowerShell 且 tool_input.command 命中全加樣式
  → stderr 印一句指回規則、exit 2（PreToolUse 的 exit 2 = 拒絕該次工具呼叫）
- 其餘一律 exit 0 放行
- 任何解析錯誤 → exit 0（hook 壞掉不可把使用者卡死）

命中樣式（2026-10-03 改走 `_cmdparse.py` 的 token 解析；原 regex 版漏了 `./`、`"."`、
`-u`、`-c a=b`、`commit -a` 等寫法）：
    git add -A / --all / . / ./ / "." / :/ / * / ..      git add -u（無 pathspec）
    git -c a=b add .     git -C <path> add .     git stage .（stage 是 add 的別名）
    git commit -a / -am / --all       git commit -- .（pathspec 等於整棵樹）
    bash -c "git add ."（殼包一層也展開）     指名路徑其實就是 repo 根
不命中：`git add wiki/`、`git add ./scripts/x.py`、`git add -p`、`git add -u wiki/`、
    `git commit -m x`、以及只在字串或 heredoc 裡提到的字面（commit 訊息、echo、grep 的引數）
已知邊界（刻意不擋）：git alias、寫進腳本再執行、變數展開——靜態解析看不到
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmdparse import is_whole_tree_spec, iter_git  # noqa: E402

try:
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

TOOLS = {"Bash", "PowerShell"}

REASON = (
    "🚫 擋下全加寫法（`git add -A`／`.`／`./`／`-u`、`git commit -a` 等）。\n"
    "本專案一律指名路徑（如 `git add wiki/ .claude/`）——commit 訊息說不出某個檔案"
    "為什麼在裡面，它就不該在這個 commit 裡。\n"
    "規則與立法依據：.claude/rules/dev-done.md 第 2 條＋ docs/rules-changelog/CLAUDE.md 2026-08-29。"
)


def _is_root_path(spec: str, cwd: str | None) -> bool:
    """指名路徑其實就是 repo 根（`git add C:/…/CLAUDE_NEWS`）也算全加。"""
    if not cwd:
        return False
    try:
        root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd
        target = Path(spec) if Path(spec).is_absolute() else Path(cwd) / spec
        return target.resolve() == Path(root).resolve()
    except (OSError, ValueError):
        return False


def is_add_all(command: str, cwd: str | None = None) -> bool:
    for g in iter_git(command):
        if g.sub in ("add", "stage"):
            if g.has_flag("-A", "--all"):
                return True
            specs = g.positionals()
            if any(is_whole_tree_spec(s) or _is_root_path(s, cwd) for s in specs):
                return True
            if g.has_flag("-u", "--update") and not specs:
                return True
        elif g.sub == "commit":
            if g.has_flag("-a", "--all"):
                return True
            # `-m`/`-F`/`-C` 等吃引數的旗標，其引數不是 pathspec；只看 `--` 之後
            if "--" in g.args:
                after = g.args[g.args.index("--") + 1:]
                if any(is_whole_tree_spec(s) or _is_root_path(s, cwd) for s in after):
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
    if not isinstance(command, str) or not is_add_all(command, payload.get("cwd")):
        return 0
    sys.stderr.write(REASON + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())

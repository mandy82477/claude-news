"""
PreToolUse hook: 擋下會捲走共用工作樹或改寫遠端歷史的 git 指令。

死因：
- 2026-09-05 功能記者 `git stash` → `checkout stash@{0} -- 自己的檔` → `stash drop`，
  另外兩位記者已完成的三頁就此消失（docs/rules-changelog/reporter-shared.md）。
  當事記者真心以為「沒碰別人的檔」——`stash` 的作用域是整個工作區，從記者的視角看不見。
- 2026-09-29 雲端 17:00 班看到 detached HEAD 就臨場 `checkout -B master`／`push HEAD:master`，
  被 Auto Mode 判破壞性全擋、整班推不上去（docs/cloud-runbooks/_shared.md）。

邊界（2026-10-03 定；依據是規則原文「作用域是整個工作區」）：

所有 session（主 session 與子 agent）：
    git stash（list／show 以外）           任何 autostash（`--autostash`、`-c rebase.autostash=true`）
    git reset --hard／--merge／--keep        git clean（`-n`／`--dry-run` 以外）
    git checkout／restore 的 pathspec 是整棵樹（`.`、`:/`、`*`）    git checkout -f／switch -f／--discard-changes
    git push --force／-f／--force-with-lease／--mirror／`+refspec`  git push <非 master>:master（含 HEAD:master）
    git checkout -B master／switch -C master
子 agent 且在共用工作樹內（payload 有 `agent_id`、cwd 為專案根；`isolation: worktree` 的子 agent 不受此限）：
    另擋 checkout、switch、restore、reset、clean、pull、rebase、merge、cherry-pick、revert、am 全部寫法
    （規則：.claude/reporter-rules/shared.md「不可執行任何改動工作區全域狀態的 git 指令」）

刻意放行（主 session 的正當用途，管線本身會用到）：
    git checkout -- src/gathered_items.json（web-publish replay 還原，指名單檔）
    git pull --rebase origin master（push 重試；髒樹時 git 自己會拒絕，rebase.autoStash=false）
    git rebase --abort／--continue、git reset（mixed，只動 index）、git restore --staged
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
PROTECTED_BRANCHES = {"master", "main", "refs/heads/master", "refs/heads/main"}
SUBAGENT_BANNED = {"checkout", "switch", "restore", "reset", "clean", "pull", "rebase",
                   "merge", "cherry-pick", "revert", "am", "stash"}

WHY_SHARED = (
    "工作樹由多個 session／記者共用，這個指令的作用域是整個工作區，"
    "會連同別人當下正在寫的檔一起捲走。"
)


def _autostash(g) -> bool:
    for a in g.args:
        if a == "--autostash":
            return True
    for c in g.configs:
        k, _, v = c.partition("=")
        if k.lower().endswith(".autostash") and v.lower() in ("", "true", "yes", "on", "1"):
            return True
    return False


def _push_violation(g) -> str | None:
    if g.has_flag("--force", "--force-with-lease", "--mirror") or g.has_flag("-f"):
        return "force push 會改寫遠端歷史，雲端班與 GitHub Actions 的 commit 會被蓋掉。"
    refs = [a for a in g.positionals()]
    for r in refs[1:] if len(refs) > 1 else []:
        if r.startswith("+"):
            return "`+refspec` 等同 force push。"
        if ":" in r:
            src, dst = r.split(":", 1)
            if dst in PROTECTED_BRANCHES and src not in PROTECTED_BRANCHES:
                return (
                    f"`{r}` 把非 master 的 HEAD 直接推上 master。不在 master 上時照 "
                    "web-publish Step 5 推 `cloud-daily-<日期>-unmerged` 分支保住成果。"
                )
    return None


def violation(command: str, is_shared_subagent: bool = False) -> str | None:
    """回傳擋下理由；None＝放行。"""
    for g in iter_git(command):
        sub = g.sub
        if _autostash(g):
            return "autostash 背後就是 `git stash`。" + WHY_SHARED
        if is_shared_subagent and sub in SUBAGENT_BANNED:
            if sub == "stash" and g.args[:1] and g.args[0] in ("list", "show"):
                continue
            if sub == "clean" and g.has_flag("-n", "--dry-run"):
                continue
            return (
                f"子 agent 不可執行 `git {sub}`：commit 與還原屬主 session 收尾。" + WHY_SHARED
                + "遇到 git 狀態異常，在回報末尾寫「⚠️ 工作區異常：…」交主 session。"
            )
        if sub == "stash":
            if g.args[:1] and g.args[0] in ("list", "show"):
                continue
            return "`git stash` 會把整個工作區的未 commit 改動收走。" + WHY_SHARED
        if sub == "reset" and g.has_flag("--hard", "--merge", "--keep"):
            return "`git reset --hard` 丟棄整個工作區的未 commit 改動。" + WHY_SHARED
        if sub == "clean" and not g.has_flag("-n", "--dry-run"):
            return "`git clean` 永久刪除未追蹤檔（含別人剛建的新檔）。" + WHY_SHARED
        if sub in ("checkout", "restore"):
            if sub == "checkout" and g.has_flag("-f", "--force"):
                return "`git checkout -f` 丟棄整個工作區的改動。" + WHY_SHARED
            if sub == "checkout" and "-B" in g.args:
                i = g.args.index("-B")
                if i + 1 < len(g.args) and g.args[i + 1] in PROTECTED_BRANCHES:
                    return "`checkout -B master` 會把 master 強制指到目前 HEAD。照 web-publish Step 5 改推 unmerged 分支。"
            worktree = sub == "checkout" or not g.has_flag("--staged", "-S") or g.has_flag("--worktree", "-W")
            if worktree and any(is_whole_tree_spec(s) for s in g.positionals()):
                return f"`git {sub}` 的 pathspec 是整棵樹，會丟棄所有未 commit 改動。" + WHY_SHARED
        if sub == "switch":
            if g.has_flag("--discard-changes", "--force") or g.has_flag("-f"):
                return "`git switch --discard-changes` 丟棄整個工作區的改動。" + WHY_SHARED
            if "-C" in g.args:
                i = g.args.index("-C")
                if i + 1 < len(g.args) and g.args[i + 1] in PROTECTED_BRANCHES:
                    return "`switch -C master` 會把 master 強制指到目前 HEAD。"
        if sub == "push":
            why = _push_violation(g)
            if why:
                return why
    return None


def _is_shared_subagent(payload: dict) -> bool:
    if not payload.get("agent_id"):
        return False
    root = os.environ.get("CLAUDE_PROJECT_DIR")
    cwd = payload.get("cwd")
    if not root or not cwd:
        return True  # 判斷不了就當共用樹——子 agent 這端寧可嚴
    try:
        return Path(cwd).resolve() == Path(root).resolve()
    except (OSError, ValueError):
        return True


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not isinstance(command, str):
        return 0
    why = violation(command, _is_shared_subagent(payload))
    if not why:
        return 0
    sys.stderr.write(
        "🚫 擋下破壞性 git 指令。\n" + why + "\n"
        "規則：.claude/reporter-rules/shared.md「不可執行任何改動工作區全域狀態的 git 指令」、"
        ".claude/skills/web-publish/SKILL.md「push 失敗重試」。真的需要時請使用者自己在終端機執行。\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
repo_walk.py — 掃整個 repo（或其子樹）的檢查共用的「列檔」函式，排除巢狀 git worktree。

為什麼：Claude Desktop 會例行在 `.claude/worktrees/<名>/` 替其他 session 開 git worktree，
那是整個 repo 的一份副本（含 scripts/、.claude/、src/）。腳本用 `rglob` 掃 `.claude/` 或整個
repo 時會走進去，把副本裡的內容當成本 repo 的程式碼——check_no_llm_calls 因此誤報，
check_rules 的「basename 唯一命中」判斷因副本多一份而靜默失效。

判準（兩者並用）：
1. 子目錄含 `.git`（worktree 的 `.git` 是檔案、submodule 同；一般 clone 是資料夾）→ 它是另一個
   工作樹，不下探。比單獨排除路徑穩：app 改放別的位置也擋得住。
2. `.claude/worktrees/` 一律排除：worktree 被 prune 或半途失敗時 `.git` 檔可能不在，
   但目錄還在、內容仍是副本。
**不用 `git ls-files`**：各閘刻意要掃到尚未 git add 的新檔（只掃 tracked 檔是已知的洞）。
"""
from __future__ import annotations

import os
from pathlib import Path

ALWAYS_PRUNE = {".git", "__pycache__", "node_modules"}
WORKTREE_DIR_PARTS = (".claude", "worktrees")


def _is_worktrees_dir(root: Path, d: Path) -> bool:
    try:
        parts = d.relative_to(root).parts
    except ValueError:
        return False
    return parts[:2] == WORKTREE_DIR_PARTS


def is_nested_worktree(root: Path, p: Path) -> bool:
    """p（檔或目錄）是否落在巢狀 worktree 內（相對 root）。"""
    root = Path(root)
    p = Path(p)
    try:
        rel_parts = p.relative_to(root).parts
    except ValueError:
        return False
    if rel_parts[:2] == WORKTREE_DIR_PARTS:
        return True
    cur = root
    for part in rel_parts[:-1] if p.is_file() else rel_parts:
        cur = cur / part
        if (cur / ".git").exists():
            return True
    return False


def iter_files(base: Path, root: Path | None = None, suffixes: set[str] | None = None):
    """遞迴列 base 下的檔，剪掉巢狀 worktree。root 預設 base（base 自己有 .git 不算巢狀）。"""
    base = Path(base)
    root = Path(root) if root is not None else base
    if not base.is_dir():
        return
    for dirpath, dirnames, filenames in os.walk(base):
        here = Path(dirpath)
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in ALWAYS_PRUNE
            and not _is_worktrees_dir(root, here / d)
            and not (here / d / ".git").exists()
        )
        for name in sorted(filenames):
            p = here / name
            if suffixes is None or p.suffix.lower() in suffixes:
                yield p

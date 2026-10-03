#!/usr/bin/env python3
"""
check_no_llm_calls.py — 程式碼裡不得出現 `claude -p` 呼叫或 LLM SDK 匯入。

為什麼（2026-10-03）：CLAUDE.md「環境限制」禁止 `claude -p`（任何情境，含 script、
子程序、間接觸發）與「有 API key 才能運作」的功能，但當天盤點：hooks 與 scripts 內
沒有任何機械看守。`.claude/hooks/block_claude_print.py` 擋的是 session 當場下指令；
本閘擋的是「寫進程式碼、以後才執行」的那一半——那一半 hook 看不到。

掃描範圍：src/、scripts/、.github/、.claude/ 下的
    .py      AST：import anthropic／openai；字串常數以 `claude -p`／`claude --print` 開頭；
             list/tuple 字面首元素是 claude 且含 -p／--print
    .sh .ps1 .bat .cmd .yml .yaml   逐行（去註解、去 `run:` 前綴）交給 hook 同一套解析器
    .claude/settings*.json          hook 指令字串
不掃 .md（規則與文件會引用禁令本身）、資料 JSON（新聞內容會提到 `claude -p`）。

用法：python scripts/check_no_llm_calls.py
    無新命中 → exit 0（已知存量印 WARN）；有新命中 → 列出並 exit 1。
"""
from __future__ import annotations

import ast
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".claude" / "hooks"))
from block_claude_print import is_claude_print  # noqa: E402

SCAN_DIRS = ("src", "scripts", ".github", ".claude")
SKIP_PARTS = {"__pycache__", "gathered_archive", "fixtures", "node_modules", ".git"}
SHELL_EXT = {".sh", ".ps1", ".bat", ".cmd", ".yml", ".yaml"}
LLM_MODULES = {"anthropic", "openai"}

# 刻意含禁用字面的檔（測試資料本身就是要被擋的指令）
ALLOW: dict[str, str] = {
    "src/tests/test_block_claude_print.py": "hook 的測試案例：字面就是要被擋的指令",
    "src/tests/test_check_no_llm_calls.py": "本閘的測試案例",
    "src/tests/test_settings_hooks.py": "用 settings.json 原樣指令實跑 hook 的測試案例",
}
# 已知存量：不擋但每次印出，直到使用者裁決
KNOWN: dict[str, str] = {}  # 2026-10-03 analyzer.py 的 SDK 路徑經使用者裁決移除後清空

_CMD_STR_RE = re.compile(
    r"^\s*(?:npx\s+@anthropic-ai/claude-code\S*|claude(?:\.exe|\.cmd)?)\s+(?:.*\s)?(?:-p|--print)(?:\s|=|$)"
)
_COMMENT_RE = re.compile(r"^\s*(?:#|REM\b|::)", re.I)
_RUN_PREFIX_RE = re.compile(r"^\s*-?\s*run:\s*\|?\s*")
_CLAUDE_BINS = {"claude", "claude.exe", "claude.cmd"}


def scan_python(text: str) -> list[tuple[int, str]]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in LLM_MODULES:
                    hits.append((node.lineno, f"import {a.name}"))
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] in LLM_MODULES:
                hits.append((node.lineno, f"from {node.module} import …"))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            if _CMD_STR_RE.match(node.value):
                hits.append((node.lineno, f"指令字串：{node.value[:60]!r}"))
        elif isinstance(node, (ast.List, ast.Tuple)):
            vals = [e.value for e in node.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
            if vals and Path(vals[0]).name.lower() in _CLAUDE_BINS and any(v in ("-p", "--print") for v in vals):
                hits.append((node.lineno, f"指令陣列：{vals[:4]!r}"))
    return hits


def scan_shell(text: str) -> list[tuple[int, str]]:
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if _COMMENT_RE.match(line):
            continue
        line = _RUN_PREFIX_RE.sub("", line)
        if is_claude_print(line):
            hits.append((i, line.strip()[:80]))
    return hits


def scan_settings(text: str) -> list[tuple[int, str]]:
    try:
        data = json.loads(text)
    except ValueError:
        return []
    hits = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "command" and isinstance(v, str) and is_claude_print(v):
                    hits.append((0, v[:80]))
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    return hits


def iter_files(root: Path):
    for d in SCAN_DIRS:
        base = root / d
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if not p.is_file() or SKIP_PARTS & set(p.relative_to(root).parts):
                continue
            yield p


def scan(root: Path = ROOT) -> list[tuple[str, int, str]]:
    findings = []
    for p in iter_files(root):
        rel = p.relative_to(root).as_posix()
        if p.suffix == ".py":
            fn = scan_python
        elif p.suffix.lower() in SHELL_EXT:
            fn = scan_shell
        elif rel.startswith(".claude/settings") and p.suffix == ".json":
            fn = scan_settings
        else:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line, what in fn(text):
            findings.append((rel, line, what))
    return findings


def main() -> int:
    out = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace") if hasattr(sys.stdout, "buffer") else sys.stdout
    findings = scan()
    new = [f for f in findings if f[0] not in ALLOW and f[0] not in KNOWN]
    known = sorted({f[0] for f in findings if f[0] in KNOWN})
    for rel in known:
        out.write(f"WARN: 存量 {rel} — {KNOWN[rel]}\n")
    if new:
        out.write("❌ 程式碼出現 `claude -p` 呼叫或 LLM SDK 匯入（CLAUDE.md「環境限制」禁止）：\n")
        for rel, line, what in new:
            out.write(f"  {rel}:{line}  {what}\n")
        out.write("修法：改由 Claude session 直接執行；確屬誤判，在本檔 ALLOW 登記理由。\n")
        out.write(f"FAIL: check_no_llm_calls — {len(new)} 筆新命中\n")
        out.flush()
        return 1
    out.write(f"OK: check_no_llm_calls — 無新命中（存量 {len(known)} 檔待裁決）\n")
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

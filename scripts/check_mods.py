#!/usr/bin/env python3
"""
check_mods.py — 本機 mod（.claude/mods/*）的 `claude plugin validate --strict` 與 `claude plugin test`。

mod 是 TypeScript，單元測試不在 src/tests 的 unittest 裡；這道閘把它們接進 run_tests，
改 mod 的人跟改 Python 的人走同一條「測試綠才算完成」。

跳過（印 WARN、exit 0）而非紅燈的情況：
- 雲端 session（CLAUDE_CODE_REMOTE=true）：mod 只在本機載入，雲端驗它只會讓環境差異擋住 web build
- PATH 上沒有 claude，或版本低於 2.1.287（mods 的最低版本，官方 mods overview「Turn mods on or off」）
- `claude plugin test` 回報 hooks modules are turned off（該環境不允許載入 mod）

用法：python scripts/check_mods.py
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODS = ROOT / ".claude" / "mods"
MIN_VERSION = (2, 1, 287)


def _run(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=str(cwd) if cwd else None, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=300,
                          env=dict(os.environ, PYTHONIOENCODING="utf-8"))


def version_of(text: str) -> tuple[int, ...] | None:
    m = re.search(r"(\d+)\.(\d+)\.(\d+)", text)
    return tuple(int(x) for x in m.groups()) if m else None


def main() -> int:
    # reconfigure 而非另包 TextIOWrapper：後者被 GC 時會關掉底層 buffer，測試在同程序呼叫
    # main() 後整個 unittest runner 的輸出就死了（同 .claude/hooks/block_foreign_stage.py 的註解）
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    out = sys.stdout
    mods = sorted(p for p in MODS.glob("*") if (p / ".claude-plugin" / "plugin.json").is_file()) if MODS.is_dir() else []
    if not mods:
        out.write("OK: check_mods — 無本機 mod\n")
        return 0
    if os.environ.get("CLAUDE_CODE_REMOTE", "").lower() == "true":
        out.write(f"OK: check_mods — 雲端 session 跳過（{len(mods)} 個 mod 只在本機載入）\n")
        return 0
    claude = shutil.which("claude")
    if not claude:
        out.write("WARN: check_mods — PATH 上沒有 claude，跳過 mod 驗證\n")
        return 0
    ver = version_of(_run([claude, "--version"]).stdout)
    if not ver or ver < MIN_VERSION:
        have = ".".join(map(str, ver)) if ver else "未知"
        out.write(f"WARN: check_mods — Claude Code {have} < 2.1.287，mod 無法載入，跳過 {len(mods)} 個 mod 的驗證\n")
        return 0

    failed = []
    for mod in mods:
        rel = mod.relative_to(ROOT).as_posix()
        v = _run([claude, "plugin", "validate", "--strict", str(mod)])
        if v.returncode != 0:
            failed.append((rel, "validate --strict", v.stdout + v.stderr))
            continue
        t = _run([claude, "plugin", "test", str(mod)], cwd=mod)
        if "hooks modules are turned off" in (t.stdout + t.stderr):
            out.write(f"WARN: check_mods — {rel}：此環境不允許載入 mod，跳過 plugin test\n")
            continue
        if t.returncode != 0:
            failed.append((rel, "plugin test", t.stdout + t.stderr))
    if failed:
        for rel, step, text in failed:
            out.write(f"❌ {rel}：{step} 失敗\n{text}\n")
        out.write(f"FAIL: check_mods — {len(failed)} 個 mod 未過\n")
        return 1
    out.write(f"OK: check_mods — {len(mods)} 個 mod validate --strict 與 plugin test 全過\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

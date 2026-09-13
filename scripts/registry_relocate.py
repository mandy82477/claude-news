#!/usr/bin/env python3
"""
registry_relocate.py — 檔案搬家時一行指令改 .claude/review-registry.json 的路徑。

用法：
    python scripts/registry_relocate.py OLD_PATH NEW_PATH            # 改 registry
    python scripts/registry_relocate.py OLD_PATH NEW_PATH --dry-run  # 只列出會改什麼
    python scripts/registry_relocate.py OLD_PATH NEW_PATH --mv       # 另用 git mv 搬檔

做什麼：
  - registry 內所有「值恰等於 OLD_PATH」的字串（sync_pairs[].files、anchors、allowlist…）換成 NEW_PATH
  - pattern／_note 這類含有 OLD_PATH 片段但不是整值的字串**不改**，改印出來給人判斷
    （pattern 本身是檔名時才該改，registry 的 pattern 是 regex，機器不猜）
  - 輸出：改了幾處、哪幾組；需人判斷的 pattern 列表
  - 寫回時保持 indent=2、ensure_ascii=False，與現有格式一致

為什麼：2026-09-12～13 四批 skill 搬家，registry 100→117 組，每次搬檔都要人逐組改 files；
這件事是機械的，人只該判斷「這組約定還成不成立」。
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / ".claude" / "review-registry.json"


def _norm(p: str) -> str:
    return p.replace("\\", "/").strip()


def relocate(data: dict, old: str, new: str) -> tuple[int, list[str], list[str]]:
    """就地改 data；回傳 (改動數, 改動說明, 需人判斷的 pattern 說明)。"""
    old, new = _norm(old), _norm(new)
    old_base = old.rsplit("/", 1)[-1]
    old_base_rx = re.escape(old_base)  # pattern 裡的檔名長這樣：foo\.md
    changed: list[str] = []
    review: list[str] = []

    def needs_review(v: str) -> bool:
        # 整值不等於舊路徑、但內含完整舊路徑（_note、allowlist）或 regex 逃脫過的檔名（pattern）
        return old in _norm(v) or old_base_rx in v

    def walk(node, trail: str):
        nonlocal changed, review
        if isinstance(node, dict):
            for k, v in list(node.items()):
                if isinstance(v, str):
                    if _norm(v) == old:
                        node[k] = new
                        changed.append(f"{trail}.{k}")
                    elif needs_review(v):
                        review.append(f"{trail}.{k}: {v[:80]}")
                else:
                    walk(v, f"{trail}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                if isinstance(v, str):
                    if _norm(v) == old:
                        node[i] = new
                        changed.append(f"{trail}[{i}]")
                    elif needs_review(v):
                        review.append(f"{trail}[{i}]: {v[:80]}")
                else:
                    walk(v, f"{trail}[{i}]")

    for key, section in data.items():
        if key == "sync_pairs" and isinstance(section, list):
            for i, pair in enumerate(section):
                label = f"sync_pairs[{i}]〈{str(pair.get('name', ''))[:40]}〉"
                walk(pair, label)
        else:
            walk(section, key)
    return len(changed), changed, review


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    if len(args) != 2:
        print(__doc__)
        return 2
    old, new = args
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    n, changed, review = relocate(data, old, new)

    print(f"registry：{n} 處路徑 {old} → {new}")
    for c in changed:
        print(f"  - {c}")
    if review:
        print(f"需人判斷（含舊路徑或檔名片段的 pattern／備註，機器不改）：{len(review)} 處")
        for r in review:
            print(f"  ? {r}")

    if "--dry-run" in flags:
        print("dry-run：未寫檔")
        return 0
    if n:
        REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"已寫回 {REGISTRY.relative_to(ROOT)}")
    if "--mv" in flags:
        src, dst = ROOT / _norm(old), ROOT / _norm(new)
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "mv", str(src), str(dst)], cwd=ROOT, check=True)
            print(f"git mv {old} → {new}")
        else:
            print(f"WARN: {old} 不存在，未搬檔")
    print("接著跑：python scripts/check_rules.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

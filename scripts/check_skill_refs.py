#!/usr/bin/env python3
"""
check_skill_refs.py — skill 目錄的指路完整性機械閘。

用法：
    python scripts/check_skill_refs.py            # 掃 .claude/skills/*/
    python scripts/check_skill_refs.py --list     # 另印每個 skill 的行數／reference 清單

規格端：C:\\Users\\Mandy\\.claude\\SKILL-PRINCIPLES.md（skill 只寫步驟；模板／契約／判準放 references/；
目錄固定 references/ scripts/ assets/；description 100 字內；SKILL.md 沒寫「哪個檔裝什麼、何時讀」
第三層等於不存在）。本腳本是它的消費端，掛在 scripts/run_tests.py。

檢查五項（每個 .claude/skills/<name>/）：
  1. 有 SKILL.md，frontmatter 有 description，且 ≤ 100 字元
  2. 頂層只有 SKILL.md；子目錄只有 references/、scripts/、assets/
  3. SKILL.md 內提到的 references/… 路徑（相對或 .claude/skills/<name>/references/…）都存在
  4. references/ 裡每個檔至少被自己的 SKILL.md 指到一次（否則是孤兒，agent 永遠不會讀）
  5. SKILL.md ≤ 500 行

例外：EXEMPT 內的 skill（外部匯入的設計系統、單檔 skill）跳過 1（長度）與 2；仍做 3–5。
exit 0 = 全過；1 = 有違規（逐條印「skill:問題」）。
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"

DESC_MAX = 100
LINES_MAX = 500
ALLOWED_DIRS = {"references", "scripts", "assets"}
# 外部匯入或使用者親定形狀的 skill：不套目錄與 description 長度規則
EXEMPT = {"claude-news-llm-wiki-design", "page-audit-review"}

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.S)
DESC_RE = re.compile(r"^description:\s*(.*)$", re.M)


def frontmatter_description(text: str) -> str | None:
    m = FM_RE.match(text)
    if not m:
        return None
    d = DESC_RE.search(m.group(1))
    if not d:
        return None
    val = d.group(1).strip()
    if val.startswith(("'", '"')) and val.endswith(("'", '"')) and len(val) >= 2:
        val = val[1:-1]
    return val


def check_skill(skill_dir: Path) -> list[str]:
    name = skill_dir.name
    problems: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{name}: 缺 SKILL.md"]
    text = skill_md.read_text(encoding="utf-8-sig")
    exempt = name in EXEMPT

    # 1. description
    desc = frontmatter_description(text)
    if desc is None:
        problems.append(f"{name}: SKILL.md frontmatter 缺 description（description 是觸發器）")
    elif not exempt and len(desc) > DESC_MAX:
        problems.append(f"{name}: description {len(desc)} 字，超過 {DESC_MAX}")

    # 5. 行數
    n_lines = len(text.splitlines())
    if n_lines > LINES_MAX:
        problems.append(f"{name}: SKILL.md {n_lines} 行，超過 {LINES_MAX}")

    # 2. 目錄形狀
    if not exempt:
        for child in sorted(skill_dir.iterdir()):
            if child.is_dir():
                if child.name not in ALLOWED_DIRS:
                    problems.append(f"{name}: 子目錄 {child.name}/ 不在 references/ scripts/ assets/ 之內")
            elif child.name != "SKILL.md":
                problems.append(f"{name}: 頂層多了 {child.name}（reference 放 references/）")

    # 3. SKILL.md 指到的 references/ 都存在
    #    `.claude/skills/<other>/references/x.md` 是跨 skill 引用，算在 <other> 頭上；
    #    裸的 `references/x.md`（前面不是 `/`）才是本 skill 的。
    refs_dir = skill_dir / "references"
    mentioned: set[str] = set()
    full_re = re.compile(r"\.claude/skills/([A-Za-z0-9_\-]+)/references/([A-Za-z0-9_.\-]+\.md)")
    for m in full_re.finditer(text):
        owner, fname = m.group(1), m.group(2)
        if owner != name:
            if not (SKILLS / owner / "references" / fname).exists():
                problems.append(f"{name}: SKILL.md 指到 .claude/skills/{owner}/references/{fname}，檔不存在")
            continue
        mentioned.add(fname)
        if not (refs_dir / fname).exists():
            problems.append(f"{name}: SKILL.md 指到 references/{fname}，檔不存在")
    stripped = full_re.sub("", text)  # 剩下的裸 references/x.md 才是本 skill 的相對引用
    for m in re.finditer(r"(?<![/\w])references/([A-Za-z0-9_.\-]+\.md)", stripped):
        fname = m.group(1)
        mentioned.add(fname)
        if not (refs_dir / fname).exists():
            problems.append(f"{name}: SKILL.md 指到 references/{fname}，檔不存在")

    # 4. references/ 裡沒有孤兒
    if refs_dir.exists():
        for f in sorted(refs_dir.glob("*.md")):
            if f.name not in mentioned:
                problems.append(f"{name}: references/{f.name} 沒被 SKILL.md 指到（孤兒，agent 不會讀）")

    return problems


def _use_utf8_stdout() -> None:
    """Windows 主控台預設 cp950，訊息含 ≤ 與中文會 UnicodeEncodeError。只在 main() 呼叫，
    不放模組層級（見 src/tests/test_script_stdout_hygiene.py）。"""
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def main(argv: list[str]) -> int:
    _use_utf8_stdout()
    if not SKILLS.exists():
        print("OK: 無 .claude/skills/，跳過")
        return 0
    dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    problems: list[str] = []
    for d in dirs:
        problems.extend(check_skill(d))
        if "--list" in argv:
            md = d / "SKILL.md"
            n = len(md.read_text(encoding="utf-8-sig").splitlines()) if md.exists() else 0
            refs = sorted(p.name for p in (d / "references").glob("*.md")) if (d / "references").exists() else []
            print(f"  {d.name:<32} SKILL.md {n:>3} 行  references: {', '.join(refs) or '—'}")
    if problems:
        print(f"skill 指路完整性：{len(problems)} 筆違規（{len(dirs)} 個 skill）")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"OK: skill 指路完整性 — {len(dirs)} 個 skill 全過（description ≤{DESC_MAX} 字、目錄形狀、references 無孤兒無斷鏈、≤{LINES_MAX} 行）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

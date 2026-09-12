#!/usr/bin/env python3
"""
check_reader_digest.py — 讀者版日報（daily/YYYY-MM-DD.md）格式閘。

用法：
    python scripts/check_reader_digest.py [YYYY-MM-DD]   # 指定日期
    python scripts/check_reader_digest.py                # 掃全部 daily/*.md

由 `.claude/skills/reader-digest/SKILL.md` 第 4 步呼叫。
規格（節名、三段式、無新知行）住該步的「機械契約字串」表，本腳本是它的消費端；
兩端互相指認並登記於 .claude/review-registry.json 的 sync_pairs。

檢查六項：
  1. 標題行 `# YYYY-MM-DD 今天 wiki 學到什麼`，日期與檔名一致
  2. h2 節名必須是六個領域之一（拼錯的節名整段會在網站上消失，這是唯一的看守）
  3. 每個條目恰好三段（事實 → wikilink → 判斷句）；少一段代表「改變了什麼判斷」沒寫
  4. 每條 ≤ 200 字元（剝掉 wikilink 後量測）
  5. wikilink 目標存在於 wiki/（指到不存在的頁＝讀者點了沒有東西）
  6. 事實句與總結句不含整理語（HOUSEKEEPING_WORDS）——主詞必須是世界上的東西，
     不是本庫的頁面／表格／目錄（2026-09-12 乙-2，使用者：「每個領域都有一樣問題」）

行為：全過 exit 0；任何違規印出「檔案:行號 問題」後 exit 1。
「今日 wiki 無新知」的空日檔一律視為合法（它是規格要求的寫法，不是失敗）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = ROOT / "daily"
WIKI_DIR = ROOT / "wiki"

TITLE_RE = re.compile(r"^#\s+(\d{4}-\d{2}-\d{2})\s+今天 wiki 學到什麼\s*$")
NO_NEWS_RE = re.compile(r"^>\s*今日 wiki 無新知（(\d{4}-\d{2}-\d{2})）\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
ITEM_SEP = "→"
ITEM_MAX_CHARS = 200

# 整理語：出現在事實句或總結句，代表這條寫的是知識庫自己動了哪裡，不是世界發生了什麼。
# 規格端見 Step 2b「事實句的主詞必須是世界上的東西」。判斷句不查（它本來就可以談本庫怎麼看）。
HOUSEKEEPING_WORDS = [
    "本庫", "本頁", "拆成兩頁", "拆頁", "併頁", "汰除", "汰掉", "移出", "升為第一",
    "改版", "主題頁", "新增頁", "獨立成新頁", "概覽表", "目錄補", "表格升", "留在原頁",
]

# 與 build_web.READER_DOMAIN_SECTIONS 同一組節名（規格端見 Step 2b 契約表）
DOMAIN_LABELS = [
    "🛠️ 功能",
    "🤖 模型",
    "💼 商業",
    "🏛️ 安全政策",
    "🌐 社群",
    "👤 人物",
]


def _valid_wiki_targets() -> set[str]:
    targets: set[str] = set()
    for sub, prefix in (("entities", "entities/"), ("topics", "topics/")):
        for f in (WIKI_DIR / sub).glob("*.md"):
            targets.add(f.stem)
            targets.add(prefix + f.stem)
    for f in WIKI_DIR.glob("*.md"):
        targets.add(f.stem)
    return targets


def check_file(f: Path, valid_targets: set[str]) -> list[str]:
    problems: list[str] = []
    try:
        rel = f.relative_to(ROOT)
    except ValueError:
        rel = f.name  # repo 外的檔（測試 tmp 目錄）也要檢查得動
    lines = f.read_text(encoding="utf-8").splitlines()

    title_seen = False
    no_news = False
    current_label: str | None = None

    for n, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue

        m = TITLE_RE.match(stripped)
        if m:
            title_seen = True
            if m.group(1) != f.stem:
                problems.append(f"{rel}:{n} 標題日期 {m.group(1)} 與檔名 {f.stem} 不一致")
            continue

        if NO_NEWS_RE.match(stripped):
            no_news = True
            continue

        # 總結句（第一個領域節之前的 `>` 行）也不得是整理紀錄
        if current_label is None and stripped.startswith(">"):
            hit = [w for w in HOUSEKEEPING_WORDS if w in stripped]
            if hit:
                problems.append(f"{rel}:{n} 總結句含整理語「{hit[0]}」——寫今天世界發生了什麼，不寫動了哪頁")
            continue

        h = H2_RE.match(stripped)
        if h:
            label = h.group(1).strip()
            if label not in DOMAIN_LABELS:
                problems.append(
                    f"{rel}:{n} 節名「{label}」不在六個領域內，該段在網站上會整段消失"
                )
                current_label = None
            else:
                current_label = label
            continue

        if not stripped.startswith("-"):
            continue

        if current_label is None:
            problems.append(f"{rel}:{n} 條目不在任何領域節底下，不會上站")
            continue

        parts = [seg.strip() for seg in stripped[1:].split(ITEM_SEP)]
        if len(parts) != 3 or not all(parts):
            problems.append(
                f"{rel}:{n} 條目不是三段式（事實 → [[頁名]] → 改變了什麼判斷），"
                f"實得 {len(parts)} 段"
            )
            continue

        hit = [w for w in HOUSEKEEPING_WORDS if w in parts[0]]
        if hit:
            problems.append(
                f"{rel}:{n} 事實句含整理語「{hit[0]}」——主詞必須是世界上的東西，不是本庫的頁面／表格"
            )

        plain = WIKILINK_RE.sub(r"\1", stripped)
        if len(plain) > ITEM_MAX_CHARS:
            problems.append(f"{rel}:{n} 條目 {len(plain)} 字元，超過上限 {ITEM_MAX_CHARS}")

        links = WIKILINK_RE.findall(parts[1])
        if not links:
            problems.append(f"{rel}:{n} 中段沒有 [[頁名]]，讀者無處可跳")
        for raw in links:
            target = raw.split("|")[0].split("#")[0].replace("\\", "").strip()
            if target not in valid_targets:
                problems.append(f"{rel}:{n} wikilink [[{target}]] 指向不存在的 wiki 頁")

    if not title_seen:
        problems.append(f"{rel}:1 缺標題行 `# {f.stem} 今天 wiki 學到什麼`")
    if not no_news and current_label is None and not any(
        H2_RE.match(l.strip()) for l in lines
    ):
        problems.append(f"{rel}:1 既無領域節也無「今日 wiki 無新知」行，內容為空")

    return problems


def main(argv: list[str]) -> int:
    valid = _valid_wiki_targets()
    if len(argv) > 1:
        files = [DAILY_DIR / f"{argv[1]}.md"]
        if not files[0].exists():
            print(f"FAIL: {files[0]} 不存在")
            return 1
    else:
        files = sorted(DAILY_DIR.glob("*.md"))

    problems: list[str] = []
    for f in files:
        problems.extend(check_file(f, valid))

    if problems:
        print(f"讀者版日報格式檢查：{len(problems)} 筆違規")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"讀者版日報格式檢查：{len(files)} 份全過")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

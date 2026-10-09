"""patterns 樹週更自查（唯讀）：母頁契約兩條＋節點落點。/wiki-lint 社群週更第 4 步跑；exit 1 就照輸出修。

  1. 母頁正文（扣 frontmatter 與 %% 備忘）≤ 300 行（page-lifecycle「一頁一故事」）
  2. 母頁 `## 技術彙整` 底下的 `####` 節點只准在 `### 未歸類`（事件流不回流母頁）
  3. 七個子頁每則節點：「與既有模式的關係」第一個逐字寫出的類別名（口徑同 pages.md 第 1 條：去空白、
     全形斜線轉半形；「主線填…」「歸入主線…」那段不算）查 pages.md 第 0 條路由表，該住的子頁 ≠ 所在子頁即列出。
     關係行沒寫任何類別名的不判（那是記者判斷，未歸類照第 0 條處理）。
路由表的家是 pages.md 第 0 條，本檔直接讀那張表，不另抄。
用法：python scripts/patterns_tree_audit.py [wiki 目錄] [pages.md 路徑]
"""
import io, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "wiki"
RULES = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / ".claude" / "reporter-rules" / "community" / "pages.md"

rules = io.open(RULES, encoding="utf-8").read()
sec = rules[rules.index("### 0."):]
sec = sec[:sec.index("\n### ", 5)]
ROUTE = {m.group(1): [x.strip() for x in m.group(2).split("、")]
         for m in re.finditer(r"^\|\s*`topics/(community-[\w-]+)`\s*\|\s*([^|]+?)\s*\|", sec, re.M)}
assert len(ROUTE) == 7, f"pages.md 第 0 條路由表讀到 {len(ROUTE)} 列，預期 7"


def norm(s):
    return re.sub(r"\s", "", s).replace("／", "/")


NAMES = [(norm(n), page) for page, ns in ROUTE.items() for n in ns]


def body(p):
    t = io.open(p, encoding="utf-8").read().replace("\r\n", "\n")
    if t.startswith("---\n"):
        t = t[t.index("\n---\n", 4) + 5:]
    return re.sub(r"%%.*?%%", "", t, flags=re.S).rstrip("\n").split("\n")


bad = []
mother = body(WIKI / "topics" / "community-tech-patterns.md")
if len(mother) > 300:
    bad.append(f"母頁正文 {len(mother)} 行 > 300")
h2 = h3 = None
for line in mother:
    if line.startswith("## "):
        h2, h3 = line[3:].strip(), None
    elif line.startswith("### "):
        h3 = line[4:].strip()
    elif line.startswith("#### ") and h2 == "技術彙整" and h3 != "未歸類":
        bad.append(f"母頁 ### {h3} 底下有節點（只准在 未歸類）：{line[:60]}")
for page in ROUTE:
    title = None
    for line in body(WIKI / "topics" / f"{page}.md"):
        if line.startswith("#### "):
            title = line
        elif title and line.lstrip("- ").startswith("**與既有模式的關係：**"):
            r = norm(re.sub(r"(主線填|歸入主線).*?(。|$)", "", line))
            hits = sorted((r.find(k), p) for k, p in NAMES if k in r)
            if hits and hits[0][1] != page:
                bad.append(f"{page}：{title[5:55]} → 依路由表該住 {hits[0][1]}")
            title = None
print("\n".join(bad) or "OK: patterns 樹母頁契約與節點落點無異常")
sys.exit(1 if bad else 0)

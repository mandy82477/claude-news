#!/usr/bin/env python3
"""
check_focus.py — 日報「📌 今日聚焦」閘：同一故事不得換家媒體再當一次頭條。

用法：
    python scripts/check_focus.py YYYY-MM-DD --list   # 寫日報前：印出前 5 份日報的聚焦，供比對
    python scripts/check_focus.py YYYY-MM-DD          # 寫入後：檢查 news/YYYY-MM-DD.md 的聚焦

由 `.claude/skills/news-digest/SKILL.md` 第 1a、3a-3 步呼叫；判準住
`.claude/skills/news-digest/references/selection.md`「📌 今日聚焦」節。

檢查三件事，任一違規印出後 exit 1：
  1. 與前 WINDOW 份日報的某條聚焦相似度 ≥ THRESHOLD，卻沒標「（續 MM-DD）」
  2. 標了「（續 MM-DD）」卻不是 [持續追蹤]，或 [持續追蹤] 沒標「（續 MM-DD）」
     ——[持續追蹤] 對讀者承諾「這條線前幾天出現過」，要指得出是哪天
  3. 連結標籤寫 [HN] 卻不是連到 news.ycombinator.com

相似度：聚焦句（去掉標籤與句末來源連結）取英文詞＋中文二字組，以近 60 份日報聚焦算 IDF，
共有詞權重 ÷ 較短一句的總權重。0.30 以 2026-08-06～09-24 回放校準：命中者約九成是同一
故事重登或續報；換角度重寫（同一事件、字面不同）抓不到，那一半靠第 1a 步人工比對。
"""
import math
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NEWS_DIR = REPO_ROOT / "news"
WINDOW = 5
IDF_DAYS = 60
THRESHOLD = 0.30

FOCUS_RE = re.compile(r"^### 📌 今日聚焦\n(.*?)(?=^### |\Z)", re.S | re.M)
LABEL_RE = re.compile(r"^- \*\*\[([^\]]+)\]\*\*\s*")
CONT_RE = re.compile(r"（續 (\d{2}-\d{2})）")
HN_LINK_RE = re.compile(r"\[HN\]\((?!https?://news\.ycombinator\.com)[^)]*\)")
STOP_EN = {"anthropic", "claude", "openai", "google", "microsoft", "code", "api", "ceo",
           "the", "and", "for", "with", "from", "that", "this", "repo", "claude-code"}
STOP_CJK = set("宣布 表示 報導 指出 同日 媒體 公開 今日 已經 推出 發布 官方 開放 方案 使用 "
               "新增 支援 一則 累積 留言 反應".split())


def focus_bullets(text: str) -> list[str]:
    m = FOCUS_RE.search(text)
    return [l for l in m.group(1).splitlines() if l.startswith("- **[")] if m else []


def body(bullet: str) -> str:
    s = LABEL_RE.sub("", bullet)
    s = re.sub(r"（\[[^（]*$", "", s)                  # 句末來源連結
    s = CONT_RE.sub("", s)
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)


def tokens(bullet: str) -> set[str]:
    s, out = body(bullet), set()
    for w in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[.\-][A-Za-z0-9]+)*", s):
        if len(w) >= 3 and w.lower() not in STOP_EN:
            out.add(w.lower())
    for run in re.findall(r"[一-鿿]{2,}", s):
        out.update(g for g in (run[i:i + 2] for i in range(len(run) - 1)) if g not in STOP_CJK)
    return out


def digests_before(date: str, n: int, news_dir: Path) -> list[Path]:
    return sorted(p for p in news_dir.glob("????-??-??.md") if p.stem < date)[-n:]


def similarity(a: set[str], b: set[str], idf) -> float:
    shared = a & b
    if not shared:
        return 0.0
    denom = min(sum(map(idf, a)), sum(map(idf, b)))
    return sum(map(idf, shared)) / denom if denom else 0.0


def check(date: str, news_dir: Path = NEWS_DIR) -> list[str]:
    today_path = news_dir / f"{date}.md"
    today = focus_bullets(today_path.read_text(encoding="utf-8"))
    prior = [(p.stem, b) for p in digests_before(date, WINDOW, news_dir)
             for b in focus_bullets(p.read_text(encoding="utf-8"))]

    corpus = [b for p in digests_before(date, IDF_DAYS, news_dir)
              for b in focus_bullets(p.read_text(encoding="utf-8"))] + today
    df = Counter(t for b in corpus for t in tokens(b))
    idf = lambda t: math.log(len(corpus) / (1 + df[t])) if corpus else 0.0

    problems = []
    for i, b in enumerate(today, 1):
        label = (LABEL_RE.match(b) or [None, ""])[1]
        cont = CONT_RE.search(b)
        if cont and label != "持續追蹤":
            problems.append(f"聚焦第 {i} 條：標了（續 {cont.group(1)}）就要標 [持續追蹤]，現為 [{label}]")
        if label == "持續追蹤" and not cont:
            problems.append(f"聚焦第 {i} 條：[持續追蹤] 要寫出接續哪天——在標籤後加（續 MM-DD）")
        if HN_LINK_RE.search(b):
            problems.append(f"聚焦第 {i} 條：[HN] 標籤連到的不是 news.ycombinator.com——標籤改成實際來源名")
        if cont:
            continue
        tb = tokens(b)
        best = max(((similarity(tb, tokens(pb), idf), d, pb) for d, pb in prior),
                   default=(0.0, "", ""))
        if best[0] >= THRESHOLD:
            problems.append(
                f"聚焦第 {i} 條與 {best[1]} 的聚焦相似 {best[0]:.2f}，疑同一故事重登：\n"
                f"      今天：{body(b)[:80]}\n"
                f"      {best[1][5:]}：{body(best[2])[:80]}\n"
                f"    → 今天沒有新進展就移出聚焦；有新進展改標 [持續追蹤]（續 {best[1][5:]}）並寫出新在哪")
    return problems


def list_prior(date: str, news_dir: Path = NEWS_DIR) -> str:
    lines = []
    for p in digests_before(date, WINDOW, news_dir):
        lines.append(f"## {p.stem}")
        lines += [f"- {body(b)}" for b in focus_bullets(p.read_text(encoding="utf-8"))]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        print(__doc__)
        return 2
    date = args[0]
    if "--list" in argv:
        print(list_prior(date))
        return 0
    if not (NEWS_DIR / f"{date}.md").exists():
        print(f"找不到 news/{date}.md")
        return 2
    problems = check(date)
    for p in problems:
        print(f"✗ {p}")
    print(f"check_focus {date}：{'✅ 通過' if not problems else f'❌ {len(problems)} 項'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

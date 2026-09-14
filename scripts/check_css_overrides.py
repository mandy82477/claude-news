#!/usr/bin/env python3
"""
check_css_overrides.py — CSS 靜默覆寫機械閘。

**為什麼有這支：** 2026-09-14 的排版改版中，同一類缺陷在一輪內命中六次——
相同特異度下由「源順序」決勝，改了前面那份完全沒反應，而且不會報錯，
版面只是靜靜地不對。靠人更小心已經證明無效（見 design.css 的防治註解）。

兩類偵測：

1. **死媒體查詢**（基線外新增 → exit 1）
   `@media` 區塊裡的規則，若在它**之後**有一條**同一選擇器**、同特異度、
   設定同一屬性的非媒體規則，那條媒體覆寫永遠不生效。
   方向很重要：媒體查詢寫在基礎規則**之後**是正常做法，不報。
   只認同一選擇器：修飾子在子集上覆寫基礎類別是 BEM 的正常級聯，不是死碼。

2. **簡寫洗掉另一軸**（warn-only，不影響 exit code）
   後面的規則用 `padding` / `margin` 簡寫覆寫，而前面有會套到同一元素的規則
   在同一簡寫設了不同的水平值——水平內距會被一起洗掉。
   修法是改用 `padding-block` / `margin-block` 長寫。

存量基線（照 `data/reader-language-baseline.json` 的先例）：首跑必然命中大量
存量，全部 FAIL 只會讓人把檢查關掉。故 `data/css-override-baseline.json` 記下
既有命中，只對基線外的新增報 FAIL。

只用標準庫。掃描範圍由 `.claude/review-registry.json` 的 `css_overrides.globs`
決定，預設 `web_reader/assets/*.css`。

用法：
    python scripts/check_css_overrides.py
    python scripts/check_css_overrides.py --rebuild   # 重收基線

供 scripts/run_tests.py 呼叫。
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / ".claude" / "review-registry.json"
BASELINE = REPO_ROOT / "data" / "css-override-baseline.json"
DEFAULT_GLOBS = ["web_reader/assets/*.css"]

_COMMENT = re.compile(r"/\*.*?\*/", re.S)
_SHORTHAND = ("padding", "margin")


class Rule:
    __slots__ = ("selector", "decls", "line", "media")

    def __init__(self, selector, decls, line, media):
        self.selector = selector
        self.decls = decls
        self.line = line
        self.media = media

    def __repr__(self):  # pragma: no cover
        return f"Rule({self.selector!r}, line={self.line}, media={self.media!r})"


def _strip_comments(text: str) -> str:
    """把註解換成等長空白，保住行號與位移。"""
    def repl(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return _COMMENT.sub(repl, text)


def parse_css(text: str) -> list[Rule]:
    """極簡 CSS 解析：規則、一層 @media/@supports 巢狀。

    @keyframes / @font-face 整塊跳過（選擇器是百分比或空的）。
    """
    src = _strip_comments(text)
    rules: list[Rule] = []
    i = 0
    n = len(src)
    media_stack: list[str] = []
    skip_depth = 0

    def line_of(pos: int) -> int:
        return src.count("\n", 0, pos) + 1

    buf_start = 0
    while i < n:
        ch = src[i]
        if ch == "}":
            if skip_depth > 0:
                skip_depth -= 1
            elif media_stack:
                media_stack.pop()
            i += 1
            buf_start = i
            continue
        if ch != "{":
            i += 1
            continue

        prelude = " ".join(src[buf_start:i].split())
        if prelude.startswith("@"):
            at = prelude.split(None, 1)[0].lower()
            if at in ("@media", "@supports"):
                media_stack.append(prelude)
            else:
                skip_depth += 1
            i += 1
            buf_start = i
            continue

        depth = 1
        j = i + 1
        while j < n and depth:
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
            j += 1
        body = src[i + 1 : j - 1]
        decls: dict[str, str] = {}
        for part in body.split(";"):
            if ":" not in part:
                continue
            prop, _, val = part.partition(":")
            prop = prop.strip().lower()
            val = val.strip()
            if prop and val and not prop.startswith("--"):
                decls[prop] = val
        if prelude and decls:
            media = media_stack[-1] if media_stack else None
            for sel in prelude.split(","):
                sel = " ".join(sel.split())
                if sel:
                    rules.append(Rule(sel, decls, line_of(i), media))
        i = j
        buf_start = i
    return rules


_ID = re.compile(r"#[\w-]+")
_CLASSISH = re.compile(r"\.[\w-]+|\[[^\]]*\]|:(?!:)[\w-]+(?:\([^)]*\))?")
_ELEMENT = re.compile(r"(?:^|[\s>+~])([a-zA-Z][\w-]*)|::[\w-]+")
_COMBINATOR = re.compile(r"[\s>+~]")


def specificity(sel: str) -> tuple[int, int, int]:
    return (len(_ID.findall(sel)), len(_CLASSISH.findall(sel)), len(_ELEMENT.findall(sel)))


def _class_set(sel: str) -> set[str] | None:
    """單一複合選擇器且只由 class（可帶 pseudo-class）組成 → class 集合，否則 None。"""
    if _COMBINATOR.search(sel) or "#" in sel or "::" in sel:
        return None
    if _CLASSISH.sub("", sel).strip():
        return None
    classes = {m[1:] for m in re.findall(r"\.[\w-]+", sel)}
    return classes or None


def _bem_related(ca: set[str], cb: set[str]) -> bool:
    """BEM 修飾子：.story 與 .story--star 是兩個不同的 class，不是子集關係，
    但照慣例會同時掛在同一個元素上（app.js 的 `story story--star`）。
    只認 `base` 與 `base--mod` 這一種，兩個不同修飾子不算。"""
    for x in ca:
        for y in cb:
            if x == y:
                continue
            long, short = (x, y) if len(x) > len(y) else (y, x)
            if long.startswith(short + "--"):
                return True
    return False


def co_apply(sel_a: str, sel_b: str) -> bool:
    """兩個選擇器有沒有可能套到同一個元素（保守判斷，寧可漏報不誤報）。"""
    if sel_a == sel_b:
        return True
    ca, cb = _class_set(sel_a), _class_set(sel_b)
    if ca is None or cb is None:
        return False
    if ca <= cb or cb <= ca:
        return True
    return _bem_related(ca, cb)


def _horizontal(value: str) -> str | None:
    """取 padding/margin 簡寫的水平分量。看不懂就回 None。"""
    parts = value.split()
    if len(parts) == 1:
        return parts[0]
    if len(parts) in (2, 3):
        return parts[1]
    if len(parts) == 4:
        return f"{parts[1]}/{parts[3]}"
    return None


def scan(files: list[Path]) -> dict:
    dead: list[dict] = []
    shorthand: list[str] = []

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rules = parse_css(text)
        try:
            rel = path.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            rel = path.name

        for idx, r in enumerate(rules):
            if r.media is None:
                continue
            spec_r = specificity(r.selector)
            for later in rules[idx + 1:]:
                if later.media is not None:
                    continue
                # 只認「同一個選擇器」：修飾子在子集上覆寫基礎類別是 BEM 的正常級聯
                # （@media .section 對 .section--reader 不生效，但對一般 .section 生效，
                # 它不是死碼）。跨選擇器的洗值由下面的簡寫偵測負責。
                if later.selector != r.selector:
                    continue
                if specificity(later.selector) != spec_r:
                    continue
                clash = sorted(set(r.decls) & set(later.decls))
                if not clash:
                    continue
                dead.append({
                    "fp": f"{r.media}|{r.selector}|{','.join(clash)}",
                    "text": (
                        f"{rel}:{r.line}  {r.media} 裡的 `{r.selector}` 的 "
                        f"{'、'.join(clash)} 被 {rel}:{later.line} 的 "
                        f"`{later.selector}` 蓋掉（同特異度、在後）"
                    ),
                })
                break

        for idx, r in enumerate(rules):
            for prop in _SHORTHAND:
                if prop not in r.decls:
                    continue
                h_r = _horizontal(r.decls[prop])
                if h_r in (None, "0", "0px"):
                    continue
                for later in rules[idx + 1:]:
                    if prop not in later.decls or later.selector == r.selector:
                        continue
                    if not co_apply(r.selector, later.selector):
                        continue
                    h_l = _horizontal(later.decls[prop])
                    if h_l is None or h_l == h_r:
                        continue
                    shorthand.append(
                        f"{rel}:{later.line} `{later.selector}` 的 {prop} 簡寫會把 "
                        f"{rel}:{r.line} `{r.selector}` 的水平值 {h_r} 洗成 {h_l}"
                        f"——改用 {prop}-block 長寫"
                    )
                    break

    return {"dead": dead, "shorthand": shorthand}


def resolve_globs() -> list[Path]:
    globs = DEFAULT_GLOBS
    try:
        cfg = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")).get("css_overrides")
        if isinstance(cfg, dict):
            if not cfg.get("enabled", True):
                return []
            globs = cfg.get("globs") or DEFAULT_GLOBS
    except (OSError, json.JSONDecodeError):
        pass
    out: list[Path] = []
    for g in globs:
        out.extend(sorted(REPO_ROOT.glob(g)))
    return out


def load_baseline() -> set[str]:
    if not BASELINE.exists():
        return set()
    try:
        return set(json.loads(BASELINE.read_text(encoding="utf-8")).get("fingerprints", []))
    except (OSError, json.JSONDecodeError):
        return set()


def write_baseline(dead: list[dict]) -> None:
    fps = sorted({d["fp"] for d in dead})
    payload = {
        "_note": (
            "CSS 靜默覆寫閘的存量基線（命中指紋清單）。check_css_overrides.py 只對基線外的"
            "新增命中報 FAIL，基線內的印為 WARN 摘要。修好一筆就把它從清單移除——棘輪只能"
            "往下轉，不可為了轉綠而加回去。指紋 = 媒體條件 + 選擇器 + 衝突屬性，"
            "把該 @media 區塊移到基礎規則之後即失效。"
        ),
        "_baseline_set": "2026-09-14",
        "_hits": len(fps),
        "fingerprints": fps,
    }
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    BASELINE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    stream = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    files = resolve_globs()
    if not files:
        stream.write("OK: CSS 覆寫閘 — 無掃描目標\n")
        stream.flush()
        return 0

    res = scan(files)
    dead = res["dead"]

    if "--rebuild" in argv:
        write_baseline(dead)
        stream.write(f"已重收基線：{len({d['fp'] for d in dead})} 筆\n")
        stream.flush()
        return 0

    baseline = load_baseline()
    new = [d for d in dead if d["fp"] not in baseline]
    legacy = [d for d in dead if d["fp"] in baseline]

    for line in res["shorthand"]:
        stream.write(f"WARN: {line}\n")
    if legacy:
        stream.write(f"WARN: 存量基線內 {len(legacy)} 筆死媒體查詢（修好一筆就從基線移除）\n")

    if new:
        stream.write("\nFAIL: CSS 靜默覆寫 — 媒體查詢寫在基礎規則之前，永遠不生效\n\n")
        for d in new:
            stream.write(f"  {d['text']}\n")
        stream.write(
            "\n修法：把該 @media 區塊移到它要覆寫的基礎規則之後；"
            "媒體查詢不增加特異度，同特異度靠出現順序決勝。\n"
            "誤擋自查：若該筆本來就在基線、你也沒新增，跑 --rebuild 重收並在 commit 訊息說明。\n"
        )
        stream.flush()
        return 1

    stream.write(
        f"OK: CSS 覆寫閘 — {len(files)} 個檔無新增死媒體查詢"
        f"（存量 {len(legacy)} 筆、簡寫提示 {len(res['shorthand'])} 筆）\n"
    )
    stream.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""週報預告帳本一致性檢查。

週報第 (3) 段是一本帳：每期立下可證偽預告，下一期回收。這本帳沒有外部事實來源
（刻意的——markdown 才是事實，web 只是視圖），因此它的完整性必須靠機械比對維持，
否則所有失敗都是靜默的：

  1. 漏收    上期立的預告，下期沒回收 → 該條靜默蒸發（2026-W31 實際發生：三條未結案的
             條目回收一次寫「未定」後就再也沒被提起）
  2. 改判準  回收時把當初的判準改寫成對自己有利的版本 → 帳面永遠好看，讀者無從查證
  3. 殭屍    同一條每期都「未定」，長住帳本卻不產生資訊
  4. 跳期    某週沒跑週報，下期不知道該回收哪一期
  5. 湊數    硬湊條數，混進沒把握怎麼驗的題目

檢查對象是 weekly/ 內**最新兩期**（更早的已凍結，不重複檢查）。
規格見 `.claude/skills/weekly-report/references/forecast.md` 第 (3) 段；欄名與標題為兩者共用錨點。
"""

from __future__ import annotations

import difflib
import io
import re
import sys
from pathlib import Path


def _stdout():
    """Windows 主控台預設 cp950，直接 print 狀態符號會 UnicodeEncodeError（同 check_rules.py）。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout

REPO_ROOT = Path(__file__).resolve().parent.parent
WEEKLY_DIR = REPO_ROOT / "weekly"

RECAP_HEADER_RE = re.compile(r"^\|\s*上週預告\s*\|\s*判準\s*\|\s*本週結果\s*\|\s*$", re.MULTILINE)
FORECAST_HEADER_RE = re.compile(r"^\|\s*類型\s*\|\s*預告\s*\|\s*判準\s*\|\s*$", re.MULTILINE)
RECAP_HEADING_RE = re.compile(r"^###\s*上週的線怎麼了（(\d{4}-W\d{2})）", re.MULTILINE)
SEPARATOR_RE = re.compile(r"^\|[-: |]+\|$")

# 結案 vs 未結案：結果欄首字元決定。
# ⏰（到期日未到）算未結案——它必須一路帶到期限那週才結，否則會在中途靜默消失；
# 但它天生就會跨多期，故豁免下方的殭屍規則（到期日本身即內建結案時點）。
CLOSED_MARKS = ("✅", "❌")
OPEN_MARKS = ("⏳", "🟡", "⏰")
ZOMBIE_EXEMPT_MARKS = ("⏰",)

MIN_FORECASTS = 3
MAX_FORECASTS = 6

# 深挖小標必須恰好是 `###`——`scripts/build_web.py` 以 h3 切子區塊，再把「深挖：」
# 那節抽成專屬元件（kicker「深挖專欄 · DEEP DIVE」＋標題＋內文）。寫成 `####` 時
# 子區塊根本不存在，deepDive 變 None，整段內文被靜默併進「討論綜述」，網站上專欄
# 消失且無任何錯誤——2026-08-16 W33 踩過。規格檔的範例原本就寫成 `####`（那是規格
# 文件自己的巢狀深度，輸出檔少一層），W30–W32 三期各自從輸出結構推導出 `###`、
# 沒人回頭改規格，於是錯誤範例活了三週而無人察覺。
DEEPDIVE_HEADING_RE = re.compile(r"^(#{2,6})\s*深挖[：:]\s*(.*)$", re.MULTILINE)
DEEPDIVE_LEVEL = "###"
# 「本週數字」必須寫成 `- **值**——說明` 條列：build_web 的 WEEKLY_STAT_RE 只認這個形狀，
# 寫成表格會解析出 0 筆、網站上該節渲染成空殼，而 markdown 看起來完全正常。
# 2026-08-30 W35 踩過：整節寫成三欄表格，五個數字一個都沒上站，是使用者發現的。
STAT_BULLET_RE = re.compile(r"^-\s*\*\*(.+?)\*\*\s*——\s*(.+)$", re.MULTILINE)
NUMBERS_HEADING_RE = re.compile(r"^##\s*四、本週數字\s*$", re.MULTILINE)
STAT_MIN = 2  # 2026-09-25 起只收讀者用得上的數字，淡週 2 個合法

DEEPDIVE_MIN_CHARS = 900
DEEPDIVE_MAX_CHARS = 1300

# 只數「讀者讀得到的字」：URL、wikilink 路徑、程式碼反引號、粗體星號都不是。
# 2026-08-30 校準：舊版連 markup 一起數，佔比在 5%–20% 之間浮動（W31 5%、W34 20%），
# 於是同樣長度的兩段文字可能差 300 字才觸發提醒——那不是字數上限，是雜訊。
def deepdive_visible_len(body: str) -> int:
    """回傳深挖正文的可見字數（去空白、去 markdown 標記與連結目標）。"""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)   # [文字](url) -> 文字
    s = re.sub(r"\[\[([^\]|#]*)[^\]]*\]\]", "", s)      # [[頁面#錨點]] -> 移除
    s = re.sub(r"`([^`]*)`", r"\1", s)                    # `code` -> code
    s = re.sub(r"\*{1,3}", "", s)                         # 粗體／斜體標記
    return len(re.sub(r"\s", "", s))


def _strip_bold(text: str) -> str:
    return re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text).strip()


def _parse_table(body: str, header_re: re.Pattern) -> list[list[str]]:
    m = header_re.search(body)
    if not m:
        return []
    rows: list[list[str]] = []
    started = False
    for line in body[m.end():].splitlines():
        ls = line.strip()
        if not ls.startswith("|"):
            if started:
                break
            continue
        if SEPARATOR_RE.match(ls):
            started = True
            continue
        if not started:
            continue
        cells = [_strip_bold(c.strip()) for c in ls.strip("|").split("|")]
        if len(cells) >= 3:
            rows.append(cells)
    return rows


def _norm(text: str) -> str:
    """比對用正規化：去空白與全半形括號差異，避免換行/排版差異造成假失敗。"""
    t = re.sub(r"\s+", "", text)
    for a, b in (("（", "("), ("）", ")"), ("／", "/"), ("，", ",")):
        t = t.replace(a, b)
    return t


def _issues() -> list[Path]:
    return sorted(WEEKLY_DIR.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md"))


def check(report: list[str]) -> bool:
    if not WEEKLY_DIR.exists():
        return True  # 尚未啟用週報體裁

    files = _issues()
    if len(files) < 2:
        report.append(f"  ℹ️ 週報僅 {len(files)} 期，無上一期可比對，跳過帳本檢查")
        return True

    prev_f, curr_f = files[-2], files[-1]
    prev_raw = prev_f.read_text(encoding="utf-8-sig")
    curr_raw = curr_f.read_text(encoding="utf-8-sig")
    prev_id, curr_id = prev_f.stem, curr_f.stem

    ok = True

    # ── 1. 跳期：回收小標必須指名實際的上一期 ────────────────────────────────
    m = RECAP_HEADING_RE.search(curr_raw)
    if not m:
        report.append(f"  ❌ {curr_id}：找不到回收小標（需為 `### 上週的線怎麼了（{prev_id}）`）")
        ok = False
    elif m.group(1) != prev_id:
        report.append(
            f"  ❌ {curr_id}：回收小標指向 {m.group(1)}，但 weekly/ 內實際的上一期是 {prev_id}"
            f"（跳期未處理，帳會斷）"
        )
        ok = False

    prev_forecasts = _parse_table(prev_raw, FORECAST_HEADER_RE)
    prev_recap = _parse_table(prev_raw, RECAP_HEADER_RE)
    curr_recap = _parse_table(curr_raw, RECAP_HEADER_RE)
    curr_forecasts = _parse_table(curr_raw, FORECAST_HEADER_RE)

    if not curr_recap:
        report.append(f"  ❌ {curr_id}：回收表解析不到任何列（欄名須為 `| 上週預告 | 判準 | 本週結果 |`）")
        return False

    def _pair(forecast: str) -> list[str] | None:
        """把「應收」條目配到回收表的某一列。

        逐字比對太脆——同一條在回收表裡順手縮寫措辭就會誤報漏收；但完全放寬又會讓
        真正的漏收混過去。折衷：先試完全相同，再用相似度／包含關係配對，配到了才
        進一步檢查判準是否被改。配不到才算漏收。
        """
        key = _norm(forecast)
        for row in curr_recap:
            if _norm(row[0]) == key:
                return row
        best, best_ratio = None, 0.0
        for row in curr_recap:
            cand = _norm(row[0])
            if key in cand or cand in key:
                return row
            ratio = difflib.SequenceMatcher(None, key, cand).ratio()
            if ratio > best_ratio:
                best, best_ratio = row, ratio
        return best if best_ratio >= 0.6 else None

    # ── 2. 漏收：上期「新立的」＋「仍未結案的」都必須被回收 ────────────────────
    owed: list[tuple[str, str, str]] = []          # (預告, 判準, 來源)
    for row in prev_forecasts:
        owed.append((row[1], row[2], "上期新立"))
    for row in prev_recap:
        result = row[2]
        if result.startswith(OPEN_MARKS):
            owed.append((row[0], row[1], "上期未結案"))

    for forecast, criterion, origin in owed:
        row = _pair(forecast)
        if row is None:
            report.append(f"  ❌ {curr_id}：漏收（{origin}）「{forecast[:40]}」")
            ok = False
            continue
        # ── 3. 改判準：回收時的判準必須與立案當期逐字相同 ──────────────────
        if _norm(row[1]) != _norm(criterion):
            report.append(
                f"  ❌ {curr_id}：判準遭改寫「{forecast[:30]}」\n"
                f"       立案（{prev_id}）：{criterion[:70]}\n"
                f"       回收（{curr_id}）：{row[1][:70]}"
            )
            ok = False

    # ── 4. 結果欄必須帶狀態符號，未結案者必須寫明續盯去向 ──────────────────────
    for row in curr_recap:
        result = row[2]
        if not result.startswith(CLOSED_MARKS + OPEN_MARKS):
            report.append(
                f"  ❌ {curr_id}：結果欄缺狀態符號（需 ✅／❌／⏰ 結案，或 ⏳／🟡 續盯）"
                f"——「{row[0][:30]}」"
            )
            ok = False
        elif result.startswith(OPEN_MARKS) and "續盯" not in result:
            report.append(
                f"  ❌ {curr_id}：未結案卻未寫續盯去向（需「→ 續盯至 Wnn」）——「{row[0][:30]}」"
            )
            ok = False

    # ── 5. 殭屍：同一條連續兩期未結案 → 應強制結案 ────────────────────────────
    prev_open = {
        _norm(r[0]) for r in prev_recap
        if r[2].startswith(OPEN_MARKS) and not r[2].startswith(ZOMBIE_EXEMPT_MARKS)
    }
    for row in curr_recap:
        if (_norm(row[0]) in prev_open and row[2].startswith(OPEN_MARKS)
                and not row[2].startswith(ZOMBIE_EXEMPT_MARKS)):
            report.append(
                f"  ❌ {curr_id}：殭屍條目——「{row[0][:36]}」連續兩期未結案，"
                f"依規格應強制結案（無結論／降級為未證實）"
            )
            ok = False

    # ── 6. 條數與可查證性 ────────────────────────────────────────────────────
    n = len(curr_forecasts)
    if not (MIN_FORECASTS <= n <= MAX_FORECASTS):
        report.append(f"  ❌ {curr_id}：新開 {n} 條，規格為 {MIN_FORECASTS}–{MAX_FORECASTS} 條（寧缺勿湊）")
        ok = False
    missing_probe = [r[1] for r in curr_forecasts if "查證：" not in r[2]]
    if missing_probe:
        for forecast in missing_probe:
            report.append(
                f"  ❌ {curr_id}：判準缺查證線索（結尾需「｜查證：關鍵字1、關鍵字2」）——「{forecast[:36]}」"
            )
        ok = False

    if ok:
        report.append(
            f"  ✅ {curr_id} ← {prev_id}：回收 {len(curr_recap)} 筆、應收 {len(owed)} 筆全數到位；"
            f"判準無改寫；新開 {n} 條均帶查證線索"
        )
    return ok


def check_weekly_numbers(report: list[str], weekly_dir: Path = WEEKLY_DIR) -> bool:
    """『本週數字』必須解析得出 stats，否則網站上是空殼。

    硬擋：這是靜默失敗——markdown 讀起來正常，只有網站上少一整節，
    而沒有任何人會去比對 JSON。W30–W34 各 5 筆，W35 寫成表格得 0 筆。
    """
    ok = True
    files = sorted(weekly_dir.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md")) if weekly_dir.exists() else []
    for path in files:
        if path.stem < HEADLINE_RULES_SINCE:
            continue
        text = path.read_text(encoding="utf-8-sig")
        m = NUMBERS_HEADING_RE.search(text)
        if not m:
            continue
        body = re.split(r"^##\s", text[m.end():], maxsplit=1, flags=re.MULTILINE)[0]
        n = len(STAT_BULLET_RE.findall(body))
        if n < STAT_MIN:
            ok = False
            hint = ("該節寫成表格了？" if "|" in body else "格式須為 `- **值**——說明`（全形破折號）")
            report.append(
                f"  ❌ {path.stem}：本週數字只解析出 {n} 筆（需 ≥ {STAT_MIN}）——{hint}"
                "；build_web 的 WEEKLY_STAT_RE 只認條列，網站上該節會是空殼"
            )
    return ok


def check_deepdive(report: list[str]) -> bool:
    """深挖專欄的小標層級與篇幅。

    層級錯誤會讓網站上的專欄元件整個消失（見 DEEPDIVE_HEADING_RE 註解），故硬擋；
    篇幅只 WARN——那是編輯判斷，且本專案不用「數字只准往某方向走」的機械棘輪。
    """
    ok = True
    for path in _issues():
        text = path.read_text(encoding="utf-8-sig")
        matches = DEEPDIVE_HEADING_RE.findall(text)
        if not matches:
            # 規格允許「查無不補位」時整段省略，故不硬擋，只提醒。
            report.append(f"  ⚠️ {path.stem}：找不到深挖小標（若為本週略過，忽略此提醒）")
            continue
        if len(matches) > 1:
            report.append(f"  ❌ {path.stem}：出現 {len(matches)} 個深挖小標，專欄應只有一個")
            ok = False
        level, title = matches[0]
        if level != DEEPDIVE_LEVEL:
            report.append(
                f"  ❌ {path.stem}：深挖小標為 `{level}`，必須是 `{DEEPDIVE_LEVEL}`"
                f"——build_web.py 以 h3 切子區塊，其他層級會讓專欄元件整個不渲染、"
                f"內文被靜默併進「討論綜述」"
            )
            ok = False

        # 回收小標與表格之間的導言：build_web 抽成 nextweek.intro，缺了網站上會
        # 從小標直接跳進表格。只 WARN——它不影響內容正確性，只影響版面一致。
        for heading_re, label, why in (
            (r"^###\s*上週的線怎麼了（\d{4}-W\d{2}）\s*$",
             "回收表",
             "build_web 的 nextweek.recapIntro 會是空的，盤點摘要不會出現在網站上"),
            (r"^###\s*下週值得關注：新開\s*\d+\s*條\s*$",
             "新開表",
             "它與節導言合併為網站的 nextweek.intro，缺了讀者不知道這 N 條是不是全部"),
        ):
            gap = re.search(heading_re + r"(.*?)^\|", text, re.MULTILINE | re.DOTALL)
            if gap and not gap.group(1).strip():
                report.append(f"  ⚠️ {path.stem}：{label}小標與表格之間缺導言一行（{why}）")

        start = text.index(matches[0][1]) if matches[0][1] else 0
        body = re.split(r"^#{2,3}\s", text[start:], maxsplit=1, flags=re.MULTILINE)[0]
        n = deepdive_visible_len(body)
        if not (DEEPDIVE_MIN_CHARS <= n <= DEEPDIVE_MAX_CHARS):
            report.append(
                f"  ⚠️ {path.stem}：深挖 {n} 字（可見字數，不含連結與標記），規格為 "
                f"{DEEPDIVE_MIN_CHARS}–{DEEPDIVE_MAX_CHARS}（提醒，不擋）"
            )
    return ok


# ── 頭條敘事規則（規格：weekly-report.md 第 (1) 段，W35 起生效）───────────────
#
# 舊期（W30–W34）在規則立下前寫成，已凍結——回溯檢查只會產出一批永遠不修的
# ❌，把真訊號淹掉，故以期號閘門排除。字串比較對 YYYY-Wnn 格式即字典序即時序。
HEADLINE_RULES_SINCE = "2026-W35"

# 規則 0：頭條標題（h2 冒號後那句）。W30–W34 五期都有、渲染層 weeklyHeadlineDeck()
# 也一直支援，但**規格從未寫下它**——於是 W35 一漏，沒有任何東西擋得住，W36 補回的
# 也只有另立的「本週一句話」callout。2026-09-06 合併兩者：句子住 h2，callout 退場。
# 這條檢查存在的唯一理由，就是「上一次它是靠沒人注意而死的」。
HEADLINE_DECK_SINCE = "2026-W36"
HEADLINE_DECK_RE = re.compile(r"^##\s*一、頭條敘事[：:]\s*(\S.*?)\s*$", re.MULTILINE)
HEADLINE_DECK_MAX = 60

# 頭條節＝「## 一、…」到下一個 ## 之間。
HEADLINE_SECTION_RE = re.compile(r"^##\s*一、[^\n]*\n(.*?)(?=^##\s)", re.MULTILINE | re.DOTALL)

# 規則 7：跨期收束模板。連兩期命中同一句型骨架才算違規（單期首次使用合法）。
COLLAPSE_TEMPLATE_RE = re.compile(r"把[一二三四五六七八九十\d]+條線並排")

# 規則 9：日期句首與段內遞增。只認 MM-DD 形式（08-17），不碰 8/31 這類到期日寫法。
DATE_LEAD_RE = re.compile(r"^\s*\d{2}-\d{2}")
DATE_RE = re.compile(r"\b(\d{2})-(\d{2})\b")

# 規則 10：粗體預算。
HEADLINE_BOLD_MAX = 2
HEADLINE_BOLD_SPAN_MAX = 15

# 規則 8：同段 ≥2 個同單位金額時，每個數字 ±12 字內要有角色詞。
MONEY_RE = re.compile(r"\d[\d,.]*\s*[億兆]")
ROLE_WORDS = ("已實現", "年化", "單季", "預測", "估值", "額度", "一次性", "合約總額", "收購價")
ROLE_WINDOW = 12


def _headline_paragraphs(text: str) -> list[str]:
    m = HEADLINE_SECTION_RE.search(text)
    if not m:
        return []
    return [p.strip() for p in re.split(r"\n\s*\n", m.group(1)) if p.strip() and not p.strip().startswith(("|", ">"))]


def check_headline(report: list[str], weekly_dir: Path = WEEKLY_DIR) -> bool:
    """頭條敘事的機械規則（規格第 (1) 段帶 🔧 者）。

    硬擋（❌）只留誤判率低的三項：跨期模板、日期句首、粗體數量；
    段內日期遞增與角色詞誤判空間較大（前情錨合法回指、金額語境多樣），只 WARN。
    """
    ok = True
    files = sorted(weekly_dir.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md")) if weekly_dir.exists() else []
    for i, path in enumerate(files):
        if path.stem < HEADLINE_RULES_SINCE:
            continue
        text = path.read_text(encoding="utf-8-sig")
        paras = _headline_paragraphs(text)
        if not paras:
            report.append(f"  ⚠️ {path.stem}：找不到「## 一、」頭條節，頭條規則未檢查")
            continue
        section = "\n\n".join(paras)

        # 規則 0：h2 冒號後必須有頭條標題，且 ≤60 字
        if path.stem >= HEADLINE_DECK_SINCE:
            dm = HEADLINE_DECK_RE.search(text)
            if not dm:
                report.append(
                    f"  ❌ {path.stem}：`## 一、頭條敘事` 後缺頭條標題"
                    "（格式 `## 一、頭條敘事：<一句話>`；規格見 weekly-report.md 第 (1) 段）"
                )
                ok = False
            elif len(dm.group(1)) > HEADLINE_DECK_MAX:
                report.append(
                    f"  ❌ {path.stem}：頭條標題 {len(dm.group(1))} 字，上限 {HEADLINE_DECK_MAX}"
                )
                ok = False

        # 規則 7：與上一期（不受生效閘限制——上期是比對基準，不是受檢對象）同構
        if i > 0 and COLLAPSE_TEMPLATE_RE.search(section):
            prev_text = files[i - 1].read_text(encoding="utf-8-sig")
            if COLLAPSE_TEMPLATE_RE.search(prev_text):
                report.append(
                    f"  ❌ {path.stem}：收束句型「把 N 條線並排」與上期（{files[i - 1].stem}）同構"
                    f"——換一種收束方式（時間因果鏈／反問／直接給結論）"
                )
                ok = False

        for n, para in enumerate(paras, 1):
            # 規則 9a：每段日期開頭句 ≤1
            sentences = [s for s in re.split(r"[。；]", para) if s.strip()]
            leads = sum(1 for s in sentences if DATE_LEAD_RE.match(s))
            if leads > 1:
                report.append(
                    f"  ❌ {path.stem}：頭條第 {n} 段有 {leads} 句以日期開頭（上限 1）"
                    f"——其餘句事件先行、日期後置"
                )
                ok = False
            # 規則 9b：段內日期非遞減（WARN——前情錨回指上週屬合法例外）
            dates = [(int(a), int(b)) for a, b in DATE_RE.findall(para)]
            if any(dates[j] > dates[j + 1] for j in range(len(dates) - 1)):
                report.append(
                    f"  ⚠️ {path.stem}：頭條第 {n} 段日期非由早到晚（{['-'.join(f'{x:02d}' for x in d) for d in dates]}）"
                    f"——若非前情錨回指，代表混了兩條時間線，建議拆段"
                )
            # 規則 8：同段 ≥2 個金額，每個 ±12 字內要有角色詞（WARN）
            monies = list(MONEY_RE.finditer(para))
            if len(monies) >= 2:
                for m2 in monies:
                    ctx = para[max(0, m2.start() - ROLE_WINDOW): m2.end() + ROLE_WINDOW]
                    if not any(w in ctx for w in ROLE_WORDS):
                        report.append(
                            f"  ⚠️ {path.stem}：頭條第 {n} 段「{m2.group()}」缺角色詞"
                            f"（已實現／年化／單季／預測／估值／額度…）——同段多金額時讀者無從比較"
                        )

        # 規則 10：粗體預算
        bolds = re.findall(r"\*\*([^*]+)\*\*", section)
        if len(bolds) > HEADLINE_BOLD_MAX:
            report.append(
                f"  ❌ {path.stem}：頭條粗體 {len(bolds)} 處（上限 {HEADLINE_BOLD_MAX}）——只標數字／專名"
            )
            ok = False
        for b in bolds:
            if len(b) > HEADLINE_BOLD_SPAN_MAX:
                report.append(
                    f"  ⚠️ {path.stem}：頭條粗體「{b[:20]}…」長 {len(b)} 字（上限 {HEADLINE_BOLD_SPAN_MAX}）"
                    f"——整句判斷加粗是把金句感用字重再放大一次"
                )
    return ok


# ── 探針活性（W39 起生效）────────────────────────────────────────────────────
# 探針要能在日報 grep 到後續，前提是它**用的是日報的詞**。撰稿者立預告時很容易
# 用自己在頭條裡造的詞（W37「週配額、17%、撞上限」），而日報寫的是另一套
# （「用量縮減、額度、usage limits、25%」）。這種探針在立案當週就找不到生出它的那則
# 新聞，當然永遠找不到後續——下期回收只會看到「零命中」，然後把有事的線判成沒事。
# 2026-09-20 回溯量測：九期 150 個探針中 21% 立案當週即零命中；整條全滅的 3 條
# （W36 沙箱、W37 額度被偷／配額換軌）後來全數以「零命中」收場，其中配額換軌那條
# 實際有 5 則相關日報條目，是判錯。W31–W35 無一條全滅，零誤擋。
PROBE_LIVENESS_SINCE = "2026-W39"
PROBE_TAIL_RE = re.compile(r"｜查證：(.+?)\s*$")
NEWS_DIR = REPO_ROOT / "news"


def _issue_window_text(issue_id: str, news_dir: Path) -> str | None:
    """該期 ISO 週（含前一日，週報常於週日寫、涵蓋上週六起）的日報全文；一份都沒有回 None。"""
    from datetime import date, timedelta
    m = re.match(r"(\d{4})-W(\d{2})$", issue_id)
    if not m:
        return None
    monday = date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
    chunks = []
    for i in range(-1, 7):
        f = news_dir / f"{(monday + timedelta(days=i)).isoformat()}.md"
        if f.exists():
            chunks.append(f.read_text(encoding="utf-8-sig"))
    return "\n".join(chunks) if chunks else None


def check_probe_liveness(report: list[str], weekly_dir: Path = WEEKLY_DIR,
                         news_dir: Path = NEWS_DIR) -> bool:
    """新開預告的探針，在立案當週的日報至少要有一個命中——全滅即硬擋。"""
    files = sorted(weekly_dir.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md")) if weekly_dir.exists() else []
    if not files:
        return True
    curr = files[-1]
    if curr.stem < PROBE_LIVENESS_SINCE:
        return True  # 舊期已凍結，不回溯
    text = _issue_window_text(curr.stem, news_dir)
    if text is None:
        report.append(f"  ℹ️ {curr.stem}：找不到該週日報，探針活性略過（不當作通過的證據）")
        return True
    hay = text.lower()
    ok = True
    for row in _parse_table(curr.read_text(encoding="utf-8-sig"), FORECAST_HEADER_RE):
        if len(row) < 3:
            continue
        tail = PROBE_TAIL_RE.search(row[2])
        if not tail:
            continue  # 缺線索由 check() 另行硬擋
        probes = [x.strip() for x in re.split(r"[、,，]", tail.group(1)) if x.strip()]
        if probes and not any(p.lower() in hay for p in probes):
            ok = False
            report.append(
                f"  ❌ {curr.stem}：探針在立案當週的日報全數零命中——「{_strip_bold(row[1])[:30]}」"
                f"（{'、'.join(probes)}）。連生出這條預告的新聞都找不到的探針，找不到後續；"
                "改用日報原文裡真的出現過的字串（產品名、issue 編號、機構名）"
            )
    if ok:
        report.append(f"  ✅ {curr.stem}：新開預告的探針在當週日報皆有命中")
    return ok


# ── 讀者面三條（規格：headline.md 第 3 條、deepdive.md「本週要動的事」、
#    forecast.md 回收段與檔尾數字；W39 起生效，舊期凍結不回溯）──────────────
# 2026-09-25：W36–W38 三期頭條與深挖同題，頭條都寫進了深挖的指令名、官方連結
# （W36 `/sandbox`、W37 `CLAUDE_CODE_OAUTH_TOKEN`、W38 memory 文件連結）；冷讀者
# 讀 W38 時說可動作的事散在五處要自己撿，並在回收表的「初版誤判…同日更正」、
# 本週數字的「109 → 0 逾期待查證」處跳讀——那是編輯台的帳，不是讀者的內容。
READER_RULES_SINCE = "2026-W39"
ACTIONS_HEADING_RE = re.compile(r"^###\s*本週要動的事\s*$", re.MULTILINE)
ACTIONS_NONE = "本週沒有需要動的事"
URL_RE = re.compile(r"\]\((https?://[^)\s#]+)")
CODE_RE = re.compile(r"`([^`\n]+)`")
NUMBER_RE = re.compile(r"\d[\d,.]*\s*(?:%|則|個|美元|萬|億|倍|讚)")
DESK_WORDS_RE = re.compile(r"初版|同日更正|整期改版|改版一次|待查證|本刊 ?wiki|日報收錄|收錄的文章|來源數")
SECTION_THREE_RE = re.compile(r"^##\s*三、", re.MULTILINE)


def _deepdive_body(text: str) -> str:
    m = DEEPDIVE_HEADING_RE.search(text)
    if not m:
        return ""
    return re.split(r"^#{2,3}\s", text[m.end():], maxsplit=1, flags=re.MULTILINE)[0]


def _section_after(text: str, heading_re: re.Pattern) -> str:
    m = heading_re.search(text)
    if not m:
        return ""
    return re.split(r"^#{2,3}\s|^---\s*$", text[m.end():], maxsplit=1, flags=re.MULTILINE)[0]


def check_reader_rules(report: list[str], weekly_dir: Path = WEEKLY_DIR) -> bool:
    ok = True
    files = sorted(weekly_dir.glob("[0-9][0-9][0-9][0-9]-W[0-9][0-9].md")) if weekly_dir.exists() else []
    for path in files:
        if path.stem < READER_RULES_SINCE:
            continue
        text = path.read_text(encoding="utf-8-sig")

        # 1. 頭條不寫深挖的具體物
        hm = HEADLINE_SECTION_RE.search(text)
        deck = (HEADLINE_DECK_RE.search(text) or [None, ""])[1]
        dd = _deepdive_body(text)
        if hm and dd:
            head = hm.group(1)
            links = set(URL_RE.findall(head)) & set(URL_RE.findall(dd))
            codes = {c for c in set(CODE_RE.findall(head)) & set(CODE_RE.findall(dd)) if c not in deck}
            if links or codes:
                ok = False
                shared = "、".join(sorted(codes) + sorted(links))
                report.append(
                    f"  ❌ {path.stem}：頭條寫進了深挖的具體物（{shared}）——頭條只講這件事為什麼"
                    "重要、讀者要不要反應；指令、設定名與官方文件引用只放深挖，頭條用一句話指過去"
                )
            nums = set(NUMBER_RE.findall(head)) & set(NUMBER_RE.findall(dd))
            if nums:
                report.append(f"  ⚠️ {path.stem}：頭條與深挖出現同一個數字（{'、'.join(sorted(nums))}），確認不是同一件事講兩次")

        # 2. 本週要動的事
        am = ACTIONS_HEADING_RE.search(text)
        three = SECTION_THREE_RE.search(text)
        if not am:
            ok = False
            report.append(f"  ❌ {path.stem}：缺 `### 本週要動的事`（第二節最後一個小標；沒有就寫「{ACTIONS_NONE}。」）")
        else:
            body = _section_after(text, ACTIONS_HEADING_RE)
            if not re.search(r"^- \S", body, re.MULTILINE) and ACTIONS_NONE not in body:
                ok = False
                report.append(f"  ❌ {path.stem}：本週要動的事是空的——列條目，或寫「{ACTIONS_NONE}。」")
            if three and am.start() > three.start():
                ok = False
                report.append(f"  ❌ {path.stem}：本週要動的事要放在第二節（深挖之後、`## 三、` 之前）")

        # 3. 第三、四節與檔尾不放編輯台的帳
        # 判準欄是凍結的程式契約（deepdive.md「讀者版禁用內部詞」射程），不查
        tail = text[three.start():] if three else ""
        prose = [l for l in tail.splitlines() if not l.lstrip().startswith("|")]
        cells = [c for r in _parse_table(tail, RECAP_HEADER_RE) for c in (r[0], r[-1])]
        cells += [c for r in _parse_table(tail, FORECAST_HEADER_RE) for c in r[:2]]
        tail = "\n".join(prose + cells)
        hits = sorted(set(DESK_WORDS_RE.findall(tail)))
        if hits:
            ok = False
            report.append(
                f"  ❌ {path.stem}：第三節以後出現編輯台用語（{'、'.join(hits)}）——製作過程、"
                "收錄量與 wiki 維護指標記進 wiki/log.md，週報只寫讀者要的結果"
            )
    return ok


def main() -> int:
    report: list[str] = []
    ok = check(report)
    ok = check_weekly_numbers(report) and ok
    ok = check_deepdive(report) and ok
    ok = check_headline(report) and ok
    ok = check_probe_liveness(report) and ok
    ok = check_reader_rules(report) and ok
    out = _stdout()
    print("# check_weekly_ledger.py 報告\n", file=out)
    print("\n".join(report) if report else "  （無週報）", file=out)
    print(file=out)
    print("狀態：" + ("✅ 週報帳本一致" if ok else "❌ 週報帳本有缺口"), file=out)
    out.flush()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

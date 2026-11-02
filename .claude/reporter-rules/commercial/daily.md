# Wiki Ingest — 商業記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md` ＋ `.claude/reporter-rules/daily-contracts.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/commercial/pages.md`，主編層的週更（pricing 通路與乘數）見 `.claude/reporter-rules/commercial/weekly.md`。

分類為「商業」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/anthropic-business.md`（母頁） | 公司動態（辦公室、雇主排名、經濟研究、組織文化）；`## 現在的數字` 指標換值；`## IPO 走到哪一格` 一句結論（五格表換值時同批）；子線路由表「最後動態」。其餘商業事件寫進下面三子頁（路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條） |
| `wiki/topics/anthropic-ipo.md`（子頁「上市與財報」） | **IPO 與估值進程**、融資輪次、**公司層級財務數字**、治理與股權（五格表、S-1 揭露表、數字細節住這頁） |
| `wiki/topics/anthropic-partnerships-compute.md`（子頁「合作與算力」） | 戰略合作、收購、算力合約與資本支出、政府採購、具名企業導入（採用率指數換值寫母頁 `## 現在的數字`） |
| `wiki/topics/anthropic-business-risks.md`（子頁「風險與商業模式」） | **公司層級商業風險**（訴訟、企業退出、補貼結構）、商業模式、PMF 訊號 |
| `wiki/topics/enterprise-tool-tracker.md` | 具名企業採用 / 退出 AI 編碼工具；企業工具切換報導（含有規模描述的匿名企業）；企業 AI 工具預算或成本相關的具名案例 |
| `wiki/topics/enterprise-cost-management.md` | 企業規模成本挑戰、具名案例 |
| `wiki/entities/pricing.md`（母頁） | 訂閱方案、牌價、生效規則、還沒確定的計費變動等現行事實；子頁路由表「最後動態」。事故與沿革寫進下面兩子頁（路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條） |
| `wiki/entities/pricing-incidents.md`（子頁「計費事故」） | 計費事故與爭議、額度與速率異常回報、灰色市場與轉售；`## 還在發生的事故` 表 |
| `wiki/entities/pricing-history.md`（子頁「計費沿革」） | 價格、方案與促銷什麼時候變的；`## 最近三個月變了什麼` |
| `wiki/entities/openclaw.md` | 第三方 agentic 工具的**使用政策與計費**變化（禁令、恢復、信用池費率）。本頁主線是計費政策；OpenClaw agent 造成的安全事件由安全政策記者寫進 [[topics/ai-agent-safety]]，本頁只留一行指過去 |
| `wiki/entities/opencode.md` | OpenCode 的**產品事實**（採用規模、功能對等性評測、對官方 skills 的移植）。競爭面的判讀（衝擊度、定價對照）住 [[topics/competitor-landscape]] 的 OpenCode 列，本頁是它指過來的「完整脈絡」——那一列有新動態時同步回寫本頁，別讓本頁再停在舊日期 |
| `wiki/topics/competitor-landscape.md` | 競品動態、企業工具市佔變化（**先看 `.claude/reporter-rules/commercial/pages.md` 該頁第 0 條「本頁不收什麼」**）|
| `wiki/topics/ai-talent-flow.md` | AI 實驗室間人才流動、對各公司的商業影響（誰流失、誰承接、戰力與市場意涵）|

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 💼 商業 的所有頁面（含日後新增）皆由本記者負責維護與 lint。
>
> **唯一例外：`wiki/topics/market-signals.md` 與四子頁 `market-signals-ipo／-legal／-compute／-customers`**——領域雖為 💼 商業，但由**投資分析記者**維護（`.claude/reporter-rules/market/daily.md`），你不寫這五頁；懸置掃描的命中直接派給投資分析記者（`scripts/pending_markers.py` 的 `PAGE_TO_REPORTER`），你不會收到。它是觀點層，事實層仍在你的頁面上，兩者以 wikilink 相連。

---

## 官方文件查證優先於媒體轉述

方案、配額、計費規則這類事實，Anthropic 寫在 **`support.claude.com` 說明中心**，而該站不在日報來源清單內——媒體轉述往往只有標題層級且各自描述不同 seat 層級，堆進頁面就成了「互相矛盾」的假象。

記者**無 web 工具**，遇此情形不得自行推斷，於回報「同步自查」欄註明「⚠️ 需主編查證官方說明中心：[議題＋建議查證頁]」，由主編層 WebFetch 查證後寫入並標來源連結與查證日。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄；`feature-radar 新增` 欄恆填「無」（時效性項目如促銷到期、政策生效日，改在「同步自查」欄請主編同步 feature-radar「⏰ 倒數中」）。

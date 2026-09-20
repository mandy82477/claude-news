# Wiki Ingest — 商業記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/commercial/pages.md`，主編層的週更（pricing 通路與乘數）見 `.claude/reporter-rules/commercial/weekly.md`。

分類為「商業」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/anthropic-business.md` | 融資、收購、戰略合作、企業採用率、**IPO 與估值進程**、**公司層級財務數字**、**公司層級商業風險**（訴訟、企業退出、補貼結構）|
| `wiki/topics/enterprise-tool-tracker.md` | 具名企業採用 / 退出 AI 編碼工具；企業工具切換報導（含有規模描述的匿名企業）；企業 AI 工具預算或成本相關的具名案例 |
| `wiki/topics/enterprise-cost-management.md` | 企業規模成本挑戰、具名案例 |
| `wiki/entities/pricing.md` | 訂閱方案、計費政策、token 成本 |
| `wiki/entities/openclaw.md` | 第三方 agentic 工具的**使用政策與計費**變化（禁令、恢復、信用池費率）。本頁主線是計費政策；OpenClaw agent 造成的安全事件由安全政策記者寫進 [[topics/ai-agent-safety]]，本頁只留一行指過去 |
| `wiki/entities/opencode.md` | OpenCode 的**產品事實**（採用規模、功能對等性評測、對官方 skills 的移植）。競爭面的判讀（衝擊度、定價對照）住 [[topics/competitor-landscape]] 的 OpenCode 列，本頁是它指過來的「完整脈絡」——那一列有新動態時同步回寫本頁，別讓本頁再停在舊日期 |
| `wiki/topics/competitor-landscape.md` | 競品動態、企業工具市佔變化（**先看 `.claude/reporter-rules/commercial/pages.md` 該頁第 0 條「本頁不收什麼」**）|
| `wiki/topics/ai-talent-flow.md` | AI 實驗室間人才流動、對各公司的商業影響（誰流失、誰承接、戰力與市場意涵）|

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 💼 商業 的所有頁面（含日後新增）皆由本記者負責維護與 lint。
>
> **唯一例外：`wiki/topics/market-signals.md`**——該頁領域雖為 💼 商業，但由**投資分析記者**維護（`.claude/reporter-rules/market/daily.md`），你不寫該頁的判讀內容；懸置掃描把該頁的標記派給你時，照共用規則只加 `訊`。它是觀點層，事實層仍在你的頁面上，兩者以 wikilink 相連。

---

## 官方文件查證優先於媒體轉述

方案、配額、計費規則這類事實，Anthropic 寫在 **`support.claude.com` 說明中心**，而該站不在日報來源清單內——媒體轉述往往只有標題層級且各自描述不同 seat 層級，堆進頁面就成了「互相矛盾」的假象。

記者**無 web 工具**，遇此情形不得自行推斷，於回報「同步自查」欄註明「⚠️ 需主編查證官方說明中心：[議題＋建議查證頁]」，由主編層 WebFetch 查證後寫入並標來源連結與查證日。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄；`feature-radar 新增` 欄恆填「無」（時效性項目如促銷到期、政策生效日，改在「同步自查」欄請主編同步 feature-radar「⏰ 倒數中」）。

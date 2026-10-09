---
page: "entities/haiku-5-5"
kind: "entity"
type: "model"
status: "active（Claude 5.5 家族第三款模型，取代 Haiku 4.5；Haiku 4.5 無獨立頁，細節見 [[topics/model-comparison]]）"
domain: "🤖 模型"
last_updated: "2026-10-08"
last_news_update: "2026-10-08"
status_main: "active"
days_since_news: 1
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 1
inbound_links: 15
attribution_count: 13
attribution_last: "2026-10-08"
top_source: "google-news"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-22"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Haiku 5.5

**類型：** model
**狀態：** active（Claude 5.5 家族第三款模型，取代 Haiku 4.5；Haiku 4.5 無獨立頁，細節見 [[topics/model-comparison]]）
**領域：** 🤖 模型
**別名：** claude-haiku-5-5
**首次出現：** 2026-10-08（本站收錄；官方發布日 2026-10-07）
**最後更新：** 2026-10-08
**最後新聞更新：** 2026-10-08

> **Haiku 5.5 發布**（2026-10-08）
> 2026-10-07 官方發布：最便宜、最快、最具能力的小型模型，平均執行成本比 Haiku 4.5 降約 75%；精確牌價官方發布文未附具體數字，見 [[entities/haiku-5-5#你現在拿到的是什麼]]。

---

## 現況

**2026-10-07 最新**：Anthropic 發布 Claude Haiku 5.5（API ID `claude-haiku-5-5`），為 Claude 5.5 家族第三款模型，繼 Opus 5.5（09-22）、Sonnet 5.5（09-28）之後。官方定位為「目前最便宜、最快、最具能力的小型模型」，面向高流量、成本敏感的工作（摘要、壓縮、資料庫查詢、分類），與 Opus 5.5／Sonnet 5.5 搭配作編碼任務的 subagent 效果好；官方稱它也是迄今最快的模型，適合即時客服、瀏覽器操作等延遲敏感場景。平均執行成本比 Haiku 4.5 低約 75%（[官方發布文](https://www.anthropic.com/claude-haiku-5-5)，2026-10-07）。同批官方也將 Claude Sonnet 5.5 的快取讀取價砍半，定價細節見 [[entities/pricing]]。

精確 $/Mtok 牌價與 context 上限，官方發布文摘要未附具體數字，詳見下方「歷史記錄」⟨Q-01⟩；AWS、GitHub Copilot 同日同步上架（Reuters／VentureBeat，2026-10-07）。

---

## 你現在拿到的是什麼

> 本表比的是 Haiku 這一代（4.5 vs 5.5）；資料截至 2026-10-07（官方發布文）。Haiku 4.5 無獨立 entities 頁，對照數字取自 [[topics/model-comparison]]。

| 這一格 | Haiku 4.5（前代） | Haiku 5.5（現行） | 官方出處（查證日）|
|---|---|---|---|
| 現在誰是預設 | 輕量 worker，退役下限 2026-10-15 | 現行 Haiku；是否已成為各方案預設 worker，原文未提及 | 官方發布文（2026-10-07 查證）|
| 牌價（輸入／輸出，每百萬 token）| $1 ／ $5（官方確認，2026-08-20 查證） | 原文未附具體金額，僅稱「平均執行成本降約 75%」；精確值見⟨Q-01⟩ | 官方發布文（2026-10-07 查證）|
| 知識截止 | 原文未提及 | 原文未提及（2026-10-07 查證） | 官方發布文（2026-10-07 查證）|
| 會不會停掉 | 退役下限 2026-10-15（非確定停用日） | 尚無退役時程公告 | [[topics/model-comparison]]（2026-10-03 查證）|
| 從舊代升上去會壞什麼 | —（基準世代）| 官方發布文未提及破壞性變更；migration guide 待查 | 待補 |
| 官方推薦拿它做什麼 | real-time applications／sub-agent tasks | 高流量成本敏感任務（摘要、壓縮、DB 查詢、分類）；Opus 5.5／Sonnet 5.5 的編碼 subagent；即時客服、瀏覽器操作 | 官方發布文（2026-10-07 查證）|
| 我的方案能不能用 | 全方案可用 | 官方原文僅提及 Anthropic 一般發布；Pro／Max／Team／Enterprise 是否同步未載 | 待補 |

**表下細節**

- context 上限：三家媒體標題稱 1M（MarkTechPost、shattered.io、tech-insider.org），與 Haiku 4.5 的 200K 不同；僅標題可讀，無法讀取完整內文，官方發布文摘要未見此數字，不採信推算，見⟨Q-01⟩。
- 官方同批宣布 Sonnet 5.5 快取讀取價砍半，屬 Sonnet 定價事件非 Haiku 本身，細節見 [[entities/sonnet-5-5]]、[[entities/pricing]]。

---

## 跟它怎麼說話

官方 prompting 指南尚未發布。本次更新未見官方 prompting／migration 內容，待後續更新補上官方 [choosing-a-model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) 與 migration guide 的 Haiku 5.5 專屬段落。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥（Hacker News＋Blog／Simon Willison＋HN Repo Bridge 合計 1,005 分，3 個來源，2026-10-08 查核；同步 [[feature-radar]]）|
| 試用價值 | ⚡ 有條件推薦（精確牌價與 context 細節見上方表格）|
| 最適合 | 官方稱：高流量成本敏感任務（摘要、壓縮、分類、DB 查詢）、Opus 5.5／Sonnet 5.5 的編碼 subagent、即時客服／瀏覽器操作 |
| 不適合 | 待補 |

> 本表跟著 [[feature-radar]] 全覽表走；最新熱度以 [[feature-radar]] 為準。

---

## 核心功能

- 官方稱是目前最便宜、最快、最具能力的小型模型，平均執行成本比 Haiku 4.5 降約 75%
- 定位高流量成本敏感任務：摘要、壓縮、資料庫查詢、分類
- 可作 Opus 5.5／Sonnet 5.5 編碼任務的 subagent；亦適合即時客服、瀏覽器操作等延遲敏感場景
- AWS、GitHub Copilot 同日上架（Reuters／VentureBeat，2026-10-07）

---

## 相關議題

- [[topics/model-comparison]] — 這份工作該用哪個模型、Haiku 4.5 退役下限與選型細節
- [[entities/sonnet-5-5]] — 同批官方砍半快取讀取價的模型
- [[entities/opus-5-5]] — 官方稱可與之搭配作編碼 subagent 的旗艦
- [[entities/pricing]] — 精確牌價與分層費率
- [[topics/ai-agent-safety]] — Help Net Security 等 3 家媒體稱其抵抗隱藏指令注入能力比前代提升，安全框架細節見該頁
- [[topics/anthropic-business]] — Reuters 將此次發布放進「IPO 前擴充產品線」敘事
- [[feature-radar]] — 這禮拜官方動了什麼、熱度現在幾格

## 參考來源

- [Claude Haiku 5.5 官方發布文](https://www.anthropic.com/claude-haiku-5-5)（2026-10-07）
- [Claude Help Center Release Notes](https://support.claude.com/en/articles/12138966-release-notes)（內容變動偵測，含「Claude Haiku 5.5 launch」段，2026-10-08 查核）
- [Google News/VentureBeat：Anthropic launches Claude Haiku 5.5 with 90% API price reduction, matching GPT-6 Luna](https://news.google.com/rss/articles/CBMiugFBVV95cUxNOTFMTVFQOTJ2SmdCSGdjR2Z4Q2ZYMF9ncldZM3NUNTlEWUVOUERVUVVpdHdfQno4c3F3aWJ1WnIybnpYNGxnMmk5d3FCaUlkdkhCeHpPMENmRG81MEpBcGx5Y1kxY25GY3oxb3gzNGk1bDdOS0JwMkxFZ1hkUFI2M21GMWowTzc4VVJaLUNaajc5MGJrMTdtcXNJem93Q2lpSGFvYXJCbEFwN2hMTnY4bzcxdEswa29DWFE?oc=5)（2026-10-07）
- [Google News/Reuters：Anthropic launches third Claude 5.5 model, expanding AI lineup before planned IPO](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPbENadk1Lcm1iLUZOd0hYSmRZLWJHLTd0YjAwTExuMVozWW9McllnVWJuTHdPY3ZfRWJwVGdzMmpVaHhvODVVMkFMd0U0ejdyRjQxcEJMVzRqcTJqbWVaLXI5QnM1ckRSYmZVYjlBR2NqRTZaaW42QjFZMC00ZmxKOF9Fal9EODV2dEZnb1BPUDBlSFJrRDVtWkNLTWhacE04b3dyemlvckZTR3JmR0xONmxGb19hNU1tWFJMcVlJajNYUQ?oc=5)（2026-10-07）
- [Google News/Help Net Security：Anthropic's new budget model gets much better at ignoring hidden commands](https://news.google.com/rss/articles/CBMiekFVX3lxTE5aQlFGYTQwWEp6TkhTZnc2Q2hEQ2MyZGV6RkJNTWNwenVqYUxROVhtTjU5LXpxRXplYnlkZEFfbzllQldCQnZOWUJjS1ZEWDZSRTQyQzh3Q3F6VWw5MGY1anpCQWcxVm44QS1JUEVqYkdmdWZpeF8zREJB?oc=5)（2026-10-08）
- [Google News/MarkTechPost：Anthropic Releases Claude Haiku 5.5: A Small Model With 1M Context Priced at $0.10 per Million Input Tokens](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNQ004TDgwUFlDTU9VcE12Rl9IZDRVR0VNREdxdWQ0dTNnRlpQbmNVa25uZGhDN2FNTklfVENRZFN6cmpFWU1jdEwtV2VMcDV2Y2lCMDFLbXQwSThrRHRQaTdjZDEzQm03Rnhhc1BybEt2VEVUT0t2UUZmZ1MyMEVEX09ZV01UMXhxNFVldnBacWlGd3ZwUXlRaklsb0ttNlFnRm9zbExWM0Z5Qld4TnV2OHduaDZ4NWVsR3VONDZ0eDhXT25MejRuQk1oTF84RVItT0JvOTlHazhBdFlUeGRz)（2026-10-07）
- [Google News/MIXED Reality News：Claude Haiku 5.5 replaces Haiku 4.5, but Priority Tier does not come with it](https://news.google.com/rss/articles/CBMihwFBVV95cUxOZ005N19yTVQzUzA1dVlocUJVaEczR0Vwb05tMlZHNVRKakVQN0lBVGplZG5od1gtU014dmVuWG4tMjFHeUZYYlQ2bDg5QWJfSUdEdURsV1pPR2RlTUFWemVicnlldzhUbkxuazhPa3FnMkJnNzYxUXhUSnUzS3JMVFFEYWU1QXM?oc=5)（2026-10-08）
- [Google News/shattered.io：Claude Haiku 5.5: Anthropic Cuts API Costs 75%](https://news.google.com/rss/articles/CBMid0FVX3lxTE9Xdk8tc0NrZDY2LWdtbVhkZEg4SEJBYk9NZEozSFZsV3RJZXBBZjRzRnVlVlVVR2VWRDNMa3lxRUhEZGVJOGg0c3ZKMWZ6cXNSUlJhVi1GV1lVa3ZmcjVZbUhic0g4ZkFnUWNYMzlnMERzeEpPUm84?oc=5)（2026-10-07）
- [Google News/tech-insider.org：Claude Haiku 5.5 Slashes Price 75% to $0.10/M](https://news.google.com/rss/articles/CBMidkFVX3lxTE9SZEdHdzY1TDBveFYtWmI1WFA5MEZLaWtONVNIV0txTE1xOEwzZUF2T013WG1hc0ctSjRjM3ZoeV9zZDdKVXNTejdPeDVTLV84VHliVmM0VDFHMGR1ZkhKeUtPUWppTGtrZm9rRmpBdFBpdkVYLWc?oc=5)（2026-10-07）
- [[news/2026-10-08]]

## 歷史記錄

> 表格是索引，每一則的完整說明與來源在下方。❓ ⟨Q-01⟩ 這類記號代表「這一則我們還沒查到答案」，完整說明同樣在下方。

| 日期 | 事件 |
|------|------|
| 2026-10-08 | Help Net Security 等 3 家媒體稱抵抗隱藏指令注入能力比前代提升（僅標題可讀）；精確牌價與 1M context 聲稱 ❓待查證⟨Q-01⟩ |
| 2026-10-07 | 正式發布，Claude 5.5 家族第三款模型；官方稱成本比 Haiku 4.5 降約 75%；AWS、GitHub Copilot 同日上架；Reuters 將發布放進 IPO 前產品線擴張敘事 |

**歷史記錄細節**

- **2026-10-08**：Help Net Security 等 3 個來源（Google News，10/08 11:24 UTC）報導 Haiku 5.5 抵抗隱藏指令注入（prompt injection）的防禦力比前代顯著提升；原文僅標題可讀，具體測試方法與數字未見完整記載，不採信推算。完整安全框架分析見 [[topics/ai-agent-safety]]。
  - ⟨Q-01⟩ ❓ **待查證**（標 2026-10-08｜查 [[entities/haiku-5-5]]、0.10｜複 2026-10-22）｜**精確 $/Mtok 牌價與 1M context 官方發布文未附具體數字**：官方僅稱降約 75%；VentureBeat 稱降 90%；3 家標題稱 input $0.10／Mtok、1M context，皆僅標題可讀，口徑不一，不採信推算。
  - VentureBeat 稱定價已與 GPT-6 Luna 看齊，屬跨家比較，本頁不展開，相關快照見 [[topics/competitor-landscape]]；精確牌價更新見 [[entities/pricing]]。
- **2026-10-07**：Anthropic 發布 Claude Haiku 5.5（[官方發布文](https://www.anthropic.com/claude-haiku-5-5)，2026-10-07）。
  - 官方定位：最便宜、最快、最具能力的小型模型，面向高流量成本敏感任務（摘要、壓縮、DB 查詢、分類），與 Opus 5.5／Sonnet 5.5 搭配作編碼 subagent；平均執行成本比 Haiku 4.5 降約 75%
  - 同批官方將 Sonnet 5.5 快取讀取價砍半，屬 Sonnet 定價事件，細節見 [[entities/sonnet-5-5]]、[[entities/pricing]]
  - AWS、GitHub Copilot 同日同步上架（[AWS 官方文章](https://news.google.com/rss/articles/CBMiigFBVV95cUxOQkU2SklzNGNKdXpOWUpkMFJhVEZvbGpLWlpUeDIzakxtcE1HbVRFeGp5N3FDNXlRd21BWWwzd19Na3RadEpaVk9wY3luT3lBc2tQdk9EcVkwNEZ1RTZJeUlpaDlVaG42MWx6U2h2RERsWXA0RTk3eXlTUC1EVzNFQ25EVjBLQUlrYVE?oc=5)，2026-10-07）
  - Reuters 將此次發布放進「Anthropic 第三款 5.5 系列模型、IPO 前擴充產品線」敘事，屬商業脈絡，見 [[topics/anthropic-business]]（[Google News/Reuters](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPbENadk1Lcm1iLUZOd0hYSmRZLWJHLTd0YjAwTExuMVozWW9McllnVWJuTHdPY3ZfRWJwVGdzMmpVaHhvODVVMkFMd0U0ejdyRjQxcEJMVzRqcTJqbWVaLXI5QnM1ckRSYmZVYjlBR2NqRTZaaW42QjFZMC00ZmxKOF9Fal9EODV2dEZnb1BPUDBlSFJrRDVtWkNLTWhacE04b3dyemlvckZTR3JmR0xONmxGb19hNU1tWFJMcVlJajNYUQ?oc=5)，2026-10-07）
  - HN 互動合計 1,005 分（Hacker News＋Blog／Simon Willison＋HN Repo Bridge 3 個來源，2026-10-07），互動量高
  - Mezha 標題稱其效能超越 GPT-6 Luna（僅標題可讀，跨家比較不採信推算）

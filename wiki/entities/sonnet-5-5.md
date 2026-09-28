---
page: "entities/sonnet-5-5"
kind: "entity"
type: "model"
status: "active（現行 Sonnet；取代 [[entities/sonnet-5|Sonnet 5]] 成為 Anthropic API 預設，Sonnet 5 是否比照 Opus 5.5 模式列 Legacy 見 [[entities/sonnet-5]]）"
domain: "🤖 模型"
last_updated: "2026-09-28"
last_news_update: "2026-09-28"
status_main: "active"
days_since_news: 0
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 0
inbound_links: 16
attribution_count: 8
attribution_last: "2026-09-28"
top_source: "google-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Sonnet 5.5

**類型：** model
**狀態：** active（現行 Sonnet；取代 [[entities/sonnet-5|Sonnet 5]] 成為 Anthropic API 預設，Sonnet 5 是否比照 Opus 5.5 模式列 Legacy 見 [[entities/sonnet-5]]）
**領域：** 🤖 模型
**別名：** claude-sonnet-5-5
**首次出現：** 2026-09-28
**最後更新：** 2026-09-28
**最後新聞更新：** 2026-09-28

> **今日發布**（2026-09-28）
> Claude 5.5 家族第二款模型；Terminal-Bench 4.0 由 Sonnet 5 的 10.3% 躍升至 70.6%，成為 Anthropic API 預設 Sonnet，牌價維持 $2/$10。

---

## 現況

**2026-09-28 最新**：Anthropic 發布 Claude Sonnet 5.5（API ID `claude-sonnet-5-5`），為 Claude 5.5 家族第二款模型（首款為 09-22 發布的 [[entities/opus-5-5|Opus 5.5]]）。官方稱較 Sonnet 5「明顯升級」：速度快逾 30%、多數工作成本省最多 30%（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)，2026-09-28）。隨 Claude Code v2.1.284 更新，Sonnet 5.5 成為 **Anthropic API 預設 Sonnet 模型**；是否同步為 Claude Code CLI 本身的預設、[[entities/sonnet-5|Sonnet 5]] 是否比照 Opus 5.5 模式列為 Legacy，官方原文均未載明（[GitHub v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)，2026-09-28）。

官方定位：Opus 5.5 面向需審慎判斷的複雜工作，Sonnet 5.5 專攻「界定清楚的日常任務」——修 bug、產出文件／簡報／試算表，並對設計細節敏銳；官方另預告 **Claude Haiku 5.5**（面向高流量、成本敏感場景）將於未來數週內加入 5.5 家族，尚未發布。

定價分層細節見 [[entities/pricing]]，這份工作該用哪個模型見 [[topics/model-comparison]]。

---

## 你現在拿到的是什麼

> 本表比的是 Sonnet 這一代（5 vs 5.5）；資料截至 2026-09-28（官方發布文、GitHub v2.1.284 changelog）。

| 這一格 | Sonnet 5（前代） | Sonnet 5.5（現行） | 官方出處（查證日）|
|---|---|---|---|
| 現在誰是預設 | 曾為 Claude Code CLI 預設（v2.1.197 起）| Anthropic API 預設 Sonnet；是否同步為 CLI 預設官方未載 | GitHub v2.1.284 changelog（2026-09-28 查證）|
| 牌價（輸入／輸出，每百萬 token）| $2 ／ $10 | $2 ／ $10（不變，快取讀取 $0.20＝標準 0.1 倍）| 官方發布文＋GitHub changelog（2026-09-28 查證）|
| 知識截止 | 官方未載（2026-09-28 查證）| 官方未載（2026-09-28 查證；本站可讀摘要於此節截斷）| 官方發布文（2026-09-28 查證）|
| 會不會停掉 | 官方未載退役時程（2026-09-28 查證）| 尚無退役時程公告 | 官方發布文（2026-09-28 查證）|
| 從舊代升上去會壞什麼 | —（基準世代）| 官方 migration guide 尚未見完整記載（原文截斷）| 待補 |
| 官方推薦拿它做什麼 | 已非 API 預設 | 界定清楚的日常任務：修 bug、產出文件／簡報／試算表，設計細節敏銳 | 官方發布文（2026-09-28 查證）|
| 我的方案能不能用 | 同右，兩代同一套方案規則 | 官方原文僅提及 Anthropic API；Pro／Max／Team／Enterprise 是否同步未載 | 官方發布文（2026-09-28 查證）|

**表下細節**

- **牌價完全不變，靠速度換效率**：$2/$10 維持不動，官方以「速度快 30%＋多數工作省最多 30% 成本」表述升級，與 Opus 5.5 那次「牌價降 20%」的換代邏輯不同。
- **快取讀取 $0.20／Mtok＝基礎輸入價（$2）的標準 0.1 倍**，非 Fable 5.1／Mythos 5.1 的 0.025 倍優惠費率，見 [[entities/pricing]]。
- 官方發布文提及在另一項評測（疑似 GDPval 系列）「落後 Opus 5.5 兩分」，本站可讀摘要於此處截斷，benchmark 全名與雙方分數皆未見完整記載，不採信推算。

---

## 這些數字是誰量的

> 資料截至 2026-09-28。

| 官方拿來說的基準 | Sonnet 5.5 | Sonnet 5 |
|---|---|---|
| Terminal-Bench 4.0（agentic coding）| 70.6% | 10.3% |

**表下細節**

- 官方稱在 GDPval 系列某項評測「落後 Opus 5.5 兩分」，原始摘要於該處截斷，benchmark 全名與雙方分數未見完整記載，本頁不採信推算（官方發布文，2026-09-28）。
- **互動量偏低**：Hacker News 累計 46 分（2 個來源），遠低於 Opus 5.5 發布當日的 1,674 分；同日另有路透、TechCrunch、VentureBeat、The Decoder、SiliconANGLE 等至少 7 個來源報導，媒體覆蓋廣但社群討論熱度偏弱，訊號強度低。
- 路透報導將此次上線與 Anthropic 上市（IPO）籌備進度並列，屬商業脈絡，見 [[topics/anthropic-business]]。
- **跨家分數不進本頁**：見 [[topics/model-task-leaderboard]]。

**所以呢**：官方僅公布 Terminal-Bench 4.0 一項具體對照分數（10.3%→70.6%）；另一項宣稱的「差兩分」數據不完整，社群獨立複測尚未出現。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥（HN 46 分，發布日，訊號偏弱；媒體覆蓋廣）|
| 試用價值 | ⏳ 剛發布、資料不足（2026-09-28 判定）|
| 最適合 | 官方稱：界定清楚的日常任務、修 bug、文件／簡報／試算表產出 |
| 不適合 | 待補 |

> 本表跟著 [[feature-radar]] 全覽表走；最新熱度以 [[feature-radar]] 為準。

---

## 跟它怎麼說話

官方 prompting／migration 指南尚無可讀內容（2026-09-28）——原始摘要未載 Sonnet 5.5 專屬的 prompt／effort 建議。

---

## 核心功能

- 1M context（沿用 Sonnet 5 規格，官方發布文未特別提及變動）
- Claude Code v2.1.284 新增支援，API ID `claude-sonnet-5-5`
- 官方稱對設計細節（design）敏銳，適合產出文件、簡報、試算表

---

## 相關議題

- [[entities/sonnet-5]] — 前代，現況與是否列 Legacy 追蹤於此頁
- [[entities/opus-5-5]] — 同 5.5 家族首款模型，發布於 09-22
- [[entities/fable-5]] — 現行旗艦，5.5 家族外的最高階公開模型
- [[entities/pricing]] — 分層費率細節，官方定價頁同步改版
- [[entities/claude-code]] — v2.1.284 完整改動，含「Yes, but ask」新功能
- [[topics/model-comparison]] — 這份工作該用哪個模型、換一個實付差多少
- [[topics/model-task-leaderboard]] — 跨家排名，現在誰在前面
- [[topics/anthropic-business]] — 路透將此次發布與 IPO 籌備並列報導
- [[feature-radar]] — 這禮拜官方動了什麼、熱度現在幾格

## 參考來源

- [Claude Sonnet 5.5 官方發布文](https://www.anthropic.com/claude-sonnet-5-5)（2026-09-28）
- [[anthropics/claude-code] v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)（2026-09-28）
- [[news/2026-09-28]]

## 歷史記錄

> 表格是索引，每一則的完整說明與來源在下方。

| 日期 | 事件 |
|------|------|
| 2026-09-28 | 正式發布，Claude 5.5 家族第二款模型；Terminal-Bench 4.0 由 10.3%→70.6%；成為 Anthropic API 預設 Sonnet；牌價維持 $2/$10 |

**歷史記錄細節**

- **2026-09-28**：Anthropic 發布 Claude Sonnet 5.5，Claude Code v2.1.284 同步新增支援並設為 API 預設 Sonnet（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)；[GitHub v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)，2026-09-28）
  - Terminal-Bench 4.0：70.6%（前代 Sonnet 5 為 10.3%）；官方稱另在 GDPval 系列某評測落後 Opus 5.5 兩分，原文截斷未載完整名稱與分數
  - 牌價維持 $2/$10 每 Mtok、快取讀取 $0.20（標準 0.1 倍）；官方定價頁同步改版，分層費率細節見 [[entities/pricing]]
  - 官方預告 Claude Haiku 5.5 將於未來數週內加入 5.5 家族，尚未發布
  - 路透報導將此次上線與 Anthropic IPO 籌備進度並列；TechCrunch、VentureBeat、The Decoder、SiliconANGLE 及 Hacker News、Reddit 同日跟進，合計至少 7 個來源（Reuters，2026-09-28）
  - HN 互動 46 分（2 個來源），訊號偏弱

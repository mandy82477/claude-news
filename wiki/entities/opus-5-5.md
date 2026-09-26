---
page: "entities/opus-5-5"
kind: "entity"
type: "model"
status: "active（現行 Opus；取代 [[entities/opus-5|Opus 5]] 成為各方案預設，Opus 5 官方已改列 Legacy）"
domain: "🤖 模型"
last_updated: "2026-09-23"
last_news_update: "2026-09-23"
status_main: "active"
days_since_news: 3
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 3
inbound_links: 23
attribution_count: 11
attribution_last: "2026-09-23"
top_source: "google-news"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-07"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Opus 5.5

**類型：** model
**狀態：** active（現行 Opus；取代 [[entities/opus-5|Opus 5]] 成為各方案預設，Opus 5 官方已改列 Legacy）
**領域：** 🤖 模型
**別名：** claude-opus-5-5
**首次出現：** 2026-09-23（本站收錄；官方發布日 2026-09-22）
**最後更新：** 2026-09-23
**最後新聞更新：** 2026-09-23

> **最新動態**（2026-09-23）
> Anthropic 發布 Claude Opus 5.5，Claude Code v2.1.280 起設為預設 Opus；牌價降至 $4／$20 每 Mtok（較 Opus 5 降 20%），官方稱「運算成本降 40%」。同日 OpenAI 發布 GPT-6 Sol／Luna 應戰新一輪價格戰。

---

## 現況

**2026-09-23 最新**：Anthropic 發布 Claude Opus 5.5（API ID `claude-opus-5-5`），Claude Code v2.1.280 已將其設為預設 Opus 模型；Pro／Max／Team／Enterprise／API 的預設 Opus 同步改為 Opus 5.5（官方 models overview（2026-09-23 查證））。官方稱多數工作表現追平 [[entities/fable-5|Fable 5.1]]、運算成本降 40%（相對 Opus 5）；媒體另有「API 價格便宜 60%」一說，兩個百分比對照的基準不同，見下方「這些數字是誰量的」。[[entities/opus-5|Opus 5]] 與 Fable 5 同步改列 Legacy，仍可用（2026-09-23 查證）。

上線同時伴隨資安相關防護機制強化（The Verge 報導），紐約時報將此次發布放進近期 AI 安全爭論的脈絡報導；機制細節與爭議屬安全政策線，本頁僅記模型面，完整脈絡見 [[topics/ai-agent-safety]]。定價與方案內含見 [[entities/pricing]]，這份工作該用哪個模型見 [[topics/model-comparison]]。

---

## 你現在拿到的是什麼

> 本表比的是 Opus 這一代（5 vs 5.5）；資料截至 2026-09-23（官方 GitHub changelog、官方 models overview（2026-09-23 查證））。一格一個換代時會問的問題，兩欄是兩代的答案。

| 這一格 | Opus 5（Legacy） | Opus 5.5（現行） | 官方出處（查證日） |
|---|---|---|---|
| 現在誰是預設 | 否，Claude Code v2.1.280 起改預設 Opus 5.5 | 是——Pro／Max／Team／Enterprise／API 的預設 Opus | GitHub `v2.1.280` changelog；官方 models overview（2026-09-23 查證）|
| 牌價（輸入／輸出，每百萬 token）| $5 ／ $25 | $4 ／ $20（快取讀取 $0.20，為基礎輸入價 5%）| 官方 GitHub changelog；官方 models overview（2026-09-23 查證）|
| 知識截止 | 2026-05 | 2026-06（官方稱「可靠」知識截止）| 官方 models overview（2026-09-23 查證）|
| 會不會停掉 | 已改列 Legacy，退役**不早於 2027-07-24**（沿用既有查證值） | 退役**不早於 2027-09-22** | 官方 models overview（2026-09-23 查證）|
| 從舊代升上去會壞什麼 | —（基準世代） | **thinking 不可再關閉**（官方：no longer available with thinking switched off）；08-31 後新 API 帳號套 preserved thinking 反蒸餾 | 官方發布文（2026-09-25 查證）|
| 官方推薦拿它做什麼 | 已不再是預設 Opus | 官方稱多數工作表現追平 Fable 5.1；未另列「何時該升 Fable 5.1」的分界 | 官方發布文（2026-09-23 查證）|
| 我的方案能不能用 | 同右，兩代同一套方案規則 | Pro／Max／Team／Enterprise／API 皆為預設 Opus；Team standard 依 [[entities/pricing]]「同 Pro」慣例推得，官方未逐一列出 | 官方 models overview（2026-09-23 查證）|

**表下細節**

- **牌價降 20%，官方稱「運算成本降 40%」**：$5→$4、$25→$20 皆為降 20%；官方發布文另稱「costs 40% less to run than Opus 5」，兩個數字口徑不同（前者為牌價降幅，後者疑似另計入速度／效率），本頁不擅自換算，並陳見下方「這些數字是誰量的」。
- **快取讀取費率低於全站慣例值**：$0.20／Mtok＝基礎輸入價的 5%（0.05×），低於一般模型的 0.1× 慣例（近似 Fable 5.1／Mythos 5.1 的 0.025× 低費率處理，但非同一數字），乘數細節見 [[entities/pricing]]。
- **Pro／Max 用量上限同步調高**（Google News／MIXED Reality News，2026-09-23 報導），與預設模型換成 Opus 5.5 同批發生，實際換算後的每次執行成本是否也同步變化，本頁未見官方數字，暫不下結論。

---

## 這些數字是誰量的

> 資料截至 2026-09-25。**更正（2026-09-25，使用者提問查證）**：本節 09-23 版寫「官方未見具名基準與分數」是錯的——官方發布文有整張基準表，同時列 Fable 5.1、Opus 5、GPT-6 Astra、GPT-5.6 Sol 對照；當日僅讀到媒體轉述，未核對官方原文。

| 基準 | Opus 5.5 | Fable 5.1 | Opus 5 |
|---|---|---|---|
| Terminal-Bench 4.0 | 66.4% | 55.8% | 52.3% |
| FrontierCode v1.1（Main） | 54.4% | 50.3% | 48.0% |
| CursorBench 4.0 | 57.8% | 51.8% | 46.6% |
| GDPval-AA v2.1（Elo） | 1846 | 1735 | 1708 |
| AutomationBench | 40.0% | 31.4% | 26.9% |
| Humanity's Last Exam（tools） | 67.7% | 65.6% | 63.6% |
| Terminal-Bench-Science 0.1 | 58.7% | 52.6% | 29.0% |
| OSWorld 2.0（partial） | 81.8% | 80.7% | 74.0% |
| Chartography（tools） | 89.0% | 88.4% | 83.4% |

- **官方自己的但書**：「leads in agentic coding, computer use, and knowledge work」，但明寫實際使用上與 Fable 5.1 的差距比分數看起來小；另稱輸出比 Opus 5 快 30% 以上（[官方發布文](https://www.anthropic.com/claude-opus-5-5)，2026-09-25 查證）。
- **VentureBeat 稱「勝過 Fable 5.1、API 價格便宜 60%」**：「勝過」對得上官方表；「60%」是對 Fable 5.1 牌價（$10/$50）的比較，與官方「典型工作負載比 Opus 5 少花 40%」不是同一對照，並陳不選邊。
- **快取讀取 $0.20 是降 60%**（Opus 5 為 $0.50），與牌價降 20% 分開看。
- **HN 討論**（1,674 分，7 個來源同日交叉報導，2026-09-22）：屬互動量訊號，非能力數字。
- **跨家分數不進本頁**：GPT-6 Astra／GPT-5.6 Sol 欄位不抄進來；跨家「誰強」見 [[topics/model-task-leaderboard]] 與 [[topics/competitor-landscape]]。

**所以呢**：官方有具名基準表且全項領先前代；要看的是社群獨立複測，目前還沒有。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥（HN 1,674 分，發布日）|
| 試用價值 | ⏳ 剛發布、資料不足（2026-09-23 判定）|
| 最適合 | 待社群累積實測後補；官方定位同 Opus 5（數小時無人盯著的編碼任務、跨數十檔 refactor）|
| 不適合 | 待補 |

> 本表跟著 [[feature-radar]] 全覽表走；最新熱度以 [[feature-radar]] 為準。

---

## 核心功能

- **1M context、128K 最大輸出**（官方 models overview，2026-09-23 查證）
- **SDK 支援**：`anthropic-sdk-python` v1.8.0 新增 `claude-opus-5-5` 支援（2026-09-22 上架）
- **Claude Code 整合**：v2.1.280 新增 Opus 5.5 並設為預設 Opus；同批版本亦為全螢幕模式更多清單加入滑鼠支援（與模型本身無關，見 [[entities/claude-code]]）

---

## 相關議題

- [[entities/opus-5]] — 前代次旗艦，官方已改列 Legacy，仍可用
- [[entities/fable-5]] — 現任旗艦；官方稱 Opus 5.5 多數工作表現與其追平
- [[entities/mythos]] — 同權重無護欄版
- [[entities/sonnet-5]] — Claude Code 的整體預設，日常規模開發首選
- [[entities/pricing]] — 牌價 $4／$20、快取讀取費率、Pro／Max 用量上限調高
- [[topics/model-comparison]] — 這份工作該用哪個模型、換一個實付差多少
- [[topics/model-task-leaderboard]] — 跨家排名，現在誰在前面
- [[topics/competitor-landscape]] — 同日 GPT-6 Sol／Luna 發布的價格戰脈絡
- [[topics/ai-agent-safety]] — 資安防護機制強化與安全爭論脈絡
- [[entities/claude-code]] — v2.1.280 完整改動
- [[feature-radar]] — 這禮拜官方動了什麼、熱度現在幾格

## 參考來源

- [Claude Opus 5.5 官方發布文](https://www.anthropic.com/claude-opus-5-5)（2026-09-22）
- [[anthropics/claude-code] v2.1.280](https://github.com/anthropics/claude-code/releases/tag/v2.1.280)（2026-09-22）
- [anthropic-sdk-python v1.8.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.8.0)（2026-09-22）
- [MIXED Reality News：Claude Opus 5.5 undercuts Opus 5 at $4 per million tokens, and Pro and Max limits go up](https://mixed-news.com/en/claude-opus-5-5-price-4-per-million-tokens-usage-limits/)（2026-09-23）
- [VentureBeat：Anthropic releases Claude Opus 5.5, beating Fable 5.1 on key agentic benchmarks at 60% cheaper API price](https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price)（2026-09-22）
- [Fortune：What AI slowdown? OpenAI, Anthropic release dueling models as price wars heat up](https://fortune.com/2026/09/22/what-ai-slowdown-openai-anthropic-release-dueling-moreaffordable-models-as-ai-price-wars-heat-up/)（2026-09-22）
- [The Verge：Anthropic launches Claude Opus 5.5 with stricter safeguards for cybersecurity](https://www.theverge.com/ai-artificial-intelligence/998868/anthropic-claude-opus-5-5-cybersecurity)（2026-09-22）
- [The New York Times：Anthropic Releases a New A.I. Model, Opus 5.5, Amid Safety Debate](https://www.nytimes.com/2026/09/22/technology/anthropic-ai-model-safety.html)（2026-09-22）
- [Simon Willison：Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/)（2026-09-22）
- [[news/2026-09-23]]

## 歷史記錄

> 表格是索引，每一則的完整說明與來源在下方。🔎 ⟨Q-01⟩ 這類記號代表「已查官方一手來源，確認未載」，完整說明同樣在下方。

| 日期 | 事件 |
|------|------|
| 2026-09-23 | 正式發布（官方日期 09-22），取代 Opus 5 成為預設 Opus；牌價降 20%、官方稱運算成本降 40%；具名基準分數 🔎查無官方⟨Q-01⟩ |

**歷史記錄細節**

- **2026-09-23**：Anthropic 發布 Claude Opus 5.5，Claude Code v2.1.280 設為預設 Opus（[Anthropic](https://www.anthropic.com/claude-opus-5-5)；[GitHub](https://github.com/anthropics/claude-code/releases/tag/v2.1.280)，2026-09-23）
  - 1M context、128K 最大輸出，牌價 $4／$20 每 Mtok、快取讀取 $0.20／Mtok（官方 5%）；Pro／Max 用量上限同步調高（[MIXED Reality News](https://mixed-news.com/en/claude-opus-5-5-price-4-per-million-tokens-usage-limits/)，2026-09-23）
  - 同日 OpenAI 發布 GPT-6 Sol／Luna，Fortune 稱 AI 價格戰再度升溫，跨家比較不進本頁（[Fortune](https://fortune.com/2026/09/22/what-ai-slowdown-openai-anthropic-release-dueling-moreaffordable-models-as-ai-price-wars-heat-up/)，2026-09-22）
  - The Verge 報導隨附資安防護機制強化，NYT 將發布放進近期 AI 安全爭論脈絡報導；機制與爭論細節屬安全政策線，見 [[topics/ai-agent-safety]]（[The Verge](https://www.theverge.com/ai-artificial-intelligence/998868/anthropic-claude-opus-5-5-cybersecurity)；[NYT](https://www.nytimes.com/2026/09/22/technology/anthropic-ai-model-safety.html)，2026-09-22）
  - ⟨Q-01⟩ 🔎 **查無官方**（標 2026-09-23｜查 `claude-opus-5-5`、benchmark｜複 2026-10-07）｜**具名基準分數未見官方公布**：官方僅稱「多數工作表現追平 Fable 5.1」，未附具名基準或分數，與 Opus 5 發布時同批公布 CursorBench 等做法不同（2026-09-23 查證）

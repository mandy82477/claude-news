---
page: "entities/opus-5-5"
kind: "entity"
type: "model"
status: "active（現行 Opus；取代 [[entities/opus-5|Opus 5]] 成為各方案預設，Opus 5 官方已改列 Legacy）"
domain: "🤖 模型"
last_updated: "2026-10-03"
last_news_update: "2026-10-03"
status_main: "active"
days_since_news: 2
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 2
inbound_links: 25
attribution_count: 18
attribution_last: "2026-10-03"
top_source: "google-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
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
**最後更新：** 2026-10-03
**最後新聞更新：** 2026-10-03

> **「降智」說法有了查證時程**（2026-10-03）
> livenerf 已建立 Opus 5.5 第 0 天基準線並連測 30 天，最早約 10-24 才能下結論；在那之前，10-01 週熱門貼文的「近日失手」仍只是無量化指標的觀感。

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
- **社群反應正向但屬弱訊號**：[週熱門貼文](https://www.reddit.com/r/ClaudeAI/comments/1wqcara/aight_i_get_it_opus_55_is_actually_peak/)稱程式碼品質與可控性優於前代；另兩則（[複現實測](https://www.reddit.com/r/ClaudeAI/comments/1wovwao/jaw_literally_dropped_i_ran_the_prompt_from_the/)、[原展示貼文](https://www.reddit.com/r/ClaudeAI/comments/1wogab3/made_entirely_with_opus_55_321_of_openrouter_api/)）以約 $3–4 API 花費重現 Opus 5.5 專案。三則皆單則貼文、0 留言、無測試方法或量化指標，不構成獨立複測。
- **與上則相反：「降智」觀感回報，同屬弱訊號**：[週熱門貼文](https://www.reddit.com/r/ClaudeAI/comments/1wuw9bc/opus_55_nerfing_how_to_measure_how_to_spot_how_to/)稱 Opus 5.5 上線前 5–6 天在其複雜工作（自製 C++ 3D 引擎、軟體物理求解器、Blender MCP）表現穩定，近日起在原本能處理的任務上失手；未附測試方法或量化指標、0 留言，屬主觀觀感，不構成已驗證的能力下降；同類主張累計見 [[topics/code-quality-decline]]。
- **livenerf 的 30 天量測才剛開始**：dev.to 貼文稱已為 Opus 5.5 建立第 0 天基準線、每日重測連續 30 天，最早約 10-24 才能下結論（[dev.to](https://dev.to/axrisi/is-claude-opus-55-nerfed-a-30-day-benchmark-started-the-clock-151d)，2026-09-30；3 讚，題組與評分方法未見載）；尚無結果，不能拿來支持或反駁上則。
- **跨家分數不進本頁**：GPT-6 Astra／GPT-5.6 Sol 欄位不抄進來；跨家「誰強」見 [[topics/model-task-leaderboard]] 與 [[topics/competitor-landscape]]。
- **VentureBeat：em-dash 用量降 99%，但仍測得 2,548 處「AI 寫作特徵」**：報導稱 Opus 5.5 回覆中 em-dash（—）出現頻率較前代大幅降低、讀來更像真人，但同一批測試仍抓到 2,548 處其他「AI 寫作痕跡」；原文僅標題可讀，測試方法、樣本數與痕跡定義均未見完整記載，不採信推算（[VentureBeat](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNGpWZl9FaU93X1NjTFdHWHhmdmZlX3pLd3FDT2NxX0FZY2JKM1NZb1dZSUM5d1NsRUhUSjdOb3BFWGxNZmlBV2VpbTRXOHF3TWVMLWc0WmVxZnVKZkFDdGtzaDdnN0xGeGZGcl9yYTRoLXRtaUhBU1FranZGVUVVVS1jLWVrdVJ6NGhCMy1CRC1ndUlOenFwUFc0QjExdzVTOFBkT1FueFUyNlMwNVhWYTJ5eE51ZE5YNEZyM0JnVERqazNpbTFsMnhwd2VvU2RLV3FV?oc=5)，2026-09-30）

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

## 跟它怎麼說話

官方 prompting 指南：[Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)（查證 2026-10-03）。

- **effort 預設 `medium`（Opus 5 是 `high`），且同一級它比 Opus 5 想更多**：官方測試 `medium` 追平或超過 Opus 5 的 `high`，而沿用 Opus 5 的 effort 值換到的是更長的回合與更多 output token；要少想就降級，官方明說降 effort 比用提示叫它少想可靠。
- **要刪系統提示裡「think carefully before answering」這類句子**：模型自己決定想多久，官方在聊天產品實測刪掉該行讓回覆更早開始、品質無明顯下降。
- **原本跑 `thinking: disabled` 的整合要改從 `low` 起量，並刪掉「把推理寫進回覆」當替代品的指令**：那類提示會吃 `reasoning_extraction` 拒答，改設 `display: "summarized"` 從 thinking 區塊讀。
- **非監督 agent 迴圈要把「只有文字、沒有 tool call」的回合當成報告而不是完工**：它會邊做邊回報、而那種回合的 `stop_reason` 是 `end_turn`，把它當結束的 harness 會停在半路；官方建議在系統提示末端點名你不要的那幾種提早收手。
- **使用者貼進來的文字要用帶同一組隨機 id 的 `<pasted_content>` 標記並在系統提示說明**：它對間接注入的抵抗力強過任何前代 Opus，但貼上內容這一塊要靠這個標記才吃得到。

**表下細節**

- 與相鄰世代相反的那一邊：本頁要**刪**「think carefully」，[[entities/fable-5]] 則要**加**「你在自主執行」那段；effort 旋鈕的通用建議見 [[topics/model-comparison]]「Effort dial 細節」。
- 從 Opus 5 升上來的四項破壞性 API 變更不在本節，走官方 [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#migrating-from-claude-opus-5)。

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
- [Reddit r/ClaudeAI：Aight I get it, Opus 5.5 is actually peak](https://www.reddit.com/r/ClaudeAI/comments/1wqcara/aight_i_get_it_opus_55_is_actually_peak/)（週熱門，2026-09-26）
- [Reddit r/ClaudeAI：Jaw literally dropped...](https://www.reddit.com/r/ClaudeAI/comments/1wovwao/jaw_literally_dropped_i_ran_the_prompt_from_the/)（週熱門，2026-09-24）
- [Reddit r/ClaudeAI：Made entirely with Opus 5.5 + $3.21 of OpenRouter API usage](https://www.reddit.com/r/ClaudeAI/comments/1wogab3/made_entirely_with_opus_55_321_of_openrouter_api/)（週熱門，2026-09-23）
- [Google News/VentureBeat：Claude Opus 5.5 uses em-dashes 99% less often and sounds more human — but still exhibits 2,548 AI writing tells](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNGpWZl9FaU93X1NjTFdHWHhmdmZlX3pLd3FDT2NxX0FZY2JKM1NZb1dZSUM5d1NsRUhUSjdOb3BFWGxNZmlBV2VpbTRXOHF3TWVMLWc0WmVxZnVKZkFDdGtzaDdnN0xGeGZGcl9yYTRoLXRtaUhBU1FranZGVUVVVS1jLWVrdVJ6NGhCMy1CRC1ndUlOenFwUFc0QjExdzVTOFBkT1FueFUyNlMwNVhWYTJ5eE51ZE5YNEZyM0JnVERqazNpbTFsMnhwd2VvU2RLV3FV?oc=5)（2026-09-30）
- [Reddit r/ClaudeAI：Opus 5.5 nerfing - how to measure, how to spot, how to sue](https://www.reddit.com/r/ClaudeAI/comments/1wuw9bc/opus_55_nerfing_how_to_measure_how_to_spot_how_to/)（週熱門，2026-10-01）
- [dev.to：Is Claude Opus 5.5 nerfed? A 30-day benchmark started the clock](https://dev.to/axrisi/is-claude-opus-55-nerfed-a-30-day-benchmark-started-the-clock-151d)（2026-09-30）
- [[news/2026-09-23]]
- [[news/2026-09-27]]
- [[news/2026-09-30]]
- [[news/2026-10-01]]

## 歷史記錄

> 表格是索引，每一則的完整說明與來源在下方。🔎 ⟨Q-01⟩ 這類記號代表「已查官方一手來源，確認未載」，完整說明同樣在下方。

| 日期 | 事件 |
|------|------|
| 2026-10-03 | livenerf 為「降智」說法建立第 0 天基準線，連測 30 天，最早約 10-24 下結論（日報 09-30 貼文）|
| 2026-10-01 | Reddit 週熱門貼文稱上線前 5–6 天表現佳、近日起在複雜任務上失手，無量化指標，弱訊號 |
| 2026-09-30 | VentureBeat 稱 em-dash 用量降 99%、仍測得 2,548 處 AI 寫作特徵（方法論未載）|
| 2026-09-23 | 正式發布（官方日期 09-22），取代 Opus 5 成為預設 Opus；牌價降 20%、官方稱運算成本降 40%；具名基準表見「這些數字是誰量的」（2026-09-25 查證）|

**歷史記錄細節**

- **2026-10-03**：dev.to 貼文（09-30 發）稱 livenerf 針對 Opus 5.5「變笨」傳言建立第 0 天基準線，連續測 30 天，最早約 10-24 可下結論（[dev.to](https://dev.to/axrisi/is-claude-opus-55-nerfed-a-30-day-benchmark-started-the-clock-151d)，2026-09-30；3 讚，題組與評分方法未見載，尚無結果）
- **2026-10-01**：Reddit r/ClaudeAI 週熱門貼文稱 Opus 5.5 上線前 5–6 天在複雜任務（自製 C++ 3D 引擎、軟體物理求解器、Blender MCP）表現穩定，近日起在原本能處理的任務上失手（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wuw9bc/opus_55_nerfing_how_to_measure_how_to_spot_how_to/)，2026-10-01；0 留言，無測試方法或量化指標，屬主觀觀感回報，不採信推算是否構成能力下降）
- **2026-09-30**：VentureBeat 報導稱 Opus 5.5 回覆的 em-dash 用量較前代降 99%、讀起來更像真人，但同一批測試仍測得 2,548 處其他「AI 寫作特徵」（[VentureBeat](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNGpWZl9FaU93X1NjTFdHWHhmdmZlX3pLd3FDT2NxX0FZY2JKM1NZb1dZSUM5d1NsRUhUSjdOb3BFWGxNZmlBV2VpbTRXOHF3TWVMLWc0WmVxZnVKZkFDdGtzaDdnN0xGeGZGcl9yYTRoLXRtaUhBU1FranZGVUVVVS1jLWVrdVJ6NGhCMy1CRC1ndUlOenFwUFc0QjExdzVTOFBkT1FueFUyNlMwNVhWYTJ5eE51ZE5YNEZyM0JnVERqazNpbTFsMnhwd2VvU2RLV3FV?oc=5)，2026-09-30；原文僅標題可讀，方法論未見完整記載，不採信推算）
- **2026-09-23**：Anthropic 發布 Claude Opus 5.5，Claude Code v2.1.280 設為預設 Opus（[Anthropic](https://www.anthropic.com/claude-opus-5-5)；[GitHub](https://github.com/anthropics/claude-code/releases/tag/v2.1.280)，2026-09-23）
  - 1M context、128K 最大輸出，牌價 $4／$20 每 Mtok、快取讀取 $0.20／Mtok（官方 5%）；Pro／Max 用量上限同步調高（[MIXED Reality News](https://mixed-news.com/en/claude-opus-5-5-price-4-per-million-tokens-usage-limits/)，2026-09-23）
  - 同日 OpenAI 發布 GPT-6 Sol／Luna，Fortune 稱 AI 價格戰再度升溫，跨家比較不進本頁（[Fortune](https://fortune.com/2026/09/22/what-ai-slowdown-openai-anthropic-release-dueling-moreaffordable-models-as-ai-price-wars-heat-up/)，2026-09-22）
  - The Verge 報導隨附資安防護機制強化，NYT 將發布放進近期 AI 安全爭論脈絡報導；機制與爭論細節屬安全政策線，見 [[topics/ai-agent-safety]]（[The Verge](https://www.theverge.com/ai-artificial-intelligence/998868/anthropic-claude-opus-5-5-cybersecurity)；[NYT](https://www.nytimes.com/2026/09/22/technology/anthropic-ai-model-safety.html)，2026-09-22）
  - **具名基準表**：官方發布文附完整基準表（Terminal-Bench 4.0、FrontierCode 等九項，全項領先 Opus 5、Fable 5.1），見本頁「這些數字是誰量的」（[Anthropic](https://www.anthropic.com/claude-opus-5-5)，2026-09-25 查證）

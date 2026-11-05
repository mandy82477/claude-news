---
page: "entities/sonnet-5-5"
kind: "entity"
type: "model"
status: "active（現行 Sonnet；Claude Code 的 `sonnet` 別名指向它，各方案預設是 [[entities/opus-5-5|Opus 5.5]]；前代 [[entities/sonnet-5|Sonnet 5]] 已列 Legacy）"
domain: "🤖 模型"
last_updated: "2026-11-05"
last_news_update: "2026-10-25"
status_main: "active"
days_since_news: 11
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 11
inbound_links: 32
attribution_count: 15
attribution_last: "2026-10-25"
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

Anthropic 現行的中階 Claude 模型，2026-09-28 發布，API ID `claude-sonnet-5-5`。

**類型：** model
**狀態：** active（現行 Sonnet；Claude Code 的 `sonnet` 別名指向它，各方案預設是 [[entities/opus-5-5|Opus 5.5]]；前代 [[entities/sonnet-5|Sonnet 5]] 已列 Legacy）
**領域：** 🤖 模型
**別名：** claude-sonnet-5-5
**首次出現：** 2026-09-28
**最後更新：** 2026-11-05
**最後新聞更新：** 2026-10-25

本頁回答：Claude Sonnet 5.5 是什麼、在 Claude Code 與 API 怎麼拿到（預設、別名、effort）、從 Sonnet 5 換過來差在哪與會壞什麼、官方拿哪些數字說它好、prompt 要改哪幾句；選型看 [[topics/model-comparison]]，費率看 [[entities/pricing]]。

> **在 Claude Code 怎麼用到它**（2026-11-05）
> - **預設不是它**：各方案預設 Opus 5.5。
> - **要用就選**：`/model sonnet`（需 v2.1.284+；限 Anthropic API 與訂閱方案，Bedrock 等雲平台的 `sonnet` 指舊版，要寫完整 ID），effort 預設 medium。
> - **從 Sonnet 5 換來**：5 項 API 變更回 400、1 項不報錯，見[[entities/sonnet-5-5#從 Sonnet 5 換過來會壞什麼|逐項清單]]。

---

## 現況

**2026-11-05 查官方**：Claude Code 各方案預設是 [[entities/opus-5-5|Opus 5.5]]，Sonnet 5.5 要用 `/model sonnet` 或 `--model` 選；被資安分類器標記的請求會自動改跑 [[entities/sonnet-5|Sonnet 5]]（[Claude Code model-config](https://code.claude.com/docs/en/model-config)）。最近一則新聞是 10-25 多款模型錯誤率升高約 30 分鐘，見 [[#歷史記錄]]。

2026-09-28 發布，是 5.5 家族第二款（[[entities/opus-5-5|Opus 5.5]] 09-22、[[entities/haiku-5-5|Haiku 5.5]] 10-07）。官方稱比 Sonnet 5 快 30% 以上、多數工作省最多 30%，定位「界定清楚的日常任務」：修 bug、產出文件／簡報／試算表，官方另稱它對設計很有眼光（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)）。該選哪個模型見 [[topics/model-comparison]]，費率見 [[entities/pricing]]。

---

## 你現在拿到的是什麼

> 本表比的是 Sonnet 這一代（5 vs 5.5）；資料截至 2026-11-05（兩代官方模型頁、What's new、Claude Code model-config）。

| 這一格 | Sonnet 5（Legacy） | Sonnet 5.5（現行） | 官方出處（查證日）|
|---|---|---|---|
| 現在誰是預設 | v2.1.280 前是 Pro 與 Team Standard 的 Claude Code 預設 | 不是任何方案的預設（各方案預設 Opus 5.5）；`sonnet` 別名指向它，需 v2.1.284 以上 | Claude Code model-config（2026-11-05 查證）|
| 牌價（輸入／輸出，每百萬 token）| $2 ／ $10；快取讀取 $0.20 | $2 ／ $10；快取讀取 **$0.10**（Sonnet 5 的一半）；5 分鐘快取寫入 $2.50、1 小時 $4 | 兩代官方模型頁（2026-11-05 查證）|
| context 與最大輸出 | 1M ／ 128K（Batch beta 300K） | 同左 | 兩代官方模型頁（2026-11-05 查證）|
| 知識截止 | Jan 2026 | Jun 2026 | 兩代官方模型頁（2026-11-05 查證）|
| 會不會停掉 | Legacy，仍可用；退役不早於 2027-06-30 | 退役不早於 2027-09-28 | 兩代官方模型頁（2026-11-05 查證）|
| 從舊代升上去會壞什麼 | —（基準世代）| 5 項 API 變更會回 400、1 項不報錯但回應形狀改變；逐項見 [[#從 Sonnet 5 換過來會壞什麼]] | 官方 What's new（2026-11-05 查證）|
| 官方推薦拿它做什麼 | 已被取代，官方建議遷移到 Sonnet 5.5 | 速度與智慧的最佳組合；界定清楚的日常任務：修 bug、產出文件／簡報／試算表 | 官方發布文（2026-09-28 查證）；What's new（2026-11-05 查證）|
| 我的方案能不能用 | 各平台仍上架 | Claude Code 各方案可用 `/model sonnet` 選；Claude API 全部客戶、Bedrock、Claude Platform on AWS、Google Cloud、Foundry 皆上架 | model-config、What's new（2026-11-05 查證）|

**補充**

- **`sonnet` 別名看平台**：Anthropic API 與訂閱方案指 Sonnet 5.5；Claude Platform on AWS 指 Sonnet 4.6，Bedrock、Google Cloud、Foundry 指 Sonnet 4.5，在這些平台要寫完整 ID（[model-config](https://code.claude.com/docs/en/model-config)，2026-11-05 查證）。
- **effort 有兩個預設**：Claude API 是 `high`，Claude Code 與 Claude app 是 `medium`（[模型頁](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)、[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)，2026-11-05 查證）；級距怎麼選見 [[#跟它怎麼說話]]。
- **牌價不變，官方稱多數工作省最多 30%**：tokenizer 與 Sonnet 5 相同，同一段文字 token 數不變（[What's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)）；省在哪官方沒說（細節未載）。
- **快取讀取 $0.10 是發布時就定的價**：官方 [migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) 寫明是 Sonnet 5 的一半；乘數與 Batch 細節見 [[entities/pricing]]。

---

## 從 Sonnet 5 換過來會壞什麼

官方 [What's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) 列了 5 項會讓既有 Sonnet 5 程式出錯的變更，和 1 項不報錯、只改回應形狀的變更（2026-11-05 查證）。換 model ID 前逐項對一遍：

- **關掉 thinking 要改寫法**：送 `thinking: {"type": "disabled"}` 回 400，改送 `"between_tools"`；它只收 `low`／`medium`／`high` effort，`xhigh`／`max` 要用 adaptive（[官方](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#turn-off-up-front-thinking)）。
- **強制工具呼叫回 400**：`tool_choice` 設 `any` 或指定 `tool` 會被拒，只剩 `auto` 與 `none`；要工具輸入合 schema，改用 `strict: true` 或 structured outputs（[官方](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#forced-tool-use-is-not-supported)）。
- **thinking block 綁模型與對話**：改過 system、tools 或先前訊息後再回放它的 thinking block，2026-08-31 起建立的帳號會回 400；對話要只增不改（[官方](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#thinking-blocks-are-tied-to-the-model-that-produced-them)）。
- **Claude API 不收 `computer_20251124`**：回 400，改用 `computer_toolset_20260801`；Bedrock 仍收舊版（[官方](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#computer-20251124-is-not-supported)）。
- **advisor 少了四個搭檔**：它當執行者時，Opus 4.8、Opus 4.7、Sonnet 5、Haiku 5.5 當 advisor 會回 400（[官方](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#advisor-tool-pairings)）。
- **不報錯的那一項：工具呼叫之間的文字改走 thinking block**：預設 `display: "omitted"` 下內容是空的，把這段文字串流給使用者的前端會在工具呼叫間變安靜；設 `thinking.display`，或改用 `between_tools`（[官方](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#text-between-tool-calls)）。

**換過來還會遇到的事**

- **Claude Code 裡被標記的請求會換模型**：資安旗標的請求自動改跑 Sonnet 5，生物旗標直接拒答；`/config` 選「Ask each time」或設 `switchModelsOnFlag: false`，改成每次問你（[model-config](https://code.claude.com/docs/en/model-config)）。
- **API 端可自己開 fallback**：server-side fallback（beta，`fallbacks: "default"`）把 `cyber`、`frontier_llm` 拒答重試到 Sonnet 5，其他類別不重試（[What's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#refusals-fallback-and-billing)）。
- **最小可快取 prompt 從 1,024 降到 512 token**：較短的 prompt 也能進快取（[What's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)）。
- **設 `temperature`／`top_p`／`top_k` 回 400**：Sonnet 5 本來就是如此，從 Sonnet 4.x 跳上來的才會撞到（兩代[模型頁](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)，2026-11-05 查證）。
- **兩則媒體報導對得上官方**：MIXED Reality News（09-30）「five ways, one fails silently」與上列 5＋1 結構一致（僅標題，逐項未核）；mixed-news.com（10-01）的「被降回 Sonnet 5」即上述資安旗標改跑。

---

## 這些數字是誰量的

> 資料截至 2026-11-05（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)基準表）。分數由官方提交，未見第三方複跑。

| 官方拿來說的基準 | Sonnet 5.5 | Sonnet 5 | Opus 5.5 |
|---|---|---|---|
| Terminal-Bench 4.0 | 70.6% | 10.3% | 66.4% |
| FrontierCode 1.1（Main） | 46.2%（max）／52.1%（xhigh） | 42.4% | 54.4% |
| CursorBench 4.0 | 55.5% | 34.1% | 57.8% |
| GDPval-AA v2.1 | 1844 | 1449 | 1846 |
| AA-Briefcase v1.1 | 1811 | 1359 | 1822 |
| Humanity's Last Exam（with tools） | 64.5% | 54.9% | 67.7% |
| OSWorld 2.1（partial） | 80.1% | 57.0% | 81.8% |
| Chartography（no tools） | 61.6% | 15.6% | 64.4% |

- **相對 Opus 5.5**：Terminal-Bench 4.0 高 4.2 個百分點，其餘 7 項落後，百分比項差 1.7–3.2 個百分點（FrontierCode 取 xhigh 差 2.3、取 max 差 8.2），分數制的 GDPval-AA 差 2、AA-Briefcase 差 11；Opus 5.5 那一側的完整表見 [[entities/opus-5-5#這些數字是誰量的]]。
- **effort 設定不一**：官方註腳寫明 Terminal-Bench 4.0 的 Opus 5.5 是 xhigh effort 的成績；FrontierCode 的 Sonnet 5.5 列了 max 與 xhigh 兩個數，max 反而較低（註腳稱 max 下較常自跑 code review，導致逾時或多改；52.1% 對應 xhigh 依註腳推得）。
- **社群實測稱與 Opus 5.5 難以分辨**：同一組 skills 各跑 3 次，發文者稱看不出差異（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wtend0/tested_sonnet_55_vs_opus_55_with_the_same_skills/)，2026-09-29；0 留言、未附分數，單一社群回報）。
- **跨家分數不進本頁**：官方表另列 GPT-6 Sol，跨家比較見 [[topics/model-task-leaderboard]]。

---

## 熱度與試用價值

社群熱度與試用判定以 [[feature-radar]] 全覽表的 Sonnet 5.5 那一列為準。

---

## 跟它怎麼說話

官方 prompting 指南：[Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)（查證 2026-10-03）。

- **effort 級距已重新校準、與 Sonnet 5 不等量，要重掃**：agentic coding 與多步工具從 `medium` 起、較難較長的再升 `high`；聊天等重延遲的工作從 `medium` 或 `low` 起；官方明說 `medium` 以上它幾乎每則回覆都會先想一下、連招呼也算，首字延遲就是這樣來的；「叫它少想」不可靠、要降級。
- **`low` effort 下它會把改完的程式回報為完成卻沒跑真正的檢查**：加官方那段「改到可執行的程式就要跑真實檢查（測試／型別檢查／build）」，官方測得略增成本、任務品質無可測變化。
- **`low`／`medium` 的長 agentic 任務它會中途停下來問**：先升 effort，或加「做到使用者要的都做完為止」那段；反過來在 `xhigh`／`max` 它會自己開額外的 review 輪甚至派 reviewer subagent，要加「做完就停」那段，官方測得省約三分之一成本而品質不變。
- **要刪「hold all findings for the final response」**：它在工具呼叫之間本來就會寫進度筆記，留著這句會互相打架；前端因此變安靜怎麼處理見 [[#從 Sonnet 5 換過來會壞什麼]]。
- **不要把使用者中途輸入放進 `tool_result`，也不要在每次工具結果後加 token 倒數**：它受過抵抗間接注入的訓練，會把那種位置的文字當成假冒使用者的注入而忽略或要求確認。

**補充**

- 與相鄰世代相反的那一邊：本頁 `low` effort 的問題是**跳過驗證**，[[entities/fable-5]] 的 `low` 問題是**搜尋觸發變少**；effort 旋鈕的通用建議見 [[topics/model-comparison]]「Effort dial 細節」。

---

## 相關議題

- [[entities/sonnet-5]] — 前代，官方已列 Legacy；Claude Code 裡被資安旗標的請求會自動改跑它
- [[entities/opus-5-5]] — Claude Code 各方案的預設模型；同 5.5 家族首款，09-22 發布
- [[entities/haiku-5-5]] — 同 5.5 家族的輕量款，10-07 發布
- [[entities/fable-5]] — 現行旗艦，5.5 家族外的最高階公開模型
- [[entities/pricing]] — 精確牌價、快取與 Batch 乘數
- [[entities/claude-code]] — v2.1.284 完整改動，含「Yes, but ask」新功能
- [[topics/model-comparison]] — 這份工作該用哪個模型、換一個實付差多少
- [[topics/model-task-leaderboard]] — 跨家排名，現在誰在前面
- [[topics/anthropic-ipo]] — 路透將此次發布與 IPO 籌備並列報導
- [[feature-radar]] — 這禮拜官方動了什麼、熱度現在幾格

## 參考來源

- [Claude Sonnet 5.5 官方發布文](https://www.anthropic.com/claude-sonnet-5-5)（2026-09-28；基準表 2026-11-05 查證）
- [Claude Sonnet 5.5 模型頁](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)（2026-11-05 查證）
- [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)（2026-11-05 查證）
- [Claude Sonnet 5.5 migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)（2026-11-05 查證）
- [Claude Code：Model configuration](https://code.claude.com/docs/en/model-config)（2026-11-05 查證）
- [Claude Sonnet 5 模型頁](https://platform.claude.com/docs/en/models/sonnet-5/overview)（2026-11-05 查證）
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)（2026-10-03 查證）
- [[anthropics/claude-code] v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)（2026-09-28）
- [Simon Willison：Claude Sonnet 5.5](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/)（2026-09-28）
- [Reddit r/ClaudeAI：Tested Sonnet 5.5 vs Opus 5.5 with the same skills](https://www.reddit.com/r/ClaudeAI/comments/1wtend0/tested_sonnet_55_vs_opus_55_with_the_same_skills/)（2026-09-29）
- [Google News/MIXED Reality News：Claude Sonnet 5.5 breaks Sonnet 5 code in five ways, and one fails silently](https://news.google.com/rss/articles/CBMiigFBVV95cUxNSGplNGg4aERiNE9YSm90SE1CZkNuMkFxWk5feFJCdnptTjhqdnpKZHNLNVhhMWFRSXMzV2NsdXR1VDBCdHhuREw5WW1NV2pUZmVGaHJvOHpxYmJkQVBDTnBObmdyVExQWHpfc0NGYlV6dUd0MlpiX2Njb2JlT0wyRHJQdktSQlNZd0E?oc=5)（2026-09-30）
- [Google News/mixed-news.com：Claude Sonnet 5.5 can drop you to Sonnet 5 over something you never typed](https://news.google.com/rss/articles/CBMif0FVX3lxTFBFcVJCd0NrVEZkeDZxTHJsakdDWXJXRVZ4NzVTNTJ5VjhFV0pOZVhsajYtRXR1cERpOWdaZ0lLeXYxQk16T3VORE4ybVVFdUsyemVrUmFTNi13Y2M1SHF1a055M0l4TVlHaEZGdkFuc3JmSkVPX2VZa0owQ2RrQVE?oc=5)（2026-10-01）
- [[news/2026-09-28]]
- [[news/2026-09-29]]
- [[news/2026-09-30]]
- [[news/2026-10-01]]

## 歷史記錄

> 表格是索引，每一則的完整說明與來源在下方。

| 日期 | 事件 |
|------|------|
| 2026-10-25 | Anthropic Status：Sonnet 5.5 等多款模型錯誤率升高，06:05–06:35 UTC，07:53 UTC 已解決 |
| 2026-10-01 | mixed-news.com 稱工作階段可能被自動降回 Sonnet 5；11-05 查官方：是資安旗標請求的自動改跑，可改成每次詢問 |
| 2026-09-30 | MIXED Reality News 稱升級有 5 處行為差異、1 處靜默失敗；與官方 What's new 的 5＋1 清單結構一致（11-05 查證） |
| 2026-09-29 | Reddit 使用者同組 skills 各跑 3 次，稱與 Opus 5.5 難以分辨；HN 互動回升至 853 分 |
| 2026-09-28 | 正式發布，Claude 5.5 家族第二款模型；Terminal-Bench 4.0 由 10.3%→70.6%；Claude Code v2.1.284 起可選；牌價維持 $2/$10 |

**歷史記錄細節**

- **2026-10-25**：Anthropic Status 通報 Sonnet 5.5 等多款模型錯誤率升高，06:05–06:35 UTC（約 30 分鐘），07:53 UTC 已解決；受影響模型清單未完整列出。同日另有一起獨立事件影響 Fable 5.1，見 [[entities/fable-5]]（[Anthropic Status](https://status.claude.com/incidents/334jvgbrc4ff)，2026-10-25）
- **2026-10-01**：mixed-news.com 報導 Sonnet 5.5 工作階段可能在使用者未主動輸入下被自動降回 Sonnet 5（[mixed-news.com](https://news.google.com/rss/articles/CBMif0FVX3lxTFBFcVJCd0NrVEZkeDZxTHJsakdDWXJXRVZ4NzVTNTJ5VjhFV0pOZVhsajYtRXR1cERpOWdaZ0lLeXYxQk16T3VORE4ybVVFdUsyemVrUmFTNi13Y2M1SHF1a055M0l4TVlHaEZGdkFuc3JmSkVPX2VZa0owQ2RrQVE?oc=5)，2026-10-01；僅標題）
  - 2026-11-05 查官方 [model-config](https://code.claude.com/docs/en/model-config)：Claude Code 裡被資安分類器標記的請求會自動改跑 Sonnet 5，可改成每次詢問，見 [[#從 Sonnet 5 換過來會壞什麼]]
- **2026-09-30**：MIXED Reality News 報導從 Sonnet 5 升級會在五種情境出現行為差異，其中一種無錯誤訊息即靜默失敗，建議升級前先跑回歸測試（[MIXED Reality News](https://news.google.com/rss/articles/CBMiigFBVV95cUxNSGplNGg4aERiNE9YSm90SE1CZkNuMkFxWk5feFJCdnptTjhqdnpKZHNLNVhhMWFRSXMzV2NsdXR1VDBCdHhuREw5WW1NV2pUZmVGaHJvOHpxYmJkQVBDTnBObmdyVExQWHpfc0NGYlV6dUd0MlpiX2Njb2JlT0wyRHJQdktSQlNZd0E?oc=5)，2026-09-30；僅標題）
  - 官方 What's new 同樣列 5 項破壞性變更＋1 項不報錯的回應形狀改變（2026-11-05 查證），逐項見 [[#從 Sonnet 5 換過來會壞什麼]]
- **2026-09-29**：Reddit 使用者以同一組 skills 對 Sonnet 5.5 與 Opus 5.5 各跑 3 次，稱看不出輸出差異（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wtend0/tested_sonnet_55_vs_opus_55_with_the_same_skills/)，2026-09-29；0 留言，訊號極弱，未附具體分數）
  - HN 互動累計回升至 853 分（HN＋HN Repo Bridge 2 個來源，2026-09-29 查核），仍低於 Opus 5.5 發布當日的 1,674 分
- **2026-09-28**：Anthropic 發布 Claude Sonnet 5.5，Claude Code v2.1.284 同步新增支援（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)；[GitHub v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)，2026-09-28）
  - Terminal-Bench 4.0：70.6%（前代 Sonnet 5 為 10.3%）；當日只讀到摘要，完整 8 項官方表 2026-11-05 對原文補齊，見 [[#這些數字是誰量的]]
  - 牌價維持 $2/$10 每 Mtok；快取讀取**$0.10（×0.05）**——本庫當日記為 $0.20（×0.1），2026-10-10 對官方模型頁更正；Batch 半價 $1／$5、無方案分層，見 [[entities/pricing]]
  - 官方預告 Claude Haiku 5.5 將於未來數週內加入 5.5 家族，尚未發布。**後續（2026-10-07）**：Haiku 5.5 已發布，見 [[entities/haiku-5-5]]
  - 路透報導將此次上線與 Anthropic IPO 籌備進度並列，見 [[topics/anthropic-ipo]]；TechCrunch、VentureBeat、The Decoder、SiliconANGLE 及 Hacker News、Reddit 同日跟進，合計至少 7 個來源（Reuters，2026-09-28）
  - HN 互動 46 分（2 個來源），訊號偏弱
  - Simon Willison 以其慣例「畫一隻騎腳踏車的鵜鶘」測試，稱 Sonnet 5.5 出現與 [[entities/opus-5-5|Opus 5.5]] 相同的 bug：「max」thinking effort 下鵜鶘圖示渲染異常（[Simon Willison](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/)，2026-09-28；僅摘要可讀，bug 具體表現細節未載）

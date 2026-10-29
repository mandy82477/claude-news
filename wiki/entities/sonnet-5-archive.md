---
page: "entities/sonnet-5-archive"
kind: "entity"
type: "model"
status: "resolved（封存頁）"
domain: "🤖 模型"
last_updated: "2026-10-25"
last_news_update: "2026-07-31"
status_main: "resolved"
days_since_news: 90
parent: "entities/sonnet-5"
children: "[]"
page_role: "archive"
days_since_news_subtree: 90
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-11-26"
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Sonnet 5 — 原始條目封存

**類型：** model
**狀態：** resolved（封存頁）
**領域：** 🤖 模型
**上層：** [[entities/sonnet-5]]
**首次出現：** 2026-07-01
**最後更新：** 2026-10-25
**最後新聞更新：** 2026-07-31

> 本頁為原始條目封存，重點層見 [[entities/sonnet-5]]。

---

## 2026-07

#### 2026-07-31
**Degraded performance 事件（同日解決，約 46 分鐘）**：Anthropic Status 通報 Claude Sonnet 5 效能降級，2026-07-31 06:18 UTC 起偵測，07:04 UTC 確認事件已解決，無需採取行動（[Anthropic Status](https://status.claude.com/)）。Reddit r/ClaudeAI 同步出現對應 Megathread「Megathread for New Claude Incident: Degraded performance on Claude Sonnet 5 on Jul 31, 2026」，互動 0 留言（可能因剛發布尚未累積），內容與官方 Status 一致，屬社群對同一事件的跟進討論，非獨立事件。屬穩定性事件，非能力或定價變化，與本頁 07-07、07-08 已記錄的同類型錯誤率事件屬同一模式。

#### 2026-07-25
**dev.to 重申促銷折扣「real but temporary」+ Opus 5 同日發布**：dev.to 作者 tokenmixai 於〈I Did the Math on Claude Sonnet 5. The 60% Opus Discount Is Real, But Temporary.〉一文中指出，Anthropic 已將 Sonnet 5 以促銷定價廣泛開放至 2026-08-31，與既有 $2/$10 per Mtok 資訊一致，未提供新的定價數字（定價細節見 [[entities/pricing]]）。同日 Anthropic 正式發布 [[entities/opus-5|Claude Opus 5]]，取代 Opus 4.8 成為次旗艦；Sonnet 5 本身的 Claude Code 預設模型定位不受影響。

#### 2026-07-14
**MarkTechPost 三模型深度比較（Sonnet 5 vs Sonnet 4.6 vs Opus 4.8）**：MarkTechPost 發布文章〈Anthropic Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8: Agentic Coding Benchmarks, API Pricing, and Cost-Performance Tradeoffs Compared〉，涵蓋三模型的 agentic coding 基準測試、API 定價與成本效益取捨分析；本則日報摘要僅提供標題級資訊，未附具體評測數字，暫列為外部延伸閱讀資源，待後續補充量化內容時再擴寫（Google News／MarkTechPost，2026-07-14）。完整選型對照見 [[topics/model-comparison]]。

#### 2026-07-09
**媒體「正式發布」報導 + 評測分數/定價初步數字**（2026-08-26 查證，部分結案）：Mashable 於 07-09 03:41 UTC 報導 Anthropic「finally, officially launches Claude Sonnet 5」，與既有 07-01 官方發布日重疊；tech-insider.org 同日另發文宣稱評測分數達 57 分、API 成本較前代減半（"Claude Sonnet 5 Debuts: 57 Score, Half the API Cost"，13:10 UTC）。查證結果：

- **「正式發布」非新事件**：官方發布公告為 2026-06-30 美西／本庫採計之 07-01（[Anthropic Blog](https://www.anthropic.com/news/claude-sonnet-5)、TechCrunch 同日），Mashable 07-09 一文屬遲到報導，**不構成第二次發布**
- **「API 成本減半」屬實**：$2/$10 per Mtok 對前代 Sonnet 4.6 的 $3/$15 為降價，對 Opus 4.8 的 $5/$25 更省約 60%；該價已於 2026-08-10 永久化（見 [[entities/pricing]]）
- 🔎 **查無官方**（標 2026-08-26｜查 tech-insider.org、57 Score｜複 2026-11-26）｜**「57 分」的 benchmark 名稱**：官方模型頁與發布公告均未見此數字，原文亦未指明測的是哪個 benchmark，**不採信為評測事實**；tech-insider.org 為模板化標題農場型來源（同站另有多篇 "X vs Y: $N Gap" 系列，見 [[entities/fable-5]]），本庫不以其數字入表

此外 Reddit r/ClaudeCode 出現「回應內容重複」的弱訊號回報（score 恆 0，見「爭議」區）。

#### 2026-07-08
**錯誤率再度升高（同日解決）**：Anthropic Status 通報 Sonnet 5 錯誤率一度升高，於 06:40 UTC 解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/n3v83qmtlbqm)）；另有 07-07 23:46 UTC 一起「部分模型請求錯誤率升高」事件同日解決。屬穩定性事件，非能力或定價變化。

#### 2026-07-02
**發布次日爭議：圖表可信度質疑 + 個性流失回饋**：
- **官方圖表換版爭議**：HN 文章指 Anthropic 換掉讓 Sonnet 5 表現不佳的官方對比圖（[vincentschmalbach.com](https://www.vincentschmalbach.com/anthropic-changed-sonnet-5-chart-after-it-made-sonnet-look-bad/)，HN score 3）；2026-08-26 查證確認換版屬實，官方 06-30 changelog 說明為 BrowseComp 方法論更正，細節見上方 [[entities/sonnet-5#爭議]]
- **個性流失回饋**：Reddit 多位使用者反映 Sonnet 5 相較 Sonnet 4.6 智力提升但互動個性/語氣弱化，感覺更通用化（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1ulf5xc/something_important_was_lost_between_sonnet_46/)），屬主觀體驗，非量化評測

#### 2026-07-01
**正式發布**：Claude Sonnet 5 正式上線，定位最 agentic Sonnet。效能接近 Opus 4.8，促銷定價 $2/$10 per Mtok 至 2026-08-31（該到期日後於 08-10 取消）。Claude Code v2.1.197 設為預設模型。Terminal-Bench 2.1（2026-06）有明確排名（85.2%，2026-09-13 查得，見上方「核心能力」）；社群稱「cost reset for AI agents」。

#### 2026-07-07
**錯誤率一度升高（同日解決）**：Anthropic Status 通報 Claude Sonnet 5 錯誤率升高（Elevated errors），事件於 07:37 UTC 解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/hh9hj15mxkrx)）。屬穩定性事件，非能力或定價變化。

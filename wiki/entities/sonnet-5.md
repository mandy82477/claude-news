---
page: "entities/sonnet-5"
kind: "entity"
type: "model"
status: "active（Legacy，仍可呼叫）"
domain: "🤖 模型"
last_updated: "2026-10-25"
last_news_update: "2026-09-28"
status_main: "active"
days_since_news: 33
parent: null
children: "['entities/sonnet-5-archive']"
page_role: "hub"
days_since_news_subtree: 33
inbound_links: 21
attribution_count: 3
attribution_last: "2026-07-31"
top_source: "google-news"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-11-10"
pending_signalled: 0
staleness_exempt: null
signal: "⚠️ 高引用但停滯"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Sonnet 5

**類型：** model
**狀態：** active（Legacy，仍可呼叫）
**領域：** 🤖 模型
**首次出現：** 2026-07-01
**最後更新：** 2026-10-25
**最後新聞更新：** 2026-09-28

> **最新動態**（2026-09-28）
> [[entities/sonnet-5-5|Sonnet 5.5]] 發布，成為 Anthropic API 預設 Sonnet；本頁官方已列 Legacy（2026-10-10 查證，見下方「現況」）。

---

## 現況

**2026-09-28 最新**：Anthropic 發布 [[entities/sonnet-5-5|Claude Sonnet 5.5]]，Claude Code v2.1.284 將其設為 **Anthropic API 預設 Sonnet 模型**；Terminal-Bench 4.0 由本代的 10.3% 升至 70.6%，牌價維持 $2/$10 不變（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)；[GitHub v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)，2026-09-28）。完整換代對照見 [[entities/sonnet-5-5]]。自 2026-09-28 起無新動態（2026-10-31 核）；本代已被 Sonnet 5.5 取代，停滯是事實而非漏更新。

- **本頁已是官方 Legacy（2026-10-10 查證）**：官方 [Sonnet 5 模型頁](https://platform.claude.com/docs/en/models/sonnet-5/overview) 頁首標 **Legacy**、狀態欄寫 `Active (legacy)`，[models overview](https://platform.claude.com/docs/en/about-claude/models/overview) 也把它列在「Legacy models (still available)」；
  - 發布日 2026-06-30、退役不早於 **2027-06-30**（[model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)）。
  - 可靠知識截止與訓練資料截止皆為 **Jan 2026**，預設 effort `high`，牌價 $2／$10、快取讀取 $0.20。
- 🔎 **查無官方**（標 2026-09-28｜查 Sonnet 5.5、Claude Code CLI 預設｜複 2026-11-10）｜**Sonnet 5.5 是否同步為 Claude Code CLI 本身的預設模型**：官方只說「Anthropic API 預設 Sonnet」。
  - 2026-10-10 查官方 models overview、model deprecations 與 [Claude Code settings reference](https://code.claude.com/docs/en/settings-reference) 三處皆未載 CLI 預設模型，同一題見 [[entities/sonnet-5-5]] ⟨Q-01⟩

**2026-09-27**：GitHub Issue #65961 回報 Claude 生成程式碼時預設加上大量註解，即使於 prompt 中明確指示停止仍持續產生，累積 248 個反應、39 則留言，尚無官方回應；與社群既有「Claudism」冗語傾向同屬一類，見 [[topics/community-tech-patterns]]「CCN」清理工具章節，完整記錄見下方「爭議」與「歷史記錄」。

Claude Sonnet 5 於 2026-07-01 正式發布，定位為 Anthropic **最 agentic 的 Sonnet 模型**，在 reasoning、tool use、coding、knowledge work 等多個面向均有顯著提升，效能接近 Opus 4.8。

**與 [[entities/fable-5]] 的定位差異**：Fable 5（2026-09-01 起為 5.1）是最高階旗艦（Mythos 級推理能力，適合最複雜的多步驟任務）；Sonnet 5 則是主力平衡選項——以約 60% 的成本換取接近 Opus 4.8 的效能，適合日常 agentic 工作流與成本敏感場景，非追求極致推理深度的定位。

**Claude Code 預設模型**：Claude Code v2.1.197 起已將 Sonnet 5 設為預設模型，取代前一代 Sonnet 版本。

**定價**：$2/$10 per Mtok（input/output）。發布時為入門促銷價、載明 2026-08-31 到期，**已於 2026-08-10 官方永久化為標準價**，原訂 9/1 調至 $3/$15 的計畫取消（官方模型總覽頁 2026-08-26 查證：定價欄已無任何到期字樣）。社群稱此定價較 Opus 4.8 省約 60% 成本，形成「cost reset for AI agents」的討論；Opus 4.8 本身 API 定價未見官方逐項公布數字，完整定價彙整見 [[entities/pricing]]。

**1M context window**：原生支援 100 萬 token 上下文，與 Fable 5 / Opus 4.8 相同。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ✅ 廣泛推薦 |
| 最適合 | agentic 工作流、Claude Code 日常使用、tool use 密集任務、成本敏感場景 |
| 不適合 | 需要 Mythos 級推理深度的極複雜長期任務（此時考慮 Opus 4.8） |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

**快速上手（Claude Code）：**
```
# Claude Code v2.1.197 已預設使用 Sonnet 5，無需指定
claude

# 明確指定：
claude --model claude-sonnet-5-20260701
```

**注意事項：**
- $2/$10 per Mtok 為標準價，無到期日（2026-08-10 永久化；原載 2026-08-31 到期）
- 效能接近 Opus 4.8，但 60% 成本差距使其在 agentic 工作流中具備明顯性價比優勢
- 1M context 原生支援，適合整個 codebase 的大型 agentic 任務

## 核心能力

- **Agentic 定位**：reasoning、tool use、coding、knowledge work 全面提升，是 Anthropic 目前最強 agentic Sonnet
- **效能 vs Opus 4.8**：社群多篇評測確認在 agentic 任務上效能接近 Opus 4.8，60% 成本差距
- **1M token context**：原生支援，無需外部管理
- **Claude Code 預設**：v2.1.197 起為 Claude Code 預設模型

**Terminal-Bench 2.1 成績已查得（2026-09-13）**：第三方彙整站給出 Sonnet 5 在 TB 2.1 為 **85.2%**；若固定在 Terminus-2 harness 上比較，Sonnet 5 **80.4%**、Opus 4.8 **74.6%**、Sonnet 4.6 **67.0%**——**這是本站記錄中第一個中階模型在同 harness 上勝過旗艦的評測項**，較 Sonnet 4.6 的 13.4 分進步幅度在該表中排第二大（[Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-v2-1)、[Vellum](https://www.vellum.ai/blog/claude-sonnet-5-benchmarks-explained)，皆為第三方彙整、非 Anthropic 官方公布）。跨版次不可比：TB 2.1 與 3.0／4.0 分數不能互換，榜單現況見 [[topics/model-task-leaderboard]]。

## 爭議

- ⚠️ **預設冗語註解、忽略停止指示**：GitHub Issue #65961 回報 Claude 生成程式碼預設加大量註解，即使明示停止仍持續產生；累積 248 反應、39 留言，尚無官方回應（[GitHub Issue #65961](https://github.com/anthropics/claude-code/issues/65961)，2026-09-27）。同屬既有「Claudism」冗語傾向，見 [[topics/community-tech-patterns]]
- **官方 BrowseComp 對比圖表換版（爭議已落地，2026-08-26 查證）**：Anthropic 於 **2026-06-30 以 changelog 更正**替換了 Sonnet 5 的 BrowseComp 成本效能圖——原圖未套用其標準 agentic-search 方法論，新圖改用 Sonnet 5 system card 設定（10M token 預算、compaction、programmatic tool calling），成本軸上限也從約 $10 拉到 $50。官方定調為**方法論更正**，非挑選有利數據；批評方（[vincentschmalbach.com](https://www.vincentschmalbach.com/anthropic-changed-sonnet-5-chart-after-it-made-sonnet-look-bad/)，HN score 3）認為敘事從「Sonnet 落後 Opus」變成「花得夠多就有用」。**該文未提供修改前後圖表的存檔對照**，換版事實與官方理由則有 changelog 可稽；讀者可自行判斷方法論更正是否合理，本頁不代為裁定
- ⚠️ **個性/語氣不如 Sonnet 4.6（主觀回饋）**：Reddit 多位使用者反映 Sonnet 5 智力提升但互動個性流失——Sonnet 4.6 原本較有個性、懂得對話節奏、簡短回應精準，Sonnet 5 感覺更像通用「help」助手而非有特色的對話夥伴（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ulf5xc/something_important_was_lost_between_sonnet_46/)）；屬主觀體驗回饋，非量化評測，與 Fable 5「失去靈魂」討論（見 [[entities/fable-5]] 爭議區）呈現類似的世代模型「個性 vs 能力」取捨模式（推論）
- ⚠️ **回應內容重複（弱訊號，2026-07-09）**：Reddit r/ClaudeCode 使用者詢問是否也遇到 Sonnet 5 回應內容重複的情形；貼文無 score（Reddit RSS 恆 0，非跨平台佐證），暫僅列為待觀察訊號，不構成已驗證問題。同方向的世代級品質觀感（含 Sonnet 5 在內的第 5 代）整理在 [[topics/code-quality-decline]]

## 相關議題

- [[entities/sonnet-5-5]] — 2026-09-28 發布的新一代，取代本頁成為 Anthropic API 預設 Sonnet
- [[entities/fable-5]] — 現任最高階公開模型；Sonnet 5 為次階平衡選項，定位差異見上方「現況」
- [[entities/opus-4-8]] — Opus 4.8 能力對比（Sonnet 5 效能接近 Opus 4.8，Opus 4.8 已於 2026-07-25 被 [[entities/opus-5|Opus 5]] 取代次旗艦地位）
- [[entities/opus-5-5]] — 現行 Opus（2026-09-22 起取代 [[entities/opus-5|Opus 5]]），與 Sonnet 5 分屬不同定位（旗艦級 vs 主力平衡選項）
- [[entities/pricing]] — 完整定價與促銷方案細節
- [[entities/claude-code]] — Claude Code v2.1.197 更新

## 參考來源

- [Anthropic Blog：Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)（2026-07-01）
- [[news/2026-07-01]]

## 歷史記錄

### 2026-09-28
**Sonnet 5.5 發布，取代本代成為 Anthropic API 預設 Sonnet**：Anthropic 發布 [[entities/sonnet-5-5|Claude Sonnet 5.5]]，Claude Code v2.1.284 將其設為 API 預設 Sonnet 模型；Terminal-Bench 4.0 由本代 10.3% 升至 70.6%，牌價維持 $2/$10（[官方發布文](https://www.anthropic.com/claude-sonnet-5-5)；[GitHub v2.1.284](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)，2026-09-28）。是否同步為 Claude Code CLI 本身的預設、本頁是否比照 Opus 5.5 模式改列 Legacy，官方原文均未載明。

### 2026-09-27
**GitHub Issue #65961：預設冗語註解、忽略停止指示**：使用者回報 Claude 生成程式碼時預設加上大量註解，即使於 prompt 中明確指示停止仍持續產生，累積 248 個反應、39 則留言，尚無官方回應（[GitHub Issue #65961](https://github.com/anthropics/claude-code/issues/65961)，2026-09-27）。與社群既有「Claudism」冗語傾向同屬一類，見 [[topics/community-tech-patterns]]「CCN」清理工具章節；本則聚焦「指示不受控」本身，非事後清理方案。

### 2026-09-03
**錯誤率一度升高（同日解決，約 19 分鐘）**：Anthropic Status 通報 Claude Sonnet 5 錯誤率升高，官方時序為 12:37 UTC 調查中 → 12:47 UTC 監控修復結果 → 12:56 UTC 已解決，無需採取行動（[Anthropic Status](https://status.claude.com/incidents/288w7p4hk1l1)，2026-09-03）。同日另有一起**獨立**事件影響 Fable/Mythos 5.1、Fable/Mythos 5、Opus 5、Opus 4.8、Opus 4.6，13:41 UTC 已鎖定原因，同日 16:16 UTC 標記已解決（2026-09-07 查證），本頁模型不在受影響清單內，完整記錄見 [[entities/fable-5]]（[Anthropic Status](https://status.claude.com/incidents/461yvfrzpwtt)，2026-09-03）。屬穩定性事件，非能力或定價變化。

### 2026-07（總結；原始條目已移出）

- **07-01 發布**：最 agentic 的 Sonnet，效能接近 Opus 4.8；促銷價 $2/$10（08-10 永久化）；Claude Code v2.1.197 設為預設；Terminal-Bench 2.1 85.2%（09-13 查得，見「核心能力」）。
- **07-02 發布次日爭議**：官方 BrowseComp 圖表換版（HN 3 分）與個性流失回饋，結論見上方「爭議」。
- **穩定性事件三起，皆非能力或定價變化**：07-07 錯誤率升高（07:37 UTC 解決）；07-08 再度升高（06:40 UTC 解決）；07-31 效能降級（06:18–07:04 UTC，約 46 分鐘）。
- **07-09 媒體報導查證**：Mashable「正式發布」為遲到報導、非第二次發布；「API 成本減半」屬實（對 Sonnet 4.6 的 $3/$15）；tech-insider.org 的「57 分」查無官方、不採信（🔎 標記複 2026-11-26，見 [[entities/sonnet-5-archive#2026-07]]）；Reddit「回應重複」為弱訊號。
- **07-14 MarkTechPost 三模型比較**（Sonnet 5／Sonnet 4.6／Opus 4.8）：僅標題，無量化數字；選型見 [[topics/model-comparison]]。
- **07-25 dev.to 促銷「real but temporary」**：無新定價數字；同日 Opus 5 發布，不影響本代預設定位。
- 原始條目見 [[entities/sonnet-5-archive#2026-07]]


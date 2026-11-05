# 主編官方查證 — 第 28 波 entities/sonnet-5-5（2026-11-05）

查證工具：WebFetch 官方一手（anthropic.com 發布文、platform.claude.com 模型頁／What's new／migration guide、code.claude.com model-config）。行號為 `wiki/entities/sonnet-5-5.md` 2026-11-05 原檔（190 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 官方一手（2026-11-05） | 判定 |
|---|---|---|---|
| 1 | L60 ⟨Q-01⟩「是否同步為 CLI 預設 🔎 查無官方」；L68–70 懸置細節「官方文件不載 CLI 預設模型」 | code.claude.com/docs/en/model-config「Special model behavior」：「**Pro, Max, Ultra, Team, Enterprise, and Anthropic API**: defaults to Opus 5.5」；Bedrock／Google Cloud 同為 Opus 5.5、Foundry 為 Sonnet 4.5；「before v2.1.280, `default` resolved to Sonnet 5 on Pro and Team Standard」；`sonnet` 別名在 Anthropic API 解析為 **Sonnet 5.5**（Claude Platform on AWS 為 4.6、Bedrock／Google Cloud／Foundry 為 4.5）；「Sonnet 5.5 requires Claude Code v2.1.284 or later」 | **可結案**：答案是「不是」——Claude Code 各方案預設是 Opus 5.5，Sonnet 5.5 要用 `/model sonnet` 或 `--model` 選；10-10 查的三頁沒查到 model-config 頁。⟨Q-01⟩ 依 daily-contracts 改寫為事實並移除 |
| 2 | L65「我的方案能不能用：官方原文僅提及 Anthropic API；Pro／Max／Team／Enterprise 是否同步未載」 | 同上 model-config：`sonnet` 別名與 `/model` 在所有 Claude Code 方案可用；What's new「Availability」：Claude API（all customers）、Bedrock、Claude Platform on AWS、Google Cloud 兩種、Microsoft Foundry | **過期**：Claude Code 各方案可選；claude.ai 方案頁本次未逐字核（推論可用，不寫成事實） |
| 3 | L64、L74「從舊代升上去會壞什麼：migration guide 尚未見完整記載（原文截斷）；社群回報 5 處行為差異」；L75 MIXED「5 處、1 處靜默失敗，未經官方證實」 | What's new：「**Five breaking changes** can affect code already running on Claude Sonnet 5」——`disabled` 改 `between_tools`、forced tool use（`tool_choice` any/tool）回 400、thinking block 綁模型與對話（改歷史回放 400）、`computer_20251124` 在 Claude API 不收、advisor 拒 Opus 4.8／4.7／Sonnet 5／Haiku 5.5；「One more change alters the response shape **without failing any request**: text between tool calls comes back in thinking blocks」 | **錯（方向）**：MIXED 的「5 處＋1 處靜默」就是官方 What's new 的原文結構，是**官方一手**，不是「未經證實的社群回報」；「原文截斷」不成立 |
| 4 | L73「mixed-news：工作階段可能被自動降回 Sonnet 5（細節未載）」；L180 | model-config「Automatic model fallback」：「**Sonnet 5.5**: cybersecurity-flagged requests re-run on Sonnet 5. Biology-flagged requests end with a refusal」；可設「Ask each time」或 `switchModelsOnFlag: false`。API 端：server-side fallback（`fallbacks: "default"`，beta）把 `"cyber"`、`"frontier_llm"` 拒答重試到 Sonnet 5 | **可結案**：觸發條件＝資安分類器旗標；可關。官方一手，改寫為事實 |
| 5 | L79、L89「GDPval 系列某評測落後 Opus 5.5 兩分，原文截斷」（同句兩處） | 發布文基準表（Sonnet 5.5／Sonnet 5／Opus 5.5）：GDPval-AA v2.1 **1844／1449／1846**；Terminal-Bench 4.0 70.6%／10.3%／66.4%；CursorBench 4.0 55.5%／34.1%／57.8%；HLE（with tools）64.5%／54.9%／67.7%；OSWorld 2.1 80.1%／57.0%／81.8%；AA-Briefcase v1.1 1811／1359／1822；Chartography（no tools）61.6%／15.6%／64.4% | **過期且漏**：「兩分」＝GDPval-AA 1844 vs 1846，已可讀；官方表有 7 項不是 1 項；L93「所以呢：官方僅公布一項」錯；Terminal-Bench 上 Sonnet 5.5 **高於** Opus 5.5（66.4%） |
| 6 | L61 牌價 $2／$10、快取讀取 $0.10（×0.05） | 模型頁：$2／$10；5m 快取寫入 $2.50、1h $4、快取讀取 $0.10；Batch 5 折 | 一致；可補快取寫入兩檔 |
| 7 | L62 知識截止 Jun 2026；L63 退役不早於 2027-09-28 | 模型頁：Reliable knowledge cutoff Jun 2026、Training data cutoff Jun 2026；Retirement「Not sooner than September 28, 2027」 | 一致 |
| 8 | L138「1M context（沿用 Sonnet 5 規格，官方發布文未特別提及）」 | 模型頁：Context 1M、Max output 128K、Batch beta 300K；輸入文字＋圖片 | 一致；補 128K 輸出、改官方出處 |
| 9 | L44「速度快逾 30%、多數工作成本省最多 30%」 | 發布文：「runs 30%+ faster, and costs up to 30% less for most work」 | 一致 |
| 10 | L122「effort 預設 `high`」 | 模型頁：Claude API 預設 `high`；model-config：Claude Code 裡 **Opus 5.5、Sonnet 5.5、Haiku 5.5 預設 `medium`** | 一致但缺 Claude Code 端口徑：重度使用者在 CLI 拿到的是 medium |
| 11 | （頁面未載） | 模型頁「Good to know」：設 `temperature`／`top_p`／`top_k` 回 400；最小可快取 prompt 512 token（Sonnet 5 為 1,024）；tokenizer 與 Sonnet 5 相同 | 漏列：前兩項是升級會壞的實務坑 |

## 二、考題的官方錨句

- **Q1 是什麼、差在哪、該不該換**：官方「best combination of speed and intelligence」；較 Sonnet 5 快 30%+、多數工作省最多 30%；7 項基準全面高於 Sonnet 5、與 Opus 5.5 差距在 1–3 分內（Terminal-Bench 反超）；牌價同、快取讀取減半。
- **Q2 Claude Code 預設與方案**：各方案預設 Opus 5.5；`sonnet` 別名＝Sonnet 5.5（Anthropic API／訂閱）；需 v2.1.284+；Claude Code 內 effort 預設 medium；資安旗標請求會自動改跑 Sonnet 5（可關）。
- **Q3 一百萬 token**：$2 輸入／$10 輸出；快取讀取 $0.10、5m 寫入 $2.50、1h 寫入 $4；Batch 半價 $1／$5。
- **Q4 會壞什麼**：官方 5 項破壞性變更＋1 項不報錯的回應形狀改變（工具呼叫間文字進 thinking block）；另 sampling 參數 400、最小快取 512；effort 級距重校、要重掃。

## 三、給設計者三句

1. ⟨Q-01⟩ 與 mixed-news「被降回 Sonnet 5」兩筆都由官方一手結案：CLI 預設是 Opus 5.5、降回是資安旗標的自動 fallback（可關）——照 daily-contracts 改寫為事實、移除標記、回掃 L180 歷史細節。
2. 「會壞什麼」一格與 MIXED 兩條要改成官方 What's new 的 5＋1 清單（每項一句、附錨點連結），它是讀者 Q4 的答案，不是社群傳聞。
3. 「這些數字是誰量的」表改成官方 7 項三欄（Sonnet 5.5／Sonnet 5／Opus 5.5），刪掉兩處「GDPval 兩分截斷」與「所以呢：只有一項」。

來源（全一手）：[發布文](https://www.anthropic.com/claude-sonnet-5-5)、[模型頁](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)、[What's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)、[Migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)、[Claude Code model-config](https://code.claude.com/docs/en/model-config)。

## 四、補查（對健檢卡 V1–V10，2026-11-05）

- **V1**：見第一節 #3——官方 What's new 明列 5 項破壞性變更＋1 項不報錯的回應形狀改變，與 MIXED 標題「five ways, one fails silently」結構一致（MIXED 是否逐項相同：推論，只讀得到標題）。migration guide「Migrating from Claude Sonnet 5」另列 safety classifiers 擴大類別（cyber／bio／frontier_llm／reasoning_extraction／general_harms）、最小快取 512、建議重掃 effort。
- **V2／V3**：發布文基準表 7 項三欄（第一節 #5），Sonnet 5 Terminal-Bench 4.0 10.3% 出自同一張官方表；opus-5-5 頁 Opus 5 的 52.3% 本次未核（非本頁事）。
- **V4／V6／V8**：見第一節 #1、#2、#4（model-config 頁一手）。
- **V5**：發布文定價段即寫「Cache reads: $0.10」，migration guide「same prices as Claude Sonnet 5, except for prompt cache reads, which cost $0.10 … half the Claude Sonnet 5 rate」——**發布時就是 $0.10**，不是 10-07 調降。本頁「本庫原記 $0.20、10-10 更正」是本庫記錄錯誤的更正，口徑對；haiku-5-5（同維護者）與 pricing-history（商業）若寫成「調降」則錯——交設計者判同維護者那頁的互指句，pricing-history 走轉知。
- **V7**：模型頁 Context 1M、Max output 128K、Batch beta 300K、API 預設 effort `high`（第一節 #8、#10）。
- **V9**：status.claude.com 雲端解析不到（不在允許網域），未核；維持頁面原記。
- **V10**：逐字「runs 30%+ faster, and costs up to 30% less for most work」，一致。

---
page: "entities/pricing-archive"
kind: "entity"
type: "policy"
status: "resolved（封存頁）"
domain: "💼 商業"
last_updated: "2026-11-02"
last_news_update: "2026-05-19"
status_main: "resolved"
days_since_news: 167
parent: "entities/pricing"
children: "[]"
page_role: "archive"
days_since_news_subtree: 167
inbound_links: 9
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 訂閱方案與計費政策 — 原始條目封存

**類型：** policy
**狀態：** resolved（封存頁）
**領域：** 💼 商業
**上層：** [[entities/pricing]]
**首次出現：** 2026-04-25
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-05-19

> 本頁是 [[entities/pricing]] 的原始條目封存，現行規則與牌價在主頁，還在發生的事故在 [[entities/pricing-incidents]]，價格沿革在 [[entities/pricing-history]]。

## 2026-04

#### ⏸ 2026-04-29：Token 費用預估翻倍（靜默修訂，逾 90 天無後續，2026-09-06 轉 ⏸）

Business Insider 報導 Anthropic 低調調高 Claude Code 預期 Token 費用估算值一倍，無官方公告。

#### ✅ 2026-04-28：Opus「圍牆內圍牆」事件（已修正）

Pro 用戶無預告須額外購買才能使用 Opus；Anthropic 事後澄清 Pro 仍可存取，但信任損失已造成。

#### ⛔ 2026-04-25：HERMES.md 靜默計費 Bug

git commit 歷史出現大寫字串「HERMES.md」會觸發靜默切換至 API 額外計費模式，已知損失單日 $200；Anthropic 確認為 bug 但**拒絕退款**。
**立即行動**：`git log --all | grep -i HERMES`
來源：[GitHub Issue #53262](https://github.com/anthropics/claude-code/issues/53262)

## 2026-05

#### 2026-05-23：模型別名退役警示

- **⚠️ claude-opus-4-20250514 與 claude-sonnet-4-20250514 退役（2026-06-15）**：Anthropic 確認這兩個模型版本將於 6/15 正式退役，使用舊版別名（如 `claude-opus-4-0`、`claude-sonnet-4-0`）的生產環境程式碼將開始失敗。需在 2026-06-14 前遷移至新版模型 ID（如 `claude-opus-4-5-20251001`、`claude-sonnet-4-6-20260101` 等）
- **Max 方案實質差異說明**：dev.to 分析文章確認 Max 方案不僅是「更多用量」，而是在 context window 長度、Claude Code 可用額度、優先排隊等方面有結構性不同；Max 5x（$100/月）vs Max 20x（$200/月）在 agentic 工作流上的差異尤其顯著

#### ✅ 2026-05-20：Claude Code 定價溝通混亂事件（Simon Willison 分析）

- **Claude Code 曾短暫顯示為 Max 方案專屬功能**：Anthropic 定價頁在毫無公告的情況下短暫顯示 Claude Code 為 Max 方案（$100–$200/月）專屬功能，引發社群恐慌後已撤回。Simon Willison 深度分析指出問題根源是 Anthropic 的定價溝通策略缺乏透明度。此事件發生於 2026-04-22 前後，但 HN 於 2026-05-19/20 再度廣泛討論，反映社群對 Anthropic 定價透明度的持續不滿
- **建議**：用戶應持續追蹤官方 [Choosing a Plan](https://www.anthropic.com/pricing) 頁面，而非依賴第三方資訊；Anthropic 任何定價頁更動均可能未經公告

#### 2026-05-19：臨時用量提升優惠、企業成本壓力持續

- **Anthropic 臨時用量提升**：部分使用者收到 Anthropic 提供的臨時優惠——5 小時使用量加倍（x2）+ 每週上限提高 50%；社群反應熱烈，積極利用有限期額度進行密集開發；此舉可能是為緩解近期用量限制帶來的用戶不滿，或配合 Max 方案促銷；具體受惠條件 Anthropic 未公開說明
- **企業帳單達雲端費用三倍**：HN 討論串揭示多家企業月 AI 工具費用已達雲端 SaaS 費用三倍，部分企業即將全面停用 Claude Code 並禁止個人方案；顯示用量暴增 + 計費透明度不足的問題仍在持續（見 [[topics/enterprise-cost-management]]）

#### 2026-05-16：Max 用量上限未實際生效、社群促銷驗證、成本焦慮高峰

- **Max 20x 用量上限未生效（數學實證）**：一位 Max 20x 重度用戶以計算明確證明——5/6 宣佈的 2 倍 session 上限與 5/13 宣佈的 1.5 倍週用量上限均未在其帳號生效；客服零回應；多位用戶跟進驗證，顯示「宣告即生效」與實際體驗可能存在系統性落差
- **社群系統驗證 Anthropic 促銷時序**：Reddit 用戶系統整理 2025 年 8 月以來所有官方用量促銷完整時序（對照官方來源），引發對方案透明度的廣泛質疑，討論串聚焦「宣告與實際生效」之間的落差
- **Lanes.sh 說明 6/15 影響範圍**：Lanes.sh 因架構不同而未受波及，並提供清楚分析：Zed、Conductor、T3 Code、superset.sh 等建構於 Agent SDK 之上的平台的 Max 5x 訂閱用戶實際可用量大幅縮水
- **API 費用焦慮達本週最顯著高峰**：同日出現多篇 Claude Code API 費用優化指南（7 種降費策略、不改代碼省 10–30%、bootstrapped 創業者費用管控討論、Claude Code 替代方案整理），顯示開發者對 API 費用的集體焦慮達近期峰值
- **週用量配額意外提前重置（bug 或後端調整）**：部分用戶反映在正常重置日前週配額意外歸零，原重置日期未變（等同一輪額外免費用量）；不清楚是後端調整副作用或 bug；社群擔心用量可能被「追回」
- **「用 credit 包裝的漲價」批評**：部分開發者在優化指南中明確指出 6/15 公告本質是 API token 上限收緊而非計費重組；Anthropic 對此立場無官方回應

#### 2026-05-13：Anthropic 定價主導權強勁

The Information 報導企業客戶即使面對成本上漲仍持續採用；Anthropic API 定價策略短期維持強勢。

#### ⏸ 2026-05-11：Pro 方案 0% 用量仍遭收費

用戶儀表板顯示 0% 情況下，2–3 個提示後被收取 $3.37 Extra Usage；根本問題：1M context window 觸發 API 計費通道，獨立於訂閱用量計量。Anthropic 尚未公告改善。

#### 2026-05-10：Opus API 速率限制悄悄調降

ServeTheHome 首報；與 SpaceX 算力到位（Sonnet 速率翻倍）同時期出現，顯示差異化模型速率管理。

#### 2026-05-07–09：SpaceX 算力到位，速率上限翻倍

三項變更同步生效：Pro/Max Claude Code 五小時視窗速率翻倍、取消 Pro/Max 尖峰時段降速、API Tier 4+ 速率提升。Dario Amodei 在 Code with Claude 大會現場宣布。

#### ⏸ 2026-05-05：提示快取窗口悄悄縮短（未公告）

Anthropic 於 4 月初靜默縮短預設 prompt cache 窗口，實質提高 token 消耗速度；為繼 Token 費用估算翻倍（2026-04-29）後第二次被社群自行發現的靜默計費改動。

## 2026-06

#### 2026-06-30：配額再次縮減（社群反映，Anthropic 無官方公告）

- **社群集體反映配額縮減**：Reddit r/ClaudeCode 多個討論串，訂閱用戶集體反映 Claude Code 配額再次縮減，不滿高漲；Anthropic 無官方公告，縮減幅度與觸發機制不明。結構上，這是 6/16 計費暫停後改以調降配額（而非計費改制）控管成本的另一路徑（推論）。**對採用率的意涵**：重度用戶持續感受配額壓縮可能加速評估競品，「配額縮減 → 不滿 → 切換」的漏斗對訂閱留存構成風險（推論）（Reddit https://old.reddit.com/r/ClaudeCode/comments/1uim4jb/this_is_a_message_for_anthropic_bring_back_the/）
- **注意**：無具名企業規模數據，此條目為訂閱用戶個人反映，非企業層級案例。

#### 2026-06-26：Max 5x × 2 vs Max 20x × 1 方案分析

- **社群發現：兩個 Max 5x 帳號可並行兩個 session，性價比策略受關注**：Reddit 用戶（r/ClaudeAI）分析指出，雙 Max 5x 帳號架構可**同時**運行兩個獨立的 Claude Code session，對需要並行工作流的獨立開發者而言可能更具彈性，單一 Max 20x 帳號無法同時跑兩個 session（Reddit https://www.reddit.com/r/ClaudeAI/comments/1ug6kjv/two_max_5x_accounts_cost_the_same_as_one_20x_and/）
- **⚠️ 價格更正**：原始 Reddit 貼文與本頁前版將 Max 5x 誤植為 $50/月（兩個合計 $100 = 一個 Max 20x）；查證 2026-05-14 官方政策公告原文（xda-developers、dev.to）確認 **Max 5x 實際為 $100/月、Max 20x 為 $200/月**，兩個 Max 5x（$200）與一個 Max 20x（$200）費用相同，而非原貼文所述的 Max 5x×2 = Max 20x×1 的低價組合；性價比論點仍成立（可並行兩個 session），但費用比較基準已修正
- **適用場景**：主要利好獨立開發者與小型團隊；企業用戶因合規與帳號管理需求，不一定適合多帳號架構（多帳號合規邊界見「計費切割風波」2026-05-17 條目）
- **注意**：此為社群分析，Anthropic 官方未就多帳號策略表態；使用前仍需確認 ToS 合規邊界

#### ⏸ 2026-06-24：隱私政策更新 + 帳號盜刷事件

- **隱私政策更新，新增年齡或身份驗證條款**：Anthropic 更新隱私政策，新增年齡或身份驗證相關條款，2026-07-08 正式生效；影響範圍與具體執行細節未完整公開，用戶應於生效前查閱更新版條款
- **加州用戶帳號遭盜刷，歐元計費未授權費用**：ABC7 報導，加州用戶反映 Claude 帳號遭他人盜用，產生以歐元計費的未授權費用；顯示 Anthropic 計費帳號安全存在漏洞，建議用戶定期檢查帳號活動記錄（ABC7 2026-06-24）
- （未列入總表：距最後動態已逾 90 天〔2026-09-26 查證，已達 94 天〕，本輪已掃日報至 2026-09-25 無新回報，轉 ⏸）

#### 2026-06-09：Claude Fable 5 定價發布

- **Fable 5 定價**：$10 input / $50 output per million token（double Opus 4.8）；context window 1M；最大 output 128K
- **6/22 前含括於訂閱**：Pro / Max 訂閱用戶 6/22 前免費使用 Fable 5，之後改為消費制（enterprise consumption-based plan 或 API 直接計費）
- **Mythos 5**（無護欄完整版）：僅限授權用戶，定價比 Fable 5 更高，細節未公開
- **30 天資料保留政策**：Fable 5 / Mythos 5 所有流量（含 AWS Bedrock）強制保留 30 天，資料離開 AWS 安全邊界；企業應評估隱私影響
- **AWS Bedrock 強制 provider data sharing（2026-06-21 新增）**：AWS Bedrock 的 Fable 5 model card 顯示，客戶須同意啟用 `anthropic.model-invocation-logging`（即 provider data sharing），Anthropic 可存取推理日誌；金融、醫療等受嚴格資料合規監管的行業在採購決策前需評估此條件（dev.to 2026-06-21）


## 計費切割風波

Agent SDK／`claude -p` 用量脫離訂閱、改按 API 費率的計畫：2026-05-14 公告、06-16 暫停，重推時間未定。政策本身已不在進行中，原始條目照搬於此；現行規則見 [[entities/pricing#當前生效的計費規則]]「訂閱配額制維持」。

#### 2026-06-18：Agent SDK 計費持續觀望中，B2B 定價差距引發分析

- **DevOps.com 確認計費暫停持續**：DevOps.com 報導 Anthropic 尚未宣布 Agent SDK 計費調整的新時程，訂閱配額維持現狀；社群開發者持續觀望（DevOps.com 2026-06-18）
- **SaaStr 分析：個人 vs 企業 API 定價差距懸殊**：個人用戶以 $20-$200/月訂閱 Claude 即可完成大量工作，而企業 API 呼叫一次要 $1，最多差距可達數十倍；SaaStr 文章指出這使老牌 B2B 軟體廠商面臨根本性競爭劣勢（SaaStr 2026-06-18）
- **HN 社群 AI 花費調查**：HN 討論串顯示 AI 編碼費用分佈極廣——從每月數十美元到超過 $100,000 的全自動化重度用戶均有；反映出 AI 工具從個人玩具到企業基礎設施的多層需求（HN 2026-06-18）

#### 2026-06-17：Ars Technica 深度報導計費暫停始末

- **Ars Technica 詳細報導**：完整梳理 5/13 計費切割公告至 6/16 緊急喊停的事件全貌——背景是重度 Agent SDK 使用者與第三方 app 開發者（Zed、Conductor、T3 Code 等）的強烈反彈；官方 `claude -p` 使用者亦受影響；Ars Technica 指出此決策對依賴 Agent SDK 的第三方 app 開發者商業模式衝擊最大（Ars Technica 2026-06-16）
- **政策現狀**：Agent SDK、`claude -p`、第三方 app 繼續使用訂閱配額，無需額外信用池；週配額過渡性提高 50%（至 7 月 13 日）仍持續

#### 2026-06-16：Agent SDK 計費政策暫停 + Claude Max 集體訴訟

- **Agent SDK 計費切割暫停**：Anthropic 寄信給用戶宣布暫停原定 6/16 生效的計費切割政策，訂閱配額維持現狀，無需領取信用點數。「正在調整方案以更好支持用戶使用方式」，重新推行時間未定（HN score 30，多個討論串）
- **Claude Max 集體訴訟**：原告 Karl Kahn 在北加州聯邦地院提起集體訴訟，指控 Claude Max 5x 與 Max 20x 方案實際使用限制遠低於廣告宣稱。$200/月 Max 20x 實際僅提供 Pro 的 6–8 倍用量，而非廣告的 20 倍；Max 5x 亦類似（CNET、Decrypt 報導）
- **AI 價格戰壓力**：WSJ 分析 AI 定價戰加劇，部分重度用戶比較後發現 DeepSeek $20/月（按用量）等效用途的成本遠低於 Claude Max，引發訂閱價值討論

#### 2026-05-21：6/15 計費影響持續發酵，社群替代方案成熟

- **clarp（drop-in claude -p 替代品）**：開發者開源 clarp，在本地啟動隱藏 PTY 的 Claude Code 互動 CLI，並透過唯讀代理攔截 Anthropic API 串流，重建 `claude -p` 行為；多數專案只需改一個 binary 名稱即可遷移至互動計費軌道，是 6/15 後最直接的工作流保全方案
- **vibe-skill（57M tokens 節省，成本降逾九成）**：開發者開源 vibe-skill，讓 Claude 負責規劃與 diff 審查，實際撰碼任務委派給 Mistral Vibe（低成本執行層）；10 天實測節省 57M tokens，成本降逾九成，Claude 品質的規劃輸出基本保留；是 6/15 計費壓力下最具代表性的混合策略落地案例
- **atrium 工作區設計含 6/15 預案**：macOS 工作區管理工具 atrium 在設計動機中明確提及「規避 6/15 API 計量鎖定」，顯示 6/15 政策已開始影響工具設計決策
- **dev.to 分析文章**：「Anthropic Is Splitting Claude Code's Billing — What It Means for Dev Teams Using Agents」整理 6/15 後對依賴 print mode 自動化工作流程的開發團隊衝擊，clarp 和 vibe-skill 均在文章中被引用為社群因應方案

#### 2026-05-17：`claude -p` 計費衝擊持續、多帳號架構合規紅線

- **`claude -p` 計費調整後的工作流適應**：dev.to 出現以 AI agent 第一人稱視角記錄 6/15 計費規則調整後如何重新設計自動化工作流的文章，代表計費政策變更對長期用戶的實際衝擊仍在延續，開發者正積極找因應方案
- **多帳號 Claude Code 架構合規邊界明確**：文章詳細比較兩種多帳號 Claude Code 使用架構，明確指出其中一種已被 Anthropic 視為違反使用條款（ToS），提醒規模化使用需求的開發者在帳號管理策略上需注意合規邊界；目前僅知「其中一種被禁」，未公開具體判斷標準

#### 2026-05-15：6/15 計費變更社群反應、第三方工具衝擊、官方回應

- **社群情緒**：約六成負面（Max 5x $100 信用池對重度 agent 用量嚴重不足）、兩成理解、兩成觀望
- **受衝擊工具**：Zed、Conductor、T3 Code、Superset；Lanes 聲明不受影響；Zed 已發布應對說明
- **官方回應**：Ars Technica 專訪 Claude Code 產品主管，說明「lean harness」設計哲學，社群認為說明仍不足
- **灰色地帶**：VS Code 擴充套件用量是否計入新信用池，Anthropic 尚未明確答覆
- **Ungate 工具出現**：宣稱可將 Max 訂閱用量路由至 Cursor（$100 = $2,000 API 等值）；**使用前確認 ToS**

#### 2026-05-14：正式宣布 Programmatic 計費分離

Anthropic 宣布 6/15 起 `claude -p`、Agent SDK、Claude Code GitHub Actions 及第三方 Agent SDK app 完全脫離訂閱，改為獨立信用池，按完整 API 費率計費。主要後續效應：
- 部分用戶宣告取消訂閱，轉向 Codex 或 Gemini（見 [[topics/competitor-landscape]]）
- 社群開發者發布 `claude-pee` 繞過工具（PTY 終端模擬），Anthropic 尚未回應
- OpenClaw 等第三方工具恢復，但改走信用池計費（見 [[entities/openclaw]]）

#### 2026-04-25：第三方 Agentic 工具配額限制

The Verge 報導 Anthropic 限制 OpenClaw 等工具；Claude Code 負責人 Boris Cherny：「訂閱方案的設計並非為這類第三方使用模式而生。」（預示 6/15 政策的早期信號）

#### 原定計費架構設計（2026-05-14 公告，2026-06-16 暫停，保留供歷史參考）

⚠️ 此計費架構已於 2026-06-15 暫停、尚未生效，以下為原定設計，當前計費仍依現行方案。

> **2026-06-16 更新**：Anthropic 宣布暫停原定 6/16 生效的 Agent SDK 計費切割政策。目前 Agent SDK、`claude -p`、第三方 Agent SDK 應用的用量仍維持原訂閱配額制，無需額外信用池。重新推行時間未定，將提前通知。

Anthropic 將使用場景切分為**兩條獨立計費軌道**：

**軌道 1：互動式使用（Interactive）— 訂閱涵蓋**

| 涵蓋範圍 | 說明 |
|---------|------|
| Claude.ai 網頁介面 | 人工驅動對話 |
| Claude Code 互動 session | 使用者在終端手動操作 |
| 一般 API 互動呼叫 | 人工觸發的請求 |

→ 費用包含在訂閱月費內，受「5 小時視窗速率上限」管控

**軌道 2：程式化使用（Programmatic）— 信用池計費**

| 涵蓋範圍 | 計費方式 |
|---------|---------|
| `claude -p`（headless / 非互動模式） | 按完整 API 費率，從信用池扣除 |
| Agent SDK 呼叫 | 同上 |
| Claude Code GitHub Actions | 同上 |
| 第三方 Agent SDK app（如 Zed、Conductor、T3 Code） | 同上 |

→ **不享任何訂閱折扣**，信用池用盡後需額外購買

**方案對照表（2026-06-15 後）**

| 方案 | 月費 | 互動用量 | Programmatic 信用池/月 |
|------|------|---------|----------------------|
| Free | $0 | 基本限制 | 無 |
| Pro | $20 | 標準 | $20（按 API 費率） |
| Max 5x | $100 | 5× Pro | $100（按 API 費率） |
| Max 20x | $200 | 20× Pro | $200（按 API 費率） |
| API only | 按量 | — | 直接按 API 費率 |

> **財務衝擊試算**：Max 5x 用戶若程式化使用達週配額 40%，換算 API 費率約需 **$1,000/月**（是月費的 10 倍）

> **過渡緩衝**：6/15 前 Anthropic 臨時將所有付費方案週用量上限**提高 50%**（至 7 月 13 日）

**6/15 計費切割回顧（已暫停）**：原定 2026-06-15 生效的計費切割政策於 **2026-06-16 宣布暫停**，以下為當時社群的主要因應建議，保留供未來政策重啟時參考：

- 盤點所有 `claude -p`、Agent SDK、CI 自動化的月均用量
- 對照各方案信用池上限，評估是否足夠或需升級/備案
- 若使用 Zed、Conductor、T3 Code 等第三方工具，確認其計費切換說明
- 設定費用警報（Anthropic 儀表板有顯示延遲，建議自建監控腳本）

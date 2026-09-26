---
page: "entities/boris-cherny-archive"
kind: "entity"
type: "person"
status: "resolved（封存頁）"
domain: "👤 人物"
last_updated: "2026-09-20"
last_news_update: "2026-05-27"
status_main: "resolved"
days_since_news: 122
parent: "entities/boris-cherny"
children: "[]"
page_role: "archive"
days_since_news_subtree: 122
inbound_links: 0
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
# Boris Cherny — 原始條目封存

**類型：** person
**狀態：** resolved（封存頁）
**領域：** 👤 人物
**上層：** [[entities/boris-cherny]]
**開始日期：** 2026-04-23
**最後更新：** 2026-09-20
**最後新聞更新：** 2026-05-27

> 本頁保存 [[entities/boris-cherny]] 被搬離主頁的原始條目，一字不刪。想知道現況，回主頁「現況」或「公開言論摘要表」。

---

## 2026-04

### 第三方工具邊界聲明（2026-04-25）
在 The Verge 報導中公開表示：「訂閱方案的設計並非為這類第三方使用模式而生」，被視為 Anthropic 將持續收緊第三方 agentic 工具門檻的明確信號。詳見 [[entities/pricing]] 與 [[entities/openclaw]]。

### 4/23 事後報告（2026-04-23）
Claude Code 效能退步事件確認後，Boris Cherny 發布事後報告，承諾超過 50 項修復。社群開發者自 2026-05-03 起逐一獨立驗證這些承諾，為少見的社群對官方承諾進行系統性問責案例；逐項驗證未見完成結果，本站已於 2026-09-07 停止追蹤這一條。詳見 [[topics/code-quality-decline]]。

#### 歷史記錄原文（2026-04）
- 2026-04-25：在 The Verge 報導中聲明訂閱方案並非為第三方 agentic 工具使用模式而設計
- 2026-04-23：Claude Code 效能退步事件確認後發布事後報告，承諾超過 50 項修復

## 2026-05

### 「軟體工程師的終結」——Platformer 專訪（2026-05-27）
Platformer 刊出 Boris Cherny 長篇專訪，標題「Claude Code's creator on the end of the software engineer」，從他的視角論述 AI 如何根本性地改變軟體工程師的角色。這是他繼「coding is solved」（2026-05-08）與「軟體工程已死」（2026-05-06）後最完整的公開論述。社群熱議程度與他過去的宣言相當，引發開發者身份認同的再次討論。

### 每晚數千個 AI 子代理工作流（2026-05-13）
公開了每晚讓數千個 AI 子代理執行「深度工作」的工作流架構，被 Business Insider 與 Let's Data Science 同步報導，成為本週最受矚目的 agentic AI 使用案例。案例展示：白天由人類設定任務框架，夜間由數千個並行子代理自主深入研究執行「深度工作」，早上整合結果；是其「Loops 是未來」（2026-05-05）哲學的最極端公開實踐。此報導進一步推動社群對大規模並行代理架構的廣泛討論，結合 v2.1.140 的 subagent_type 匹配改善，顯示官方工具正在降低大規模子代理配置的摩擦。見 [[entities/managed-agents]]。

### 「coding is solved」（2026-05-08）
在「Code with Claude」大會宣稱「寫程式問題已被解決」，並公開表示厭倦「vibe coding」一詞，尋找替代描述；自稱 2026 年從未手寫一行程式。言論在 Business Insider、HN、YouTube 等多平台引發廣泛討論，社群反應兩極：有人認同 AI 輔助開發效率躍升，也有人直接回應「Claude Code 太不穩定、已放棄使用」。

### 「軟體工程已死」（2026-05-06）
再次公開宣示 Anthropic 內部已無傳統軟體工程師職位，引發業界廣泛論戰，Times of India 等媒體跟進報導，開發者身份認同議題持續發酵。

### 「Loops 是未來」（2026-05-05）
在 podcast 中宣示已 100% 用 Claude Code 取代手動編碼，並提出 **Loops（迴圈執行）是 AI 編碼的未來範式**，而非單次 prompt 補全。這是 Claude Code 設計哲學的第一手公開陳述，解釋了 Claude Code 為何以 Hooks、Skills、session 持久化為核心設計——目標是讓 agent 能在無人監督下持續迴圈執行。

#### 歷史記錄原文（2026-05）
- 2026-05-27：Platformer 長篇專訪「Claude Code's creator on the end of the software engineer」發布，為其「軟體工程已死」系列論述最完整陳述
- 2026-05-13：公開每晚數千個 AI 子代理並行執行深度工作的工作流架構，由 Business Insider 等媒體報導
- 2026-05-08：在「Code with Claude」大會宣稱「寫程式問題已被解決（coding is solved）」，並公開反對「vibe coding」一詞
- 2026-05-06：公開宣示 Anthropic 內部已無傳統軟體工程師職位，引發業界廣泛論戰
- 2026-05-05：在 podcast 中宣示已 100% 用 Claude Code 取代手動編碼，提出「Loops 是 AI 編碼的未來範式」

## 2026-06

### 13 個日常 Claude Code 使用技巧（2026-06-28）

Boris Cherny 在 [howborisusesclaudecode.com](https://howborisusesclaudecode.com) 公開分享個人日常 setup，具體技巧包括：

- 同時開 5 個 Claude Code 實例，各自對應同一 repo 的 5 個獨立 git checkout
- 另開 5–10 個 claude.ai/code 瀏覽器 session 並行操作
- 使用 `&` 指令將 session 背景化
- 使用 `--teleport` 旗標在本地環境與 Web 環境之間切換
- 從 iPhone 早上啟動 session，下午在桌機接力繼續
- 依賴系統通知提醒何時需要介入輸入

他特別強調此 setup 是「surprisingly vanilla」——Claude Code 開箱即用，無需特殊魔改配置。此次分享被 Hacker News 收錄（06/27 17:10 UTC，score 5），是其個人工作流從「哲學宣言」轉向「操作實踐」的一次具體展示。

- 來源：[howborisusesclaudecode.com](https://howborisusesclaudecode.com)（Hacker News 2026-06-27）

### 「AI 寫 100% 程式碼正在變得有問題」立場轉變（2026-06-24）

Times of India 報導 Boris Cherny 承認「AI 寫 100% 程式碼正在變得有問題（is getting problematic）」，這與他此前在「Code with Claude」大會宣稱「AI 已解決程式設計問題（coding is solved）」的立場形成明顯對比。此聲明與企業端近期出現的 AI 過度依賴反彈聲浪相呼應，顯示 Claude Code 創始人自身的公開立場已出現調整。

- 來源：[Times of India，2026-06-23](https://timesofindia.indiatimes.com/technology/tech-news/claude-code-creator-boris-cherny-who-declared-ai-has-solved-coding-admits-ai-writing-100-code-is-getting-problematic-as-companies-/articleshow/131954700.cms)

### AI ROI 與實驗平衡論述（2026-06-23）

Business Insider 報導 Boris Cherny 對企業 AI 投資策略的立場：支持企業聚焦 AI ROI 是正確方向，但同時主張企業仍需保留實驗空間，不應將預算完全鎖定在 ROI 導向的評估框架。這是他繼「coding is solved」系列宣言後，首次針對企業採購與投資邏輯公開發聲，定位在協助企業領導人理解 AI 工具投資的雙軌思維。

- 來源：[Business Insider，2026-06-23](https://www.businessinsider.com/boris-cherny-anthropic-token-cost-roi-ai-2026-6)

### 「Claude Code 讓工程師更孤獨」論述歸屬釐清（2026-06-22）

2026-06-22 Business Insider「engineering leader 讓工程師更孤獨」一說，後續具名來源確認發言人為 Anthropic 工程副總裁 **Fiona Fung**，**並非 Boris Cherny**。此聲明不歸於本頁，詳見 [[entities/fiona-fung]]。

### Loop Engineering 哲學引用（2026-06-20）
techstackups.com 技術文章引用 Boris Cherny 採訪中的論述：「我不再 prompt Claude，我寫 loop 讓 loop 去 prompt Claude；我的工作是寫 loop。」此聲明被視為他繼「coding is solved」後的第二個重要設計哲學表態，進一步將 **工程師角色重新定義為「寫迴圈的人」而非「寫 prompt 的人」**。這也是 2026-05-05「Loops 是未來」哲學的延伸具體化，從範式宣言進化為操作層面的自我定位描述。注意：此引用來自採訪轉述，而非 Boris 直接發文。

#### 歷史記錄原文（2026-06）
- 2026-06-28：在 howborisusesclaudecode.com 公開 13 個日常 Claude Code 使用技巧，涵蓋 5 個並行實例搭配獨立 git checkout、`--teleport` 跨環境切換、iPhone 啟動電腦接力等；強調「surprisingly vanilla」setup（Hacker News，score 5）
- 2026-06-24：Times of India 報導其承認「AI 寫 100% 程式碼正在變得有問題」，與早前「coding is solved」立場形成對比，呼應企業端過度依賴反彈聲浪
- 2026-06-23：Business Insider 報導其對企業 AI 投資的立場：支持 ROI 導向，但反對完全不留實驗預算
- 2026-06-22：「engineering leader 讓工程師更孤獨」一說，後續具名來源確認發言人為 Anthropic 工程副總裁 Fiona Fung（[[entities/fiona-fung]]），非 Boris Cherny；原歸屬懸置已排除
- 2026-06-20：techstackups.com 採訪引用 Loop 工程哲學名言「我不再 prompt Claude，我寫 loop 讓 loop 去 prompt Claude；我的工作是寫 loop」，被視為繼「coding is solved」後的第二個重要設計哲學表態

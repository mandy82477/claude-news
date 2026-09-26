---
page: "topics/community-large-codebase-workflow"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-09-23"
last_news_update: "2026-09-23"
update_freq: "🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）"
status_main: "ongoing"
days_since_news: 3
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 3
inbound_links: 52
attribution_count: 2
attribution_last: "2026-08-05"
top_source: "reddit"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 大型 Codebase 規模化開發：社群工作流主線

**狀態：** ongoing
**領域：** 🌐 社群
**更新頻率：** 🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）
**開始日期：** 2026-05-02
**最後更新：** 2026-09-23
**最後新聞更新：** 2026-09-23

> **四面牆，官方都已給了起點**（2026-09-23）
> 每個 agent 一個 worktree、腳本呼叫加 `--bare`、跨 session 的 auto memory、用 Stop hook 擋住「說做完卻沒做」——四面牆官方都已給了零件；Claude Code 一個 session 預設最多同時跑 20 個 subagent，那是上限，不是「20 個都跑得穩」。四條線的「現在的答案」第一條因此都改成官方零件在哪，社群做法接在後面。

---

## 摘要

小專案上好用的做法——單一 CLAUDE.md、單一 session、讀完整檔案——搬進大型 codebase 就開始失靈：並行 agent 互踩、context 被工具輸出撐爆、agent 記不住昨天的架構決策、多 agent 產出沒人把關。本頁按這四面牆整理社群現在怎麼組做法、做到哪、還缺什麼，每條線的第一條先指官方已給的零件。官方每塊零件是什麼見 [[topics/anthropic-agent-stack]]，官方流程每一段怎麼設定見 [[topics/coding-workflow-guide]]，卡在某個症狀該裝哪個工具見 [[topics/community-tech-tools]]，每個做法的原始證據見 [[topics/community-tech-patterns]]。

| 主線 | 一句話問題 | 現在的答案 |
|------|-----------|-----------|
| 1. 並行規模 | 幾個 agent 同時跑會互踩？ | 每個 agent 一個 worktree（官方已內建）；隔離之後的協調分統一容器與任務脈絡互通兩路 |
| 2. Context / Token | context 怎麼不被大 repo 撐爆？ | 不預先加載、按需取回；變笨先測量再歸因 |
| 3. 索引與記憶 | agent 怎麼記得住跨 session 的決策？ | repo 才是記憶體——決策外化成 CLAUDE.md／spec／ADR，本地索引按需查 |
| 4. 除錯與分工 | 多 agent 產出誰把關？ | 審查者唯讀＋工具範圍限制；跨模型交叉審查在論文測試裡有效 |

---

## 技術彙整

### 1. 並行規模：幾個 agent 同時跑會互踩？

**現在的答案**
- **官方已給**：`claude --worktree <名字>` 開隔離 session，subagent 設 `isolation: worktree` 各拿暫時 worktree（[官方文件](https://code.claude.com/docs/en/worktrees)）；何時該隔離見 [[topics/anthropic-agent-stack]]，monorepo 只取需要的目錄見 [[topics/coding-workflow-guide]]
- 隔離是並行的起點：每個 agent 一個 worktree（或等價的檔案系統隔離），社群近三個月沒有出現反對意見
- 規模一段一段加：社群的崩潰分析建議先在 10–20 個 agent 驗證協調機制，每倍增一次重驗，不線性外推
- 隔離之後的戰線是協調，兩種型態互不取代：統一容器（換底層 agent 不必重寫協作邏輯）與任務脈絡互通（各自獨立的 agent 像用 Slack 一樣互相知會）

**🧰 現在就能下的解**：見 [[topics/community-tech-tools]]「我卡在這裡」——「多個 agent 在同一 repo 互相覆蓋」列（首選 ness，原名 Harness；已經用 worktree 隔離、只差 commit 落地不打架的分界在同列第三欄）與「一堆 agent 在跑，看不到誰卡住」列（首選 Omar）

**還沒解決**：「開得出幾個」和「跑得穩幾個」是兩回事——官方的 20 是上限（Claude Code 一個 session 預設同時 20 個 subagent、可調，[官方文件](https://code.claude.com/docs/en/sub-agents)；Managed Agents 最多 20 個子代理同時跑，見 [[entities/managed-agents]]），社群實測卻在 4→20 之間就崩，中間沒人系統驗證。fork 子代理會繼承父對話（官方證實），token 因此累積多快只有社群單一觀察（查證見頁末）。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 隔離 | OS 帳號隔離 → git worktree 成共識，並工具化、動態化；官方也已內建 | Claudette、Superset、cc-fleet 等，見 [[topics/community-tech-patterns-archive]] | 多來源 |
| 規模上限 | 4→20 崩潰主因：git lock／DB 連線競爭、context 洩漏、無協調層；另有單一長 session 前後動用 147 個 subagent、24 天完成移植（09-04） | 《Why 20 Instances Break Down》、F-Zero X 移植 | 單一深度分析 |
| 統一容器 | 08-05 起一批接一批，已有 OS、團隊、平台、IDE 化幾種取向；換底層 agent 不必重寫協作邏輯 | omnigent、loopx、proliferate 等，見 [[topics/community-tech-patterns]] | 已成趨勢 |
| 任務脈絡互通 | 不取代底層 agent，讓多個獨立 agent 共享任務脈絡；09-16 出現跨終端互相傳訊的第二例 | Concord（MCP）、hcom | 單一實測 |
| 可觀測性 | 多款獨立儀表板，分「讀官方 event stream」與「自解析 transcript」兩路 | HUD、episko（原名 Cockpit）等，見 [[topics/community-pattern-trends]] 趨勢六 | 已成趨勢 |
| 落地整合 | 本地合併佇列讓 commit 依序落地（4–5 agent／日 90 commit／8GB 筆電） | Claude Code Merge Queue | 單一實測 |

**為什麼會這樣**：規模一大，共享資源（git、DB）與 context 邊界最先破，所以隔離原語最早收斂；協調層本身正在分岔成「統一容器」與「脈絡互通」兩條互補而非互斥的路線；人工盯進度撐不住，才催生一批儀表板。

---

### 2. Context / Token：context 怎麼不被大 repo 撐爆？

**現在的答案**
- **官方已給**：腳本或 SDK 呼叫加 `--bare`，跳過 hooks、skills、MCP server、auto memory、CLAUDE.md 等自動載入（[官方文件](https://code.claude.com/docs/en/headless)）；單次讀取量官方也已設上限——見 [[topics/coding-workflow-guide]]
- 不預先 @ 一堆檔案、按需取回；長 session 退化的解法是裁剪輸入，不是加 context
- 「變笨」先量 context 組成再怪工具——官方 `/context` 列出各類別即時佔用與優化建議（[官方文件](https://code.claude.com/docs/en/context-window)），還不確定誰在撐爆就先跑 PrismoDev（🧰 行那列第三欄）；越跑越笨見 [[topics/community-tech-discussions]]，換版變差見 [[topics/code-quality-decline]]
- CLAUDE.md 每行都是對每個請求課的「context 稅」：依觸發頻率決定放 CLAUDE.md／skill／hook／docs 哪一層（官方建議同方向）

**🧰 現在就能下的解**：見 [[topics/community-tech-tools]]「我卡在這裡」——「context 一直被工具輸出撐爆」列（首選 pxpipe）與「帳單爆了，看不到錢花在哪」列（首選 tare）

**還沒解決**：「該裁多少」沒有跨案例統一標準，圖片化 context（pxpipe）與 grep 輸出裁剪（Graft）都只有單一案例，Graft 的降幅還遭質疑（查證見頁末）。fork 子代理繼承父對話，裁掉的是工具輸出、放大的卻是對話歷史本身，這種撐爆來源還沒人好好量過。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 按需取回 | 預先 @-mention 定為反模式；讀取上限＋索引層；不裁剪會 O(N²)（62.8–85.9% 額外 token）；nightshift 疊三層因應多 issue context rot | Just-in-Time Retrieval、Compact Memory、nightshift 等，見 [[topics/community-tech-patterns]] | 多來源 |
| MCP 成本 | 9 個 server ≈ 每輪 38k token 冷啟動；設計（描述長度、回傳格式）實測有差 | MCP 信任邊界審查、隱藏成本實測 | 多來源 |
| 極簡輸出 | 單次回覆 70→20 token；65% 降耗；企業已當降本策略 | Caveman Skill、404 Media 報導 | 多來源 |
| CLAUDE.md 取捨 | 四層寄放地依觸發頻率；載入順序（CLAUDE.local.md 後載、受管理原則檔各 OS 路徑不同，與官方文件一致） | 「該裝什麼」「載入順序」兩篇 | 單一深度分析 |
| 固定成本量測 | `claude -p` 未加 `--bare` 冷啟動約 15 萬 token，多 agent pipeline 反覆呼叫會放大；官方沒給數字 | headless 冷啟動實測 | 單一實測 |
| 工具輸出裁剪 | grep 搜尋輸出宣稱可削減 42% token，但只測 50 題一次、p 值 0.22，benchmark 段落遭質疑 AI 代寫 | Graft | 單一實測 |
| fork 子代理的歷史 | fork 子代理繼承父對話（官方證實）；社群回報四個平行子代理耗約 200 萬 token，官方沒給數字 | Reddit 回報 | 單一實測 |
| 非主流方向 | 清程式碼內 AI 殘留註解（CCN，2,700 次迭代自陳）；文字 context 渲染成圖片（pxpipe） | CCN、pxpipe | 推論 |

**為什麼會這樣**：大 repo 的檔案量與工具輸出量本身就超過 context，任何「多讀一點保險」的直覺都會撐爆；於是社群的每一步都是在把「哪裡吃了 token」變成可量測的數字，再針對數字最大的那塊裁——但量測本身的可信度也需要驗證，不是每個宣稱的百分比都經得起檢視。

---

### 3. 索引與記憶：agent 怎麼記得住跨 session 的決策？

**現在的答案**
- **官方已給**：auto memory 讓 Claude 跨 session 自己記筆記，每個 session 載入前 200 行或 25KB；官方明說它是 context 不是強制設定，要硬擋得用 PreToolUse hook——各層該放什麼見 [[topics/coding-workflow-guide]]
- repo 才是記憶體、模型只是工作者：已確定的架構決策外化到 CLAUDE.md、spec、ADR，不靠模型跨 session 記住
- 本地優先的索引（向量 DB／圖資料庫／SQLite／純 Markdown）按需語義查詢，不把全部記憶塞進 context

**🧰 現在就能下的解**：見 [[topics/community-tech-tools]]「我卡在這裡」——接手大 repo 讓 agent 讀懂走「接手沒碰過的大 repo，agent 讀不懂」列（首選 graphify）；跨 session 記憶走「每開新 session 都要重講一遍」列（首選 brain.md，零依賴檔案式；團隊共享與 Obsidian 路線的分界在同列第三欄）

**還沒解決**：跨工具可攜、codebase 文件自動維護、「內建記憶到底解決了什麼」都只有一兩個案例，三條近期實作路線（零依賴檔案式、手動策展取代官方、團隊共享）各走各的，沒有交叉比較。「已否決方案要不要記」仍停在問題點名，沒有工具實作。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 統一框架 | Repo-as-Memory：決策外化；跨 repo 依賴圖需另注入（`nx graph` 等） | Repo-as-Memory、Cross-repo Blast Radius | 單一深度分析 |
| 本地索引 | 向量 DB（39ms 檢索）／圖資料庫／SQLite session 索引／Markdown+git，各走一路；圖譜路線採用量最大（graphify） | Memex、session-indexer、cpr-compress-preserve-resume 等，見 [[topics/community-tech-patterns]] | 多來源 |
| 零依賴檔案式 | 決策／需求／限制三類專案層級資訊，CLI 直存檔案不依賴外部服務 | brain.md | 單一實測 |
| 取代官方記憶 | 主張使用者手動策展比官方 auto memory 更可控、更可信賴 | 手動維護 Obsidian vault（[[topics/llm-wiki-pattern]] 形式） | 單一實測 |
| 團隊共享 | 鎖定「跟著使用者走」而非留在人類設計的筆記/任務管理系統 | OzBrain（HN 69）| 單一實測 |
| 可攜性 | Markdown 規則檔不跨工具 → JSON 協定或格式規約；claude-mem／gentle-ai 規模大但沒有實測 | ltm、OKF、claude-mem 等，見 [[topics/community-tech-patterns]] | 單一實測 |
| 文件自動維護 | codebase wiki 隨對話自動更新，取代手維護 MANUAL.md | CodeAlmanac | 單一實測 |
| 否決方案索引 | 「已被否決」只在人腦或討論串 → 隱形重工；8/31 補上「否決紀錄本身須可驗證、防竄改」 | 兩則概念性觀察（8/7、8/31）| 推論 |

**為什麼會這樣**：跑了數月、數百 session 的 repo，agent 每次重「猜」已知答案既費 token 又重蹈覆轍；社群的共同答案是把記憶從模型搬到 repo 與本地索引，差別只在用什麼形式存、跨不跨工具、以及要不要索性繞過官方記憶機制。

---

### 4. 除錯與分工：多 agent 產出誰把關？

**現在的答案**
- **官方已給**：要 Claude 出示證據（測試輸出、跑過的指令）而不是宣稱完成；`/goal` 只看得到對話裡說過的話，要真的擋住得靠 Stop hook 跑檢查——見 [[topics/coding-workflow-guide]] 第 9 段
- 審查者 agent 不掛編輯工具、只能輸出意見——工具範圍限制比「你是 QA」的角色描述可靠
- 對抗式審查分計畫前、程式碼後兩階段，可串接；跨模型交叉審查（Claude 審 Codex）通過率 71.6%→89.7%、反向反而下降（[arXiv 2607.21656](https://arxiv.org/abs/2607.21656)，量的是解題草稿、審查者不能跑測試，不是 PR review）
- 審查負荷撐不住時往上游移：把把關前移到任務拆解與驗收條件，而非降低審查標準

**🧰 現在就能下的解**：見 [[topics/community-tech-tools]]「我卡在這裡」——「它說做完了，但根本沒做」列（首選 Groundtruth；要留可稽核證據給團隊 → 同列第三欄 Proof Loop）

**還沒解決**：工具範圍只擋「能不能做壞事」，擋不了「有沒有誠實回報」——subagent 靜默失敗（317 項清理、4 種失敗模式回報卻乾淨）仍是缺口。針對它的工具已有兩個（見下表「回報驗證」列），都還沒有第三方使用回饋。

| 子問題 | 社群走到哪 | 代表實作 | 證據強度 |
|---|---|---|---|
| 邊界規則 | 11 條多 agent CLAUDE.md 規則（工作區邊界、禁改共享狀態、merge 責任）；PostToolUse 稽核日誌 | Multi-agent 衝突防範、稽核日誌模式 | 多來源 |
| 對抗式審查 | 計畫前／程式碼後兩做法；唯讀審查者；跨模型交叉審查（論文，解題測試）；另有把審查意見刻意「降階」以免過度採信的單一提案 | Read-Only Reviewer、Agent-plan-review-loop、interns-review-plugin 等，見 [[topics/community-tech-patterns]] | 多來源 |
| 規劃分層 | 規劃層「做什麼」／執行層「怎麼做」；把關前移 | beads 兩層架構、品質把關前移 | 單一實測 |
| 長 session 穩健化 | 心跳／超時重試／狀態快照，從 MCP 層擴到 session（工具失敗、API 500、用量限制各有自動接續） | auto-undo、nightshift、resume-on-ratelimit | 多來源 |
| 回報驗證 | 靜默失敗案例 → 證據紀錄＋可驗證交接 | 「Subagent 在騙你」、Groundtruth、loopx | 單一實測 |
| 相鄰案例 | 六秒 CI 測語意漂移；同形狀 bug 跨 repo 批修 28 PR；PR 協作健康度視覺化 | 語意漂移 CI、批量 OSS 修復、Devthropology | 推論 |

**為什麼會這樣**：單一 Claude 自審自批會照單全收（affirmative bias），多 agent 又需要一致邊界，所以社群先用「權限」而非「人設」約束；Boris Cherny 的心法「給它略難的任務、確保它能沿途驗證自己」（[[entities/boris-cherny]]）是這些做法的上位原則——而「回報是否屬實」是沿途驗證裡最後一塊還沒補上的（推論）。

---

## 目前結論

- 四條線的共同做法是把小專案已驗證的原則（隔離、精簡、對抗式審查、決策外化）**加碼到更大的規模**，而非發明新機制；四條線官方都已給了起點，社群做的多是在官方零件之上加協調、量測與把關。
- 收斂最高的是「除錯與分工」（唯讀＋工具範圍）；「並行規模」的上限沒有定論，可觀測性與落地整合正在補位；「索引與記憶」幾條路線各走各的，還沒有交叉比較。
- **與官方做法頁說法不同的兩處**：[[topics/coding-workflow-guide]] 不再推薦「自己加讀取上限」（官方已內建上限）與「已否決方案索引」（對應官方 issue 已關閉、零回應）；分界是那頁只收官方機制撐得起的做法、本頁記社群走到哪。社群這兩條也只到個別做法與概念觀察，撐不起可執行結論，所以只留在子問題表。
- **你的選項**：官方零件（worktree 隔離、腳本加 `--bare`、auto memory）都是現成的，可以先開起來，撞到哪面牆再照該線的 🧰 行找社群工具；打算跑 10 個以上 agent，可以一段一段加、每段自己量——官方上限與社群崩潰點之間沒有驗證數據。
- **接下來看什麼**：隔離之後的協調（誰先合併、寫碼前就偵測衝突）是並行線最新的方向；fork 子代理的 token 累積有沒有第二則量測，會決定規模上限那一格要不要改寫。

**查過的數字**
- **fork 子代理會不會讓 token 暴增**：《Why 20 Instances Break Down》與 Reddit 回報稱 fork 子代理每次工具呼叫都重送整段對話歷史，四個平行子代理耗約 200 萬 token。
  - [官方 subagent 文件](https://code.claude.com/docs/en/sub-agents)（2026-09-23 查）證實 fork 繼承父對話、拿到與主對話相同的工具池；文件沒有任何「每次重送」或「持續累積」的句子。
  - 所以「累積」是社群推論，「200 萬 token」是單一觀察，官方沒給數字。
- **Graft 的 42%**：Graft 稱裁剪 grep 搜尋輸出可削減 42% token，但 HN 討論質疑其 benchmark 段落疑似 AI 代寫。
  - 查 [GitHub repo](https://github.com/trailhq/Graft) 與 [HN 原討論串](https://news.ycombinator.com/item?id=49299985)（2026-09-20）：42% 來自作者內部 SWE-bench Verified 測試（8,070→4,650 token），**僅 50 題、只跑一次**。
  - HN 指出 README 的 benchmark 段落疑似 Claude／Codex 代寫，且作者自陳的效果提升 **p 值僅 0.22**（不具統計顯著性）。
  - 至今無獨立第三方重現。

---

## 相關實體

- [[topics/community-tech-patterns]]（每個做法的原始證據與出處）、[[topics/community-tech-patterns-archive]]（2026-06 以前的做法與數字）
- [[topics/community-tech-tools]]（卡在某個症狀，社群首選裝哪個）
- [[topics/coding-workflow-guide]]（官方流程每一段怎麼設定，含大型 codebase 的官方設定）
- [[topics/anthropic-agent-stack]] — 本頁的做法用到的官方零件各是什麼、還做不到什麼（本頁講社群怎麼組，那頁講官方給了什麼）
- [[topics/official-community-gap]]（同一個痛點官方補了沒）
- [[topics/community-tech-discussions]]（context 腐蝕 vs 模型退步等設計哲學層討論）
- [[topics/code-quality-decline]]（換版本後變差、帳單變多：怎麼自己量一次）
- [[topics/community-pattern-trends]]（社群做法收斂成的方向、各自怎麼走到今天）
- [[entities/claude-code]]、[[entities/managed-agents]]（各功能的版本紀錄與已知問題；Managed Agents 是平台代管的另一個產品）
- [[entities/boris-cherny]]（千級子代理工作流、「沿途驗證」心法）

%% 週更撈料：patterns 節點以 `**主線：**` 欄位標記所屬線（規則：.claude/reporter-rules/community/daily.md「主線 tag 規則」、weekly.md「週更整線重寫」）；週更已收至 2026-09-16 %%

## 參考來源

每個做法的原始出處在 [[topics/community-tech-patterns]]，2026-06 以前的在 [[topics/community-tech-patterns-archive]]；本頁只直接連讀者最常追的一手——官方文件與論文。

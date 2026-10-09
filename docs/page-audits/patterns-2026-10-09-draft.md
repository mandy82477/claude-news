# 第 18 波逐字稿：topics/community-tech-patterns 拆成母頁＋七個子頁（2026-10-09）

> 分兩欄：**進頁面**（母頁全文；子頁到 `## 技術彙整` 為止，之後的節點由 `scratchpad\w18\split_patterns.py` 填入，本稿不抄 251 則）與**進規則檔**。
> 頁面逐字以 `scratchpad\w18\out\generated\*.md` 為準（`split_patterns.py` 輸出、再在臨時副本跑過 `gen_wiki_frontmatter.py`）；本稿是它的抄本。frontmatter 由 gen 生成，實作者不手填——下列 frontmatter 是副本實跑的結果，供核對形狀。
> 「最後更新」寫 2026-10-09；實作日不同就改成實作日（八頁同一天）。行號指現檔。

## 行數與字數（正文＝扣 frontmatter）

| 頁 | 正文行 | 正文字元 | 其中 `## 技術彙整` 之前 |
|---|---|---|---|
| community-tech-patterns | 180 | 11,045 | 101 |
| community-multi-agent | 477 | 34,188 | 109 |
| community-memory | 385 | 26,829 | 36 |
| community-cost | 375 | 25,187 | 37 |
| community-skills | 431 | 31,432 | 42 |
| community-guardrails | 348 | 24,761 | 54 |
| community-integrations | 383 | 24,583 | 30 |
| community-interfaces | 231 | 13,686 | 30 |
| 合計 | 2810 | 191,711 | |
| （拆前 community-tech-patterns） | 2461 | 180,329 | |

母頁 ≤300 行：實數正文 180 行（含 frontmatter 205 行）。＝原文 128＋新寫 52。八頁合計比拆前多 349 行＝新寫 296（母頁 52、七子頁 244）＋子頁重建的月份標題與懸置標頭 81，減去丟棄的包裝 16 與改寫掉的 12（`out\accounting.txt`）。

---

# 進頁面

## 1. 母頁 `wiki/topics/community-tech-patterns.md`（全文）

````markdown
---
page: "topics/community-tech-patterns"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 2
parent: null
children: "['topics/community-cost', 'topics/community-guardrails', 'topics/community-integrations', 'topics/community-interfaces', 'topics/community-memory', 'topics/community-multi-agent', 'topics/community-skills', 'topics/community-tech-patterns-archive']"
page_role: "hub"
days_since_news_subtree: 2
inbound_links: 60
attribution_count: 265
attribution_last: "2026-10-07"
top_source: "github"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---

# Claude Code 社群工作流模式

**狀態：** ongoing
**領域：** 🌐 社群
**開始日期：** 2026-04-25
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新工作流模式**（2026-10-07）
> - **記憶與知識管理添 token-savior**：結構化程式碼導覽＋持久記憶，作者自測編碼基準達 97.9%、token 降 80%。
> - **Plugin / MCP 整合添豆包搜索、瑞士求職 CLI**：分別補國產模型連網能力、求職流程 MCP 化。
> - **機器人控制、依賴地圖首次出現**：ros-mcp-server（1,488★）接 ROS、mellos-mapping 畫即時依賴地圖，皆單一實作新切面。

---

## 摘要

社群拿 Claude Code 玩出哪些做法、哪些已經站住腳、哪些還在試。二十類做法依讀者會問的問題分成七個子頁，每頁有自己的目前結論與逐則證據，入口在下方「每一類做法住哪一頁」；本頁只留總覽：模式概覽表標每一類的成熟度與最後動態，「現在收斂到哪」寫跨類的結論。

已經定案的四類是 Skills 設計、Multi-agent 架構、CLAUDE.md 管理、Hooks 與自動化，定案的是四句話：隔離用 worktree、規則用 Hooks 強制、流程封裝成 skill、CLAUDE.md 寫規則不寫建議。還在試的十六類裡，2026-09-25 起有新動靜的十類。官方唯一一則一手依據是 Anthropic 2026-07-26 移除逾 80% Claude Code 系統提示詞那則，住 [[topics/community-memory#2026-07]]。

已經收斂成方向的做法怎麼一步步走到今天、你現有設計可以回頭檢查什麼，見 [[topics/community-pattern-trends]]（那頁是策展過的結論，本頁與子頁是原始證據）。工具該裝哪個見 [[topics/community-tech-tools]]，**社群在吵哪些觀念、哪些吵出共識**見 [[topics/community-tech-discussions]]「現在吵到哪」，大型 codebase 的四條主線見 [[topics/community-large-codebase-workflow]]。

---

## 每一類做法住哪一頁

| 子頁 | 答什麼 | 收哪幾類 | 最後動態 |
|---|---|---|---|
| [[topics/community-multi-agent]] | 多個 agent 怎麼分工、隔離、協調；開到 10 個以上會怎樣、怎麼停下來；官方機制對照與缺口 | Multi-agent 架構、Agent 規模化、Agent Loop 終止條件 | 2026-10-06 |
| [[topics/community-memory]] | 怎麼讓 agent 跨 session 記得專案、CLAUDE.md 怎麼寫才會被照做、context 怎麼不被撐爆 | 記憶與知識管理、CLAUDE.md 管理、Context 管理 | 2026-10-07 |
| [[topics/community-cost]] | 怎麼省 token、怎麼看見花了多少、哪種任務派哪個模型 | Token / 成本優化、模型使用策略 | 2026-10-06 |
| [[topics/community-skills]] | skill 怎麼寫才會觸發、有哪些慣例與地雷、品質怎麼量 | Skills 設計 | 2026-10-07 |
| [[topics/community-guardrails]] | 怎麼讓規則被強制而不只是建議、多 agent 的產出誰來審、怎麼防 agent 亂來或洩漏密鑰 | Hooks 與自動化、安全架構、多代理 PR Review、規格驅動開發、架構邊界合約 | 2026-10-05 |
| [[topics/community-integrations]] | 社群接了哪些 MCP 與 plugin、MCP 斷線或逾時怎麼辦、agent 能不能接進創作工具 | Plugin / MCP 整合、MCP 長 Session 穩健化、創意工具 Agent 整合 | 2026-10-07 |
| [[topics/community-interfaces]] | 能不能從手機控制、有沒有更好的終端機、怎麼看到 agent 正在做什麼 | 介面元件複用、行動裝置遠端控制、Agent 活動可視化 | 2026-10-07 |

一則做法若同時屬於兩類，住它第一個寫到的那一類的子頁；還分不出類的新做法，先放在本頁下方「技術彙整」的「未歸類」。

---

## 模式概覽

> 一類一列；「最後動態」是這一類最後一次有新做法進來的日期，「代表技巧」末的連結指那一則所在的子頁月份。

| 類別 | 代表技巧 | 成熟度 | 最後動態 | 核心概念 |
|---|---|---|---|---|
| **Skills 設計** | 知識框架化、drawio-skill、personal-os-skills、reladraw、geo-score、open-steps 等（[[topics/community-skills#2026-10]]） | ✅ 成熟 | 2026-10-07 | description 自動觸發，把書籍與流程封裝成可複用 skill |
| **Multi-agent 架構** | Claude Squad、ccteams、OtoDock、omnigent、orca、hcom、FrontierAgent、amux、Offrun 等（[[topics/community-multi-agent#2026-10]]） | ✅ 成熟 | 2026-10-06 | orchestrator 分派 ＋ 獨立 git worktree，防答案塌縮 |
| **Hooks 與自動化** | PostToolUse 稽核、Git Hooks 品質門、claude-code-hooks 外掛市集、精簡輸出外掛、sloppy（[[topics/community-guardrails#2026-10]]） | ✅ 成熟 | 2026-10-04 | 強制執行勝過建議；CLAUDE.md 做偏好、Hooks 做邊界 |
| **CLAUDE.md 管理** | 精簡規則策略、Self-improving Rules、防腐爛機制（[[topics/community-memory#2026-10]]） | ✅ 成熟 | 2026-10-01 | 寫成「規則」而非「建議」，CI 攔截違反架構的 PR |
| **Plugin / MCP 整合** | docsagent、solomd、atlassian-mcp-server、remote-desktop-commander、pipeboard 等（[[topics/community-integrations#2026-10]]） | ⚡ 活躍 | 2026-10-07 | 避免不必要的 context 載入；Claude Code 主導 MCP 工具鏈 |
| **記憶與知識管理** | claude-mem、projectmem、second-brain-os、agent-memory、deja-vu、hippo-memory 等（[[topics/community-memory#2026-10]]） | ⚡ 活躍 | 2026-10-07 | 跨 session、跨工具、跨機器的持久記憶協定 |
| **Context 管理** | Just-in-Time @-file、Repo-as-Memory、對話分支與合併、nightshift（[[topics/community-memory#2026-10]]） | ⚡ 活躍 | 2026-10-07 | 即時取回優於預先載入；避免 context 過早飽和 |
| **Token / 成本優化** | MCP Code Execution、穴居人模式、pxpipe、headless 冷啟動、I-have-ADHD、Pulse、mcptoon（[[topics/community-cost#2026-10]]） | ⚡ 活躍 | 2026-10-06 | HTML 轉 Markdown 降 80% token；快取不跨 session 是費用主因 |
| **模型使用策略** | 分層模型、多模型路由、Workweave Router、Fable 5 編排、MaskShift、magpie、jev-router（[[topics/community-cost#2026-09]]） | ⚡ 活躍 | 2026-09-30 | 依任務複雜度路由；社群轉載數字 46% 成本／96% 效能（非官方基準，見 [[entities/fable-5]]） |
| **多代理 PR Review** | 4-agent Code Review、對抗性審查、Read-Only Reviewer、interns-review-plugin（[[topics/community-guardrails#2026-09]]） | ⚡ 活躍 | 2026-09-05 | 架構師代理協調 ＋ 跨廠商模型交叉審查 |
| **介面元件複用** | Brainless、statuslin.es、dsh-TUI、better-agent-terminal、coralline、ClaudeTerm（[[topics/community-interfaces#2026-10]]） | ⏳ 新興 | 2026-10-06 | 把 AI coding 工具的介面美學封裝成可一鍵安裝的前端元件 |
| **安全架構** | Grepathy、OneCLI、agent-scan、自主 agent 部署閘、ThinkWatch-Lite、WaLiAPI（[[topics/community-guardrails#2026-10]]） | ⏳ 新興 | 2026-10-05 | AI 加速開發下的系統性防線；CI 攔截語義退化 |
| **創意工具 Agent 整合** | Palmier Pro、reelmimic、comfyui-mcp、video-talkcraft、GodotMaker 等（[[topics/community-integrations#2026-10]]） | ⏳ 新興 | 2026-10-04 | 把 agent 整合從程式碼場域擴到創作工具鏈 |
| **行動裝置遠端控制** | ccgram、Android Remote Control MCP、Shellular、CLI-WeChat-Bridge、Mobile-Harness（[[topics/community-interfaces#2026-10]]） | ⏳ 新興 | 2026-10-04 | 手機當 agent 控制介面，各自選不同傳輸層 |
| **Agent 活動可視化** | claude-office 即時像素風辦公室模擬、agent-office 3D 卡通辦公室（[[topics/community-interfaces#2026-10]]） | ⏳ 新興 | 2026-10-02 | 把 Claude Code 工具呼叫映射成遊戲化空間視覺化，取代純文字終端機輸出（推論） |
| **Agent 規模化** | 20-instance 崩潰分析、Personas vs Tool-scoping、agent-channels（[[topics/community-multi-agent#2026-09]]） | ⏳ 新興 | 2026-09-16 | 超過 10 個並行 agent 需獨立 worktree ＋ orchestrator 協調層 |
| **規格驅動開發** | spec-kit（[[topics/community-guardrails#2026-09]]） | ⏳ 新興 | 2026-09-12 | 先產出可審查的規格／計畫再讓 agent 依此實作（spec→plan→tasks→implement），取代直接下 vibe coding 提示 |
| **Agent Loop 終止條件** | Loop exit condition 設計模式（[[topics/community-multi-agent#2026-08]]） | ⏳ 新興 | 2026-08-19 | 「怎麼停下」比「怎麼跑起來」更難；要有顯式終止條件 |
| **MCP 長 Session 穩健化** | MCP server 失效模式防護（[[topics/community-integrations#2026-08]]） | ⏳ 新興 | 2026-08-14 | 連線中斷、工具超時、上下文失憶；對應心跳、重試、快照 |
| **架構邊界合約** | ANMA YAML contracts、ISO 29148 規格驅動（[[topics/community-skills#2026-08]]） | ⏳ 新興 | 2026-08-12 | 用合約與工業標準定義不可越過的架構規則 |

> 成熟度：✅ 成熟（社群廣泛實踐）／⚡ 活躍（持續演進中）／⏳ 新興（近期出現，尚在探索）

**七類已超過 60 天或算不出最近的動靜，原始條目仍在：** Agent 版本控制（ADR 注入、架構決策文件先於實作，最後動態 2026-07-31，已逾 60 天移出，原始條目見 [[topics/community-guardrails#2026-07]]）、Agent 預算控制（AgentWatch runtime budget enforcement，最後動態 2026-07-22，已逾 60 天移出，原始條目見 [[topics/community-skills#2026-07]]）、可靠性測試（Caliper pass@k 指標測試、Skill Linter，最後動態 2026-07-12，已逾 60 天移出，原始條目見 [[topics/community-skills#2026-07]]）、跨環境 Agent 記憶（Core Memory Packet，代表技巧與「記憶與知識管理」重疊，已併入該列）、確定性 Agent 框架（Agentic Orchestrator 混合架構）、Agent 記憶保護（結構化 Markdown 編輯器取代 regex）、跨 Repo 依賴可視化（cross-repo blast radius 分析）——後三類的原始條目見 [[topics/community-tech-patterns-archive#2026-06]]。

---

## 現在收斂到哪、哪些還在試

- **已經定案的四類**（Skills 設計、Multi-agent 架構、CLAUDE.md 管理、Hooks 與自動化）：隔離用 worktree、規則用 Hooks 強制而非建議、流程封裝成 skill，近三個月沒出現反對意見。
  **接下來看什麼：** 各子頁之後的新做法是否還在複述這幾句，複述停了就是真的定案。
- **多 agent**：隔離已定案，隔離之後誰先合併、誰驗收還沒有官方答案，社群自己補。見 [[topics/community-multi-agent]]「目前結論」。
- **記憶、CLAUDE.md 與 context**：方向收斂成兩層（官方 auto memory＋把決策寫回 repo），工具與格式還沒收斂。見 [[topics/community-memory]]「目前結論」。
- **成本控制仍是多 agent 最大的未解項**：四個平行子代理耗掉約 200 萬 token（[[topics/community-memory#2026-08]]），但把純 I/O 工作路由給便宜模型可降 90% token（[[topics/community-cost#2026-09]]）。
  - 同一個問題兩個相反答案，還沒收斂。官方數量級參照見 ⟨Q-06⟩：多 agent 系統約耗一般對話 15 倍 token。
- **Skills**：觸發寫法是最大的地雷，慣例與地雷整理在 [[topics/community-skills]]「慣例與地雷」。
- **規則、把關與安全**：強制勝過建議；「檢查型」與「強制型」把關的分界與各自破口見 [[topics/community-guardrails]]「目前結論」。
- **外部整合**：十月新做法最多的一群，但還沒有人篩過「哪個值得裝」；該裝哪個看 [[topics/community-tech-tools]]，逐則證據見 [[topics/community-integrations]]。
- **手機、介面與可視化**：先試官方的遠端控制；社群走 bot、MCP、web-app 三條路，沒有逐項比較。見 [[topics/community-interfaces]]「目前結論」。
- **還在試的十六類裡，2026-09-25 起有新動靜的十類**：最後動態停在九月中旬以前的六類是 Agent 規模化、規格驅動開發、多代理 PR Review、Agent Loop 終止條件、MCP 長 Session 穩健化、架構邊界合約。

**懸置細節**
- ⟨Q-06⟩ **「多 agent 約耗 15 倍 token」官方原文**：已查證（[Anthropic 官方部落格](https://www.anthropic.com/engineering/built-multi-agent-research-system)，2025-06-13 發布，查證日 2026-09-20）。
  - 原文：「agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats」。
  - [[topics/community-tech-patterns-archive]] 先前的轉述屬實。

> 概念辯論與設計哲學見 [[topics/community-tech-discussions]]

### 缺口追蹤：文獻主張 × Claude Code 現況

文獻主張的多 agent 機制，Claude Code 補了哪幾項、哪幾項還沒補，逐列見 [[topics/community-multi-agent#缺口追蹤：文獻主張 × Claude Code 現況]]。

---

## 技術彙整

> 每一則做法的原始證據依類別住在七個子頁（見上方「每一類做法住哪一頁」）。這裡只留還分不出類的新做法，以及早期月份的總結。

### 未歸類

目前沒有。

### 2026-07

2026-07 的原始條目依類別分住各子頁：[[topics/community-multi-agent#2026-07]]、[[topics/community-memory#2026-07]]、[[topics/community-cost#2026-07]]、[[topics/community-skills#2026-07]]、[[topics/community-guardrails#2026-07]]、[[topics/community-integrations#2026-07]]、[[topics/community-interfaces#2026-07]]。

%% 拆頁評估 2026-10-09：已依讀者問題拆成七個子頁（第 18 波）。本節與上方「缺口追蹤」h3 兼作過渡錨點，給 coding-workflow-guide 的 #2026-07 與 official-community-gap 的 #缺口追蹤 兩條舊連結落腳；兩張轉知單結案後刪 h3，本節在 2026-07 蒸餾時改成時段總結。 %%

### 2026-06

多 agent 規模化與崩潰分析成為主軸：20 個並行 instance 的崩潰原因（共享資源競爭、context 洩漏至鄰近 agent）催生獨立 orchestrator 層與 git worktree 隔離的具體對策；Aharness（FSM 強制流程）、ANMA（YAML 邊界合約，實測 0/20 架構違規）等框架把「規則遵守」從建議層推進強制層，呼應本月「Hooks 取代 CLAUDE.md 規則」的核心共識。

Token/context 裁剪從討論走向實測：Compact Memory 提出 O(N²)→O(N) 壓縮，但後續查證未見獨立第三方重現（已標懸置）；Context 裁剪 tool output、Just-in-Time @-file Retrieval、Agent Context 上限主動管理三者共同指向「少讀、少存、按需取回」。跨 session 記憶方案百花齊放（OKF 物件鍵格式、beads 兩層規劃架構）但尚無收斂共識。

成本感知路由本月首見大規模採用訊號：Workweave Router（HN 181，本月社群工具最高分）針對 Opus 4.7 成本暴增問題以隱式難度評估取代手動路由規則。

仍具引用價值：Workweave Router、ANMA、Aharness、AgentWatch（runtime 預算攔截層）、Read-Only Reviewer Agent（唯讀審查者權限約束設計）。

原始條目見 [[topics/community-tech-patterns-archive#2026-06]]

### 2026-05

本頁草創期：CLAUDE.md 管理（領域化安全規則、各語言生態規則集同日密集出現、防腐爛機制）、multi-agent 架構（worktree/OS 帳號獨立隔離、11 條多 agent 衝突防範規則）、hooks 強制化（PostToolUse 生產稽核、Git hooks 代碼品質門檻）三大類別的首批案例集中於本月奠基。

跨環境記憶協定百花齊放但尚未收斂：ltm（JSON Core Memory Packet）、Memex（本地 RAG）、本機圖資料庫索引、Iantha（純 Markdown+git，後續查證未見獨立報導，已標懸置）——均解決「記憶不可跨 session/工具攜帶」，各自實作路線互不相通。

官方功能首次系統性採納社群既有模式：[[entities/managed-agents]] 的 Dreaming（記憶整合）、Outcomes（規格驅動執行）、20 路並行子代理三項機制被視為對社群做法（Dreamer、beads、Harness）的制度化；`/goal` fire-and-forget 指令發布後引發「Anthropic 抄自開源」爭議。

大規模並行實踐標竿：[[entities/boris-cherny]] 公開數千子代理夜間工作流，是 Managed Agents 並行能力在個人工作流的極端應用案例。

原始條目見 [[topics/community-tech-patterns-archive#2026-05]]

---

## 相關實體

- [[entities/claude-code]]
- [[entities/claude-skills]]（官方 Skills 產品線與生態單一入口——官方 bundle、平台支援、第三方移植；本頁只管 skill 設計面）
- [[entities/pricing]]（token 消耗與模型選擇策略相關）
- [[entities/managed-agents]]（官方 Agent 框架：Dreaming 記憶整合、20 路並行、Outcomes 規格驗證）
- **Project Deal**（Claude 代理人交易談判實驗，multi-agent 應用的商業探索；詳見 [[entities/claude-code]]）
- [[entities/claude-design]]（AI 設計工具，與 Claude Code + Figma MCP 工作流有定位重疊）
- [[topics/community-tech-discussions]]（概念辯論、設計哲學、實證研究）
- [[topics/community-tech-patterns-archive]]（2026-04-25～05-22 的社群時序流水帳，已併入該頁）
- [[topics/community-large-codebase-workflow]]（大型 codebase 規模化開發主題式主線：並行規模、Context/Token 管理、索引與記憶、除錯與分工，從本頁節點縫成）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [[news/2026-05-03]]
- [[news/2026-05-04]]
- [[news/2026-05-05]]
- [[news/2026-05-06]]
- [[news/2026-05-07]]
- [[news/2026-05-08]]
- [[news/2026-05-09]]
- [[news/2026-05-11]]
- [[news/2026-05-14]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-15]]
- [[news/2026-05-17]]
- [[news/2026-05-16]]
- [[news/2026-05-22]]
- [[news/2026-05-23]]
````

## 2. 子頁 A：`wiki/topics/community-multi-agent.md`

````markdown
---
page: "topics/community-multi-agent"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-06"
status_main: "ongoing"
days_since_news: 3
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 3
inbound_links: 2
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：多 agent 怎麼分工與協調

社群把多個 Claude Code agent 組起來跑的做法：怎麼分工、怎麼隔離、隔離之後怎麼協調、開到多大、怎麼停。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-01
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-06

> **最新做法**（2026-10-06）
> - **跨廠商協調器再添一款**：open-mercato/cezar 平行執行 Claude Code、Codex、OpenCode、Pi 等多款 agent。
> - **同一工作區並排管理多款 agent**：Offrun（10-03，Show HN）把 Claude Code、Codex、AGY、Grok Build 放進同一個工作區。

---

## 摘要

官方給了三條路：subagent 是做完回報的工人（官方原話「quick, focused workers that report back」）；agent teams 讓隊友彼此傳訊、自己協調，目前實驗性、預設關閉；cross-session 讓獨立 session 互傳文字（[sub-agents](https://code.claude.com/docs/en/sub-agents)、[agent teams](https://code.claude.com/docs/en/agent-teams) 官方文件，2026-10-09 查證）。社群這邊，每個 agent 一個 worktree 的隔離已經定案；隔離之後誰先合併、誰驗收，官方還沒有答案，社群用合併佇列和控制平面自己補。

下方三節是官方機制與學術名詞的對照、「誰來拆任務」的五種來源、文獻主張的缺口補了沒；「技術彙整」是逐則證據。大型 repo 上並行互踩的現在答案見 [[topics/community-large-codebase-workflow]] 第 1 線，隔離這個方向怎麼走到今天見 [[topics/community-pattern-trends]] 趨勢二。

---

## 目前結論

- **隔離已定案**：每個 agent 開一個 git worktree，官方已內建（subagent 設 `isolation: worktree` 就拿到一份獨立的 repo 副本）。agent teams 這邊沒有隔離（見下方缺口追蹤「協調與衝突解決」那一列）。
- **戰線已經從「怎麼隔離」移到「隔離之後怎麼協調」**：worktree 解決了互相覆蓋，但沒有解決誰先合併、誰驗收（見下方缺口追蹤「協調與衝突解決」那一列）。**你的選項：** 用本地合併佇列（[[topics/community-multi-agent#2026-07]]）自己排序，或維持人工把關，或等官方補。
- **開到多大**：超過 10 個並行 agent 要獨立 worktree 加一層協調；官方 session 預設同時跑到 20 個 subagent 時再開新的會失敗，上限可用 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 調（官方 sub-agents 文件，2026-10-09 查證）。
- **怎麼停下來**：「怎麼停」比「怎麼跑起來」更難，要寫顯式終止條件；目前只有一則做法（2026-08-19），還在試。
- **接下來看什麼：** 官方 agent teams 何時脫離實驗性、會不會補上隔離；社群控制平面（amux、cezar、Offrun 這一路）有沒有人拿出跨工具比較。

**機制細節**
- **Multi-agent 架構**：ccteams 將驗證良好的 subagent 組合打包為可跨專案安裝的套件；OtoDock 將 Claude Code 與 Codex 組成協作團隊部署於自有伺服器；omnigent 把協調邏輯與底層 harness（Claude Code／Codex／Cursor／Pi）解耦，換 harness 不必重寫協作邏輯
- **Agent 規模化**：工具範圍限制比角色描述更可靠的邊界守護；無人監督排程任務已有完整 Mac Mini M4 方案；可觀測性層（live-log-viewer-next）開始補足「多 agent 進度難追蹤」的協調盲點；agent-channels 提供跨 worktree 通訊

---

## 學術對照：多智能體 orchestration 術語

**資料截至 2026-10-09**（官方文件查證）。Claude Code 的多 agent 機制官方分成三層階梯：subagent（結果回報主 agent）→ agent teams（共享任務表、彼此傳訊，實驗性、預設關閉）→ cross-session（獨立 session 之間傳純文字）。

| Claude Code 機制 | 官方狀態 | Anthropic《Building Effective Agents》 | 控制流 | 通訊原語 |
|---|---|---|---|---|
| **Subagent** | 正式，預設可用 | Orchestrator–Workers；用於審查時為 Evaluator–Optimizer | Dynamic | 父子之間直接傳訊，單回合請求與回應 |
| **Workflow** | 正式，預設可用 | Workflow 類：Prompt Chaining ＋ Parallelization | Static（腳本寫死、可重現） | 由程式碼中繼，agent 之間不通訊 |
| **Agent Teams** | 實驗性，預設關閉 | Agent（autonomous）側的多 agent 協作 | Dynamic／emergent | 任務表當共享黑板、信箱直接傳訊、依賴自動解鎖 |
| **Cross-session 傳訊** | 正式，預設開啟 | 不在該文分類內 | Dynamic | 獨立 session 之間傳純文字，不帶對話歷史或檔案 |

**補充對照：** 手動開兩個 session ＋ 共享檔案協調，只有共享記憶一個原語且被動輪詢，所以無法自動反應；Agent Teams 在此之上補了直接傳訊與依賴解鎖。官方明載團隊之間不可巢狀、一個 session 只能有一個團隊、lead 不可更換，多層階層只能靠 subagent 巢狀：預設最多往下三層，可用 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 調。

### 誰負責拆分（decomposition）

「誰來拆分任務」是選用機制的核心軸。五種來源對應不同場景，官方欄為 2026-10-09 查證的官方文件說法。

| 拆分來源 | 對應機制 | 官方怎麼說（2026-10-09 查證） | 應用場景 |
|---|---|---|---|
| 模型自動委派 | **Subagent**（官方預設） | Claude 依你的要求、subagent 描述欄與當前脈絡自動決定何時委派 | 你不想管拆法，只想設好邊界 |
| 人類事先凍結成確定性流程 | **Workflow / Skill** | 官方無自動化，靠你自己把流程寫成 skill | 同形狀改動批量、每個 PR 跑固定維度審查 |
| 強模型當場動態拆 | **Subagent**（社群做法） | 官方未提供「編排者與工人分別指定模型」的預設，但可在 subagent 定義填 model 欄自行指定 | 進陌生子系統修 bug，人在旁隨時修正方向 |
| lead 拆分後隊友自領 | **Agent Teams**（實驗性） | lead 把工作拆成任務並自動指派；隊友做完會自己認領下一個未指派、未卡住的任務 | 跨層 feature，拆法邊做邊長出來 |
| 不拆分 | 單一 session | — | 一句話描述得完的小改動 |

**社群這邊實際跑出來的三則：**
- 單一長 session 加 147 個 subagent、24 天完成一次移植（[[topics/community-multi-agent#2026-09]]）——證明「一個人拆、模型執行」在超長專案上撐得住。
- 四個平行子代理耗掉約 200 萬 token，疑似每次工具呼叫都重送整段歷史（[[topics/community-memory#2026-08]]）——動態拆分的成本上限還沒有人量出來。
- 分層做法：Opus 當腦、Sonnet 當手，加一份持久狀態檔（[[topics/community-multi-agent#2026-08]]）——社群自己補官方沒給的分模型編排。

**文獻怎麼說（截至 2026-07-22）：** 拆分才是瓶頸，弱的拆分者卡死全系統而強的執行者補不回，且拆分只佔約 20% token（PEAR）；粒度應按執行者能力當場調整（ADaPT、Coarse-to-Fine）；人類介入的正確形式是在共享計畫上持續協調並中途糾錯，不是交一份完稿（Cocoa）；重複性任務把規格與拆法凍結成 skill。

**參考論文／來源：**
- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)（Workflow vs Agent；orchestrator-workers、routing、parallelization、evaluator-optimizer、prompt chaining 五 pattern）
- [LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns（Future Internet, 2026）](https://doi.org/10.3390/fi18060326)（centralized／decentralized／hierarchical／blackboard；三種 communication primitives）
- [Multi-Agent Collaboration Mechanisms: A Survey of LLMs（arXiv:2501.06322）](https://arxiv.org/pdf/2501.06322)
- [PEAR: Planner-Executor Agent Robustness Benchmark（arXiv:2510.07505）](https://arxiv.org/html/2510.07505v3)（強 planner > 強 executor；planning ~20% token）
- [ADaPT: As-Needed Decomposition and Planning with Language Models（arXiv:2311.05772）](https://arxiv.org/pdf/2311.05772)（按 executor 能力遞迴拆分）
- [From Coarse to Fine: Self-Adaptive Hierarchical Planning for LLM Agents（arXiv:2604.23194）](https://arxiv.org/pdf/2604.23194)（拆分粒度自適應）
- [How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning（arXiv:2605.23023）](https://arxiv.org/pdf/2605.23023)、[JumpStarter（arXiv:2410.03882）](https://arxiv.org/pdf/2410.03882)（mixed-initiative／共享計畫協調）
- [Spec-Driven Development with AI Coding Agents（2026）](https://zeroshot.ghost.io/spec-driven-development-with-ai-coding-agents/)（Spec→Plan→Tasks→Implement；skill 讓流程可重複）

### 缺口追蹤：文獻主張 × Claude Code 現況

**資料截至 2026-10-09**（官方文件查證；「通訊原語」「脈絡交接」兩列為 2026-09-06，「信任與驗證層」一列為 2026-10-04）。狀態三值：已補／部分補上／未補。

| 缺口 | 文獻主張 | 現況 | 狀態 |
|---|---|---|---|
| 通訊原語 | 共享黑板需補直接傳訊與事件驅動 | cross-session 傳訊 v2.1.224 起預設開啟，任意 session 皆可互傳，涵蓋跨機器；共享頻道式 A2A（issue #28300）仍缺，見 [[topics/official-community-gap]] | 已補（2026-09-06 查證；措辭於 2026-09-20 依 official-community-gap 對齊） |
| 編排者與工人的脈絡交接 | 工人需承接編排者的上下文才接得住任務 | fork 型 subagent 繼承整段對話與工具集，互動 session 預設開啟 | 已補（2026-09-06 查證） |
| 強拆分者勝過強執行者 | 應把強模型或人力投在拆分 | subagent 定義有 model 欄，呼叫時可另行指定，也有全域環境變數；官方 agent teams 文件的範例以 Sonnet 當隊友 | 已補（2026-10-09 查證） |
| 動態粒度 | 拆分粒度應按執行者能力當場調整 | 官方只有工作流大小三檔靜態旋鈕，截至查證日未見動態粒度 | 未補（2026-10-09 查證） |
| 共享計畫的雙向編輯 | 人類應能在共享計畫上持續協調並中途糾錯 | 可中途插話，但沒有雙方都能編輯的計畫載體 | 未補 |
| 協調與衝突解決 | 多 agent 併行需要協調衝突的機制 | 官方答案是 git worktree 隔離——用不共用工作區迴避協調，不是解決協調；agent teams 連隔離都沒有，官方只建議每位隊友各管一組檔案 | 未補 |
| 信任與驗證層 | 多 agent 產出需要信任與驗證機制 | 官方已有完成判定與攔截零件，仍無跨 agent 產出的信任機制，也不保證品質；零件與理由見下方細節 | 部分補上（2026-10-04 查證） |

**信任與驗證層（2026-10-04 查證）**
- 官方零件：`/goal` 判完成條件、`/code-review`（v2.1.218 起背景執行，v2.1.288 加 `--max-findings`）。
- v2.1.287 Mods 可掛旁觀 agent，內建 `cc-plugin-you-should-know`，預設停用。
- 判「部分補上」：先前說的空白已不成立；但這些答的是做完沒、能不能攔，不保證品質，也沒有跨 agent 的信任機制。
- `/code-review` 自 v2.1.215 起不自動觸發（見下方倒退項）。社群工具見 [[topics/community-guardrails]]「把關層彙整」。

**一項倒退：** v2.1.215（2026-07-19）起 `/verify` 與 `/code-review` 不再自動觸發，評估與改進的迴路從自動降為手動（見下方懸置細節 ⟨Q-07⟩ 已查證：未恢復）。

**懸置細節**
- ⟨Q-07⟩ **是否已恢復自動觸發**：已查證（[GitHub Release v2.1.215](https://github.com/anthropics/claude-code/releases/tag/v2.1.215)，查證日 2026-09-20）——官方將此列為明確變更項：`/verify` 與 `/code-review` 不再自動執行，需明確以指令呼叫才會觸發；此後官方文件與後續版本 changelog 均未再提及恢復自動觸發，判定**未恢復**、維持手動。

**與官方缺口矩陣互見：** [[topics/official-community-gap]] 是官方視角（官方功能 vs 社群痛點的完整追蹤），上表是文獻視角（學術文獻主張 vs Claude Code 現況）——查「官方功能覆蓋到哪」去那頁，查「文獻主張有沒有兌現」看這裡。

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 40 則節點，月份分組 2026-10 2 則、2026-09 23 則、2026-08 10 則、2026-07 5 則⟫
````

## 3. 子頁 B：`wiki/topics/community-memory.md`

````markdown
---
page: "topics/community-memory"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 2
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 4
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：記憶、CLAUDE.md 與 context

社群讓 Claude Code 記得專案的做法：跨 session 記憶、CLAUDE.md 怎麼寫、context 怎麼不被撐爆。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-10
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **記憶工具添 token-savior**：結構化程式碼導覽＋持久記憶，作者自測編碼基準 97.9%、token 降 80%，尚無第三方覆核。
> - **context 該移到哪**：10-06〈Claude Code Context Is Like a Fridge〉談主對話容量有限時，何時把工作移到 subagent、第二個 session 或 headless。

---

## 摘要

最常見的做法是兩層：底層用官方 auto memory，讓 Claude 跨 session 自己記筆記（[官方 memory 文件](https://code.claude.com/docs/en/memory)；每個 session 載入多少、它不是強制設定，見 [[topics/community-large-codebase-workflow]] 第 3 線）；上層把已確定的決策寫回 repo——CLAUDE.md、spec、ADR——不靠模型自己記住。context 這邊的共識是少讀、按需取回，不預先塞滿。

收斂了沒：方向收斂了（[[topics/community-pattern-trends]] 趨勢九），做法沒有。七月以來每週都有新的記憶工具進來，格式互不相通，沒有一條路線經過第二方採用驗證。該裝哪個先看 [[topics/community-tech-tools]]「每開新 session 都要重講一遍」那一列。

---

## 目前結論

- **記憶**：官方 auto memory＋把決策寫回 repo 是現在的底；社群工具（claude-mem、projectmem、brain.md、token-savior 等）各走一路，還沒收斂。**接下來看什麼：** 有沒有人拿兩三個工具在同一個專案上做比較。
- **CLAUDE.md**：寫成規則而不是建議，違反架構的改動交給 CI 或 hook 攔；要 100% 遵守的規則不該只放 CLAUDE.md，見 [[topics/community-guardrails]]。
- **Context**：即時取回優於預先載入；官方 2026-07-26 移除逾 80% Claude Code 系統提示詞，是這條路唯一的廠商一手依據（見下方 2026-07）。
- **你的選項：** 先用官方 auto memory，決策寫進 repo；要團隊共享或跨工具攜帶時才加社群工具，並記得它們都還沒有第二方驗證。

**機制細節**
- **記憶與知識管理**：OKF 標準化 agent 知識格式供團隊共用；已否決方案未結構化記錄會導致 agent 重新實作已被殺掉的方案；OzBrain 主張取代傳統筆記/任務管理工具，鎖定團隊共用而非單一使用者記憶；Karpathy 式 LLM wiki 這條路線的設計對照見 [[topics/llm-wiki-pattern]]

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 39 則節點，月份分組 2026-10 8 則、2026-09 14 則、2026-08 11 則、2026-07 6 則⟫
````

## 4. 子頁 C：`wiki/topics/community-cost.md`

````markdown
---
page: "topics/community-cost"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-06"
status_main: "ongoing"
days_since_news: 3
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 3
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：token、成本與模型路由

社群在 Claude Code 上省 token、看見花費、把任務分派給不同模型的做法。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-03
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-06

> **最新做法**（2026-10-06）
> - **別把工具塞進 context**：Armin Ronacher〈What is Codemode〉重申改用程式碼呼叫工具；10-04 mcptoon 把 MCP 工具發現與 schema 的成本壓到最低。
> - **額度看得見**：10-03 Pulse 在 macOS 邊緣常駐，顯示 70 餘款 AI 工具的剩餘額度。

---

## 摘要

省 token 的做法分三路：少送（精簡輸出、清掉 AI 留下的註解、工具結果轉 Markdown）、晚送（工具改用程式碼呼叫，不把定義全塞進 context）、送便宜的（純 I/O 工作路由給便宜模型）。看見花費這一路，現有工具只顯示帳號額度與重置時間，還沒有一款給出每批並行 subagent 花了多少。多 agent 到底比較省還是比較貴，同一個問題有兩個相反答案，見 [[topics/community-tech-patterns]]「現在收斂到哪」。

模型路由這條方向怎麼走到今天見 [[topics/community-pattern-trends]] 趨勢四；企業規模的成本結構與因應見 [[topics/enterprise-cost-management]]。

---

## 目前結論

- **費用可觀測性從選配變必備**：2026-06 計費切割風波（該政策已於 2026-06-16 暫停）之後，帳單看得見成了工具的基本要求；工具清單見 [[topics/community-tech-tools]]。
- **並行成本歸因是缺口**：額度監控工具都有，「這一批 subagent 花了多少、做出了什麼」沒有人答得出來（見下方機制細節）。
- **你的選項：** 先量再省——用額度監控工具看清楚是哪一類工作在燒；再挑上面三路之一，路由給便宜模型的降幅目前最高，但只有單一團隊的數字。

**機制細節**
- **模型使用策略**：Dragoman / Workweave 自動路由，嵌入 Claude Code / Codex / Cursor 的成本感知路由；InstantVideos 將分工路由思路延伸至內容生成（文字/圖像/影音各交專門模型）
- **Token / 成本優化**：極簡輸出模式（穴居人）企業採用獲 404 Media 確認，OpenAI、Nvidia、GitHub 開發者使用；claude-thermos 以保活請求維持快取不過期，但引發「成本轉嫁其他用戶」爭議；pxpipe 反其道而行，把文字 context 渲染成圖片傳遞以降低 token 用量；`claude -p` 未加 `--bare` 冷啟動實測約耗 15 萬 token
- **並行用量與成本歸因（缺口）**：Pulse、Offrun、[Usage Updates](https://usageupdates.com/)（Show HN，10-01）只顯示帳號額度與重置，不給每批並行 subagent 的成本；r/ClaudeAI 10-03 [提問](https://www.reddit.com/r/ClaudeAI/comments/1wwlwys/how_do_you_track_cost_and_outcome_across_parallel/)庫內無解答；遞迴失控見 [#68619](https://github.com/anthropics/claude-code/issues/68619)

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 38 則節點，月份分組 2026-10 4 則、2026-09 12 則、2026-08 8 則、2026-07 14 則；懸置細節 Q-05 放在所屬月份分組末，技術彙整標題下帶原 L185 說明一行⟫
````

## 5. 子頁 D：`wiki/topics/community-skills.md`

````markdown
---
page: "topics/community-skills"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 2
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 1
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：Skills 怎麼寫

社群寫 Claude Code skill 的做法：怎麼寫才會被觸發、有哪些慣例和地雷、品質怎麼量。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-11
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **把創業流程封裝成 skill**：claude-skills-founder 從終端機產出產品簡報、競品分析、定價策略與募資 deck。
> - **平實語言寫的 skill**：10-02 open-steps 給 Claude Code、Codex、Cursor、Gemini CLI 共用。

---

## 摘要

官方的寫法規範在 [官方 skills 文件](https://code.claude.com/docs/en/skills)，什麼時候該把流程做成 skill、skill 和 hook 各管什麼，見 [[topics/coding-workflow-guide]]。本頁收社群實際寫出來的 skill 與踩到的坑；該裝哪些現成 skill 見 [[topics/community-tech-tools]]「Skills 速查」，官方 Skills 產品線見 [[entities/claude-skills]]。

## 慣例與地雷

**慣例（社群目前的寫法）**
- **description 就是觸發器**：session 啟動時只把 name 和 description 建成索引，SKILL.md 本體要等描述對上提示才載入——描述寫得籠統，skill 就永遠不會被叫起來。出處：〈Skill 不觸發的根因：session 啟動只索引 name+description，本體不預先載入〉（2026-08-04，見下方 2026-08）。
- **一個 skill 只做一件事**：單一職責的寫法自 2026-05 起沒有人再反對，見 [[topics/community-tech-discussions]]「現在吵到哪」表下。

**地雷（會靜默失效的地方）**
- **描述字數有預算**：單一 skill 的 description 加 when_to_use 上限 1,536 字元，整份清單的預算約為 context 的 1%；skill 裝多了，舊的會被悄悄擠出清單、不報錯。出處：〈Claude Code Skills 清單字元預算機制：description 超額會讓既有 skill 悄悄失效〉（2026-07-28，見下方 2026-07）。
- **公開 skill 多數觸發寫法不可靠**：一份對 216 個公開 skill 的靜態檢查，判 69% 的觸發條件寫法不可靠。出處：〈Show HN：Linting 216 個公開 Claude Code skills——69% 觸發條件寫法不可靠〉（2026-09-17，單一作者工具，見 [[topics/community-guardrails#2026-09]]）。
- **品質量得出來，但只有個案**：用 linter 掃一個高星 repo 的 24 個 skill 得 84/100，歸納出邊界不明、指令模糊等共通問題。出處：〈Skill Linter 對 52k-Star Repo 的 84/100 診斷案例：Skill 品質共通模式〉（2026-07-12，見下方 2026-07）。

證據強度：前兩條地雷各只有一位作者的第一手拆解或工具，沒有第二方重現；慣例第一條也是單一作者的機制說明。

---

## 目前結論

- **Skills 正從「指令封裝」變成「知識框架載體」**：單一職責的寫法已獲社群反覆驗證（[[topics/community-skills#2026-09]]）。**接下來看什麼：** 第三方 skill 的品質量測（可靠性測試那一類）會不會補上來。
- **你的選項：** 寫新 skill 前先把 description 寫成「什麼時候該叫我」的具體條件；skill 一多就檢查清單有沒有被擠掉；要硬擋的規則改用 hook。

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 42 則節點，月份分組 2026-10 2 則、2026-09 23 則、2026-08 10 則、2026-07 7 則⟫
````

## 6. 子頁 E：`wiki/topics/community-guardrails.md`

````markdown
---
page: "topics/community-guardrails"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-05"
status_main: "ongoing"
days_since_news: 4
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 4
inbound_links: 4
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 2
pending_overdue: 1
pending_next_review: "2026-10-20"
pending_signalled: 1
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：規則強制、審查與安全

社群讓 Claude Code 守規矩、讓產出有人審、防它亂來或洩漏密鑰的做法。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-02
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-05

> **最新做法**（2026-10-05）
> - **本機閘道管金鑰**：WaLiAPI 在本機統一三種 API 協議並內建安全審計；10-04 ThinkWatch-Lite 讓金鑰只留在閘道。
> - **專抓 AI 留下的技術債**：10-04 sloppy 對 PHP 做靜態分析，全程不碰 LLM。

---

## 摘要

社群的共識是強制勝過建議：CLAUDE.md 放偏好，要 100% 遵守的邊界交給 hook 或 CI 這類 agent 碰不到的一層。hook 怎麼擋才算擋（exit 2 才擋、exit 1 不擋）見 [[topics/community-pattern-trends]] 趨勢一與 [[topics/coding-workflow-guide]]，官方說明在 [官方 hooks 文件](https://code.claude.com/docs/en/hooks-guide)。多 agent 的產出誰來審，社群做法是唯讀審查者與跨模型交叉審查；官方的完成判定與攔截零件補到哪，見 [[topics/community-multi-agent]]「缺口追蹤」的「信任與驗證層」那一列。

---

## 目前結論

- **強制勝過建議**：規則寫進 CLAUDE.md 只是提醒，邊界要放在 hook、CI 或部署閘這類 agent 改不到的地方。
- **把關分兩型**：檢查型事後比對、不擋；強制型直接擋或回滾。檢查器若和 agent 同處一個環境，agent 可能動到檢查本身（見下方「把關層彙整」）。
- **審查有方向性**：跨模型互審不是對稱的，Claude 審 Codex 有效、反向反而變差（見下方「查證備註」）。
- **你的選項：** 先把「必須遵守」的規則從 CLAUDE.md 搬到 hook；多 agent 的產出至少配一個只能讀、不能改的審查者。

**機制細節**
- **Hooks 與自動化**：Stop Hook 要求可驗證完成證明；Pre-completion Hook 防模糊結束；hooks 可感知 agent 活躍狀態驅動環境副作用（螢幕喚醒、實體燈光顏色，見 Adrafinil、氛圍狀態燈）
- **安全架構**：Grepathy 偵測、追蹤 agent 自主做出但未經人工核准的決策行為；Spare Mac 隔離環境以備用實體裝置作為 agent 全權控制沙箱，降低主力工作機風險（`--dangerously-skip-permissions` 風險隔離）；OneCLI 在網路層攔截請求並代換真實憑證，agent 本身全程不接觸密鑰
  - **Skills 品質／合規稽核**：agent-scan 掃工具本身安全性；skillcrossroads 稽核 216 個公開 skill 的觸發條件，69% 寫法有問題，87 個 subagent 中 57% 未宣告 tools 清單，加計裸 Bash／萬用字元後 85% 不符最小權限（[[topics/community-guardrails#2026-09]]）

**查證備註**
- 「Claude 審查 Codex 通過率 71.6%→89.7%」已查得學術來源：[Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?](https://arxiv.org/abs/2607.21656)（arXiv 2607.21656）——116 則 LiveCodeBench 中／難題，六種條件對照，reviewer 只見題目與 writer 草稿、不能執行測試，近似真實 code review 流程；反向（Codex 審查 Claude）則使通過率從 91.4% 降至 82.8%，顯示審查方向有明顯不對稱效應，並非任一模型互審都有效（2026-08-13 查證）

**把關層彙整（2026-10-04）**

> 「它做完了、守規矩了嗎」目前有兩種把關：**檢查型**事後比對、不擋它；**強制型**由 agent 碰不到的一層直接擋或回滾。社群這一週的例子各有破口。

| 工具／事件 | 類型 | 怎麼把關 | 已知破口 |
|---|---|---|---|
| RuleReceipt（09-30） | 檢查型 | 比對 agent 有沒有守 CLAUDE.md／AGENTS.md | 討論串有人質疑 agent 能關掉檢查 hook；趕工時最常繞過規則；無使用回報 |
| Perspica（09-30） | 檢查型（輔助人審） | 審閱大型 AI PR 的語意化 diff，可選不靠 LLM 的機械分組 | 只幫人讀、不攔合併（推論）；LLM 分組模式仍靠模型判斷；無使用回報 |
| 自主 agent 部署閘（10-01） | 強制型 | 預檢契約、帶硬門檻的 canary、agent 無法推翻的自動回滾 | 作者自述 340 餘次部署、零人工呼叫，無 repo 或指標可複核；閘是事故後才加 |
| 刪除 48,000 檔事件（09-25，TechRadar） | 強制型缺位的個案 | 報導未提任何攔截層 | 僅標題可用、單一媒體；備份、指令與版本均未見報導，不當作定論 |

- **檢查型的共同破口**：被檢查的 agent 與檢查器同處一個環境時，agent 可能動到檢查本身；強制型把關住在 agent 碰不到的地方，這是兩型的分界（推論）。
- **兩型都沒回答的是品質**：Ask HN〈Is anybody producing good code with coding agents?〉（HN 26 分，10-02）轉述資深工程師抱怨 AI 程式碼難讀、品質差；守規則與能安全出貨，不等於寫得好。
- 來源：[RuleReceipt](https://github.com/rulereceipt/rulereceipt)、[Perspica](https://github.com/sshah03/perspica)（Show HN，日報 2026-10-01）；[部署閘](https://dev.to/yureki_lab/how-i-built-a-deploy-gate-so-my-autonomous-coding-agent-can-ship-to-prod-safely-1egb)；[Ask HN](https://news.ycombinator.com/item?id=49934037)；[TechRadar 報導](https://news.google.com/rss/articles/CBMiqAJBVV95cUxNQVVjM0pQRFpzektxX3NLM1ZqSERGMEljWW5pYWJ2c1hnTUZMTmZCVnRRdGtkRlpCQjlEQTR5bnd6MTRudlA3dWVubjZISzBGZng5eVg5NlBjcTdVRHdobXB5bDlfb1BncldYc2lUWVUzY0s2RkFZZmxpdFN2ZlNBU2huNzRIYUtEUGszYldjMksyS3ZXd0dwdFh2b1I3ZEQ2cFVuXzFKRVhlWGNUVC1ISkhvazJOYTZ0emtJR3FKUzBGR1JlMHdSekowekRDSzRZTmhGalZyWHZsdlVvQ1dHQVdWQ3lhWV9VakVFWUM2YkFDdUw0cXZUUEd2dmVSYnlldTAxeVVULUd0NjdqMTVXd2J5NUV3RjNYRHVmZjdFaWJRTHNPU2V0Mw?oc=5)（日報 2026-09-25；庫內條目見 [[topics/ai-agent-safety]]）；RuleReceipt 工具選型見 [[topics/community-tech-tools]]。

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 32 則節點，月份分組 2026-10 4 則、2026-09 11 則、2026-08 9 則、2026-07 8 則；懸置細節 Q-01、Q-03、Q-04 放在所屬月份分組末，技術彙整標題下帶原 L185 說明一行⟫
````

## 7. 子頁 F1：`wiki/topics/community-integrations.md`

````markdown
---
page: "topics/community-integrations"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 2
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 1
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-20"
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：MCP、plugin 與外部工具整合

社群把 Claude Code 接上外部服務、工具與創作軟體的做法，以及 MCP 長時間連線怎麼不斷。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-15
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **國產模型補連網、求職流程 MCP 化**：huashu-doubao-search 用豆包搜索補連網能力；swissdevjobs-cli 讓 agent 搜尋並應徵瑞士等 7 國的職缺。
> - **接上實體機器人**：ros-mcp-server（1,488★）透過 MCP 串接 ROS，目前只有這一個實作。

---

## 摘要

這是十月新做法最多的一群：每週都有新的 MCP server 或 plugin 進來，多數是單一作者工具（推論），還沒有人篩過哪個值得裝——該裝哪個看 [[topics/community-tech-tools]]。共同的設計原則是避免不必要的 context 載入；MCP 長時間連線的三種失效（連線中斷、工具逾時、上下文失憶）對應心跳、重試、快照三種防護。官方怎麼裝 plugin、怎麼接 MCP，見 [官方 plugins 文件](https://code.claude.com/docs/en/plugins/overview) 與 [官方 MCP 文件](https://code.claude.com/docs/en/mcp)；官方新出的 plugin 與 MCP 功能見 [[feature-radar]]。

---

## 目前結論

- **整合面一直往外擴**：從程式碼工具鏈擴到創作工具（影片、遊戲引擎、ComfyUI），十月起也接上實體機器人。
- **MCP 長 session 穩健化**：最後一則做法停在 2026-08-14，心跳、重試、快照三種防護還沒有新的實測。
- **你的選項：** 先查 tools 頁有沒有對應症狀的首選；裝單一作者的 MCP server 前，先確認它會載入多少工具定義進 context。

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 38 則節點，月份分組 2026-10 15 則、2026-09 15 則、2026-08 2 則、2026-07 6 則；懸置細節 Q-02 放在所屬月份分組末，技術彙整標題下帶原 L185 說明一行⟫
````

## 8. 子頁 F2：`wiki/topics/community-interfaces.md`

````markdown
---
page: "topics/community-interfaces"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 2
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：手機遠端、介面與 agent 可視化

社群從手機控制 Claude Code、換一個更好的終端機或介面、把 agent 正在做什麼畫出來的做法。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-08
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **先畫依賴地圖再開工**：mellos-mapping 先畫分層藍圖，建置時逐一點亮，目前只有這一個實作。
> - **圍繞 hooks 打造的終端機**：10-06 ClaudeTerm 用 hooks 與 statusLine 做出 Windows 終端機；10-04 Mobile-Harness 是免 root 的 Android 版行動端 IDE。

---

## 摘要

從手機控制這件事，先試官方：Claude Desktop 已可遠端控制 Claude Code session，怎麼開見 [[entities/claude-code]]。社群的實作走 bot、MCP、web-app 三條路，各選各的傳輸層，沒有和官方逐項比較過；這條方向怎麼走到今天見 [[topics/community-pattern-trends]] 趨勢八。介面元件多是把終端機或狀態列包裝得更好用；可視化目前只有把工具呼叫畫成遊戲化辦公室的兩個實作，多 agent 看板與儀表板見 [[topics/community-pattern-trends]] 趨勢六。

---

## 目前結論

- **手機遠端**：官方已可遠端控制；社群五個以上實作各走一路，還沒有收斂。**接下來看什麼：** 有沒有人比較官方與社群做法在離線、通知、多 session 上的差別。
- **介面與可視化**：各自單一實作居多，還在試。
- **你的選項：** 要從手機看進度先開官方遠端控制；要多 agent 總覽看 tools 頁「一堆 agent 在跑，看不到誰卡住」那一列。

---

## 技術彙整

⟪由 split_patterns.py 填入：本群 22 則節點，月份分組 2026-10 7 則、2026-09 9 則、2026-08 1 則、2026-07 5 則⟫
````

---

# 進規則檔

改前先照 `.claude/rules/claude-md-edit.md` 跑兩個反向查詢（`.claude/` 與 `scripts/ web_reader/assets/ src/tests/`）；下列句子裡的子頁一律寫完整路徑或 `topics/<slug>`，不寫裸檔名（`check_rules.py` 的裸露引用只登記了 `community-tech-patterns.md`）。行號指現檔。

## A. `.claude/reporter-rules/community/pages.md`

**A1. L21（節首導言）整句換成：**

> 母頁回答「社群拿 Claude Code 玩出哪些做法、哪些已經站住腳、哪些還在試」，是 patterns 這棵樹的入口：結論層是母頁的 `## 模式概覽`、`## 每一類做法住哪一頁`（子頁路由表）與 `## 現在收斂到哪、哪些還在試`；逐則節點住七個子頁的 `## 技術彙整`（每日 prepend，不受本節拘束）。學術對照、誰負責拆分、缺口追蹤三張表住 `topics/community-multi-agent`（第 2–4 條）。**第 2–4 條的欄位規定取代原「multi-agent orchestration 學術對照維護」節；該節的「屬非新聞性更新，只動最後更新、不動最後新聞更新」與「論文查證屬主編、記者無 web 工具不得自行補文獻」兩條紀律繼續適用。**

**A2. L22 與 L23 之間插入新條「### 0.」：**

> ### 0. patterns 樹的路由表（寫節點前先查）
>
> | 子頁 | 收哪幾類（節點「與既有模式的關係」行裡第一個逐字寫出的類別名） |
> |---|---|
> | `topics/community-multi-agent` | Multi-agent 架構、Agent 規模化、Agent Loop 終止條件、確定性 Agent 框架 |
> | `topics/community-memory` | 記憶與知識管理、CLAUDE.md 管理、Context 管理、Agent 記憶保護、跨環境 Agent 記憶 |
> | `topics/community-cost` | Token / 成本優化、模型使用策略、Agent 預算控制 |
> | `topics/community-skills` | Skills 設計、可靠性測試 |
> | `topics/community-guardrails` | Hooks 與自動化、安全架構、多代理 PR Review、規格驅動開發、架構邊界合約、Agent 版本控制 |
> | `topics/community-integrations` | Plugin / MCP 整合、MCP 長 Session 穩健化、創意工具 Agent 整合 |
> | `topics/community-interfaces` | 介面元件複用、行動裝置遠端控制、Agent 活動可視化、跨 Repo 依賴可視化 |
>
> - 關係行沒有逐字寫出任何類別名：依它補的是哪一種做法判最近的子頁（額度監控、帳號橋接、看見實際送出的內容→`topics/community-cost`；課程與合輯→`topics/community-skills`）；判不出就寫進母頁 `## 技術彙整` 的 `### 未歸類`，週更時分派。不設預設子頁（`.claude/reporter-rules/page-lifecycle.md`「路由」條）。
> - 一則節點只住一頁；別頁要提它就寫 `[[topics/<子頁>#YYYY-MM]]`。
> - 新類別入 `## 模式概覽` 的同一輪加進本表某一列；某一群自己長出第二個故事、子故事三題答得齊，才開新子頁，屬裁決事項。

**A3. L29「最後動態」定義：**
- 「`## 技術彙整` 中，」→「母頁與七個子頁的 `## 技術彙整` 中，」
- 「先 `Grep "\*\*與既有模式的關係：\*\*" wiki/topics/community-tech-patterns.md`，」→「先對第 5 條指令列的八個檔 `Grep "\*\*與既有模式的關係：\*\*"`，」
- 「（技術彙整新條目在上、月份新到舊，即行號最小者）」→「（同日多則取第 0 條路由表順序在前的子頁；同一頁內取行號最小者）」

**A4. L30 換成：**

> - **「代表技巧」欄末必附錨點，指「最後動態」那一則所在的子頁月份，一律寫全頁形式** `[[topics/<子頁 slug>#YYYY-MM]]`（例：`[[topics/community-skills#2026-10]]`）。**不可寫同頁簡寫 `[[#YYYY-MM]]`**——`scripts/build_web.py` 的 `ANCHORED_WIKILINK_RE`（L329）要求 `#` 前至少一個字元，同頁簡寫不會被 `check_wikilink_anchors()` 檢查到，等於沒有看守。

（原句的 L276 已漂到 L329，順手更正。）

**A5. L38、L42、L46 三個標題的「community-tech-patterns 的」→「community-multi-agent 的」**（`scripts/table_census.py` 的 `_mechanism()` L71–75 要求命中行或所屬標題含該頁 slug 基名）。

**A6. L57 指令換成（副本實測：拆前舊指令 239／62、拆後舊指令 0／0、拆後新指令 239／62）：**

```
python -c "import io,re;fs=['wiki/topics/community-tech-patterns.md']+['wiki/topics/community-'+s+'.md' for s in ('multi-agent','memory','cost','skills','guardrails','integrations','interfaces')];a=[x for f in fs for x in re.findall(r'\*\*主線：\*\*\s*(\S)',io.open(f,encoding='utf-8').read())];print(len(a),'則節點，已填',sum(1 for x in a if x!='—'))"
```

L60「而週更整線重寫只撈填了非 `—` 的那 11 則」→「而週更整線重寫只撈填了非 `—` 的節點」（同段寫死的 11 違反本條自己的「分母不得寫死」，實測已是 62）。

**A7. L64 句末加：**「子頁增減或改名也算鉤子失效。」

**A8. L68 句末加：**「patterns 樹的短標記與它的細節區必須住同一個子頁（`scripts/check_pending_markers.py` 檢查 6 逐頁對帳，L186）。」

**A9. L72 整條換成：**

> 照 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」。**patterns 樹（母頁＋七個子頁）共用一個 archive：`topics/community-tech-patterns-archive`，掛母頁下**——archive 按月封存，與分群無關，不每個子頁各開一個。對象為七個子頁 `## 技術彙整` 的 `### YYYY-MM` 分組：同一個月份七個子頁一起蒸，原文都 append 進 archive 同一個 `## YYYY-MM`；各子頁該月份改成 ≤15 行時段總結，末行 `原始條目見 [[topics/community-tech-patterns-archive#YYYY-MM]]`；母頁 `### YYYY-MM` 分住段同批改成指 archive 的一行。**2026-05／06 已封存，2026-07 於 2026-10 起達 3 個月門檻**——搬走之前先做兩件事：(a) `## 模式概覽` 與表下段指向任一子頁 `#2026-07` 的錨點同批改指 archive；(b) 母頁 `## 摘要` 那句官方 context engineering 指路（現指 `topics/community-memory#2026-07`）同批改指 archive 對應錨點，本樹唯一的官方一手引用不能失去入口。

**A10. L76「（patterns / discussions 兩頁的 `## 技術彙整` 皆適用）」→「（patterns 七個子頁與 discussions 的 `## 技術彙整` 皆適用；patterns 母頁的 `## 技術彙整` 只有 `### 未歸類` 與早期時段總結）」；L93 句末加：「patterns 樹寫進第 0 條路由表指定的子頁，不寫母頁。」**

**A11. L99「新增工具至 `community-tech-patterns.md` 時」→「新增節點至 patterns 子頁時」。**

**A12. L99 之後加新條「### 11. community-skills 的 `## 慣例與地雷`」：**

> 兩組條列（慣例／地雷），各 ≤5 條，每條一句機制＋「出處：〈節點標題〉（日期，見哪個月份或哪個子頁）」，最後一行寫證據強度。入口只有一種：Skills 設計或可靠性測試出現**新的觸發機制或靜默失效條件**；同類工具再多一個不加條。滿 5 條時換掉證據最弱的一條。只能引本樹既有節點或已查證的官方文件，不寫社群轉述的通則。週更時與第 1 條同批複查。

## B. `.claude/reporter-rules/community/weekly.md`

- **L3**：「`community-tech-patterns.md` 模式淘汰審查」→「patterns 樹（`community-tech-patterns.md` 母頁＋七個子頁，路由見 `.claude/reporter-rules/community/pages.md` 第 0 條）模式概覽週更與結論層重寫」。
- **L54**：「每次 `/wiki-lint` 對 `## 模式概覽` 執行三步」→「每次 `/wiki-lint` 對母頁 `## 模式概覽` 與各子頁結論層執行四步」。
- **L56 第 1 步**：「先撈全頁 `**與既有模式的關係：**` 行」→「先撈母頁與七個子頁的 `**與既有模式的關係：**` 行（八個檔，指令同 pages.md 第 5 條的檔案清單）」；「覆寫日期欄與全頁式錨點」→「覆寫日期欄與錨點（指那一則所在子頁的 `#YYYY-MM`）」。
- **L58 之後加第 4 步：**

> 4. **結論層重寫（page-lifecycle 母頁契約的週更觸發邊）**：本週有新節點的子頁，重寫它的 `## 目前結論`（≤5 條，覆寫不 append，最後一條是「你的選項」或「接下來看什麼」）與頂部導言的結論句；再重寫母頁 `## 現在收斂到哪、哪些還在試` 該群那一句（只寫結論變了沒並指子頁，不抄子頁數字）、`## 摘要` 第二段的計數句（定案幾類、還在試幾類、YYYY-MM-DD 起有新動靜幾類，寫絕對日期），並重算路由表「最後動態」欄；`### 未歸類` 有節點就照 pages.md 第 0 條分派到子頁。沒有新節點的子頁不動。

- **L65 回報格式加一行**：`結論層重寫：子頁 N 頁（slug）／母頁收斂句 N 句／未歸類分派 K 則`。
- **L83**：「`Grep "\*\*主線：\*\* [^—]" wiki/topics/community-tech-patterns.md`」→「對 pages.md 第 5 條指令列的八個檔 `Grep "\*\*主線：\*\* [^—]"`」；「若已不在 patterns 本體（月度封存搬走）」→「若已不在 patterns 母頁或子頁（月度封存搬走）」。
- **L105**：「（patterns 本體、archive 或 trends）」→「（patterns 子頁、archive 或 trends）」。
- **L121**：整句換成「**archive 頁：** patterns 樹（母頁＋七個子頁）共用 `topics/community-tech-patterns-archive`（掛母頁下，規格見 pages.md 第 8 條）；discussions 用 `topics/community-tech-discussions-archive`。時段單位是技術彙整的 `### YYYY-MM` 月份分組，條目為其下 `####`。」
- **L135**：「每種做法的證據與採用成熟度（✅⚡⏳）住 `community-tech-patterns`」→「每種做法的採用成熟度（✅⚡⏳）住 patterns 母頁的模式概覽表、逐則證據住七個子頁」。
- **L158**：「`Grep "\*\*與既有模式的關係：\*\*" wiki/topics/community-tech-patterns.md`」→「對 pages.md 第 5 條指令列的八個檔 `Grep "\*\*與既有模式的關係：\*\*"`」。
- L67（分母 M）不改字：它指向 pages.md 第 5 條，那條指令已在 A6 改掃八檔。

## C. `.claude/reporter-rules/community/daily.md`

- **L13 負責頁面列換成：**

> | `wiki/topics/community-tech-patterns.md`（母頁）＋七個子頁 | 工作流模式、multi-agent 設計、最佳實踐。**節點寫進子頁**：依節點「與既有模式的關係」第一個寫出的類別，查 `.claude/reporter-rules/community/pages.md`「topics/community-tech-patterns」第 0 條路由表；判不出寫母頁 `### 未歸類`。寫了節點的子頁覆寫它的 callout（括號日期＝TARGET_DATE），母頁 callout 同批覆寫成當天各子頁新做法的一句總覽並連子頁——母頁 callout 日期落後子頁「最後新聞更新」，`scripts/check_hierarchy.py`（L137）會紅。母頁其餘只准動路由表「最後動態」欄與既有懸置標記加 `訊`，「最後新聞更新」不動（page-lifecycle 母頁契約） |

- **L27**：「（patterns 頁新增條目）」→「（patterns 子頁新增節點）」。
- **L31**：「（歸 `community-tech-patterns.md`）」→「（歸 patterns 子頁，路由見 pages.md 第 0 條）」。
- **L65**：「每次為 `community-tech-patterns.md` 新增節點時」→「每次為 patterns 子頁新增節點時」（registry `sync_pairs[39]` 要的兩個 pattern 仍在本檔）。

## D. 其他規則檔

- `.claude/skills/wiki-lint-sweeps/references/sweeps.md` **L261**：「`wiki/topics/community-tech-patterns.md` 的 `## 模式概覽`（上限 21 列）、`### 誰負責拆分`（五列固定）與 `### 缺口追蹤`（上限 8 列）」→「`wiki/topics/community-tech-patterns.md` 的 `## 模式概覽`（上限 21 列）與 `wiki/topics/community-multi-agent.md` 的 `### 誰負責拆分`（五列固定）、`### 缺口追蹤`（上限 8 列）」；**L263**「派社群記者執行該節三步」→「四步」，句末補「；第 4 步重寫子頁與母頁的結論層」。
- `.claude/reporter-rules/devpractice/pages.md` **L30**、**L31**：「`community-tech-patterns` 新節點」／「`community-tech-patterns` 有對應證據」→「patterns 樹（`community-tech-patterns` 母頁與七個子頁）新節點」／「patterns 樹有對應證據」。
- `.claude/skills/wiki-ingest/references/classification.md` **L67**：「`topics/community-tech-patterns`，出處標明官方」→「`topics/community-tech-patterns` 樹（節點依 `.claude/reporter-rules/community/pages.md` 第 0 條路由表寫進子頁），出處標明官方」。
- `.claude/review-registry.json`：**不需改**——`anchors` 沒有登記本頁節名；`sync_pairs[39]` 的兩個 pattern 改後仍在 daily／weekly；`bare_name_search_dirs` 只需既有的 `community-tech-patterns.md`（新子頁一律寫路徑）。
- `.claude/reporter-rules/shared.md` L33「典型大型頁面」清單、`data/reader-tags.json`：不改（子頁從母頁下鑽，不入標籤；page-lifecycle L43）。

## E. 資料檔（`data/`）

- `data/reader-language-allow.json`：`line_contains` 為 `shadcn-ui/lint` 的那筆 `page` 改 `topics/community-guardrails`；`個人化覆寫` 那筆改 `topics/community-memory`（副本：不改＝3 筆新增 FAIL，改後 0）。`非預期覆寫` 那筆指母頁、母頁早已無此句，不動。
- `data/cell-limit-baseline.json`：八頁落地後跑 `python scripts/check_cell_limits.py --rebuild --allow-grow --reason "第 18 波 patterns 拆頁：母頁 66 筆存量隨節點原文搬到 7 子頁（錨點與長度不變）"`。副本輸出「新增 66」、帳本 `added` 66 筆全在七子頁（guardrails 15／memory 14／multi-agent 13／skills 11／cost 7／integrations 3／interfaces 3）、`removed` 含母頁 66。新增若不是恰 66 或出現七子頁以外的頁，停下回報——那是別的 session 的改動被吸進基線。
- `data/pending-marker-count.json`：不 rebuild（見 proposal §8）。

## F. `scripts/check_wiki_freshness.py` 修法（L179–193 換掉；L194–197 原樣保留在新 `if` 底下）

```python
    parent_of = {k: p for p, ks in children.items() for k in ks}

    def ancestor_att(slug: str) -> str:
        best, cur, guard = "", parent_of.get(slug), 0
        while cur and guard < 50:
            best = max(best, last_att.get(cur, ""))
            cur, guard = parent_of.get(cur), guard + 1
        return best

    for slug, last_news in scan_pages():
        if last_news is None:
            missing_field.append(slug)
            continue

        own = last_att.get(slug)
        # 1. 漏更：只比「自己」的歸因。母頁「最後新聞更新」不因子頁動（page-lifecycle 母頁契約）；
        #    拿子樹歸因來比，子頁一進新聞母頁就紅，逼人去動母頁不該動的欄位
        if own and last_news < own:
            stale_updates.append(
                f"{slug}：頁面宣稱 {last_news}，但 {own} 日報有條目落地此頁"
            )
        # 2. 無從對照：自己、子樹、上層三處都找不到撐得住這個日期的歸因。
        #    子樹＝母頁的新聞落在子頁；上層＝拆頁時節點從母頁搬下來，拆出前的歸因記在母頁
        #    （帳本 append-only，不改寫舊行的 page）——只認「宣稱日不晚於上層最後一筆歸因」
        cover = own or (subtree_att(slug) if slug in children else "")
        if not cover:
            anc = ancestor_att(slug)
            if anc and last_news <= anc:
                cover = anc
        if cover:
            continue
        if last_news >= max(recent_cutoff, ATTRIBUTION_START) and slug not in DERIVED_PAGES:
```

- 檔頭 docstring 第 2 類說明句末加：「有上層的頁，宣稱日不晚於上層最後一筆歸因也算有對照（拆頁搬下來的節點，歸因記在上層）。」L160–161 註解「第 2 類對母頁改看子樹歸因」後加「；第 1 類只看自己」。
- 新增測試 `src/tests/test_wiki_freshness_hierarchy.py`：逐字取自 `scratchpad\w18\patch\test_wiki_freshness_hierarchy.py`（四案；現版 2 FAIL、修後 4 OK，已實跑）。
- 已驗：套用後現行全庫（未拆）`2026-10-09`、`2026-10-15` 兩天結果與修前相同（exit 0）。

## G. 轉知帳本（`python scripts/pending_handoffs.py open`；先 `--dry-run`，再去掉跑一次）

```
python scripts/pending_handoffs.py open --from 社群 --to 開發實務 --page topics/coding-workflow-guide --note "L478 錨點 [[topics/community-tech-patterns#2026-07]]（本地合併佇列）改指 [[topics/community-multi-agent#2026-07]]：patterns 第 18 波拆成七個子頁，那一則住多 agent 子頁；母頁 ### 2026-07 是過渡錨點，改完回報即可刪"
python scripts/pending_handoffs.py open --from 社群 --to 功能 --page topics/official-community-gap --note "L41 錨點 [[topics/community-tech-patterns#缺口追蹤：文獻主張 × Claude Code 現況]] 改指 [[topics/community-multi-agent#缺口追蹤：文獻主張 × Claude Code 現況]]：缺口表隨 patterns 第 18 波拆頁搬到多 agent 子頁；母頁同名 h3 是過渡指路，改完回報即可刪"
python scripts/pending_handoffs.py open --from 社群 --to 功能 --page entities/claude-skills --note "L116 改指 [[topics/community-skills]]「慣例與地雷」（patterns 第 18 波拆出 Skills 子頁）；同句「74 個 skill 只有 3 個真正改變行為」在 patterns 母頁、七個子頁與 archive 皆查無此筆，請查出處或刪；另 L45「尚未提供正式…市集」與 L97「已有官方市集」互斥（第 18 波冷讀者撐不起 #1、#2）"
```

`wiki/log.md` 的 Query 條目寫到這三筆時帶單號（`scripts/check_log_handoffs.py` 只放行帶 `H-xxxxxx` 的「轉知」行）。

## H. 實作者跑閘的順序（我只在 `scratchpad\w18\tmprepo` 副本跑過，結果在 `final_validate.log`）

1. 跑 `split_patterns.py` 後把 `out\` 八頁複製進 `wiki/topics/`（母頁覆蓋、七子頁新增），改 discussions 三處、LCW 五處、index 三處（逐字見 proposal §7 與 map 第三節）。
2. 改 `scripts/check_wiki_freshness.py`（§F）並加測試；改規則檔 A–D；改 `data/reader-language-allow.json` 兩筆（§E）。
3. `python scripts/gen_wiki_frontmatter.py`（全庫寫入；只 `git add` 本波八頁、index、鄰居兩頁，其餘頁的 frontmatter 漂移不收）。
4. `python scripts/check_cell_limits.py --rebuild --allow-grow --reason "…"`（§E），核對新增恰 66。
5. 逐支：`check_hierarchy.py`、`check_pending_markers.py`（預期「152 筆／其中 3 筆尚未入基線」類訊息，不 rebuild）、`check_wiki_freshness.py`、`check_reader_language.py`、`check_cell_limits.py`、`check_rules.py`、`build_web.py`（尾行錨點 WARN 與改前同數）；最後 `run_tests.py` exit 0。
6. 主 session：commit 後 `python scripts/devpractice_diff.py mark`（搬家 diff 不得被當新料，page-lifecycle L69）、§G 三筆轉知、`wiki/log.md` Query 條目、ledger 定稿列；同一個 commit push。

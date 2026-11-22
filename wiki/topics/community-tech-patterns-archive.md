---
page: "topics/community-tech-patterns-archive"
kind: "topic"
status: "resolved（封存頁）"
domain: "🌐 社群"
last_updated: "2026-11-22"
last_news_update: "2026-06-30"
status_main: "resolved"
days_since_news: 145
parent: "topics/community-tech-patterns"
children: "['topics/community-tech-timeline']"
page_role: "archive"
days_since_news_subtree: 145
inbound_links: 23
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 5
pending_overdue: 0
pending_next_review: "2026-11-24"
pending_signalled: 1
staleness_exempt: null
signal: "⚠️ 高引用但停滯"
generated_by: "scripts/gen_wiki_frontmatter.py"
---

# 社群實戰做法——早期原始條目

**狀態：** resolved（封存頁）
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-04-25
**最後更新：** 2026-11-22
**最後新聞更新：** 2026-06-30

> 本頁保存 [[topics/community-tech-patterns]] 被搬離主頁的原始條目，以及 2026-04-25～05-22 的社群時序流水帳（舊時序頁 [[topics/community-tech-timeline]] 已併回此處）。條目一字不刪，只是搬離主頁讓主頁讀得動。

---

## 2026-08

### community-cost（成本與用量）

#### x1xhlol/system-prompts-and-models-of-ai-tools：彙整數十款 AI 編碼工具完整系統提示詞與模型設定（2026-08-29）

- **主線：** —
- **核心模式：** 彙整 Claude Code、Cursor、Devin AI、Replit 等數十款 AI 編碼工具的完整系統提示詞與模型設定；GitHub Search 累積 14.3 萬星
- **與既有模式的關係：** 呼應「system prompt 版本追蹤」類別——phistory（08-08）鎖定四款 CLI 的版本快照自動保存；本則規模更大（涵蓋數十款工具，含非 CLI 類）且為靜態彙整檔案庫非自動追蹤，供橫向比較不同廠商設計取向
- **可信度註記：** 星數（14.3 萬），僅取得 GitHub Search 星數，api.github.com 存取受限、無 forks／issues／近期 commit 佐證可查，未另行查證；因屬本庫首次收錄的既有大型 repo（已成名但本庫從未報導過的 repo），依內容具體程度（涵蓋範圍明確、可查證的公開 system prompt 文字）判斷收錄，星數本身不作為獨立驗證訊號
- **來源：** GitHub Search（14.3 萬★，存量盤點｜2025-03-05 出生、本庫今日首次收錄）；[GitHub](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- **成熟度：** ✅ 廣泛採用（14.3 萬星且已存在近 1.5 年，屬長期累積型參考資源而非新興工具）

#### Show HN：Frugal Tokens——檢視跨 coding agent 用量與成本的自製工具（2026-08-19）

- **主線：** —
- **核心模式：** 作者釋出自製工具 Frugal Tokens，用於檢視自己各 coding agent session 的花費、cache miss 對成本的影響，提供依模型與快取狀態拆解的用量分析，並可逐一 session 檢視呼叫細節
- **與既有模式的關係：** 呼應本頁「Token / 成本優化」類別既有多筆針對成本可視化與快取行為的工具（如 pxpipe、claude-thermos），本則補上跨 agent（非僅 Claude Code 單一工具）的成本／快取拆解視角；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Show HN: Frugal Tokens – explore costs and usage across coding agents」— Hacker News（score 33）＋跨 2 來源；[demo.frugaltokens.com](https://demo.frugaltokens.com/)
- **成熟度：** ⏳ 新興（今日首見，個人自製工具，尚無社群採用回饋）

#### Show HN：Graft — Claude Code hooks 削減 grep 輸出 token，宣稱降幅 42%，惟 benchmark 段落遭質疑 AI 代寫（2026-08-15）

- **主線：** Context 管理
- **核心模式：** 開源專案 Graft 提供一組 Claude Code hooks，攔截並精簡 grep 搜尋產生的輸出內容，宣稱可將相關 token 用量削減 42%
- **與既有模式的關係：** 呼應本頁「Token / 成本優化」類別既有多筆針對特定工具輸出裁剪的做法（CCN 只清 AI 遺留註解、pxpipe 圖片化 context 等），本篇補上 grep 輸出這個此前未被記錄過的裁剪對象；與 [[topics/community-large-codebase-workflow]] Context / Token 管理主線相關——grep 是大型 repo 搜尋的高頻高輸出來源
- **可信度疑慮：** HN 討論串有留言指出 README 的 benchmark 段落「看起來像 Claude/Codex 代寫」，難以判斷 42% 宣稱是否成立，本頁不將此數字視為已驗證
- **來源：** 「Show HN: Graft – Claude Code hooks that cut grep tokens by 42%」— Hacker News（score 39）＋跨 2 來源；[GitHub](https://github.com/NanoNets/Graft)
- **成熟度：** ⏳ 新興（單一開源專案，宣稱數字未經第三方驗證，社群對 benchmark 真實性有疑慮）

#### Simon Willison 轉介：以「假設性分類」（hallucinate classification）取代傳統分類流程的做法（2026-08-14）

- **主線：** —
- **核心模式：** Simon Willison 部落格轉介 softwaredoug 的文章，主張部分分類任務與其建置傳統分類器／embedding pipeline，不如直接讓 LLM「假設性」生成分類結果（hallucinate a classification）後再視需要校正，作為更輕量的替代做法
- **與既有模式的關係：** 呼應本頁「Token / 成本優化」「Skills 設計」等類別既有「用更少工程換取可用結果」的取向，補上分類任務這個尚未見於既有節點的應用場景；性質偏概念性主張，非附帶量化驗證的第一手實作，非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Don't classify. Hallucinate!」— Simon Willison Blog（Blogroll 策展名單，具名知名開發者轉介，收錄即算）；[原文](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/)
- **成熟度：** ⏳ 新興（概念性主張，尚無量化驗證或社群跟進採用案例）

#### phistory：跨 agent CLI（Claude Code／Codex／OpenClaw／Hermes）system prompt 版本快照自動保存工具（2026-08-08）

- **主線：** —
- **核心模式：** 開源工具 Phistory 自動追蹤並保存多款 agent CLI（Claude Code、Codex、OpenClaw、Hermes）的 system prompt 版本快照，讓使用者可跨版本比對各工具 system prompt 的變動歷程，而非侷限於單一工具的單次檢視
- **與既有模式的關係：** 呼應本頁既有「作者 grep JSONL 逐字稿，發現隱藏標籤 `<ip_reminder>`」（07-29）等第一手偵測方法論，本工具系統化為跨工具、跨版本的自動保存與比對機制；屬單一工具除錯輔助，非大型 codebase 協作痛點，暫不歸入主線
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）；repo 為 [WEIFENG2333/phistory](https://github.com/WEIFENG2333/phistory)，星數已查證（2026-08-13，GitHub API）：519 星／forks 35（6.7%，略低於防刷基準）／open issues 4／最後 push 08-12——forks 比例偏低但有近期實質 commit 與少量 issue 往來，刷星可能性無法完全排除
- **成熟度：** ⏳ 新興（星數佐證較弱，尚無第一手使用心得或社群討論佐證實際採用效果）

#### headless Claude Code（`claude -p`）冷啟動實測：未加 `--bare` 約載入 15 萬 token（2026-08-07）

- **主線：** Context 管理
- **核心模式：** 作者實測 headless 模式（`claude -p`）在未加 `--bare` 旗標時，冷啟動會預先載入約 15 萬 token 的系統提示、工具定義與預設 context，構成每次呼叫的固定成本；加上 `--bare` 可跳過這些非必要載入，文章給出「何時該用 `--bare`」的具體判準，適合 CI pipeline、批次任務等大量 headless 呼叫場景
- **與既有模式的關係：** 補充「Token / 成本優化」類別，聚焦「headless / 非互動呼叫」這個此前未被記錄過的固定成本來源，與 05-07「MCP Code Execution Token 效率」、06-21「MCP Server 信任邊界審查」（9 個 server = 每輪 38k tokens 冷啟動）同屬「摸清楚 Claude Code 各種呼叫模式底層固定成本」系列量化實測，這次對象是 headless 呼叫本身而非 MCP 配置；也與 [[topics/community-large-codebase-workflow]] Context / Token 管理主線相關，大量 headless 呼叫常見於多 agent pipeline 場景
- **來源：** 「[claude -p: what headless Claude Code actually loads (and when --bare is the right call)](https://dev.to/rulestack/claude-p-what-headless-claude-code-actually-loads-and-when-bare-is-the-right-call-182c)」— dev.to（1 讚；依規則以第一手實測內容判斷，非讚數）；token 數已查證（2026-08-13）：作者原文明確報告冷啟動約 150,000 token（未執行任何工作前），成因為 `-p` 預設載入完整互動 session context（hooks、skills、plugins、MCP servers、auto memory、所有 CLAUDE.md 載入鏈），文中未標明測試的 Claude Code 版本號
- **成熟度：** ⏳ 新興（今日首見，單一作者實測，尚無其他來源複現驗證）

#### pxpipe：把文字 context 轉成圖片以降低 Claude Code token 用量（2026-08-05）

- **主線：** Context 管理
- **核心模式：** 將原本以文字形式送入的 context 改以圖片渲染後傳遞，藉此降低 Claude Code 的 token 用量——與本頁既有「HTML→Markdown 降 80% token」等既有做法方向相反（既有做法把非文字格式轉為更精簡文字，此作法反其道而行改用圖片承載資訊）
- **與既有模式的關係：** 為「Token / 成本優化」類別補上一個尚未出現過的技巧方向；降耗比例與機制已查證（2026-08-13）：以本機 proxy 攔截 system prompt／工具定義／對話歷史，渲染成 PNG 圖片區塊送出，實測將約 25,000 text token 壓縮至約 2,700 image token，依情境不同整體帳單降幅約 59–70%（[GitHub teamchong/pxpipe](https://github.com/teamchong/pxpipe)、[explainx.ai 報導](https://explainx.ai/blog/pxpipe-cut-claude-code-tokens-image-context-proxy-2026)）
- **來源：** GitHub Search 批次抓取（非今日新發布，星數為累積值）；星數 6,955，已查證 fork 598（比例 8.5%，接近防刷佐證基準）、open issues 25、累計 commit 402 次，corroboration 尚可，判斷非刷星
- **成熟度：** ⏳ 新興（技巧方向具新意，但缺乏第一手使用心得、量化降耗數字或社群討論佐證實際效果）

#### resume-on-ratelimit.sh：以 PROGRESS.md + 20 行 shell script 自動恢復被限速中斷的 Claude Code Session（2026-08-04）

- **主線：** 除錯分工
- **核心模式：** 針對「長任務跑到一半撞上 5 小時／7 天用量限制、process 以非零狀態退出、手動重啟又常忘記先前進度」的痛點，作者寫成 20 行的 resume-on-ratelimit.sh：搭配持續寫入進度的 PROGRESS.md，偵測到限速中斷後自動重試並帶著既有進度紀錄接續執行，取代人工守著電腦手動重啟
- **與既有模式的關係：** 補充本頁「Token / 成本優化」類別既有做法在「限速中斷復原」面向的具體實作——既有記錄多聚焦事前的用量監控/節流，本篇聚焦「撞牆後如何自動接續」的下游解法
- **來源：** 「How I Auto-Resume a Rate-Limited Claude Code Session with PROGRESS.md and Retries」— dev.to / bokuwalily（依 dev.to 內容判斷原則收錄：第一手實作記錄，含具體腳本與踩坑細節；3 讚不作為判斷依據）
- **成熟度：** ⏳ 新興（單一開發者工具，20 行 shell script，尚待社群採用回饋）

#### CCN：只清除程式碼中 AI 遺留註解、不動其他內容的清理工具（2026-08-02）

- **主線：** —
- **核心模式：** 針對 AI 模型常在程式碼留下大量註解、佔用 context 的問題，作者打造 CCN，只清除程式碼中的註解，不變動其他任何內容；作者聲稱經過 2,700 次迭代測試
- **與既有模式的關係：** 補充本頁「Token / 成本優化」類別既有「HTML→Markdown 降 80% token」「Token Bloat 對策」等做法在「程式碼本體」面向的新實作——既有做法多聚焦工具輸出/文件層級的 token 精簡，本篇聚焦「AI 留下的程式碼註解本身」這個較少被關注的 context 膨脹來源
- **來源：** 「Show HN: Nuking the crap Claude left in the codebase – CCN」— Hacker News（score 2；訊號強度弱，但具體清理機制與 2,700 次迭代測試的量化聲稱有具體技術實質，依內容判斷收錄）
- **成熟度：** ⏳ 新興（今日首見，單一開發者工具，2,700 次迭代測試聲稱未經第三方驗證）


## 2026-07

### community-guardrails（規則強制、審查與安全）

#### 準備 Anthropic 新版架構師認證考試歸納出的 12 種常見架構決策錯誤（2026-07-31）

- **主線：** —
- **核心模式：** 作者為準備 Anthropic 新推出的 Claude Certified Architect: Professional 認證考試，系統性整理出準備過程中歸納的 12 種常見 Claude 架構決策錯誤
- **與既有模式的關係：** 呼應本頁「架構邊界合約」「Agent 版本控制」等強調「決策先於實作、降低方向偏移」的既有類別，本篇以官方認證考試為切入點系統化整理常見錯誤，是社群將官方認證教材轉化為實戰檢查清單的首個案例
- **來源：** 「12 ways a Claude architecture decision goes wrong (learned these prepping for Anthropic's new Professional cert)」— Reddit r/ClaudeAI（0 留言；單一貼文，訊號強度較弱，依內容判斷收錄）
- **成熟度：** ⏳ 新興；🔎 查無官方 ⟨Q-03⟩

#### 「你的 AI Subagent 在騙你」：317 色碼平行清理任務揭露 4 種 subagent 靜默失敗模式（2026-07-29）

- **主線：** 除錯分工
- **核心模式：** 作者將一項含 317 個硬編碼色碼的 design-token 清理工作拆給多個 Claude Code subagent 平行處理，各自分到一批檔案並回報「完成」，但實際檢查發現多種靜默失敗模式（各 agent 回報乾淨卻結果不然）
- **與既有模式的關係：** 呼應本頁「安全架構」類別中 Grepathy（agent 未經核准決策稽核）對「agent 自主決策是否可信」的既有關注，本篇聚焦「回報完成」本身不可信的具體案例，是對「orchestrator 分派後如何驗證真的完成」這一環節的第一手踩坑記錄
- **來源：** 「Your AI Subagents Are Lying to You: 4 Silent Failure Modes」— dev.to / #claudecode（依 dev.to 內容判斷原則收錄：第一手實作與踩坑記錄，讚數不作為判斷依據；3 讚）
- **成熟度：** ⏳ 新興（單一案例）；🔎 查無官方 ⟨Q-04⟩

#### OneCLI：開源憑證閘道器，讓 AI agent 呼叫服務時不接觸真實密鑰（2026-07-23）

- **主線：** —
- **核心模式：** OneCLI 是一個網路層閘道器，安插在 AI agent 與其呼叫的外部服務之間；依 host/path 比對請求、驗證該 agent 是否應有此存取權限後，才將請求中的佔位符換成真實憑證再放行——agent 本身全程不持有、不可見真實密鑰
- **與既有模式的關係：** 補充本頁「安全架構」類別在「憑證/密鑰管理」面向的具體實作——既有 Grepathy 聚焦事後稽核未經核准的 agent 決策、CLAUDE.md for K8s 聚焦架構層防線，OneCLI 聚焦「請求層即時憑證替換」，把最小權限原則落實在網路層而非應用層
- **來源：** 「Show HN: OneCLI – OSS credential gateway that keeps secrets out of AI agents」— Hacker News（score 101）
- **成熟度：** ⏳ 新興（今日首見，單一開源專案，尚待社群採用回饋）

#### Spare Mac 作為 Claude Code 專屬常駐環境：隔離 --dangerously-skip-permissions 風險（2026-07-18）

- **主線：** —
- **核心模式：** 作者撰寫完整步驟教學，示範如何把備用 Mac 設定為 Claude Code 可透過 computer use 全權控制的常駐環境，並可透過手機或 SSH 遠端下指令；核心動機是風險隔離——作者指出在主力工作機器上開啟 `--dangerously-skip-permissions` 旗標具有固有風險，獨立於主機之外的備用裝置可用來承擔研究與開發任務的風險，即使 agent 出錯也不影響主力環境
- **與既有模式的關係：** 與本頁「安全架構」類別（CLAUDE.md for K8s、Grepathy 等）同屬降低 agent 自主行為風險的思路，差異在於本模式以「實體裝置隔離」而非軟體層稽核/合約作為防線；也與「行動裝置遠端控制」類別（ccgram、Shellular）有交集——皆透過手機遠端操作常駐執行中的 Claude Code / Codex session，但本模式的核心訴求是風險隔離而非單純便利性
- **來源：** 「Setting up your spare Mac for Claude Code to control, a step-by-step guide」— Hacker News（score 234，本輪最高分）
- **成熟度：** ⏳ 新興（今日首見，HN 234 分，顯示高度社群興趣，尚待社群後續實測回饋佐證是否有隱藏風險或限制）

#### Grepathy：偵測與追蹤 Agent 未經核准之自主決策的稽核工具（2026-07-15）

- **主線：** 除錯分工
- **核心模式：** 開發者在一次承包案件中發現，Claude 自行於 Clerk 建立多個帶有空白 email/name 的「訪客帳號」，此舉並不在任何原定計畫內；CTO 詢問原因時，開發者本人也表示自己並不知情、無法解釋此決策從何而來；作者因此釋出 Grepathy，用於偵測、追蹤 agent 做出的未經核准決策
- **與既有模式的關係：** 補足本頁「安全架構」/「Agent 預算控制」類別在「決策可追溯性」面向的缺口——既有 AgentWatch 聚焦資源額度、CI 語意漂移測試聚焦程式碼品質，Grepathy 聚焦「agent 自主決策」本身的稽核；此工具衍生自 [[topics/community-tech-discussions]] 同日收錄的「Claude 未經核准自行建立訪客帳號」信任疑慮討論（雙向連結，該頁「衍生」欄已填 Grepathy）
- **來源：** 「Show HN: Grepathy – Claude made a decision nobody approved」— Hacker News（score 18，跨來源報導）
- **成熟度：** ⏳ 新興（今日首見，工具與其誘因事件同日發布，尚待後續採用回饋）

#### 語音提示／語音輸出小趨勢觀察：Mr. Meeseeks 語音提示外掛（HN 130，本日最高分）與 aloud TTS 輸出工具並現（2026-07-14）

- **主線：** —
- **核心模式：** thephw/claude-meseeks 讓 Claude Code 在長對話準備結束話題時播放 Mr. Meeseeks 的語音台詞作為提示；同日另一 Show HN 專案 softcane/aloud 用 kokoro 語音模型讓 Claude Code / Codex 具備通用語音輸出能力；兩者同屬「為 agent 完成／等待狀態加上語音訊號」思路的不同實作層次——前者是幽默彩蛋式提示音，後者是通用 TTS 輸出層
- **與既有模式的關係：** 延伸既有「Stop Hook 音效通知：最小化版本的 Agent 完成感知」（2026-06-28）音效提示脈絡，從單純音效升級為語音／台詞內容；HN 討論串中另提及既有的 peonping.com 多聲音包方案，顯示「agent 狀態語音化」已累積至少三個獨立實作（peonping、Mr. Meeseeks、aloud）；惟 aloud 互動數據極低（HN 2 分），是否形成穩定趨勢仍待觀察（推論）
- **來源：** 「Claude Code plugin that plays a Mr. Meeseeks voice line whene Claude is waiting」— Hacker News（GitHub thephw/claude-meseeks，score 130，本日社群條目最高分）；「Show HN: Giving Claude Code and codex its voice using kokoro」— Hacker News（GitHub softcane/aloud，score 2）
- **成熟度：** ⏳ 新興（單日集中出現兩則相關工具，尚無跨專案採用數據，是否形成穩定模式待後續觀察）

#### Agent-plan-review-loop：對抗式 Claude Reviewer 逐步挑戰實作計畫（2026-07-10）

- **主線：** 除錯分工
- **核心模式：** 開發者開源 agent-plan-review-loop，讓一個預設「這個計畫是錯的」的對抗式 Claude reviewer 讀取真實 codebase，反覆挑戰待審計畫直到通過審查才放行，解決 LLM 審查者過度樂觀、容易對計畫照單全收的問題
- **與既有模式的關係：** 與既有「多代理 PR Review」類別中「對抗性審查（計畫前 + 程式碼後）」（2026-05-12／06-25）同屬同一模式家族，此案例是該模式在「計畫審查」階段的具體開源實作，reviewer 明確讀取實際 codebase 而非僅憑計畫文字判斷
- **來源：** 「I built a multi-agent loop where an adversarial Claude reviewer reads your actual codebase before approving plans」— dev.to（作者 execute25，#claudeai，原文發布 06-25）
- **成熟度：** ⏳ 新興（單一開源專案，尚無採用數據）

#### 氛圍狀態燈：Hooks 驅動實體 LED 燈號提示 Agent 狀態（2026-07-02）

- **主線：** —
- **核心模式：** 用 ESP32 + WS2812 LED 燈條（跑 WLED 韌體，約 $10 材料成本）搭配 Claude Code hooks，在 session 各階段觸發燈光顏色變化，將 agent 狀態從螢幕通知延伸為實體環境訊號
- **狀態對應：** 藍色＝執行中、琥珀色呼吸＝需要輸入/授權、綠色＝完成、紅色＝失敗
- **解決的問題：** 長時間背景執行 agent 時容易忘記回頭查看是否卡在等待輸入，實體燈光比螢幕通知更不容易被忽略，尤其適合多視窗/多螢幕工作環境
- **與既有模式的關係：** 與 Adrafinil（hooks 感知 agent 活躍狀態決定是否保活螢幕）同屬「hooks 驅動環境副作用」子類別，差異在於 Adrafinil 作用於電腦本身（喚醒/休眠），此模式作用於外部實體裝置（LED）
- **來源：** [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ulgtcq/made_a_10_desk_light_that_tells_me_when_fable_is/)（07-02）
- **成熟度：** ⏳ 新興（單一實作案例，硬體門檻使複製率偏低，但機制簡單可推廣至其他通知媒介如 Home Assistant／智慧燈泡 API）

**懸置細節**
- ⟨Q-03⟩ 🔎 **查無官方**（標 2026-08-10｜查 Certified Architect、12 種｜複 2026-11-24）：複查（2026-10-24）原始 Reddit 貼文仍未能定位，多輪關鍵字調整均無結果。
  - 僅查得背景資訊：Anthropic 於 2026-03-12 發布首個技術認證「Claude Certified Architect, Foundations」。
  - 12 條具體錯誤內容仍無法查證。
- ⟨Q-04⟩ 🔎 **查無官方**（標 2026-08-10｜查 subagent、silent failure｜複 2026-12-14｜訊 2026-08-15）：原始文章已定位（2026-11-14 複查：08-15 日報確認指向同一篇，dev.to 在本輪連線範圍外、四種模式逐條內文仍未核對
  - 官方文件沒有專談這四種模式的說明）——dev.to《Your AI Subagents Are Lying to You: 4 Silent Failure Modes》（07-29 發表，08-15 日報收錄附連結）
  - 內容是「約 317 個硬編碼色碼的 design token 清理切給多個並行 subagent」的第一手記錄；四種模式的逐條內文仍未核對
  - 官方文件只載明失敗如何回報給父代理，不是對這四種模式的回應（2026-11-14 查 [Claude Code subagents 文件](https://code.claude.com/docs/en/sub-agents)）：被截斷的 subagent 會回傳部分輸出並註明未完成，完全無產出會回錯誤而非空結果；「內容對不對」仍須自行驗證。

### community-interfaces（介面與行動裝置）

#### Agenta：開源、可自架模型的 Claude Cowork 替代品，支援任意 harness（2026-07-28）

- **主線：** —
- **核心模式：** 開源專案 Agenta 提供與 Claude Cowork 相似的協作體驗，但可搭配自架（self-hosted）模型與任意 harness，不綁定單一廠商模型
- **與既有模式的關係：** 呼應本頁「介面元件複用」「模型使用策略」等類別中「降低廠商鎖定」的既有關注，是社群對官方 Cowork 產品提出開源平替方向的首個具體實作
- **來源：** 「Agenta: an open-source Claude Cowork alternative where you can use self-hosted models (and any harness)」— Reddit r/LocalLLaMA · 週熱門
- **成熟度：** ⏳ 新興

#### 開源手寫畫布：Claude 回應顯示於使用者手寫筆記旁（2026-07-17，補記技術做法）

- **主線：** —
- **核心模式：** 開發者釋出開源畫布工具，讓 Claude 的回應直接顯示在使用者手寫筆記旁，將 AI 輔助思考與紙本手寫筆記工作流結合，而非侷限於純聊天視窗介面
- **與既有模式的關係：** 與 [[topics/community-tech-discussions]] 07-15 記錄的「r/ClaudeAI 週熱門三則大型個人專案展示」為同一專案（手寫畫布），本頁首次以「模式」角度補記其技術做法；概念上與「介面元件複用」類別（Brainless）同屬 AI coding 工具介面美學探索，但本模式聚焦「手寫 + AI 回應並置」的新互動形式，而非既有元件封裝
- **來源：** 「I built an open-source canvas where Claude responds beside your handwritings」— Reddit r/ClaudeAI（週熱門，已達標；原貼 2026-07-17）
- **成熟度：** ⏳ 新興（單一開源專案展示，尚無其他採用案例佐證）

#### Brainless：模仿 Claude Code / Codex / Grok 介面風格的 shadcn 元件庫（2026-07-15）

- **主線：** —
- **核心模式：** 開發者釋出 shadcn 元件庫 Brainless，收錄模仿 Claude Code、Codex、Grok 等 AI coding 工具介面外觀風格的可安裝 UI 元件（如 pricing block），透過 `bunx shadcn add brainless/pricing` 等單一指令即可加入專案；把「AI coding 工具介面美學」封裝為可直接複用的前端元件
- **與既有模式的關係：** 本頁尚未有「前端 UI 元件複用」類別，屬新出現的類型，與既有 Skills/Plugin 的「封裝可複用單元」思路相通，差異在於封裝對象是視覺元件而非邏輯/流程
- **來源：** 「Brainless: Shadcn components that look like Claude Code, Codex and Grok」— Hacker News（score 124，本日社群條目最高分）
- **成熟度：** ⏳ 新興（今日首見，HN 124 分，顯示高度社群興趣，尚待後續採用回饋）

#### Devthropology：GitHub Repo 貢獻者互動與程式碼健康度視覺化（2026-07-10）

- **主線：** —
- **核心模式：** Show HN 工具 Devthropology 分析 GitHub PR 資料，提供貢獻者互動關係與程式碼健康度的視覺化洞察，供團隊了解協作模式與潛在瓶頸
- **與 Claude Code 生態的關係：** 非 Claude Code 專屬工具，但屬於「AI 輔助開發團隊如何觀察協作健康度」的鄰接工具類別，可作為 agent 大量產出 PR 後的團隊層可觀測性補充（推論）
- **來源：** [Show HN: Devthropology – Better Insights for GitHub Repos](https://devthropology.com/demo)（原文已失效）（Hacker News Show HN，34 分）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；HN≥30分）

#### AI 思考表徵編輯器：視覺化並編輯模型回答前的內部推理（2026-07-10）

- **主線：** —
- **核心模式：** 開發者受 Anthropic 論文《Verbalizable Representations Form a Global Workspace in Language Models》啟發，做出可視覺化並編輯開源模型內部推理表徵（thinking representation）的網頁工具，讓使用者在模型正式作答前介入調整其「思考」內容
- **與既有模式的關係：** 呼應既有「Extended Thinking 為摘要而非真實推理」討論（見 [[topics/community-tech-discussions]]）對「thinking blocks 究竟代表什麼」的持續關注；此工具提供社群一個實驗性介面直接操作內部表徵，而非僅停留在文本層辯論
- **來源：** [Show HN: I built a web tool to see and edit what an AI thinks before it answers](https://lucid.earthpilot.ai)（Hacker News Show HN，31 分）；相關論文亦見於同日 MIT Technology Review 報導「Anthropic found a hidden space where Claude puzzles over concepts」
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；HN≥30分）

#### Shellular：從手機遠端操作本機 Claude Code / Codex Session（2026-07-08）

- **主線：** —
- **核心模式：** 開發者發布 Shellular，讓使用者從手機遠端連線至自有機器，操作正在執行的 Claude Code、Codex 等 coding agent 與終端機、開發伺服器
- **與既有模式的關係：** 與 ccgram（2026-06-28，透過 Telegram 遠端控制 Claude Code）、Android Remote Control MCP（Plugin 設計模式一節）同屬「行動裝置遠端操作 agent session」模式家族的第三個獨立實作；三者共同顯示「手機作為 agent 控制介面」是社群反覆出現的需求，各自選擇不同傳輸層（Telegram bot、MCP、專屬 web app）
- **來源：** [Show HN: Shellular – run Claude Code, Codex, Pi from your phone](https://shellular.dev/)（Hacker News Show HN，32 分，跨 2 來源報導）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；但屬第三個獨立佐證同一需求的實作，模式本身已具跨案例重複出現的訊號）

### community-memory（記憶與 Context）

#### 官方 context engineering 新規則：Anthropic 移除逾 80% Claude Code 系統提示詞（2026-07-26）

- **主線：** Context 管理
- **核心模式：** Anthropic 部落格〈Claude 5 世代模型的 context engineering 新規則〉揭露官方已移除逾八成的 Claude Code 系統提示詞，並給出把同一原則套用到自訂 agent 的建議
- **與既有模式的關係：** 為本頁「Context 管理」類別長期累積的「少即是多、只給最小必要 context」社群直覺，補上第一份廠商側的一手依據；同日的 Opus 5 硬編碼工具限制爭議見 [[entities/claude-code]]，社群辯論見 [[topics/community-tech-discussions]]
- **來源：** 〈Claude 5 世代模型的 context engineering 新規則〉— Anthropic Blog（Hacker News 393 分）
- **成熟度：** ✅ 成熟（官方一手，社群跨平台延燒）

#### CLAUDE.md 載入順序：四層記憶範圍完整拆解（2026-07-31，補記）

- **主線：** —
- **核心模式：** 作者指出「Claude Code 忽略我的規則」的常見根因是規則寫在 Claude Code 根本沒有載入的檔案裡；文章依官方文件（2026-07-31 查證）整理四種記憶範圍與其載入順序，並指出兩個容易忽略的細節：CLAUDE.local.md 在同層級的共用 CLAUDE.md 之後載入，適合放個人化覆寫（沙盒網址、個人測試篩選條件）而不動團隊共用檔案；受管理原則檔（managed policy file）在 Linux／Windows 上也存在，位置不同於 macOS
- **與既有模式的關係：** 補充本頁「CLAUDE.md 管理」類別既有「精簡規則策略」「防腐爛機制」之外的載入機制層細節——既有記錄多聚焦「該寫什麼、多寫會怎樣」，本篇補上「寫了會不會真的被讀到」這個更上游的前提，與 2026-08-04 已收錄的「四層寄放地判斷內容歸屬」互補（該篇談歸屬判準，本篇談載入順序機制）
- **來源：** 「Which CLAUDE.md Files Claude Code Actually Loads (and in What Order)」— dev.to / rulestack（依 dev.to 內容判斷原則收錄：對照官方文件查證的第一手技術拆解，非行銷稿；0 讚不作為排除理由）
- **成熟度：** ✅ 成熟（記憶範圍機制為官方既有設計，本篇是查證後的完整說明整理）

#### CodeAlmanac：從與 Claude Code / Codex 對話自動更新的 Karpathy 風格程式碼庫 Wiki（2026-07-22）

- **主線：** 索引記憶
- **核心模式：** YC S26 團隊釋出開源工具 CodeAlmanac，會隨著使用者與 Claude Code / Codex 的對話內容自動更新程式碼庫 wiki，取代過去需手動維護的 MANUAL.md、DESIGN.md 等文件；強調本地執行、免費、自動維護，降低文件與程式碼庫實際狀態脫節的心力
- **與既有模式的關係：** 補充「記憶與知識管理」類別在「團隊/專案層級知識沉澱」面向的新做法——既有 ltm/NanoBrain/OKF 聚焦 agent 跨 session 記憶，CodeAlmanac 聚焦「程式碼庫本身的說明文件」隨對話自動同步；也與「CLAUDE.md 管理」類別「防腐爛機制」精神相通，皆試圖解決文件隨時間腐化的問題
- **來源：** 「Show HN: CodeAlmanac – Karpathy-style codebase wiki from your conversations」— Hacker News（score 54，YC S26 團隊）
- **成熟度：** ⏳ 新興（今日首見，YC 新創團隊產品，尚待社群採用回饋）

#### Context 分支與合併：精準控制 Claude 對話可見範圍的手動 Context 管理工具（2026-07-15）

- **主線：** Context 管理
- **核心模式：** 開發者釋出應用程式，讓使用者能從任一則歷史訊息分支（branch）出新對話、並可將多個對話串合併（merge），藉此精準控制 Claude 在後續互動中實際看到的 context 範圍；核心訴求與既有「Context Rot 修復」「Just-in-Time @-file Retrieval」同屬「限制/裁剪 context 輸入」思路，差異在於以對話樹狀分支/合併作為使用者可視化操作介面，而非工具層自動裁剪
- **與既有模式的關係：** 補充「Context 管理」類別在使用者互動層（非工具自動化層）的手動控制選項；同一貼文，跨來源出現，視為具一定訊號強度，但尚無公開 repo/demo 連結可查證實作細節
- **來源：** 「I built an app where you control exactly what context Claude sees: branch from any message, merge whole chats. Free to try.」— Reddit r/ClaudeCode
- **成熟度：** ⏳ 新興（今日首見，免費試用產品，尚待社群後續採用回饋佐證）

#### session-indexer：本地 SQLite 索引 Claude Code 逐字稿供跨 Session 語意搜尋（2026-07-12）

- **主線：** 索引記憶
- **核心模式：** Go 工具 session-indexer 讀取 Claude Code session transcript，索引進本地 SQLite 資料庫，讓開發者能跨 session 語意搜尋過去對話與程式碼決策，避免「跨專案記憶消失」問題
- **與既有模式的關係：** 同屬「本機持久化記憶架構」與「Session 記憶與搜尋工具生態」（2026-05-05）模式家族的新實作版本，聚焦本地 SQLite 索引而非雲端或純 Markdown
- **來源：** 「session-indexer: giving Claude Code a memory that doesn't die with the project next door」— dev.to（作者 valpere，原文發布 07-04）
- **成熟度：** ⏳ 新興（單一作者工具，尚無採用數據）

#### Context Window 診斷法：先測量再究責 MCP（2026-07-10）

- **主線：** Context 管理
- **核心模式：** 作者觀察到 agent 在長 session 中途「變笨」，最初直覺懷疑是某個 MCP server 佔用過多 context，但實際測量 context window 使用量後才找到真正原因（並非 MCP 本身），提供「先測量、再歸咎工具」的可複用診斷流程，避免不必要的除錯繞路
- **與既有模式的關係：** 呼應既有「Context 管理生命週期」與「Context Rot 修復五法」（見 [[topics/community-tech-discussions]]）已建立的共識——「越用越笨」多為 context 腐蝕而非模型或工具退步；此案例補充具體診斷步驟（測量優先於歸因），而非直接假設某個外部工具是元凶
- **來源：** 「My AI agent got dumber mid-session. I measured the context window before blaming MCP.」— dev.to（作者 rapls，#claudecode，原文發布 06-17）
- **成熟度：** ⏳ 新興（單一作者第一手診斷經驗，尚無其他來源複現）

### community-skills（Skills）

#### Claude Code Skills 清單字元預算機制：description 超額會讓既有 skill 悄悄失效（2026-07-28）

- **主線：** —
- **核心模式：** 拆解 Claude Code skills 清單載入的字元預算機制：單一 skill 的 description + when_to_use 合計上限 1,536 字元；整體 skills 清單的字元預算則依 context window 的 1% 計算——新增 skill 數量一多，既有 skill 可能悄悄被排出清單、不再被模型觸發使用，且過程中不會出現任何錯誤訊息
- **與既有模式的關係：** 補充本頁「Skills 設計」類別既有「description 自動觸發」機制的邊界條件：過去記錄的是「怎麼設計 skill 讓它被觸發」，本篇補上「觸發預算有硬上限、超額會靜默失效」這項使用者需知曉的限制，屬機制補完而非全新類別
- **來源：** 「Too many Claude Code skills? How the listing budget decides which descriptions Claude sees」— dev.to / rulestack（依 dev.to 內容判斷原則收錄：第一手技術實作拆解，非行銷/SEO 稿；讚數 2 不作為判斷依據）
- **成熟度：** ⚡ 活躍（既有 Skills 設計類別的機制補完）

#### nb2lite-skill-claude：以 Gemini Interactions API 打造有狀態圖片編輯 Claude Code Skill（2026-07-22）

- **主線：** —
- **核心模式：** 作者將 Google gemini-3.1-flash-lite-image 封裝為 Claude Code Skill 與 MCP server（nb2lite-skill-claude），支援多輪、有狀態的圖片編輯（版本追蹤與迭代修改，而非每次重新生成獨立圖片），並提供安裝指南與 dogfood 封面圖範例
- **與既有模式的關係：** 延伸「Skills 設計」與「模型使用策略」類別中「跨模態內容生成分工（InstantVideos）」的既有做法——不同於單次生成或單向 pipeline，此技巧強調「有狀態」的多輪編輯迴圈，補上 Skills 生態中「圖像類多輪任務狀態管理」的具體實作案例
- **來源：** 「Teaching Claude Code to Paint: A Stateful Image-Editing Skill Built on Gemini's Interactions API and MCP」— dev.to / #claudecode（3 讚；依規則以第一手實作內容判斷，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一開發者第一手實作，尚待社群採用回饋）

#### tpu-management：讓 Gemma 4 在 Cloud TPU 上運行的 Claude Code Skill（2026-07-22）

- **主線：** —
- **核心模式：** 作者釋出 Claude Code skill 搭配 MCP server 組合，可一鍵佈建 Google Cloud TPU、以 vLLM 服務 Gemma 4 模型、執行 benchmark，並在完成後自動拆除雲端資源，將原本繁瑣的 TPU 基礎設施佈建/拆除流程封裝為 Claude Code 可呼叫的 skill
- **與既有模式的關係：** 屬「Skills 設計」類別新型態——既有 Skills 案例多聚焦知識框架化或流程封裝，本篇將其延伸至「雲端基礎設施生命週期管理」（佈建→服務→測試→拆除全流程自動化）；與「Agent 預算控制」類別（AgentWatch）同屬降低雲端資源浪費風險的思路，但聚焦點是基礎設施自動拆除而非請求層費用攔截
- **來源：** 「tpu-management: a Claude Code skill for running Gemma 4 on Cloud TPUs」— dev.to（7 讚；依 dev.to 收錄規則以內容判斷，屬第一手實作記錄，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一作者實作記錄，尚無其他來源複現）

#### Sx 2.0：透過 Dropbox / Google Drive / iCloud 免 git 分享 Claude/Codex Skill（2026-07-14）

- **主線：** —
- **核心模式：** Sx 2.0 讓非技術團隊透過既有雲端硬碟（Dropbox、Google Drive、iCloud 等）分享 Claude/Codex 的 skill vault，不需依賴 git 版控知識；2.0 版新增 Mac/Windows/Linux 原生 app 與 Skill Evals 擴充系統，vault 格式重構為可直接作為 Claude 或 Codex plugin 使用
- **與既有模式的關係：** 屬「Skills 設計模式」類別下新的**分享／分發**取向，與既有 ccteams（npm 套件化 subagent 團隊，2026-07-11）同屬「降低 skill/subagent 配置重複勞動」思路，差異在於 ccteams 面向技術團隊（npm 生態），Sx 2.0 面向非技術團隊（免 git、雲端硬碟同步）
- **來源：** 「Show HN: Sx 2.0 – Share AI skills with your team through a Dropbox folder」— Hacker News（score 39）
- **成熟度：** ⚡ 活躍（達 HN，2.0 版已有既有使用者基礎，但採用規模不明）

#### Skill Linter 對 52k-Star Repo 的 84/100 診斷案例：Skill 品質共通模式（2026-07-12）

- **主線：** —
- **核心模式：** 作者自製 skill linter，對一個 52k star 高星 repo 中 24 個 skills 逐一檢測，量化出 84/100 品質分數，並歸納出多個 skill 撰寫的共通可修正模式（如缺乏明確邊界、指令模糊等）
- **與既有模式的關係：** 呼應既有「Caliper：pass@k 指標的 Skill 可靠性測試方法」（2026-06-29），同屬「量化評估 skill 品質」思路的新工具，此案例聚焦靜態規則檢查（linter）而非執行時測試
- **來源：** 「I Pointed a Skill Linter at a 52k-Star Repo. Here Is What 84/100 Looks Like.」— dev.to（作者 sayed_ali_alkamel，原文發布 06-13）
- **成熟度：** ⏳ 新興（單一作者工具與案例，尚無其他來源複現）

#### 用 Claude Code Skill 在 Reddit/LinkedIn 找潛在客戶而非同業（2026-07-12）

- **主線：** —
- **核心模式：** 作者建置自動搜尋潛在客戶的 Claude Code skill，早期版本曾誤抓同業競品作為目標，記錄調整篩選邏輯排除同業、聚焦真實潛在客戶的過程
- **與既有模式的關係：** 新的應用領域案例——「Skill 設計模式」類別過去多聚焦開發流程本身，此案例將 skill 用於銷售/業務開發場景，補充 skill 應用場景多樣性的佐證
- **來源：** 「I built a Claude Code skill that finds customers, not competitors, on Reddit & LinkedIn」— dev.to（作者 newan2001，原文發布 06-19）
- **成熟度：** ⏳ 新興（單一作者工具，尚無採用數據）

%% 拆頁評估 2026-11-21：不拆，分不出群。正文約 700 行，但 Skills 設計一類佔約 470 行（46 則）、可靠性測試只有 6 則約 59 行（每群太薄，<150，併回鄰群）、其餘 15 則多是週邊；Skills 設計內部是各領域 skill 清單（設計、影片、資安、SEO、金融、課程與合輯），讀者問題都是「有沒有現成的 X skill」，沒有各自的結論與節奏；寫法與觸發機制已集中在本頁「慣例與地雷」與「給 coding agent 的 Skill 與角色檔」兩節。下次評估觸發：可靠性測試連續兩個月累積過 150 行，或領域清單裡某一域（如影片 skill）自己長出第二個故事。 %%

### community-multi-agent（Multi-agent）

#### 本地合併佇列：讓多個平行 Claude Code agent 的 commit 依序落地、避免同時建置測試拖垮機器與 CI 帳單（2026-07-30）

- **主線：** 並行規模
- **核心模式：** 作者以 4–5 個平行 Claude Code agent 在 8GB MacBook Air 上每天推送近 90 次 commit，若各分支各自同時觸發建置與測試，機器資源會被拖垮當機；若每次推送都各自跑一輪 CI，90 次推送的 CI 分鐘費用也難以負擔。作者因此打造本地合併佇列，讓所有提交排隊依序落地，逐一完整建置測試後才合併下一筆，取代平行分支各自即時觸發 CI 的做法
- **與既有模式的關係：** 補充本頁「Multi-agent 架構」「Agent 規模化」既有類別在「執行/協調」面向之外的「落地/整合」面向缺口——既有記錄（Claude Squad、ccteams、20-instance 崩潰分析等）多聚焦多 agent 如何並行工作與分派任務，本篇聚焦「多 agent 產出的大量 commit 如何序列化落地」這個下游整合瓶頸，是本頁首次出現針對本地資源與 CI 成本雙重限制設計的合併佇列做法
- **來源：** 「Show HN: A local merge queue for parallel Claude Code agents」— Hacker News（score 39）
- **成熟度：** ⏳ 新興（今日首見，單一開發者工具，尚待社群採用回饋）

#### OtoDock：在自有伺服器上運行 Claude Code + Codex Agent 團隊（2026-07-15）

- **主線：** 並行規模
- **核心模式：** 開發者釋出 OtoDock，讓使用者能在自己的伺服器上，將 Claude Code 與 Codex 組成協作 agent 團隊運作，取代過去分別於終端機單獨呼叫兩工具的做法；作者提到自己過去長期單獨從終端機使用這兩款工具做編碼工作，此工具將其團隊化、伺服器化
- **與既有模式的關係：** 屬本頁既有「Multi-agent 架構」類別的新實作，聚焦「自架伺服器 + 跨工具（Claude Code / Codex）團隊化部署」的形式，與 ccteams（套件化 subagent 團隊配置）同屬打包既有多工具工作流的思路
- **來源：** 「Show HN: OtoDock, run Claude Code and Codex as a team of agents on your server」— Hacker News（score 2，跨來源報導）
- **成熟度：** ⏳ 新興（今日首見，跨來源訊號但單一分數偏低，尚待社群後續採用回饋）

#### ccteams：套件化管理 Claude Code Subagent 團隊（2026-07-11）

- **主線：** 並行規模
- **核心模式：** 開發者發布 npm 套件 ccteams，讓使用者以單一指令（`ccteams use go-api` / `next-ts` / `generalist`）將預先調校好的 builder + reviewer subagent 團隊套用到當前專案，取代過去每個新專案都需重新手寫相同 subagent 組合的重複勞動
- **與既有模式的關係：** 與既有「Multi-agent 架構」「Skills 設計」重疊但聚焦點不同——不是設計新的協作邏輯，而是把已驗證良好的 subagent 配置打包成可跨專案安裝、可版本化的套件，類似把 npm 套件生態的可重用性延伸到 agent 團隊配置本身
- **來源：** 「One command turns Claude Code into a full dev team」— dev.to（作者 toffy，原文發布 06-18）
- **成熟度：** ⏳ 新興（單一作者 npm 套件已發布，尚無採用數據）

#### 平行 Agent 即時對話地圖：讀取本機 JSONL Transcript 的可觀測性工具（2026-07-06）

- **主線：** 並行規模
- **核心模式：** 讀取 Claude Code / Codex 在本機留下的 JSONL transcript 檔案，即時解析並以視覺化「地圖」呈現多個平行 agent 的當前狀態與對話進度，解決「開了多個平行 agent 後不知道彼此進度」的協調痛點
- **解決的問題：** 呼應既有「20-instance 崩潰分析」（2026-06-26）與「1000 Subagents Fan-out」（2026-07-01）已指出的規模化痛點——當平行 agent 數量增加，人工逐一切換視窗確認進度的成本迅速上升；此工具提供集中式可觀測層，補足官方尚未內建的多 agent 協調可視化
- **與既有模式的關係：** 與「Agent 規模化」類別下既有子模式互補：既有模式聚焦「如何讓多 agent 穩定運作」（worktree 隔離、budget enforcement），此模式聚焦「運作中如何被人類即時看懂」；與 Grafana + Prometheus 企業監控（費用/用量導向）不同層次，此工具聚焦單機開發者的即時對話狀態，不涉及計費指標
- **來源：** [Show HN: Orchestrate parallel Claude Code and Codex agents on a live map](https://github.com/Latand/live-log-viewer-next)（Hacker News Show HN，score 2）
- **成熟度：** ⏳ 新興（單一低分 Show HN 專案，尚無採用數據；概念本身回應了規模化章節已反覆出現的真實痛點，值得後續觀察是否有更成熟工具跟進）

#### Claude Code 動態工作流與 1000 Subagents Fan-out（2026-07-01）

- **主線：** 並行規模
- **核心模式：** 以 Claude Code 為主協調器，動態生成大量 subagent 並行執行子任務（宣稱可達 1000 個子代理級別）；fan-out 模式讓任務分解從靜態預設走向執行時動態派發，協調器根據任務複雜度即時決定分支數量
- **實作方向：**
  - 主 agent 先分析任務複雜度，動態決定分支數量與各子任務邊界
  - 每個 subagent 在獨立 worktree 或容器中執行，防止資源競爭
  - 協調器負責彙整所有子代理結果並進行一致性驗證
  - 設計終止條件：子代理失敗閾值、超時機制、人工審查節點
- **解決的問題：** 靜態多 agent 工作流難以應對動態任務規模；100+ subagent 場景下的協調與成本爆炸
- **來源：** dev.to（Claude Code 動態工作流教學；07-01）
- **注意事項：** 1000 子代理為理論上限，實際成本需搭配 AgentWatch 等 budget enforcement 工具；成本爆炸風險高，建議先從 10-20 個 subagent 驗證協調架構

#### Git Worktree 多 Agent 並行：新佐證教學（2026-07-01）

- **主線：** 並行規模
- **核心模式：** 此為 git worktree 多 agent 並行模式的新佐證教學（既有模式見 2026-05-23「Git Worktrees 作為多 Agent 隔離原語」與 2026-06-24「Multi-agent 工作流轉型指南」），dev.to 教學文章提供具體步驟，使此模式從「社群實踐」進一步強化為「有文件可循的標準做法」
- **新增細節：**
  - 明確的 worktree 創建指令序列（`git worktree add`）與 Claude Code session 綁定方法
  - 結果彙整策略：各 worktree 完成後的 merge 時機與衝突解決規範
  - 與動態 fan-out 模式的組合使用：靜態 worktree 預先分配 vs 動態按需創建
- **成熟度更新：** 多篇獨立教學、工具化（Claude Squad、Superset、Claudette）、企業場景驗證，此模式實際成熟度已達 ✅，模式概覽維持 ✅ 成熟確認
- **來源：** dev.to（Git worktree 多 agent 並行教學；07-01）

### community-cost（成本與用量）

#### 作者 grep 自己的 Claude Code JSONL 逐字稿，發現未見於官方文件的 `<ip_reminder>` 隱藏標籤（2026-07-29）

- **主線：** —
- **核心模式：** 作者未查閱官方文件，而是直接翻自己的 Claude Code session JSONL 逐字稿，找到一個名為 `<ip_reminder>` 的標籤在對話中途出現；此標籤未見於任何官方文件說明
- **與既有模式的關係：** 呼應本頁既有「Local Reverse Proxy」「Context Window 診斷法」等「直接檢視 Claude Code 實際送出/收到內容」的第一手偵測方法論類別，補上「逐字稿逆向檢視」這個更輕量、免架設代理即可執行的檢視手段
- **來源：** 「I Grepped My Own Claude Code Logs and Found the Hidden Tag Anthropic Never Shows You」— dev.to / nomurasan（依 dev.to 內容判斷原則收錄：第一手日誌挖掘，非行銷/SEO 稿；讚數不作為判斷依據）
- **成熟度：** ⏳ 新興（單一開發者觀察，暫不歸入既有機制類別；原文已查證，見下方懸置細節 ⟨Q-05⟩）

#### Anyclaude-SDK：讓 OpenAI/Anthropic 端點都能使用 Claude Code 風格 SDK（2026-07-28）

- **主線：** —
- **核心模式：** 開源 SDK，讓開發者可用 Claude Code 風格介面呼叫 OpenAI 或 Anthropic 端點，降低切換供應商時的介面改寫成本（僅有標題可考，具體實作細節未知）
- **與既有模式的關係：** 呼應本頁「模型使用策略」類別既有多模型路由思路，但聚焦「介面層一致化」而非「路由決策」，補上供應商切換降低改寫成本的角度
- **來源：** 「Show HN: Anyclaude-SDK – Claude Code-Style SDK for OpenAI/Anthropic Endpoints」— Hacker News（score 4）
- **成熟度：** ⏳ 新興（今日首見，說明有限，暫記觀察）

#### 只在需要頂尖判斷力任務用 Fable 5，其餘交給便宜 subagent 控制成本（2026-07-26）

- **主線：** —
- **核心模式：** 作者分享實務作法：僅在需要頂尖判斷力的任務（架構決策、疑難排解）呼叫 Fable 5，其餘實作、測試、雜務等交由較便宜的 subagent 處理，藉此控制整體 token 成本
- **與既有模式的關係：** 呼應本頁「模型使用策略」類別既有「分層模型（Sonnet + Opus）」「依任務複雜度路由」思路，屬同一分層成本策略在 Fable 5 世代的具體延伸案例，非新機制
- **來源：** 「Use Fable 5 where it pays for itself」— dev.to / #claudecode（依 dev.to 內容判斷原則收錄：第一手成本控制實作經驗，非行銷/SEO 稿；讚數 9 不作為判斷依據）
- **成熟度：** ⚡ 活躍（既有分層模型策略的延伸案例）

#### claude-thermos：保持 Claude session 快取熱度的工具，引發「成本轉嫁」爭議（2026-07-23）

- **主線：** —
- **核心模式：** 作者釋出 claude-thermos，透過定期送出保活請求維持 Claude session 的 prompt cache 不過期，避免快取到期後重新產生內容所帶來的高成本；HN 討論中同時揭露 Pro/Max 方案目前快取到期時間為 1 小時，此前一度退化至僅 5 分鐘
- **與既有模式的關係：** 直接對應本頁「Token / 成本優化」類別既有觀察「快取不跨 session 是費用主因」——此工具是社群對該痛點的具體 workaround；但 HN 高分留言同時質疑「這只是把成本轉嫁給其他用戶」，認為此類保活行為可能變相佔用共享額度/基礎設施資源，工具本身與其正當性皆有爭議，尚無社群共識（爭議面詳見 [[topics/community-tech-discussions]] 同日收錄之討論）
- **來源：** 「Show HN: Claude-thermos keeps your Claude session warm for you」— Hacker News（score 102）
- **成熟度：** ⏳ 新興（今日首見，工具本身與其倫理正當性皆有爭議，尚待社群共識）

#### 依任務類型分工選用 Claude 模型／Code／Cowork（2026-07-23）

- **主線：** —
- **核心模式：** 媒體報導使用者依任務性質分別選用不同 Claude 產品線（模型選擇、Claude Code、Cowork），依情境切換使用工具而非單一工具包辦所有任務（僅標題可考，具體判準細節未知）
- **與既有模式的關係：** 呼應本頁「模型使用策略」類別既有「依任務複雜度路由」思路，但本篇聚焦人工決策層面的產品線分工，而非自動化路由機制，補上使用者側手動選型的案例角度
- **來源：** 「I use Anthropic's Claude AI tools for very different jobs: How to pick between models, Code, and Cowork」— ZDNET（Google News；僅標題可用，內容細節未知，暫不深入推論）
- **成熟度：** ⏳ 新興（媒體標題轉載，缺乏第一手操作細節，暫記以觀察後續是否有更詳細跟進報導）

#### MCP Server 設計對每輪對話隱藏 token 成本的實測比較（2026-07-21）

- **主線：** Context 管理
- **核心模式：** 作者為 Claude Code 加裝多款不同設計的 MCP server，實測量化各設計注入每輪對話的隱藏 context token 量，比較不同工具清單/描述長度/回傳格式設計對 token 成本的具體影響，屬第一手量化測量而非單純教學或新聞轉述
- **與既有模式的關係：** 補充既有「Token / 成本優化」類別下「MCP context bloat」（9 個 MCP 伺服器 = 每輪 38k tokens 冷啟動）與「Plugin / MCP 整合」類別「Plugin 反模式整理」的量化佐證，聚焦「MCP server 設計選擇」本身對 token 成本的影響，而非工具數量單一變因
- **來源：** 「I added MCP servers to Claude Code. Here's what they cost in tokens.」— dev.to（1 讚；依 dev.to 收錄規則以內容判斷，屬第一手量化實測，非讚數）
- **成熟度：** ⏳ 新興（單一作者實測，尚無其他來源複現比較數字）

#### Fable 5 Orchestrates, Cheap Models Execute：社群轉載 46% 成本達 96% 效能的多模型工作流模式（2026-07-14）

- **主線：** —
- **核心模式：** Reddit 社群整理流傳的多模型工作流量化數字：由 Fable 5 負責任務協調（orchestrate）、便宜模型負責實際執行（execute）的分工架構，宣稱可在僅 46% 成本下達到 96% 的效能表現；此模式並非未來規劃，而是可直接在 Claude Code 中設定使用的現行做法
- **與既有模式的關係：** 與既有「模型使用策略」類別下社群自建的分層模型路由（Sonnet + Opus）、Workweave Router 同屬「依任務複雜度分流節省成本」思路，差異在於本則提供具體量化數字（46% 成本／96% 效能），將社群長期實務直覺量化為可比較的基準；惟數字來源為 Reddit 整理轉載，非官方逐字確認的第一方發布
- **來源：** Reddit r/ClaudeAI（週熱門，社群轉載，原始官方發布連結未見）；第三方查證（2026-08-13）：BrowseComp 上 Fable 5 orchestrator + Sonnet 5 executor 86.8%（Fable 5 單獨 90.8%），成本 $18.53 vs $40.56／題；細節見 [explainx.ai](https://explainx.ai/blog/fable-5-advisor-orchestrator-patterns-july-2026)、[Jon Krohn](https://www.jonkrohn.com/posts/2026/7/20/fable-5-as-advisor-anthropics-two-model-pattern-for-smarter-cheaper-agents)
- **成熟度：** ✅ 成熟（社群轉載量化數字＋第三方查證，可直接複現於 Claude Code；原始官方發布連結未見，來源等級為社群轉載非官方基準，2026-09-07 更正，見 [[entities/fable-5]]）

#### AWS Bedrock 執行 Claude Code 單日 $8.43 計費教訓（2026-07-12）

- **主線：** —
- **核心模式：** 開發者首次改用 AWS Bedrock 執行 Claude Code，記錄單日花費 $8.43 的實測計費細節與意外之處，作為「透過 Bedrock 用 Claude Code」路徑的第一手成本參考
- **與既有模式的關係：** 補充既有「費用可觀測性工具」與「Token 路由與成本優化」類別中缺乏的 Bedrock 路徑具體數字，可與 API 直連、Claude Desktop 訂閱制的成本案例並列比較
- **來源：** 「How My First Claude Code on AWS Bedrock Experiment Cost Me $8.43 in Just One Day」— dev.to（作者 aws-builders，原文發布 06-16）
- **成熟度：** ⏳ 新興（單日單一案例，樣本量小）

#### 「讓 Fable 5 物有所值」的分層模型路由實務（2026-07-12）

- **主線：** —
- **核心模式：** 作者主張僅在需要頂尖判斷力的任務上使用 Fable 5，其餘工作交給成本較低的 subagent 處理，以此讓 Fable 5 的高單價「物有所值」
- **與既有模式的關係：** 屬「模型使用策略」類別下既有 Workweave Router／Dragoman 等成本感知路由思路的實務心法版，聚焦「何時該用旗艦模型」的判斷原則而非工具本身
- **來源：** 「Use Fable 5 where it pays for itself」— dev.to（作者 toffy，原文發布 07-02）
- **成熟度：** ⏳ 新興（單一作者實務分享，未見量化數據）

#### Local Reverse Proxy：攔截並檢視 Claude Code 實際送出的請求內容（2026-07-10）

- **主線：** —
- **核心模式：** 因 Claude Code 不遵守 HTTP_PROXY 環境變數設定，作者自建一個跑在 loopback 的本地反向代理，即時攔截並檢視每次請求送往 Anthropic 的完整 prompt、token 用量與花費，補足官方缺乏的請求層可觀測性
- **與既有模式的關係：** 與既有「費用可觀測性工具」類別（成本追蹤/預算工具）互補，差異在於此工具聚焦「請求內容本身」的透明度而非僅統計費用數字；也呼應 07-01「Claude Code 隱寫術」信任危機事件後，社群對「Claude Code 究竟送了什麼出去」的關注升高（見 [[topics/community-tech-discussions]]）
- **來源：** 「I built a local reverse proxy to see what Claude Code actually sends to Anthropic」— dev.to（作者 houleixx，#claudecode，原文發布 06-10）
- **成熟度：** ⏳ 新興（單一作者工具，未見開源 repo 連結或採用數據）

#### InstantVideos：Claude + GLM-5.2 + Nano Banana 2 Lite + ffmpeg 多模型短影音自動化 pipeline（2026-07-07）

- **主線：** —
- **核心模式：** 開發者以 Claude（腳本/協調邏輯）搭配 GLM-5.2（文案/對話生成）、Nano Banana 2 Lite（圖像/畫面素材生成）與 ffmpeg（影片合成輸出）組成端到端自動化短影音生成與發布 pipeline，宣稱 30 秒內可產出一支短片
- **與既有模式的關係：** 屬「模型使用策略」類別下的多模型路由思路在**內容生成領域**的新應用——既有 Dragoman / Workweave Router 聚焦編碼任務的成本路由，此案例改為依「任務類型」（文字/圖像/影音合成）分派給各自最擅長的專門模型，而非單一模型包辦全流程；反映多模型編排正從程式碼領域擴散至內容生產領域
- **來源：** [Show HN: InstantVideos](https://instantvideos.org/)（Hacker News Show HN，23 分，跨 2 個獨立來源提及）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；多模型分工生成內容的具體組合方式值得後續觀察是否有其他工具跟進類似「依內容類型路由至專門模型」的架構）

#### CaveMan Skill：單次回覆 Token 從 70 降至 20 的極簡輸出模式新實作（2026-07-06）

- **主線：** —
- **核心模式：** 開源 Claude Code skill「CaveMan」透過強制模型以極簡風格回應，聲稱可將單次回覆 token 使用量從約 70 降至約 20（降幅約 71%），延續「穴居人模式」（極簡輸出降低 token 消耗）的既有思路
- **與既有模式的關係：** 與 2026-05-05 已記錄的「Caveman Skill 實測 65% 降耗」、2026-07-01「企業穴居人模式採用確認」（404 Media：OpenAI、Nvidia、GitHub 開發者採用）同屬同一模式家族的新實作版本；顯示極簡輸出降耗已從單一實測案例演變為社群持續產出的多個獨立實作
- **來源：** [Claude Code with CaveMan (opensource skill) cuts token usage per response from 70 to 20](https://www.reddit.com/r/ClaudeCode/comments/1uox6ko/claude_code_with_cavemanopensoure_skill_cuts/)（Reddit r/ClaudeCode，07-06）
- **成熟度：** ⚡ 活躍（沿用「穴居人模式」既有活躍分類；具體降幅為單一作者自述，未見第三方獨立複現數據）

#### 本地小模型分流節省 Context：Fast Context Task Router 機制觀察（2026-07-05）

- **主線：** Context 管理
- **核心模式：** 將程式碼探索（code exploration）工作委派給本地執行的小型 LLM（local-Ollama task router）分流處理，僅將篩選後的精簡結果送回主 agent，藉此降低主 context window 的 token 消耗
- **效果：** 使用者聲稱可節省 50–60% context token，代價是整體執行時間增加（本地小模型推論延遲 + 額外一層路由判斷）
- **來源：** [Why did Microsoft pull Fast Context from public domain?](https://www.reddit.com/r/ClaudeCode/comments/1unz1s5/why_did_microsoft_pull_fast_context_from_public/)（Reddit r/ClaudeCode，07-05）；原專案（Microsoft）含 arXiv 論文、GitHub repo、自訓練模型，現已從公開領域下架，原因不明
- **與既有模式的關係：** 與「模型使用策略」類別下的分層模型路由（Dragoman / Workweave Router）同屬「依任務複雜度分流降低成本」思路，差異在於此模式分流對象是 context 探索階段而非整個任務執行；下架爭議與機制本身的社群反思見 [[topics/community-tech-discussions]]
- **成熟度：** ⏳ 已停擺（原專案 07-05 下架，逾 60 天無任何後續實作接手，機制僅存本則社群轉述，無可裝的現行版本；官方最接近的替代是 `CLAUDE_CODE_SUBAGENT_MODEL`，見 [[topics/community-pattern-trends]] 趨勢四）

#### 額度監控與自動恢復工具生態（2026-07-03）

- **主線：** —
- **核心模式：** 針對 Fable 5 額度限制帶來的使用者焦慮，社群自發出現兩類輔助工具：① 自動恢復型——限制解除瞬間自動送出 continue，減少手動盯盤等待（呼應 06-27 已記錄的「quota 重置後需手動 continue」automation gap 痛點）；② 監控可視化型——在作業系統選單列即時顯示剩餘額度與使用比例，讓使用者在額度耗盡前主動調節任務節奏
- **代表工具：**
  - [CCLimitPing](https://github.com/wavever/CCLimitPing)（Show HN score 2）：5 小時限制解除的瞬間自動觸發 continue
  - [LimitBar](https://mikaweiss6.gumroad.com/l/limitbar)（Show HN score 2，跨來源佐證）：macOS 選單列 app，即時顯示 Claude 用量限制
- **解決的問題：** 額度耗盡後的手動恢復延遲、以及額度使用狀態缺乏即時可視性，兩者共同構成「額度感知能力不足」的體驗缺口；與既有 Tokenyst（任務層級 token 預算顯示）同屬費用/額度控管工具鏈，但聚焦於「限制與恢復時機」而非「花費金額」
- **來源：** Hacker News Show HN（07-03，兩則均為個人專案，分數低於工具目錄一般所需分數）
- **成熟度：** ⏳ 新興（單日兩個獨立小工具同時出現，尚無採用數據，回應的是同晚 Reddit 額度焦慮情緒串所反映的真實痛點，值得後續觀察是否有更成熟工具跟進）

**懸置細節**
- ⟨Q-05⟩ **ip_reminder 標籤**：原始文章已定位——[dev.to/nomurasan](https://dev.to/nomurasan/i-grepped-my-own-claude-code-logs-and-found-the-hidden-tag-anthropic-never-shows-you-17c0)（2026-07-27 發表，查證日 2026-09-20）。
  - 作者 grep 自己的 JSONL session log 找到 `<ip_reminder>` 標籤，單一 session 比對出 151 行相符、437 次出現，判定為版權安全用途的系統層注入。
  - **屬社群逆向工程發現、非官方確認**，且與先前查得的 `<system-reminder>` 標籤（GitHub issue #52018、#17601）不是同一個。

%% 拆頁評估 2026-11-21：不拆，分不出群。正文約 610 行，剛過門檻；三類中 Agent 預算控制只有 1 則約 9 行（太薄），Token／成本優化約 208 行、模型使用策略約 173 行、額度監控與帳號橋接等其他約 180 行，讀者問題都是「怎麼少花錢、怎麼看見花在哪」，目前結論與「用量去向歸因」「用量窗口與配額守門」兩節共用同一組結論（subagent 既是用量來源又是路由對象），切開後每群都得借另一群的結論。模型使用策略受官方定價與模型發布影響最大，若之後一個月內有官方定價事件把路由與監控的讀者問題拉開，再評估切出。 %%


## 2026-06

#### Agentic Orchestrator：確定性框架 + 非確定性 Agent 混合架構（2026-06-30）

- **核心模式：** DoorDash 開源的長時間 coding agent 編排 TUI（Go 語言），將 agent 工作流切分為確定性階段（需求釐清 → 研究 → 設計 → 多階段規劃 → 實作 → 審查），每個階段由人工審查閘門控制是否繼續；非確定性的 LLM 只在每個階段內部執行（[GitHub doordash-oss/agentic-orchestrator](https://github.com/doordash-oss/agentic-orchestrator)；HN Show HN score 13，06-30）
- **解決的問題：** 長時間 agent 任務缺乏可見性和可控性；agent 自主執行 8 小時的「黑盒感」讓工程師難以信任輸出——可視化各階段進度並在關鍵節點插入人工決策點，降低大型任務失控風險
- **設計亮點：** 明確分離「確定性工作流編排（框架）」與「非確定性 LLM 執行（agent）」——框架掌管任務順序與人工閘門，agent 掌管每個階段的具體執行；一個使用者報告 8 小時連續使用無問題
- **與既有模式的差異：** 既有 multi-agent 框架（Aharness、ANMA）著重 agent 間的協調與邊界合約；Agentic Orchestrator 著重「人機混合審查的 stage gate」——人類在框架中是一等公民而非觀察者
- **成熟度：** ⏳ 新興
- **訊號強度：** HN Show HN score 13，DoorDash 工程團隊出品，有完整 Go 實作

#### Loop Exit Condition：Agent 循環終止設計模式（2026-06-30）

- **核心模式：** 明確設計 agent loop 的終止條件——「如何停下」是長時間 agent 工作流中最容易被忽視、最難正確設計的部分；終止條件設計不良是 runaway agent 的主要根因（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ujqht2/running_claude_in_a_loop_is_the_easy_part_getting/)，06-30）
- **解決的問題：** 「跑起來容易，停下難」——社群普遍能讓 agent 進入循環，但終止邏輯複雜：成功條件、失敗條件、最大重試次數、人工介入觸發點，每一個設計錯誤都可能導致無限循環或過早終止
- **已知終止條件設計方向：**
  - 計數器：最大迴圈次數上限（防 runaway）
  - 狀態機：定義合法的終止狀態（success/failure/timeout）
  - 人工確認閘門：關鍵決策前要求人工確認
  - 自評估：agent 在每輪結束後評估「任務是否完成」（需防幻覺——agent 容易錯誤自評為完成）
- **與 AgentWatch 的關係：** AgentWatch 是預算層的強制截斷（runtime enforcement）；Loop exit condition 是業務邏輯層的合法終止設計——兩者互補，都是 runaway agent 防護的必要元件
- **成熟度：** ⏳ 新興（概念廣泛共識，但系統化最佳實踐尚未收斂）
- **訊號強度：** Reddit r/ClaudeAI 社群討論，無具體工具但有廣泛共鳴

#### 結構化 Markdown 編輯器：防止 Agent 記憶損壞的架構模式（2026-06-30）

- **核心模式：** agent 需要修改 Markdown 記憶檔案時，改用結構化編輯器（AST 層操作）取代 regex 字串替換；regex 在 Markdown 結構複雜時（嵌套清單、代碼塊、YAML front matter）容易造成非預期覆寫或格式損壞（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ujqbwy/my_agent_kept_destroying_its_own_memory_file_with/)；另提供 hosted 無本地磁碟版本，06-30）
- **解決的問題：** 開發者發現 agent 使用 regex 修改記憶檔案，在處理嵌套結構時反覆破壞檔案格式；損壞的記憶檔案導致後續 session 無法正確讀取跨 session 知識，造成 cascade failure
- **實作方向：** 使用 Markdown AST（如 remark/unified 生態）定位並修改特定節點，保留周圍結構；也可使用 section-level 操作（定位標題、替換整個 section 內容）取代字元層 regex
- **與既有記憶架構的關係：** OKF（物件鍵格式）著重記憶內容的格式標準化；此模式著重記憶操作的安全性——是記憶管理的防禦性基礎設施
- **成熟度：** ⏳ 新興
- **訊號強度：** Reddit r/ClaudeAI，開發者開源解決方案並提供 hosted 版本

#### Cross-repo Blast Radius 分析：補足 Claude Code 與 Cursor 的依賴圖盲點（2026-06-30）

- **核心模式：** Claude Code 讀取完整 clone、Cursor 讀取相似度索引，但兩者都無法看到跨 repo 的依賴圖（blast radius）；透過串接外部依賴圖工具，分析一個變更會影響多少下游 repo 或服務（[dev.to](https://dev.to/danielwe/claude-code-reads-your-clone-cursor-reads-similarity-neither-sees-the-graph-487i)，06-30）
- **解決的問題：** AI 編碼工具在單一 repo 內表現良好，但跨 repo 依賴可視性差——修改一個共用函式庫時，無法知道有哪些下游服務會受影響（blast radius 不透明）
- **實作方向：** 在 Claude Code session 開始前，先執行 blast radius 分析（如 `nx graph`、Gradle dependency tree、自建依賴圖），將結果注入 context；讓 agent 在執行前知道「修改這個函式會影響 N 個服務」
- **注意事項：** 依賴圖的維護成本高，需定期更新才能反映真實依賴狀態（推論）；此方案不改變 Claude Code 本身，是 pre-session context 注入策略
- **成熟度：** ⏳ 新興
- **訊號強度：** dev.to 文章，有具體技術分析，但無 HN/Reddit 討論驗證

#### MCP Server 長 Session 失效模式與穩健化策略（2026-06-30）

- **核心模式：** MCP server 在長時間 session 中有三大常見失效模式，各需對應穩健化策略（[dev.to](https://dev.to/ursula_harrell_32416a7c42/building-reliable-claude-code-workflows-with-mcp-servers-pon)，06-30）
- **三大失效模式：**
  - **連線中斷（Connection Drop）：** MCP server 在長 session 中無聲斷線，Claude Code 繼續呼叫已失效工具得到靜默失敗；對應：心跳檢查 + 自動重連
  - **工具超時（Tool Timeout）：** 慢速工具（如資料庫查詢、外部 API）在 agent loop 中累積延遲；對應：設定超時閾值 + 重試策略
  - **上下文失憶（Context Amnesia）：** 長 session 後 MCP server 的 stateful context 與 Claude 的理解出現分歧；對應：在關鍵節點快照 session 狀態，必要時重置 server
- **與既有 MCP 討論的差異：** 既有討論（MCP 成本結構、工具選擇混亂）著重「工具過多」的靜態問題；此模式著重「長時間運行」的動態穩定性問題——是 agent pipeline 生產化的必要考量
- **成熟度：** ⏳ 新興
- **訊號強度：** dev.to 文章，有系統性分析框架，尚無大規模社群驗證

#### AgentWatch：請求攔截層的 Runtime Budget Enforcement（2026-06-29）

- **核心模式：** 在 LLM 請求到達模型前攔截並強制執行預算限制（token 數或費用上限）；超過預算則拒絕請求或回傳錯誤，防止 runaway agent 持續消耗資源（[agent-watch.dev](https://agent-watch.dev/)；HN Show HN score 7）
- **實作方向：** 修改 base URL 指向 AgentWatch proxy；支援 OpenAI、Anthropic、Gemini API；無 SDK 依賴，不需修改應用程式碼；可設定每個 session 或全局的費用/token 上限
- **解決的問題：** Agent 失控（runaway）是多 agent 架構的已知風險——循環呼叫、錯誤重試、無終止條件均可導致費用暴增；此方案在請求層設置硬邊界，比應用層 guard 更可靠
- **與既有模式的差異：** 既有 budget 控制策略（Token 成本優化、模型路由）著重「用更少 token 完成任務」；AgentWatch 著重「超過上限直接截斷」——是防禦性邊界，不是優化策略
- **注意事項：** 截斷中途任務可能導致 partial state；需配合 checkpoint 機制設計才能安全使用（推論）；HN score 7，有公開網站，尚無社群大規模驗證
- **成熟度：** ⏳ 新興
- **訊號強度：** HN Show HN score 7，有公開網站

#### Caliper：pass@k 指標的 Skill 可靠性測試方法（2026-06-29）

- **核心模式：** 以 pass@k（執行 k 次，至少成功 1 次的比率）衡量 Claude Code / Codex skills 的可靠性，而非單次執行成功率；用 YAML 定義任務的成功條件，本地輕量執行（[GitHub](https://github.com/edonadei/caliper)；HN Show HN score 3）
- **實作方向：** 以 YAML 格式描述 skill 的輸入、預期輸出、成功判定條件；執行多次取通過率；pass@k 越高代表 skill 的可靠性越高
- **解決的問題：** 「跑一次成功 ≠ 可靠」——非確定性 LLM 輸出在生產環境需要統計意義上的可靠性評估，而非單次 demo
- **與既有模式的差異：** 既有測試模式（Judge Gate、語意漂移 CI）著重「正確性驗證」；pass@k 著重「穩定性分布」——後者更適合用來選擇 skill 設計方案
- **成熟度：** ⏳ 新興
- **訊號強度：** HN Show HN score 3，有公開 repo，概念清晰可直接採用

#### beads + Claude Code 兩層工作規劃架構（2026-06-29）

- **核心模式：** 以 beads（或類似高層規劃工具）進行任務分解和工作規劃，再搭配 Claude Code 執行具體開發工作；規劃層（人類或工具）處理「做什麼」，執行層（Claude Code）處理「怎麼做」（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uiri45/nice_workflow_in_claude_code/)）
- **解決的問題：** 直接讓 Claude Code 處理高層規劃，容易在方向性決策上偏移或遺漏邊界案例；分層後規劃層保持人類主導，執行層充分利用 Claude Code 的自動化能力
- **設計分層：** 與「任務開始前先 Interview」模式（2026-06-25）互補：beads 在外部規劃，Interview 模式在 session 內部澄清；beads 的外部規劃輸出可作為 Claude Code session 的高品質初始 context 注入
- **注意事項：** beads 工具本身的採用訊號有限；核心模式（規劃/執行分層）概念已在社群多處出現（/specs 目錄、Agentic 目錄結構等），beads 是此模式的一種實作選擇
- **成熟度：** ⏳ 新興（模式概念有效；具體工具組合待更多驗證）
- **來源：** [Reddit r/ClaudeAI 討論](https://www.reddit.com/r/ClaudeAI/comments/1uiri45/nice_workflow_in_claude_code/)

#### Agent Context 上限主動管理：56KB 問題與即時截斷策略（2026-06-29）

- **核心模式：** 主動為 agent 設定 context 讀取上限，避免「為回答單一問題讀取 56KB 文件」的低效行為；核心做法是在 task 設計時明確約束 agent 可讀取的最大 context 量（[dev.to](https://dev.to/enjoy_kumawat/my-ai-agent-read-56-kb-to-answer-one-question-i-made-it-stop-34g5)）
- **實作方向：** 在工具設計或 hook 層設定讀取上限（行數、字元數）；搭配索引 / 摘要層讓 agent 先查索引再決定是否全讀；明確在 CLAUDE.md 或 skill 描述中指定「不需要讀取整個檔案」的場景
- **解決的問題：** Agent 為確保「完整性」傾向讀取整個文件，但大量場景只需讀取相關片段；過度讀取既消耗 token 又降低 context 訊噪比
- **與既有模式的差異：** Just-in-Time @-file（2026-06-26）著重「何時取回」；本模式著重「取回多少」——兩者結合形成完整的 context 精準注入策略
- **成熟度：** ⏳ 新興

#### Hooks 環境感知條件觸發：依 Agent 活躍狀態驅動系統副作用（2026-06-28）

- **核心模式：** 用 Claude Code hooks 偵測 agent 是否正在執行，依此決定是否觸發系統層副作用（如 `pmset disablesleep 1`）；典型應用：Adrafinil 解決 Mac 半開蓋走動時 agent 被睡眠中斷的問題，只在 agent 工作時保活，完成後自動釋放（[GitHub](https://github.com/kageroumado/adrafinil)；HN score 113）
- **與既有模式的差異：** 既有 hooks 模式（PostToolUse 稽核、Pre-completion Hook）以 hooks 執行業務邏輯（規則驗證、輸出格式）；此模式以 hooks 回讀 agent 狀態來決定副作用是否觸發——從「規則執行觸發器」升格為「環境感知條件觸發器」
- **應用延伸（推論）：** 相同模式可延伸至其他環境感知場景：依 agent 活躍狀態控制 Slack DND、資源分配、冷卻提醒；任何「只在 agent 工作時才需要的副作用」均可套用
- **成熟度：** ⚡ 活躍（HN 113 顯示真實痛點，解法可直接使用）
- **訊號強度：** HN Show HN score 113，有公開 repo，可直接複製

#### OKF：物件鍵格式跨 Session Agent 記憶（2026-06-28）

- **核心模式：** 以「物件鍵格式（Object Key Format，OKF）」標準化 Claude Code agent 在 session 之間傳遞的知識結構；讓 agent 產生的記憶片段可攜、可讀，適合團隊共用同一個 Claude Code 工作流（[dev.to](https://dev.to/scaccogatto/okf-for-claude-code-structured-portable-memory-your-agent-and-team-can-read-4ocn)，06-28）
- **與既有模式的差異：** 既有跨 session 記憶方案（ltm Core Memory Packet、本機圖資料庫）偏向工具驅動；OKF 是格式標準（純 Markdown 可讀），不依賴特定工具實作，偏向「規約」而非「框架」
- **適用場景：** 多人共用 Claude Code 工作流、需要 agent 知識在 session 間保持一致性的長期專案
- **注意事項：** 文章為個人分享，無 HN 訊號，尚待社群驗證複現性
- **成熟度：** ⏳ 新興

#### Stop Hook 音效通知：最小化版本的 Agent 完成感知（2026-06-28）

- **核心模式：** 透過 Claude Code `stop` hook 在 agent 完成時觸發系統音效，讓開發者立即得知可繼續操作，無需輪詢終端輸出；是 hooks 最低門檻的實用應用案例（[dev.to](https://dev.to/anand_rathnas_d5b608cc3de/i-made-claude-code-ding-when-its-done-and-it-changed-my-workflow-5e35)，06-27）
- **實作方向：** 在 Claude Code 設定中加入 `stop` hook，呼叫 `afplay` / `paplay` 播放提示音；可擴展為系統通知（macOS `osascript`、Linux `notify-send`）
- **解決的問題：** agent 執行時開發者切換至其他工作，需要知道何時返回；音效比輪詢終端更低認知成本
- **設計分層：** 與 Adrafinil 的「環境感知條件觸發」構成一組：Adrafinil 是 agent 開始時的環境感知，stop hook 音效是 agent 結束時的環境通知
- **成熟度：** ⚡ 活躍（原理簡單，可即時複製）

#### ccgram：透過 Telegram 遠端控制 Claude Code Sessions（2026-06-28）

- **核心模式：** 透過 tmux + ccgram 讓 Claude Code sessions 在 Telegram 可視、可控；sessions 繼續在本地終端機真實執行，Telegram 作為遠端控制介面；v4.3.0 更新（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhogpe/ccgram_v430_control_claude_code_and_shell_from/)，06-27）
- **適用場景：** 離開電腦時監控長時間 agent 任務、行動裝置臨時介入正在執行的 session
- **與既有模式的差異：** 既有遠端控制方案（iOS app 接力）依賴官方 claude.ai 介面；ccgram 走 Telegram，適合已有 Telegram bot 生態的用戶，且可同時控制 Claude Code + 一般 shell 工作階段
- **注意事項：** Reddit 來源，無 HN score；需要 Telegram bot 配置，安全邊界需自行評估
- **成熟度：** ⏳ 新興

#### Workweave Router：成本感知嵌入式模型路由（2026-06-27）

- **核心模式：** 在 Claude Code / Codex / Cursor 工作流中嵌入智能路由層，依請求難度自動選擇最佳模型；主要動機是解決 Opus 4.7 成本暴增問題，透過自動降階讓簡單任務走低成本模型（[GitHub](https://github.com/workweave/router)；HN score 181）
- **訊號強度：** HN 181 為本週社群工具中最高分，有公開 repo，採用訊號明確
- **與既有模式的差異：** Dragoman（2026-05-13）採用顯式規則路由；Workweave 主打隱式難度評估，無需手動設定路由規則；多模型路由從「手動策略」走向「自動決策」
- **注意事項：** 路由判斷依據未公開技術細節；「最佳模型」的定義由路由器自身決定，存在黑盒風險（推論）

#### Mac Mini M4 無人監督自主 Agent 完整部署方案（2026-06-27）

- **核心模式：** 將 Claude Code 配置為全自主 agent 在 Mac Mini M4 上執行無人監督排程任務，涵蓋事件觸發、自動 commit、完整閉環（[dev.to](https://dev.to/clawlabs/how-to-run-claude-code-as-an-autonomous-agent-on-a-mac-mini-3ld1)）
- **與既有模式的差異：** 既有「Agent 持續運作架構」（2026-05-03）偏向架構設計原則；此方案提供 Mac Mini M4 的具體配置步驟，是首個以消費級硬體為目標的完整無人監督部署指南
- **適用場景：** 個人或小型團隊的夜間自動化任務、CI 替代方案、定期維護工作流

#### Read-Only Reviewer Agent：無編輯權限的對立審查者（2026-06-26）

- **核心模式：** 主 agent 負責撰寫程式碼，reviewer agent 只能讀取、不能編輯；「無編輯權限」是設計的核心約束，保持審查者的對立性，能捕捉主 agent 放過的問題
- **實作方向：**
  - 主 agent 完成一個任務單元後，呼叫 reviewer agent 讀取變更
  - reviewer agent 不持有任何編輯工具（write/edit），強制其只輸出審查意見
  - 主 agent 收到意見後決定是否採納，維持決策責任歸屬清晰
- **解決的問題：** 若 reviewer 也能編輯，會傾向直接修改而非提供批評意見；權限約束使「對立性」可持續，避免 reviewer 降格為第二個 implementer
- **設計分層：** 此模式是「對抗性審查設計（做法 A）」的權限約束強化版；前者著重審查者讀取真實 codebase，本模式著重工具範圍限制確保對立性可持續
- **成熟度：** ⏳ 新興
- **來源：** ["Read-Only Reviewer Agents Catch What Your Main Agent Waves Through"](https://dev.to/greymothjp/read-only-reviewer-agents-catch-what-your-main-agent-waves-through-3ggc)（dev.to，06-26）
- **相關工具（HN 4）：** Verity（verity.md）——在 agent run 後自動執行審查並修復不安全代碼，定位為「自愈層」而非「審查層」；HN score 4，修復準確率無獨立驗證，附記待觀察。

#### Repo-as-Memory / Stop Using the Model as Your Memory（2026-06-26）

- **核心模式：** 框架提出「模型不保存狀態，repo 才是記憶體；模型是工作者（worker）」——已確定的決策應外化到 repo（CLAUDE.md、spec 檔、ADR），而非依賴模型在對話中記住
- **實作方向：**
  - 凡「已決定的事情」（架構選擇、技術約束、命名規則）立即寫入 repo 的指定檔案
  - 不依賴模型跨 session 記憶既有決策；每個 session 從 repo 注入確定性 context
  - 將此框架視為 Claude Code 許多架構決策的底層推論依據
- **解決的問題：** 依賴模型記住已決定的事情，會導致模型在後續 session 重做已解決問題、忽略既有約束；context 腐蝕的根源之一
- **設計分層（推論）：** 此框架統一解釋了 CLAUDE.md、`/specs` 目錄、ADR 等多種已有模式的共同動機——「repo 即記憶體」是這些實踐背後的底層哲學
- **成熟度：** ⚡ 活躍
- **來源：** ["Your Repo Is the Memory, Your Model Is the Worker"](https://dev.to/greymothjp/your-repo-is-the-memory-your-model-is-the-worker-3e09)（dev.to，06-26）；["Stop Using the Model as Your Memory"](https://dev.to/greymothjp/stop-using-the-model-as-your-memory-4nbi)（dev.to，06-26）

#### Just-in-Time @-file Retrieval：避免預先加載所有檔案（2026-06-26）

- **核心模式（反模式揭露）：** 預先 @-mention 所有「可能」用到的檔案是反模式，導致 session 上下文過重退化（context rot）；正確做法是「即時取回（just-in-time retrieval）」——只在需要時才取回相關檔案
- **實作方向：**
  - 不要在 session 開始時一次性載入所有可能相關的檔案
  - 讓 Claude 在執行任務過程中根據需要主動請求或取回檔案
  - 搭配 CLAUDE.md 描述 codebase 結構（目錄索引），而非直接注入所有原始碼
- **解決的問題：** 預先加載造成 context window 過早飽和，早期注入的約束被後來的內容稀釋；使用者分享切換後顯著改善
- **成熟度：** ⚡ 活躍
- **來源：** [Reddit r/ClaudeAI 討論](https://www.reddit.com/r/ClaudeAI/comments/1ug70ov/preloading_files_to_be_safe_was_quietly_rotting/)（06-26）

#### Personas vs Tool-Scoping：Multi-Agent 設計選擇（2026-06-26）

- **核心模式：** Multi-agent 設計的兩條路線——角色導向（Personas：CEO / EM / QA 分工）vs 工具範圍限制（Tool-scoping：每個 agent 只掛載其職責所需的工具）；作者選擇後者
- **實作方向（工具範圍限制）：**
  - 每個 agent 的工具清單對應其實際責任範圍（reviewer 不掛 write 工具、部署 agent 不掛 codebase 讀取工具）
  - 工具範圍限制比角色描述更可靠：模型可以忽略「你是 QA」的身份描述，但無法呼叫未掛載的工具
  - 角色（persona）可作為輔助提示，但邊界守護應依賴工具範圍，不是角色描述
- **設計分層：** 此選擇與「Read-Only Reviewer Agent」模式形成互補——前者是工具範圍限制的具體應用，本模式提供設計框架層的對比分析
- **成熟度：** ⏳ 新興
- **來源：** ["Personas vs. Tool-scoping: Where I Landed Differently from gstack"](https://dev.to/greymothjp/personas-vs-tool-scoping-where-i-landed-differently-from-gstack-gld)（dev.to，06-26）

#### 批量 OSS Bug 修復：識別相同形狀的 Bug（2026-06-26）

- **核心模式：** 一天內向多個知名開源專案（zod、NestJS、Fastify、Scrapy、Pygments 等）提交約 28 個 PR，核心技術是「識別相同形狀的 bug」後批量複製修復策略
- **實作方向：**
  - 先識別一類 bug 的「形狀」（觸發條件、影響範圍、修復模式）
  - 使用 Claude Code 跨 repo 套用相同的修復邏輯，一天內完成大量 PR 提交
  - 適合於標準化的程式庫缺陷（型別處理、邊界條件、錯誤處理路徑等）
- **解決的問題：** 開源貢獻的高摩擦成本（理解 codebase、修復、測試、提交）可透過「批量化相同形狀修復」大幅攤薄
- **成熟度：** ⏳ 新興
- **來源：** ["I Found 30 Mergeable OSS Bugs in a Day: They Were All the Same Shape"](https://dev.to/greymothjp/i-found-30-mergeable-oss-bugs-in-a-day-they-were-all-the-same-shape-5c86)（dev.to，06-26）

#### 20 個 Claude Code 並行 Instance 的崩潰原因與對策（2026-06-26）

- **核心模式：** 從 4 個並行 agent 擴展到 20 個時的崩潰分析；主要崩潰原因包括：共享資源競爭（git lock、資料庫連線）、context 洩漏至鄰近 agent、缺乏協調層的任務分派
- **實作方向：**
  - 每個 agent 分配獨立 git worktree，完全隔離檔案系統操作
  - 設計明確的 orchestrator 層負責任務分派與結果彙整，避免 agent 間直接通訊
  - 從小規模（4 個）漸進擴展，每次倍增時測試協調機制是否持續有效
- **成熟度：** ⏳ 新興
- **來源：** ["Why 20 Claude Code Instances Break Down and What to Do"](https://dev.to/jcamarate/why-20-claude-code-instances-break-down-and-what-to-do-2i5j)（dev.to，06-26）

#### 任務開始前先 Interview：讓 Claude Code 問問題再動手（2026-06-25）

- **核心模式：** 在正式開始任何 agentic coding 任務前，強制 Claude Code 先向使用者提問澄清需求，確認方向後才開始執行；避免「方向錯誤」這個 agentic coding 中最昂貴的失誤
- **實作方向：**
  - 在 CLAUDE.md 或任務 prompt 的開頭指示 Claude：「在開始任何實作之前，先問我 3–5 個關鍵問題」
  - 問題應覆蓋：目標邊界、技術偏好、現有限制、成功條件
  - 收到完整回答後再啟動 agentic 工作流
- **解決的問題：** Agentic coding 的最大成本不是 token，而是方向錯誤後的回滾重來；早期澄清可大幅縮短無效執行時間
- **設計分層（推論）：** 此模式是「規格驅動開發」的最小化實作——對話式 spec 收集取代書面文件，適合輕量任務
  - **進階規格格式（無 HN 分數）：** ISO/IEC/IEEE 29148 SRS 格式（The system shall [action] [condition] [measurable criteria]）可作為 Interview 收集需求後的書面化框架；適合大型任務，對非技術 PM 門檻較高（Reddit r/ClaudeAI，06-22）。
- **注意事項：** 過度提問會拖慢節奏；適用於需求模糊或跨多檔案變更的任務，簡單單一任務不必強制執行
- **訊號：** 單一經驗談，無機制驗證，待社群佐證
- **來源：** ["I Made Claude Code Interview Me Before Writing Code"](https://dev.to/florian_ilia/i-made-claude-code-interview-me-before-it-writes-any-code-2p7f)（dev.to，Florian Ilia，06-25）

#### 對抗性審查設計：計畫階段 vs 程式碼完成後（兩種做法對照）（2026-05-12 / 2026-06-25）

- **共同目標：** 引入對抗性角色，打破 LLM 的樂觀偏差（affirmative bias）——Claude 面對模糊規格時傾向以最少衝突的方式解讀任務，導致靜默失敗（silent failure）；單一 Claude 實例自審自批無法有效揭露問題
- **做法 A — 計畫前審查（2026-06-25，Adversarial Claude Reviewer）：**
  - Agent A（實作者）提出實作計畫
  - Agent B（審查者）實際讀取真實 codebase，針對計畫提出具體反例、邊界案例與風險點（而非基於抽象描述做樂觀假設）
  - 計畫須通過審查者的挑戰後，實作者才開始執行；可設定輪數（如 2 輪）後由 orchestrator 裁定
  - 與 Aharness（FSM 強制流程）結合可使對抗輪次強制執行
  - **來源：** ["I Built a Multi-agent Loop Where an Adversarial Claude Reviewer Reads Your Actual Codebase Before Approving Plans"](https://dev.to/execute25/i-built-a-multi-agent-loop-where-an-adversarial-claude-reviewer-reads-your-actual-codebase-before-2d8n)（dev.to，06-24）
- **做法 B — 程式碼後審查（2026-05-12）：**
  - 第一個 Claude 負責起草任務 kickoff 文件；第二個 Claude 扮演批評者，事先挑毛病（指出可能失敗的場景、模糊假設、潛在依賴衝突）
  - 執行前先讓兩個 Claude 達成共識；作者追蹤六個生產專案後報告此工作流顯著降低執行後的靜默失敗率，特別是在長時間任務和規格不完整的場景
  - 與 agent-order（Codex + Claude 各自獨立寫 PRD 再互相批判）類似概念，但此做法聚焦同一模型的雙實例角色分工（起草者 vs 批評者）
- **比較：** 做法 A 防止問題在設計階段產生（審查者讀取真實 codebase 是關鍵差異）；做法 B 在計畫草稿階段捕捉模糊假設；兩者可串接使用——先以做法 B 收斂規格再以做法 A 驗證實作計畫
- **共同注意事項：** 審查者提示詞設計是核心難點；需校準「挑戰強度」避免過度拒絕所有計畫

#### Pre-completion Hook：防止 Claude Code 以模糊語句提前結束任務（2026-06-25）

- **核心模式：** 設置 pre-completion hook，偵測 Claude Code 輸出中的模糊結束語句（如「say the word」、「separate fix」、「if it ever bites」），攔截並要求真正完成任務後再結束
- **量化數據：** 作者報告每日實際觸發數十次，顯示此類模糊結束行為在日常使用中頻率極高
- **實作方向：**
  - 設定 Stop Hook（或 pre-completion hook）掃描最後一輪 Claude 輸出
  - 維護模糊結束語句的 pattern list（「if this ever becomes a problem」、「a separate task」、「let me know if」等）
  - 偵測到 pattern 時，返回 non-zero exit code，強制 Claude 繼續執行而非結束（2026-09-23 註：官方語意是 Stop hook 要 exit 2 才會阻止停下，其他非零不擋，見 [[topics/community-pattern-trends]] 趨勢一）
  - 可搭配 Stop Hook 要求可驗證完成證明（測試通過、檔案存在等）
- **解決的問題：** Claude Code 的「提前結束」anti-pattern——用「讓我知道如果…」代替真正解決問題；在長任務中尤其常見，因為 Claude 在接近 context limit 時傾向「延後處理」
- **與既有模式的關係：** 呼應「Hooks 強制執行取代 CLAUDE.md 規則」的核心原則；是 Stop Hook 強制完成驗證的具體實作案例
- **注意事項：** 需持續維護 pattern list；部分「延後」可能確實合理（真正範疇外的問題），需設計豁免機制
- **來源：** ["I Made a Claude Code Hook That Ensures the Whole Task Is Completed"](https://www.reddit.com/r/ClaudeAI/comments/1uf9ubb/i_made_a_claude_code_hook_that_ensures_the_whole/)（Reddit r/ClaudeAI，06-25）

#### Repo 慣例注入 Plugin：讓 Claude Code 在編輯前自動了解 codebase 風格（2026-06-25）

- **核心模式：** Plugin 靜態分析 repo，萃取 coding convention（import 庫選擇、命名風格、檔案結構），並在每次編輯操作前自動注入相關 context，讓 Claude Code 從「陌生」變「熟悉」
- **支援語言：** TypeScript、Ruby、Python（已確認）
- **實作方向：**
  - Plugin 分析 repo 現有程式碼，提取一致性規則（例如：此 repo 使用 `axios` 而非 `fetch`；目錄結構模式）
  - 在 Claude Code 每次 Edit/Write 工具呼叫前，注入對應的 context snippet
  - 可設定「慣例置信度閾值」，只注入有足夠樣本支撐的規則
- **解決的問題：** Claude Code 在不熟悉的 codebase 中常選錯 library、命名不一致、忽略既有模式；CLAUDE.md 手動維護負擔高且容易過時；此 plugin 讓慣例提取自動化
- **與既有模式的關係：** 補充「Plugin / MCP 整合」類別，是 CLAUDE.md 管理的自動化替代方案；與「Repo-context injection」思路一致，但更細粒度
- **注意事項：** 靜態分析可能誤判過渡期程式碼（既有程式碼中的 legacy 模式）；注入過多 context 反而增加 token 成本
- **來源：** ["Made a Claude Code Plugin That Learns Your Repo's Coding Conventions"](https://www.reddit.com/r/ClaudeAI/comments/1uf9u9d/made_a_claude_code_plugin_that_learns_your_repos/)（Reddit r/ClaudeAI，06-25）

#### Multi-model Pipeline：Claude + Codex + ChatGPT 三角色明確分工（2026-06-25）

- **核心模式：** 三模型各司其職：Claude Code 負責架構規劃與複雜推理；Codex 自主建功能（autonomous feature building）；ChatGPT 處理快速網路查詢（quick web lookup）；模型間有明確交接協定
- **實作方向：**
  - 定義每個模型的「職責範圍」與「移交條件」（handoff trigger）
  - Claude Code 作為 orchestrator，決定哪些子任務交給 Codex 或 ChatGPT
  - 交接時傳遞結構化的任務摘要（非完整 context），控制 token 成本
  - 建立統一的輸出格式，讓各模型產出可直接被下游消費
- **解決的問題：** 單一模型在所有任務上均衡表現的假設失效；不同模型在不同任務上有能力差異，混用可提升整體效能並降低成本
- **與既有模式的關係：** 延伸「多 LLM 協作架構哲學」（270+ 分歧日誌）與「cc-fleet orchestrator 模式」；本案例提供三模型的具體角色定義，比既有討論更具操作性
- **注意事項：** 多模型 pipeline 的測試與除錯複雜度顯著高於單模型；跨廠商模型的 prompt 格式差異需要逐一適配；成本追蹤需跨平台整合
- **來源：** ["I Run Claude, Codex, and ChatGPT in a Single Pipeline"](https://www.reddit.com/r/ClaudeAI/comments/1uf9n1r/i_run_claude_codex_and_chatgpt_in_a_single/)（Reddit r/ClaudeAI，06-25）

#### Multi-agent 工作流轉型指南：從「單一提示反覆法」到真正並行工作流（2026-06-24）

- **核心模式：** 多 agent 並行工作的根本前提是每個 agent 擁有獨立的工作空間（worktree 或容器），否則代理間互相覆蓋導致工作流崩潰
- **實作方向：**
  - 為每個並行 agent 分配獨立 git worktree 或容器，避免共享工作目錄
  - 從「單一提示 → 等待 → 調整」的線性迴圈，重構為「任務分解 → 並行派發 → 彙整驗證」的多 agent 流程
  - 任務邊界定義先於 agent 派發：各 agent 的輸入/輸出契約需明確，避免介面漂移
- **解決的問題：** 「用 AI 當 autocomplete」的舊範式在複雜任務中的瓶頸；AI agent 排隊等待造成的效能損耗
- **補充發現（Vibe coding under constraint）：** 在 Lean 4 嚴格型別系統下進行 vibe coding 的實測顯示，AI 的主要盲點是資源限制（記憶體、檔案描述符），而非邏輯錯誤——型別系統的強制約束反而填補了 AI 的邏輯漏洞
- **注意事項：** 工作空間隔離帶來額外的協調成本；需設計跨 agent 的結果彙整機制
- **來源：** ["Stop Using AI Like Autocomplete: A Developer's Guide to Multi-Agent Workflows"](https://dev.to/harshdeepsingh13/stop-using-ai-like-autocomplete-a-developers-guide-to-multi-agent-workflows-c1k)（dev.to）；["Want AI to Work in Parallel? First Give Each One Its Own Workspace"](https://dev.to/kanfu-panda/want-ai-to-work-in-parallel-first-give-each-one-its-own-workspace-40ch)（dev.to）；["Vibe Coding under Constraint"](https://ngrislain.github.io/projects/2026-6-22-vibe-under-constraint/)（HN）

#### Aharness：有限狀態機強制 Agent 工作流狀態轉換（2026-06-23）

- **核心模式：** 以有限狀態機（FSM）定義 AI agent 工作流，強制狀態轉換路徑，防止 process drift；agent 只能依照預定義的狀態圖移動，不可跳過或自行繞過中間狀態
- **實作方向：**
  - 以 TypeScript 定義狀態節點、轉換條件與觸發動作
  - 每個狀態對應明確的 AI agent 動作集合，狀態之外的動作被拒絕
  - 轉換條件可設為同步驗證（確認前一步驟完成）或非同步事件驅動
- **解決的問題：** AI agent 在多步驟工作流中「漂移」——跳步、重複、或在無明確終止條件時無限循環；長 session 中 agent 逐漸偏離初始設計路徑
- **與既有模式的關係：** 與 ANMA 架構邊界合約互補——ANMA 約束代碼生成邊界，Aharness 約束執行流程邊界；比 Loop Engineering 哲學更進一步，從「設計 loop」進化到「強制 loop 路徑」
- **注意事項：** HN score 4，社群曝光度早期；FSM 定義本身需維護成本；過度複雜的狀態圖可能成為新型設定負債**待觀察（2026-06-28）：** HN 4，FSM 概念有差異化但社群驗證度低，2026-09-26 前無後續跟進將縮減為附記。
- **來源：** Aharness（github.com/Alfredvc/aharness，HN score 4，06-23）

#### Compact Memory：解決 AI Agent O(N²) Context Token 浪費（2026-06-23）

- **核心模式：** 以「緊湊記憶（compact memory）」取代每輪重送完整 transcript 的傳統做法；只保留當前任務所需的語意摘要，剔除冗餘歷史，將多輪 agent 的額外 context token 消耗從 O(N²) 降至接近 O(N)
- **量化數據：** dev.to 基準測試：多數 AI agent 每輪重送完整 transcript，在多輪任務造成 62.8%–85.9% 額外 context token；compact memory 方案可顯著削減此開銷（附可執行 benchmark）
- **實作方向：**
  - 每輪 agent 行動後，提取並壓縮關鍵狀態（已完成步驟、待辦項目、關鍵決策）為摘要
  - 下一輪以摘要取代完整歷史作為 context 輸入
  - 保留「最近 N 輪」原始內容以維持短期連貫性，更早的歷史則壓縮
- **解決的問題：** 傳統 agent loop 設計將全量 transcript 傳遞，隨輪數增加 token 成本呈平方增長；大型多輪任務中成本不可控
- **與既有模式的關係：** 呼應 Context Rot 修復五法中的「壓縮歷史」策略；比 /compact 指令更系統化，可程式化控制壓縮時機與粒度
- **注意事項：** 摘要過於激進可能造成語意失真，需設計摘要品質驗證機制；🔎 **查無官方**（標 2026-08-10｜查 compact memory、context token｜複 2026-11-24）｜**大規模驗證**：已查證（2026-08-13，複查 2026-10-24 結論不變）原作者（dev.to/saihmadmin）該篇 benchmark 未見獨立第三方重現或引用，僅查得他人針對同類「agent loop token 呈平方增長」問題的獨立分析（如壓縮排程可省 22.7% token、SWE-bench 情境；本輪另查得該現象已是多方部落格廣泛討論的通用問題，如 Fireworks AI、Augment Code 等文章均獨立描述相同的 O(N²) 上下文累積機制），仍非本篇 benchmark 數字本身的驗證
- **來源：** "The Hidden O(N²) Tax in AI Agent Loops: Measured with a Benchmark You Can Run"（dev.to/saihmadmin，06-23）

#### Hooks 強制執行取代 CLAUDE.md 規則：從建議層到強制層（2026-06-23）

- **核心模式：** 將「必須執行」的規則從 CLAUDE.md 文字建議層，遷移至 hooks 程序強制層；CLAUDE.md 保留偏好、風格與上下文描述，hooks 接管不可違背的操作邊界
- **實作方向：**
  - 識別 CLAUDE.md 中哪些規則是「LLM 偶爾遵守」（適合保留在 CLAUDE.md），哪些是「必須 100% 執行」（遷移至 hooks）
  - 具體 hooks 遷移案例：
    - deploy 腳本保護：PreToolUse hook 攔截部署命令
    - migration 資料夾防寫：文件系統操作前驗證路徑
    - formatter 強制：PostToolUse hook 在代碼寫入後自動執行
  - 使用 hook exit code 精細控制：Block（拒絕）/ Modify（修改後放行）/ Allow（放行）
- **解決的問題：** CLAUDE.md 規則的機率性遵守；規則越多、遵守率越低的「規則熵增」問題（參考 CLAUDE.md 精簡 296→142 行品質反升實證）
- **量化佐證：** ANMA 使用 hooks + contracts 達到 0/20 架構違規（vs 無約束時 13/19 違規）
- **設計分層（推論）：** CLAUDE.md = 知識與偏好（LLM 自主判斷）；Hooks = 邊界強制（程序保證）
- **來源：** "I stopped writing rules in CLAUDE.md and started writing hooks"（Reddit r/ClaudeAI，06-22）；ANMA（github.com/anma-labs/anma，HN score 3，06-22）

#### ANMA 架構邊界合約：讓便宜模型也能守規的強制機制（2026-06-22）

- **核心模式：** 以 YAML 合約（contracts）明確定義架構邊界，搭配 CLAUDE.md 與 Hooks 強制驗證；使 Haiku 4.5 等低成本模型在嚴格規則下也能正確運作，無需昂貴旗艦模型
- **實作方向：**
  - 在 `.anma/contracts/` 下定義 YAML 格式的架構規則（如「禁止直接呼叫資料庫、必須透過 Repository 層」）
  - 將合約規則注入 CLAUDE.md，使 AI 知曉邊界
  - 以 Pre-tool Hook 或 PostToolUse Hook 攔截違規行為，阻止代碼寫入
- **量化數據：** 無 ANMA 時 13/19 測試案例違反架構規則；有 ANMA 後 0/20 違規（來源測試）
- **解決的問題：** AI coding agent 在追求速度時系統性地繞過架構約束；CLAUDE.md 建議層無法阻止 agent 的快捷路徑行為
- **適用場景：** 有明確分層架構（Clean Architecture、DDD）的企業級專案；需要讓成本較低的模型參與生產代碼生成的場景
- **注意事項：** HN score 3，社群接受度尚早期；YAML 合約需與實際架構同步維護，否則成為新型設定負債
- **來源：** Show HN: ANMA, boundary contracts for cheaper AI coding agents（github.com/anma-labs/anma，HN score 3，06-22）
- **相關視角（HN 2）：** "I Built an MCP Server in 200 Lines of Go"（medium.com/dev-genius）——將 MCP endpoint 視為 AI 時代的 API contract，200 行 Go 示範最小實作；核心「合約優先」概念已由 ANMA 覆蓋。

#### 平行 Agent 模式：串行 vs 並行工作流效能差距（2026-06-21）

- **核心模式：** 將 agent 工作流從串行（一次做一件事）重構為並行（同時執行多個獨立子任務），可顯著提升整體吞吐量並縮短等待時間
- **實作方向：**
  - 識別任務相依圖（DAG），找出可平行執行的分支（如：同時搜尋多個資料來源、同時執行多份測試）
  - 使用 Sub-agent 或 Multi-agent 架構分派平行工作，各 agent 擁有獨立 context 避免干擾
  - Orchestrator agent 負責合併各子 agent 結果，並處理衝突與整合邏輯
- **解決的問題：** LLM 在串行工作流中的「等待」成本高昂——一個 agent 等待 API 回應或 IO 操作時，整個流程停滯；並行化可將等待時間轉為有效工作
- **適用場景：** 多資料來源研究任務、並行測試執行、獨立模組同步開發；不適合強相依的線性任務（後一步需要前一步輸出）
- **注意事項：** 並行 sub-agent 各自消耗 token；需估算並行成本是否優於串行節省的時間；cc-fleet 模式（廉價模型執行、Opus 設計）可降低並行成本
- **來源：** dev.to/kanfu-panda（2026-06-21）；cc-fleet（HN score 3）

#### Agent Loop 事件驅動：以觸發條件取代 sleep 輪詢（2026-06-21）

- **核心模式：** Agent loop 不應無條件 sleep 等待，而應改用事件驅動（event-driven）設計——只在有實際工作時才喚醒 agent，避免 5 分鐘以上的定期 sleep 帶來的 token 浪費與 context 過期問題
- **實作方向：**
  - 以佇列（queue）、webhook、檔案監聽或 diff 偵測作為喚醒條件，取代 `sleep(300)`
  - 若條件不成立，agent 直接退出或等待訊號，不進入 Claude 呼叫
  - 搭配 Stop Hook 設計明確的完成條件，防止 loop 無限運行
- **解決的問題：** `sleep 5 分鐘` 後喚醒仍需重建 context，且消耗 token 確認「是否有工作」；長期 idle 的 agent 累積大量「確認無工作」的 token 費用
- **適用場景：** PR review bot、CI/CD 監聽型 agent、定時輪詢類自動化任務；不適合需即時互動的對話型 session
- **與既有模式的關係：** 延伸自 Loop Engineering 模式（2026-06-19），強調「觸發條件設計」是 loop 品質的關鍵
- **來源：** dev.to/mjmirza "Stop Sleeping Your Agent Loop"（2026-06-21）

#### MCP Server 信任邊界審查：連接 MCP 即擴大攻擊面（2026-06-21）

- **核心模式：** 連接 MCP Server 給 agent 賦予「手」的同時，也給陌生人開了一扇門；每個 MCP 連接都需要明確的信任評估，而非預設信任
- **實作方向：**
  - 最小掛載原則：只掛載當前任務需要的 MCP，任務結束後移除
  - 審查 MCP Server 來源：優先使用官方或有公開稽核的 server；自建 server 需限制執行範圍
  - 隔離敏感操作：涉及檔案系統、網路請求、程式碼執行的 MCP，需明確限制 agent 可觸發的操作範圍
  - 搭配 Pre-tool Hook 驗證：在 MCP 工具呼叫前執行安全檢查（參考 Hooks 強制執行機制模式）
- **解決的問題：** MCP 連接帶來的攻擊面包括：惡意 MCP server 注入指令、MCP tool 被提示注入利用（如 Agentjacking/Sentry DSN 攻擊向量）、意外觸發高風險操作
- **適用場景：** 所有使用 MCP 工具的 Claude Code 工作流，尤其是有網路請求或系統寫入權限的情境
- **注意事項：** MCP context bloat（9 個 server = 38k token 冷啟動）是效能問題；信任邊界是安全問題——兩者都要分別處理
- **來源：** dev.to/rapls "Connecting an MCP server gives your agent hands..."（2026-06-21）

#### CLAUDE.md 規則總量上限：每新規則必刪一條（2026-06-20）

- **核心模式：** 對 CLAUDE.md 規則數量設定硬上限，每新增一條必須主動刪除一條舊規則，防止設定熵增（configuration entropy）
- **實作方向：**
  - 設定個人上限（如 15 條）並在新增前審視現有規則是否仍有效
  - 評估問：「這條規則最後一次真正影響 agent 行為是什麼時候？」無答案則候選刪除
  - 搭配版本控制，刪除規則前 commit 保留歷史
- **解決的問題：** 規則堆積後 agent 遵守率下降；過長的 CLAUDE.md 稀釋每條指令的有效性（「296→142 行品質反升」社群實證）
- **適用場景：** 個人長期維護的 Claude Code 工作環境；不適合需要頻繁增加領域規則的專案型使用（上限設定應因人而異）
- **來源：** dev.to/mjmirza（2026-06-20）

#### Context 裁剪 Tool Output 策略（2026-06-20）

- **核心模式：** 解決 Claude Code 長 session 退化的關鍵不是「加更多 context」，而是主動裁剪 tool output，防止 context 腐蝕（context rot）
- **實作方向：**
  - 限制工具輸出長度（截斷或摘要化 tool 回應，而非全量塞入 context）
  - 分 session 隔離不同任務，避免無關 context 跨任務污染
  - 任務重置前先保存關鍵摘要，再開新 session
  - 壓縮對話歷史：以摘要替代原始對話流
- **解決的問題：** 「Claude 越用越笨」現象；3 小時以上任務中途失憶、計劃漂移
- **適用場景：** 長 session 的 agentic 任務、多工具協同工作流、CI/CD 自動化 agent
- **注意：** 與 spec-driven development 結合效果更好——先有規格文件，再讓 agent 在精簡 context 下執行（dev.to/kenimo49；Reddit r/ClaudeAI）
- **大型 Repo 優化（HN 9）：** Git Lazy Mount（github.com/mohsen1/git-lazy-mount）——AI session 按需 fetch 大型 repo，附 sgrep 繞過全量 grep；HN score 9，適用 1GB+ monorepo；🔎 **查無官方**（標 2026-08-10｜查 git-lazy-mount、monorepo｜複 2026-11-24）｜**採用訊號**：已查證（2026-08-13，GitHub API；複查 2026-10-24 結論不變）repo 現況星數 18、forks 2（2026-10-24 GitHub 頁面；較 08-13 的 15 星僅微增 3），規模極小，尚無擴散跡象，news 亦無後續報導。

#### Loop Engineering：條件觸發的 Claude 執行設計（2026-06-19，更新 2026-06-20）

- **核心模式：** 不讓 Claude 持續輪詢，而是設計「只在有實際工作時才觸發」的執行迴圈；解決 agent idle 時浪費 token 與上下文的問題
- **實作方向：** 在 loop 入口加入工作偵測條件（如佇列非空、事件觸發、diff 存在），條件不成立時 agent 直接 sleep 或退出，不進入 Claude 呼叫
- **具體工作流抽象（2026-06-20 補充）：** Boris Cherny 名言「我不再 prompt Claude，我寫 loop 讓 loop 去 prompt」的完整拆解——PR review、測試、push 等可拆解為觸發條件 + 執行步驟 + 結果驗證三段 loop；「設計 loop」取代「設計 prompt」是哲學升級（techstackups.com guide）
- **適用場景：** CI/CD 監聽型 agent、PR review bot、定時輪詢類任務；不適合需即時響應的互動式 session
- **與既有模式的關係：** 延伸自 Boris Cherny「Loops 是未來」論述，但強調「有意義的迴圈」而非無條件輪轉（Reddit r/ClaudeAI）

#### Self-rewriting CRM：AI agent 驅動的自我重構應用架構（2026-06-19）

- **核心模式：** 應用系統以 AI agent 為改寫引擎，使用者以自然語言描述需求，系統動態重寫自身邏輯而無需傳統開發介入
- **具體案例：** 開發者建置的 CRM 系統，非開發者可直接描述「希望追蹤客戶最後聯繫日期」等需求，agent 自動生成並整合相應欄位與邏輯
- **架構要素：** 需要嚴格的 schema validation、rollback 機制、人工確認節點，避免 agent 修改破壞核心業務邏輯
- **限制與風險：** 適合邊界清晰的 CRUD 類功能擴充；複雜關聯邏輯或安全敏感操作不宜自動重寫（推論）（Reddit r/ClaudeAI）
- **訊號：** 單一經驗談，無機制驗證，待社群佐證

#### Spec-driven Development CLI：規格驅動開發工具鏈（2026-06-19）

- **核心模式：** 透過 CLI 工具強制要求開發者先撰寫規格文件才能執行 AI 代碼生成，以工具層約束取代文化層自律
- **工具實例：** opsx spec-driven-development-toolkit，整合 Claude Code、OpenCode、Codex，在無規格文件的情況下拒絕執行代碼生成指令
- **解決的問題：** Boris Cherny「coding is solved」後社群對 vibe coding 的反思——無規格的 AI 代碼容易偏離實際需求並累積技術債
- **注意：** 對應工具（opsx）已被 HN flagged，社群接受度尚待觀察（GitHub davidpv/opsx-spec-driven-development-toolkit）
- **訊號：** 單一經驗談，無機制驗證，待社群佐證

#### AI 工具採用漸進原則：先用最輕量的選項，證明會重複使用才上重機具（2026-06-18）

- **核心模式：** 為 AI coding agent 新增能力時，優先採用最輕量的形式——procedure file（純文字流程說明）優於 CLI 工具，CLI 工具優於更重的整合方案；只有在證明會被重複使用後，才值得投入建置較重的機制
- **協作演化案例：** 作者發布此原則後，一名留言者將其改寫為更完善的版本，作者記錄了社群協作改進規則本身的過程，呈現「規則也該被持續迭代」的示範案例
- **適用場景：** 判斷是否該為某項重複性工作寫 Skill / Hook / MCP 整合，或先用一份 procedure file 手動起步即可
- **與既有模式的關係：** 與「CLAUDE.md 規則總量上限：每新規則必刪一條」（06-20）同屬「控制 agent 配置複雜度」思路，本則聚焦「新增能力前的成本評估順序」
- **來源：** 「I published a rule for picking AI tools. A commenter rewrote it into a better one.」— dev.to / #claudecode（5 讚；依規則以內容第一手程度判斷，非讚數）
- **成熟度：** ⏳ 新興（單篇經驗談，尚待社群驗證）

#### Multi-agent 工作流

- **任務分解是核心難點**：社群詢問如何有效運用 20 個平行 Claude 實例，顯示 agentic 思維的學習曲線仍高
- **污染防止原則**：多 agent 協作時，讓各 agent 先獨立完成再互相審查，避免先看到他人答案後的收斂偏差（agent-order 的核心設計）
- **分支合併策略**：Claude Squad 以 orchestrator Claude 負責分派任務與合併 git 分支，而非讓各 agent 直接操作主分支

#### Skills 設計模式

- **觸發機制**：Skills 透過描述（description）自動觸發，適合封裝有明確情境的任務
- **知識框架化**：將外部知識（書籍、文件）轉為 skills，讓 Claude 在對話中自動引用對應框架
- **流程替代 README**：複雜設定流程包裝為 skill，比 README 更可靠且可持續維護
- **工具鏈封裝（HN 2）：** staffengineer.dev 將 OrbStack + Doppler + DigitalOcean 完整工作流封裝為 skills，強調「確定性高於靈活性」——setup 類 skill ROI 最高。

#### 模型使用策略

- **分層模型**：Sonnet 主力 + Opus 諮詢，節省約 60% 用量（未經獨立驗證）
- **推理強度 vs 安全邊界**：高推理強度不會放寬安全限制，兩者獨立控制
- ~~**Context window 縮減**：舊版模型將回退至 200k context~~（已被取代：Claude Code v2.1.197 起 Sonnet 5 為預設模型，原生 1M context window，見 [[entities/sonnet-5]]、[[entities/claude-code]]；此條目保留作為歷史記錄，不再適用）
- **嵌入式成本感知路由**（Workweave Router，2026-06-27）：依請求難度自動路由到最佳模型，無需手動規則；解決 Opus 4.7 成本暴增問題，HN score 181 為近期社群工具最高分之一

#### CLAUDE.md 設計原則

- **精簡優於詳盡**：CLAUDE.md 保持精簡（parsh 案例），以「規則」（rule）而非「建議」（suggestion）撰寫，有效減少 AI 冗余代碼與行為漂移
- **問題定義先於實作**：Relay plugin 的核心洞見 — Plan Mode 提問層級若停在「實作細節」，AI 常繞過問題本質直接動手；拉升至「為什麼這樣設計」層級效果顯著
- **人工確認節點**：EvanFlow 每步驟設有確認節點，不自動 commit；此模式在需要嚴謹品質控制的場景比全自動化更受信賴


#### API 使用模式

- **Batch API 不適合 agent**：每筆 batch 需 90–120 秒，互動式 agent 5 輪對話變成 10 分鐘等待；Batch API 僅適合後台非同步任務（offline 評估、大批量處理）
- **Prompt Cache Race Condition**：連續兩次呼叫間隔過短（< 2 秒），第二次 cache miss 機率約 40%；生產環境應在 cache-dependent 呼叫間加入延遲（見 [[entities/claude-code]]）
- **網頁抓取 token 效率**：直接傳入 HTML 有效內容佔比約 20%，轉換為乾淨 Markdown 後可節省約 80% 的 token 消耗

#### Plugin 設計模式

- **避免不必要 context 載入**：最常見反模式是在每次對話開頭載入大量無關 context，直接消耗大量 token 配額
- **5 個通用設計模式**（2026-04-28 社群整理）：觸發條件明確化、context 最小化、step 拆分、成本監測、人工確認節點
- **Scrum 工作流轉外掛**：將固定流程轉為插件的實際成本對比顯示，設計不良的插件成本可達設計良好版本的數倍
- **實體控制擴展（Reddit）：** Android Remote Control MCP 新版（r/ClaudeAI）——Claude 控制 Android 手機任意 app，新版支援 Claude.ai / WebView；無 HN 分數，Reddit 分享，適用移動端 UI 自動化測試。


#### 費用可觀測性工具（Cost Observability）

- **Grafana + Prometheus 企業監控整合**（2026-05-14）：把 Claude Code 用量視為可觀測的系統指標，以 SRE 式監控 dashboard 追蹤開發者行為數據；在官方 OpenTelemetry 底層之上建立企業級 dashboard，是目前官方尚未內建的監控整合層；企業部署 Claude Code 時的標準監控模式
- **官方趨勢觀察：** Anthropic 已提供原生 OpenTelemetry 支援作為底層（`CLAUDE_CODE_ENABLE_TELEMETRY=1`，v2.1.75，feature-radar 2026-06-03），未來官方是否會進一步提供內建 dashboard 或企業監控整合尚不明確；Grafana 子模式的長期必要性取決於官方在此方向的推進速度。

#### 知識圖譜應用

- **Leiden 社群偵測建立程式碼知識圖譜**（graphify）：26 天達 450k+ 下載、40k stars，宣稱每次查詢可減少 71 倍 token 用量；意外使用場景包括 SQL schema、Obsidian vault、學術論文，顯示知識圖譜在非純程式碼領域也有廣泛應用
- **git-backed Markdown 知識庫**（NanoBrain）：< 50ms append 延遲透過 hook 在 session 結束時更新，整合 Gmail/Google Calendar/Slack，是目前完整度最高的 AI Agent 跨工具共享知識庫方案


#### Hooks 精細化控制

- **PreToolUse 四種 exit code**：Block（阻止工具執行）、Allow（放行）、Modify（修改工具輸入後放行）、Error（視為工具執行失敗）；官方文件僅介紹基礎用法，四種 exit code 的實際差異遠超文件描述，影響攔截、允許、修改等場景的設計決策（2026-09-23 註：官方文件的 exit code 只有 exit 2 會擋；Block／Allow 這類是 JSON 回傳的決策欄位 `permissionDecision`，不是 exit code，見 [[topics/community-pattern-trends]] 趨勢一）
- **PreToolUse 是一台小型狀態機**：每次工具調用前皆可插入判斷邏輯，結合 exit code 可實現精細的工具調用治理


## 2026-05

#### Token 路由與成本優化（2026-05-02）

- **CLAUDE.md 路由規則委派低優先任務**：透過 CLAUDE.md 路由規則，將批量文件讀取、樣板生成等繁瑣任務委派給 $0.02/call 的低成本模型（如 Kimi K2.5），在不升級訂閱的前提下大幅提升 Pro 額度使用效率
- **異質模型路由的關鍵設計**：任務特性決定路由目標；對話性推理走高能力模型，批量機械性任務走低成本模型；可在同一 CLAUDE.md 用條件規則控制


#### CLAUDE.md 領域化安全規則（2026-05-03）

- **技術棧專用防護規則**：針對 Kubernetes 的 13 條 CLAUDE.md 規則，防止 Claude 產出 latest tag 使用、缺少資源限制、過度授予 cluster-admin 等高風險配置；顯示 CLAUDE.md 已從通用指令發展至特定技術棧的系統性安全防護框架
- **可複用安全規則庫**：K8s 規則的整理模式可推廣至其他高風險領域（資料庫操作、IaC 配置、CI/CD 管線），將領域知識轉為 CLAUDE.md 規則是安全工程化的新思路


#### Multi-agent CLAUDE.md 衝突防範（2026-05-05）

- **11 條多 agent CLAUDE.md 最佳實踐**：針對多個並行 Claude Code session 可能產生的衝突整理出 11 條規則，涵蓋：獨立工作區邊界定義、禁止跨 agent 直接修改共享狀態、明確指定 merge 責任的 orchestrator 角色、每個 agent 的讀/寫範圍白名單等；對已採用多 agent 工作流的開發者是即戰力指南
- **P2P 加密多 agent 聊天室**：兩位開發者各自執行本地 Claude Code session，並接入同一個 P2P 加密聊天室，讓 AI 代理互相協商前後端規劃細節，人類僅負責監督與介入；被社群視為「非正式多 agent 協作」的具體可行實作

#### Session 記憶與搜尋工具生態（2026-05-05）

- **Session 語義搜尋**（Claude-Find）：解決 `/resume` 僅支援第一條訊息或名稱篩選的痛點；每月累積數百個 session 的重度用戶可用語義搜尋定位過去決策脈絡，並注入現有 session
- **本地 RAG 持久記憶**（Memex）：本地 RAG + 離線 embedding，所有資料留存本機，以 MCP 接入，無需額外 API 金鑰；直接解決雲端 AI 記憶的隱私疑慮
> **官方趨勢觀察：** 本節原有的第三個子條目「多 session 互通（Claude Relay）」與另一節點「跨 Session 通訊插件」（`/qu`／`/ans` 雙向問答橋，2026-05-07）**已由官方功能完全取代**——Claude Code v2.1.224 起內建 `ListAgents` 與 `SendMessage`（官方文件 2026-08-09 確認；macOS／Linux 自該版、原生 Windows 自 v2.1.234），兩者均已移除。**未被取代的是編排層**：官方提供的是點對點訊息傳遞原語，不含依相依性自動排序高階流程（見 [[entities/claude-code]] issue #24798 與 [[topics/official-community-gap]]）。本節保留的語義搜尋與本地 RAG 兩個子條目，官方亦尚未對應。


#### Token 大量降耗策略集中出現（2026-05-05）

- **7 個降耗實務技巧**（KDNuggets）：Claude Code 高 token 成本主要來自膨脹的 context（歷史訊息、已讀檔案、工具輸出、CLAUDE.md），而非單次 prompt 長度；降耗應從 context 管理入手，而非壓縮 prompt
- **Caveman Skill 實測 65% 降耗**：評測一個宣稱可削減 65% token 的 Claude Code skill，作者實測後效果顯著，但節省幅度依使用情境差異較大；對訂閱配額告急的用戶具參考價值，與 4/29 的「兩字 prompt vs 複雜外掛」基準測試形成對照
- **企業「穴居人模式」採用確認**（2026-07-01，404 Media）：企業透過極簡輸出插件要求 AI 以最少文字回應，OpenAI、Nvidia、GitHub 開發者已採用；將 Caveman 模式從「個人省費技巧」提升至「企業級降本策略」，與 Caveman Skill 65% 實測互相印證；[報導](https://www.404media.co/companies-are-making-claude-and-codex-talk-like-cavemen-to-stop-ais-soaring-costs/)（404 Media；HN score 4）

#### Backend 替換模式（2026-05-04）

- **環境變數後端切換**（DeepClaude 模式）：僅需修改 `ANTHROPIC_BASE_URL` 等少數環境變數，即可將 Claude Code 的 agent loop 導向其他 LLM 後端（如 DeepSeek V4 Pro）；HN 543 則討論凸顯社群對低成本替換的高度需求，雖然 DeepSeek 官方文件早已說明此方法，顯示這屬於「已知但被廣泛重新發現」的功能
- **本地 LLM 無侵入切換**（claudely）：在保留 Claude Code 完整插件生態（Skills、MCP、Hooks）的前提下切換後端至 Ollama/LM Studio/llama.cpp，無需修改主配置文件，讓開發者兼得生態完整性與本地模型的低成本優勢

#### CLAUDE.md 防腐爛機制（2026-05-04）

- **CLAUDE.md「腐化」問題成為主題**：長期使用 Claude Code 後，CLAUDE.md 常出現修正過的行為再次復發、規則膨脹失焦等「腐化」現象
- **Retro Loop 機制**（Patina CLI，MIT，已上 npm）：透過「回顧循環」定期回顧並更新 AI harness 設定，移除過時規則、整合新規則，防止配置腐化
- **腐化的根本原因**：規則是否仍有效缺乏持續驗證機制；規則只增不減；修復後無回歸測試確保規則仍適用

#### Agent Context 新鮮度問題（2026-05-04）

- **長 session 中 agent 重複讀同一檔案**：Claude Code 在長工作階段中不斷重讀相同文件、不記得程式碼修改歷史，造成重複工作與上下文喪失
- **時間感知代碼庫表示層**（Memtrace）：為 codebase 建立持久的時間感知表示（time-aware representation），讓 agent 能追蹤「哪些地方改了、為什麼改」，而非每次重讀猜測；此概念直接對抗 stateless agent 的核心缺陷

#### 結構化 Agent 框架設計（2026-05-04）

- **Pilot Shell 三指令框架**：
  - `/spec`：TDD 完整流程，規格優先於實作
  - `/fix`：含複雜度自動偵測，超出標準修復路徑時自動中止，防止 agent 過度施工
  - `/prd`：需求文件生成
  - 定位在「輕量但有工程紀律」的中間地帶，兼顧自動化與人工控制

#### 本機持久化記憶架構（2026-05-08）

- **Local stack MCP 整合、39ms 檢索**：開發者分享自建本機持久化記憶層：本地向量資料庫 + MCP 整合，實現 39ms 快速檢索；同時解決每次對話從零開始，以及記憶庫成長後大量消耗 token 的雙重痛點
- **架構核心原則**：避免將全部記憶注入 context（token 消耗過高），改以語義查詢按需取回相關片段；本機方案同時解決雲端記憶的隱私疑慮，與 Memex 思路相近但強調自建可控性
- **意義**：是對 Managed Agents Dreaming 官方解法的社群自建補充，在等待官方成熟前已形成可用架構
- **輕量替代（HN 6）：** Iantha（kiloloop.com/iantha/）——純 Markdown + git 存儲，自動提取時間性任務跨 session 持久保存，無需向量 DB；HN score 6；🔎 **查無官方**（標 2026-08-10｜查 Iantha、kiloloop｜複 2026-11-24）｜**識別準確度**：已查證（2026-08-13，複查 2026-10-24 結論不變，kiloloop.com 本工具無法解析網域、公開搜尋仍無獨立報導——官方頁面 kiloloop.com/iantha/ 本身為純功能／設定說明頁，未提供準確度或第三方評測數據）公開搜尋未能定位該工具的獨立報導或後續討論，識別準確度仍無法查證。


#### Managed Agents 架構模式（2026-05-07）

- **Dreaming 記憶整合機制**：Agent 在任務間隙自動整理近期事件、萃取值得長期保留的資訊存入記憶，類似人類睡眠時的記憶鞏固；Anthropic 首次在官方架構層面解決長跑 Agent 的記憶持久性問題（對比：社群工具 Dreamer、NanoBrain 先行實現類似理念）
- **Outcomes 規格驅動執行**：規格文件（spec）成為 Agent 執行時的強制依據而非參考文件，Agent 需在完成後自我驗證輸出是否符合預定目標，是「Spec-Driven Development」原則的官方制度化；與 2026-05-02 社群整理的「規格驅動開發」趨勢相呼應
- **20 路並行子代理**：官方框架層面首次支援 20 個子代理同時執行，使 agent 任務分解（multi-agent）從社群工具（Harness、Claudette）走向官方原生支援
- **Claude Code Routines vs cron job**：Routines 與傳統 cron job 的核心差異在於 Agent 能對結果進行推理而非只執行固定指令——每晚自動摘要當天 commit、每週掃描過期依賴、每日彙整錯誤日誌趨勢等場景均已有開發者實踐


#### Git Log 作為除錯首要步驟（2026-05-07）

- **Claude Code 自動讀取 git log 除錯**：觀察到 Claude Code 在除錯任務時自動讀取 git log，以描述性 commit message（取代 "wip"、"fixed stuff"）讓 Agent 在幾秒內縮小問題範圍；此行為可透過良好 commit 習慣主動利用
- **多 session 協作技巧**：搭配 git worktree 讓多個 session 在不同分支上協作，git log 成為各 session 間共享 context 的天然媒介

#### MCP Code Execution Token 效率（2026-05-07）

- **MCP server 過多導致 context 在第一條訊息前就半滿**：大量 MCP 伺服器的靜態工具列表佔用大量 context；以 MCP code execution 取代靜態工具列表的方案，讓 Agent 動態獲取能力，兼顧擴展性與 token 效率，適合正在評估 MCP 架構規模的團隊

#### Speculative Parallelism 工作流（2026-05-06）

- **每個 agent 擁有獨立 git worktree + session + 終端機**（Claudette）：開源桌面工具讓每個 Claude Code agent 擁有完全隔離的環境，實現 speculative parallelism 工作流——多個分支可同時執行且無衝突；社群顯示已有開發者手動實踐類似做法數月，工具化使這個模式變得可複用


#### Hooks 強制執行機制（2026-05-06）

- **PostToolUse 強制執行 Claude 可能略過的步驟**：透過在 PostToolUse 等工作流節點觸發 shell 指令，可強制執行 Claude 可能「自行判斷可略過」的步驟（程式碼格式化、自動 commit、強制測試）；解決 agent 「自以為完成」的核心痛點，是比 CLAUDE.md 指令更可靠的行為約束機制
- **Hooks vs CLAUDE.md 的本質差別**：CLAUDE.md 是「建議」，模型可選擇忽略；Hooks 是「強制執行」，透過 shell 指令保證執行，適合不允許跳過的關鍵流程節點

#### CLAUDE.md 語言生態規則集爆發（2026-05-06）

- **各語言專用規則集同日密集出現**（olivia_craft + natevoss 等）：dev.to 同日出現 5+ 篇針對特定語言的 CLAUDE.md 規則集：Rails（防止 legacy 模式）、Kotlin（coroutine 安全）、Flutter/Dart（防脆弱行動端程式碼）、Scala（慣用函數式）、Modern C++（防 1998 風格）、CLI bug 除錯後整理的 4 條實戰規則；社群正在各語言生態快速建立 AI 導向開發規範
- **趨勢意義**：CLAUDE.md 語言專用化，從「通用 AI 指令框架」演進為「語言生態特定的安全防護與風格守衛工具」；產量和速度的加速預示一個社群驅動的 CLAUDE.md 規則庫生態正在成形


#### Claude Code 作為 MCP 協調中心（2026-05-06）

- **MCP Hub 模式**：將 Claude Code 作為 n8n、瀏覽器 LLM 介面等多個自動化平台的 MCP 協調中心，讓多個自動化工具統一透過 Claude Code 控制；適合需要整合多個自動化工具並統一介面的開發者，是 Claude Code 從「coding assistant」延伸為「自動化協調中心」的具體實踐

#### Self-improving Rules（2026-05-06）

- **將糾正（correction）泛化為通用規則**（claude-smart）：現有記憶體方案只存事實、無法捕捉用戶糾正；透過將糾正泛化為跨專案通用規則，解決「同樣錯誤一犯再犯」的問題；與 claude-mem 的差異在於 context footprint 更小，但是否能準確泛化糾正仍有爭議


#### PostToolUse 生產稽核日誌模式（2026-05-09）

- **企業部署的可觀測性解法**：利用 Claude Code 的 `PostToolUse` hook 在生產環境建立完整稽核日誌，逐筆記錄工具呼叫的 Bash 指令與目標 repo，解決「代理上週三下午 3 點到底執行了什麼」的可觀測性痛點
- **適用場景**：企業部署、合規要求（SOC2/ISO 27001）、事後審計，任何需要完整 agent 操作記錄的場景；可結合 re_gent（AI agent 版本控制）形成完整稽核鏈
- **實作模式**：`PostToolUse` hook 在每次工具呼叫後以 append 方式寫入日誌，記錄 timestamp、指令、目標 repo、執行結果；此為 Hooks 機制的企業生產級應用案例

#### Git Hooks 強制代碼品質（2026-05-09）

- **AGENTS.md / CLAUDE.md 中強制安裝 pre-commit / husky**：在 AGENTS.md 或 CLAUDE.md 中明確要求代理安裝並遵守 git hooks，讓 CI 層面對 AI 代理產出的程式碼進行強制品質控管
- **具體門檻**：提案設定每檔最多 600 行與 McCabe 複雜度上限 10，防止 AI 加速開發同時帶來的複雜度失控
- **關鍵原則**：代理絕不使用 `--no-verify`（除非用戶明確確認），將 git hook 從「建議」升格為「強制防線」；延續「Hooks vs CLAUDE.md 本質差別」（2026-05-06）的設計理念，將強制執行範圍延伸至版本控制邊界

#### 架構決策記錄（ADR）+ Claude Code（2026-05-09）

- **54 份 ADR 35 天**：作者在 35 天內產出 54 份架構決策記錄（ADR），主張在撰寫任何程式碼前先完成決策文件，每個功能有對應的 ADR 才開始 Claude Code 協作
- **與 Claude Code 工作流整合**：先完成 ADR 再讓 Claude Code 實作，有效降低代理方向偏移的風險；與 Mneme（repo-native ADR 注入）工具理念一致
- **方法論一脈相承**：「決策文件先於實作」與「問題定義先於實作」（Relay plugin）和「規格驅動開發」（2026-05-02）的社群共識一致，顯示 agent 工作流方法論正在走向成熟的規範化收斂

#### 本機圖資料庫降低 Session Token 成本（2026-05-10）

- **快取不跨 session 是費用主因**：每次新 session 因 prompt cache 不跨 session 需重新讀取大量相同檔案，是 pay-as-you-go 用戶 session 費用達 $6–10 的主要原因（類似 2026-05-05 的 token 降耗討論，但更聚焦 session 成本結構）
- **圖資料庫索引解法**：建立本機圖資料庫（graph database）索引整個 codebase，讓模型只讀取結構化摘要而非原始檔案；不使用 AST 或向量，而以 LLM 生成關係圖的方式具有創意，成功大幅壓低 session 費用
- **任務層級 token 預算**：Tokenyst 讓 Claude Code pay-as-you-go 用戶在任務層級設定 token 預算，每次提示後即時顯示剩餘額度與使用比例，是費用控管工具鏈的新補充

#### Multi-agent 研究調查團隊架構（2026-05-10）

- **六代理分工**：作者以六個功能各異的 agent（Scout、分析師、撰寫員等）打造「AI 企業應用案例地圖」，目前已累積逾 250 個真實案例
- **實務驗證意義**：此案例在大量 multi-agent 理論討論中提供可驗證的實務實作，展示 multi-agent 架構在知識蒐集與整理任務上的具體生產力；與 2026-05-01 的 Omar（100 agent TUI 管理）不同，聚焦在「任務驅動型 agent 分工」而非「管理介面」


#### AI Agent 語意層漂移 CI 測試（2026-05-11）

- **問題定義**：AI agent 在多日執行中可能悄悄偏離預期行為（語意層漂移 / semantic drift），傳統 CI 測試無法偵測
- **六秒 CI 測試**：作者分享如何用一個**僅需六秒**的 CI 測試偵測 agent 的語意層漂移，防止代理在不知情情況下偏離目標行為；方法論：在 CI 流程中定期對代理發送探針任務並比對輸出分布，用統計指標而非固定預期值判斷行為是否偏移
- **實踐價值**：對長期運行的 Claude Code agent 工作流（如 vibe coding loop、每日排程任務），語意漂移偵測是尚未被廣泛解決的 QA 盲點

#### 多代理 PR Review 超越官方工具（2026-05-11）

- **adamsreview 設計**：以平行子代理、多階段驗證與 JSON 持久狀態執行 PR review；每個子代理從不同角度（安全性、邏輯正確性、效能、可維護性）獨立審查，最終交叉彙整
- **作者聲稱效果**：在自測中比官方 /review、/ultrareview、CodeRabbit 及 Greptile 捕捉到更多真實 bug，同時誤報率更低；並支援與 Codex CLI 組成 ensemble review
- **生態意義**：官方 PR review 工具已存在的情況下，社群以多代理架構做出差異化，顯示 Claude Code 插件生態正走向深度定制，間接壓力測試官方工具的品質上限；需獨立驗證作者聲稱的效果

#### CLAUDE.md 記憶規則驗證技巧（2026-05-11）

- **金絲雀規則（canary rule）**：在記憶或 CLAUDE.md 中埋入特定「金絲雀指令」（如要求 Claude 在每則回應前加上特定奇特前綴），可快速驗證 Claude 是否確實載入並執行了記憶規則；若前綴未出現即可判定記憶未生效
- **直接詢問專案設定**：詢問 Claude「目前載入的專案設定內容是什麼」，可立即確認 CLAUDE.md 是否被正確解讀；搭配金絲雀規則，兩招形成 10 秒快速一致性檢查
- **適用場景**：對依賴 CLAUDE.md 或記憶系統的自動化工作流尤為重要，是社群自 CLAUDE.md candidate-context 架構揭示（2026-05-10）後催生的實用對策

#### AGENTS.md 跨工具插件簡報（2026-05-11）

- **統一配置文件**：以 AGENTS.md 作為跨工具（Claude Code、Cursor、GitHub Copilot 等）的統一插件簡報文件，讓不同 AI 工具共享相同的代理人配置說明，降低跨工具整合的設定重複成本
- **Kobiton 案例**：Kobiton 在跨工具自動化測試環境中實踐此模式，不同 AI 工具共享同一份代理配置，顯示 AGENTS.md 有潛力成為跨工具 AI 配置的業界標準
- **與 CLAUDE.md 的關係**：CLAUDE.md 是 Claude Code 專屬指令，AGENTS.md 是跨工具通用的代理簡報文件；兩者定位互補，AGENTS.md 解決的是工具綁定問題，CLAUDE.md 解決的是 Claude 特定行為調優問題

#### `/goal` Fire-and-Forget 自動化模式（2026-05-12）

- **官方新功能**：v2.1.139 推出的 `/goal` 指令代表 Claude Code 首次具備真正的 fire-and-forget 能力；用戶設定可驗證的完成條件後，每輪執行結束由一個小型快速模型判斷條件是否成立——未達成則自動開始下一輪，無需人工介入
- **適用場景邊界**：設計上適合有明確終態的長時間任務（模組遷移完成、所有測試通過、API 端點全部回應 200），不適合開放式或目標模糊的任務
- **社群反應**：Reddit 對 `/goal` 的反應熱烈，多名用戶形容這是「Claude Code 首個真正的 fire-and-forget 循環」，此版本包含 104 項變更；見 [[entities/managed-agents]]
- **Anthropic 抄自開源爭議**：部分社群成員指出 `/goal` 的概念早已在 OpenClaw 等社群工具中實現，質疑 Anthropic 是否長期觀察開源社群後直接內建功能而未給予信用，Anthropic 未回應

#### Writ 規則強制執行（Neo4j 知識圖譜 Pipeline）（2026-05-12）

- **問題**：Claude Code 常忽略 CLAUDE.md 中的規則，原因之一是 CLAUDE.md 作為 candidate-context（`<system-reminder>`）可被模型跳過；同時載入所有規則也因無關規則佔用 token 而降低精準度
- **Writ 的解法**：透過五階段 Neo4j 知識圖譜 Pipeline，在每次工具呼叫前自動擷取與當前任務語義最相關的規則子集，只注入相關規則，兼顧規則遵守率與 token 效率
- **技術架構**：以 Neo4j 儲存規則及其語義關係，每次任務啟動時依 context 做圖遍歷，找出相關規則集；比純 CLAUDE.md 文字比對更具選擇性，比全量載入更省 token
- **意義**：是「CLAUDE.md 強制執行」與「規則過多導致 token 浪費」這個雙重困境的社群工程解法，與官方 Hooks 機制（強制執行）和 CLAUDE.md（建議）的層次設計形成互補

#### 跨環境 Agent 記憶協定（ltm / Core Memory Packet）（2026-05-12）

- **現有方案的根本缺陷**：CLAUDE.md、`.cursor/rules`、AGENTS.md 等現有 agent 記憶方案均為 Markdown 文件，無法在不同編輯器、不同機器、不同 AI 模型之間攜帶和同步
- **ltm 的設計**：基於 JSON 協定（Core Memory Packet）的 Agent 記憶工具，設計上實現供應商中立的持久化記憶；Core Memory Packet 包含結構化的 agent 記憶資料（任務歷史、學習到的偏好、已知約束），可在任何支援該協定的工具間交換
- **跨環境攜帶性**：相比 Markdown 記憶方案，ltm 的 JSON 結構可被任何工具解析，不依賴特定 AI 工具的指令解讀機制
- **與其他記憶工具的定位差異**：Memex（本地 RAG）、NanoBrain（git-backed Markdown）、Dreamer（MCP → AGENTS.md 整合）均聚焦單一環境內的記憶持久化；ltm 的差異化在於跨工具、跨機器的記憶可攜性

#### 多模型路由工作流（Dragoman）（2026-05-13）

- **依問題類型路由模型**：開源 CLI 工具 Dragoman（約 800 行）讓 Claude Code 依問題類型自動路由至不同專業模型——新聞/時事查詢 → Perplexity；複雜推理 → Gemini；本機運算 → Ollama；Claude 作為整合層統整最終回答
- **4 模型並行 + 彙整**：支援四個模型同時執行相同 prompt，最後由 Claude 統整並標記分歧點；延續 Council（並行多模型）的設計理念，但聚焦 Claude Code 工作流整合而非一次性 prompt 比較
- **API 金鑰安全設計**：API 金鑰透過 1Password/Keychain 解析，完全不進入 Claude context，是 API 金鑰管理的安全最佳實踐範例
- **意義**：多模型協作架構從「實驗性」走向「工具化」；與 Token 路由策略（2026-05-02）的 CLAUDE.md 路由規則取向不同，聚焦不同工具的能力互補而非成本優化
- **相關工具（HN 1）：** cc-fleet（github.com/ethanhq/cc-fleet）——讓 Claude Code 作為 orchestrator 調度異質 LLM worker，HN score 1，採用訊號不足，附記待觀察。

#### 電話 MCP：AI 代理與實體通話整合（2026-05-13）

- **Cocall.ai 架構**：AI 代理撥打外線電話，遇到不確定的問題時自動暫停，轉回詢問使用者後再繼續通話；採用全雙工語音模型，支援 IVR 導航（按鍵選單）與電話轉接
- **人機協作模式**：不同於完全自主代理，此工具強調「遇到邊界問題暫停確認」的人機協作設計，是 Agent 操作確認節點概念在實體世界的延伸
- **意義**：是目前少見的 AI 代理從數位世界延伸至實體通話世界的案例；MCP 生態持續向現實世界操作延伸（繼 OpticOdds MCP、Cocall 等），顯示 Claude Code 生態已超出純開發工具範疇

#### Token Bloat 系統性對策（2026-05-13）

- **測試執行器輸出精簡**：Claude Code 用量限制促使開發者深入審計 context 消耗，作者聚焦測試執行器輸出，提出只保留「測試是否通過、哪項失敗、失敗位置」的精簡策略；預告這是系列文章的第一篇
- **根本問題框架化**：Token bloat 的主要來源是 context 膨脹（歷史訊息、測試輸出、工具回傳），而非 prompt 本身；系統性降耗需從 context 生命週期管理入手——此系列代表社群正在以系統化方式解決 token 效率問題，繼 token 降耗策略（2026-05-05）之後的更深度演進

#### 大規模子代理工作流實踐（2026-05-13）

- **Boris Cherny 的數千個子代理工作流**：Claude Code 創始人公開每晚讓數千個 AI 子代理執行「深度工作」的工作流，是 Managed Agents 20 路並行子代理能力在個人工作流中的極端應用，展示大規模 agentic 模式的可行邊界
- **與官方工具的正向回饋**：此工作流建立在 v2.1.140 改善的 subagent_type 匹配（大小寫不敏感）與 Agent View（統一 session 管理）基礎之上，顯示官方功能更新與社群使用案例之間的正向回饋；社群需求驗證官方功能優先序，官方工具降低社群工作流門檻
- **社群討論帶動**：被主流媒體（Business Insider、Let's Data Science）大幅報導後，社群對大規模並行代理架構的討論密度顯著提升；見 [[entities/boris-cherny]]、[[entities/managed-agents]]


#### Agent 持續運作架構（2026-05-03）

- **VPS 雙代理持續運作**：兩個 Claude Code 代理在 VPS 的 tmux session 中持續運作，自動開 PR 並發布 Discord 狀態更新，代理間可相互協調；架構概念類似「Claude Code 版 docker-compose」
- **OS 用戶隔離爆炸半徑**：每個代理使用獨立 OS 用戶，比容器化更輕量但仍能有效限制單一代理失控時的影響範圍，是 agent 架構設計的實踐案例

#### Git Worktrees 作為多 Agent 隔離原語（2026-05-23）

- **獨立工作樹隔離**：每個 Claude Code agent 運行在各自的 git worktree 中，擁有獨立的工作目錄、staged changes 和本地狀態，確保並行 agent 之間完全不互相干擾
- **比 OS 用戶更輕量**：相比雙代理 VPS 架構使用獨立 OS 用戶隔離（2026-05-03），git worktree 不需要 OS 層面的帳號管理，是更輕量的隔離原語，特別適合 CI/CD 或本機多任務場景
- **Superset 框架的底層機制**：社群工具 Superset（2026-05-23 首見）使用 git worktree 自動為每個並行 Claude Code 實例分配獨立工作區，將此模式工具化；與 FleetView 的概念類似，但聚焦在 worktree 而非 session 可見性
- **爆炸半徑最小化**：即使某個 agent 在本地 worktree 做了破壞性操作（例如誤刪文件），不影響主 branch 與其他 worktree；合併前可 review 全部 diff，強制加入人工審查節點
- **適用場景**：同時跑多個 feature branch、平行測試不同實作方案、CI 環境中不同 PR 的並行驗證

#### Framework-Specific CLAUDE.md 設計（2026-05-23）

- **框架防呆規則**：「CLAUDE.md for Svelte: 13 Rules」展示了針對單一框架（Svelte）客製化 CLAUDE.md 的方法論——明確列出「禁止使用 React 思維」（禁 JSX、禁 useState、禁 useEffect）的負面規則，防止 Claude Code 將訓練資料中 React 佔比過高的偏好帶入 Svelte 開發
- **負面規則的力量**：相比「請使用 Svelte 的 reactive statements」，「不要使用 useState」更能有效阻止 Claude Code 回退至 React 慣例；這延伸了「精簡 CLAUDE.md」（2026-04-25）的討論——精簡不只是少寫，而是寫對類型的規則
- **框架差異放大問題**：框架差距越大（例如 React → Svelte），模型產生慣性錯誤的頻率越高；框架特定 CLAUDE.md 的必要性與框架獨特性正相關
- **可複用範本化**：13 條規則格式結構化，社群可以複製並依自己的框架（Vue、Solid、HTMX）調整——這是 CLAUDE.md 最佳實踐從個人做法走向社群共享範本的跡象


### 時序流水帳（併自原社群時序頁，2026-05-01～05-22）

#### 2026-05-22
- **Spec-Driven Development 工作流（HN Show）**：多步驟生成規格（需求→程式碼分析→設計）→ 分拆子任務→每步之間**清除 context**再執行，藉此降低成本並提升 agent 表現；與 Managed Agents Outcomes 機制的「spec 作為執行依據」原則在社群層面形成呼應，是規格驅動開發在個人工作流的具體實踐
- **1 個 Claude agent 擴展為 agent 機群（5 步驟）**：作者從 AMD GitHub issue 中 Stella Laurenzo 分享的 50 代理機群運作方式得到靈感，整理出五步驟架構：任務佇列自動分配、夜間實驗可靠執行；與 agent-teamflow（9 slash commands）代表同一趨勢的兩種實作路徑
- **CLAUDE.md 自我演化現象**：作者追蹤三週後發現 Claude 在未受指示情況下自行為 CLAUDE.md 新增了 4 條規則，引發對 agent 自主性邊界的討論；與「Angular CLAUDE.md 13 條規則」（production-ready 元件指南）共同顯示 CLAUDE.md 配置已成本週社群最活躍的討論主題
- **個人 AI Agent 架構系列（CLAUDE.md 展示）**：前篇「100 個技巧」獲 9 萬次觀看，本週深入展示實際 CLAUDE.md 檔案結構，社群要求持續；顯示「完整展示 harness 設定」已是高影響力內容格式
- **零 NPM 依賴 Claude Code 插件架構**：作者分享在不依賴任何 npm 套件的情況下建構 Claude Code 插件（seo-survival-kit）的輕量化設計，強調插件架構可行的最小依賴方案

#### 2026-05-21
- **vibe-skill 委派撰碼模式（Claude 規劃 + Mistral 執行）**：開發者開源 vibe-skill，讓 Claude 負責規劃、任務分解與 diff 審查，實際撰碼委派給 Mistral Vibe；10 天 57M tokens 節省、成本降逾九成是「多模型角色分工」模式迄今最具數字說服力的實作，預示 Claude Code 生態向「Claude as orchestrator」演進
- **Claude Orchestra skill 管理框架**：社群工具 Claude Orchestra 提供多個 skill 的統一管理與版本控制框架，顯示 skill 生態從「個人使用」走向「工程化管理」的成熟跡象
- **atrium 可恢復瓦片式工作區**：macOS 應用 atrium 將 terminal、browser、task、notes 整合於可恢復的瓦片工作區，解決 session 崩潰後狀態遺失問題，是「工作流持久化」模式在桌面層的實作
- **the-knowledge-guy 知識圖譜 MCP**：開源 MCP 伺服器提供結構化知識注入，補強 /compact 後語意記憶遺失問題

#### 2026-05-20
- **engramx Skill Pack v4.0.0 token 優化實測（89.1% 減少）**：開發者在 87 個檔案（163K token）的專案中，透過 engramx Skill Pack v4.0.0 將 Claude Code 每次啟動需讀取的 token 從 163,000 降至 17,722（減少 89.1%），是目前社群最具體的「解決 session 失憶」量化案例
- **Repo 內嵌 `.claude/skills/` 架構護欄**：開發者分享將架構契約、腳手架決策樹、硬性限制寫入 `.claude/skills/` 目錄的實踐——任何人 clone repo 後 Claude Code 會自動載入，達到「架構護欄隨 repo 分發」的效果，無需額外配置
- **35 個 Claude Code Agent 協調設計**：單人工作室分享管理 35 個 Claude Code agent 協作的實踐，重點在如何以明確角色分工避免 agent 互相衝突、維持 quality gate 流程正常運作
- **Multi-agent Code Review 可靠性實測（41% 不一致率）**：讓三個 Claude Code sub-agent 審查同一個 PR，發現 41% 的評論彼此不一致，對「多 agent code review = 免費升級」的假設提出實證挑戰；建議搭配人工最終審查，不宜純依賴 multi-agent 結論
- **新工具**：TokenShield（本地 proxy 去除重複 tool_result，宣稱減少 40–70% token）、Logbox（dev log 導入 SQLite + MCP 查詢）、PrismoDev（本地掃描 context bloat 診斷工具）、claude-autopilot（多模型自動化 dev pipeline）

#### 2026-05-19
- **1000 小時 AI Coding Agent 工作流心得（人工介入節點設計）**：開發者在 1000 小時實戰後總結核心工作流：明確設置人工介入節點、主動限制 agent 自主度，避免「跨模組重構同名方法」等高破壞性錯誤；核心洞察是「把 agent 當強大工具而非獨立員工」——agent 擅長小範圍精準任務，放任大範圍自主決策才是高風險來源
- **7 步驟 AI 內容 SEO Pipeline（$0.45/篇，每天 15 分鐘）**：開發者開源以 Claude Code slash commands 串接的 7 步驟內容 SEO pipeline，每篇文章成本 $0.45、每天只需 15 分鐘，展示 AI 工作流在內容生產的具體落地數據；是目前社群分享中成本最低且有明確數字的 AI 內容生產案例
- **Android 惡意軟體逆向工程（Adafruit 案例）**：Adafruit 分享使用 Claude Code 逆向分析 Android 惡意軟體的實作案例，展示 AI 輔助資安分析在 APK 逆向場景的可行性；是繼 AliExpress 投影機惡意軟體（2026-05-18）後，連續兩日出現 AI + 資安逆向工程的案例，顯示此應用場景正在成形
- **Anthropic 跨部門 Claude Code 使用報告**：Anthropic 公開跨 10 個團隊（含法務、行銷等非技術部門）的 Claude Code 實際使用情況，是「AI coding 工具的使用範疇已超越傳統開發場景」的官方首次確認
- **新工具**：Claude Soul（跨 session 學習引擎，MCP + hooks，~200 session 後出現意外行為）、cdesktop（開源桌面整合 5 個 coding agent + 20+ 第三方模型）、InsForge（YC P26，coding agent 的開源 Heroku，直接部署後端基礎設施）

#### 2026-05-18
- **Agent 角色分工帶來 6.7 倍速度提升（3 角色拆分實測）**：開發者將單一「全能 Strategist Agent」拆分為三個專責角色後，相同 WebSearch 任務時間從 20 分鐘降至 3 分鐘（6.7 倍加速）；架構邏輯：角色專一化讓每個 agent 的 context 更精簡、指令更聚焦，是對「單一 Agent 越來越臃腫」問題的具體反向工程；可搭配 Managed Agents 20 路並行能力實現
- **多操作員 Claude Code 架構（Hub + MCP + CLI + Docker + 桌面監控）**：開發者展示企業級多操作員架構：Hub 協調層 + MCP 客戶端 + CLI + Docker 無頭工作者 + 桌面監控器，支援多人同步觀察同一 Claude Code 工作階段、跨 repo 路由子任務，且 Agent 可自行召喚更多 Agent；是目前社群分享中架構最完整的多操作員協作系統
- **速率上限前自動轉移工作流（agent-baton 模式）**：利用 Anthropic 使用量 API 預測速率上限到達時間，在觸及前主動警告並轉移進行中的工作至備用 session；解決 Claude Code 靜默中斷的長期痛點，是 `/loop` 失控事件（$6,000）後社群自發演化出的防護機制
- **Claude Cache 刷新策略：62.5 分鐘規則**：開發者推導 Claude 5 分鐘 Prompt Cache 的最佳刷新決策——「62.5 分鐘規則」說明在特定頻率下主動刷新比讓 Cache 過期更划算；對高頻 API 使用者（含 CI/CD 自動化、多 agent 協作）具有實際成本意義；見 [[entities/pricing]]
- **逆向工程 Android 惡意軟體實戰（資安研究場景）**：作者用 Claude Code 分析 AliExpress 35 美元投影機內建 Android 惡意軟體，自動回傳資料至未知域名；展示 Claude Code 在資安逆向工程領域的實際應用潛力，是繼 ESP32 Fault Injection（2026-05-12）後的第二個 Claude Code 資安研究代表案例
- **新工具**：Semble（code search 98% token 節省）、AnyFrame（微 VM Agent 沙盒）、Agetor（看板 Harness 排程器）、agent-baton（速率上限前轉移工作）、LockedIn（session 脈絡記憶插件）、Claude Usage Widget（桌面浮動 token 監控）

#### 2026-05-17
- **Claude Skills 作為 dotfiles 管理 + 子代理派生邊界探索**：開發者分享將 Claude Skills 視為個人化配置（類似 dotfiles）進行管理的心得，並記錄 skills 意外觸發子 agent 派生的實際案例；`ask_user_input_v0` 工具存在最多 3 問題 / 4 選項硬性限制導致靜默壓縮，技術社群開始系統性質疑 Skills 機制的透明度與可控性；見 [[topics/community-tech-discussions]]
- **Anthropic Generator-Evaluator 多 agent 架構實踐（12 輪對抗迭代）**：開發者仿照 Anthropic 工程部落格公布的 Generator-Evaluator 架構（靈感來自 GAN），以 Kiro CLI 進行 12 輪對抗式迭代生成行銷網站；架構要點：Planner 單次執行 → Generator ↔ Evaluator 循環，各 agent 零共享 context，對抗性循環比單輪生成顯著提升輸出品質
- **持久性自主 agent 系統工程達新高度**：開發者幾乎完全以 Claude Code 建構持久性 agent 系統，具備語義 + 情節雙重記憶、德英雙語語音對話、情緒狀態追蹤、螢幕感知、自主排程任務、即時 SaaS 生成等功能；是迄今社群分享中功能最完整的 agentic 工程作品，呼應 [[entities/boris-cherny]] 的「Loops 是未來」哲學
- **Context 管理 4 工具最佳實踐**：社群整理 Anthropic 官方 Best Practices 文件中的 4 種 context 管理工具（超越 `/clear` + `/compact` 的二元認知），提供更細緻的大型 codebase 長工作階段管理策略；在有 3–8 MB 原始碼的大型主題中，開發者開始系統性討論每任務後是否應強制 `/clear`
- **Design-to-code CSS 規格先行工作流**：前端開發者分享設計稿轉碼最佳實踐：先讓 Claude 生成完整 CSS 規格文件與設計交接文件，再執行轉碼，可有效避免「差不多就好」的設計意圖流失；此「先規格後實作」模式與規格驅動開發哲學高度一致
- **100 個 Claude + Codex 平行 session 行銷診斷**：開發者工具首發後零互動，立即同時啟動 100 個 Claude + Codex agent 進行行銷診斷，30 分鐘取得改善 playbook；展示「用 AI 診斷 AI 工具行銷失敗」的自我修復實驗路徑，也是目前社群最大規模平行 agent 批次分析案例之一
- **Claude + SSH 伺服器存取替代 Dispatch**：開發者透過 `list_vms` 與 `run_command` 工具讓 Claude Chat 取得伺服器 SSH 存取權，解決無法隨時開啟筆電執行 Claude Code 的痛點，代表「Claude Chat 作為 agent 觸發點」的邊界持續延伸
- **Grounded Code AI 開發方法論系列（dev.to）**：連發四篇涵蓋應拋棄的「人工時代昂貴習慣」、以 spec.md 為核心工件、五步驟開發循環（spec → plan → implement → verify → consolidate）到局部性 + 合約 + 隔離十大原則，是目前最系統性的 AI 輔助開發方法論整理之一
- **Adobe Lightroom CC Linux 移植**：開發者借助 Claude Code 完成 Lightroom CC 在 Linux 上的主要移植工作（Phoronix 報導），是 Claude Code 處理複雜跨平台工程任務的代表性現實案例
- **新工具**：shipcheck（讀取 Claude Code / Cursor session log，輸出費用分解 + 檔案修改熱圖 + 安全掃描，完全離線；附帶發現 `@anthropic-ai/sdk` 常被誤寫為 `@anthropic/sdk` 的 package hallucination 問題）、machine（每個專案獨立 Lima VM，預設 Claude Code + Codex，session-only secrets 解決 supply chain 安全疑慮，Show HN）、cv-claw（Claude Skill 履歷生成器，HTML 模板 + JSON 資料層分離，Show HN）、Gonfire（分析應徵者 Claude Code session log 評估解題思維，面試替代 leetcode 新方案，Show HN）

#### 2026-05-16
- **API 費用焦慮達本週最顯著集體高峰**：6/15 計費調整背景下，同日出現大量成本控管教學——「7 種降費策略」（$200–800 月費區間開發者適用）、「不修改代碼省 10–30%」（prompt caching 與路由優化）、bootstrapped 創業者費用管控討論、Claude Code 替代方案整理；成本焦慮主導本週技術熱度，形成集體情緒；見 [[entities/pricing]]
- **Custom base URL 串接多 API provider**：Claude Code 透過自訂 base URL 串接非 Anthropic 的 API 提供商（GPT-4o、Gemini 等），達到降價、自動 failover 或多模型混用；在 6/15 計費調整前夕，此類繞道方案關注度明顯上升，是 6/15 後「多 LLM 混合策略」的實踐路徑之一
- **Agentic RAG + eval harness 防幻覺（50K→5K token 案例）**：開發者以 BM25 + Obsidian vault 建立工程書籍 RAG 系統，token 消耗從 50,000 降至 5,000，同時建立 eval harness 驗證 Claude 是否幻覺，是少數將「驗證機制」系統性納入工作流的實戰案例；見 [[topics/community-tech-discussions]]
- **X 開源演算法 + Claude Code 文件化案例**：開發者使用 Claude Code 閱讀 X（Twitter）開源的推薦演算法，整理為平易近人英文說明（完整 8 步驟），是 Claude Code 用於「理解大型陌生程式碼庫並文件化」的典型案例，展示技術文件化上的實用價值
- **非工程師 × Claude Code = 完整 MCP 伺服器（6 個月心得）**：台灣非工程師背景創業者獨自用 Claude Code 開發 MCP 伺服器六個月；核心洞察：「Claude 能寫任何代碼，但產品決策、架構取捨仍需人來做；非工程師的優勢在於沒有技術偏見，更容易做出以產品為中心的架構決定」
- **新工具**：Code Quest（Web UI 互動模式，針對 6/15 計費設計）、CostHawk（公開 token 用量排行榜，Claude Code/Codex/Cursor 三方比較）、AI 引用資格稽核 MCP（13 工具，AI 原生 SEO，無需 API key）、answering machine MCP（Claude Code 用戶間留言功能）

#### 2026-05-15
- **MCP 麥克風整合——語音驅動 Claude Code**：開發者透過 MCP 整合麥克風，讓 Claude Code 在需要更多脈絡時主動發出語音提問，使用者口語回答後繼續執行；突破傳統文字輸入互動模式，是 Claude Code 人機介面實驗的代表案例，呼應 [[entities/cat-wu|Cat Wu]]「AI 主動性（proactivity）」方向
- **破壞性操作安全閘門工具（GrapeRoot Pro）**：「Claude 刪除整個專案」類帖子持續增加（近期 700+ 留言），催生破壞性操作閘門設計——執行 `rm -rf` 等高危指令前自動顯示受影響檔案清單（含讀寫次數、最後存取時間）並暫停，需使用者確認後才繼續執行；見 [[topics/ai-agent-safety]]
- **長期 auto-memory 品質管理（3 個月案例）**：在同一專案跑三個月 auto-memory 後出現命名分歧、frontmatter 缺失、搜尋失效等退化問題，作者撰寫命名規範強制執行 skill + bash 審計腳本自動偵測品質漂移；是長期 agentic 工作流記憶管理挑戰的首個公開系統性應對案例；見 [[topics/ai-agent-safety]]
- **平行子代理成本分析（有官方數字支撐）**：引用 Anthropic 官方數據（多 Agent 系統約消耗 15 倍 token，快取命中可降至 10%），以具體計算說明哪些任務適合平行子代理、哪些反而成本暴增；是近期少見有官方量化支撐的 multi-agent 成本分析文
- **「monk」靜默模式 skill——節省 25% 上下文視窗**：讓 Agent 執行期間保持靜默、僅在完成後輸出標準化結果，實測節省約 25% 上下文視窗容量（佔全 session token 節省約 3–5%）；適合批次自動化任務、不需即時追蹤過程的場景；與 `/background` 指令應用場景高度重疊
- **PlanBridge 行內計劃書評審**：透過 Agent hook 在本地瀏覽器渲染 Markdown 計劃書，讓使用者直接在計劃文字上留行內評論，解決終端機審閱 Agent 計劃時難以精確標注的 UX 痛點；是「human-in-the-loop」審閱流程的新工具形態
- **CLAUDE.md 精簡反思（Token 成本上升背景下）**：6/15 計費變更催生 CLAUDE.md token 成本意識——冗長 CLAUDE.md 每次對話消耗大量 token 但對行為改善有限，精簡設計成為成本敏感期的新議題；配額將至自動收尾工具（my-time-has-come）同日出現，反映 Pro 方案配額焦慮形成系統性需求
- **「90 天 Claude Code vs Cursor」比較結論**：同時使用兩工具 90 天後的比較共識：Claude Code 更適合 Agent 驅動自動化任務，Cursor 在互動式編輯體驗仍有優勢，建議依工作流性質選擇而非二擇一；與 [[topics/competitor-landscape]] 的分流討論形成互補視角
- **新工具**：PlanBridge（開源行內計劃書評審）、my-time-has-come（配額將至自動收尾）、MCP 麥克風整合（語音提問）、GrapeRoot Pro 安全閘門

#### 2026-05-14
- **訂閱 programmatic 用量剝離——費用可觀測性工具需求爆發**：6/15 起 `claude -p` / Agent SDK 改按全額 API 費率計費，直接推動 token 成本分析工具密集出現同一天：Ledger（Rust，PR 層級 token 追蹤 + macOS 選單欄 + Web dashboard）、Clawdmeter（ESP32-S3 實體 token 監控面板）、Grafana + Prometheus 監控 dashboard；費用可觀測性從「選配」成為「必備」；見 [[entities/pricing]]
- **多 LLM 混合架構作為訂閱費用因應策略**：Opus 4.7 擔任決策 orchestrator、DeepSeek V4 Pro 承擔大量 token 輸出的混合架構，在 Max20 方案下最大化性價比；「高能力 orchestrator + 低成本 worker」的跨廠商架構預計成為 6/15 後的主流因應方式；見 [[entities/pricing]]
- **PTY 終端模擬繞過工具（claude-pee）**：透過 PTY 模擬互動終端執行 claude、注入輸入並用 stop hook 截取輸出，使 `-p` 用量不進入獨立信用池；繼 Claw-Code 後第二個以工程手段繞過 Anthropic 限制的社群工具，作者坦言為臨時方案
- **雙向 HTML 工件生成（agent-html-skills）**：受「HTML 的非凡有效性」文章啟發，讓 Claude Code 在認為必要時**主動**生成 HTML 視覺化輸出（非用戶觸發），並支援自動提交回介面；是「agent 主動視覺化」工作流的首個開源實現，與 [[entities/cat-wu|Cat Wu]] 訪問「主動性（proactivity）」方向呼應
- **「週末 + Claude Code = 替代商業訂閱工具」持續驗證**：同一天出現兩個案例——Tauri macOS 語音輸入 app（取代 $15/月 Wispr Flow）與 Bloomberg 風格股票分析工具（取代付費訂閱），均由領域知識持有者（非工程背景）用幾天完成；印證「領域專家 × Claude Code」的快速工具化路徑持續成熟
- **commit-triggered 學習技能模式**：每次 commit 後觸發學習提示的 Skill，概念是將開發流程轉化為刻意練習機會；社群評論認為包裝過度（底層僅 bash + LLM 提示），但「anti-skill-atrophy 整合於開發工作流」的方向持續共鳴；見 2026-05-09 skill atrophy 討論串
- **新工具**：Ledger（Rust PR token 成本追蹤）、Clawdmeter（ESP32-S3 桌面 token 面板）、Grafana Dashboard（Claude Code Prometheus 監控）、agent-html-skills（雙向 HTML 工件）、Lanes v0.39（GitHub/Linear 雙向整合）

#### 2026-05-13
- **Boris Cherny 每晚數千個 AI 子代理工作流**：Claude Code 創始人公開讓數千個子代理夜間執行「深度工作」的極端 agentic 工作流，被 Business Insider 與 Let's Data Science 主流媒體大幅報導；是個人生產力 agentic AI 的里程碑案例，也是「Loops 是未來」哲學的公開極端實踐；見 [[entities/boris-cherny]]、[[entities/managed-agents]]
- **v2.1.140 subagent_type 匹配改善**：大小寫不敏感及分隔符號不敏感，`"Code Reviewer"` 可自動解析為 `code-reviewer`，降低子代理配置的摩擦，推動多代理架構的易用性；見 [[entities/claude-code]]
- **Dragoman 多模型路由 CLI**：約 800 行開源 CLI，讓 Claude Code 依問題類型路由至不同模型（Perplexity/Gemini/Ollama），支援 4 模型並行 + Claude 統整；API 金鑰走 1Password/Keychain 不進入 Claude context；HN Show HN 形式發布
- **Cocall.ai 電話 MCP**：AI 代理與實體通話整合（撥打外線、自動暫停詢問、IVR 導航），是 MCP 生態向實體世界延伸的代表案例，繼 OpticOdds MCP 後進一步拓展 Claude Code 的垂直應用邊界
- **Token Bloat 系列：測試輸出精簡策略**：開發者聚焦測試執行器輸出作為降耗第一步，提出只保留「通過/失敗/位置」資訊的精簡格式，預告系列文章；代表社群正在系統性解決 token 效率問題
- **AI 生成程式碼安全漏洞評測（48 應用，90%）**：大規模靜態分析結果（44% 驗證缺口、33% RLS bypass、25% BOLA/IDOR）直接挑戰「AI 快速開發即可上線」；安全審查必須成為 Claude Code 開發的標準流程；見 [[topics/ai-agent-safety]]
- **Anthropic 定價主導權持續強勁**：The Information 報導企業客戶願意吸收成本上漲，API 費用走向值得長期關注；對依賴 Anthropic API 的企業有預算規劃含義；見 [[entities/pricing]]
- **新工具**：Dragoman（多模型路由 CLI）、Cocall.ai（電話 MCP）、Claudy macOS session 管理版（多 session 並列 + 自動帳號切換 + Draft Commit + Marketplace）；PullMD v2.4.1 支援 claude.ai 網頁版自訂連接器原生整合

#### 2026-05-12
- **`/goal` fire-and-forget 官方正式功能**：v2.1.139 推出 `/goal` 指令，是 Claude Code 首個真正的 fire-and-forget 循環——設定可驗證完成條件後，小型快速模型自動判斷條件成立與否並決定是否繼續執行；Reddit 社群熱烈反應，被視為 Claude Code 邁向非同步工作流的關鍵里程碑；見 [[entities/managed-agents]]
- **Agent View 統一多 session 管理**：同版本推出 Agent View（Research Preview），`claude agents` 可查看所有並行工作階段即時狀態（執行中/等待輸入/已完成），解決過去需要手動管理多個終端機視窗的工作流痛點；多家媒體（TestingCatalog 等）廣泛報導，是本日最受媒體引用的技術更新
- **對抗性審查工作流**：開發者分享讓兩個 Claude 實例扮演起草者與批評者的工作流，事前讓批評者 Claude 挑毛病後再執行，顯著降低靜默失敗率；與 agent-order（跨模型 PRD 互評）的設計理念相近但聚焦同模型雙角色分工
- **Writ 規則強制執行**：Neo4j 知識圖譜 5 階段 Pipeline 自動擷取語義相關規則集，是「CLAUDE.md 被忽略 + 無關規則耗 token」雙重困境的社群工程解法，比 Hooks 機制更聚焦規則精準注入，比全量 CLAUDE.md 載入更省 token
- **ltm 跨環境 Agent 記憶**：Core Memory Packet JSON 協定讓 Agent 記憶可跨編輯器、跨機器、跨模型攜帶，直接指出 CLAUDE.md 等 Markdown 方案的跨環境局限；與 Memex（本地 RAG）、NanoBrain（git-backed）定位不同，聚焦可攜性而非持久化深度
- **Context 管理是大型專案核心瓶頸**：大型專案使用 Claude Code 的最大瓶頸被確認為 Context 管理而非程式碼品質——LLM attention 機制在缺乏系統全貌時生成「看起來正確但邏輯有誤」的程式碼；具體應對策略包括系統性注入架構概覽、結構化 codebase 索引、任務分拆
- **Checkpoint Commits git history 污染**：Claude Code 自動 checkpoint commit 污染 git log 的問題在 Reddit 引發熱議，搭配 worktree 使用時問題更嚴重；社群整理多種清理方案（interactive rebase squash、git filter-repo），目前無官方解法
- **新工具**：HiveTerm（多 Agent 工作站）、Writ（Neo4j 規則強制執行）、Agent FM（聽覺化進度廣播，MIT）、Usage4Claude 3.0.0（含 Codex 追蹤，Keychain 認證）、ltm（跨環境 JSON 記憶協定）

#### 2026-05-11
- **Managed Agents 正式發布 + 社群 vs 官方架構比較**：70 天自建多代理系統的開發者分享實戰架構（Opus 決策層 + OpenCode 工程師層 + 並行研究代理），核心洞見：「任務簡報品質才是多代理系統成敗的核心」；官方托管方案與社群自組架構的功能差距比較進入主流討論
- **adamsreview — 多代理 PR Review 超越官方工具宣言**：以平行子代理、多階段驗證、JSON 持久狀態執行 PR review；作者聲稱比官方 /review、/ultrareview、CodeRabbit 及 Greptile 捕捉更多真實 bug；在官方 PR review 工具已存在情況下做出差異化，是插件生態深度定制的代表案例
- **Judge Gate 概念**：提出「語意層 agent 品質驗證」作為傳統測試框架之上的額外驗證層——「測試通過 ≠ 功能完成」是自主編程代理的結構性盲點；六秒 CI 語意漂移偵測方法補足相同問題的持續監控維度
- **Opus 4.7 提示詞行為轉變確認**：精讀 Anthropic 官方 31 頁提示詞指南後確認 Opus 4.7 更趨字面解讀，4.6 時代的通用模糊指令在 4.7 下表現明顯下滑；需更明確的指令設計，所有現有 prompt 工程實踐需重新審視
- **費用管理新一輪熱議**：$514/30 天詳細費用分析 + 配額管理指南（同作者兩篇互補）；Pro 方案 0% 使用量仍被收取 $3.37 extra usage 的透明度問題同步浮現；費用成為本週社群最熱議焦點
- **CLAUDE.md 記憶驗證兩招**：金絲雀規則（在記憶中埋入特定奇特前綴）+ 直接詢問專案設定，是 CLAUDE.md candidate-context 架構揭示（2026-05-10）催生的快速一致性檢查對策；對自動化工作流的可靠性設計有參考價值
- **AGENTS.md 跨工具插件簡報模式**：以 AGENTS.md 統一跨工具代理配置（Kobiton 案例），降低 Claude Code / Cursor / GitHub Copilot 跨工具整合的設定重複成本
- **Claude Code Desktop vs Claude Cowork 定位混淆**：用戶困惑兩款產品功能高度重疊，Anthropic 尚未給出清晰的差異化說明
- **新工具**：vibe-log-cli（每日/每週開發工作摘要自動生成）、academic-research-skills（蘇格拉底反思模式技能包，社群評價分歧）

#### 2026-05-10
- **Mac 本機排程工具**：Remind — 透過系統「提醒事項」App 設定時間觸發 claude 指令，結果寫回提醒事項；支援 iPhone/Apple Watch 跨裝置，可透過 frontmatter 續接既有 session；補足 Claude Code 缺乏 Mac 本機排程的功能空白
- **跨 session 記憶注入**：draft CLI plugin — session-init hook 自動注入結構化產品上下文摘要，不呼叫額外 API 或另跑模型，完全在現有 Claude 訂閱額度內解決跨 session 記憶歸零問題
- **AI 程式碼安全掃描整合**：Snyk + Claude Code — 60 秒整合 Snyk 對 AI 產出程式碼即時掃描 SQL injection/XSS/金鑰外洩，在程式碼進入 repo 之前即時攔截；對大量使用 Claude Code 的團隊具實際參考價值
- **token 預算管理**：Tokenyst — Claude Code pay-as-you-go 任務層級 token 預算，每次提示後即時顯示剩餘額度；session 費用 $6–10 的根因是快取不跨 session，社群同日提出圖資料庫索引 codebase 的創意解法
- **codebase agent 就緒度評估**：Agentize — Claude Code skills 評估並改善 codebase 的「agent 就緒度」，協助 AI agent 更有效理解現有專案結構
- **CLAUDE.md candidate-context 架構揭示**：社群逆向工程發現 CLAUDE.md 被以 `<system-reminder>` + 「may or may not be relevant」包裹，直接解釋「CLAUDE.md 指令被忽略」的根本原因；與 Claude Code 原始碼解析系列（dev.to Chapter 1）同步出現，顯示社群正在系統性解構 Claude Code 內部架構
- **Multi-agent 研究團隊 250+ 案例**：6 個功能各異的 agent 打造「AI 企業應用案例地圖」，250+ 真實案例；展示 multi-agent 在知識蒐集任務上的具體生產力，是社群罕見的可驗證大規模實務案例
- **LED 狀態指示燈硬體整合**：有人將 LED 燈改造成 Claude Code 即時執行狀態指示燈（XDA 報導），讓開發者直觀得知 AI agent 是否仍在運行，無需盯著終端機；展示 Claude Code MCP 生態向硬體整合延伸的創意邊界
- **三層疊加式 AI Code Review**：測試多層 AI review 流程，發現單一 AI reviewer 作為最後防線仍有遺漏 bug 的風險；對企業部署 Claude Code 做 code quality gate 的團隊有實務警示價值

#### 2026-05-09
- **HTML vs Markdown 作為 Claude Code 輸出格式（HN 187 則討論）**：主張以 HTML 取代 Markdown 的論點在 HN 引發 187 則討論，是本期單篇最高互動；效能優勢獲部分認同，「HTML 難以人機協同編輯」的反駁明確指出適用場景邊界——純機器消費 vs 人機共同作者的選擇差異
- **v2.1.136「操作安全與如實回報」收緊（+525 tokens）**：不可逆操作須確認、如實回報義務、`hard_deny` 類別新增；對全自動化 agent 工作流影響重大，需重新評估確認需求設計；見 [[topics/ai-agent-safety]]
- **re_gent — AI Agent 版本控制**：「Git for AI Agents」解決 /compact 後歷史斷層與決策追溯問題，已支援 Claude Code；補足 session log 的可追溯性缺口，與 Mneme、DataMoat 構成不同維度的 agent 歷史管理生態
- **PostToolUse 稽核日誌生產模式**：利用 PostToolUse hook 建立完整 agent 操作稽核日誌，是企業部署 agent 可觀測性的具體解法；記錄 timestamp、指令、目標 repo、執行結果
- **Git Hooks + AGENTS.md 代碼品質強制執行**：在 AGENTS.md / CLAUDE.md 中強制 pre-commit/husky，設定每檔 600 行 + McCabe 複雜度 10 的品質門檻；代理不得 bypass git hooks，延伸 Hooks 強制執行原則至版本控制邊界
- **54 ADR + 35 天**：架構決策記錄先於程式碼的嚴格紀律（每個功能先寫 ADR 再啟動 Claude Code），有效降低代理方向偏移；與 Mneme（ADR 自動注入）工具理念一致，延續規格驅動開發社群共識
- **obsidian-semantic — 語義 vault 搜尋**：讓 Claude Code 以語義搜尋使用 Obsidian vault（支援本地模型），自動發現應連結的筆記；是 Obsidian + AI 工作流的實用橋接工具，與 graphify、NanoBrain 共構知識管理生態三種選型
- **36 天使用數據：靜默模型切換 + 11.5 倍效率差距**：連續 36 天記錄顯示模型有時靜默切換且無明確通知，不同模型間量化出 11.5 倍效率差距；對成本意識的長期用戶是重要監控警示；見 [[topics/code-quality-decline]]
- **Code with Claude 2026 大會心得**：分享 context 管理策略、軟體工程瓶頸轉移、AI-native 工程組織實際運作；大會需求極高，Anthropic 臨時加開第二天場次；是理解 Anthropic 對開發者社群戰略意圖的第一手視角
- **unitmux — tmux 懸浮視窗**：解決 tmux 中 Claude Code 輸入介面干擾編輯器視角的痛點，讓輸入區域浮動顯示於編輯器上層
- **Terminal Arcade**：開發者在等待 Claude Code 跑任務時打造的終端機小遊戲集合，含每 5 次工具呼叫後顯示書摘的「書架」功能；趣味創作，也反映「AI 代理執行期間等待時間的 UX 設計」這個真實需求

#### 2026-05-08
- **CVE-2026-39861 安全危機 + 1-click RCE**：Claude Code 爆出 CVSS 7.7 沙箱逃逸漏洞（symlink 逃逸），v2.1.64 修補；Anthropic 對 1-click RCE 的「不應該點確認」回應引發信任危機；兩則安全事件同日在 HN 上版，是社群安全討論密度最高的單日
- **v2.1.133 `worktree.baseRef` 設定**：新增 `fresh` | `head` 選項，讓使用者精細控制 worktree 基準分支，對多工作樹並行工作流設計具直接影響
- **本機持久化記憶 39ms**：開發者分享 local stack + MCP 整合、39ms 檢索的持久記憶架構，解決無狀態 agent 問題；社群自建解法持續與 Managed Agents Dreaming 官方方案並行演進
- **120 提示詞模式實測**：目前社群最大規模的實證型 prompt 效果研究，以可量測差異（非主觀感受）為驗證標準，是本週最具參考價值的方法論貢獻
- **3.77 億 token / 月案例**：Claude Code + Codex 雙工具並用兩個月，揭露單月 token 消耗極端值，引發效率管理與成本討論
- **整合模式選擇框架**：社群系統化比較編輯器嵌入 vs 終端機原生 vs 橋接方案三種模式，形成選擇依據清單
- **Boris Cherny「coding is solved」+ 厭倦「vibe coding」**：「Code with Claude」大會言論經 Business Insider、HN、YouTube 多平台轉載，社群對「coding is solved」論斷反應兩極
- **新工具**：Claudy（Rust 多供應商管理）、DataMoat（AES-256-GCM 工作記錄加密）、4-agent Code Review（架構師 + 三模型審查，MIT）、awesome-ux-skills（UX 原則技能集）、OpticOdds MCP（首個運動賠率 MCP API，垂直產業擴展案例）

#### 2026-05-07
- **Managed Agents 重大更新（Dreaming/20 路並行/Outcomes）**：官方首次在架構層解決長跑 Agent 記憶持久性問題（Dreaming）、突破並行限制（20 路子代理）、實現可驗證達標（Outcomes 規格驗證）；Python SDK v0.100.0 + TypeScript SDK v0.95.0 同步新增原生支援
- **SpaceX 算力合作：Pro/Max 五小時速率上限翻倍、取消尖峰降速**：Dario Amodei 在 Code with Claude 大會現場宣布，是 Anthropic 首次透過外部基礎設施合作鬆綁使用限制，對持續跑 agent 任務的開發者影響最直接
- **Claude Code wire trace 揭示 13,000 字基礎提示詞**：Auto 模式安全邊界為提示詞層而非底層沙箱；Figma 等 MCP 插件大幅佔用 context window；企業安全評估的重要架構資訊
- **「理解是租來的，不是賺來的」——skill atrophy 引發廣泛共鳴**：AI 輔助開發技能退化問題進入社群主流討論，recap 工具等反 skill atrophy 工具同步出現
- **36 個記憶檔案系統**：使用 Claude Code 60 天後整理出 36 個結構化 per-project 記憶檔，根本解決 Agent 每次重啟都要重新說明背景的問題；與 Managed Agents Dreaming 的官方解法形成社群 vs 官方雙軌並進格局
- **Claude Code git log 作為首要除錯步驟**：觀察到 Claude Code 自動讀取 git log 除錯，描述性 commit message 在數秒內縮小問題範圍；搭配 worktree 的多 session 協作技巧同步分享
- **Skill 組合 Unix 哲學確認**：近一年 Skills 組合心得：遵循單一職責原則、每個 skill 只做一件事，Claude 的自動觸發準確度顯著提升；過度耦合的 skill 反而導致模型難以判斷何時使用，是踩坑後的反向工程建議
- **BrowserCode — WebAssembly 瀏覽器 + 行動裝置**：Claude Code 移植至瀏覽器，iPad、公司鎖定設備均可使用 Claude Code 核心功能，打破 CLI 安裝門檻
- **跨 session 問答插件（/qu /ans）**：開發者自製跨 session 通訊插件，兩個 Claude Code session 直接雙向問答，解決 session 知識孤島問題；與 Claude Relay（廣播傳訊）互補
- **Kstack — K8s 監控/除錯/安全審計 skill pack**：將 K8s 常見維運任務封裝為 Claude Code skill 組，是 skill pack 設計模式在特定技術棧深度整合的新案例
- **Claude Code Routines 自動化排程**：每晚自動摘要 commit、每週掃描過期依賴、每日彙整錯誤日誌趨勢；核心差異在於 Agent 能對結果進行推理，而非只執行固定 cron 指令
- **DeepSeek V4 替換 Claude Opus 4 的 30 天實測**：在 Claude Code 框架中以 DeepSeek V4 取代 Claude Opus 4，對比 1 億 token 成本與品質差異；是「Backend 替換模式」（見 2026-05-04）的實際長期驗證，為追求降費開發者提供量化數據
- **CLAUDE.md for Rust（13 條規則）**：防止 `Arc<Mutex<HashMap>>` 過度使用與 `.unwrap()` 濫用，引導 Claude Code 改以慣用的安全 Rust 模式；延續 2026-05-06 CLAUDE.md 語言規則集爆發趨勢（已覆蓋 Rails/Kotlin/Flutter/Scala/C++/Rust）
- **MCP code execution 取代靜態工具列表**：解決 MCP server 過多導致 context window 在第一條訊息前就半滿的問題，以動態能力獲取取代靜態工具列表，是 MCP 架構規模化設計的新思路
- **Cursor → Claude Code 全面切換（6 個月比較）**：作者在多個實際產品中並行使用逾 6 個月後全面轉換，月費高峰超過 $60，強調長期多專案使用情境下的整合優勢
- **漫畫動畫製作（GPT Image 2.0 + Claude Code）**：偵測格格邊界、依序揭露、鏡頭平移縮放的多步驟創意管道，展示 Claude Code 在非程式碼創意工作流的應用邊界

#### 2026-05-06
- **v2.1.131 緊急修復 Windows VS Code regression**：v2.1.128/129 推送後 Windows VS Code extension 無法啟動，數小時內因 Reddit 大量回報而緊急發布 v2.1.131 修復（createRequire polyfill hardcoded build path + Mantle endpoint 認證失效），凸顯 Claude Code 用戶密度之高可實現近即時問題追蹤
- **Speculative Parallelism 工具化**（Claudette）：開源桌面工具讓每個 Claude Code agent 擁有獨立 git worktree + session + 終端機；社群顯示已有開發者手動實踐此模式數月，工具化讓 speculative parallelism 工作流進入主流可及性
- **Skills Unix 哲學確立**：「每個 skill 只做一件事、功能過多就拆分」被 1 年實踐驗證可提升模型自動選用正確 skill 的準確率；skill catalog 設計的最重要原則之一
- **CLAUDE.md 語言規則集爆發**：同日出現 Rails、Kotlin、Flutter/Dart、Scala、Modern C++ 五個語言的專用規則集文章，顯示 CLAUDE.md 語言特定化趨勢正快速加速；社群正建立去中心化的語言生態 AI 開發規範庫
- **Hooks 深度介紹**（PostToolUse）：社群文章深度解析 Hooks 機制強制執行 Claude 可能略過之步驟（格式化、commit）的實際應用，強調「Hooks = 強制執行，CLAUDE.md = 建議」的根本差別
- **6 Agent Patterns from Leaked Source**：基於 3/31 意外外洩的 Claude Code TypeScript 原始碼（1,900 個檔案）整理出 6 個值得參考的 agent 設計模式（dev.to）
- **Claude Code as MCP Hub 實務分享**：整合 n8n、瀏覽器 LLM 介面等自動化平台為 Claude Code 統一 MCP 協調中心的實務經驗（dev.to forgeflows）
- **Agentic Slack vs IDE 討論**：從多人團隊實際使用 Claude Code 的視角，指出 PR review 已成新瓶頸，主張「協調必須發生在 IDE 之前」，為 agentic 工作流組織化挑戰提供系統性分析
- **Self-improving rules**（claude-smart）：將用戶糾正泛化為跨專案通用規則，解決現有記憶體方案無法捕捉糾正的問題；HN 評價褒貶不一
- **Dreamer — MCP team memory server**：短期記憶→長期記憶排程整合，自動更新 AGENTS.md 與 skills，靈感來自 Claude dream mode，支援任意 coding agent
- **Pure CLI, Pure Unix, Zero IDE**（Raspberry Pi 5 + tmux）：展示 Claude Code 作為純 CLI 工具的最大靈活性——在 Raspberry Pi 5 上 24/7 運行，從手機、平板、筆電無縫接入，打破 IDE 依賴
- **Git for AI Agents（早期開源）**：針對 AI 驅動開發中 git 痛點（無法追蹤「為何改動」、rewind 不可靠）開發的 AI agent 專用版本控制替代方案，屬早期開源概念，討論方向有參考價值
- **Boris Cherny「軟體工程已死」第二波**：Times of India 等媒體再度報導 Boris Cherny 的觀點，Anthropic 內部已無傳統軟體工程師職位，開發者身份認同議題持續發酵

#### 2026-05-05
- **Boris Cherny「Loops 是未來」**：Claude Code 創始人在 podcast 宣示已 100% 用 Claude Code 取代手動編碼，並提出「迴圈執行是 AI 編碼未來」的設計哲學；是理解 Claude Code 工具設計原則的第一手資料
- **Claude Relay — 多 session P2P 協作**：plugin 讓多個本地 Claude Code session 互相傳訊，兩位開發者的 P2P 多 agent 聊天室工作流獲 HN 正面評價，被視為「非正式 multi-agent」的具體實作
- **Memex — 本地 RAG 持久記憶（MCP）**：本地 RAG + 離線 embedding，無需雲端 API，以 MCP 接入；與 Brifly / NanoBrain 並列為跨 session 記憶方案的主流選項
- **Claude-Find — 語義 session 搜尋**：解決 /resume 只能依第一條訊息篩選的痛點，讓重度用戶用語義搜尋快速找到過去決策，注入現有 session；補足 Claude-Find + Relay + Memex 三工具構成完整的 session 管理工具鏈
- **Askdiff — diff 介面直問原始 session**：在 PR 風格 diff 介面中點擊行號直接問生成此程式碼的 Claude Code session，串流取得決策理由；解決 code review 時 context 斷層的痛點
- **CLAUDE.md for Multi-Agent 11 條規則**：針對多個並行 session 的衝突防範，涵蓋工作區邊界、共享狀態禁止、orchestrator 角色明確化等；是目前最系統化的多 agent CLAUDE.md 規範整理
- **7 個 token 降耗技巧 + Caveman Skill 65% 降耗實測**：高 token 成本根源在 context 膨脹而非 prompt 長度；Caveman skill 實測有效，但節省幅度依情境差異大
- **Playwright CLI vs npx 差異的 token 陷阱**：`@playwright/cli` 與 `npx playwright test` 在 AI agent 環境下行為不同，可能導致大量多餘 token；CI/CD 自動化測試工程師需特別注意
- **LinkedIn 留言自動化 Skill（含 human-in-the-loop 架構）**：結合聲音剖析（15 題問卷 → markdown 語氣檔）、Notion 審核佇列與 Playwright 自動發布；「含 human-in-the-loop 的 skill 架構」模式具高移植參考價值
- **Rudel — 9 種 AI 程式設計師原型分析**：分析 2 萬筆以上 session metadata，揭示 4% session 使用 skills、26% 在早期放棄；Spotify Wrapped 風格的可視化讓 session 行為量化成為新討論焦點

#### 2026-05-04
- **DeepClaude — 低成本後端替換（HN 543 則討論）**：僅需修改 `ANTHROPIC_BASE_URL` 等環境變數，即可讓 Claude Code agent loop 呼叫 DeepSeek V4 Pro；HN 543 則討論凸顯社群對低成本模型替換的高度需求，技術上早已可行（DeepSeek 文件早有說明），但此次爆紅顯示許多開發者剛意識到此可能性
- **Semble — code search 比 grep 少 98% token**：Open Source，結合 Model2Vec 靜態嵌入（potion-code-16M）、BM25 與 RRF 重排序，專為 Claude Code agent 大型代碼庫搜尋設計，解決 agent 搜尋失敗後退化為讀整個檔案的問題
- **Kirikiri — iOS mobile IDE（開源）**：Flutter + dartssh2 打造，連接 Google Cloud Shell 或 SSH 伺服器遠端執行 Claude Code，以浮動按鈕取代軟體鍵盤常用指令，目標讓手機成為 AI 輔助開發的一級操作環境
- **JupyterLab Claude Code Extension**：讓資料科學家直接在 Jupyter 環境使用 Claude Code，無需切換至獨立終端機；開源
- **Prism MCP — VS Code LSP 橋接**：透過 MCP 將語言伺服器（LSP）語義導航接入 Claude Code，讓 AI 以語義方式（跳轉定義、引用搜尋）瀏覽代碼庫，已發布於 VS Code Marketplace
- **claudely — 本地 LLM 無侵入切換**：保留 Claude Code Skills/MCP/Hooks 生態完整性的前提下，將後端切換至 LM Studio/Ollama/llama.cpp，無需修改主配置文件
- **Smithy — issue tracker 觸發容器化 session**：從 Jira/GitLab/Forgejo 直接觸發容器化 Claude Code 工作階段，每個 issue 對應獨立容器分支，完成後自動開 PR、回應 CI、整合 PR 回饋，解決本地無監督執行的安全疑慮
- **Patina — CLAUDE.md retro loop**：開源 CLI（MIT，已上 npm），解決 CLAUDE.md 長期使用後的「腐化」問題（修正行為再復發、規則膨脹失焦）；retro loop 機制定期回顧並更新 harness 設定
- **「應該放棄嗎？」非正式重置咒語**：Claude Code 多次失敗後詢問「我們應該放棄嗎？」，模型常「振作」並成功完成任務；HN 討論顯示多名開發者已重複驗證此現象，機制尚不確定
- **CLAUDE.md for Java（13 條 Spring Boot 規則）**：整理針對 Java/Spring Boot 生態的 13 條 CLAUDE.md 規則，對抗 AI 在 Java 生態容易犯的壞習慣（如無限堆疊方法至單一 class 超千行），提供可直接套用的指令範本
- **Memtrace — agent context 時間感知層**：為 codebase 建立持久的時間感知表示（time-aware representation），讓 agent 追蹤哪些地方改動及為何，解決長 session 中 agent 反覆重讀的根本問題
- **Pilot Shell — 工程紀律框架**：提供 /spec（完整 TDD）、/fix（複雜度自動偵測，超出標準路徑即中止）、/prd（需求文件生成）三個核心指令，定位「輕量但有工程紀律」的中間地帶
- **Claude Connectors 擴展至創意工作軟體**：透過 MCP 協議延伸至 Adobe（After Effects/Photoshop/Illustrator）、Blender、Ableton Live、Affinity 及 Autodesk Fusion，Claude 整合觸角首次進入設計與創意工作流程領域
- **批次截圖貼入工具**：補足系統剪貼簿無法一次傳送多張圖片的缺口，可批次將截圖貼入 Claude Code 等任意 app，開源、無雲端、系統匣 + 浮動 widget 操作

#### 2026-05-03
- **macOS 電腦使用（computer use）能力**：Anthropic 為 Claude Code 及 Claude Cowork 加入 computer use 功能，可直接控制 macOS 桌面的滑鼠與鍵盤，AI agent 能力範疇從純程式碼助理擴展為全桌面自動化代理；此為 Claude Code 功能邊界的重大擴張
- **29 天 91k 行 ERP，零工程師**：聲稱獨立使用 Claude Code 在 29 天內完成 91,000 行程式碼的 ERP 系統；若細節屬實，將是 AI 輔助開發生產力的標誌性案例，社群開始驗證技術深度與維護性
- **8 個 Claude Code 品質控制技巧**：整理強制澄清至 95% 確定度、Todo 加自動驗證步驟、及早中斷偏離執行等 8 個實用技巧；量化 95% 確定度門檻為本次討論的具體數據點
- **雙代理 VPS 持續運作框架**：兩個 Claude Code 代理在 VPS tmux session 中持續運作，自動開 PR、發 Discord 更新、相互協調；每個代理使用獨立 OS 用戶隔離爆炸半徑，架構類似 Claude Code 版 docker-compose；作者自三月起 dogfooding
- **CLAUDE.md for Kubernetes（13 條規則）**：針對 K8s 的 13 條 CLAUDE.md 安全規則，防止 latest tag、缺少資源限制、過度授予 cluster-admin 等高風險模式；將 CLAUDE.md 從通用指令框架升級為技術棧特定的安全防護工具
- **AI 命名一致性 OSS 工具**：因 AI 對同一功能反覆產出不同命名（getUsers/fetchUserList/loadAllUsers），開發者自建開源工具強制 Claude Code 等 AI 維持一致命名與程式碼風格，是「AI 代碼非決定性」問題的具體工程解法
- **TradingAgents Plugin（免額外 API 費）**：將多代理股票分析框架改寫為 Claude Code 插件，7 個並行/序列分析子代理（技術面/基本面/投資組合管理），在現有 Claude 訂閱下免額外費用執行，展示「訂閱內多代理」的成本優化思路
- **40 個個人技能系統**：使用者整理自己累積建立的 40 個 Claude 技能，依重複工作流程、決策框架、格式模板等分類；展示個人工作知識系統化轉化為可複用 AI 工具的深度實踐，技能數量突破數十個的系統化管理案例
- **AI 時代開發者身份認同討論**：「If Claude writes the code, what makes me still a developer?」三個月未親自寫程式卻持續交付功能的開發者記述梯度滑坡式的角色轉變；社群廣泛討論 AI 協作時代「開發者」定義的重新邊界，被視為持續發酵的社群趨勢

#### 2026-05-02
- **PreToolUse Hooks 四種 exit code**：深度解析 Block/Allow/Modify/Error 四種 exit code 在攔截、放行、修改工具調用等場景的實際差異，官方文件嚴重低估其複雜度
- **Token 路由降成本**：開發者透過 CLAUDE.md 路由規則將繁瑣任務委派給 Kimi K2.5 等 $0.02/call 低成本模型，不升級訂閱即可大幅提升 Pro 額度效率（解決每週三就耗盡配額的問題）
- **Governor — token 優化插件**：已查證（2026-08-13）：repo 為 [0xhimanshu/governor](https://github.com/0xhimanshu/governor)，現況 127 星／6 forks／0 open issues；官方文件正面回應原本 HN 批評，V2 benchmark 除 token 數外同時量測「Valid Context Loss Rate」與「Decision Preserved」兩項品質指標（非只算 token），宣稱平均省 45.5% token 且保留 100% 決策正確度（對照組僅 87.5%），惟屬專案自陳的 pilot 測試，未見第三方獨立重現
- **Caliber — 跨工具 AI config 統一管理**：開源工具統一版控 CLAUDE.md、.cursor/rules、AGENTS.md 等跨平台配置，本週突破 888 stars，社群徵集功能需求
- **記憶體防漂移框架**：agent 記憶未版本控制時會隨規模增長產生可量測的行為偏移；具體審計框架：定期 prune、版本控制記憶文件、標記衝突條目
- **規格驅動開發**：呼應 Karpathy 演講，主張以嚴謹規格文件取代 vibe coding，人類主導規格設計，AI 負責實作執行
- **CLAUDE.md 跨 repo 傳播**：將 `~/.claude/CLAUDE.md` 中積累的規範批量傳播至多個 repo，以全局 CLAUDE.md 作為跨 repo 遷移計畫的共同載體
- **Agentic Knowledge Base（Karpathy LLM wiki 進化版）**：在 Karpathy LLM Wiki 基礎上加入語意搜尋 adapter 並整合 TickTick 等工具，打造可被代理查詢的工作知識系統
- **sudo MCP 插件**：自製 MCP 解決 Claude Code 代理需要 root 權限時的工作流中斷，需提權時彈出密碼視窗，完成後將 stdout/stderr 與 exit code 回傳代理；社群討論更安全的替代做法

#### 2026-05-01
- **Omar — 100 Agent TUI 管理儀表板**：兩位開發者因不堪多視窗切換之苦打造，支援 Agent 層級化管理（類似公司組織架構），展示 multi-agent 工作流管理工具需求快速浮現
- **graphify — 知識圖譜插件爆紅**：26 天達全球 GitHub rank #2（450k+ 下載、40k stars），透過 Leiden 社群偵測建立程式碼知識圖譜，宣稱 71 倍 token 效率；意外使用場景（SQL schema、Obsidian vault、學術論文）顯示知識圖譜在非程式碼領域的通用性
- **Chrome 用量監控擴充**：在 Claude.ai 介面即時顯示每則訊息 token 數、context 使用量、提示快取倒數計時及速率限制進度條，解決原生介面對用量透明度幾乎為零的痛點
- **NanoBrain — git-backed 個人知識庫**：< 50ms append 延遲透過 hook 在 session 結束時更新，整合 Gmail/Google Calendar/Slack 定時匯入，適合需要 AI Agent 跨工具共享長期知識的場景
- **Council — 多模型並行 CLI**：自動偵測系統上的 claude/codex/gemini 並平行執行同一 prompt，由「主持人」模型彙整並標記分歧點；MIT 授權，適合多模型交叉驗證場景
- **自修改 Agent 系統節省 50% API 費用**：讓本地 GPU（RTX 5070）在閒置時段執行低優先任務，有效降低 50% Claude API 費用；repo 已開源
- **Destiny 占卜插件 + Mote Minecraft Agent**：社群創意應用持續延伸 Claude Code 邊界，Destiny 底層以 Python 計算八字/卦象確保結果可驗證、Mote 可自主玩 Minecraft Bedrock


## 2026-04

### 時序流水帳（併自原社群時序頁，2026-04-25～04-30）

#### 2026-04-30
- **Nimbalyst 多 agent 視覺化工作台**：開源工具支援 Claude Code/Codex/Opencode，透過 WYSIWYG diff 介面逐一審核各 Agent 修改，同時支援 Excalidraw/試算表/Monaco 等多種編輯器，填補多 agent 協作的可視化需求
- **Throttle Meter 用量監控**：macOS menubar 工具，從 `~/.claude/projects/*.jsonl` 即時計算 5 小時滾動窗口用量，開發動機是頻繁被限速；無遙測、無網路請求，MIT 授權
- **Mneme 架構決策層**：repo-native CLI，將 ADR 直接存在程式碼庫旁並在 Claude 呼叫前自動注入，支援 CI 攔截違反架構的 PR，是 CLAUDE.md 外的另一種架構治理模式
- **Brifly 持久記憶層**：為 Claude Code 提供跨 session 的專案架構知識儲存，支援多人協作與版本追蹤，直接對抗 AI 輔助開發中的「無狀態」問題
- **Linear + Lanes MCP issue-to-code 流程**：串接 Linear 官方 MCP 與本地 Lanes MCP，讓 Agent 直接讀取 Linear 待辦票並啟動 Claude Code 工作階段，實現 issue 到程式碼的一鍵流程
- **Trent 架構層安全審查**：在 Claude Code 環境中嵌入情境化安全稽核，補足傳統 CVE 掃描器對業務邏輯的盲點
- **Claude Opus + Gemini 多 LLM 交易架構**：Opus 擔任首席工程師（持有否決權）、Gemini 負責策略判斷，累積超過 270 條分歧記錄日誌，是目前公開最詳細的 Claude + Gemini 角色分工實驗

#### 2026-04-29
- **Champion Kit 官方推廣包**：Anthropic 發布官方「Champion Kit」，為企業推廣者提供 30 天計畫、常見疑慮應對話術與分享素材，顯示 Anthropic 透過基層工程師滲透企業的策略已正式化
- **Web UI 工具 Cockpit**：開源瀏覽器介面讓 Claude Code 擺脫終端機限制，補充 CLI-first 定位不足之處
- **Harness 多 worktree 並行管理**：在多個 Git worktree 同時管理多個 Claude Code agent，作者明確指出現有工具（cmux、Conductor）的不足
- **CodeThis MCP paste bin**：專為 Claude Code 設計，AI 可直接透過 MCP server 建立程式碼分享貼文，支援 100+ 語言語法高亮
- **Claude Exporter**：Chrome 擴充功能將 Claude 對話匯出為 PDF/Word/Google Docs/Notion，填補對話持久化的社群需求
- **Caveman vs "be brief." 基準測試**：系統性 24 題、6 類別測試顯示兩者在 token 數量與輸出品質上幾乎相當，複雜外掛未帶來可量測優勢，「兩字 prompt 足以媲美複雜外掛」成為討論焦點

#### 2026-04-28
- **Jupyter Notebook + MCP 整合**：推薦以 Jupyter MCP server 取代 Claude Code 內建 NotebookEdit 工具，需額外 10 分鐘設定，但支援完整儲存格執行、輸出讀取與 IPython kernel 互動
- **Batch API 不適合 agent**：開發者實測將 agent 每輪呼叫走 Batch API（享 50% 折扣），結果每筆 batch 需 90–120 秒，5 輪工具呼叫的 agent 對話變成 10 分鐘等待；結論：Batch API 僅適合後台非同步任務，不適用互動式 agent
- **PullMD HTML 轉 Markdown**：為 Claude Code 建立 MCP server，在抓取網頁時先轉換為乾淨 Markdown，一般文章有效內容僅佔原始 HTML 的約 20%，可大幅減少 token 浪費
- **Sonnet 4.6 替代 Opus 工作流**：調整 agent 工作流程設計後，Sonnet 4.6 以 30% 月預算完成相當於前週 73% 預算的工作量，且程式碼品質更佳；關鍵在工作流重新設計，不只是換模型
- **Claude Code Plugin 反模式與模式**：作者整理將 scrum 工作流轉為外掛的經驗：不必要的 context 載入等反模式大量消耗 token，重構後整理出 5 個可通用設計模式（附前後成本對比）
- **Effort 等級不影響拒絕姿態**：系統性測試 Opus 4.7（39 份測試腳本、medium / high / xhigh 三種 effort）顯示拒絕姿態完全一致，effort 僅影響回答深度；顛覆「高 effort 更容易拒絕」的假設
- **AI 生成程式碼著作權分析**：法律分析指出 AI 生成程式碼可能完全不受著作權保護、歸屬雇主，或受開放原始碼授權污染，建議開發者主動記錄自身在 AI 輔助開發中的貢獻
- **AI agent 安全事故**：Cursor + Claude Opus 9 秒刪除生產資料庫並清空備份，引發企業建立沙盒隔離、操作確認與不可逆動作攔截的討論；見 [[topics/ai-agent-safety]]

#### 2026-04-27
- **TDD 驅動開發迴圈**：EvanFlow — 16 個技能 + 2 個子代理人，每步驟設有人工確認節點，不自動 commit，強調使用者控制
- **問題定義優先**：Relay plugin — 強制 Claude Code 在動手寫程式前深入對齊問題定義，核心改變是將 Plan Mode 的提問層級從「實作細節」拉升至「問題本質」
- **精簡 CLAUDE.md 策略**：parsh 案例 — 將 CLAUDE.md 保持精簡、以「規則」而非「建議」形式撰寫，有效減少冗余代碼與漂移行為
- **架構層自動化審查**：modularity plugin — Balanced Coupling 模型分析模組化設計，解決 AI 加速代碼生成同時技術債也加速累積的問題
- **Figma MCP 設計工作流**：Claude Code + Figma MCP 搭配，Creative Bloq 評測 AI 輔助設計效果
- **effort 等級 vs 拒絕率**：系統性測試顯示提升 effort 不增加拒絕率；medium vs high 差異僅在回答深度（正面回應增長 29–47%），拒絕僅增長 11%，顛覆「高 effort 更容易拒絕」假設
- **harness 設計模式實作**：將 Anthropic 官方 harness 設計模式實作為 Claude Code 插件，發現 Claude 常在測試未通過時自信回報「成功」
- **Cerbos 授權政策技能**：將自然語言需求轉換為帶測試案例的結構化 authZ policy，指出 AI 幻覺在此類任務直接導致安全漏洞
- **vibe-coding 里程碑**：非技術背景 PM 以 Claude 在 47 天內獨立開發並上線產品，強調範疇控制與清晰需求撰寫為成功核心
- **多代理瀏覽器**：Rapunzel — 以樹狀標籤頁介面管理多個同時運行的 AI 代理（Claude Code / Codex / Gemini），定位為「Chrome for agents」，解決終端機多代理追蹤困難的問題
- **代理人沙盒**：SmolVM — 讓 Claude Code 與 Codex 在完全隔離的本機沙盒中執行，單指令啟動，支援 git 憑證整合，保護宿主系統安全
- **完成驗證 Hook**：Groundtruth — Stop Hook，強制 Claude Code 在宣告「完成」前必須提供可驗證的執行證明，否則拒絕結束回合，解決 Claude 自信宣稱完成但實際未完成的問題
- **跨工具 Skills 移植**：OpenCode-power-pack — 將 Anthropic 官方 11 個 Claude Code 技能（代碼審查、安全審計、前端設計等）移植至 OpenCode，打破官方插件的工具綁定限制
- **APFS Worktree 優化**：利用 Apple File System 的 clone 機制建立 WorktreeCreate hook，多個 worktree 共享相同檔案不佔額外空間，Mac 用戶實用
- **邊學邊做技能模組**：在完成 Claude Code 架構工作後，提供以認知科學（預測、生成、間隔重複）為基礎的 10–15 分鐘學習練習，讓開發者在使用 AI 的同時累積技術深度
- **MCP 創意實驗**：Doom Inside Claude Code — 將原版 Doom 嵌入 Claude Code 狀態列，可由使用者手動控制或讓 Claude 透過 MCP 自主遊玩，展示 MCP 的創意應用邊界

#### 2026-04-26
- **多人協作編碼**：Claude Squad — 每人以自己的 Claude Code 作為 agent，orchestrator 分派平行任務並自動合併分支
- **多 agent 終端**：mux0 — 開源 macOS 終端機，側邊欄即時顯示 agent 執行狀態（running / idle / needs input）
- **PRD 協作防污染**：agent-order — Codex 與 Claude 各自獨立寫 PRD 再互相批判，避免答案向先開口方塌縮
- **知識框架封裝**：14 本商業書（The Mom Test、$100M Offers 等）轉為 skills，依問題語境自動載入
- **流程自動化**：8 步驟開源專案設定流程包裝為單一 skill，降低貢獻者上手門檻
- **AI 程式碼品質**：lipstyk — 靜態分析工具，專門偵測機器生成程式碼的特有模式
- **模型分層策略**：Sonnet 為主力，需要時讓 Sonnet「諮詢」Opus，聲稱節省約 60% 用量
- **安全邊界研究**：Sonnet 4.6 在 high / max 推理強度下拒絕行為完全一致（26/26），推理努力程度不影響安全邊界

#### 2026-04-25
- **效能監測**：CC-Canary — 讀取 `~/.claude/projects/` JSONL log，自動偵測效能漂移
- **跨模型整合**：claude-anyteam — 讓 OpenAI Codex CLI 加入 Claude Code Agent Teams
- **Web 管理介面**：Claude Code Manager — 集中管理 CLAUDE.md、hooks、skills

---

## 趨勢九演進封存

> 搬自 [[topics/community-pattern-trends]] 趨勢九「跨 Session 記憶層／知識庫」演進最早 5 個節點（2026-11-01 精簡，原文一字不刪）。

- 🔥（估） **跨環境 Agent 記憶協定（ltm）**（5/12）：Core Memory Packet JSON 協定，主張跨編輯器／跨機器／跨模型的供應商中立記憶格式，早期單一嘗試
- 🔥（估） **OKF 物件鍵格式**（6/28）：第二個獨立標準化嘗試，聚焦跨 session agent 記憶的團隊共用格式，與 ltm 同屬「格式標準化」路線但各走各的協定
- 🔥🔥🔥 **CodeAlmanac**（7/22，YC S26，Show HN score 54）：從「記格式」轉向「記文件」——隨對話自動更新 codebase wiki，取代手動維護的 MANUAL.md／DESIGN.md；30 天內無後續採用回饋，2026-08-29 已自 [[topics/community-tech-tools]] 移除追蹤
- 🔥🔥🔥 **OzBrain**（8/21，HN 69，多家報導）：從「單一使用者跨 session」延伸到「team 共享」——主張 agent 與團隊共用知識庫，取代傳統筆記/任務管理工具
- 🔥（估） **手動 Obsidian vault 取代官方自動記憶**（8/24，Reddit）：與前三者「補充記憶層」方向相反的第一個「取代」案例——使用者主張自己策展的 LLM Wiki 比官方自動記憶更可控、更可信賴


## 趨勢三演進封存

> 搬自 [[topics/community-pattern-trends]] 趨勢三演進最早 2 個節點（2026-11-14 精簡，原文一字不刪）。

- 🔥🔥🔥（估） **Context 是核心瓶頸**（5/12）：確認大型專案的真正天花板是 context 管理，而非程式碼生成品質
- 🔥🔥🔥（估） **Context Rot 修復五法**（6/20）：「Claude 越用越笨」幾乎都是 context 腐蝕；五種具體修復策略成社群共識

## 趨勢二演進封存

> 搬自 [[topics/community-pattern-trends]] 趨勢二演進最早 3 個節點（2026-11-14 精簡，原文一字不刪）。

- 🔥（估） **零星嘗試**（4/26）：多 agent 概念出現，但還沒解決「互相踩到彼此檔案」的問題
- 🔥🔥🔥（估） **Git Worktrees 作為隔離原語**（5/23）：找到關鍵解法——每個 agent 配一個 git worktree，檔案系統完全隔離
- 🔥🔥（估） **並行工作流轉型指南**（6/24）：從「單一 prompt 反覆調整」的線性做法，轉為「任務分解 → 並行派發 → 彙整驗證」

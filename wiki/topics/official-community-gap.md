---
page: "topics/official-community-gap"
kind: "topic"
status: "ongoing"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-20"
last_news_update: "2026-09-20"
status_main: "ongoing"
days_since_news: 2
parent: null
children: "['topics/official-community-gap-archive']"
page_role: "hub"
days_since_news_subtree: 2
inbound_links: 32
attribution_count: 15
attribution_last: "2026-09-19"
top_source: "github-issues"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 官方功能 vs 社群痛點缺口分析

**狀態：** ongoing
**領域：** 🛠️ 工具/功能
**開始日期：** 2026-05-17
**最後更新：** 2026-09-20
**最後新聞更新：** 2026-09-20

> **AGENTS.md 已補**（2026-09-20）
> Claude Code v2.1.277（09-18）起原生讀 `AGENTS.md`，不必再寫 `@AGENTS.md` import 或做 symlink。三個邊界：有 `CLAUDE.md` 時預設仍只讀 `CLAUDE.md`；要兩者並讀得在 `/config` 把「Project instructions」改成 `claude-md-and-agents-md`；Bedrock／Vertex／Foundry 或關掉遙測的 session 讀不到。
> 同批更正：2026-08-17 官方一次關掉本頁引用的五個 issue（#6235、#24798、#47023、#24316、#29006），本頁原先把它們當成還在累積的社群壓力。

## 摘要

**2026-09-18 官方補上了本頁掛最久的那一個**：Claude Code 自 v2.1.277 起原生讀 `AGENTS.md`，這一列從「全站讚數最高的未解缺口」變成「已補，但有三個邊界」。

本頁只答一件事：社群喊的痛，官方補了哪幾個、哪幾個還沒補、為什麼沒補，沒補的你現在有什麼選項。**要裝哪個社群工具，答案不在本頁**——看 [[topics/community-tech-tools]]「我卡在這裡」；官方積木各自怎麼用、怎麼疊看 [[topics/anthropic-agent-stack]]；學術文獻主張與 Claude Code 現況的落差是另一個視角，見 [[topics/community-tech-patterns#缺口追蹤：文獻主張 × Claude Code 現況]]。

13 個痛點裡，1 個官方目前沒有任何對應、6 個補了一半、6 個已經能直接用。

---

## 官方補了沒

> ✅ 官方有正式功能、能直接用｜🧪 官方有東西但受限（測試中、須申請、只給企業端）｜❌ 官方目前無對應
> 「核對日」＝這一列最後一次對過官方文件或 CHANGELOG 的日期；`—` 代表還沒對過，要拿它做決定時建議自己再查一次官方文件。
> 每個 issue 現在多少人在吵、官方回了什麼，見 [[entities/claude-code]]。

| 你痛的是什麼 | 官方補了沒 | 官方給的是什麼 | 還缺什麼、你現在能怎麼辦 | 核對日 |
|---|---|---|---|---|
| 想在一個地方操作好幾家 agent | ❌ | 無——官方只管 Claude Code 自己的 session，截至 2026-09-19 官方文件未見 | 只有社群工具，08-24 起一個月冒出 10 款 ⟨G-11⟩ | 2026-09-19 |
| 新開一個 session 它就忘光 | 🧪 | Claude Code 的 auto memory（依你的更正與偏好自己寫筆記，`/memory` 管理，子代理也各有一份） | 跨工具、跨模型、團隊共享仍要靠社群工具；要自己接外部記憶層，四個 session／compact hook 都能用 ⟨G-05⟩ | 2026-09-19 |
| 額度快用完、錢花到哪看不看得到 | 🧪 | `/usage` 拆到 skills／subagents／plugins／各 MCP server 的百分比與每個 loop 的 token、狀態列 `rate_limits`、VS Code 70% 警示橫幅 | 沒有逐次請求的金額，數字是本機估算、不含其他裝置與 claude.ai；告警門檻似乎不能自訂 ⟨G-07⟩ | 2026-09-19 |
| 想自己決定哪段用哪個模型、不被鎖住 | 🧪 | 個人端有 `opusplan`：規劃時用 Opus、開始執行自動換 Sonnet；org default model（v2.1.196）與 `enforceAvailableModels` 白名單則是企業管理端 | 只有這一種固定切換，依成本或任務動態選模型的路由截至 2026-09-19 官方文件未見；換設定差多少錢見 [[topics/model-comparison]] ⟨G-13⟩ | 2026-09-19 |
| 一堆 agent 在跑，看不到誰卡住 | 🧪 | Agent view（研究預覽）每個 session 一列，標出它在跑、在等你、還是做完了；提示列會顯示還有幾個 agent 在等你；`--forward-subagent-text` 可帶出子代理文字 | 看得到單一 session 的狀態，看不到誰在等誰這種依賴關係的全圖 ⟨G-09⟩ | 2026-09-19 |
| Agent 之間直接傳訊 | 🧪 | 跨 session 訊息 `ListAgents`＋`SendMessage`（v2.1.224 起，原生 Windows v2.1.234），可達他機與雲端 | 點對點已跨機器；共享頻道式 A2A（issue #28300 仍開著）與自動依賴排序沒有 ⟨G-10⟩ | 2026-09-19 |
| 它說做完了，但品質夠不夠 | 🧪 | `/goal` 判完成條件（一般功能）、`/code-review`（v2.1.218 起背景執行）；Outcomes 規格驗證屬 Managed Agents，仍是 beta、要帶 beta header | 答的是「做完沒」不是「寫得好不好」；社群的多模型對抗審查無公開對照數據 ⟨G-06⟩ | 2026-09-19 |
| 把多 agent 工作流寫成能重跑的腳本 | ✅ | Dynamic workflows 全部付費方案可用（Pro 要在 `/config` 打開），最多 1,000 平行子代理；Claude Code Projects 可用一個對話協調多個雲端 session | Projects 還是 public beta、只給 Pro 與 Max；本庫因 UltraCode 1.7M token 事件在 [[feature-radar]] 標為暫不推薦，官方未就此發過說明 ⟨G-02⟩ | 2026-09-19 |
| 別家 agent 的 AGENTS.md，它讀不讀 | ✅ | v2.1.277（2026-09-18）起原生讀 `AGENTS.md` | 有 `CLAUDE.md` 時預設只讀 `CLAUDE.md`；要兩者並讀在 `/config` 設 `claude-md-and-agents-md`；Bedrock／Vertex／Foundry 讀不到 ⟨G-08⟩ | 2026-09-19 |
| 它需要你輸入時會不會叫你 | ✅ | 接上 Remote Control 可推手機通知、桌面閒置通知、`Notification` hook、`waitingFor` 可見性 | 社群補的是終端機標籤變色、實體燈號這類形式 ⟨G-03⟩ | 2026-09-19 |
| 把活分給 subagent、編排它們 | ✅ | Managed Agents（beta，須帶 beta header）、`/fork`／`/subtask`、subagent forking 預設開啟（v2.1.232） | 隊友可指名 `.claude/agents/` 的定義（#24316 已於 08-17 出貨），但 `skills`／`mcpServers` 不套用 ⟨G-01⟩ | 2026-09-19 |
| 它會不會跑出破壞性指令 | ✅ | 破壞性 git 指令自動封鎖（v2.1.183）、Sandboxing、`hard_deny`、worktree 隔離（v2.1.222） | git 層已完整；更廣的資源限制仍靠社群沙盒 ⟨G-04⟩ | — |
| Slack 裡要一個 AI 隊友 | ✅ | [[entities/claude-tag\|Claude Tag]]（2026-06-24，Slack 原生） | 這一列的社群前驅稀薄、官方主導色彩強，放在這裡只供對照 | 2026-09-19 |

---

## 目前結論

**官方為什麼還沒補**

上面那個 ❌、下方對照表裡的兩列，加上「花費估不準」這一面，原因不是「還沒排到」，而是官方的動機本身指向別的方向。但它們說的是**到目前為止**的理由，不是預言——AGENTS.md 曾經也在這一節裡，2026-09-18 官方補了。

**花費為什麼還是估不準**：六個以上的成本監測工具（Tokenyst、CostHawk、Usage4Claude、Throttle Meter、Agent FM 等）反映的焦慮是真的。官方現在給得出歸因——`/usage` 能拆到哪個 skill、哪個子代理、哪個 MCP server 吃掉幾成，但給不出「這一次請求花了多少錢」，而且那些數字是這台機器的本機估算，不含你其他裝置與 claude.ai。官方的產品方向（讓 agent 自主執行更久）在結構上讓花費更難預估，6/15 信用池改制又加了一層。這不是技術做不到，是商業模式：用量變多對 Anthropic 有利。

**CLAUDE.md 寫了它不聽**：Writ（語意規則注入）、Caliber（跨工具設定統一）、Patina（腐化偵測）問的是同一件事——怎麼讓 AI 的行為邊界持久、可維護。官方對複雜 CLAUDE.md 幾乎沒有文件指引，`/doctor`（v2.1.206，2026-07-10）只會建議你把已提交的 CLAUDE.md 寫短，沒有碰到「規則被當成參考脈絡而遭略過」這個核心。

**用 AI 寫久了的副作用**：recap（技能退化）、modularity plugin（技術債加速）、AI 命名一致性（命名漂移）指的是長期隱憂。官方公開敘事（Cat Wu 的「AI 主動性」、Boris Cherny 的「數千子代理深度工作」）方向相反，承認這件事會削弱它自己的說法。

剩下那個 ❌（想在一個地方操作好幾家 agent）不在這一節——它太新，官方連表態都還沒有，沒有可寫的理由。

**你的選項**：這三件目前都得自己來——花費自己量（企業端的做法見 [[topics/enterprise-cost-management]]）、規則寫短並搭社群的注入工具、副作用靠自己定期回頭讀 agent 寫出來的東西。

---

**缺口細節**

> 下面提到的社群工具是當時的代表案例，不是現在的推薦；要裝哪個一律看 [[topics/community-tech-tools]]「我卡在這裡」。

- ⟨G-01⟩ 把活分給 subagent、編排它們：2026-07-17 官方把「背景多開新 session」（`/fork`）與「同 session 委派子任務」（`/subtask`）拆成兩個指令；v2.1.232（08-13）讓 `subagent_type: "fork"` 預設繼承完整對話與 prompt cache。
  - 子項缺口已補：issue #24316（自訂 `.claude/agents/` 定義無法當隊友）官方 2026-08-17 關閉，答「spawning a teammate 時可指名 `.claude/agents/` 的定義，隊友照該定義的 `tools` 白名單與 `model`」。
  - 同一則官方留言明說 `skills` 與 `mcpServers` frontmatter 不套用到隊友。代表社群工具：Claude Squad、Harness（multi-worktree）；Boris Cherny 2026-05-13 揭露內部「數千子代理夜間跑批」工作流。
- ⟨G-02⟩ 把多 agent 工作流寫成能重跑的腳本：官方文件現在寫 Dynamic workflows「所有付費方案、Anthropic API、Bedrock、Google Cloud Agent Platform 與 Microsoft Foundry 皆可用」，Pro 要自己在 `/config` 的 Dynamic workflows 那一列打開——已不再標研究預覽。
  - 同一份文件寫：某個 agent 撞到你的 claude.ai 用量上限時，那一次執行會暫停而不是讓該 agent 失敗。
  - Claude Code Projects（public beta）讓一個對話協調多個平行雲端 session，目前只給 Pro 與 Max，Team 與 Enterprise 還沒有。
  - 手機遠端操控那條線已經收掉：issue #28322（`/rc` 不被辨識）官方 2026-08-19 關閉，答 v2.1.76 修好「Unknown skill」、v2.1.206 讓 `/remote-control` 一律解析得到。
  - issue #29006（Desktop 遠端控制 Claude Code session）2026-08-17 關閉，答遠端控制已可用，在「設定 > Claude Code > 預設啟用遠端控制」打開。
  - 代表社群工具：Gorchestra、TBD（agent-channels）、Superset。UltraCode 1.7M token 退款爭議官方沒有專文，這一輪查不到它現在算不算解決。
- ⟨G-03⟩ 它需要你輸入時會不會叫你：官方現在有四種——接上 Remote Control 後長任務結束或需要你決定時推手機通知（2026 第 16 週公告）、桌面閒置通知、`Notification` hook、`waitingFor` 可見性（v2.1.162）。社群工具補的是形式面：claude-needs-input（終端機標籤變色）、氛圍狀態燈（實體 LED）。
- ⟨G-04⟩ 破壞性指令防護：官方對 git 層級防護已完整覆蓋且評價高（🔥🔥🔥 ✅ 推薦）；社群沙盒工具仍在更廣泛的資源限制場景（非僅 git）補位。
- ⟨G-05⟩ 新開一個 session 它就忘光：Claude Code 自己的官方記憶是 **auto memory**——依你的更正與偏好自己寫筆記，`/memory` 管理，子代理也各自維護一份，且跨 git worktree 共享。
  - Dreaming 是 Managed Agents（API 產品）那邊的功能，在 beta 之內還是更受限的研究預覽、須另外申請。
  - 要自己接外部記憶層：`PreCompact`／`PostCompact`（v2.1.76 起）／`SessionStart`／`SessionEnd` 四個 hook 官方確認都有，`SessionStart` 可回傳 `additionalContext` 把記憶注回來。
  - issue #14227（session 間持久記憶）官方 2026-05-25 以 not planned 關閉，見 [[entities/claude-code]]。
- ⟨G-05b⟩ 社群那邊沒有變少：ltm、VIR、CoreMem、OKF、OzBrain、ambient-context、mindmuxai/brain.md 各走不同路——OKF 跨工具跨模型，OzBrain 鎖團隊共享，ambient-context 走被動螢幕記錄，brain.md 走顯式寫入。
  - 它們解的不是 auto memory 解的那一題，所以 auto memory 上線後數量沒有下降。
- ⟨G-06⟩ 它說做完了，但品質夠不夠：官方的 Outcomes 規格驗證現在標 Beta，跟 Managed Agents 共用同一個 beta header；`/goal` 文件沒有預覽或 beta 標示，但它的 check-ins 要 v2.1.234 以上。`/code-review` 自 v2.1.218 起改在背景以子代理執行。
  - 這幾個答的是「任務條件成不成立」，不是「這段程式碼寫得好不好」。社群的 adamsreview、Mira、Read-Only Reviewer Agent 補的是後者，但「多模型對抗審查抓到更多真 bug」的說法雙方都沒有公開對照數據。
- ⟨G-07⟩ 額度快用完、錢花到哪看不看得到：官方 `/usage` 現在會拆到 skills、子代理、外掛與個別 MCP server 各佔幾成，標出佔比 ≥10% 的行為旗標，也給每個 loop 的 token 數；狀態列可讀 `rate_limits.five_hour.used_percentage` 與 `seven_day` 自己做顯示。
  - VS Code 另有額度警示橫幅，門檻 70%；企業端有 Spend Controls（2026-07-04 宣布，控管粒度未公開，見 [[topics/enterprise-cost-management]]）。
  - 官方自己註明：這些數字是從這台機器的本機 session 紀錄算出來的近似值，不含你其他裝置或 claude.ai 的用量。
  - 還缺的比原先寫的窄：沒有逐次請求的金額，也沒有主動推到手機或桌面的額度告警、門檻似乎不能自訂（官方文件未見此設定，不是官方明說沒有）。代表社群工具：LimitBar、CCLimitPing。
- ⟨G-08⟩ 別家 agent 的 AGENTS.md，它讀不讀：**已補**。Claude Code v2.1.277（2026-09-18）起可直接把 `AGENTS.md` 當專案指示讀，官方文件寫「works without adding a `CLAUDE.md`, an import, or a setting」。
  - 三個邊界：有 `CLAUDE.md` 或 `CLAUDE.local.md` 時預設只讀 `CLAUDE.md`；要兩者並讀，把 `/config` 的「Project instructions」設成 `claude-md-and-agents-md`。
  - Bedrock／Vertex／Foundry 或關掉遙測的 session 讀不到，那些場合仍用 `@AGENTS.md` import。issue #6235 官方已於 2026-08-17 關閉，當時給的是 import／symlink 做法，原生支援是一個月後的事。
  - 社群另回報 `.agents/skills` 資料夾不在原生支援範圍內（HN 討論，2026-09-19；官方文件未提）。
- ⟨G-09⟩ 多平行 agent 即時可觀測性／協調地圖：官方 Agent View 為**列表式** session 管理，非跨 agent 即時狀態流的 live map；當數十至上千平行 agent 併跑時「誰卡住、誰在等、彼此依賴」缺乏即時可觀測面，社群自建地圖式檢視器補位，官方無對應方向。2026-07-15 v2.1.211 新增 `--forward-subagent-text` 旗標與 `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` 環境變數，讓 `stream-json` 輸出包含 subagent 文字與思考內容，為社群建構觀測工具提供官方資料來源；2026-07-17 v2.1.212 將 `/fork` 改為建立獨立背景 session（`claude agents` 自成一列），原同 session 子 agent 行為更名 `/subtask`，使多開背景任務與同 session 委派的列表可見度更清楚拆分，但本身仍非官方 live map 產品，狀態未變。
- ⟨G-10⟩ Agent 間直接通訊協定：與上一列「即時可觀測性／協調地圖」的區別：協調地圖是**被動觀測**（讀 transcript/log，agent 本身不互相收送訊息）；本列是**主動通訊**（agent 間或跨機器交換訊息以協調依賴順序），先前只能靠檔案系統或外部工具中繼。
  - 2026-08-09 官方文件確認跨 session 訊息功能，對應 issue #24798（[[entities/claude-code]] 已知問題轉 ✅ 已修復 v2.1.224）；留言持續累積（60→75→78），核心訴求其實是「依相依性排序高階流程步驟」的工作流編排。
  - 2026-09-19 查證：**跨機器已涵蓋**——同機走本機 socket（Windows 為 named pipe），他機與雲端 session 經 Remote Control 由 Anthropic 伺服器轉送，v2.1.225 起可主動發起。
  - 仍未涵蓋：issue #28300 要的 MCP 為底共享頻道／工作區（A2A 協定），文件只給純文字點對點訊息；自動依賴排序也沒有（`ListAgents`／`SendMessage` 僅是原語），故狀態維持 🧪 部分產品化。
  - 2026-08-24 issue #86069（Windows/MSIX 1.28929.0）：訊息送進目標 session 輸入框卻不會自動送出、該 session 無回應；文件載明原生 Windows 自 v2.1.234 起支援，但未載明桌面 MSIX 版是否適用，見 [[entities/claude-code]] 已知問題。
- ⟨G-11⟩ 跨 harness 統一操作層：缺執行期統一操作面，非設定檔互通（⟨G-08⟩）。08-24 起密集湧現，官方僅涵蓋 CC 自身 session。09-10 再添 avibe、ccteam；09-12 再添 orca（ADE，7 天 +4,966★，日增最快），官方狀態不變，見 [[topics/community-tech-tools]]「多 agent 協調混亂」。

- ⟨G-12⟩ Agent 跟 agent 做生意、吵架怎麼判：目前只有 internet-court-skill 一個社群方案在談這件事（自然語言協議＋ERC-7710 委任權限＋x402 支付＋履約爭議仲裁），證據還撐不起單獨成一列，工具本身見 [[topics/community-tech-tools]]。
- ⟨G-13⟩ 想自己決定哪段用哪個模型、不被鎖住：個人端官方只有 `opusplan` 這一種固定切換——規劃模式用 Opus，進到執行換 Sonnet。org default model（v2.1.196，2026-06-29）與 `enforceAvailableModels`（v2.1.175）都是企業管理端的設定。
  - 依成本或任務動態挑模型，截至 2026-09-19 官方模型設定文件未見。代表社群工具：Workweave Router（HN 181，實測降 40%+）、Dragoman、Council、Ungate、Rayline。
  - The Information（2026-09-15）與 Dealroom（2026-09-16）均報導開發者正把 Claude Code 接到非 Anthropic 模型後端執行，兩則都沒有規模數字。

---

## 對照矩陣

> 符號與上表同義（✅／🧪／❌）。

| 社群痛點 | 工具密度 | 官方對應功能 | 收斂程度 |
|---------|---------|-------------|---------|
| CLAUDE.md 規則失效 | ⭐⭐⭐ | 無 | ❌ |
| 平台可及性（行動/瀏覽器） | ⭐⭐ | Claude Code Artifacts（2026-06-18，輸出共享）＋ Claude Cowork 行動/網頁版 beta access（2026-07-07，Max 用戶優先，雲端持續執行） | 🧪（輸入操作面已補上；官方明言桌面版才是完整體驗） |
| AI 輔助開發副作用 | ⭐⭐ | 無（官方敘事方向相反） | ❌ |

---

## 技術彙整

### ✅ 高度對應：多 agent 執行能力

4/28 至 5/16 幾乎每天都有 agent 相關功能（Managed Agents、`/goal`、Agent View、`/loop`/`/batch`/`/background`、`claude agents` 細粒度旗標）。官方與社群在此痛點上罕見同步，但方向略有差異：

- **官方**著重「讓 agent 能自主執行更久、更可靠」
- **社群**著重「讓人能監控和控制 agent」（Omar、HiveTerm、CC-Canary）

兩者互補，但 agent 監控需求官方仍未主動回應。

### ✅ 高度對應：安全邊界

Claude Code Sandboxing（OS 層隔離）、`hard_deny`（不可覆蓋的提示層邊界）、Claude Security（公開 Beta）在 5/06–5/10 集中發布，與 CVE-2026-39861 沙箱逃逸漏洞（5/08）的時間高度吻合。社群安全工具（SmolVM、Trent、DataMoat）在此之後需求有所降溫。

### 🧪 部分對應：輸出品質驗證

Outcomes 規格驗證與 `/goal` 解決了「任務是否完成」的機器可驗證問題，但未解決「程式碼品質是否足夠」的更主觀需求。`adamsreview`、`lipstyk`、`Pilot Shell` 填補的是後者，官方目前沒有對應方向。

### 🧪 部分對應：跨 session 記憶

Claude Code 自己的官方記憶是 auto memory（依你的更正與偏好自己寫筆記，`/memory` 管理，子代理也各自維護一份），官方有這一面了，但還有已知毛病（見 [[entities/claude-code]]）。Dreaming 是 Managed Agents 那邊更受限的研究預覽，不等於「每次開新對話可以繼續上次」。社群 8+ 記憶工具在 auto memory 上線後沒有減少，說明兩者解決的不是同一個問題。差距仍大。

**2026-08-04 社群訴求成型：** GitHub issue [#47023](https://github.com/anthropics/claude-code/issues/47023)「Expose compact/session lifecycle hooks for external memory layers」彙整 5 個既有開放 issue（#14227、#32627、#34192、#34556、#46138），指出社群已自行拼湊三層式 markdown 架構、知識圖譜等替代方案，訴求官方開放 compact／session 生命週期 hook 供外部記憶層串接——這是社群首次把散落的持久化記憶需求收斂為單一具體 API 訴求（hook 介面），而非各自繼續造輪子；#47023 已於 2026-08-17 CLOSED／COMPLETED，官方答四個 hook（`PreCompact`／`PostCompact`／`SessionStart`／`SessionEnd`）今天都有；彙整清單中的 #14227 為 CLOSED／NOT_PLANNED（2026-05-25）。

**2026-08-09 缺口的兩個切面各自累積：** #47023 彙整清單中的兩個成員本日各自延燒——跨 session 記憶訴求 [#14227](https://github.com/anthropics/claude-code/issues/14227) 累積至 34 則留言、跨 compaction 記憶訴求 #34556 累積至 62 則留言，合計 96 則留言；兩者訴求範圍不同（跨 session vs. 單一 session 內跨壓縮），但同屬本缺口，官方仍無回應，狀態不變。

### 🧪 部分對應：平台可及性

Claude Code Artifacts（2026-06-18）讓工作階段進度可即時輸出為可共享互動網頁（PR 摘要、系統說明文件、儀表板、釋出清單），任何人可在瀏覽器直接瀏覽，無需安裝工具。這部分解決了「非工程師團隊成員無法看到 Claude 工作成果」的共享缺口。

**2026-06-25 進展：** Anthropic 曾測試 Claude Cowork 行動（mobile）版本，BleepingComputer 與 Techzine 等多家媒體確認報導，當時仍為測試階段。

**2026-07-07 beta access：** Claude Cowork 官方 blog 發布日為 2026-07-07，用詞是 beta access，首波開放 Max 訂閱用戶，任務可在雲端持續執行、闔上筆電或關閉裝置也不中斷，此次擴展也涵蓋政府機構客戶；The Verge、TechCrunch、WIRED、NBC News、The New Stack 等多家媒體同步報導。這是「輸入操作」面的首次正式填補——使用者可在手機或瀏覽器直接指派任務給 Cowork，不再僅限 Artifacts 的輸出共享。官方明言桌面版才是完整體驗，網頁與行動版用不到本機檔案與瀏覽器；矩陣狀態維持 🧪。

### 🧪 部分對應：多模型路由 / 鎖定防禦

v2.1.196（2026-06-29）新增 org default model 功能，企業管理員可在 org console 統一設定組織預設模型，使用者在 `/model` 看到「Org default」選項。v2.1.175 的 `enforceAvailableModels` 則可強制限制可用模型清單。個人端官方只有 `opusplan` 這一種固定切換（規劃用 Opus、執行換 Sonnet）。

這兩個功能覆蓋的是**企業側的模型管控**需求，與社群訴求（個人用戶在複雜 agent 場景中的多模型動態路由、成本最佳化路由）仍有本質差距。社群工具（Dragoman、Council、Ungate）填補的是後者，官方目前無對應方向。The Information（2026-09-15，僅標題）報導部分開發者正找方法在 Claude Code 中繞開官方模型、改接其他供應商，方向與本列社群訴求一致，惟原文無可讀內文，具體手法與規模未載。Dealroom（2026-09-16，2 個來源同日報導）同向補充：開發者傾向把 Claude Code 接到非 Anthropic 模型後端執行，Anthropic 因此收不到對應 token 費用，惟同樣未附具體規模數字。

---

## 相關實體

- [[topics/community-tech-tools]] — 該裝哪個社群工具，答案只在這裡（「我卡在這裡」症狀決策表）
- [[topics/anthropic-agent-stack]] — 官方的 agent 積木各自為什麼出、怎麼疊起來
- [[topics/community-tech-patterns]] — 社群拿這些工具玩出哪些做法、哪些已經站住腳
- [[topics/community-tech-discussions]] — 社群在吵的觀念問題（「該不該這樣用」；本頁答的是「有沒有這個功能」）
- [[feature-radar]] — 這禮拜官方動了什麼、值不值得現在跟
- [[entities/claude-code]] — Claude Code 現在有哪些毛病、哪些修了，以及每個 issue 的留言與讚數

## 時序

### 2026-09-20
- **AGENTS.md 由缺口轉為已補**：Claude Code v2.1.277（09-18）起原生讀 `AGENTS.md`，本頁該列自 ❌ 改 ✅ 並補三個邊界；同時更正 08-17 官方一次關閉的五個 issue（#6235、#24798、#47023、#24316、#29006）與 #14227（05-25 標為不打算做），本頁原先仍當它們是進行中的社群壓力。
- **「通知」與「額度監控」兩列低估官方**：手機推播（2026 第 16 週）、桌面閒置通知、`Notification` hook 使前者改 ✅；`/usage` 的歸因拆解、狀態列 `rate_limits`、VS Code 70% 警示橫幅使後者的缺口收窄為「沒有逐次請求金額、不含其他裝置、告警不能自訂」。
- **「跨 session 記憶」比錯了對象**：Claude Code 使用者的官方記憶是 auto memory，不是 Managed Agents 的 Dreaming；四個 session／compact hook 官方確認都存在。
- **另有四列狀態更正**：Dynamic workflows 已開放所有付費方案、不再是研究預覽（另收 Claude Code Projects public beta）；Agent view 是研究預覽而非「官方無對應」；Outcomes 為 beta；個人端模型切換官方只有 `opusplan`。
- **Cowork 網頁／行動版的範圍問到了**：官方發布日為 2026-07-07、用詞是 beta access（先開放 Max），且明說桌面才是完整體驗——網頁與行動版用不到你本機的檔案與瀏覽器。本頁原記的「正式擴展（07-08）」與「功能範圍是否等同桌面待觀察」兩點就此結清。
- **internet-court-skill 的採用程度查過了**：5,855★、106 forks，但只有 9 位 watcher、4 筆 commit、1 位貢獻者，2026-08-19 後未再更新；星數不足以當作被採用的證據，該列改為據實記載。
- **「agent 跟 agent 做生意」這條線先不單獨列**：2026-09-19 查 internet-court-skill 本身——5,855★、106 forks，但只有 9 位 watcher、1 位貢獻者、4 筆 commit，2026-08-19 後未再更新。
- 一個工具的星數撐不起一整條缺口，等有第二個獨立方案再說；工具本身見 [[topics/community-tech-tools]]。
- **同一個痛點不再有兩個互相打架的狀態**：先前「多模型路由」一處寫「官方無對應」、另一處寫「部分對應」，跨 session 記憶也有兩個狀態；現在每個痛點只有一個狀態，並標出最後一次對過官方的日期。
- **「Slack 裡要一個 AI 隊友」這一列開始計時**：這一列的社群前驅一直只有 Ano 一個，開列日在本頁時序上查不到；自 2026-09-20 起算，若往後 90 天社群這邊仍無新東西、官方也沒動，就把它移出表。

### 2026-09-19
- **「Agent 間直接通訊協定」列查證更新（使用者提問）**：⟨Q-01⟩ 結案——跨機器已涵蓋、原生 Windows 自 v2.1.234 起支援；v2.1.224 release notes 本就載明此功能（08-08、08-09 條目稱「changelog 未見」為漏看）。#28300 的共享頻道式 A2A 仍缺，維持 🧪。
- **AGENTS.md 原生支援還沒涵蓋的一塊**：`.agents/skills` 資料夾不在內（HN 討論指出，社群回報，官方文件未提）。

### 2026-09-16
- **多模型路由/鎖定防禦再添佐證**：Dealroom（2 個來源同日報導）稱開發者傾向讓 Claude Code 接到非 Anthropic 模型後端執行，與 09-15 The Information 報導方向一致；矩陣狀態維持 ⚡ 部分對應，未見具體規模數字，不升級。

### 2026-09-12
- **orca**（stablyai/orca，多 agent ADE，用既有訂閱跑任意 coding agent，7 天 +4,966★）併入既有 ⟨G-11⟩ 跨 harness 統一操作層代表工具清單，非新模式。
- **spec-kit**（github/spec-kit，Spec-Driven Development 入門工具包，7 天 +2,311★）與官方 Outcomes 規格驗證＋`/goal` 概念重疊，不新增矩陣列。
- **comet**（rpamis/comet，把想法轉成可評測工作流程的 agent skill harness，3,023★，今日首次收錄）僅一行摘要、缺動能數據，證據不足暫不處置，待更多案例佐證再評估。

### 2026-09-11
- 評估 09-10 社群新增 9 筆 agent 工作模式條目：avibe、ccteam 併入 ⟨G-11⟩；OtoDock 為既有工具細節補充，非新缺口；Nightshift 記於 [[entities/claude-code]] 待查證；Security Cards、Hordev、dsh-TUI、better-agent-terminal、Orchestrator 密度或性質皆不足以新增缺口列。

### 2026-09-03
- **新增矩陣列「Agent 間商業/支付基礎設施」**：internet-court-skill（2026-08-18 首見，5,317★）提出 agent-to-agent 經濟往來信任層方案（自然語言協議＋ERC-7710＋x402 支付＋爭議仲裁），官方無任何對應，新增 ❌ 無官方對應列；工具星數缺乏 forks/issues 佐證，證據強度標注保留。
- **評估 dev.to「7 of My 8 Claude Code Agents Had Zero Calls」不新增矩陣列**：作者盤點自訂 subagent 使用紀錄、建立殭屍 agent 自動偵測機制，屬單一使用者第一手實測而非工具/repo，證據密度不足以獨立成列；與 ⟨G-09⟩ 多平行 agent 即時可觀測性談的「執行中誰卡住」不同層（本則談的是「哪些配置的 agent 從未被呼叫」），暫不歸入任何既有列，待更多獨立案例佐證同類「agent 使用率/生命週期監控」需求再評估。

### 2026-08-25
- **「跨 session 記憶持久化」新增兩個代表社群工具**：ambient-context（Show HN，score 51，Accessibility API 讀螢幕文字寫成 Markdown 日誌）與 mindmuxai/brain.md（GitHub Search，504★，零依賴檔案式跨 session「專案大腦」）；兩者取徑不同於既有 OKF／OzBrain，但均未觸及官方 Dreaming 尚未涵蓋的缺口，矩陣狀態維持 🧪 部分產品化。另評估同日新增的 rsmdt/the-startup（commands／skills／agents 打包套件）與 l3a0/claude-plugins 的 Kindle highlights OCR skill：前者屬既有「打包驗證過配置」取向的另一實例，非新工作模式，不對應任何矩陣列；後者為特定消費服務（Kindle）的個人化 OCR 應用，非可與官方 agent 工作模式路線圖比較的一般性痛點，兩者均不新增矩陣列。

### 2026-08-23
- **「跨 session 記憶持久化」代表社群工具新增 OzBrain**：2026-08-21 Show HN 發布，鎖定跨 agent／團隊共享知識庫（而非單一使用者跨 session 記憶），主張取代傳統筆記/任務管理工具；矩陣狀態維持 🧪 部分產品化（Dreaming 未觸及團隊共享面向）
- **「Subagent 派工/編排」新增子項缺口回報**：GitHub issue #24316 反映自訂 `.claude/agents/` 定義無法加入 agent team 作為隊友；矩陣狀態維持 ✅ 已產品化，缺口分析欄補記此子項

### 2026-08-13
- **v2.1.232：Subagent forking 預設開啟**：帶 `subagent_type: "fork"` 的 subagent 現在預設繼承完整對話與 prompt cache；「Subagent 派工/編排」的官方對應再進一步降低手動設定門檻，矩陣狀態維持 ✅ 已產品化

### 2026-08-09
- **「Agent 間直接通訊協定」列官方文件確認（取代媒體報導階段）**：官方文件（code.claude.com/docs/en/cross-session-messaging）正式確認 Claude Code 跨 session 訊息互通功能，需 v2.1.224 以上版本、限 macOS／Linux，工具為 `ListAgents`＋`SendMessage`；已知問題 #24798 狀態由懸置轉為 ✅ 已修復 v2.1.224，矩陣狀態維持 🧪 部分產品化（同機通訊已確認，跨機器 A2A 需求 #28300 涵蓋範圍未載明）
- **「跨 session 記憶」缺口新增獨立訴求範例**：GitHub issue #14227（跨 session 持久記憶，34 則留言）與既有 #34556（跨 compaction 記憶，62 則留言）合計 96 則留言，凸顯此缺口官方仍無直接對應；矩陣狀態維持 ⏳ 正在做但不夠

### 2026-08-08
- **「Agent 間直接通訊協定」列首度出現官方對應線索（未經 changelog 證實）**：MacRumors、The Mac Observer、biggo.com、Inshorts、9to5Mac 五家媒體同步報導 Claude Code 新增跨 session 訊息互通功能（macOS/Linux），直接呼應 issue #24798、#28300 的長期訴求；GitHub release 資料查無對應 changelog 條目，暫無法確認具體版本號，矩陣狀態從 ❌ 升為 🧪 部分產品化（媒體報導，未經官方 changelog 證實）

### 2026-08-04
- **v2.1.222：worktree session 隔離漏洞修復**：修復 worktree-isolated session 與其 subagent 可對主 checkout 執行破壞性 git 指令的問題，隔離範圍擴大至每個 session 的檔案編輯與 Bash 執行；「安全隔離」對照矩陣列的官方對應清單新增此修復，矩陣狀態維持 ✅ 高度對應

### 2026-07-22
- **v2.1.218：`/code-review` 改為背景 subagent 執行**：「多代理 PR/程式碼審查」的官方對應再進一步——審查工作不再佔用對話內容，且維持 stacked slash commands 作為審查對象；矩陣狀態維持 🧪 部分產品化，社群「adversarial 多模型審查」說法的對照數據仍缺

### 2026-07-17
- **v2.1.212：`/fork` 改為背景 session 化，`/subtask` 承接同 session 子 agent 語意**：「Subagent 派工/編排」的指令介面更明確拆分為「多開背景 session」與「同 session 委派」；「多平行 agent 即時可觀測性」缺口的列表管理面再進一步，但仍非即時依賴關係 live map，矩陣狀態維持 ❌ 無官方對應

### 2026-07-15
- **v2.1.211 新增 `--forward-subagent-text` 旗標，為「多平行 agent 即時可觀測性」缺口提供官方資料來源**：`stream-json` 輸出可包含 subagent 文字與思考內容，讓社群建構觀測/監控工具時不必自行拼湊資料來源；但官方仍未推出 live map 類產品，矩陣狀態維持 ❌ 無官方對應

### 2026-07-08
- **Claude Cowork 正式擴展至行動裝置與網頁版**：首波開放 Max 訂閱用戶，任務可雲端持續執行、涵蓋政府機構客戶；「平台可及性」缺口的輸入操作面首度正式填補（先前僅 Artifacts 覆蓋輸出面），矩陣狀態維持 ⚡ 部分對應（官方稱完整體驗仍限桌面版）

### 2026-06 時段總結
- 「平台可及性」缺口本月首度部分填補：Claude Code Artifacts（06-18，輸出共享）升矩陣狀態至 ⚡；官方研究揭露 40 萬場 session 顯示領域專業度是效能倍增器（06-26），並同步測試 Cowork 行動版
- 「多模型路由/鎖定防禦」本月首度部分填補：v2.1.196 org default model（06-30）供企業端統一設定預設模型，個人用戶動態路由缺口仍未解
- 原始條目見 [[topics/official-community-gap-archive#2026-06]]

### 2026-05 時段總結
- 05-17 初版建立缺口矩陣：識別 5 個官方未對應的核心缺口並分析結構性原因
- 同日新增「CLAUDE.md 規則失效」缺口佐證：Claude Skills `ask_user_input_v0` 靜默限制、Skills 觸發子 agent 派生問題，以及 HN 廣泛討論 CLAUDE.md／AGENTS.md 維護效益、指令常被忽略
- 原始條目見 [[topics/official-community-gap-archive#2026-05]]

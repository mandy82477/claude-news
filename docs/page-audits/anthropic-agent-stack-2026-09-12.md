# 健檢卡：topics/anthropic-agent-stack（第 13 波，2026-09-12）

健檢者：健檢卡 agent。對象 `wiki/topics/anthropic-agent-stack.md`（116 行，含 frontmatter；行號一律檔案原始行號）。子頁 `wiki/entities/managed-agents.md`（146 行）。
機械輸入：`wiki_graph.py explain topics/anthropic-agent-stack`（出 14／入 6）、`similar`、`table_census.py`。
不開藥、不猜官方現況——官方事實一律引 `anthropic-agent-stack-2026-09-12-verified.md`（以下稱 V）。

---

## 1. 使命句候選（≤2）

**A（使用者已批，推薦）**
> 每個官方 agent 積木是為了解決什麼痛而出，讓我多做出哪些工作流。

**B（替代，僅供對照）**
> 官方 agent 積木各自打開了哪種做法——沒有它之前你只能怎麼做、有了之後你能跑出什麼，以及它現在還做不到什麼。

B 的唯一理由：A 的後半句對八個積木裡的兩個撐不起。V 第一節對 agent view 與 self-hosted runner 給的官方句是「使用時機」與「換來什麼」，**沒有工作流場景**（V:L16、V:L18），照 A 寫會被迫用通用工程常識補，違反 skill 原則第 4 條（資料撐不起的裁決句製造假結論）與 features 規則 L286「不得以通用工程常識補」。B 用「它現在還做不到什麼」把那兩塊的誠實出口留好。

**推論：**A 仍優於 B——A 更短、更像讀者問句，且 B 的出口可以用 A ＋每卡一行「它現在還做不到」達成，不必改使命句。建議維持 A，把「做不到」寫成卡片固定第三欄。

---

## 2. 考題集（四題：讀者起點、預測跳數＝開頁數、預測卡點行號與原句）

跳數口徑依第 12 波校準：**index 算一跳**。

### Q1　dynamic workflows 官方為什麼出，沒有它之前會撞到什麼牆？

- **讀者起點**：`wiki/index.md` L30「我想讓 agent 自己跑幾小時／過夜，該用哪個（`/goal`、subagent、dynamic workflows、Managed Agents、Agent SDK）→ `[[topics/anthropic-agent-stack]]`「你該用哪個」」——這是全站唯一逐字寫出 dynamic workflows 的路由列，命中率高。
- **預測跳數**：**2**（index → agent-stack）。
- **預測卡點**：L54 選型表第 3 列儲存格「一件事要幾十個 agent（全庫掃描、大規模遷移、交叉查證），或要把編排寫成可重跑的 script」。這是**什麼時候選它**，不是**為什麼有它**。讀者往下捲會撞到第二個卡點 L81 末「判斷式：**這個編排下週還會照原樣再跑一次嗎？**」——這行是給已經懂的人做決定用的，不解釋牆在哪。
- **頁面最接近答案的兩處**：L41 摘要「先前 agent 之間只能互傳訊息、沒辦法排定誰先誰後」、L81「計畫不再由 Claude 逐回合決定」。兩處都是本頁自己的敘述；V:L13 的官方原句是 "A workflow moves the plan into code… A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer" 與 "The difference is who holds the plan"——**「context 被中間結果塞爆」這個真正的痛，頁面寫在 L65「形狀」而不是「為什麼」**。
- **預測結果**：**半拿到**（拿到抽象的「編排缺口」，拿不到「沒有它之前我要自己在對話裡逐回合盯著、context 被中間結果吃光」）。

### Q2　我現在用 subagent 加 workflows 能跑出什麼具體工作流？要一個能照做的場景，附最小指令。

- **讀者起點**：index L30。次高風險起點是 index L28「我卡住了（…agent 互踩…）→ `[[topics/skill-interest-watch]]`」——該列排在 L30 之前，第 8／9 波冷讀者連兩次被它吸走（ledger 第 8 波回訪第 1 項），本題「我想跑一個多 agent 流程」極可能再中一次，那會多浪費一跳。
- **預測跳數**：**3–4**（index → agent-stack → coding-workflow-guide 第 6／9 段，再折返）。L60 明文把讀者送去 guide「四級驗證階梯見 [[topics/coding-workflow-guide]] 第 6、9 段」，而 guide L77 又把「我想讓它自己跑幾小時／過夜」送回本頁——**兩頁互指成環，Q2 的答案不在環上任何一點**。
- **預測卡點**：L66「Dynamic workflows 怎麼觸發：prompt 帶 `ultracode` 關鍵字或直說「use a workflow」」——讀者拿到觸發方式後的下一個問題「那我打什麼內容？」頁面沒有下一句。第二個卡點是 L81 結尾原句「社群拿它玩出什麼配置，尚無社群配置回報（2026-09-10）」——這是本頁對 Q2 的正面棄權。
- **對照**：V:L13 列出官方**六個可逐字抄的 prompt 範本**（route handler 稽核＋對抗驗證、`npx tsc --noEmit` 修到過、JS→TS 逐檔隔離遷移、PR 逐檔審後合併排序、三家競品並行研究、flaky test 重跑）。本頁引用了 workflows 官方文件三次（L65／L67／L81），**六條範本一條都沒落地**。
- **預測結果**：**沒拿到**。

### Q3　agent teams 加跨 session 傳訊讓我多做什麼，跟 subagent 差在哪？

- **讀者起點**：index L30（該列五種形態**不含 agent teams、不含 cross-session messaging**，讀者不確定該不該進本頁）或 index L102 摘要「五種形態怎麼挑、積木怎麼組」。本頁 L29 別名有 `agent teams, cross-session messaging`，但別名不進 index、不可搜。
- **預測跳數**：**3**（index → agent-stack → entities/claude-code 找 teammate 定義；`reader-notes.md` L20 記載 teammate 軸線的家在 claude-code 的 subagent 型別差異表）。
- **預測卡點**：L83 原句「以及互動 session 下的 agent teams（實驗性、預設關閉）——由主對話帶 `name` 派出的 teammate 可被點名傳訊。」**agent teams 在全頁只有這半句，而且與 cross-session messaging 綁在同一層同一段**，讀者分不出哪個能力屬於哪個積木。
- **對照**：V:L14 的官方分界句 "Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own"，以及官方先勸退句 "Before you set up a team, check whether a lighter option does the job"——**頁面零覆蓋**。官方四類場景與兩個逐字 prompt（三 reviewer 審 PR #142、五 teammate 互相反駁）亦零覆蓋。
- **預測結果**：**半拿到**（拿到「能點對點傳純文字、不傳歷史」，拿不到 teams vs subagent 的分界，也拿不到「什麼時候不該開 team」）。

### Q4　這頁跟 topics/coding-workflow-guide、entities/managed-agents 三頁分不分得出差別？

- **讀者起點**：index L102（Topics 表本頁摘要列）→ 本頁 → 兩個鄰居。
- **預測跳數**：**3**。
- **預測卡點**：L95–97「子頁怎麼分」表只有一列，欄名是「子頁答什麼」——**它說得出子頁答什麼，說不出母頁答什麼**，讀者要反推。第二個卡點在子頁 `managed-agents.md` L56–57「最適合／不適合」兩格，與母頁 L55 選型表第 4 列儲存格是同一件事的兩個版本；子頁 L59 的互指句「跟其他官方 agent 形態怎麼挑…見上層」寫得比母頁自己的分工句清楚。
- **本頁 vs guide 的分工句**：本頁無專句；guide L77 有「各選項的分界見 [[topics/anthropic-agent-stack]]「你該用哪個」」，features 規則 L20 也明文規定 guide 第 6 段留出口。**單邊**——母頁沒有反指句說「流程視角看 guide」，只有 L107 相關實體一行「「我在做這件事該用哪個」的流程視角」，位置在頁尾。
- **預測結果**：**拿到，但有摩擦**。分得出（三頁各有一句能說），摩擦在兩張選型表看起來都在做選型、且分工句只有單邊。

---

## 3. 逐節診斷

「雷達」＝會隨官方動作每週變的現在式；「百科」＝寫一次就長期有效的解釋。

| # | 節（行） | 服務哪幾題 | 雷達／百科 | 去向 |
|---|---|---|---|---|
| 1 | frontmatter＋頁首 L1–36（含 callout L34–35） | 無 | 雷達 | **留**。callout 現在寫的是 SDK 版號（「積木架構本身無變動」），對使命句 A 零貢獻——改為每次覆寫「本週哪個積木的『為什麼／能跑什麼』有新官方說法」 |
| 2 | `## 摘要` L39–41 | Q1（半）、Q4 | 雷達 | **改寫**。現行末句「本頁回答兩個問題：這件事該交給哪種 agent 形態（選型表），以及積木之間怎麼組（架構節）」＝舊使命句逐字，與新使命句 A 直接打架，必改。L41 的「編排缺口已被補上大半」是全頁唯一的痛點句，應升格為八卡導言 |
| 3 | `## 你該用哪個` L45–56（5 欄 5 列，`table_census` 判 unknown 成長、有機制） | Q1（半）、Q3（半）、Q4 | 雷達 | **降附錄（使用者已定，不砍）**。它答的是「選哪個」，A 問的是「為什麼有」——兩者都要，但順序倒了。附錄位置要保留 index L30 的可達性（見第 4 節風險） |
| 4 | `選型細節` L58–71（12 條 bullet） | Q1、Q2（半）、Q3 | 混雜 | **拆**。這 12 條現在同時裝四種東西：官方事實（L60、L65、L67）、已被 V 推翻的事實（L61、L62、L63）、計費（L68–70）、社群對照（L70、L71）。八卡改版時，L60／L65／L67 是唯一可直接搬進卡片「能跑什麼」欄的素材；L68–70 計費三條的家在子頁與 pricing，此處是副本 |
| 5 | `## 這些積木能組出什麼架構` L73–89（導言＋六層＋hooks） | Q1（半）、Q3（半） | 百科 | **降附錄（使用者已定）＋抽料**。這是全頁寫得最好的散文，但它的軸是「架構層級」不是「積木」——agent teams、agent view、self-hosted runner 三個積木**只以半句寄居在別層裡**（L83／L79／L85），這正是 Q3 卡點的結構成因。八卡的「互動模式」與「社群拿它玩出什麼」兩欄全部可從這裡抽，抽完六層才降附錄 |
| 6 | `## 子頁怎麼分` L93–97（1 列） | Q4 | 百科 | **留，改欄**。一列表格的成本不值回票價，但它是母子分工的唯一明文；建議並進摘要成一句，或加一欄「母頁答什麼」讓它雙向 |
| 7 | `## 相關實體` L101–108（6 條，全為樣板邊） | Q4 | 百科 | **留**。L107 對 guide 的描述句是全頁最好的分工句，但位置在頁尾，Q4 讀者到不了 |
| 8 | `## 時序` L112–116（3 條，全是 2026-09-10 建頁當天） | 無 | 雷達 | **留**。建頁才兩天，時序還不需處置；但三條全同日、內容是「本波查了什麼」而非「官方做了什麼」，屬編輯部進度報告口吻（第 1 波同型未修項） |

### 本波主軸：八個積木的兩欄盤點

判準——**「官方為什麼出」**：頁面有沒有寫「沒有它之前撞到什麼牆」或官方自己的存在理由（只寫「什麼時候選它」＝半，只寫「它做什麼」＝無）。**「可照做的工作流場景」**：要**場景＋可貼上就跑的最小指令**兩者；只有其一＝半，光是指令名（`claude agents`）不算最小指令。

| 積木 | 官方為什麼出 | 行號／原句證據 | 可照做的工作流場景 | 行號／原句證據 |
|---|---|---|---|---|
| `/goal` | **無** | L52 只有「選它的分界」；L77「你給一條可執行的完成檢查，它自己跑到符合為止」＝它做什麼。V:L11 的官方理由「a small fast model checks whether the condition holds／completion is decided by a fresh model rather than the one doing the work」——**evaluator 是另一個模型**這件事全頁零字 | **半** | L60「最小用法 `/goal npm test 執行結果零失敗`」＝唯一符合「最小指令」的一處；但無場景，V:L11 官方四例（migrate a module／implement a design doc／split a large file／issue backlog）零落地 |
| 內建 subagent | **半** | L53「只是要把大量讀檔丟進獨立 context」呼應 V:L12「a side task would flood your main conversation」，但寫成選型分界、非存在理由 | **無** | L63 有 `claude --agent <名>`、L64「隔天 `--continue` 接續」＝能力描述。V:L12 的續用範例（code-reviewer 審 auth module → 接著審授權邏輯）零落地 |
| Dynamic workflows | **半** | L41「先前…沒辦法排定誰先誰後」＋L81「計畫不再由 Claude 逐回合決定」；皆本頁自述，非官方錨句。V:L13 的真痛（context 只留最終答案）被寫在 L65「形狀」欄 | **無** | L54「全庫掃描、大規模遷移、交叉查證」＝三個名詞；L66 只有觸發字 `ultracode` 與內建範例名 `/deep-research`。V:L13 六條官方 prompt 範本零落地 |
| Agent teams | **無** | 全頁僅 L83 半句「互動 session 下的 agent teams（實驗性、預設關閉）」＋L29 別名＋L115 時序。V:L14 的官方分界句與勸退句零覆蓋 | **無** | 零。V:L14 兩個逐字 prompt（三 reviewer 審 PR #142、五 teammate 互相反駁）與「3–5 位起步」零落地 |
| Cross-session messaging | **半** | L83「原始需求（issue #24798，75 則留言）要的『依相依性排序高階流程步驟』…」——寫的是**社群**要什麼，不是官方為什麼給；且 V:L31 判此句兩處失實（issue 已 CLOSED、84 則；「由 workflows 承接」是本頁推論） | **無** | 零。V:L15 三條官方 prompt（問另一個終端機的 migration 好了沒／通知 @api-worker／`notify_when_idle`）零落地 |
| Agent view | **無** | L79 半句「agent view（`claude agents` 面板，研究預覽）——把獨立任務丟給背景 session、一個畫面看狀態」＝它做什麼 | **無** | 只有指令名 `claude agents`；`claude --bg "…"` 與 worktree 自動隔離（V:L16）零落地 |
| Managed Agents | **半** | L55「要跑數小時以上並跨 session 保留狀態，或需 20 路並行、資料不出境」＝V:L17 六條 when-to-use 的三條；但官方核心理由「Instead of building your own agent loop, tool execution, and runtime」零覆蓋 | **無** | 零場景零指令。L68–70 是計費算式，不是工作流 |
| Self-hosted runner | **無** | L85 半句「`claude self-hosted-runner`（v2.1.224，Team 與 Enterprise）」＝它是什麼。V:L18 的三個換來的東西（network access／custom tooling／compliance）零覆蓋 | **無** | 只有指令名；V:L18 場景（cloud session 碰內網 DB／registry、runner image 預裝內部 CLI）零落地 |

**合計：16 格中「無」11 格**（為什麼出 4／8：`/goal`、agent teams、agent view、self-hosted runner；工作流 7／8，唯一非無是 `/goal` 的半格）。**「有」零格。**

**結構歸因（推論）**：不是漏寫，是**軸選錯了**。頁面的兩個軸是「選型（表）」與「架構層級（散文）」，兩者都是**積木之間的關係**；使命句 A 問的是**每個積木自己的來歷與產出**，這個軸在頁面上不存在。所以八個積木裡有三個（agent teams、agent view、self-hosted runner）只能以半句寄居在別的積木那一層底下——這也同時解釋了 Q3 為什麼卡住。

---

## 4. 鄰居分工＋節點去留

| 頁 | 入邊 | 它答什麼（一句） | 與本頁的邊界 | 節點三問 |
|---|---|---|---|---|
| `topics/anthropic-agent-stack`（本頁） | 6 | 官方 agent 積木各自為什麼出、讓我多做出什麼 | — | **留**。八個積木的來歷與產出全站只有這裡收；問題是現在收得不夠（16 格 11 無），不是不該收 |
| `entities/managed-agents` | 33 | 代管平台產品本身：現況、計費、零件成熟度、歷史 | 母子。子頁 L59 的互指句寫得比母頁清楚 | **留**。有自己的時序（L116 歷史記錄 17 列）、自己的懸置（pending 1／逾期 1）、入邊 33 遠高於母頁 6——是被獨立引用的頁。但**子頁 L56–57「最適合／不適合」與母頁 L55 選型列重複**，去重一處 |
| `topics/coding-workflow-guide` | 24 | 一條開發流程九個階段，每段官方給了什麼、社群補了什麼、還缺什麼 | 本頁＝形態（該用哪種 agent），guide＝流程階段（我現在在哪一步）。規則檔 L20 已明文 | **留**。但**分工句單邊**——guide L77 指得過來，母頁只有 L107 頁尾樣板句指回去。八卡改版時在摘要補一句反指 |
| `topics/official-community-gap` | — | 社群發明的 agent 工作模式，官方做出對應產品了嗎（矩陣 9 類痛點） | gap＝官方**有沒有**對應（缺口視角），本頁＝官方**為什麼**這樣做＋怎麼用 | **留，但邊界最模糊**。gap L30「Multi-agent workflow 腳本化」列的「官方對應」欄與本頁 L81 第三層講同一件事，兩處日期與狀態不同（gap 寫「2026-05-28，Research Preview」，本頁寫「全部付費方案」）——**跨頁事實打架，需回掃**（同維護者，皆功能記者） |
| `topics/community-tech-patterns` | — | 社群拿 Claude Code 玩出哪些做法的逐則記錄 | 本頁六層每層末段的社群案例都是 patterns 的摘錄 | **留**。本頁只有樣板邊 L108 指過去，六層散文裡引用的七個社群案例（147 subagent、殭屍 agent、Concord、cumora、brain.md、OzBrain、meta-harness）**一個都沒有 wikilink 回 patterns**——違反「每個事實只有一個家」，八卡的社群欄應改為指路而非重述 |

**額外一筆（不在本波五頁，但機械輸入指出）**：`wiki_graph.py similar` 第一名是 `topics/community-large-codebase-workflow`（0.27，共享 managed-agents＋coding-workflow-guide），`wiki/log.md:6229` 已把這兩頁登記為**併頁候選（擱置 0 週）**。本波不處置，但八卡改版後兩頁的重疊會變大或變小，屬回訪項。

---

## 5. 表格生命週期（`## 你該用哪個` 五列各自何時過期）

`table_census.py`：本頁 2 張表（選型表 5 欄 5 列、子頁分工表 3 欄 1 列），成長型皆判 `unknown`，機制欄皆判「有（wiki-ingest-features.md）」——但規則檔 L300 的週更機制**只覆寫「現在拿得到嗎」一欄**（以 radar 為準），其餘四欄無看守。

| 列 | 最易過期的格 | 何時過期 | 有無機制 |
|---|---|---|---|
| `/goal` | L52「✅ 正式發布（v2.1.139）」 | 版本號一旦不是新聞即成噪音；真正會變的是條件語法（V:L26 官方專頁的 4,000 字元上限、"or stop after 20 turns"、`/goal clear`、resume 行為） | 狀態欄有（lint 週覆寫）；**語法無** |
| 內建 subagent | L53「Explore 唯讀、一次性、不能追問」＋L62「跳過 CLAUDE.md…以 Opus 為上限（v2.1.198 起）」 | **已過期**：V:L27 判「跳過 CLAUDE.md」官方查無、v2.1.198 對應的是 extended thinking 繼承不是 Opus 上限 | 無 |
| **Dynamic workflows** | L54「✅ 全部付費方案」＋L67「上限 16 路並行、單次 1,000 agent」 | **已落後**：V:L29 指 v2.1.269 起 `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` 可提到 256。此列跟 changelog 走，是五列裡過期最快的（週級） | 無（radar 不收限制數字） |
| Managed Agents | L55「10 個零件中只有 `/goal` 正式發布」＋$0.08/session-hr | 零件數與子頁 `## 各零件現在到哪` 表列數綁死，子頁增列時此處不會自動跟；計費隨牌價變 | **五列中唯一有機制**（規則 L300 每週對 radar 覆寫，母頁選型表明文同源） |
| Agent SDK | L56「Python SDK v0.100.0＋／TypeScript v0.95.0＋」＋「2026-06-16 起計費切割暫停，重新推行時間未定」 | SDK 版號是流水，寫死即日日過期；計費切割那句的家在 `entities/pricing`（第 3 波定稿），此處是副本——**ledger 第 3 波回訪第 2 項寫 09-14 換軌**，換軌後本列會與 pricing 打架 | 無 |

---

## 6. 需官方查證表（V 未覆蓋、建議補查）

| # | 項 | 為什麼要查 |
|---|---|---|
| 1 | Agent SDK 列（L56）的兩個版本下限 v0.100.0／v0.95.0，以及「2026-06-16 起計費切割暫停，重新推行時間未定」現在還成立嗎 | V 十四條判定不含此列；09-14 pricing 換軌（ledger 第 3 波回訪第 2 項）後本列可能與 pricing 打架 |
| 2 | **Q2 的組合題**：workflow script 裡能不能派 subagent／開 agent teams？`/goal` 能不能寫進 workflow？官方文件有沒有明說 | 使用者 Q2 逐字問「subagent 加 workflows」，八卡若各自獨立寫，仍答不到「加」這個字。V:L20 的三問決策樹只答「挑哪個」，不答「能不能疊」 |
| 3 | L62「Explore 跳過 CLAUDE.md」 | V:L27 判「本次未在官方頁查得」，處置是刪或標待查證——屬官方事實，我不開藥 |
| 4 | L87 Managed Agents 持久記憶「公開測試」、L85 MCP 隧道 | V:L30 已更正 MCP 隧道（研究預覽須申請）；但持久記憶／Dreaming 的零件狀態沿用第 2 波 2026-09-06 查證（V:L41），本波未重查 |
| 5 | `official-community-gap` L30 與本頁 L81 對 dynamic workflows 的狀態不一致（gap：2026-05-28 Research Preview、feature-radar 標 ❌ 暫不推薦；本頁：全部付費方案） | 同一積木兩頁兩個狀態，且 gap 那列還帶「退款爭議」；哪個是現在需官方定 |

---

## 7. Q2 及格與否＋一句給設計者

**Q2 不及格。** 三個獨立證據：(a) 八積木盤點的工作流欄 8 格中 7 格「無」、唯一非無是 `/goal` 的半格；(b) 頁面對 Q2 有一句正面棄權——L81「社群拿它玩出什麼配置，尚無社群配置回報（2026-09-10）」；(c) 本頁 L60 與 guide L77 互指成環，而答案不在環上任何一點。V:L13 官方自己給了六條可逐字抄的 workflow prompt 範本，本頁引用該文件三次、一條都沒抄進來。

**一句給設計者：**
> 八張卡的骨架不要從現有的選型表或六層架構改出來——那兩個軸講的都是「積木之間的關係」，使命句問的是「每個積木自己的來歷與產出」，這個軸頁面上不存在；請直接照 V 第一節那張表一積木一卡（為什麼出／能跑什麼＋最小指令／現在還做不到什麼），社群案例一律 wikilink 回 `community-tech-patterns` 不重述，然後再把選型表與六層擺到卡片後面當附錄。

---

## 8. 預測對照（主 session 代做，冷讀者交件 `wave13-cold-reader-2026-09-12.md`）

| 題 | 健檢卡預測 | 冷讀者實測 | 對上？ |
|---|---|---|---|
| Q1 | 2 跳、半拿到 | 1 跳、✅ 拿到（L41／L81／L83，issue 編號是最強證據） | ✗ 低估頁面：卡點預測在「為什麼出」欄無，實際 L83 一句就答了 |
| Q2 | 3–4 跳、沒拿到 | 1 跳＋2 次回頭、🟡 半拿到；卡 L65 四原語只有名字、L66 預設已有 script、L81 正面棄權 | ✓ 方向對（不及格），跳數高估；卡點 L81 命中 |
| Q3 | 3 跳、半拿到 | 1 跳、✅ 拿到；「多做什麼」弱，最好的一句埋在 L64 選型細節；teams 怎麼開沒寫 | ✗ 低估：差異軸 L79／L83 一頁答完；卡點「寄居別層」部分命中（L64 位置錯） |
| Q4 | 3 跳、拿到但有摩擦 | 1–2 跳、🟡 半拿到；guide 分得清，**managed-agents 分不清**（計費裂在 L55／L68–69／子頁 L59，來回三次） | ✗ 方向反：卡預測摩擦在 guide，實際在子頁計費重複 |

**校準結論**：4 題對 1。健檢卡系統性高估跳數（index L30 路由列直達，卡以為入口難）並低估「關係軸」對 Q1／Q3 的解答力；正確的是 Q2 不及格與其成因。對設計者的含義：**不必重寫關係軸，補「來歷與產出」軸即可**；Q4 的真卡點是母子頁計費重複，要在去向表處理（母頁只留 wikilink）。冷讀者另抓到 feature-radar L227 狀態矛盾（V 五-5 已處置）、agent teams 開關名稱缺（V 一節表格有 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`）、callout 戴雷達帽（L34–35 是子頁 SDK 版號）。

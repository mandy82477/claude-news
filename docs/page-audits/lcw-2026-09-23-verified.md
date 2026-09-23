# 第 16 波主編官方查證：topics/community-large-codebase-workflow

查證日 2026-09-23。工具：WebFetch 官方文件（code.claude.com）、arXiv、`gh api repos/<owner>/<repo>`（星數／forks／最後 push 為當日即時值）。行號＝對象頁檔案原始行號（含 frontmatter）。「頁面寫什麼」逐字抄自頁面。

## 一、結論（五行）

1. **第 1 線「每個 agent 一個 git worktree」官方早已內建，頁面零字提及**：官方 [worktrees 文件](https://code.claude.com/docs/en/worktrees)有 `claude --worktree <name>`、`EnterWorktree` 工具、subagent frontmatter `isolation: worktree`、四項隔離強制檢查（檔案編輯／命令工作目錄／git 轉向／命令形狀）、`.worktreeinclude`、週期清掃。L52 把 worktree 寫成社群共識、L63 🧰 行指社群工具 ness。官方對應在庫內**已有家**：`anthropic-agent-stack` L213「它們會不會碰到同一批檔案？會 → 用 worktree 隔離（背景 session 會自動搬進 `.claude/worktrees/`）」、L149／L173；`entities/claude-code` L502（v2.1.233 `--worktree` 旗標）、L515（v2.1.222 worktree 隔離安全修復）；`coding-workflow-guide` L253（`worktree.sparsePaths`）。本頁缺的是一句指路，不是缺事實。
2. **「官方 20 路並行」（L55）有兩個一手出處，頁面沒指任何一個**：Claude Code [subagent 文件](https://code.claude.com/docs/en/sub-agents)「By default, when 20 subagents are running in a session, spawning another with the Agent tool fails with `Concurrent subagent limit reached`」，可用 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 改、ultracode 豁免；Managed Agents 平台「最高 20 個子代理同時執行」（`entities/managed-agents` L89）。兩者是不同產品的同一個數字。
3. **⟨Q-01⟩／⟨Q-03⟩ 的官方句今天仍成立但措辭要對準**：subagent 文件「The exception is a fork, which inherits the parent conversation instead of starting fresh」「Forks skip both filters and receive the main conversation's exact tool pool」；文件**沒有**任何「每次工具呼叫重送／累積」的句子——頁面 L171「此後與一般對話相同、隨每次呼叫持續累積」是推論不是引文。兩筆懸置是同一件事記兩次（L169 與 L178 引同一來源、同一結論、同一查證日）。
4. **`--bare` 冷啟動（L98）官方有明確定義、無官方數字**：[headless 文件](https://code.claude.com/docs/en/headless)「Add `--bare` to reduce startup time by skipping auto-discovery of hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory, and CLAUDE.md」「`--bare` is the recommended mode for scripted and SDK calls, and will become the default for `-p` in a future release」。「約 15 萬 token」仍只有社群單一實測。
5. **第 3 線「取代官方記憶」（L127）與官方 auto memory 現況**：[memory 文件](https://code.claude.com/docs/en/memory)「Auto memory lets Claude accumulate knowledge across sessions without you writing anything… four kinds of notes」「Loaded into every session (first 200 lines or 25KB)」「Subagents can also maintain their own auto memory」；CLAUDE.md 載入順序官方逐字：「content is ordered from the filesystem root down to your working directory… Within each directory, `CLAUDE.local.md` is appended after `CLAUDE.md`」，受管理原則檔路徑 macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`／Linux `/etc/claude-code/CLAUDE.md`／Windows `C:\Program Files\ClaudeCode\CLAUDE.md`——L97「載入順序」列與官方一致。

## 二、頁面數字 vs 一手

| 行號 | 頁面寫什麼 | 一手 | 判定 |
|---|---|---|---|
| L52、L63 | worktree 隔離＝社群共識；🧰 指 ness | 官方 `--worktree`／`EnterWorktree`／`isolation: worktree`（見上） | **官方對應缺席**，是本頁最大的一手漏洞 |
| L55 | 「官方 20 路並行、創始人『每晚數千子代理』與社群『4→20 就崩』落差沒人驗證（推論）」 | 官方：session 內同時 20 個 subagent 為預設上限，可調 | 「20 路」是**上限**不是「官方能跑 20 路不崩」；三個數字量的不是同一件事（上限／人物軼事／社群單一分析） |
| L98 | `claude -p` 未加 `--bare` 冷啟動約 15 萬 token | 官方定義 `--bare` 跳過什麼；無 token 數 | 數字二手單一，維持「單一實測」 |
| L97 | CLAUDE.md 載入順序（CLAUDE.local.md 後載、受管理原則檔各 OS 路徑不同） | 官方逐字一致 | 成立 |
| L101、L169–L178 | fork 子代理「每次工具呼叫累積整段對話歷史」、200 萬 token；⟨Q-01⟩⟨Q-03⟩ | 官方：fork 繼承父對話；無「累積／重送」句 | 「機制方向已由官方文件證實」**過度**——官方只證實「繼承」，累積是推論；200 萬仍社群單一 |
| L127 | 「取代官方記憶：手動策展比官方自動記憶更可控」 | 官方 auto memory 有四類筆記、每 session 載前 200 行／25KB、可關 | 頁面沒寫官方 auto memory 是什麼，讀者無法比 |
| L147 | 跨模型交叉審查 71.6%→89.7%，反向下降 | arXiv 2607.21656（Xiang／Zhang／Zhang／Xu，2026-07-22）：「Claude review raises Codex drafts from 71.6% to 89.7% (p_BH=.001)」「Codex reviewing Claude drafts drops the pass rate from 91.4% to 82.8% (p_BH=.046)」 | **成立且可補齊**：反向是 91.4→82.8，Codex 自審 84.5，Claude 自審不變 |
| L155 | loopx（4,476 星） | repo 已轉址 **loopx-project/loopx** 5,925★／565 forks／push 09-22 | 星數過期 32%；tools 頁 L213 連結仍是舊 owner huangruiteng |
| L122 | graphify 11.3 萬星 | 120,564★ | tools 頁已改 12.0 萬，本頁落後 |
| L123 | brain.md（504★） | 552★ | tools 頁已改 552，本頁落後 |
| L129、L136 | claude-mem／gentle-ai「僅星數佐證」 | claude-mem 94,483★／8,353 forks；gentle-ai 7,160★／779 forks | 成立（規模大、無實測） |
| L56 | Concord（MCP）「單一實測（今日首見）」 | Get-Concord-AI/concord-mcp 323★／push 09-22；節點日 08-27 | 「今日首見」是 08-27 那天的措辭，已 27 天 |
| L54 | proliferate（09-13，僅星數） | 505★／push 09-22 | 成立 |
| L53 | Claudette、Superset、cc-fleet | patterns 節點無 URL（grep 零命中） | **本頁與 patterns 都給不出連結**，冷讀者拿不到 |
| L146 | interns-review-plugin | 2★／0 forks／push 09-05 | 「多來源＋學術重現」那格把它混進去，撐不起 |
| L96 | nightshift | 12★／push 09-08 | 「多來源」格的四個代表實作之一只有 12★ |

## 三、考題的官方錨句

### 10 個 agent 改 monorepo（Q1）
- 隔離：`claude --worktree feature-auth`「Run the command again with a different name in another terminal to start a second isolated session」；subagent `isolation: worktree`「Each subagent gets a temporary worktree that Claude Code removes automatically when the subagent finishes without changes」。
- 上限：「when 20 subagents are running in a session, spawning another… fails」。
- 官方比較各路並行做法：worktrees 文件指向 [Run agents in parallel](https://code.claude.com/docs/en/agents)（worktree 隔離檔案／subagent 拆工／cross-session messaging 傳結果／agent teams）。本頁與 `anthropic-agent-stack` 誰該放這句，屬設計者判。

### session 變笨怎麼量（Q2）
- 官方：「CLAUDE.md files are loaded into the context window at the start of every session, consuming tokens… The context window visualization shows where CLAUDE.md loads relative to the rest of the startup context」（有 `/context` 可視化，文件 [context-window](https://code.claude.com/docs/en/context-window)，本波未逐字抓）。
- 社群量測與 `code-quality-decline`「怎麼自己量一次」節分工，屬設計者判。

### 團隊決策讓 agent 記得（Q3）
- 官方 auto memory 四類筆記、每 session 載前 200 行／25KB；「Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook」。
- CLAUDE.md 建議「Keep it to facts Claude should hold in every session… If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill or a path-scoped rule」——與 L88 第三條「依觸發頻率決定放哪一層」一致，可指官方。

### 交叉審查數字出處（Q4）
- arXiv 2607.21656 連結在 patterns 節點（L1683 附近，健檢卡核）；本頁 L147 有「arXiv 2607.21656」字串但**無連結**，L186「本頁不重複列出」。

## 四、需設計者處理但主編查不到的

- Claudette／Superset／cc-fleet／Memex／session-indexer／CodeAlmanac／beads／auto-undo／resume-on-ratelimit／Caveman／CCN／Repo-as-Memory／《Why 20 Instances Break Down》：patterns 節點沒有 URL 或只有 Reddit 連結，無法查活性；「代表實作」欄這些名字對讀者是死名。
- 「創始人每晚數千子代理」（L55）出處在 `entities/boris-cherny`，人物頁範圍，未查。
- MCP 9 server ≈ 38k、Caveman 70→20、O(N²) 62.8–85.9%、subagent 靜默失敗 317 項：皆社群單一來源，無一手可對。

## 五、給設計者三句

1. 這頁四條線的「現在的答案」有三條官方已經給了零件（worktree 隔離＋20 上限、`--bare`＋context 可視化、auto memory＋CLAUDE.md 分層），頁面一個都沒指；「社群怎麼組」的故事只有在讀者先知道「官方給了什麼」時才成立——每線第一層該有一句官方對應（連 `entities/claude-code` 或 `anthropic-agent-stack`，連頁不連錨）。
2. 「證據強度」欄與代表實作對不上：「多來源」格裡塞 12★／2★ 的 repo，「已成趨勢」格四個月沒新節點；欄值要能被讀者從同列驗證。
3. ⟨Q-01⟩⟨Q-03⟩ 併一筆，並把「官方已證實機制方向」降為「官方證實 fork 繼承父對話；累積與 200 萬為社群推論與單一觀察」。

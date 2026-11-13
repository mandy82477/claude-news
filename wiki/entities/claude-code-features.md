---
page: "entities/claude-code-features"
kind: "entity"
type: "product"
status: "active"
domain: "🛠️ 工具/功能"
last_updated: "2026-11-10"
last_news_update: "2026-11-10"
status_main: "active"
days_since_news: 4
parent: "entities/claude-code"
children: "[]"
page_role: "child"
days_since_news_subtree: 4
inbound_links: 6
attribution_count: 10
attribution_last: "2026-11-10"
top_source: "official-docs"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-11-21"
pending_signalled: 1
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code 功能怎麼用：hooks、subagent、桌面版

功能怎麼用：hook 能不能當防線、subagent 派哪種、桌面版能做什麼。

**類型：** product
**狀態：** active
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**首次出現：** 2025（正式推出）
**最後更新：** 2026-11-10
**最後新聞更新：** 2026-11-10
%% 2026-11-01 第 21 波自 [[entities/claude-code]] 拆出：核心功能、桌面版功能地圖、hooks、subagent 原文照搬；母頁現況的 23 條桌面版文件異動與「開發者須知」中屬用法的 8 條一併搬來；hooks 結論句依官方權限文件改寫、subagent 補平行分派一句（查證 2026-11-01） %%

> **最新動態**（2026-11-10）
> 桌面版文件：SSH session 改讀遠端主機的 managed settings 檔；Help Center 再移除「模型設定」段，新增 Preserved thinking（僅標題，見開發者須知）。

---

## 摘要

- **hook 能不能當防線**：hook 一觸發就是硬擋，但不保證會觸發；要保證一定擋，用沙箱；deny 規則與 hook 都當第二層（見 [[#hooks：事件、失效模式與能不能當防線]]）。
- **平行分派派哪種 subagent**：什麼都不設就在背景跑、同時最多 20 個；要共用主對話的 context 與 cache 選 fork（見 [[#Subagent 型別差異對照]]）。
- **桌面版能做什麼**：依主題歸群在 [[#桌面版功能地圖]]，每條日期對到同頁「桌面版文件時序」。
- 官方建議的做法見 [[topics/coding-workflow-guide]]；Mods 見 [[entities/claude-mods]]；文中「已知問題頁」指 [[entities/claude-code-known-issues]]。

## 核心功能

- **CLAUDE.md** — 專案級別的 AI 指令設定
- **Hooks** — 在特定事件前後注入自定義邏輯（如：修改代碼後強制跑測試）
- **Skills** — 可複用的任務封裝單元，Claude 透過描述自動觸發；官方產品線與生態詳見 [[entities/claude-skills]]
- **`/skill-doctor`**（v2.1.252+，查證日 2026-09-25，[官方 skills 文件](https://code.claude.com/docs/en/skills)）— 列出每個 skill 的 context 成本與叫用次數、標出從未叫用的並說在哪關；報告在 `/plugin` Stats 頁。只算用量，不評內容
  - 不含 bundled／enterprise skills；Remote Control 連線與跳過 feature-flag 抓取的 session 不可用
- **Agent Teams** — 多 agent 協作，目前僅支援 Claude 實例（社群已有 workaround）
- **MCP Servers** — 外部工具整合（注意：多個 MCP 可能導致每次訊息消耗 20k+ tokens）
  - **MCP Tasks（public beta）與 Elicitations 已有官方說明**：MCP tasks 由 server 執行長任務，需 Claude Code CLI v2.1.304+，v2.1.319 起無需 feature-flag 抓取即可使用，`CLAUDE_CODE_DISABLE_MCP_TASKS=1` 可關閉。
    - Elicitation 對話框可在任務執行中向使用者要輸入（[MCP 文件](https://code.claude.com/docs/en/mcp.md)、[CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)，查證日 2026-11-08）。
    - 2026-10-25 Forkast News 的「限量發布」措辭官方未用。
- **Memories** — 跨 session 的持久記憶（Managed Agents Beta）
- **Claude Artifacts 負向對照（訊號待驗）**：Show HN「r3, A local alternative to Claude Artifacts」（2026-09-26）主張本地替代方案優於官方 Artifacts；僅單一 HN 貼文、2 分，未附測試方法或具體指標，證據不足
- **1Password 整合已確認**（查證日 2026-09-20，[Claude Help Center](https://support.claude.com/en/articles/15936181-get-started-with-1password-for-claude)）：「1Password for Claude」為 beta 功能，適用 Pro／Max／Team／Enterprise 付費方案，僅支援 macOS 版 Claude Desktop；於 Desktop「設定 > Connectors」連結 1Password 後，Claude 遇到登入頁面時向 1Password 請求憑證，1Password 顯示欲使用的項目並經生物辨識確認，憑證由 1Password 直接填入頁面，密碼與一次性驗證碼皆不進入模型的 context、記憶體或 Anthropic 系統；Team／Enterprise 組織預設關閉，須由 Owner 於組織設定手動開啟。
- ❓ **待查證**（標 2026-11-07｜查 Claude Code model configuration｜複 2026-11-21｜訊 2026-11-10）｜**模型設定段落再變**：11-09 新增「model/effort/thinking」段；切換說明改指 Opus 5／5.5（原 Fable），疑搬移非功能。
  - 11-10 該段與切換說明再被移除，內容仍未載。

### 桌面版功能地圖

> 把下方「桌面版文件時序」的桌面版文件（`desktop.md`）異動依主題歸群；每條只收時序條目已記的事實，日期指向時序原條。官方文件 [desktop.md](https://code.claude.com/docs/en/desktop.md)，彙整日 2026-10-25。

**SSH 遠端與離線續跑**
- 11-10：SSH session 讀取遠端主機上的 managed settings 檔（後半句截斷）；Linux／macOS 遠端在 Desktop 斷線時，worktree 內的編輯仍可繼續。
- 11-09：新增 session 內預覽 HTML 檔案——session 內直接預覽不執行腳本，匯出後在本機瀏覽器開啟才會執行；組織可關閉此預覽的腳本執行。
- 10-08：可從連結開啟 SSH session，分「已有連線」「新連線」。
- 10-14：SSH 遠端工作流程擴充——連線需求、macOS／Linux 沿用既有 SSH 設定、支援 Windows 遠端機器；Desktop 離線時任務在背景續跑，連回後處理期間送達的請求。
- 10-15：新增 SSH／TLS 代理疑難排解（`HTTPS_PROXY`、`NODE_EXTRA_CA_CERTS` 等）。
- 10-11：SSH session 在連線設定 Worktree folder（遠端路徑，如 `~/worktrees`）。
- 10-17：結束 App 後任務是否續跑依平台分流——macOS／Linux 帳號登入可接回；Windows 或第三方 provider 接不回。
- 09-25：本機與 SSH session 自動載入帳號已啟用的 skills／plugins。

**dev box 與受管裝置**
- 10-24：新增內容集中於 dev box 設定範例（`acme-dev create`、`devbox` id／name）。
- 10-24：「Local sessions on managed devices」一節與 Notification／PermissionRequest hook 範例經 2026-11-08 查證仍在現行文件（hook 範例移到遠端 session 權限提示段），並非移除。
- 10-12：組織設定 `disableDesktopLocalSessions`、`sshHost`／`sshHostAllowlist`（見「開發者須知」）。
- 10-05：HIPAA 組織「Desktop」「雲端 session」兩個管理開關，Desktop 預設關閉（見「開發者須知」）。

**Dispatch 與 Claude 建議的任務**
- Dispatch：10-22 桌面文件增 Dispatch 說明（細節未載，見 [[entities/claude-code-releases#歷史記錄]]）；相關未修問題見已知問題頁 #40283、#45937。
- Claude 建議的任務：本頁尚無對應的時序條目。

**Auto mode availability**
- 10-21：桌面版文件新增 Auto mode availability 小節。
- 09-02：Auto mode 開放所有 Anthropic API 使用者，需 Opus 4.6／Sonnet 4.6 以上（見「開發者須知」）。

**session 資料夾與環境**
- 10-20：文件新增 171 段、移除 65 段，聚焦 session 資料夾管理與已儲存環境；新版對應寫法未見列出。
- 10-11：本機 session 於設定 > Claude Code 設 Worktree location。
- 10-09：本機 session 顯示獨立版本號；「+ New session」或 `Cmd+N`／`Ctrl+N` 開新 session。
- 10-04：「Continue in」拆成個別選項，可選 Cloud 或直接以編輯器／檔案管理器開 session 資料夾。
- 09-14：雲端 session 可掛載多個 repository。
- 09-12：Git 需求改為「用獨立 worktree 的 session 才需要」。

**Agent teams**
- 本頁沒有桌面版文件對應條目；機制見「Subagent 型別差異對照」軸線 4。

**其他**
- 11-05：文件增字（216,003→217,701），段落超過自動比對上限，改了哪些主題未知，需自行開原文比對。
- 11-04：文件增字（211,650→216,003），段落超過自動比對上限，改了哪些主題未知，需自行開原文比對。
- 11-03：文件增字（209,756→211,650），段落超過自動比對上限，改了哪些主題未知，需自行開原文比對。
- 11-02：文件增字（207,065→209,756），段落超過自動比對上限，改了哪些主題未知，需自行開原文比對。
- 10-21：session details panel 用量顯示方式、憑證來源設定步驟。
- 10-01：`claude --desktop` 直接開桌面版。
- 09-30、09-15：`/resume` 接續終端機／CLI session。
- 09-19：Transcript 新增 Thinking／Verbose 檢視。
- 09-14：`disableMobileSimulatorTools` 可封鎖 iOS 模擬器工具。

### 桌面版文件時序

- **官方文件更新**（2026-11-10）：桌面版文件字數由 223,150 增至 223,476，新增三段、移除三段（移除的三段未載）。
  - **新增內容**：SSH session 讀取遠端主機的 managed settings 檔；Linux／macOS 遠端在 Desktop 斷線時 worktree 內編輯可繼續；另一段列出 Terminal、Browser、iOS Simulator（原文截斷）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-11-09）：桌面版文件新增「在 SSH／WSL session 中預覽 HTML 檔案」一節（219,230→223,150 字）——匯出的檔案在使用者自己瀏覽器開啟會執行內含腳本；但 session 內直接預覽的檔案不執行腳本，腳本繪製的圖表／表格會顯示空白。同批新增組織層級「關閉 SSH／WSL 預覽腳本執行」開關，管理面細節見安全政策角度（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-11-07）：桌面版文件字數由 217,701 增至 219,230，但本頁段落數（1332）超過自動比對上限（1200），無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-11-05）：桌面版文件字數由 216,003 增至 217,701，但本頁段落數（1329）超過自動比對上限（1200），無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-11-04）：桌面版文件字數由 211,650 增至 216,003，但本頁段落數（1322）超過自動比對上限（1200），無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-11-03）：桌面版文件字數由 209,756 增至 211,650，但本頁段落數（1293）超過自動比對上限（1200），無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-11-02）：桌面版文件字數由 207,065 增至 209,756，但本頁段落數（1284）超過自動比對上限（1200），無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-30）：桌面版文件字數由 202,046 增至 203,154，但本頁段落數（1236）超過自動比對上限（1200），無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-26）：桌面版文件字數由 189,365 增至 201,162，但本頁段落數（1222）超過自動比對上限，無法產生逐段差異，具體改動需自行開原文比對（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-24）：桌面版文件新增約 251 段、移除約 149 段（168,290→189,391 字）；新增內容集中於 dev box 相關設定範例（`acme-dev create`、`devbox` id／name 等）（[原文](https://code.claude.com/docs/en/desktop.md)）。
  已查證（查證日 2026-11-08）：現行[桌面版文件](https://code.claude.com/docs/en/desktop.md)仍有「Local sessions on managed devices」一節（說明管理員可停用本機 session），Notification／PermissionRequest hook 範例也仍在，已移到遠端 session 權限提示段（在遠端機器的 `~/.claude/settings.json` 設定）；先前以為「被移除」其實是搬移。
- **官方文件更新**（2026-10-21）：桌面版文件新增 95 段、移除 52 段（160,296→162,725 字），新增 Auto mode availability 小節、session details panel 用量顯示方式、新增憑證來源設定步驟；移除內容未見列出（原文截斷）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-20）：桌面版文件新增 171 段、移除 65 段（148,190→160,296 字，近期最大單日異動），聚焦 session 資料夾管理與已儲存環境；移除段落多為舊版操作說明，新版對應寫法未見列出（原文截斷）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-17）：桌面版文件重寫「結束 App 後任務是否還在跑」規則，依平台分流——macOS／Linux 以 Claude 帳號登入時結束 App，重開 session 可接續正在跑的任務；Windows 版或接第三方 provider 時結束 App，進度無法接回，須保持 App 開著直到任務完成（文件字數 148,156→148,190）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-15）：桌面版文件新增 SSH／TLS 代理疑難排解章節，涵蓋 `HTTPS_PROXY`、`NODE_EXTRA_CA_CERTS` 等設定，延續 10-14 的 SSH 遠端工作流程擴充（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-14）：桌面版文件大幅擴充（99,435→122,477 字，新增 122 段、移除 6 段），集中於 SSH 遠端工作流程——連線遠端機器的需求、macOS／Linux 沿用既有 SSH 設定、Windows 遠端機器支援，以及 Desktop 離線時任務在背景持續執行、連回後處理期間送達的請求（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-11）：桌面版文件新增說明——本機 session 在**設定 > Claude Code**設 Worktree location；SSH session 則在連線設定 Worktree folder（遠端路徑，如 `~/worktrees`）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-09）：桌面版文件新增說明——Code 分頁的本機 session 現顯示獨立版本號；側邊欄「+ New session」或 macOS `Cmd+N`／Windows `Ctrl+N` 可開新 session，同時處理多項工作（文件字數 93,648→94,202）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-08）：桌面版文件新增 SSH session 連線管理說明，可從連結開啟 SSH session，分「已有連線」與「新連線」；另新增跨裝置控制 session 可見度的設定（新增 60 段、移除 13 段）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-06）：桌面版文件重新命名既有設定項，非新功能——Auto-fix／Auto-merge 補充說明文字、SSH 欄位由大寫改小寫，邏輯未變（文件字數 84,136→84,975）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-04）：桌面版文件改版——電腦使用（Computer use）開關從「設定 > 一般」搬到「設定 > 本機電腦 > 系統」；舊版「Continue in」單一選單拆成個別選項，可選「Cloud」把本機 session 接續到雲端，或選已安裝的編輯器／檔案管理器直接開啟該 session 資料夾（文件字數 83,588→83,682）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-10-01）：桌面版文件新增說明——終端機執行 `claude --desktop` 可直接開啟桌面版，不先啟動終端機 session；本機與雲端 session 皆載入 claude.ai 帳號已啟用的 skills；plugins 可依使用者帳號、特定專案或僅本機範圍設定（文件字數 82,443→83,575）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-09-30）：桌面版文件補充 `/resume` 流程——終端機關閉 session 後，桌面版 `/resume` 選取該 session 即可接續同一對話（非複本），`claude --resume` 在終端機仍找得到（文件字數 81,064→82,443）（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-09-25）：本機與 SSH session 現在自動載入帳號已啟用的 skills／plugins；桌面版 plugin 瀏覽器雲端 session 不可用，桌面裝的 plugin 不同步雲端（[原文](https://code.claude.com/docs/en/desktop.md)）。詳見 [[entities/claude-skills]]。
- **官方文件更新**（2026-09-19）：Claude Code 桌面版新增 Thinking／Verbose 兩種 Transcript 檢視模式——Thinking 讓推理過程展開、工具呼叫仍維持摺疊；Verbose 用於除錯，顯示更多細節（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-09-17）：終端機 session 載入 claude.ai 帳號 skills/plugins——本機讀個人 `~/.claude/skills/`，雲端改讀帳號設定，SSH 讀本機路徑（[原文](https://code.claude.com/docs/en/desktop.md)）。
  - 與同日 [[entities/cowork|Cowork／Chat 合併]] 同屬帳號統一方向；同批移除 1 段舊版說明。
- **官方文件更新**（2026-09-16）：桌面版新增雲端 session 接手本地工作、桌面推送分支、「Code in the web」組織開關等能力，為 09-14 已收錄功能的擴充，細節見 [[feature-radar]]（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-09-15）：桌面版新增 `/resume` 接續既有 CLI session；macOS 背景執行 computer use 時，Claude 只在已核准的 App 內作業，不再連帶隱藏其他視窗（行為變更）（[原文](https://code.claude.com/docs/en/desktop.md)）。
  - diff／終端機等面板可拉出成獨立視窗；同時移除 3 段舊版說明，含舊版 hide-windows 行為描述與 `--resume`／`--continue` 對照表列。
- **官方文件更新**（2026-09-14）：桌面版文件新增雲端 session 可同時掛載多個 repository（選擇雲端環境後點擊「+」新增），以及 `disableMobileSimulatorTools` 設定旗標，可封鎖 Claude 控制與擷取 iOS 模擬器裝置的工具（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-09-12）：桌面版文件將 Git 需求措辭從「僅 Windows 需要」改為「用獨立 worktree 執行的 session 才需要 Git」；session 定義同時拿掉「各自獨立的程式碼變更」字樣，僅保留獨立聊天紀錄與專案資料夾（[原文](https://code.claude.com/docs/en/desktop.md)）。
- **官方文件更新**（2026-08-29）：桌面版文件新增 3 段、移除 2 段——① 採用 adaptive reasoning 的模型上，`MAX_THINKING_TOKENS` 設為非預設值時的行為；② Claude 跨 session 傳訊時，該處顯示標註傳送方的卡片；③ **extended thinking 現為預設啟用**，用以提升複雜任務表現（既有功能的預設狀態澄清，非新指令／旗標）。

### hooks：事件、失效模式與能不能當防線

> 本節只彙整與導覽，細節留在原處：版本頁（`onFailure`、`PreModelSwitch`）、已知問題頁各組、本頁「開發者須知」。官方 hooks 文件 2026-10-11 查證，權限優先序 2026-11-01 查證。

**一、事件與近期新增**

| 事件／能力 | 狀態 | 去哪看 |
|---|---|---|
| `PreToolUse`／`PostToolUse` | 既有；觸發可靠性見下節 | 已知問題 #6305 |
| `Stop`／`SubagentStop` | 既有；v2.1.294 改善 `prompt` hook 行為 | 版本表 v2.1.294 |
| `PreCompact`／`PostCompact`／`SessionStart`／`SessionEnd` | 官方確認四個都有（#47023 已關閉，2026-08-17） | 已知問題 #47023 |
| `PreModelSwitch`／`PostModelSwitch` | v2.1.251 新增，可攔截、確認或標註模型切換 | 版本表 v2.1.251 |
| Claude Mods（原 Function Hooks） | v2.1.287 出貨，取代 function hooks | 已知問題 #91870、[[entities/claude-mods]] |
| 使用者中斷時觸發的 hook | 尚無，功能請求未獲回應 | 已知問題 #9516 |

**二、失效模式**

| 失效模式 | 狀態 | 修於 |
|---|---|---|
| Pre／PostToolUse 未觸發（#6305） | 🔴 open；官方協作者稱改 Settings JSON 後須 `/hooks` 確認或開新 session | 未修 |
| Stop hooks 被忽略（2026-04-24 回報） | 🔴 | 未修 |
| 改 hooks／MCP／plugin 設定要重啟 session（#24057） | 🔴 | 未修 |
| 中斷時無 hook 可用（#9516） | 🔴 | 未修 |
| 無法為不同情境隔離 hook 與設定（#7075 profile） | 🔴 | 未修 |
| `prompt`／`agent` hook 以自然語言寫「封鎖 X」實際擋不住 | ✅ | v2.1.294 |
| hook 起不來、逾時或退出碼異常時動作被放行 | ✅ 可選擇改為阻擋 | v2.1.295 起 `onFailure: "block"`（預設 `continue`） |
| PowerShell hook 指令以型別轉換、`param`、`using` 或屬性開頭時，exit 2 擋不住 | ✅ | v2.1.316 |

**三、能不能當安全控制**

- **官方立場**（2026-10-11 查證）：`if` 過濾器是盡力比對（best-effort），要硬性允許或拒絕請用權限系統而不是 hook。官方文件沒有「不要只依賴 hook 做安全防護」這句，MIXED Reality News 的轉述不準（見「開發者須知」該條）。
- **社群實測**：上表三個 🔴（#6305 未觸發、Stop hooks 被忽略、#24057 改設定要重啟）是 hook 靜默不作用的路徑；#9516、#7075 是功能請求（沒有中斷 hook、不能分情境隔離）。v2.1.294 修的那條是「寫了封鎖卻沒擋住」。
- **結論：hook 一觸發就是硬擋，但不保證會觸發。** 要保證一定擋，用沙箱（官方指定的安全邊界）；deny 規則比對的是指令文字，換個寫法就可能漏掉，見 [[topics/ai-agent-safety]]「deny-list 也不是」。hook 與 deny 規則都當第二層。
  - 擋得硬：官方 [permissions 文件](https://code.claude.com/docs/en/permissions)寫明 `PreToolUse` hook 擋下的呼叫不會被任何 allow 規則放行，exit 2 在權限規則之前就攔下（查證 2026-11-01）。
  - 不一定觸發：`if` 比對是盡力而為，也有沒觸發（#6305）、設定沒生效（#24057）的回報；`onFailure: "block"` 只補 hook 自己壞掉那一種缺口。
  - 反過來不成立：hook 回 allow 蓋不過 deny 規則。例外：沒有 managed settings、也不是 Team／Enterprise 登入時，mod 的 `tool.check` 可放行 hook 擋下的呼叫（見 [[entities/claude-mods]]）。

### Subagent 型別差異對照

**平行分派選哪種**：什麼都不設，Claude 從主對話派出的 subagent 就在背景跑，同時最多 20 個（`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 可調）；要共用主對話的 context 與 prompt cache（較便宜）用 fork，要乾淨的隔離 context 用非 fork；要在分割窗格各自協作、互派任務才用 teammate（只能前景）。（[官方 sub-agents 文件](https://code.claude.com/docs/en/sub-agents)，查證 2026-11-01）

派 subagent 前先看四條獨立軸線，可疊加（例：一個 background 的 fork）。來源：官方 `code.claude.com/docs/en/sub-agents`，2026-08-22 查證；欄位表 2026-10-22 補欄。

**軸線 1：內建 / 自訂 / plugin**

| 型別 | CLAUDE.md／git status | 模型 | 自動註冊 |
|---|---|---|---|
| Explore | 跳過（保持研究輕快省成本） | 繼承主對話，Claude API 上限為 Opus | ✅ |
| Plan | 跳過 | 繼承主對話 | ✅ |
| general-purpose | 讀取 | 繼承主對話 | ❌ 需顯式指定 |
| 其他內建 | 讀取 | 依定義 | ✅ |
| 自訂（`.claude/agents/`） | 讀取 | 依 frontmatter | 依設定 |
| plugin agent | 讀取 | 依 frontmatter | 依設定 |

- 自訂 agent 支援的 frontmatter 全集（19 欄，2026-10-22 核對）：`name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `autoCompactWindow`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `omitClaudeMd`, `effort`, `isolation`, `color`, `initialPrompt`, `experimental`
- 自訂 agent 可定義於 `.claude/agents/`、`~/.claude/agents/`、`--agents` CLI 旗標或 managed settings
- 2026-08-22 版缺的三個欄位（查證 2026-10-22，[官方 sub-agents 文件](https://code.claude.com/docs/en/sub-agents)）：

| 欄位 | 作用 | 版本門檻 |
|---|---|---|
| `autoCompactWindow` | 把該 subagent 的 auto-compact 視窗降到 100000–1000000 token；寫純整數 | v2.1.296+ |
| `omitClaudeMd` | `true` 時不載入 user／project／local CLAUDE.md（managed policy 仍載入） | v2.1.271+ |
| `experimental` | 實驗選項 map；目前 `cacheTtl` 設 `5m` 或 `1h` 選 prompt cache 壽命 | v2.1.248+ |

- **plugin agent 基於安全理由不支援 `hooks`／`mcpServers`／`permissionMode`**，其餘欄位支援；識別碼帶 scope（如 `my-plugin:review:security`）

**軸線 2：fork / 非 fork**

| 面向 | fork | 非 fork |
|---|---|---|
| Context 起點 | 繼承完整對話歷史、system prompt、工具、模型 | 全新隔離 context：僅 system prompt、任務訊息、CLAUDE.md／git status（Explore/Plan 除外）、預載 skills、sibling roster |
| 深度上限時 `Agent` 工具 | 保留在工具清單，但呼叫回傳錯誤，且不能再派 fork | 移除（僅 fork 保留） |
| 成本 | 首次請求複用 parent 的 prompt cache，較派新 subagent 便宜 | 全新 cache |
| 對主對話可見性 | 自身工具呼叫不進主對話，只有最終結果回傳 | 同左 |

**軸線 3：background / foreground**

兩者共同的第一層過濾會先移除：深度上限時的 `Agent`、`AskUserQuestion`、`EndConversation`、`EnterPlanMode`、`ExitPlanMode`（除非 `permissionMode: plan`）、`ScheduleWakeup`、`TaskOutput`、`WaitForMcpServers`、`Workflow`。

| 面向 | background | foreground |
|---|---|---|
| 內建工具 | 僅保留白名單（見下）| 全保留 |
| MCP 工具 | 全保留 | 全保留 |
| 權限提示 | 主 session 浮出、指名是哪個 subagent，結果以完成通知回來 | 即時 passthrough 給你 |

- background 白名單：`Read`, `Grep`, `Glob`, `Bash`, `PowerShell`, `Edit`, `Write`, `NotebookEdit`, `WebFetch`, `WebSearch`, `TodoWrite`, `Skill`, `ToolSearch`, `EnterWorktree`, `ExitWorktree`, `Monitor`, `TaskStop`, `SendMessage`, `Artifact`
- 前景還是背景，依序看第一個成立的：
  1. teammate 派出的 → 前景（teammate 設 `background: true` 會被拒）
  2. 設了 `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` → 前景
  3. fork 模式開著 → 背景
  4. fork 關、沒寫 `background: true` → 背景；但主對話需要結果才能繼續時是前景
  5. fork 關、寫了 `background: true` → 背景

**軸線 4：teammate / 非 teammate**

| 面向 | teammate | 非 teammate |
|---|---|---|
| 觸發條件 | interactive session 開 agent teams，主對話派出且帶 `name`（非 fork／`isolation`）| 其餘情況 |
| 額外工具 | `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate`, `CronCreate`, `CronDelete`, `CronList` | 無 |
| background | 不可（foreground-only） | 依軸線 3 規則 |
| context 隔離 | out-of-process teammate（split pane）各自獨立 context window | — |

#### 角色檔設計陷阱

> 只收官方 sub-agents 文件（查證 2026-10-22）寫得出的事實。

- **必填只有 `name` 與 `description`**；欄位名須與表格完全相符（`maxTurns`、`disallowedTools` 為駝峰），不認得的欄位靜默忽略、不報錯。
- **抓拼錯欄位**：v2.1.296+ 用 `claude --debug`，在 `~/.claude/debug/<session-id>.txt` 搜 `does not recognize or apply`，最多列出 5 個欄位並提示可能的正確名稱。
- **整檔被靜默略過的情形**：沒有 `name`（當成文件）、開頭 `---` 不在第一行、`name` 以 `-` 開頭或含 `:` 或超過 256 字元、有 `name` 無 `description`、YAML 解析失敗。
- **`tools` 省略＝繼承全部可用工具**；`tools` 與 `disallowedTools` 並用時先套 `disallowedTools`，兩邊都列的工具被移除。`tools` 內沒有任何項目能解析時通常拒絕啟動並指名錯誤項目。
- **`memory` 欄會自動開啟 Read、Write、Edit**，讓 subagent 管理自己的記憶檔（文件原文）；做唯讀角色時留意此欄。`autoMemoryEnabled` 關閉時 `memory` 欄無效。
- **觸發寫法**：description 寫「use proactively」之類字句鼓勵主動委派；官方範例用生命週期時點（「Use immediately after writing or modifying code」）。所有 subagent description 合計逾 15,000 token 會有啟動警告，仍全數載入。
- **自訂 subagent 的 system prompt 整個取代預設 Claude Code system prompt**；CLAUDE.md 與專案記憶仍照常載入，除非設 `omitClaudeMd`。
- 社群說法「用 general-purpose 代理再要它讀角色檔，`tools` 白名單不生效」：官方原文未直接記載；general-purpose 的工具是「所有可用於 subagent 的工具」，不列為已證實。

> 相關：社群 subagent 使用模式見 [[topics/community-tech-patterns]]；本表列的機制對得上學術哪些缺口（已補／未補／倒退）見 [[topics/community-tech-patterns]]「學術對照」節的缺口追蹤層；官方 vs 社群缺口對照見 [[topics/official-community-gap]]；官方建議的使用做法見 [[topics/coding-workflow-guide]]

> 本表依官方文件 2026-08-22 查證、2026-10-22 補欄、2026-11-01 補平行分派一句；逾 90 天未回訪時在此標明。

## 開發者須知

- **Help Center 新增「Preserved thinking」等三段（2026-11-10，Official Docs）**：標題稱 Messages API 調整處理 thinking blocks 的方式以防範蒸餾（僅標題）；另兩段為 Claude 如何標記 AI 生成內容、訓練資料更新程度。多輪帶 thinking blocks 的 API 使用者須開[原文](https://support.claude.com/en/articles/12138966-release-notes)確認行為。
- **Help Center 新增 Enterprise 安全／管理功能段落（2026-11-05，Official Docs）**：新增標題僅列 security center、inference hooks、centralized management，僅標題可用，與既有 [[entities/claude-code#現況|Inference Hooks]] 的關係待開[原文](https://support.claude.com/en/articles/12138966-release-notes)確認。
- **桌面版官方文件新增關閉本機 session、改走指定 SSH host 的組織設定（2026-10-12 查證，Official Docs）**：新增 `disableDesktopLocalSessions` 與 `sshHost`／`sshHostAllowlist`，供組織關閉本機 session、集中走指定 SSH host；雲端 session 不受影響。見[官方文件](https://code.claude.com/docs/en/desktop.md)。
- **hook `onFailure: "block"` 與官方安全建議有落差（2026-10-09，MIXED Reality News）**：媒體轉述的「不要只依賴 hook 做安全防護」不見於官方 hooks 文件（2026-10-11 查證）；官方原意見「hooks：事件、失效模式與能不能當防線」。
- **HIPAA 合規部署路徑擴大（2026-10-05，Official Docs）**：桌面版文件新增「Desktop」「雲端 session」兩個組織管理開關，HIPAA 組織「Desktop」預設關閉須 Owner 開啟；文件索引同步新增 [local mode HIPAA 設定指南](https://code.claude.com/docs/en/hipaa-setup.md)。
- **桌面版官方文件：Auto Mode 模型門檻與 Extended Thinking 預設開啟（2026-09-02 查證，Official Docs）**：官方 Claude Code 桌面版文件新增／異動段落載明，Auto mode 現開放給所有 Anthropic API 使用者，但需 **Claude Opus 4.6 以上或 Sonnet 4.6 以上**版本方可使用；文件同時說明 adaptive reasoning 模式下 `MAX_THINKING_TOKENS` 的行為，並明確標註 **Extended thinking 現為預設開啟**。屬既有功能的門檻／預設行為澄清（文件未附具體生效版本號或日期），非新指令旗標；見 [官方文件](https://code.claude.com/docs/en/desktop.md)。
- **任務之間執行 `/clear` 提升 token 效益（2026-08-14 官方部落格，HN 268 分，今日互動最高）**：Anthropic 官方部落格談如何讓每個 token 發揮最大價值，具體建議包含在不相關任務之間執行 `/clear`——可避免先前無關的 context 被送回模型、佔用預算與拉低訊噪比；屬使用建議而非新功能或新指令。
- **Extended Thinking 輸出為加密摘要，非原始推理（2026-06-22）**：session log 中的 thinking blocks 文字是推理的摘要版本，真實推理過程被 Anthropic 加密後存在 600 字元 signature 中，用戶端無法解密。需做審計追蹤或對推理過程有完整性要求的工程師，應避免以 thinking blocks 內容作為事實依據（見已知問題）
- **CLI 權限客製化避免手動確認（2026-06-22）**：長工作流中可透過 `settings.json` 的 `allowedTools` 與 Permission Rules 設定白名單，減少 Claude Code 在 agentic 模式下不斷彈出手動確認。`Tool(param:value)` 語法（v2.1.178）支援比對工具輸入參數，搭配 `--dangerously-skip-permissions` 旗標可完全自動化非互動批次流程（見 [教學](https://dev.to/kapoormanish/stop-clicking-approve-how-to-customize-claude-code-cli-permissions-pnh)）
- **四種儲存格式各有用途（2026-06-22 整理）**：Claude Code 儲存層包含 CLAUDE.md（專案指令）、session storage（當次對話上下文）、project state（持久狀態）、Memories（跨 session 記憶）；建議將專案持久狀態存於 repo，確保重開 session 後一致性（見 [說明](https://dev.to/arthurpro/anthropics-storage-layer-quartet-and-what-each-format-is-actually-for-4nd7)）

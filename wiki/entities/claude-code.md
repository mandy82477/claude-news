---
page: "entities/claude-code"
kind: "entity"
type: "product"
status: "active"
domain: "🛠️ 工具/功能"
last_updated: "2026-11-04"
last_news_update: "2026-11-04"
status_main: "active"
matrix_role: "產品"
days_since_news: 1
parent: null
children: "['entities/claude-code-archive', 'entities/claude-code-features', 'entities/claude-code-known-issues', 'entities/claude-code-releases', 'entities/claude-mods']"
page_role: "hub"
days_since_news_subtree: 1
inbound_links: 126
attribution_count: 844
attribution_last: "2026-11-04"
top_source: "github-issues"
pending_count: 6
pending_overdue: 2
pending_next_review: "2026-11-14"
pending_signalled: 1
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code

**類型：** product
**狀態：** active
**領域：** 🛠️ 工具/功能
**對照角色：** 產品（入口：終端機、IDE、桌面、網頁；誰起手：你每句下令）
**首次出現：** 2025（正式推出）
**最後更新：** 2026-11-04
**最後新聞更新：** 2026-11-04

> **最新動態**（2026-11-04）
> - **v2.1.318**：啟用 session 中寫出的 mods 時新增記錄使用者回答；Claude apps gateway `mantle` 上游新增 `assume_role` 設定（官方原文截斷；見 [[entities/claude-code-releases]]）。
> - **新增功能請求與互動更新**：Task queue 排入多個提示／任務（#33323）、Linear 整合觸發雲端 agent session 互動數更新（#12925）（見 [[entities/claude-code-known-issues]]）。
> - **桌面版文件增字**（211,650→216,003），段落超過自動比對上限，無逐段差異（見 [[entities/claude-code-features]]）。

---

%% 拆頁評估 2026-11-01：已拆（第 21 波）。母頁留現況、結論表與路由；已知問題、版本、功能用法住 claude-code-known-issues／-releases／-features。落選：兩子頁（功能留母頁，母頁約 333 行超過 300）、功能併進 coding-workflow-guide（它答官方建議、已 688 行）。`## 版本更新`、`## hooks：…` 是同名指路殼：前者有讀者版日報 4 筆錨點、feature-radar 3 筆；後者等 coding-workflow-guide、community-guardrails 改指 features 後可刪。 %%

## 往下鑽

| 你想知道 | 去哪頁 | 最後動態 |
|---|---|---|
| 某個 bug 修了沒、誰會遇到、有沒有繞法（九組逐條） | [[entities/claude-code-known-issues]] | 2026-11-04 |
| 現在到哪一版、stable 還是 latest、哪一版加了什麼 | [[entities/claude-code-releases]] | 2026-11-04 |
| hook 能不能當防線、subagent 派哪種、桌面版能做什麼 | [[entities/claude-code-features]] | 2026-11-04 |
| Claude Mods 是什麼、權限怎麼管 | [[entities/claude-mods]] | 2026-10-20 |

## 現在還沒修好的

只列現在還會發生、而且是壞掉而非還沒做的問題。**每一列都寫出誰會遇到**——多數只發生在特定產品或平台上，對不上號的就不會發生在你身上。狀態五值：🔴 未修復／✅ 已修復／⛔ 官方拒修／❓ 待查證／🔎 查無官方。上限 8 列；完整清單見 [[entities/claude-code-known-issues]]。

| 現在還沒修好的 | 誰會遇到 | 狀態 | 你能做什麼 |
|---|---|---|---|
| Windows Desktop 崩潰／孤兒程序／session 消失，紀錄可能被靜默清除（#80444 #42776 #26302 #53247 #26452 #59248） | Windows Desktop（含 Cursor 擴充套件）使用者 | 🔴 | 升級前備份重要對話；當機後登出或重開機再試；別依賴自動保留機制 |
| Cowork 的 Edit/Write 靜默截斷檔案（#53940） | Windows 上用 Cowork 的人 | 🔴 | 寫入後自行核對檔案長度；官方未給修復時程（44 則留言，可重現） |
| 進程增長至 120GB+ 遭 OOM killed（#4953 #11315） | Linux 上長時間執行的 session | 🔴 | 長工作分段、定期重開 session（98 則留言，可重現；07-19 社群回報 2.1.181／2.1.214 起安裝程式記憶體下降） |
| Cowork VM bundle 膨脹至 10GB，啟動與 UI 持續變慢（#22543） | 用桌面版 Cowork 的人 | 🔴 | 近期避免在 Cowork 處理大型檔案或大量寫入（官方標高優先） |
| 改 MCP／hooks／plugin 設定要重啟整個 session 才生效（#24057） | 用 MCP 的人 | 🔴 | 改設定前先收尾，重啟會失去現有內容 |
| MCP server 沒有 token 刷新機制（#5706） | 自建 MCP server 的人 | 🔴 | 改用長效期 token |
| MCP OAuth 在 `resource` 參數尾端多一個斜線，Entra ID 驗證失敗（#52871） | 企業 SSO 走 Microsoft Entra ID | 🔴 | 無繞法；改用非 SSO 的連線方式 |
| 排程 routine 呼叫 custom connector 的 MCP 工具一律要求核准（#61015） | 用排程 routine 的人 | 🔴 | 無繞法；改為手動觸發 |

本表只收 Claude Code 自身的故障；提示注入、供應鏈與帳號被劫這類外部攻擊面的安全問題不在本表，見 [[topics/ai-agent-safety]]「現在還擋不住的攻擊」。

**接下來看什麼**：這幾條翻 ✅ 的那一天會寫在 [[entities/claude-code-known-issues]] 對應分組；升版判斷見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]；官方建議的做法見 [[topics/coding-workflow-guide]]。

---

## 現況

**版本：**

- 最新 **v2.1.318**（2026-11-04）；npm `stable`＝2.1.309、`latest`＝2.1.316（查證 2026-11-01）。
- **該不該升**：沒用 Opus 4.8 fast mode，留在 stable 就夠；要 Monitor tool 或寫入邊界設定才需要 latest。逐版與通道見 [[entities/claude-code-releases]]。

**近期平台與文件異動：**

- 桌面版文件異動依主題歸群在 [[entities/claude-code-features#桌面版功能地圖]]，逐條時序在同頁。
- **官方文件更新**（2026-10-16）：文件索引新增 6 頁 Code Review 細項文件（用量費用、自訂設定、本機 `/code-review`、PR 讀取與請求審查、設定教學、疑難排解），呼應 Code Review 功能同日轉為正式發布（GA），詳見 [[feature-radar]]（[索引](https://code.claude.com/docs/llms.txt)）。
- **Claude Code Projects 進入 Beta**（[官方文件](https://code.claude.com/docs/en/claude-projects.md)，查證 2026-10-03）：Pro、Max 公開 beta、逐步開放，先從用過雲端 session 且在 claude.ai chat／Cowork 沒有既有 projects 的帳號開始，Team／Enterprise 尚未提供。
- Projects 運作：一個專案是一段持續對話，Claude 當協調者、每個任務開一條 thread（多為雲端 session，必要時可經 Remote Control 改派到自己的電腦）；用量計入與其他 Claude Code session 相同的方案額度且耗得更快，每天最多 200 個新 thread。
- 六家科技媒體 2026-09-17 同日報導；09-30 r/ClaudeCode 貼文稱已對「擁有既有 projects 的 Max 用戶」開放，與官方文件的開放順序（先從沒有既有 projects 的帳號）不一致，以官方為準、單一貼文未獨立證實。
- 與 [[topics/anthropic-agent-stack]] 積木的關係官方文件未專文論述。
- **官方文件更新**（2026-09-17）：「Use Claude Code with your Pro or Max plan」頁內容變動（23117→23163 字），移除「Choose a Claude plan」段；與同日方案與定價文件大改版（見下方「市場與競爭」與 [[entities/pricing]]）同批發生，具體異動內容未完整取得。
- **官方文件更新**（2026-09-16）：llms.txt 新增 Agent SDK「[Configure your agent](https://code.claude.com/docs/en/agent-sdk/configuration.md)」頁——依官方索引描述，說明如何組合 options 物件、設定 model、環境與上限，並指向各功能選項頁（查證 2026-10-03）；SDK 全貌見 [[topics/anthropic-agent-stack]]。
- **[[entities/cowork|Cowork]] 與網頁／App 共用記憶**（Help Center release notes，2026-08-25）：記住的項目集中列在設定 > Memory 的 Topics，可個別編輯或刪除；健康、信仰等敏感主題預設不納入，須手動開啟「Include sensitive topics in memory」才會記錄。
  - 原文於「記憶預設對部分方案開啟」處截斷，適用範圍未完整取得；八家媒體同步報導（TechCrunch、Silicon ANGLE、CNET、Engadget、SD Times、The Register、Techzine、ZDNET）。
- **Skill／外掛安全掃描（beta）**（Help Center release notes，2026-08-06 標註日期）：Enterprise 方案的第三方 Skill 或外掛在上傳、編輯時自動檢查是否含惡意內容，屬背景自動掃描，無使用者端可執行操作。
- **Inference Hooks**（Claude API Release Notes，2026-08-05）：進入 Enterprise 組織 beta，可將 claude.ai、Cowork、Claude Code 上每一次受管治 prompt 導向企業自身的 AI 安全伺服器。
- 🔎 **查無官方**（標 2026-09-08｜查 iOS App、設定區塊｜複 2026-11-30）｜**iOS App 新增用量按鈕、Claude Code 設定區塊**（Pasquale Pillitteri，09-08，僅標題）：`support.claude.com`／`code.claude.com` 週更與 changelog 均未見此項，查證 2026-09-26，僅媒體轉述；
  - 2026-10-31 複查 Help Center release notes（9 月條目 09-01／10／15／16／22／25／28，無此項）、`code.claude.com/docs/en/mobile.md` 與 changelog 仍無，維持查無官方。
- **雲端 session 底層架構**（Hacker News，58 分，2026-09-08）：技術部落格指出 Claude Code 雲端 session 各自跑在獨立 Firecracker microVM，開機直接進入 Rust 撰寫的自訂 init（`process_api` 為 PID 1，非 systemd）（[原文](https://rohanadwankar.github.io/posts/platforms.html)）。
- **年齡驗證政策升級（Yoti 第三方驗證，2026-09-11）**：Claude 消費版宣布不再開放未滿 18 歲使用者使用，改由第三方平台 Yoti 進行年齡驗證，偵測到疑似未成年使用跡象即停用帳號並要求驗證年齡才能恢復；共用帳號給青少年的家庭／教育場景會被擋。見[官方說明](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)
- **年齡驗證政策（Persona Identity Verification，2026-06-22）**：Anthropic 在特定使用情境下導入 Persona 第三方身分驗證，以落實年齡管控、使用政策與法規遵循。此政策屬平台使用條款異動，不影響 CLI 操作（09-11 起由 Yoti 年齡驗證接續，見上條）

**近期報導（尚待官方佐證）：**

- **漏洞修補負向對照（訊號待驗）**：SiliconANGLE 報導 Cogent Security 的 VR-1.1 模型在漏洞修補測試分數超越 Claude Code 與 Codex（2026-11-03）；僅標題層級，未附測試項目、樣本量或分數細節，證據不足
- **社群工具聲稱可讓 Max $20 方案用量「擴大 50 倍」**（[muaaz9329/cheap-ag](https://github.com/muaaz9329/cheap-ag)，186★，2026-11-01）：單一 GitHub repo 宣稱「50x your Claude usage」，未附測試方法或與官方用量上限的對照數據，證據薄弱；計費規則另見 [[entities/pricing]]。
- ❓ **待查證**（標 2026-10-21｜查 old chat、warns you）｜**Claude Code 傳新增「接續舊對話前提醒會吃掉本次 5 小時額度」提示**（MIXED Reality News，2 個來源，2026-10-21 報導，僅標題可用）：功能名稱、版本號與是否已上線均未見官方確認；與今日桌面版文件新增的用量顯示段落是否同一功能待查。
- ❓ **待查證**（標 2026-10-21｜查 Bedrock、schema-enforced）｜**AWS 傳 Amazon Bedrock 為 Claude 新增結構化輸出（schema-enforced outputs），涵蓋兩種 API 介面**（OpenTools，2026-10-20 報導，僅標題可用）：細節未見官方文件確認。
- 🔎 **查無官方**（標 2026-10-15｜查 nested sessions｜複 2026-11-30）｜**Claude Code 桌面版推出「巢狀對話」**（Pasquale Pillitteri＋36Kr，2026-10-15，僅標題）：2 家媒體稱可讓單人同時指揮多個並行 agent；
  - 2026-10-31 查 [桌面版文件](https://code.claude.com/docs/en/desktop.md)、`llms.txt` 索引與 changelog（2.1.316）均無「nested sessions」一詞，官方只有並行 session、side chat（`/btw`，不寫回主對話）與 session 互傳訊息，未見等同功能。
    - 同報導的「已儲存環境設定」**已查實**：桌面版文件載有 saved environment（環境選擇器記錄 Claude 執行位置與資料夾，可建立、編輯、移除；查證日 2026-10-31，來源：[Desktop 文件](https://code.claude.com/docs/en/desktop.md#create-a-saved-environment)）。
- ✅ **SneakPeek（桌面版預覽窗格漏洞，CVSS 8.7）已於 2026-08-17 修補**（[Noma Labs 原文](https://noma.security/noma-labs/sneakpeek-how-the-preview-pane-in-claude-code-desktop-can-exfiltrate-your-data)，查證 2026-10-18）：於 Claude Desktop 1.30096.1 修完並經自動更新推送；CSO Online 的「256KB 預覽窗格洩密」是同一個漏洞。
  - **你該做的**：確認桌面版不低於 1.30096.1；CVE 與 GitHub 安全公告待發，時間線見 [[topics/ai-agent-safety]]。
- ❓ **待查證**（標 2026-10-01｜查 claude.dev、developer hub｜複 2026-11-14｜訊 2026-10-04）｜**Anthropic 據報推出 claude.dev 開發者中心**（Pasquale Pillitteri via Google News，2026-10-01，僅標題）：正式性仍待官方確認。
  - 2026-10-17 搜尋補查：第三方稱其 2026-09-30 上線、由 @ClaudeDevs 宣布、內容多為彙整既有文章；claude.dev 無法自本環境連線，未取得一手公告。
  - 後續（日報 10-04）：claude.dev 網域出現 Opus 5.5 使用教學文（HN 單日 224 分），可見該網域有內容在線；是否為官方開發者中心仍待官方頁面查證。
- 🔎 **查無官方**（標 2026-09-17｜查 bank account、financial data｜複 2026-11-14）｜**BleepingComputer：Anthropic 據報推動讓 Claude 分析銀行帳戶與財務資料**（2026-09-17）：媒體稱在 Claude iOS App 發現名為「Claude Money」的 Money 分頁。
- 媒體為 BleepingComputer、gHacks、TechRepublic；該 Money 分頁可連結銀行帳戶並詢問支出與計畫，多數用戶尚未開放。
- 查證 2026-10-03：anthropic.com／support.claude.com 搜尋均未見官方公告，支援銀行、連結方式、適用方案與上線日皆未載。2026-10-17 再查 [Help Center release notes](https://support.claude.com/en/articles/12138966-release-notes)（最新一筆 2026-10-07）仍無 Money 分頁或銀行帳戶連結條目。
- **官方頁未見 Claude for Excel／Word／PowerPoint／Outlook 下架**（查證 2026-10-03）：[Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365) 頁載明 Excel、PowerPoint、Word 在所有付費方案正式可用，Outlook 在所有付費方案 beta，無下架聲明。
- support.claude.com 仍有獨立文章（[Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)、[Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)）。09-15 五份文件移除相關段落的原因官方未說明，僅確認產品仍在架。
- 同批新增 Salesforce in Claude（beta），09-16 Help Center release notes 另載 M365 connector 新增寫入工具（[release notes](https://support.claude.com/en/articles/12138966-release-notes)）。
  - 同日異動文件：Help Center release notes、Pro/Max plan 說明、usage limits、usage credits、Fable 5 on your plan 五份文件同步異動。
- **Claude in Chrome 的 session 可由企業合規團隊經 Compliance API 調閱**（查證日 2026-10-17，來源：[Compliance API 官方文件](https://platform.claude.com/docs/en/manage-claude/compliance-api)）：Enterprise 組織以 Compliance Access Key 讀取 session 逐字稿。
  - 同一介面涵蓋 Cowork、Claude Code 等產品與 Activity Feed。**beta 之說已過時**（查證日 2026-10-31，來源：[Anthropic 部落格更新註記](https://claude.com/blog/compliance-api-cowork-and-claude-code)）：
    - 2026-08-11 原文稱「beta」，2026-08-26 更新註記改為 Cowork（桌面／網頁／行動）與 Claude Code（CLI／桌面）涵蓋已 GA，僅 Microsoft 365 add-ins 與 Claude Science 仍 beta；
      - [Compliance API 官方文件](https://platform.claude.com/docs/en/manage-claude/compliance-api)對 Activity Feed 與 session 端點未標 beta，MIXED Reality News 的「beta」沿用部落格原文。與 [[entities/claude-security]] 同源。
- **Claude Code 新增 Compliance API 與企業安全功能**（查證日 2026-09-20，來源：[Claude Help Center](https://support.claude.com/en/articles/13015708-access-the-compliance-api)、[platform.claude.com](https://platform.claude.com/docs/en/manage-claude/compliance-api)）：Compliance API 提供 Enterprise／Claude Console 客戶以程式化方式讀取組織 Activity Feed（含 chat、files、projects、sessions、users），供合規、稽核與治理使用；本機 Cowork／Claude Code session 端點於 2026-08-11 上線、2026-08-26 脫離 beta（遠端 Cowork session 端點則於 08-03 先上線）。與 Claude Enterprise／Claude Code Analytics API（回傳聚合用量與成本）不同，Compliance API 回傳逐事件紀錄。
  - Futurism（2026-11-03）以「監視」用詞報導此功能，報導未附存取範圍或啟用方式細節；功能本體即上述已查證的 Compliance API，非新功能。隱私爭議面見 [[topics/ai-agent-safety]]。
- **MCP Python SDK 的 OAuth 憑證外洩漏洞已修補（GHSA-qx49-fqc8-xw99，High、CVSS 7.5，2026-09-28 公開）**（查證日 2026-10-17，來源：[官方 advisory](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-qx49-fqc8-xw99)）：安全面見 [[topics/ai-agent-safety]]。
  - 成因：OAuth 用戶端未在所有探索路徑驗證授權伺服器 issuer，惡意 MCP server 可誘使 client 把 client_secret、授權碼、PKCE verifier 送往攻擊者的 token endpoint。
  - 影響 1.9.1 至 1.30.0 前、2.0.0a1 至 2.2.0 前；1.30.0 與 2.2.0 已修補。stdio client、伺服器端與自帶 token 的 client 不受影響。
  - 升級後：ClientCredentials／PrivateKeyJWT provider 須另傳 `issuer=`，清除已存 client 註冊，疑似外洩的密鑰須輪替。
  - advisory 無 CVE，官方措辭為憑證外洩；Cycode 稱的 account takeover 是其後果推論。
- **Anthropic 為 Claude Desktop 開發的「類 Slack」功能已確認為 Claude Code Projects**（查證日 2026-09-20）：TestingCatalog（2026-08-16）原始報導所稱「built-in Slack」，經比對官方文件（[Projects](https://code.claude.com/docs/en/claude-projects.md)，2026-09-18 進入 Beta）確認為同一功能——一個對話統籌多個雲端 session（thread），可平行執行並跨裝置查看，形式類似頻道／討論串而非傳統聊天室；惟目前為 Pro／Max 方案的個人帳號功能（逐步開放中），並非 Team／Enterprise 的多人協作聊天室，TestingCatalog 原文強調的「多人協作」定位官方文件尚未載明。

其餘六則傳聞已於 2026-09-06 查證，結果見 [[entities/claude-code-releases#歷史記錄]]（五則結案、一則改列「已下架，原因未載」）。

近期新增已知問題與互動數更新見 [[entities/claude-code-known-issues]] 各組。

**產品定位：** Claude Code 是 Anthropic 的 AI 編碼 CLI 工具，已從程式碼助理擴展為完整 agent 開發平台——全桌面自動化、多代理管理（Managed Agents）、MCP Server 整合、Hooks 機制、AI 安全審查，以及可串接 1Password 憑證庫安全登入網站（密碼不外流至 Claude／Anthropic，技術細節見 [[entities/claude-code-features#核心功能]]）；GitHub Stars 達 **131,000+**。桌面版（Claude Code Desktop）官方文件（2026-08-26 查證）列出的功能：各自獨立 Git 隔離的並行 session、可拖曳的分割面板版面、整合終端機與檔案編輯器、側邊聊天（side chats），以及可從手機端啟動 session。該頁為靜態說明頁，本次重新抓取無法判斷是否含新增能力。

**官方使用研究：** Anthropic 發表基於 2025/10–2026/04 約 40 萬個 session 的分析研究，發現人類主導規劃決策、Claude 主導執行決策，且使用者領域專業越高，Claude 每條指令完成的工作量越大。

**市場與競爭：** Microsoft 正陸續取消內部授權轉推 GitHub Copilot CLI（見 [[topics/competitor-landscape]]）；Ramp AI Index 顯示 Anthropic 企業採用率持續領先 OpenAI（43.5% vs 39.7%，2026-08-12 發布，詳表見 [[topics/anthropic-business]]）；AWS 於 2026-07-15 推出「Claude Apps Gateway」，定位為 Claude Code 與 Claude Desktop 可自架部署（self-hosted）的控制平面，集中身分／政策／遙測／路由／支出上限，路由到 Bedrock 或 Claude Platform on AWS；**Claude Code CLI 官方內建支援**（`claude-apps-gateway` 專頁，2026-09-06 查證，[AWS 官方 blog](https://aws.amazon.com/blogs/) 07-08）。The GitHub Blog（2026-07-24，經 Google News 轉載）報導 Claude Opus 5 已在 GitHub Copilot 上線，屬 Anthropic 模型透過微軟生態系分發的延續；模型陣容細節見 [[topics/model-comparison]]。Unity 於 2026-09-10 推出官方 Claude Code 外掛，內建 29 項遊戲引擎相關技能，讓開發者可在 Unity 專案中直接透過 Claude Code 呼叫引擎層級操作（Pocket Gamer.biz、Inven Global 兩家遊戲媒體獨立報導）；此為 Unity 自家發行的第三方外掛，非 Anthropic 官方產物，故不進 [[feature-radar]]。The Information（09-15，僅標題）報導部分開發者正找方法在 Claude Code 中繞過官方模型、改接其他供應商，呼應既有「多模型路由/鎖定防禦」缺口，見 [[topics/official-community-gap]]；Dealroom（09-16，2 個來源同日報導）同向補充：開發者傾向把 Claude Code 接到非 Anthropic 模型後端執行，Anthropic 因此收不到對應 token 費用。TradingView（09-17，官方公告，僅標題可用）推出自家 MCP Server 讓 Claude 串接 TradingView 資料與操作，付費方案 public beta；與 Unity 外掛同屬第三方自行發行的 MCP／外掛整合，非 Anthropic 官方產物，故不進 [[feature-radar]]。

### 未歸類

%% 判不出該歸哪個子頁的條目先寫這裡，週更時分派（.claude/reporter-rules/features/pages.md 母頁路由表） %%
目前沒有。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ✅ 強烈推薦 |
| 最適合 | 需要 agentic 工作流、multi-agent 協作、或整合 MCP 工具的工程師與 SaaS 開發者 |
| 不適合 | 高度依賴 AWS Bedrock 接入（功能落差常態存在）；或對 CLAUDE.md 指令執行率有嚴格要求的場景 |

> 詳細最新熱度見 [[feature-radar]]

**反向對照**（替代方案宣稱比 Claude Code 好，證據等級寫在條內）：

- **社群工具 token-savior 自測宣稱優於 Claude Code 原生編碼表現（2026-10-07，Mibayy/token-savior GitHub repo 自述）**：作者自測稱 Claude Code 原生（plain）基準正確率 78.3%，低於其工具版本；證據等級僅作者自測，未附第三方覆核方法論或測試環境細節，僅供參考。


---

## 版本更新

逐版明細、stable／latest 通道與歷史記錄見 [[entities/claude-code-releases]]；升版前要知道的破壞性變更見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。

## hooks：事件、失效模式與能不能當防線

hook 一觸發就是硬擋（先於 allow 規則），但比對是盡力而為，也有不觸發的回報；要保證一定擋，用沙箱；deny 規則與 hook 都當第二層。事件表、失效模式與官方原句見 [[entities/claude-code-features#hooks：事件、失效模式與能不能當防線]]。

---

## 相關議題

- [[topics/code-quality-decline]]
- [[topics/competitor-landscape]]（含 Google 未命名工具、Cursor、Windsurf、GitHub Copilot 等競品動態）
- [[topics/ai-agent-safety]]
- [[topics/official-community-gap]]（官方功能路線 vs 社群痛點缺口分析）
- [[topics/community-tech-tools]]（社群工具完整目錄、活躍度與採用狀態，每週策展）
- [[entities/claude-design]]（AI 設計工具，與 Claude Code 整合尚不完善）
- [[entities/openclaw]]（第三方 agentic 工具，Anthropic 主動管控中）
- [[entities/claude-tag]]（Slack-native AI 協作工具，定位為 Claude Code 向團隊協作方向的延伸）
- [[entities/boris-cherny]]（Claude Code 創始人）
- [[entities/cat-wu]]（Claude Code 產品負責人，AI 主動性論述）
- [[entities/claude-for-teachers]]（同為 Anthropic 產品線，面向 K-12 教師的免費進階存取方案）

## 參考來源（最近 10 則）

- [[news/2026-11-01]]
- [[news/2026-10-31]]
- [[news/2026-10-30]]
- [[news/2026-10-29]]
- [[news/2026-10-28]]
- [[news/2026-10-27]]
- [[news/2026-10-26]]
- [[news/2026-10-25]]
- [[news/2026-10-24]]
- [[news/2026-10-23]]

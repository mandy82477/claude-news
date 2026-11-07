---
page: "entities/claude-code-releases"
kind: "entity"
type: "product"
status: "active"
domain: "🛠️ 工具/功能"
last_updated: "2026-11-06"
last_news_update: "2026-11-06"
status_main: "active"
days_since_news: 1
parent: "entities/claude-code"
children: "[]"
page_role: "child"
days_since_news_subtree: 1
inbound_links: 7
attribution_count: 7
attribution_last: "2026-11-06"
top_source: "github"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code 版本與發布通道：現在到哪一版、該跟哪條

現在到哪一版、我在 stable 還是 latest、哪一版加了什麼。

**類型：** product
**狀態：** active
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**首次出現：** 2025（正式推出）
**最後更新：** 2026-11-06
**最後新聞更新：** 2026-11-06
%% 2026-11-01 第 21 波自 [[entities/claude-code]] 拆出：發布通道、版本表、歷史記錄原文照搬；發布超過 90 天的 82 列與 2026-08 歷史 24 列移到 [[entities/claude-code-archive]]；母頁現況的逐版副本刪除，只在那裡的 v2.1.289、v2.1.269 補成表列 %%

> **最新動態**（2026-11-06）
> - **v2.1.319**：⚠️ auto mode 在遙測或功能旗標關閉時（含透過 LLM gateway）行為改變——伺服器無法檢查的呼叫一律詢問使用者或直接拒絕，不再退回內建傳統分類方式，無遷移期。
> - **SDK**：anthropic-sdk-typescript sdk-v1.6.0、anthropic-sdk-python v2.6.0 同步新增 ramp limit／External Key 驗證失敗的錯誤代碼，並支援強制組織成員全裝置登出。
> - **⚠️ Opus 4.8 fast mode 10-30 起棄用、11-30 移除**：移除後不會自動改用別的模型，請求直接回錯誤；用 fast mode 的人要改 Opus 5.5。

---

## 現在該跟哪條

- **stable＝2.1.309、latest＝2.1.316**（npm dist-tags，查證 2026-11-01），差 7 個版號。
- **沒用 Opus 4.8 fast mode，stable 已夠**：危險 `rm` 的兩道修正（2.1.287／288）與 bypass 模式改直接拒絕（2.1.309，限 Desktop 與 VS Code）都在 stable 裡。
- **要這些才需要 latest**：Monitor tool（2.1.310）、`blockWritesOutsideWorkingDirectories`（2.1.314，預設關）。
- **升版會改到既有行為的**：破壞性變更與預設值改變見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。

## 發布通道（stable／latest）

官方安裝文件（[setup](https://code.claude.com/docs/en/setup)，2026-10-04 查證）：Claude Code 有 latest 與 stable 兩條通道，stable 約晚一週；現在該跟哪條見上方。

- **誰會落在 stable**：自己把 `autoUpdatesChannel` 設成 `"stable"`；用 Homebrew 的 `claude-code` cask（`claude-code@latest` 才是 latest）；照官方文件用 apt、dnf、apk 安裝。原生安裝的 `autoUpdatesChannel` 預設是 latest。
- **套件管理器安裝不會自己更新**：Homebrew、apt、dnf、apk 都要手動升級，落在 stable 又沒升級的人版本會比預期更舊。
- **升版前先查**：`claude --version` 看現在跑哪一版，設定檔裡的 `autoUpdatesChannel` 看跟哪條通道。
- **`minimumVersion` 的限制**：只讓自動更新不裝比它舊的版本；官方文件沒說它會把 stable 拉高，不能拿來補 stable 的落差。

## 最新版本

> 本表只收本站報導過的版本。**v2.1.242–244 與 v2.1.253–257 未見報導，不代表未發布。** 發布超過 90 天的版本見 [[entities/claude-code-archive]]；破壞性變更與預設值改變見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。

> 版本表沒有 2.1.313：官方 CLI changelog 在 2.1.312 之後是 2.1.314（2026-11-01 查）；「2.1.312／2.1.313」是 Cursor 市集遭竄改的 VS Code 延伸套件版號，事件見 [[topics/ai-agent-safety-product-vulns#2026-10]]。

| 版本 | 發布日 | 重點 |
|------|------|------|
| **v2.1.319** | 2026-11-06 | ⚠️ auto mode 在遙測或功能旗標關閉時（含透過 LLM gateway）：伺服器無法檢查的呼叫一律詢問使用者或直接拒絕，不再退回內建傳統分類方式；無遷移期（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.319)）|
| **anthropic-sdk-typescript sdk-v1.6.0** | 2026-11-05 | Features：新增 ramp limit 錯誤代碼、External Key 驗證失敗錯誤代碼，支援強制組織成員全裝置登出（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v1.6.0)）|
| **anthropic-sdk-python v2.6.0** | 2026-11-05 | Features：同步新增 ramp limit 錯誤代碼、External Key 驗證失敗錯誤代碼，支援強制組織成員全裝置登出（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.6.0)）|
| **v2.1.318** | 2026-11-04 | 啟用 session 中寫出的 mods 時新增記錄使用者回答；Claude apps gateway `mantle` 上游新增 `assume_role` 設定；官方原文截斷，角色細節未附（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.318)）|
| **v2.1.317** | 2026-11-03 | `/schedule` 新增警告：雲端排程任務取得非使用者要求的 connector 時提示並附移除方式；新增工具呼叫前確認檢查；另有異動但原文截斷（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.317)）|
| **anthropic-sdk-python v2.4.0** | 2026-11-02 | Features：新增 analytics、spend limits 與 RBAC 的 GA 方法；新增 unified metrics、RBAC 刪除回應的具名 beta 型別（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.4.0)）|
| **anthropic-sdk-typescript vertex-sdk-v1.1.1** | 2026-11-02 | Chores：為每個子套件的已發布型別宣告加上型別檢查，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v1.1.1)）|
| **anthropic-sdk-typescript google-cloud-sdk-v1.1.2** | 2026-11-02 | Chores：同批型別檢查；Docs：範例程式改用現行模型 ID（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v1.1.2)）|
| **v2.1.316** | 2026-10-31 | 新增 `CLAUDE_CODE_DISABLE_ULTRATHINK`；⚠️ Opus 4.8 fast mode 11-30 移除；修 PowerShell hook exit 2 沒擋（[Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.316)）|
| **v2.1.314** | 2026-10-30 | 新增 `permissions.blockWritesOutsideWorkingDirectories`：Write、Edit、NotebookEdit 在任何權限模式下拒絕寫入工作目錄外路徑；另有異動但原文截斷（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.314)）|
| **v2.1.312** | 2026-10-27 | 新增 `oidc.user_id_claim` 設定，gateway 可用 `sub` 以外 id_token claim（如 Entra ID `oid`）識別使用者；另有異動但原文截斷（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.312)）|
| **v2.1.311** | 2026-10-26 | `self-hosted-runner` 新增 `--hold-idle-file`、`--max-hold-min`，host 回報殘留行程時可保留 idle session 不被提早回收（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.311)）|
| **v2.1.310** | 2026-10-23 | 新增 Monitor tool，含 Bedrock／Vertex／Foundry 的 plugin 監控；停用 telemetry 或非必要流量時攔阻長時間 foreground sleep（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.310)）|
| **anthropic-sdk-python v2.3.0** | 2026-10-23 | Features：新增 Claude Tag（Claude Enterprise 組織）API endpoint；Bug fix：Google Cloud 路由下使用者個人資料請求改送往組織端點（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.3.0)）|
| **anthropic-sdk-typescript google-cloud-sdk-v1.1.1** | 2026-10-23 | Bug fix：Google Cloud 路由下使用者個人資料請求改送往組織端點；測試不再預期 beta query 參數（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v1.1.1)）|
| **anthropic-sdk-python v2.2.0** | 2026-10-23 | 新增 message threads 支援與依維度拆分用量費用報表；client 不再建議 `max_tokens` 用 `math.inf`（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.2.0)）|
| **anthropic-sdk-typescript vertex-sdk-v1.1.0** | 2026-10-23 | 新增 message threads 支援，與同日 Python SDK 呼應（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v1.1.0)）|
| **v2.1.309** | 2026-10-22 | 修正 sandboxed Bash 執行前跑過 shell 啟動檔、macOS `denyWrite` 規則比對不完全；Desktop／VS Code 的 bypass 模式危險 `rm`／`rmdir` 直接拒絕（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.309)）|
| **v2.1.308** | 2026-10-22 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.308)）|
| **anthropic-sdk-typescript vertex-sdk-v1.0.0** | 2026-10-21 | 正式滿 1.0；⚠️ Breaking：改支援新版 API，API 版本 `2026-10-21` 移除 `temperature`、`top_p`、`top_k` 請求參數，送出任一者在所有模型回 400（[Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v1.0.0)）|
| **anthropic-sdk-python v2.1.0** | 2026-10-21 | Features：User Profiles API 新增 enforcement status、actions 與 filter 參數（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.1.0)）|
| **v2.1.306** | 2026-10-21 | Bug fixes：修正雲端 session 未帶環境變數執行 `claude -p` 誤報「Not logged in」；修正原被「prompt too long」蓋掉的 API 錯誤；純 bug 修復（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.306)）|
| **anthropic-sdk-python v1.17.0** | 2026-10-20 | Features：新增組織層級 webhook 端點與使用者個人資料強制設定事件；Admin API 新增 RBAC 群組擁有者權限錯誤碼；補 `unsupported_charset` 說明（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.17.0)）|
| **anthropic-sdk-typescript vertex-sdk-v0.22.0** | 2026-10-20 | ⚠️ 行為變更：讀取 `AnthropicVertex` 的 `userProfiles`／`beta.userProfiles` 改拋出 `AnthropicError`（Vertex 不提供此端點）（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.22.0)）|
| **v2.1.304** | 2026-10-19 | 新增 `/auto-mode-setup`、`/claude-api managed-agents-secure`、Code Review 審查等級；⚠️ tool search 預設開（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.304)）|
| **v2.1.303** | 2026-10-18 | Bug fixes and reliability improvements，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.303)）|
| **v2.1.302** | 2026-10-16 | 新增 `CLAUDE_CODE_AUTO_MODE_MODEL`、`/config` Idle compaction 開關；⚠️ `-p` 預設權限模式與 fork subagent 預設改變（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.302)）|
| **anthropic-sdk-python v1.15.0** | 2026-10-15 | thinking 類型新增 `between_tools`；Messages 新增 `speed` 參數與對應 `usage.speed`；可讀取 Console 組織用量等級（usage-tier）（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.15.0)）|
| **anthropic-sdk-typescript sdk-v0.135.0** | 2026-10-15 | 同步 Python v1.15.0：thinking 新增 `between_tools`、Messages 新增 `speed`／`usage.speed`、Console 組織用量等級（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.135.0)）|
| **v2.1.301** | 2026-10-15 | 新增 `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS`：無人值守重試模式於額度重置過久時主動結束請求（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.301)）|
| **v2.1.300** | 2026-10-14 | mods 新 hook、`virtualText`；OTel 新屬性；`/advisor`；⚠️ gzip、hook `updatedInput` 驗證（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.300)）|
| **anthropic-sdk-typescript vertex-sdk-v0.21.0** | 2026-10-14 | 新增 `execution_identity`；client 原生支援 OpenTelemetry tracing（已註冊 tracer provider 時自動匯出 span）（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.21.0)）|
| **anthropic-sdk-python v1.14.0** | 2026-10-14 | 同步新增 `execution_identity`；另新增花費上限錯誤類型 `organization_type_not_supported`、telemetry destination 測試端點（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.14.0)）|
| **v2.1.299** | 2026-10-14 | 新增 `CLAUDE_CODE_DISABLE_FILE_MENTIONS`：`@` 檔案提及只傳路徑不灌入內容；同版修復 gateway API key 外洩與排程夏令時間重複觸發（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.299)）|
| **v2.1.296** | 2026-10-09 | Claude apps gateway `managed.policies[]` 新增 `code` 鍵：套用與 `cli` 相同設定，獨立套用到 Claude Desktop 的「Code」分頁（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.296)）|
| **v2.1.295** | 2026-10-08 | 新增 hook `onFailure: "block"`；Bedrock/Vertex/Foundry token 計數改用 CountTokens API；MCP 工具描述上限 2,048→16,384 字元（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.295)）|
| **anthropic-sdk-typescript sdk-v0.133.0** | 2026-10-09 | 新增 Chat/Cowork 分析指標型別；新增 Managed Agents workflows、多代理設定與 thread 過濾（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.133.0)）|
| **anthropic-sdk-python v1.13.0** | 2026-10-09 | 同步新增 Chat/Cowork 分析指標型別；新增 Managed Agents workflows、多代理設定與 thread 過濾，細節見 [[entities/managed-agents]]（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.13.0)）|
| **v2.1.294** | 2026-10-08 | 修正 `prompt`／`agent` hook 寫成自然語言指示時擋不住該指令的問題；改善 `Stop`／`SubagentStop` 上 `prompt` hook 行為；純 bug 修復（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.294)）|
| **anthropic-sdk-python v1.12.1** | 2026-10-08 | Chores：CI 新增檢查 PR 是否更新 changelog、補充 Claude Console 查詢支出限額仍屬 early access、內部對齊 uv.lock 版本號，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.12.1)）|
| **anthropic-sdk-typescript google-cloud-sdk-v0.0.19** | 2026-10-08 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.19)）|
| **anthropic-sdk-typescript vertex-sdk-v0.20.4** | 2026-10-08 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.20.4)）|
| **v2.1.292** | 2026-10-06 | 新增 `claude plugin install --marketplace <source>`，裝外掛時一併加入所需市集來源，沿用 `claude plugin marketplace add` 政策檢查（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.292)）|
| **v2.1.291** | 2026-10-06 | 修正兩項回歸：雲端 session 遺失權限提示答案（源自 v2.1.290）、對話尾端訊息遺失（源自 v2.1.288）；純 bug 修復（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.291)）|
| **v2.1.289** | 2026-10-03 | 修正巢狀 shell 複合指令中 deny／ask 規則對使用者安裝的 mod 核准不生效；修正短指令造成終端機凍結；純 bug 修復（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.289)）|
| **v2.1.288** | 2026-10-02 | 新增 `--max-findings`、`claude purge`；修正 `bash -c` 內危險 `rm` 繞過檢查（#96300）；stable 仍在 2.1.285（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.288)）|
| **v2.1.287** | 2026-10-01 | **新增「Claude Mods」**（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.287)），細節見 [[entities/claude-mods]] |
| **v2.1.286** | 2026-09-30 | 權限提示堆疊多筆請求時新增「2 of 5」計數顯示；全螢幕模式清單「N more」列新增滑鼠點擊展開支援（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.286)）|
| **anthropic-sdk-python v1.11.0** | 2026-09-30 | Features：新增 list spend limits endpoint，可透過 API 查詢支出限額設定（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.11.0)）|
| **anthropic-sdk-typescript google-cloud-sdk v0.0.17** | 2026-09-30 | 例行維護性版本更新，官方 changelog 未列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.17)）|
| **anthropic-sdk-typescript vertex-sdk v0.20.2** | 2026-09-30 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.20.2)）|
| **v2.1.285** | 2026-09-29 | 新增 `CLAUDE_CODE_DISABLE_WEB_FETCH` 關閉 WebFetch；新增 `claude --desktop` 開啟桌面版；企業可限制 API 供應商（原文截斷，見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.285)）|
| **v2.1.284** | 2026-09-28 | Claude Sonnet 5.5（`claude-sonnet-5-5`）成 API 預設 Sonnet 模型，見 [[entities/sonnet-5-5]]；新增「Yes, but ask」功能，行為未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.284)）|
| **anthropic-sdk-python v1.9.0** | 2026-09-28 | Features：新增 `between_tools` thinking type 的 API 支援（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.9.0)）|
| **anthropic-sdk-typescript vertex-sdk v0.20.0** | 2026-09-28 | Features：官方 changelog 於「### Feature」處截斷，具體項目未知（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.20.0)）|
| **anthropic-sdk-typescript google-cloud-sdk v0.0.15** | 2026-09-28 | 例行維護性版本更新，官方 changelog 未列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.15)）|
| **v2.1.283** | 2026-09-25 | 新增 `x-claude-code-prompt-id` 閘道提示標頭，供 LLM gateway 歸組同一提示的多筆請求；需設 `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1` 選擇加入（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.283)）|
| **v2.1.282** | 2026-09-24 | 新增 `maxProseWidth` 設定，限制寬終端機下散文輸出寬度（表格／程式碼區塊全寬）；新增啟動通知，`/status` 亦有異動（原文截斷，細節未載，見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.282)）|
| **v2.1.281** | 2026-09-23 | 新增 desktop policy 設定：`blockReadsOutsideWorkingDirectories`、`disableBypassPermissionsMode`（gateway，見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.281)）|
| **v2.1.280** | 2026-09-22 | **Opus 5.5 成新預設模型**（Foundry 仍 Sonnet 4.5，2026-09-23 查證），$4／$20 每 Mtok；全螢幕更多清單支援滑鼠（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.280)）|
| **v2.1.278** | 2026-09-19 | Auto mode 預設免計費改用 server-side classifier（API／Enterprise／Bedrock／Vertex／Foundry／閘道器）；`/status` 新增顯示列（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.278)）|
| **v2.1.277** | 2026-09-18 | 新增 AGENTS.md 支援：無 CLAUDE.md 時改讀 AGENTS.md，可於 `/config` 調整；尚未支援 Bedrock、Vertex、Foundry（見 [Changelog](https://code.claude.com/docs/en/changelog)）|
| **anthropic-sdk-python v1.7.0** | 2026-09-18 | Features：新增 rate limit 群組可帶 `display_name` 欄位（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.7.0)）|
| **anthropic-sdk-typescript vertex-sdk v0.19.10** | 2026-09-18 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.19.10)）|
| **anthropic-sdk-typescript google-cloud-sdk v0.0.13** | 2026-09-18 | 例行維護性版本更新，官方 changelog 未列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.13)）|
| **v2.1.276** | 2026-09-18 | Bug fix：修復 2.1.275 迴歸——proxy/gateway 下 `advisor_20260301` 標籤觸發 400 全數失敗；純修復無新旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.276)）|
| **v2.1.274** | 2026-09-17 | 新增記憶體用量過高時的可見警示（附釋放記憶體或安全重啟步驟）；新增 `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` 旗標，限制首次非互動啟動的等待時間；官方原文於此處截斷，其餘變更項目未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.274)）|
| **v2.1.273** | 2026-09-15 | 新增 5 個內部遙測用途請求標頭，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.273)）|
| **anthropic-sdk-python v1.6.0** | 2026-09-15 | Features：新增 Managed Agents 相關 auto mode 工具權限功能，官方原文截斷、完整範圍未知，細節見 [[entities/managed-agents]]（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.6.0)）|
| **anthropic-sdk-typescript vertex-sdk v0.19.9** | 2026-09-15 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.19.9)）|
| **anthropic-sdk-typescript google-cloud-sdk v0.0.12** | 2026-09-15 | 例行維護性版本更新，官方 changelog 未列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.12)）|
| **v2.1.272** | 2026-09-15 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.272)）|
| **v2.1.270** | 2026-09-12 | Bug fix：修復 2.1.269 一項迴歸——長時間執行的 session 中，唯讀 git 指令會意外要求使用者授權；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.270)）|
| **v2.1.269** | 2026-09-11 | 新增 `claude plugin eval`：對外掛跑 eval 套件，產出可重現的 JSON＋HTML 評分（含不裝外掛的對照組）；同版新增 `/output-style`（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.269)）|
| **v2.1.268** | 2026-09-10 | gateway.yaml 新增 `pricing:` 設定，登入客戶端經 managed settings 取得一致費率，`/cost`／telemetry 對得上；見 [[entities/pricing]]（[Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.268)）|
| **v2.1.267** | 2026-09-09 | 新增 `maxEffortLevel` 設定，統一設定 Bedrock／Vertex／Foundry 等供應商的推理努力上限，仍可在上限內自選較低等級（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.267)）|
| **v2.1.266** | 2026-09-08 | Bug fix：修復 2.1.265 一項迴歸，影響 LLM-gateway／proxy 的 `CLAUDE_CODE_USE_GATEWAY` 環境變數（原文截斷，細節未知）；純 bug 修復（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.266)）|
| **v2.1.263** | 2026-09-06 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.263)）|
| **v2.1.261** | 2026-09-04 | `/status` 與 `claude doctor` 新增「Organization policy」欄位，說明組織政策載入失敗的原因（例如代理伺服器未正確轉發 endpoint）（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.261)）|
| **anthropic-sdk-python v1.4.0** | 2026-09-04 | Features：新增 Claude Tag 分類與使用者用量分項的 API 支援（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.4.0)）|
| **anthropic-sdk-typescript vertex-sdk v0.19.7** | 2026-09-04 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.19.7)）|
| **v2.1.259** | 2026-09-02 | 新增 `managedMcpServers` 管理設定，組織可統一為所有使用者佈署 HTTP/SSE MCP 伺服器，設定格式比照 `.mcp.json`；非 breaking change（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.259)）|
| **v2.1.258** | 2026-09-01 | Bug fix：修復 macOS 12（Monterey）啟動失敗問題（v2.1.255 引入的回歸），並修復 remote／排程 session 因「使用者訊息不得為空」而失敗的問題；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.258)）|
| **anthropic-sdk-typescript sdk-v0.123.0** | 2026-09-01 | Features：新增 beta 版使用者個人資料（user profiles）API 支援，含 `external_user_onboarding` 等欄位（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.123.0)）|
| **anthropic-sdk-python v1.3.0** | 2026-09-01 | Features：同步新增 beta 版使用者個人資料（user profiles）API 支援，含 `external_user_onboarding` 等欄位（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.3.0)）|
| **v2.1.252** | 2026-08-31 | Bug fix：修復 Bash 指令因「task output swap refused」在部分 Mac 上失敗的問題，以及專案缺 `.claude/settings.local.json` 時「always allow」設定無法儲存的問題；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.252)）|
| **v2.1.251** | 2026-08-28 | 新增 `PreModelSwitch`／`PostModelSwitch` hook 事件，可攔截、確認或標註模型切換；`SessionStart` resume hook 現在回傳 session 新鮮度與估計流失的內容量（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.251)）|
| **v2.1.250** | 2026-08-28 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.250)）|
| **anthropic-sdk-typescript sdk-v0.122.0** | 2026-08-27 | beta 版 files／skills 命名空間改用正式版（GA）介面形狀（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.122.0)）|
| **anthropic-sdk-python v1.2.0** | 2026-08-27 | 同步將 beta 版 files／skills 命名空間改用正式版（GA）介面形狀（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.2.0)）|
| **v2.1.247** | 2026-08-27 | 新增 `SendFeedback` 工具：session 中出錯時，Claude 可草擬一份回報供使用者於 `/feedback` 檢視後送出，可用 `feedbackDisabled` 設定關閉此功能（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.247)）|
| **v2.1.246** | 2026-08-26 | 新增啟動警告：Bash 允許規則在子指令前使用萬用字元（如 `Bash(git * main)`）會意外比對插入在子指令前的選項參數，官方提示提醒使用者留意；官方 changelog 原文截斷，其餘變更項目未完整取得；無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.246)）|
| **v2.1.245** | 2026-08-25 | Bug fix：修復搭載 glibc 2.44 的 Linux 發行版（例如 Arch Linux、CachyOS、Fedora Rawhide）上啟動時發生的當機問題；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.245)）|
| **v2.1.241** | 2026-08-23 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.241)）|
| **v2.1.239** | 2026-08-21 | Cost estimates（`/cost`、狀態列、`--max-budget-usd`）現會計入資料常駐（data-residency）工作區的 1.1 倍純美國推理附加費；另有一項全螢幕渲染器相關設定調整，官方 changelog 原文於此處截斷，其餘細節未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.239)）|
| **v2.1.238** | 2026-08-20 | 新增 `keybindingFlavor` 設定：設為 `"readline"` 時可讓提示列中的 Ctrl+W 依 Bash 慣例刪除到前一個空白字元，預設值 `"classic"` 行為不變（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.238)）|
| **anthropic-sdk-python v1.0.0** | 2026-08-20 | ⚠️ **Breaking change**：SDK 正式發布 1.0.0，client 升級至 httpx2；官方未提供明確遷移時程，升級前建議先查閱完整 changelog（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.0.0)）|
| **v2.1.237** | 2026-08-20 | 修復使用 LLM gateway 或自訂 base URL 的 session 中 prompt caching 失效問題；新增內建「Concise」輸出風格，讓 Claude 直接給結果、省去前言與敘述性文字（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.237)）|
| **anthropic-sdk-python v0.125.0** | 2026-08-19 | Features：新增 managed agents 的 web search 設定相關功能，官方 changelog 未列出具體項目，詳見 [[entities/managed-agents]]（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.125.0)）|
| **anthropic-sdk-typescript vertex-sdk v0.19.5 / google-cloud-sdk v0.0.10** | 2026-08-19 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.19.5)）|
| **v2.1.235** | 2026-08-18 | 新增可選 `spellcheck` 設定：透過本機安裝的 aspell／hunspell／ispell，即時在輸入框底線標出拼字錯誤；同時修復一項與整段提示詞（whole-prompt）相關的問題，官方 changelog 原文於此處截斷，其餘細節未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.235)）|
| **v2.1.234** | 2026-08-17 | 新增可選環境變數 `CLAUDE_CODE_PROJECT_DIR_NAME`：讓每個 session 有獨立設定目錄的主機（如 CI／多租戶執行環境）可為專案 transcript 目錄自訂短名稱；官方 changelog 原文於此處截斷，其餘細節未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.234)）|
| **v2.1.233** | 2026-08-14 | 新增 GitLab MR URL 顯示支援（`--worktree` 旗標本身早於 v2.1.133 即存在）；新增選用 `forward_user_identity` gateway 設定（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.233)）|
| **v2.1.232** | 2026-08-13 | Subagent forking 預設開啟：帶 `subagent_type: "fork"` 的 subagent 現在預設繼承完整對話與 prompt cache；互動 session 中非 teammate 的 agent 任務指派行為亦有相應調整，官方 changelog 原文於此處截斷，細節未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.232)）|
| **anthropic-sdk-typescript vertex-sdk v0.19.4** | 2026-08-13 | Chores：例行維護，官方 changelog 未列具體異動項目，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.19.4)）|
| **anthropic-sdk-python v0.122.0** | 2026-08-13 | Features：新增 API `output_behavior` 欄位支援於 dream creation（可建立新記憶庫或原地更新既有輸入庫），非先前判讀的「dream cr」截斷字詞（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.122.0)，查證日 2026-09-20）|
| **v2.1.231** | 2026-08-13 | Bug fix：修復 MCP OAuth 登入失敗問題，針對使用預先註冊 OAuth client 的伺服器（如 Slack）先前因 redirect URI 不符而登入失敗；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.231)）|
| **v2.1.228** | 2026-08-11 | Bug fixes：修復互動式 session 因罕見內部排版錯誤而停止重繪畫面（背景程序仍持續執行）；修復 Windows 上找不到 `git`／Git Bash 的問題；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.228)）|
| **v2.1.227** | 2026-08-10 | Bug fix：session 以過期登入 token 啟動時，feature flag 未依使用者訂閱層級正確評估，曾導致 Max 方案使用者被誤導提示啟用相關功能；純 bug 修復，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.227)）|
| **v2.1.226** | 2026-08-08 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.226)）|
| **anthropic-sdk-python v0.121.0** | 2026-08-07 | Features：新增 `mid-conversation-tool-changes-2026-07-01` beta——可在對話進行中的系統訊息附加工具異動（新增／移除工具）而不使既有 prompt cache 失效；另新增 session budgets、advisor tool、pinned inference location、GitHub skills 自動載入等 API 支援（2026-08-10 查證，見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.121.0)）|
| **anthropic-sdk-typescript google-cloud-sdk v0.0.7** | 2026-08-07 | Bug Fixes：client 改用固定字串作為 User-Agent，不再依賴 constructor 名稱；純相容性修正，無使用者端功能異動（2026-08-10 查證，見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.7)）|
| **anthropic-sdk-typescript vertex-sdk v0.19.1** | 2026-08-07 | Bug Fixes，具體修復項目未在摘要中顯示，純修正無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.19.1)）|
| **v2.1.224** | 2026-08-07 | 新增 `claude self-hosted-runner`（Team／Enterprise）；同版新增跨 session `SendMessage`＋`ListAgents`，見已知問題頁「📂 Session」組（[Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.224)）|
| **v2.1.223** | 2026-08-06 | ⚠️ **安全修復**：一次修補 agentic 權限層 4 項邊界——Bash 指令可隱藏部分內容躲過權限掃描、tab／隱形 Unicode 填塞讓核准對話框看不出實際內容、workflow script 用動態 `import()` 逃出沙箱、`bypassPermissions` agent 定義無視組織政策停用 bypass 模式（2026-08-10 查證，見已知問題「🛡️ 安全與隱私」）|
| **v2.1.222** | 2026-08-04 | ⚠️ **安全修復**：修復 worktree-isolated session 與其 subagent 可對主 checkout 執行破壞性 git 指令的隔離漏洞；隔離範圍擴大至每個 session 中的檔案編輯（file edits）與 Bash 執行，不再侷限於 git 層（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.222)）|
| **v2.1.221** | 2026-08-04 | **[VSCode] 新增 Focus view**：chat-menu 切換選項，將工具活動摺疊為可展開的每輪摘要並附即時執行指示，可用 `Ctrl+Alt+F` 或選單切換（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.221)）|

**表格細節**
- **vertex-sdk-v1.0.0 的 API 版本依據（查證日 2026-11-08）**：[API 版本說明](https://platform.claude.com/docs/en/api/versioning)；SDK 預設送該版本，見[發布說明](https://platform.claude.com/docs/en/release-notes/overview)。

## 開發者須知

- **anthropic-sdk-typescript 修補 ID 路徑注入漏洞（2026-11-04）**：project／location／workspace ID（Vertex 另含 model）組路徑前先百分號編碼，值為 `.` 或 `..` 改丟 `AnthropicError`，防止路徑逃逸；用 GCP／Vertex 的開發者建議升級。
- **底層 runtime 確認改用 Rust 版 Bun（2026-07-19 證實）**：Simon Willison 透過字串比對驗證 Jarred Sumner 的說法——Claude Code 自 **v2.1.181**（2026-06-17 發布）起，底層執行環境已改用 Rust 重寫版 Bun runtime，Linux 平台啟動速度提升約 10%，但屬底層基礎設施更新，多數使用者對此毫無察覺（作者以 `strings ~/.local/bin/claude | grep -m1 'Bun v1'` 等指令驗證，找到 563 個 `.rs` 檔名）。


## 歷史記錄

**2026-09-06 懸置查證備忘**
- Cowork 可於 Chrome 側邊欄執行結案（官方 08-12 blog，Max／Team 即日、Pro 數週內，不支援其他 Chromium 瀏覽器與行動版）。
- `/design` 指令結案（官方 early preview，CLI 與桌面版皆可用，`claude update` 即可取得）。
- Cowork 內建瀏覽器結案（多家媒體轉述交叉確認，未取得官方原文）；Cowork 行動版結案（官方 Help Center 確認 iPhone／iPad／Android 皆可用）。
- Legacy Console Workbench 於 08-17 存取終止，未匯出 saved prompts 不可恢復；官方文件索引移除「Slash Commands in the SDK」頁，改列「已下架，原因未載」。
- 事實更正：AWS「Claude Apps Gateway」為 Claude Code CLI 官方內建支援，非第三方生態工具。
- 2026 年 4 月效能退步事件轉列已修復（官方 04-23 說明三原因並於 v2.1.116 修復）。

| 日期 | 事件 |
|------|------|
| 2026-11-06 | **v2.1.319**：⚠️ auto mode 遙測／旗標關閉改一律詢問或拒絕。旗標+13，見 [[topics/claude-code-experimental]]。SDK 新增錯誤碼＋強制登出。互動更新 6 則。 |
| 2026-11-05 | 無新版本。SDK：python v2.5.0 新增錯誤型別／ids 篩選；typescript 兩版修補路徑注入。新增已知問題 #79305／84862／74558；互動更新 #91495／42542／79808。 |
| 2026-11-04 | **v2.1.318**：mods 回答記錄；gateway 新增 `assume_role`。旗標+12/-1（見 [[topics/claude-code-experimental]]）。新增 #33323；互動更新 #12925。 |
| 2026-11-03 | **v2.1.317**：`/schedule` connector 警告＋確認檢查；旗標+12＋2代號，消失1。文件字數增。互動更新 #26224／#30112／#53915。 |
| 2026-10-24 | **v2.1.310**：Monitor tool＋plugin 監控；旗標+4。SDK 新增 Tag endpoint，修復 GCP 路由。新增已知問題 3 則；Status 事故 3 起（已解決）。 |
| 2026-10-23 | **v2.1.309**：sandboxed Bash／`denyWrite` 修復，4 旗標。SDK 同步新增 message threads。互動更新 #74649／#65833／#23626。 |
| 2026-10-22 | **v2.1.308**：純可靠性修正。Vertex SDK 滿 1.0（⚠️ Breaking Change）；Python SDK v2.1.0 擴充 enforcement 參數；桌面文件增 Dispatch 說明；旗標增6消1。 |
| 2026-10-20 | **v2.1.304**：mod 系統新增 hook 跳過具名 transcript＋`tool.check` 的 `decider: "person"`。桌面文件新增 171 段（近期最大單日異動）。build 新增 11 個候選旗標。 |
| 2026-10-19 | **v2.1.303**：純臭蟲修復，無使用者端功能異動。互動更新 6 則：#84352（201 留言，今日最高）、#81698、#85199、#76694、#14200、#65632。 |
| 2026-10-17 | **v2.1.302**：新增 AUTO_MODE_MODEL＋閒置自動壓縮（未載）。桌面文件改寫任務接續規則。新增已知問題 1 則（#22264）。互動更新 2 則（#15942、#11002）。 |
| 2026-10-16 | **v2.1.301**：新增重試逾時旗標＋SDK speed／usage-tier；文件新增 6 頁 Code Review（轉 GA）；已知問題 4 則、互動更新 3 則。 |
| 2026-10-15 | **v2.1.300**：新增 `virtualText`、OTel 快取拆分欄位；旗標增4消1，見 [[topics/claude-code-experimental]]。互動更新2則；新增2則安全揭露指標，見母頁「近期報導」。 |
| 2026-10-14 | **v2.1.299**：新增 `DISABLE_FILE_MENTIONS`；旗標增 13 消 1，見 [[topics/claude-code-experimental]]。桌面文件擴充 122 段（SSH）。 |
| 2026-10-13 | 新增已知問題 1 則（#20571 VS Code 擴充套件 400 錯誤，133 則留言，今日全站最高）。互動數更新 2 則：#2254（151 讚、47 則留言）、#1669（51 則留言、86 讚）。 |
| 2026-10-12 | 桌面版文件新增 SSH host 組態設定。新增已知問題 1 則（#50674 ARM64）。互動數更新 4 則：#92984（今日全站最高）、#34556、#11315、#14131。 |
| 2026-10-09 | **v2.1.295**：hook `onFailure: "block"` 與官方安全建議有落差。旗標增 5 消 2，見 [[topics/claude-code-experimental]]。 |
| 2026-10-08 | **v2.1.294**：hook 自然語言封鎖指示修正。旗標增 1，見 [[topics/claude-code-experimental]]。新增已知問題 6 則，互動更新 1 則。 |
| 2026-10-06 | **v2.1.291**：兩項回歸修正（權限提示答案遺失、訊息遺失）；桌面文件重命名 Auto-fix/Auto-merge。新增已知問題 1 則（#16561）。 |
| 2026-10-04 | **v2.1.289**：deny/ask 規則與終端機凍結修正；桌面文件 Computer use 設定搬遷。新增已知問題 2 則，互動更新 1 則。 |
| 2026-10-03 | **v2.1.288**：`rm` 防護缺口修正、`--max-findings`、`claude purge`。旗標增 7，見 [[topics/claude-code-experimental]]。新增已知問題 1 則。 |
| 2026-10-01 | **v2.1.287**：Claude Mods 出貨（#91870 轉✅）。旗標增 7，見 [[topics/claude-code-experimental]]。新增已知問題 1 則，互動更新 1 則。 |
| 2026-09-30 | 桌面版文件補充 `/resume` 完整流程：終端機關閉 session 後可於桌面版接續同一對話（非複本）。 |
| 2026-09-29 | **v2.1.285**：新增 `DISABLE_WEB_FETCH`、`--desktop`；企業可限 API 供應商。旗標增9（1 已出貨）消7，見 [[topics/claude-code-experimental]]。 |
| 2026-09-28 | **v2.1.284**：Sonnet 5.5 成 API 預設模型，新增「Yes, but ask」。旗標增4消2，見 [[topics/claude-code-experimental]]。新增已知問題 2 則。 |
| 2026-09-27 | 新增已知問題 5 則：子代理無限遞迴標 CRITICAL（#68619）、CLI 格式破壞複製（#15199）、Plugins 缺 rules（#14200）、GitHub 無工具（#61682）、API 無回應（#69358）。 |
| 2026-09-26 | **v2.1.283**：新增閘道提示標頭 `x-claude-code-prompt-id`。新增已知問題 2 則：Cowork「選擇資料夾」消失（#76694）、Windows UNC 不支援（#45297）。 |
| 2026-09-25 | **v2.1.282**：新增 `maxProseWidth` 設定（截斷）。旗標增 8＋代號 2、`OCHRE_KITE` 消失。桌面文件：本機/SSH 自動載入帳號 skills/plugins。 |
| 2026-09-24 | **v2.1.281**：desktop policy 新設定；旗標增 9。新增 #60366（hi 誤判）併入 Usage Policy。互動更新：#63903、#8451、#12925。 |
| 2026-09-23 | **v2.1.280**：Opus 5.5 成新預設模型。AGENTS.md 補 telemetry 成因（#95690）。修正 v2.1.233 斷句誤導。互動數更新：#4953、#91188。 |
| 2026-09-20 | 新增已知問題 2 則：Cowork device_bash 失效（#92958）、Plugin4Shell 跨 agent RCE（僅標題可用）。GitSpawn 補記 v2.1.196 部分修補。 |
| 2026-09-19 | v2.1.278 免計費 classifier；v2.1.277 AGENTS.md 上線，#6235 轉✅。新增 #11315。旗標增3消1，見 [[topics/claude-code-experimental]]。互動4則。 |
| 2026-09-18 | **v2.1.276** 修復 400 錯誤迴歸。Projects 進 Beta，六媒體報導。旗標增減各 2，見 [[topics/claude-code-experimental]]。互動數更新 5 則。 |
| 2026-09-17 | **v2.1.274** 新增記憶體警示旗標。桌面文件新增帳號 skills/plugins 載入規則。TradingView MCP Server（第三方）。互動數更新、❓ 標記各 1 則，詳見各節。 |
| 2026-09-16 | **v2.1.273** 新增遙測標頭；sdk-python v1.6.0 擴充 Managed Agents 權限；桌面文件新增雲端 session 接手／推送分支；新增已知問題 #69044；11 則互動數更新，詳見各節。 |
| 2026-09-14 | 官方文件：桌面版新增多 repo 掛載＋`disableMobileSimulatorTools`。新增已知問題：Actions 範本 RCE（Reddit）。互動更新：#53247（29→32 讚）、#2254（138→147 讚）。 |
| 2026-09-13 | **v2.1.270**：修復 2.1.269 迴歸（git 指令誤要求授權）。互動數更新 7 則（AGENTS.md #6235、多帳號 #18435／#27302 等），詳見各節。 |
| 2026-09-12 | **v2.1.269**：新增 `claude plugin eval`；官方文件更新（桌面版 Git 需求）；新增已知問題 2 則；互動數更新 2 則。細節見已知問題頁與「最新版本」。 |
| 2026-09-11 | **v2.1.268**（gateway pricing）；SDK v1.5.0；新增已知問題 2 則；Status 事故 2 起；#2511 互動最高（635 讚）。細節見已知問題頁與「最新版本」。 |
| 2026-09-11（反向對照） | 自建 benchmark「Benzi」宣稱 SWE-bench Verified 78.2%、低於 10 美分/修復，勝過 Claude Code 與 CodeGraph；單一廠商榜單，未見第三方複測（[原文](https://benzi.fly.dev/benchmark)）|
| 2026-09-08 | 新增已知問題：`MEMORY.md` 門檻可設定（#91188）。互動更新：#26224（131 留言，今日最高）、#32479（96 留言）、#62503（40 留言）。iOS 新增用量按鈕；HN 拆解雲端 microVM 架構。 |
| 2026-09-06 | 查證懸置 6 筆結案，見已知問題頁與本表細節區。 |
| 2026-09-05 | 新增已知問題 3 則：Windows Desktop 孤兒 Silo（#53247）、Cursor 悄刪紀錄（#59248）、Function Hooks 提案（#91870，本輪互動最高）。互動更新：Session 消失（#26452）。 |
| 2026-09-04 |%% 補跑：09-04 排程抓料失敗，隔日現抓補齊 %%**v2.1.261** 發布，`/status` 與 `claude doctor` 新增「Organization policy」欄位，說明組織政策載入失敗原因（如代理伺服器未正確轉發 endpoint）。anthropic-sdk-python v1.4.0 新增 Claude Tag 分類與使用者用量分項 API 支援；anthropic-sdk-typescript vertex-sdk v0.19.7 為例行維護（chores），無使用者端功能異動。互動數更新 8 則：帳號多身份缺口三平台之一——Web connector 多帳號（#27302，227→240 則留言、480→523 讚）、Mobile 多帳號切換（#36151，164→170 則留言、879→944 讚，今日全站已知問題互動量最高）；CVP 核准組織仍遭資安防護誤擋（#84352，141→195 則留言）；付款訂閱 Max 5x 後帳號反遭停用（#5088，180→184 則留言）；幾乎每天須重新網頁驗證登入（#1757，79→83 則留言、69→70 讚）；內建 Slack MCP connector 多 workspace 功能請求（#44243，36→44 則留言、78→99 讚）；GitLab 整合功能請求（#12346，50→52 則留言、135→140 讚）；`/tmp/claude-*-cwd` 工作目錄暫存檔未清理（#8856，70→71 個 reactions）；Windows 11 Claude Desktop 主視窗持續蓋在最上層無設定可關（#85891，41→87 則留言、92→181 讚）；`/goal` stop-hook 模型行為模式回報（#60705，137→157 則留言）。Wired、Mashable 報導 Anthropic、OpenAI、xAI 三家模型服務同日上午發生罕見同步中斷，三方對外皆未說明確切成因。MacRumors 報導 Claude 據傳將支援 Apple CarPlay；另有 Anthropic 推出電商情境 Claude commerce agent 之報導，屬產品策略層動態，未見具體使用者端操作介面，暫不進 feature-radar。 |
| 2026-09-01 | **v2.1.252** 發布：修復 Bash 指令因「task output swap refused」在部分 Mac 上失敗，以及專案缺 `.claude/settings.local.json` 時「always allow」設定無法儲存的問題，純 bug 修復。新增已知問題 1 則：Cowork 對話封存後完全消失、找不回（#22931，39 則留言、38 個讚）。互動數更新 4 則：Visual Studio 2026 整合支援（#15942，514→531 讚）；Desktop 與 CLI 間同步 Skills（#20697，補上 43 則留言、159 讚）；MCP OAuth `resource` 參數尾端多加斜線導致 Entra ID 驗證失敗（#52871，補上 41 則留言、26→28 讚）；Opus 5 Auto Mode 提示注入事件由 embracethered／The Register 補上首個量化數字（實測 60–80% 攻擊成功率 vs 官方委託評測 0%），嚴重度升級。Anthropic Status 通報 08-31 兩起服務降級（claude.ai／Claude Code 16:55–19:16 UTC；claude.ai 另一起 17:52 UTC 解決），均同日修復。HackerNoon 報導 Claude 隱形浮水印上線 24 小時即被開發者繞過，該系列爭議見 [[topics/anthropic-government-policy]]、[[topics/anthropic-business]]。 |

### 2026-08 時段總結
- 08-01～08-05：v2.1.221 VS Code Focus view；v2.1.222 修補 worktree 隔離 session 可對主 checkout 下破壞性 git 指令；Claude API 新增 Inference Hooks（Enterprise beta）。
- 08-07～08-09：v2.1.224 新增 `claude self-hosted-runner`；跨 session 訊息互通（`ListAgents`＋`SendMessage`）經官方文件確認，#24798 轉 ✅。
- 08-10～08-14：官方宣布 08-14 起 auto 模式成為 Pro／Max／Team 新 session 預設、不再對分類器收費；v2.1.231 修 MCP OAuth 登入；v2.1.232 subagent forking 預設開啟。
- 08-17～08-22：v2.1.235 `spellcheck`；v2.1.237 修 gateway 下 prompt caching、新增 Concise 輸出風格；v2.1.238 `keybindingFlavor`；anthropic-sdk-python v1.0.0（⚠️ httpx2）；v2.1.239 成本估算計入資料常駐 1.1 倍。
- 08-23～08-27：Opus 5 簡單任務耗時異常，Claude Code 團隊回應是 effort 顯示方式調整；v2.1.245 修 glibc 2.44 當機；v2.1.247 新增 `SendFeedback` 工具。
- 08-29～08-30：v2.1.251 新增 PreModelSwitch／PostModelSwitch hook；SDK 的 files／skills 改 GA 介面；官方宣布 09-14 起週配額永久調高 25%、取消暫行 +50%。
- 本月 Anthropic Status 多起短暫事故均已解決；新增的已知問題與互動數見已知問題頁各組。
- 原始條目見 [[entities/claude-code-archive#2026-08]]

### 2026-07 時段總結
- 07-01：v2.1.197 Sonnet 5 成為預設模型（原生 1M context，促銷價後於 08-10 取消、$2/$10 永久化）；Enterprise Gateway 發布；Python SDK v0.115.0 支援 Managed Agents API（見 [[entities/managed-agents]]）。
- 07-08～07-09：Cowork 擴展到行動裝置與網頁版（Max 先行）；Reflect with Claude 測試版（Settings 使用模式儀表板）。
- 07-14～07-17：v2.1.210 工具摘要行即時計時；v2.1.212 ⚠️ `/fork` 改為複製對話至新背景 session，原同 session 子 agent 功能更名 `/subtask`，無過渡期。
- 07-20～07-23：v2.1.216 新增 `sandbox.filesystem.disabled`，並修補 Bash／Unicode 權限繞過；v2.1.217 表情符號 shortcode 自動完成（`emojiCompletionEnabled`）；Claude Security 終端機內掃描外掛 Beta（`/claude-security`）。
- 07-24～07-26：SDK 新增 stop reason `model_continue`；語音模式開放 Opus／Sonnet 選擇；官方證實 Claude 5 世代已移除逾 80% 的 Claude Code 系統提示詞。
- 07-25～07-31：v2.1.220 純可靠性版；Opus／Haiku／Fable 系列數起 Status 錯誤率事件均已解決；已知問題互動數持續更新（#826、#27302、#3412、#24798 等，現況見各已知問題節）。
- 原始條目見 [[entities/claude-code-archive#2026-07]]

### 2026-06 時段總結
- 06-21～06-22：v2.1.185 stream-stall 提示改為 20 秒觸發；官方部落格發布「七種控制層」框架；v2.1.186 新增 `claude mcp login/logout`、`--no-browser`。
- 06-22（續）：Extended Thinking 透明度問題社群揭露（HN 312 分，thinking blocks 加密簽章影響企業審計，詳見已知問題頁）。
- 06-24～06-25：v2.1.187 新增 `sandbox.credentials`（阻擋沙盒讀取憑證）與組織層級模型限制；v2.1.191 新增 `/rewind` 指令、修正 streaming 捲軸問題，SDK 同步支援 `client.system.message`。
- 06-29～06-30：v2.1.196 新增 org default model（見 [[topics/official-community-gap]]）；v2.1.197 初報 Sonnet 5（`/model` 選單先行出現，07-01 正式切換）。
- 06-29～06-30（續）：Explore subagent 固定用 Haiku 遭社群發現；Session 30 天自動刪除官方拒絕修復（issue #62476）；36Kr 報導背景任務升級傳聞，未經官方證實。
- 原始條目見 [[entities/claude-code-archive#2026-06]]

### 2026-05 時段總結
- 05-02～05-03：AGENTS.md 跨工具互操作缺口浮現（issue #6235，詳見已知問題頁）；GameMaker 正式啟用整合；macOS computer use 上線；社群工具 Governor、Caliber、Omar、graphify 等發布。
- 05-04～05-06：原始碼外洩 DMCA 風波擴大（詳見已知問題頁）；Cowork/Desktop 悄悄支援第三方 LLM；Claude Connectors 擴及創意軟體；Windows VS Code extension 全面故障（詳見「版本更新」）；Claude Security 進入公開 Beta（見 [[entities/claude-security]]）。
- 05-07～05-09：Managed Agents 重大更新（Dreaming、20 路子代理並行，見 [[entities/managed-agents]]）；SpaceX 算力合作提升速率上限（見 [[entities/pricing]]）；Windows IDE 擴充套件二度全面故障（詳見已知問題頁）。
- 05-10～05-12：Sandboxing 正式文件發布、CVE-2026-39861 沙箱逃逸公開並於 v2.1.64 修補（詳見已知問題頁）；CLAUDE.md candidate-context 架構遭社群發現（詳見「已知問題」）；Managed Agents 從研究預覽正式 GA。
- 05-13～05-17：Boris Cherny 揭露每晚子代理深度工作流；AI 生成應用安全掃描 90% 存在漏洞；多帳號架構合規邊界明確（見 [[entities/pricing]]）；Anthropic API 跨模型 500 錯誤中斷；「Claude Code at Scale」系列首篇（HN 203 分）。
- 05-19～05-22：Anthropic 收購 Stainless；沙箱第二個獨立繞過漏洞揭露（見 [[topics/ai-agent-safety]]）；`/simplify` 更名 `/code-review`；v2.1.148 緊急修復 Bash exit code 127（詳見「最新版本」）。
- 05-27～05-28：**Coordinator 模式**加入（多 worker 協調層）；Uber COO 確認生產力提升 25%；富士通策略合作；Cisco LLM Security Leaderboard 前十佔 8 席。
- 原始條目見 [[entities/claude-code-archive#2026-05]]

### 2026-04 時段總結
- 04-24～04-25：Anthropic 正式承認效能退步源於工程疏失（詳見已知問題頁）；Stop hooks 失效回報；CC-Canary 工具興起偵測效能漂移。
- 04-26～04-27：HERMES.md 計費 bug 曝光擴大媒體關注（詳見已知問題頁）；版本疑似靜默撤版；API 金鑰外洩經媒體報導（詳見「已知問題」）；Anthropic 測試 Bugcrawl（見 [[entities/bugcrawl]]）。
- 04-26～04-27（續）：Claude Research 架構部落格；pentest-ai-agents 釋出；社群工具 Claude Squad／mux0／agent-order。
- 04-28：v2.1.121（MCP `alwaysLoad`、`claude plugin prune`）；Runhouse 團隊股權收購；Managed Agents 加入跨會話記憶正式公告；Auto Compact 失效事件回報（詳見已知問題頁）。
- 04-29：官方發布 Champion Kit 企業推廣素材；社群工具 Cockpit／Harness／CodeThis／Claude Exporter 發布。
- 04-30：Claude Security 公開測試版推出（見 [[entities/claude-security]]）；GameMaker 整合公告；v2.1.124 系統提示更新；TypeScript SDK v0.92.0；Anthropic 定位「agentic AI 的 AWS」（Managed Agents + Persistent Memory 公測）。
- 2026-04（月）：Google 被指秘密開發競品。
- ~2026-03：效能退步開始，社群陸續察覺。
- 原始條目見 [[entities/claude-code-archive#2026-04]]


文中「已知問題頁」指 [[entities/claude-code-known-issues]]。

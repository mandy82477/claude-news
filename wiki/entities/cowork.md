---
page: "entities/cowork"
kind: "entity"
type: "product"
status: "active（09-17 起與 Claude 聊天介面合併為單一 Claude，介面選擇不再需要；先於 Pro／Max 開放，數週內擴及更多方案）"
domain: "🛠️ 工具/功能"
last_updated: "2026-10-23"
last_news_update: "2026-10-23"
status_main: "active"
matrix_role: "產品"
days_since_news: 2
parent: null
children: "['entities/cowork-archive']"
page_role: "hub"
days_since_news_subtree: 2
inbound_links: 14
attribution_count: 6
attribution_last: "2026-10-23"
top_source: "github"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Cowork

**類型：** product
**狀態：** active（09-17 起與 Claude 聊天介面合併為單一 Claude，介面選擇不再需要；先於 Pro／Max 開放，數週內擴及更多方案）
**領域：** 🛠️ 工具/功能
**對照角色：** 產品（已併入 Claude app）
**首次出現：** 2026-05（本庫日報最早提及 2026-05-03；官方正式推出日期未見報導）
**最後更新：** 2026-10-23
**最後新聞更新：** 2026-10-23
**蒐集邊界：** 官方一手來源（Help Center release notes、Anthropic Blog、Claude API Release Notes、Anthropic Status）＋日報路由到的社群回報（GitHub Issues／HN／Reddit）為主；Windows 平台不穩定事件叢集的完整清單住 [[entities/claude-code]]「已知問題」，本頁不重複列出；企業採用與商業合作案例住 [[topics/anthropic-business]]，本頁只留指路，不逐筆收錄。

> **最新動態**（2026-10-23）
> 官方查證：Chrome 側邊欄仍是 beta；Pro／Max 新任務自 10-06 起一律雲端執行，Team 為 web／mobile beta。

---

## 現況

**10-06 官方工程師說明架構轉雲端原因：** Simon Willison 部落格轉引 Anthropic 工程師 Felix Rieseberg：舊版 Cowork 推論雖在雲端，工具呼叫卻在使用者電腦上的 Anthropic VM 執行（考量能力與安全隔離），但犧牲硬碟、電池與效能，闔上筆電即中斷；新版推論與 VM 皆移至雲端，每個 session 各自獨立沙箱。r/ClaudeAI 使用者追問本機殘留 VM 是否會被自動移除以拿回硬碟空間，官方文件尚未表態。

**09-25 官方文件再度確認擴張範圍：** Help Center release notes 新增段落，稱「Claude Cowork comes to every conversation」，可在任何對話直接要求設計、簡報或文件，**含 Claude Code 與 Artifact 介面**；合併後的背景執行與沙箱見下方 2026-10-17 查證段。

**官方說明中心確認合併後的背景執行與沙箱（2026-10-17 查證）：** [〈Use Claude Cowork on web, desktop, and mobile〉](https://support.claude.com/en/articles/15520349)寫明「Claude Cowork is now just Claude」，在任何對話描述任務即可交給 Claude；雲端 session 在背景持續執行（「Close your laptop and Claude keeps going」），Pro、Max 於雲端執行，Team、Enterprise 的雲端 Cowork 為 beta。沙箱：[〈Claude Cowork architecture overview〉](https://support.claude.com/en/articles/14479288)載明雲端 session 各有獨立沙箱（session 開始時建立、結束時銷毀；未稱其為 Linux VM），本機 session 的指令與程式碼則在專屬 Linux VM 內執行。雲端 session 只能經桌面版 App 觸及本機檔案，App 離線即無法。[release notes](https://support.claude.com/en/articles/12138966-release-notes)（2026-09-16）另載聊天、Cowork 任務、專案、連接器、技能都會沿用，逐步開放給 Pro、Max。

Anthropic 的圖形化協作介面讓使用者指派任務給 Claude 在獨立 VM（沙箱）中背景執行，闔上裝置或關閉筆電後任務仍在雲端持續進行；桌面版已正式發布，行動版與網頁版自 2026-07-07 起以 Preview 形式開放（首波僅 Max）；2026-10-23 官方查證：Pro、Max 在每個介面都於雲端執行，10-06 起新任務一律雲端、介面已拿掉「Only on your computer」，Team 的 web／mobile 為 beta，Enterprise 需管理員開（[說明中心](https://support.claude.com/en/articles/15520349)；詳見 [[feature-radar]]「Claude Cowork 行動版 / 網頁版擴展」）。Windows 是這條產品線目前最不穩定的平台——本庫累積至少五起獨立的 VM／服務啟動失敗事件與多起資料完整性問題，完整清單見 [[entities/claude-code#已知問題]]，本頁不重複列出；一句結論：**Windows 上跑 Cowork，先假設它會出狀況，重要工作別只信任它的自動保存。**

**跟 Claude Code 差在哪（合併前狀態，合併後見上方查證段）：** Claude Code 是終端機 CLI，面向工程師逐指令互動；Cowork 是圖形化桌面／行動／網頁介面，任務丟出去後可背景執行，不需要盯著終端機。兩者共用底層 Claude agent 能力（如 2026-05-03 macOS 電腦使用功能，Claude Code 與 Cowork 同步取得直接控制桌面滑鼠鍵盤的能力）。2026-05-11 一則 Reddit 貼文（單一使用者觀點，非官方聲明）指出，桌面版 Claude Code 推出後與 Cowork 功能高度重疊，使用者一度分不清楚兩者定位；此後未見官方公開發文說明差異。

**現在能不能用：**

| 介面 | 狀態 | 取用門檻 |
|---|---|---|
| 桌面版 | 正式發布 | Pro 方案以上（Free 不含，claude.com/pricing 官方查證） |
| Chrome 側邊欄 | beta（2026-10-23 官方查證） | 2026-08-12 起 Max／Team 先開、Pro 數週內開放；不支援其他 Chromium 瀏覽器與行動版側邊欄 |
| 行動版（iPhone／iPad／Android） | 正式發布（Help Center 確認） | 隨帳號方案而定，官方未再細分獨立門檻 |
| 網頁版／雲端持續執行 | Pro／Max 已上線；Team beta；Enterprise beta | Pro／Max 每個介面都在雲端跑；Team 為 web／mobile beta；Enterprise 需管理員開（2026-10-23 官方查證） |

**現在會咬到你的是什麼：** 除了 Windows 平台不穩定叢集（見上方連結），近期還有三類值得留意——① **資料完整性**：Cowork 的 Edit/Write 工具因緩衝區容量上限會靜默截斷檔案（#53940，Windows 上的 Cowork 使用者），寫入後務必自行核對檔案長度；② **連結狀態失真**：Google Drive connector 顯示已連結，Cowork 中卻叫不到對應工具（#30457，2026-09-10）；③ **接入層限制**：Claude Desktop／Cowork 目前不支援 AWS Bedrock 作為替代後端，僅 Claude Code CLI 有此環境變數（#32668，功能請求，官方尚未排入路線圖）。

## 核心功能

- **背景持續執行**：任務指派後在雲端／VM 中執行，闔上裝置不中斷（2026-07-07 起擴及行動裝置與網頁版）。
- **跨介面共用記憶**（2026-08-25）：Cowork 與網頁／App 對話共用記憶，記住項目集中列在設定 > Memory 的 Topics 可個別編輯或刪除；健康、信仰等敏感主題預設不納入，須手動開啟才記錄。
- **Chrome 側邊欄執行**（官方 2026-08-12 部落格）：可在瀏覽器側邊欄直接操作 Cowork，不需切到桌面應用程式。
- **內建瀏覽器**：多家媒體轉述交叉確認，尚未取得官方原文。
- **第三方 LLM 接入**（2026-05-04，社群自行發現、官方未曾公告）：Cowork／Desktop 可接任意第三方模型，含 OpenAI、Gemini、本地模型與企業閘道（Bedrock／Vertex／Foundry）。

## 相關議題

- 同日推出的文件／簡報產品：[[entities/claude-docs]]、[[entities/claude-slides]]、[[entities/claude-design]]
- Windows 平台不穩定事件全清單、狀態標記與繞法：[[entities/claude-code#現在還沒修好的]]、[[entities/claude-code#已知問題]]
- 桌面版終端機 session 同日改讀帳號 skills/plugins（同屬帳號統一方向）：[[entities/claude-code]]
- 訂閱方案與計費規則：[[entities/pricing]]
- 官方 agent 積木總覽中 Cowork 的定位：[[topics/anthropic-agent-stack]]
- 企業採用案例（如 Amadeus、Varonis、Syracuse University）：[[topics/anthropic-business]]
- 競品對標動態（Cursor「Sand」等；Axios／Fortune 將本次合併框為對 Microsoft 的競爭壓力／「superapp」布局，細節見商業視角頁面）：[[topics/competitor-landscape]]
- 社群開源平替（Agenta）：[[topics/community-tech-patterns]]

## 參考來源

- [Quoting Felix Rieseberg](https://simonwillison.net/2026/Oct/5/felix-rieseberg/)（Blog／Simon Willison，2026-10-05，轉引 Anthropic 工程師說明架構轉雲端原因）
- [r/ClaudeAI：本機 Cowork VM 何時移除](https://www.reddit.com/r/ClaudeAI/comments/1wz56ih/will_claude_desktop_eventually_remove_the_local/)（2026-10-06，0 留言）
- [Claude Help Center release notes](https://support.claude.com/en/articles/12138966-release-notes)（官方文件變更偵測，2026-09-25 查，非新聞報導）
- [官方部落格：Claude Cowork and chat are now one Claude](https://claude.com/blog/cowork-is-now-claude)（2026-09-17；HN Repo Bridge 收錄，HN 討論 226 分；Simon Willison 部落格轉引）
- Google News／Reuters、TechCrunch、Axios、Fortune、VentureBeat、Computerworld（2026-09-17，同事件媒體報導，僅標題／框架可用）
- Help Center release notes（2026-08-25，跨介面記憶）
- Anthropic Blog（2026-08-12，Chrome 側邊欄）
- claude.com/pricing（2026-08-12 官方查證，方案功能組成）
- The Verge、TechCrunch、WIRED、NBC News、The New Stack、Let's Data Science（2026-07-07～07-08，行動版/網頁版擴展）
- GitHub Issues：#53940、#30457、#32668、#92958、#92984（Windows 相關全清單見 [[entities/claude-code]]）

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-10-23 | 官方查證：Chrome 側邊欄仍 beta；Pro／Max 各介面皆雲端、10-06 起新任務一律雲端；Team beta、Enterprise 需管理員開（[來源](https://support.claude.com/en/articles/15520349)） |
| 2026-10-06 | Simon Willison 部落格轉引 Anthropic 工程師 Felix Rieseberg 說明架構轉雲端原因（省硬碟電池、闔筆電不中斷）；r/ClaudeAI 使用者追問本機殘留 VM 何時釋放硬碟空間，官方未答 |
| 2026-09-25 | Help Center release notes 新增段落確認 Cowork 進駐每個對話，可在任何對話（含 Claude Code、Artifact 介面）直接要求設計、簡報或文件 |
| 2026-09-17 | Cowork 與 Chat 合併為單一 Claude，同步推出 Claude Docs、Slides（beta）；HN 226 分，六家媒體同日跟進（僅標題可用） |
| 2026-09-12 | Windows 九月累積更新致 device_bash 於 ARM64／x64 皆失效（#92958），與 09-08 更新致 Plan9 掛載失敗（#92984）同源；官方尚未修復 |
| 2026-09-10 | Plan9 共用資料夾因 KB5124008 全數掛載失敗（#92984，官方已識別成因，移除該 KB 可恢復）；Google Drive connector 顯示已連結卻叫不到工具（#30457） |
| 2026-08-25 | Cowork 與網頁／App 共用記憶功能整合，跨介面記住的項目集中在設定 > Memory 管理；同日功能請求：Desktop／Cowork 支援 AWS Bedrock 替代後端（#32668） |
| 2026-08-12 | 官方部落格確認 Cowork 可於 Chrome 側邊欄執行，Max／Team 即日、Pro 數週內開放，不支援其他 Chromium 瀏覽器與行動版 |
| 2026-08-05 | Inference Hooks 進入 Enterprise 組織 beta，可將 claude.ai、Cowork、Claude Code 上受管治 prompt 導向企業自有 AI 安全伺服器 |
| 2026-07-07 | Cowork 正式擴展至行動裝置與網頁版，首波開放 Max 訂閱用戶，任務可雲端持續執行，涵蓋政府機構客戶 |

### 2026-05 時段總結
- 05-03：macOS 電腦使用（computer use）功能上線，Cowork 可直接控制桌面滑鼠與鍵盤。
- 05-04：Cowork／Desktop 悄悄加入支援任意第三方 LLM（OpenAI、Gemini、本地模型、企業閘道），無官方公告，社群自行發現。
- 05-11：社群回報 Claude Code Desktop 與 Cowork 定位混淆、功能高度重疊，官方未公開釐清差異（單一 Reddit 貼文）。
- 原始條目見 [[entities/cowork-archive#2026-05]]

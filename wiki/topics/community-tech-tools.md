---
page: "topics/community-tech-tools"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-03"
last_news_update: "2026-10-02"
update_freq: "🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）"
status_main: "ongoing"
days_since_news: 2
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 2
inbound_links: 50
attribution_count: 15
attribution_last: "2026-09-26"
top_source: "github"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群工具目錄

**狀態：** ongoing
**領域：** 🌐 社群
**更新頻率：** 🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）
**開始日期：** 2026-04-25
**最後更新：** 2026-10-03
**最後新聞更新：** 2026-10-02

> **目錄新增 31 個工具、拿掉 13 個長期沒動靜的舊工具**（2026-10-03）
> 新增涵蓋 09-25～10-02 的 Show HN 與 GitHub 新品，含檢查 agent 有沒有守 CLAUDE.md 的 RuleReceipt、五個新記憶工具；拿掉的 13 個都不是任何症狀的首選或次選。決策表首選未變動。

---

## 摘要

**我卡住了，社群有什麼能救？** 本頁把社群工具依「症狀」排列：每個症狀給一個先裝的、一條「什麼時候該改裝別的」的分界，以及這個判斷是哪天下的、最近一次確認這個專案還在不在是哪天。有一個症狀我們認為答案是機制不是工具，那一格就誠實空著。
按開發流程階段找官方做法見 [[topics/coding-workflow-guide]]；做法背後的機制與實測見 [[topics/community-tech-patterns]]；概念辯論見 [[topics/community-tech-discussions]]；同一個痛點官方補了沒見 [[topics/official-community-gap]]；官方功能見 [[feature-radar]]。各類工具現在誰大、本週誰在漲的 GitHub 規模榜見 [[topics/skill-interest-watch]]；該裝哪個只有這一頁有答案。

---

## 我卡在這裡

> 每一列最後一次確認是哪天，寫在「證據」欄的**查**；工具出資安事故、棄坑、下架這種急事，會寫進該列的證據欄與下面的推薦細節；全站層級的安全事件另見 [[topics/ai-agent-safety]]。

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 帳單爆了，看不到錢花在哪 | ⌨️ [**tare**](https://github.com/kelviq/tare) | 要桌面常駐、不想開終端 → 🖥️ [TokenEater](https://github.com/AThevon/TokenEater)（僅 macOS）；想比較多個 coding agent 的花費 → 🖥️ [Frugal Tokens](https://github.com/dpclark4/frugal-tokens) | 🟡（判 08-27｜查 09-22，287★） |
| 額度快用完，想在斷線前被提醒 | ⌨️ [**Claude-Code-Usage-Monitor**](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 要跨平台、作者還在更新 → ⌨️ [claude-usage-widget](https://github.com/bozdemir/claude-usage-widget)（53★）；用 Windows、想自己設到幾 % 就叫你 → 🖥️ [usage-monitor-for-claude](https://github.com/jens-duttke/usage-monitor-for-claude) | ⚪（判 09-22｜查 09-22，8,713★、07-05 後未更新） |
| context 一直被工具輸出撐爆 | 🔌 [**pxpipe**](https://github.com/teamchong/pxpipe) | 不能接受請求過代理層 → 🧩 [Graft](https://github.com/trailhq/Graft)（數字有爭議，見細節）；還不確定是誰在撐爆 → 先跑 ⌨️ [PrismoDev](https://github.com/shanirsh/prismodev) 診斷 | 🟡（判 08-05｜查 09-22，7,426★） |
| 接手沒碰過的大 repo，agent 讀不懂 | 🧩 [**graphify**](https://github.com/Graphify-Labs/graphify) | 要讓**人**看懂而非 agent → [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)；要把架構畫成圖交付 → [archify](https://github.com/tt-a1i/archify)；改 code 要索引自動同步 → [codegraph](https://github.com/colbymchenry/codegraph) | 🟢（判 05-02 起多來源｜查 09-22，12.0 萬★） |
| 每開新 session 都要重講一遍 | ⌨️ [**brain.md**](https://github.com/mindmuxai/brain.md) | 要團隊共享而非單機 → 🖥️ [OzBrain](https://ozbrain.com)（付費服務）；已在用 Obsidian → VIR | 🟡（判 08-25｜查 09-22，552★） |
| 多個 agent 在同一 repo 互相覆蓋 | 🖥️ [**ness**](https://github.com/ness-dev/ness)（原名 Harness） | 已經用 worktree 隔離、只差 commit 落地不打架 → 🧩 [Claude Code Merge Queue](https://github.com/funador/claude-code-merge-queue)；要跨 harness 統一協作邏輯 → [omnigent](https://github.com/omnigent-ai/omnigent) | 🟢（判 04-29 起多來源｜查 09-22，99★） |
| 一堆 agent 在跑，看不到誰卡住 | ⌨️ [**Omar**](https://github.com/omar-os/omar) | 只跑 3–5 個、不想多花一毛 token → [HUD](https://github.com/adrida/hud-mode)（走官方 event stream）；要 GUI 主控台 → 🖥️ [episko](https://github.com/respeak-io/episko)（原名 Cockpit） | 🟡（判 05-02｜查 09-22，48★） |
| 它說做完了，但根本沒做 | 🧩 [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 要留可稽核證據給團隊審 → [Proof Loop](https://github.com/LeoStehlik/proof-loop)（建構者／驗證者分離） | 🟡（判 04-27｜查 09-22，7★） |
| CLAUDE.md 寫了它不聽 | —（答案是機制不是工具，見細節） | 規則多到耗 token → Writ；跨工具設定碎片化 → Caliber | —（這一列沒有工具可評，理由見細節） |
| 不想被單一供應商綁死 | 🔌 [**Workweave Router**](https://github.com/weave-os/router) | 只想改用本地模型、不動主配置 → claudely；想繞過計量計費 → clarp（⚠️ 政策風險，見細節） | 🟡（判 06-27｜查 09-22，4,735★） |

**圖例**——證據：🟢 多來源實測／🟡 單一實測（多為作者自測）／⚪ 僅星數。括號裡兩個日期：**判**＝下這個判斷的那天，**查**＝最近一次確認這個專案還在不在、多大的那天；判很舊而查很新，代表結論是舊的但專案還活著，要拿它做決定前自己再看一眼 repo。安裝：🧩 skill/plugin（一行安裝隨時可拔）／⌨️ CLI／🖥️ 桌面 app（注意平台鎖定）／🔌 proxy·MCP（**流量過第三方層，裝前先評估安全**）。

**推薦細節**

- **pxpipe vs Graft 的數字強度不同**（08-30 彙整）：pxpipe 有作者實測（25,000 text token 壓至 2,700 image token、帳單降 59–70%，08-05；星數防刷已查證 forks 8.5%）；Graft 宣稱降 42%（08-15）但 HN 討論質疑 benchmark 段落疑似 AI 代寫、未經第三方覆核。接受走代理層就選 pxpipe（證據較強）；只想掛個 hook 隨時可拔、且不介意數字未覆核，才選 Graft。
- **「CLAUDE.md 不聽」沒有工具首選是結論不是留白**：dev.to 一手實作（08-25）顯示改用 hooks 強制執行後規則遵循率達 100%——答案是機制不是工具；哪些規則該搬去 hook、hook 要回 exit 2 才擋得住，見 [[topics/community-pattern-trends]] 趨勢一。
- **「CLAUDE.md 不聽」哪些是工具能解的**：四個失效機理中只有後三者是工具能解的：規則被機率性忽略且無反饋、規則越多越貴（Writ 以語意檢索只注入相關規則）、規則腐化（Patina 偵測）、跨工具碎片化（Caliber 統一管理）。
- **接手大 repo 的分界**（09-03 補寫）：graphify 給 **agent** 用（本機 AST、免向量 DB，`/graphify` skill）；同組另三個解的是不同工種——Understand-Anything 給**人**探索、archify 給人**交付圖**、codegraph 是 graphify 的競品（自動同步索引，僅星數證據）。官方面的「接手大 repo 第一步」（先讀 CI、從子目錄啟動、LSP）在 [[topics/coding-workflow-guide]] 第 2a 段：官方設定先做，索引工具再裝。
- **三個首選換了門牌**（09-22 查證）：Harness → [ness](https://github.com/ness-dev/ness)、Omar → [omar-os/omar](https://github.com/omar-os/omar)（官網也從 omar.tech 改成 omar.rs）、Cockpit → [episko](https://github.com/respeak-io/episko)。舊網址目前還會自動轉，但作者一關轉址就失效。
- **多 agent 互踩的首選為什麼不換**：ness 09-22 查得 99★／13 forks，自述已從 CLI 變成「給 agent 用的 IDE」（徽章隨之從 ⌨️ 改為 🖥️），但 README 仍寫可同時跑十個 Claude，仍解同一個症狀，故不換首選。
- **這一列的兩個次選**：omnigent 09-22 查得 10,150★／1,609 forks（15.9%，防刷結論不變），但仍沒有任何第三方實測回報，只有規模；另有一個同名的 `revfactory/harness`（9,051★）是設計 agent team 的 meta-skill，不是首選那個。
- **監看首選的分界**：HUD 經官方 JSON event stream 運作、不額外耗 token（08-07），適合小規模；Omar 的「管到 100 個 agent」是 05-02 當時的宣稱，現版自述已改成形式化編排、09-22 查得 48★——兩個選項都很小，裝前自己看一眼活躍度。
- **額度告警：官方只能被動查**。`/usage` 看得到用量條、狀態列讀得到百分比，但不會主動叫你；官方 CLI 主動告警的需求（issue #13585，👍 124）到 09-22 仍未處理，另一條同類需求 #65292 已被官方標為不做。官方到 09-22 沒有這個功能，[[feature-radar]] 上也還沒有對應條目；有了會記在那裡。
- **額度告警的三個候選都只有星數**：Claude-Code-Usage-Monitor 8,713★ 但 2026-07-05 後未更新（表上已標）；usage-monitor-for-claude 293★、09-13 仍在更新但只有 Windows；claude-usage-widget 53★、09-21 仍在更新、跨平台，規模最小但最新。三者都未見第三方實測。
- **Usage Updates 不是告警工具**（Show HN，10-01）：它是社群維護的 Claude／Codex 額度重置與限制變更時間軸，只能拿來對照自己帳號的重置週期是否正常，額度這一列首選不變。
- **額度告警這一列的其他選項**：CCLimitPing（45★、09-14 仍在更新）解的是「額度一解封就自動接著跑」不是提醒，要它去下面目錄拿連結；目錄裡還有一個 2026-05-18 收錄的 agent-baton，宣稱在觸及上限前主動告警並轉移工作，但只有 Reddit 貼文、09-22 查不到可裝的頁，所以沒放進上面三格。
- **Groundtruth 只有 7★ 為什麼還是首選**：值錢的是它的做法（Stop hook 逼 agent 先出示可驗證證明才准說做完），不是使用人數；09-22 查得 7★／0 forks、07-20 後未更新，次選 Proof Loop 11★。沒有更強的替代出現前不換。
- **clarp 的政策風險**（05-21 收錄）：以本地 PTY＋唯讀 API 代理規避 6/15 起的計量計費，屬計費規避而非最佳化；企業環境安裝前先確認與 Anthropic 合約條款的相容性。
- **本週新出的記憶類工具都只有規模或單一討論**（09-25～10-01）：agent-memory 1,486★（純 Markdown）、deja-vu 1,113★（直接搜 session 歷史）、hippo-memory 769★、Jevmem（HN 留言質疑過期記錄不刪）、Breadcrumb（Show HN）；皆無第三方使用回報，首選不變。
- **RuleReceipt 是「檢查」不是「強制」**（Show HN，09-30）：檢查 agent 有沒有守 CLAUDE.md／AGENTS.md，討論串有人質疑 agent 能反過來關掉檢查 hook；只有單一討論串、無使用回報，「CLAUDE.md 不聽」仍維持答案是機制（hooks）而非工具。
- **記憶類的分界**：brain.md 零依賴、純檔案（08-25，552★）；OzBrain 走團隊共享知識庫，是付費服務（免費 50 篇，Pro 每月 20 美元、Max 99 美元，09-22 查證）；VIR 直接萃取 session 檔進 Obsidian vault（05-23）。單機選檔案式，跨人選共享式。
- **有三個次選只有社群貼文、沒有可裝的頁**：Writ、Caliber、claudely 到 09-22 都找不到公開 repo 或產品頁，列在這裡是因為讀者提過這些需求，不是因為我們確認過它們還在。

### AI 寫久了人會不會退化（只有現象，還沒有能推薦的工具）

- 2026-04～05 被反覆提起的四個現象：**技能退化**（不再獨立解題，調試能力萎縮）、**命名漂移**（同概念出現四個名字）、**架構邊界侵蝕**（為讓測試通過直接跨邊界）、**無法獨立 debug**（程式在跑但沒有心智模型）。
- 當時被點名的幾個嘗試（`recap`、`modularity plugin`、`Mneme`）都沒累積出實測，所以上面的決策表沒有這一列。
- 官方公開方向（加速使用、更長自主 agent）與這些擔憂反向，短期不會主動回應；官方與社群的完整對照見 [[topics/official-community-gap]]。

---

## 🧩 Skills 速查（依 coding 用途分類）

社群 Agent Skills 的用途索引（**官方** skill 另有兩條軸：按工程流程階段與按產出物格式選用，見 [[topics/coding-workflow-guide]]）。安裝多為一行（`/plugin` 或 `npx skills add`），隨時可拔。

**Codebase 理解／索引**——知識傳承的三個工種：讓 **agent** 記住 repo、讓**人**看懂 repo、把架構**講給人聽**（建程式庫的一次性設定首選在「給 agent」列）

| Skill | 證據 | 一句話 |
|---|---|---|
| [**graphify**](https://github.com/Graphify-Labs/graphify) | 🟢（判 05-02 起多來源，當時 40k★＋作者宣稱 71×；查 09-22，12.0 萬★、`/graphify` skill、本機 AST 免向量 DB） | 【給 agent·索引】把 codebase（含文件、SQL schema）建成知識圖譜供跨 harness 查詢 |
| [**codegraph**](https://github.com/colbymchenry/codegraph) | ⚪（判 09-02 讀者提問查證；查 09-22，71,801★、forks 4,612、仍在更新） | 【給 agent·索引】預索引 code 知識圖、**改 code 自動同步**、全本機——與 graphify 直接競品，auto-sync 主張更進一步，社群實測待累積 |
| [**Understand-Anything**](https://github.com/Egonex-AI/Understand-Anything) | ⚪（判 09-02 讀者提問查證；查 09-22，83,707★、forks 7,057） | 【給人·探索式理解】把任意 code 變成可探索、可搜尋、可提問的互動知識圖——新人接手看懂 codebase 的那一格 |
| [**archify**](https://github.com/tt-a1i/archify) | ⚪（判 09-02 讀者提問查證；查 09-22，69,632★、forks 4,670、20 天內漲六成） | 【給人·交付級圖表】架構／時序／資料流／生命週期圖，自包含 HTML 可匯出——把架構講給別人聽、寫進文件；🧩 `npx skills add tt-a1i/archify -g` |

**寫碼紀律／方法論**——改變 Claude 寫 code 的行為

| Skill | 證據 | 一句話 |
|---|---|---|
| [**obra/superpowers**](https://github.com/obra/superpowers) | ⚪（08-28，27.9 萬星，Reddit 有實際採用跡象） | Agentic skills 框架＋軟體開發方法論 |
| [**andrej-karpathy-skills**](https://github.com/multica-ai/andrej-karpathy-skills) | ⚪（08-29，星數增速異常，可信度低） | 單檔改善 LLM coding 常見缺陷，取材 Karpathy 觀察 |
| [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 🟡（04-27） | Stop Hook 強制出示可驗證證明才准宣告完成 |
| [**I-have-ADHD**](https://github.com/ayghri/i-have-adhd) | 🟢（09-08，HN 499） | 鎖定「Claudism」冗語，阻止 agent 完成任務後反覆交代哪些沒做 |

**產出與呈現**——生成特定產物或改變輸出形式

| Skill | 證據 | 一句話 |
|---|---|---|
| [**baoyu-design**](https://github.com/JimLiu/baoyu-design) | ⚪（08-29，3,637 星） | 本機執行 Claude Design 產自足式 HTML UI 原型 |
| [**/show-me**](https://www.humanlayer.com/blog/show-me-skill) | 🟡（08-13，雙來源） | 精簡視覺化取代大量文字輸出 |
| [**video-recap-skills**](https://github.com/zenstory-ai/video-recap-skills) | ⚪（09-08，500★） | 把任意影片剪成中文口述影評，支援剪映匯出 |
| [**effective-html**](https://github.com/plannotator/effective-html) | ⚪（09-07，3,023★） | 產出可用 HTML artifact、線框稿、互動原型、計畫與圖表 |

**領域資料**——接特定資料域（coding 周邊，非核心寫碼流程）

| Skill | 證據 | 一句話 |
|---|---|---|
| [**Geosql**](https://github.com/dekart-xyz/geosql) | 🟢（07-08，機制已查證，見下方細節） | 地理空間資料（PostGIS／BigQuery／Snowflake）；4 倍提升僅在連 Dekart 時成立（見下方細節） |
| [**Shortcuts Playground**](https://www.macstories.net/stories/introducing-shortcuts-playground/) | 🟡（05-23） | 自然語言生成 Apple Shortcuts |
| [**l3a0/claude-plugins**](https://github.com/l3a0/claude-plugins) | 🟡（08-24，HN 45） | OCR 復原 Kindle 被限制匯出的畫線筆記 |
| [**travel-hacking-toolkit**](https://github.com/borski/travel-hacking-toolkit) | ⚪（09-09，657★） | 旅遊比價 Skill 與 MCP server，跨 Claude／Codex／OpenCode |

> Sx 2.0（skill 分享工具）與 awesome-llm-apps（百餘款應用的清單）都不對應上面任何一個用途，兩者在下方工具目錄裡；只想看哪一類現在最大，見 [[topics/skill-interest-watch]]。

---

## 指標說明

| 指標 | 說明 |
|------|------|
| **證據**（上方兩表） | 🟢 多來源實測 / 🟡 單一實測 / ⚪ 僅星數（未經行為佐證）；決策表括號內「判」是下判斷那天、「查」是最近一次確認專案還在的那天 |
| **採用**（下方目錄） | ✅ 廣泛採用（要有多個獨立使用回饋，不是只有星數）/ ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑 / ❌ 已放棄——與證據等級**不同軸** |
| **類型** | 多 Agent / 記憶工具 / 費用監測 / 工作流 / 整合工具 / 搜尋/診斷 / 安全工具 / IDE/終端 / Skills / 模型路由 / UI 工具 / 其他 |
| **入選標準** | HN score ≥ 30 或評論 ≥ 5 / Show HN 投稿 / 同日 2 個獨立來源；沒有公開 repo、示範站或任何可點的連結就不列——讀者裝不了的東西不該佔一列 |

---

## 工具目錄

這份目錄是上面判斷的底：每一列都點得進去，最早到 2026-04。採用符號與證據是兩條不同的軸，見上方指標說明。

| 工具 | 類型 | 採用 | 首次出現 | 簡介 |
| --- | --- | --- | --- | --- |
| [**AgentSystemLabs/agent-office**](https://github.com/AgentSystemLabs/agent-office) | 多 Agent | ⏳ | 2026-10-02 | 3D 虛擬辦公室，團隊可「雇用」Claude Code 當座位員工，共享終端機並追蹤 issue／PR；506 星 |
| [**UNLINEARITY/CLI-WeChat-Bridge**](https://github.com/UNLINEARITY/CLI-WeChat-Bridge) | 整合工具 | ⏳ | 2026-10-02 | 把 Codex、Claude Code、OpenCode 等 CLI 接進微信／企業微信機器人，雙向對話與檔案傳輸；522 星 |
| [**Coolver/home-assistant-vibecode-agent**](https://github.com/Coolver/home-assistant-vibecode-agent) | 整合工具 | ⏳ | 2026-10-02 | Home Assistant 的 MCP server，用自然語言建立與除錯自動化、設計儀表板；630 星 |
| [**kharmanskyi/open-steps**](https://github.com/kharmanskyi/open-steps) | Skills | ⏳ | 2026-10-02 | 平實語言 agent skills，產出誠實的 session 報告與直白結論；1,078 星 |
| [**Rhun**](https://rhun.app/) | IDE/終端 | ⏳ | 2026-10-01 | Show HN：組合語言寫的輕量編輯器，內建面板可接 Claude Code／Codex session；HN 單來源 |
| [**Breadcrumb**](https://innerloop.works/breadcrumb) | 記憶工具 | ⏳ | 2026-10-01 | Show HN：本機加密記錄 Mac 螢幕、會議與 AI 對話並轉成可搜尋記憶庫，相容 Claude Code／Codex／Cursor |
| [**Usage Updates**](https://usageupdates.com/) | 費用監測 | ⏳ | 2026-10-01 | Show HN：社群維護的 Claude／Codex 額度重置與限制變更時間軸，不是告警工具 |
| [**dmitry-markin/silta**](https://github.com/dmitry-markin/silta) | 記憶工具 | ⏳ | 2026-10-01 | Show HN：自架 Matrix 家庭助理，用交接與壓縮摘要流程讓對話跨越 context 上限；HN 單來源 |
| [**Louis-CFM/coucou**](https://github.com/Louis-CFM/coucou) | IDE/終端 | ⏳ | 2026-10-01 | 常駐 macOS 瀏海或 Windows 螢幕頂端、持續顯示 Claude Code session 狀態；2,268 星 |
| [**rehan-remade/universal-modder**](https://github.com/rehan-remade/universal-modder) | Skills | ⏳ | 2026-10-01 | 讓 Claude Code 改裝任何 PC 遊戲，整合 fal MCP 生成美術／音效並做反組譯分析；1,388 星 |
| [**vshulcz/deja-vu**](https://github.com/vshulcz/deja-vu) | 記憶工具 | ⏳ | 2026-10-01 | 直接搜尋 Claude Code、Codex、Cursor 等 30 餘款 agent 硬碟上的 session 歷史、不呼叫 LLM；1,113 星 |
| [**kitfunso/hippo-memory**](https://github.com/kitfunso/hippo-memory) | 記憶工具 | ⏳ | 2026-10-01 | 會學習「這是錯的」並停止重複犯錯的記憶系統，本機 SQLite＋MCP；769 星 |
| [**infragate/capa**](https://github.com/infragate/capa) | 工作流 | ⏳ | 2026-10-01 | 單一 capabilities.yaml 把 skills、rules、sub-agents、MCP 接進 30 餘款 coding agent；726 星 |
| [**elidickinson/pi-claude-bridge**](https://github.com/elidickinson/pi-claude-bridge) | 整合工具 | ⏳ | 2026-10-01 | 讓 pi.dev 的 Pro／Max 訂閱當 Claude Code 的推論來源；509 星 |
| [**sshah03/perspica**](https://github.com/sshah03/perspica) | 工作流 | ⏳ | 2026-09-30 | Show HN：審閱大型 AI 產生 PR 的語意化 diff，可選不靠 LLM 的機械分組 |
| [**rulereceipt/rulereceipt**](https://github.com/rulereceipt/rulereceipt) | 工作流 | ⏳ | 2026-09-30 | Show HN：檢查 coding agent 有沒有真的遵守 CLAUDE.md／AGENTS.md；討論串質疑 agent 能關掉檢查 hook |
| [**Vincentwei1021/video-talkcraft**](https://github.com/Vincentwei1021/video-talkcraft) | Skills | ⏳ | 2026-09-30 | 把 Claude Code／Codex 變動態設計工作室，逐字稿配音同步、Remotion 算圖；1,314 星 |
| [**Anionex/agent-vision-toolkit**](https://github.com/Anionex/agent-vision-toolkit) | 整合工具 | ⏳ | 2026-09-30 | 為純文字模型補視覺：多圖問答、長截圖 OCR、UI 還原與 GUI 自動化；1,219 星 |
| [**alexgreensh/attention-span**](https://github.com/alexgreensh/attention-span) | Skills | ⏳ | 2026-09-30 | ADHD 友善輸出風格外掛，讓 agent 輸出更「人話」；1,149 星 |
| [**gargpratyush/jev-router**](https://github.com/gargpratyush/jev-router) | 模型路由 | ⏳ | 2026-09-30 | 依任務自動路由到最便宜可用模型的小工具；500 星 |
| [**Paritok-official/paritok-4b-v1**](https://github.com/Paritok-official/paritok-4b-v1) | 費用監測 | ⏳ | 2026-09-29 | 非破壞性壓縮閘道，宣稱最多省 85% token（自研 4B 模型），未見第三方覆核；1,453 星 |
| [**snflkd/fluent-korean**](https://github.com/snflkd/fluent-korean) | Skills | ⏳ | 2026-09-29 | 讓 Claude Code 講出流暢韓文的 output-style 外掛；1,349 星 |
| [**Nanako0129/coralline**](https://github.com/Nanako0129/coralline) | IDE/終端 | ⏳ | 2026-09-29 | 仿 Powerlevel10k 的 Claude Code 狀態列外掛，AI 訪談後自動安裝；542 星 |
| [**AMAP-ML/LongHorizon-Harness**](https://github.com/AMAP-ML/LongHorizon-Harness) | 多 Agent | ⏳ | 2026-09-28 | 長時任務 computer-use harness，跨桌面應用與 CLI 維持任務狀態，原生支援 Claude；1,638 星 |
| [**yetone/magpie**](https://github.com/yetone/magpie) | 模型路由 | ⏳ | 2026-09-28 | 選單列小工具，同一介面切換底層模型（Claude Code 搭 Kimi、Codex 搭 DeepSeek）；1,571 星 |
| [**tigerless-labs/agent-memory**](https://github.com/tigerless-labs/agent-memory) | 記憶工具 | ⏳ | 2026-09-28 | 純 Markdown 為單一事實來源的長期記憶層，Claude Code 與 Codex 共用、不需 API key；1,486 星 |
| [**emilkowalski/skills**](https://github.com/emilkowalski/skills) | Skills | ⏳ | 2026-09-26 | 給設計師與工程師的 skills 集合；41,182 星（2026-03 出生），僅星數佐證 |
| [**Yuan1z0825/nature-skills**](https://github.com/Yuan1z0825/nature-skills) | Skills | ⏳ | 2026-09-26 | 符合 Nature 論文學術表達與科研繪圖規範的 skill；44,559 星（2026-04 出生），僅星數佐證 |
| [**reladraw/reladraw**](https://github.com/reladraw/reladraw) | 其他 | ⚡ | 2026-09-26 | Show HN：可自訂版面配置的圖表描述語言，附 npm 套件與 agent skill；HN 351 分 |
| [**brumar/chess-postmortem-skills**](https://github.com/brumar/chess-postmortem-skills) | Skills | ⏳ | 2026-09-26 | Show HN：讓 Claude 以視覺看棋局並結合 Stockfish 解說、輸出講解影片；2 個來源同日報導 |
| [**Avinash-jetwani/jevmem**](https://github.com/Avinash-jetwani/jevmem) | 記憶工具 | ⏳ | 2026-09-25 | HN：Claude Code 專案記憶自動化；留言質疑「舊記錄標過時但不刪」會累積過期 context |
| [**ComposioHQ/awesome-claude-skills**](https://github.com/ComposioHQ/awesome-claude-skills) | Skills | ⏳ | 2026-09-25 | Claude Skills 精選資源與工具清單；75,625 星，2025-10 出生 |
| [**mattpocock/skills**](https://github.com/mattpocock/skills) | Skills | ⏳ | 2026-09-25 | 作者整理自己 `.agents` 目錄下的 skills 集合；269,509 星（2026-02 出生），增速異常，僅星數佐證，forks／issues 未查 |
| [**Ryze-AI-Adgent/open-seo-mcp-skills**](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) | 領域資料 | ⏳ | 2026-09-24 | 免費 SEO MCP 伺服器與開源 SEO／GEO Claude skills，可用真實 GSC／GA4／廣告數據做關鍵字研究、排名追蹤；1,449 星 |
| [**bangtutorial/bang-motion**](https://github.com/bangtutorial/bang-motion) | 其他 | ⏳ | 2026-09-24 | 瀏覽器動態圖形 agent skill，產出片頭／宣傳片／動態字卡等五種解說風格，單一 index.html 輸出，相容 Claude Code／Codex／Gemini CLI／Cursor；509 星 |
| [**Callous-0923/agent-study**](https://github.com/Callous-0923/agent-study) | 其他 | ⏳ | 2026-09-24 | 36 章 AI Agent 全端課程，涵蓋 ReAct 迴圈、Claude Code 逆向、MCP／A2A 協議、RAG、DSPy；500 星 |
| [**ApodexAI/FrontierAgent**](https://github.com/ApodexAI/FrontierAgent) | 多 Agent | ⏳ | 2026-09-23 | 原生命令列 TUI agent 框架，支援 ReAct 與 Agent Team 模式，一行指令安裝；4,515 星，近 8 天漲 1,403 |
| [**naw103/foremerge**](https://github.com/naw103/foremerge) | 多 Agent | ⏳ | 2026-09-22 | 疊在 git 之上的協調層，讓多個並行 coding agent 動手前先發布意圖，攔截架構層級的意圖衝突；Show HN，2 個獨立來源同日報導 |
| [**jens-duttke/usage-monitor-for-claude**](https://github.com/jens-duttke/usage-monitor-for-claude) | 費用監測 | ⏳ | 2026-09-22 | Windows 工作列常駐的額度監看器，可自己設到幾 % 就跳提醒；293 星、53 forks、09-13 仍在更新（查證日 2026-09-22，來自讀者提問） |
| [**Maciek-roboblog/Claude-Code-Usage-Monitor**](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 費用監測 | ⏳ | 2026-09-22 | 跨平台額度監看與用盡時間預測，額度將滿時出警告；8,713 星，2026-07-05 後未更新（查證日 2026-09-22，來自讀者提問） |
| [**wavever/CCLimitPing**](https://github.com/wavever/CCLimitPing) | 費用監測 | ⏳ | 2026-09-22 | 5 小時限制解除的瞬間自動送出 continue，省掉盯盤等待；45 星、09-14 仍在更新（查證日 2026-09-22，來自讀者提問） |
| [**bozdemir/claude-usage-widget**](https://github.com/bozdemir/claude-usage-widget) | 費用監測 | ⏳ | 2026-09-22 | 跨平台額度小工具，接近上限時跳提醒；53 星、09-21 仍在更新（查證日 2026-09-22，來自讀者提問） |
| [**docsagent/docsagent**](https://github.com/docsagent/docsagent) | 整合工具 | ⏳ | 2026-09-21 | MCP 伺服器讓 agent 即時、私有存取個人知識庫（先支援 Zotero），原生 C++ 搜尋核心（BM25＋段落排序，約 15ms）；616 星 |
| [**michael-denyer/pstack-claude**](https://github.com/michael-denyer/pstack-claude) | 整合工具 | ⏳ | 2026-09-20 | 把 Cursor 的 agent workflow 基礎架構移植給 Claude Code、Codex、opencode 使用；504 星 |
| [**CodeZeno/Claude-Code-Usage-Monitor**](https://github.com/CodeZeno/Claude-Code-Usage-Monitor) | 費用監測 | ⏳ | 2026-09-20 | Windows 工作列小工具，追蹤 Claude Code、Codex、Cursor 等工具的用量上限與重置時間；500 星（與同名的 Maciek-roboblog 版本非同一專案） |
| [**aoci-spec/aoci-code**](https://github.com/aoci-spec/aoci-code) | 記憶工具 | ⏳ | 2026-09-20 | 把整個程式庫與資料庫結構做成持久化、Git 版控的索引，供編碼 agent 動手前先讀取；446 星 |
| [**snyk/agent-scan**](https://github.com/snyk/agent-scan) | 安全工具 | ⏳ | 2026-09-18 | Snyk 出品，掃描 AI agent、MCP 伺服器與 agent skills 的資安工具；3,060 星，2025-04 出生 |
| [**browserbase/stagehand**](https://github.com/browserbase/stagehand) | 整合工具 | ⏳ | 2026-09-17 | 網頁資料擷取與互動 SDK，可搭配 Claude Code／Codex／Eve／Mastra 使用；24,318 星，2024-03 出生 |
| [**Nanako0129/sepia**](https://github.com/Nanako0129/sepia) | Skills | ⏳ | 2026-09-16 | 去 AI 化寫作風格修正 skill，相容 77 種以上 Agent Skills 相容 agent，含 Claude Code／Codex；2,640 星 |
| [**ruvnet/open-claude-code**](https://github.com/ruvnet/open-claude-code) | 其他 | ⏳ | 2026-09-16 | 逆向工程還原重建的 Claude Code CLI 每夜反編譯專案；501 星 |
| [**AThevon/TokenEater**](https://github.com/AThevon/TokenEater) | 費用監測 | ⏳ | 2026-09-16 | 原生 macOS App，監控 Claude AI 用量限制並即時觀看編碼 session；500 星 |
| [**aannoo/hcom**](https://github.com/aannoo/hcom) | 多 Agent | ⏳ | 2026-09-16 | 讓 AI agent 跨終端機互相傳訊、監看、生成彼此的工具，支援 Claude Code／Codex／Antigravity CLI／Cursor CLI／OpenCode；500 星 |
| [**RKiding/Awesome-finance-skills**](https://github.com/RKiding/Awesome-finance-skills) | Skills | ⏳ | 2026-09-16 | 金融分析 Agent Skills 開源合輯；3,011 星 |
| [**google/artemis**](https://github.com/google/artemis) | 整合工具 | ⏳ | 2026-09-16 | 把自然語言指令轉成可靠 Android 自動化操作，可接 Antigravity／Codex／Claude Code；宣稱 AndroidWorld Benchmark 達 99%+ 成功率；6,291 星，2 個獨立來源同日報導 |
| [**zenstory-ai/oh-story-claudecode**](https://github.com/zenstory-ai/oh-story-claudecode) | Skills | ⏳ | 2026-09-13 | 中文網路小說寫作 agent skills 合集，涵蓋扫榜、拆文、寫作、去 AI 味、封面全流程；6,824 星，2026-04 出生 |
| [**rpamis/comet**](https://github.com/rpamis/comet) | 工作流 | ⏳ | 2026-09-12 | 把想法轉成可評測工作流程的 agent skill harness；3,023 星，2026-05 出生 |
| [**Agents365-ai/drawio-skill**](https://github.com/Agents365-ai/drawio-skill) | Skills | ⏳ | 2026-09-11 | 把自然語言、程式碼、Terraform/K8s、SQL、OpenAPI 轉換為可編輯、經測試的 draw.io 架構圖，支援增量同步與 CI 架構測試；9,231 星，2026-03 出生 |
| [**avibe-bot/avibe**](https://github.com/avibe-bot/avibe) | 多 Agent | ⏳ | 2026-09-10 | 本機優先 Agent OS，AI 夥伴常駐使用者機器，經瀏覽器或聊天 App 驅動官方 Claude Code／Codex／OpenCode；501 星 |
| [**firstintent/ccteam**](https://github.com/firstintent/ccteam) | 多 Agent | ⏳ | 2026-09-10 | 把已在跑的多個編程 agent（Claude Code、Codex、Grok、DeepSeek Harness、Kimi、Pi）整編成一支團隊，跨廠商跨機器分派任務並經 Telegram／Lark／瀏覽器統一操控；501 星 |
| [**ccch1mneyyy/dsh-TUI**](https://github.com/ccch1mneyyy/dsh-TUI) | IDE/終端 | ⏳ | 2026-09-10 | 中國社群「DSH」官方收錄的 TUI 補位插件，Claude Code 風格介面元件（鯨魚頂欄、串流思考顯示、雙擊 Esc 回滾、含 TPS 的 context 進度條）；2,933 星 |
| [**tony1223/better-agent-terminal**](https://github.com/tony1223/better-agent-terminal) | IDE/終端 | ⏳ | 2026-09-10 | 多工作區終端機聚合工具，整合 Claude Code 的 AI 協作功能；502 星 |
| [**OtoDock**](https://github.com/OtoDock/oto-dock) | 多 Agent | ⚡ | 2026-09-09 | 自架版正式定位為「公司作業系統」，Claude Code＋Codex agent 部署於各部門、多租戶協作與遠端 WebSocket 配置；HN 46 分，另有 3 家獨立來源同日報導 |
| [**Untrivial-ai/agent-orchestrator**](https://github.com/Untrivial-ai/agent-orchestrator) | 多 Agent | ⏳ | 2026-09-09 | 可執行並監督一整組 coding agent 團隊、涵蓋規劃到合併全流程的整合平台；11,149 星 |
| [**borski/travel-hacking-toolkit**](https://github.com/borski/travel-hacking-toolkit) | Skills | ⏳ | 2026-09-09 | 旅遊比價 Skill 與 MCP server，跨 Claude／Codex／OpenCode；657 星 |
| [**I-have-ADHD**](https://github.com/ayghri/i-have-adhd) | Skills | ⏳ | 2026-09-08 | 鎖定「Claudism」冗語，阻止 coding agent 完成任務後反覆交代哪些沒做；HN score 499，另有一家獨立來源報導 |
| [**zenstory-ai/video-recap-skills**](https://github.com/zenstory-ai/video-recap-skills) | Skills | ⏳ | 2026-09-08 | Claude Code Skill 把任意影片剪成中文口述影評，支援剪映匯出；500 星 |
| [**trailofbits/coop**](https://github.com/trailofbits/coop) | 安全工具 | ⏳ | 2026-09-07 | 隔離 VM 環境跑 Claude Code 與 Codex，agent 碰不到其他專案或個人檔案；HN score 36 |
| [**plannotator/effective-html**](https://github.com/plannotator/effective-html) | Skills | ⏳ | 2026-09-07 | Agent Skills 技能包，產出可用 HTML artifact、線框稿、互動原型、計畫與圖表；3,023 星 |
| [**ruvnet/metaharness**](https://github.com/ruvnet/metaharness) | 多 Agent | ⏳ | 2026-09-07 | Agent 框架腳手架，生成自帶 CLI／MCP 伺服器／記憶與學習迴圈的專屬 harness；634 星 |
| [**nirholas/XActions**](https://github.com/nirholas/XActions) | 整合工具 | ⏳ | 2026-09-07 | X/Twitter 自動化工具組，內建供 AI agent 使用的 MCP 伺服器與 CLI；513 星 |
| [**aqm857886159/Nomi**](https://github.com/aqm857886159/Nomi) | 整合工具 | ⏳ | 2026-09-07 | 開源 AI 影片工作台，透過 MCP 讓 Claude Code／Codex／Cursor 指揮生成與剪輯；500 星 |
| [**nafeeur/MaskShift**](https://github.com/nafeeur/MaskShift) | 整合工具 | ⏳ | 2026-09-06 | 零 npm 依賴的本地優先 coding agent harness，可支援無原生 tool-calling API 的模型；HN 1 分，同日另有一則獨立來源提及 |
| [**awdr74100/figwright**](https://github.com/awdr74100/figwright) | 整合工具 | ⏳ | 2026-09-06 | 雙向 Figma MCP，設計稿轉框架感知程式碼、程式碼變更可推回畫布；684 星 |
| [**Gentleman-Programming/gentle-ai**](https://github.com/Gentleman-Programming/gentle-ai) | 記憶工具 | ⏳ | 2026-09-06 | 一套設定讓 Claude Code／Cursor／OpenCode／Codex 共用持久記憶＋規格驅動開發；6,304 星 |
| [**EliaAlberti/cpr-compress-preserve-resume**](https://github.com/EliaAlberti/cpr-compress-preserve-resume) | 記憶工具 | ⏳ | 2026-09-06 | 跨 session 儲存、搜尋並還原對話上下文；508 星 |
| [**karanb192/claude-code-hooks**](https://github.com/karanb192/claude-code-hooks) | 工作流 | ⏳ | 2026-09-06 | hooks 套件＋可安裝外掛市集，涵蓋安全性／成本／可觀測性／生產力；500 星 |
| [**feder-cr/AIHawk**](https://github.com/feder-cr/AIHawk) | 整合工具 | ⏳ | 2026-09-05 | 開源瀏覽器自動化與電腦操作 agent，含 Claude Code／Gemini CLI 適用 Browser MCP；3.03 萬星 |
| [**thedotmack/claude-mem**](https://github.com/thedotmack/claude-mem) | 記憶工具 | ✅ | 2026-09-02 | 跨 harness（Claude Code、OpenClaw、Codex、Gemini 等 7 種以上）持久記憶，擷取 session 過程並用 AI 壓縮注入後續 session；9.3 萬星，2025-08-31 出生 |
| [**yetone/cumora**](https://github.com/yetone/cumora) | 工作流 | ⏳ | 2026-09-02 | 跨平台團隊聊天工具，讓 AI agent 成為聊天中的「一等公民」隊友，可接 Claude Code／Codex；3,416 星，作者具名知名開源開發者 |
| [**wanghuan9/skilldock**](https://github.com/wanghuan9/skilldock) | Skills | ⏳ | 2026-09-02 | AI skill 管理桌面應用，安裝/整理/編輯/同步/更新 Skills、MCP servers、plugins，跨 5 種 AI coding 工具；503 星 |
| [**Understand-Anything**](https://github.com/Egonex-AI/Understand-Anything) | 搜尋/診斷 | ⏳ | 2026-09-02 | 互動式 code 知識圖（可探索/搜尋/提問），跨 harness；81,325★、2026-03 出生，09-02 查證（防刷通過），社群實測待累積 |
| [**codegraph**](https://github.com/colbymchenry/codegraph) | 記憶工具 | ⏳ | 2026-09-02 | 預索引 code 知識圖、改 code 自動同步、全本機省 token；69,253★、2026-01 出生，09-02 查證（防刷通過），graphify 競品 |
| [**archify**](https://github.com/tt-a1i/archify) | Skills | ⏳ | 2026-09-02 | 架構/時序/資料流圖 agent skill，自包含 HTML；43,378★、2026-04 出生，09-02 查證（防刷通過） |
| [**Shubhamsaboo/awesome-llm-apps**](https://github.com/Shubhamsaboo/awesome-llm-apps) | Skills | ✅ | 2026-08-30 | 彙整百餘款 AI Agent、Agent Skills 與 RAG 開源應用清單；13.5 萬星，2024-04 出生，長期累積型參考資源 |
| [**x1xhlol/system-prompts-and-models-of-ai-tools**](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 其他 | ✅ | 2026-08-29 | 彙整 Claude Code、Cursor、Devin AI、Replit 等數十款 AI 編碼工具完整系統提示詞與模型設定；14.3 萬星，2025-03 出生，長期累積型參考資源 |
| [**multica-ai/andrej-karpathy-skills**](https://github.com/multica-ai/andrej-karpathy-skills) | Skills | ⏳ | 2026-08-29 | 單一 CLAUDE.md 檔案改善 Claude Code 行為，取材自 Karpathy 對 LLM coding 常見缺陷的觀察；20.9 萬星，可信度低（見收錄註記） |
| [**JimLiu/baoyu-design**](https://github.com/JimLiu/baoyu-design) | Skills | ⏳ | 2026-08-29 | 本機以 Agent Skill 執行 [[entities/claude-design]]，供 Cursor／Claude Code 產出自足式 HTML UI 原型，官方建議搭配 Opus 4.8；3,637 星 |
| [**obra/superpowers**](https://github.com/obra/superpowers) | Skills | ⏳ | 2026-08-28 | Agentic skills 框架與軟體開發方法論；累計 27.9 萬星（08-28），2025-10 出生；只有星數佐證，forks／issues 未查，但 Reddit 上已見使用者抱怨，間接說明真有人在用 |
| [**tare**](https://github.com/kelviq/tare) | 費用監測 | ⏳ | 2026-08-27 | CLI 底部即時顯示 usage/context/model 狀態並配合 hook 監測用量暴增；Show HN score 84 |
| [**mindmuxai/brain.md**](https://github.com/mindmuxai/brain.md) | 記憶工具 | ⏳ | 2026-08-25 | 零依賴、檔案式跨 session 持久記憶層，為 coding agent 保存決策／需求／限制的「專案大腦」；504 星 |
| [**OzBrain**](https://ozbrain.com) | 記憶工具 | ⏳ | 2026-08-21 | agent 與團隊共享的知識庫，取代傳統筆記/任務管理工具；Show HN score 69，多家報導 |
| [**Proliferate**](https://github.com/proliferate-ai/proliferate) | 多 Agent | ⏳ | 2026-08-21 | YC S25，開源自架 AI IDE，統一操作 Claude Code／Codex／OpenCode／Cursor／Grok；Show HN score 39，多家報導 |
| [**Frugal Tokens**](https://github.com/dpclark4/frugal-tokens) | 費用監測 | ⏳ | 2026-08-19 | 探索跨 coding agent（含 Claude Code）的成本與用量，含 cache miss 對花費的影響；Show HN score 33，多家報導 |
| [**Graft**](https://github.com/trailhq/Graft) | 費用監測 | ⚠️ | 2026-08-15 | Claude Code hooks 削減 grep 輸出 token，宣稱降幅 42%（HN 39，跨 2 來源）；HN 討論串質疑 README 的 benchmark 段落疑似 AI 代寫，數字未經第三方覆核 |
| [**HUD**](https://github.com/adrida/hud-mode) | IDE/終端 | ⏳ | 2026-08-07 | 開源極簡終端 UI，支援 Claude Code／Codex／OpenCode；經官方 JSON event stream 運作不額外耗 token；HN 25 |
| [**omnigent**](https://github.com/omnigent-ai/omnigent) | 多 Agent | ⏳ | 2026-08-05 | harness 無關 meta-harness，換底層 agent（Claude Code／Codex／Cursor／Pi）不必重寫協作邏輯；2026-09-22 查得 10,150 星、forks 15.9% |
| [**pxpipe**](https://github.com/teamchong/pxpipe) | 費用監測 | ⏳ | 2026-08-05 | 把文字 context 渲染成圖片降低 token 用量，實測約 25,000 text token 壓至 2,700 image token；6,955 星，已查證非刷星（forks 8.5%） |
| [**claude-workflow-v2**](https://github.com/CloudAI-X/claude-workflow-v2) | 工作流 | ✅ | 2026-08-04 | 通用 Claude Code 工作流插件（7 agents+26 commands+14 skills+14 hooks），1.4k 星／188 forks，有多個獨立的實際使用回饋 |
| [**episko**](https://github.com/respeak-io/episko)（原名 Cockpit） | 多 Agent | ⏳ | 2026-08-02 | Rust 打造的 Claude Code 多 Agent 監控主控台，彙整多個 agent／session／專案執行狀態於單一介面；HN score 11，2026-09-22 查得已改名並發到 v0.30.0 |
| [**Claude Code Merge Queue**](https://github.com/funador/claude-code-merge-queue) | 多 Agent | ⏳ | 2026-07-30 | 讓多個平行 agent 的 commit 排隊依序落地、逐一建置測試後才合併，緩解低規格機器同時建置的資源競爭；HN 39 |
| [**Sx 2.0**](https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html) | Skills | ⚡ | 2026-07-13 | 透過 Dropbox / Google Drive / iCloud 免 git 分享 Claude/Codex skill；2.0 版新增原生 app 與 Skill Evals；Show HN score 39 |
| [**Geosql**](https://github.com/dekart-xyz/geosql) | Skills | ✅ | 2026-07-08 | Claude/Codex/Copilot 地理空間資料 skill（PostGIS／BigQuery／Snowflake）；「4 倍效能提升」機制已查證，見下方 Geosql 那則細節（HN score 55） |
| [**Workweave Router**](https://github.com/weave-os/router) | 模型路由 | ⚡ | 2026-06-27 | 成本感知模型路由器，作為 Anthropic/OpenAI 相容 endpoint 運作，依請求難度自動路由模型；起因 Opus 4.7 tokenizer 改版後成本大漲；實測成本降 40%+；Show HN score 181 |
| [**bulk-delete-claude-chat**](https://github.com/MatteoLeonesi/bulk-delete-claude-chat) | UI 工具 | ⚡ | 2026-06-13 | 解決 Claude 網頁版缺乏批量刪除對話功能的痛點；自動捲動、全選、刪除（對比 ChatGPT 已有內建批量刪除）；HN score 56 |
| [**AVP（Agent Vault Proxy）**](https://github.com/inflightsec/agent-vault-proxy) | 安全工具 | ⚡ | 2026-06-12 | 解決 coding agent 持有 API key 的安全風險；placeholder + 最後一刻注入，agent 環境只存 placeholder，真實金鑰在 wire 層即時替換；Show HN |
| [**Workplane**](https://workplane.co) | 整合工具 | ⚡ | 2026-06-12 | 解決 Claude/Codex 輸出的 .md/.html 檔案難以分享問題；支援版本回滾與 MCP 整合，Claude Desktop／Code／OpenClaw 均可存取共享資料夾；Show HN |
| [**VIR**](https://www.reddit.com/r/ClaudeAI/comments/1tlcai2/) | 記憶工具 | ⚡ | 2026-05-23 | 背景讀取 `~/.claude/projects` session 檔萃取知識（pattern/gotcha/decision/tool），寫入 Obsidian vault 供 MCP 存取，解決記憶歸零問題 |
| [**Shortcuts Playground**](https://www.macstories.net/stories/introducing-shortcuts-playground/) | Skills | ⚡ | 2026-05-23 | Claude Code / Codex 開源 plugin，用自然語言描述即可生成 Apple Shortcuts；MacStories 出品，完整文件化，直接指向 plugin repo 即可安裝；Show HN 發布 |
| [**Proof Loop**](https://github.com/LeoStehlik/proof-loop) | 工作流 | ⚡ | 2026-05-22 | 針對 agent 謊報任務完成的問題：要求設定驗收標準、分離建構者與驗證者角色、每項標準記錄 PASS/FAIL/UNKNOWN 結果並附證據；Show HN 發布 |
| [**clarp**](https://www.reddit.com/r/ClaudeAI/comments/1tj2exk/claude_p_is_moving_to_metered_pricing_on_june_15/) | 費用監測 | ⚡ | 2026-05-21 | `claude -p` drop-in 替代品，本地 PTY + 唯讀 API 代理，規避 6/15 計量計費，多數專案只需更換 binary 名稱 |
| [**Logbox**](https://github.com/struct-dot-ai/logbox) | 整合工具 | ⚡ | 2026-05-20 | 將 dev server log 導入本地 SQLite，再透過 MCP 讓 Claude Code 直接查詢，解決 Claude 無法即時追蹤 log 流的問題；Show HN 發布 |
| [**PrismoDev**](https://github.com/shanirsh/prismodev) | 搜尋/診斷 | ⚡ | 2026-05-20 | 掃描本地 session log，找出 context bloat 來源（過大 CLAUDE.md、重複 tool output、broad exploration），不需 API key、本地離線；Show HN |
| [**mdviewer**](https://github.com/rajatarya/mdviewer) | 其他 | ⚡ | 2026-05-20 | 100% 由 AI coding agent 完成的原生 macOS Markdown 閱覽器，支援 Obsidian 延伸語法／Mermaid／數學公式，以 Tauri 2 打造無 Electron 依賴；Show HN |
| [**cdesktop**](https://www.reddit.com/r/ClaudeAI/comments/1thlxrw/cdesktop_opensource_claude_code_desktop/) | 多 Agent | ⚡ | 2026-05-19 | 開源桌面應用，單一 UI 整合 Claude Code／Codex／Gemini CLI 等 5 個 coding agent，支援 20+ 第三方模型，`npx` 執行 |
| [**agent-baton**](https://www.reddit.com/r/ClaudeAI/comments/1tgel55/) | 費用監測 | ⚡ | 2026-05-18 | 利用 Anthropic 使用量 API + Claude Code hook，在觸及速率上限前主動發出警告並轉移進行中的工作，解決 Claude Code 靜默中斷的長期痛點 |
| [**LockedIn**](https://www.reddit.com/r/ClaudeAI/comments/1tg8yg6/) | 記憶工具 | ⚡ | 2026-05-18 | Claude Code 插件（1 路由技能 + 6 子技能），在 session 中持續記錄開發者工作脈絡，下次對話的 Claude 可直接繼承上次進度，無需重新說明背景 |
| [**Writ**](https://www.reddit.com/r/ClaudeAI/comments/1tb047p/) | 工作流 | ⚡ | 2026-05-12 | Neo4j 知識圖譜 5 階段 Pipeline 自動擷取相關規則集，解決 CLAUDE.md 被忽略 + 無關規則耗 token 雙重問題 |
| [**Usage4Claude 3.0.0**](https://www.reddit.com/r/ClaudeAI/comments/1tazqpg/) | 費用監測 | ✅ | 2026-05-12 | 開源 macOS 選單列用量追蹤，3.0.0 版新增 Codex 追蹤，憑證存 Keychain |
| **claudely** | 多 Agent | ⚡ | 2026-05-04 | 保留 Claude Code 生態的前提下切換至 Ollama/LM Studio/llama.cpp，無需改主配置；2026-09-22 查不到公開 repo 或產品頁 |
| [**Omar**](https://github.com/omar-os/omar) | 多 Agent | ⚡ | 2026-05-02 | 統一管理多個 Claude Code agent 的編排工具；05-02 收錄時的說法是「TUI 儀表板管到 100 個 agent」，2026-09-22 查得網域改為 omar.rs、repo 48★，自述已改為形式化編排 |
| [**graphify**](https://github.com/Graphify-Labs/graphify) | 記憶工具 | ✅ | 2026-05-02 | Leiden 偵測建程式碼知識圖譜，作者宣稱 71 倍 token 減少（05-02）；2026-09-22 查得 12.0 萬★、11,626 forks |
| **Caliber** | 工作流 | ⚡ | 2026-05-02 | 跨工具 AI config 統一管理（CLAUDE.md/.cursor/rules/AGENTS.md）；05-02 記到 888 stars，2026-09-22 查不到公開 repo 或產品頁 |
| [**ness**](https://github.com/ness-dev/ness)（原名 Harness） | 多 Agent | ⚡ | 2026-04-29 | 多 Git worktree 並行管理多個 Claude Code agent；2026-09-22 查得已改名 ness、99★，自述改為「給 agent 用的 IDE」，README 仍寫可同時跑十個 Claude |
| [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 工作流 | ⚡ | 2026-04-27 | Stop Hook，強制 Claude 提供可驗證執行證明才能宣告完成 |
| [**Claude Squad**](https://www.reddit.com/r/ClaudeAI/comments/1svmpkv/) | 多 Agent | ✅ | 2026-04-26 | 多人多 agent 並行開發，orchestrator 分派任務並合併分支 |
| [**mux0**](https://mux0.com/) | IDE/終端 | ✅ | 2026-04-26 | 開源 macOS 終端，側邊欄即時顯示多 agent 狀態 |

**收錄註記**（表內「見收錄註記」的一筆）
- **andrej-karpathy-skills**（08-29）：僅 GitHub Search 星數，無 forks／issues 佐證可查，增速異常，不作為獨立驗證訊號。

**一則細節**
- **Geosql 的「4 倍」只在連 Dekart 時成立**（2026-08-13 查證）：GeoSQL 讓 agent 把查詢結果經 Dekart 渲染成地圖、回看修正幾何錯誤；沒連 Dekart 時表現與一般 SQL agent 相當，先前細部數據加總不一致就是這個原因（[dekart.xyz 部落格](https://dekart.xyz/blog/claude-code-vs-aino-geospatial-agent/)、[Show HN](https://news.ycombinator.com/item?id=48829242)）。

---

## 參考來源

- [[topics/community-tech-patterns]] — 工作流模式與技術做法
- [[topics/community-tech-discussions]] — 概念辯論與設計哲學
- [[topics/official-community-gap]] — 官方 vs 社群缺口分析
- [[topics/skill-interest-watch]] — 社群工具規模榜：各類工具在 GitHub 上現在誰大、本週誰在漲
- [[topics/community-large-codebase-workflow]] — 大型 codebase 的四條做法主線，每條線都指回本頁的症狀列
- [[feature-radar]] — 官方功能熱度雷達

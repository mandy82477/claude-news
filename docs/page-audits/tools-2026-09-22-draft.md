# 第 15 波設計者逐字稿：topics/community-tech-tools

兩大節：**A 進頁面**（可直接貼上）、**B 進規則檔**（寫明檔名＋節名＋放在哪一條之後）。行號＝對象頁檔案原始行號（含 frontmatter）。
官方事實一律取自 `docs/page-audits/tools-2026-09-22-verified.md`；本檔所有星數、owner、issue 狀態皆逐字對應該檔，未另行推測。
**分岔標示**：正文照**保守預設**寫（裁決點「tools 決策表 ↔ skill-interest-watch 逐字副本要不要併」未回覆）；`〔併〕` 標記處為使用者裁「併」時的替代逐字。
`<實作當天>` 由實作者填當日日期。

---

# A. 進頁面

## A-1 標頭（取代 L33–L34）

```markdown
**最後更新：** <實作當天>
**最後新聞更新：** <實作當天>
```

> 全頁只留 callout 一個日期口徑；frontmatter 由 `scripts/gen_wiki_frontmatter.py` 產，不手填。

## A-2 callout（取代 L36–L37）

```markdown
> **三個首選工具改了名，舊連結靠轉址活著**（<實作當天>）
> 多 agent 互踩那列的 Harness 已改名 ness、監看那列的 Omar 換了網域與 repo、GUI 主控台 Cockpit 改叫 episko——照舊名搜尋會找不到，連結全部換成現在的位址。決策表同時新增「額度快用完，想在斷線前被提醒」一列。
```

## A-3 摘要（取代 L43–L44）

```markdown
**我卡住了，社群有什麼能救？** 本頁把社群工具依「症狀」排列：每個症狀給一個先裝的、一條「什麼時候該改裝別的」的分界，以及這個判斷是哪天下的、最近一次確認這個專案還在不在是哪天。有一個症狀我們認為答案是機制不是工具，那一格就誠實空著。
按開發流程階段找官方做法見 [[topics/coding-workflow-guide]]；做法背後的機制與實測見 [[topics/community-tech-patterns]]；概念辯論見 [[topics/community-tech-discussions]]；同一個痛點官方補了沒見 [[topics/official-community-gap]]；官方功能見 [[feature-radar]]。[[topics/skill-interest-watch]] 是這張決策表的每日副本，外加各類 GitHub 規模榜——判斷只寫在這一頁，想知道某一類現在誰大、本週誰在漲就去那邊。
```

> **〔併〕-1** 末句改：`…官方功能見 [[feature-radar]]。各類工具現在誰大、本週誰在漲的 GitHub 規模榜見 [[topics/skill-interest-watch]]；該裝哪個只有這一頁有答案。`

## A-4 `## 我卡在這裡` 整節（取代 L48–L84）

**節名一字不改**（`review-registry.json:107`、`check_tools_page.py:32`、`skill_interest_snapshot.py:167` 三方凍結）。表頭四欄與分隔列照舊（`skill_interest_snapshot.py:248` 寫死四欄）。十列的**症狀欄**除新列外一字不改。

```markdown
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
- **「CLAUDE.md 不聽」沒有工具首選是結論不是留白**：dev.to 一手實作（08-25）顯示**以 hooks 強制執行取代 prompt 建議後，規則遵循率達 100%**——答案是機制不是工具，做法見 [[topics/community-tech-patterns]]。四個失效機理中只有後三者是工具能解的：規則被機率性忽略且無反饋、規則越多越貴（Writ 以語意檢索只注入相關規則）、規則腐化（Patina 偵測）、跨工具碎片化（Caliber 統一管理）。
- **接手大 repo 的分界**（09-03 補寫）：graphify 給 **agent** 用（本機 AST、免向量 DB，`/graphify` skill）；同組另三個解的是不同工種——Understand-Anything 給**人**探索、archify 給人**交付圖**、codegraph 是 graphify 的競品（自動同步索引，僅星數證據）。官方面的「接手大 repo 第一步」（先讀 CI、從子目錄啟動、LSP）在 [[topics/coding-workflow-guide]] 第 2a 段：官方設定先做，索引工具再裝。
- **三個首選換了門牌**（09-22 查證）：Harness → [ness](https://github.com/ness-dev/ness)、Omar → [omar-os/omar](https://github.com/omar-os/omar)（官網也從 omar.tech 改成 omar.rs）、Cockpit → [episko](https://github.com/respeak-io/episko)。舊網址目前還會自動轉，但作者一關轉址就失效。
- **多 agent 互踩的首選為什麼不換**：ness 09-22 查得 99★／13 forks，自述已從 CLI 變成「給 agent 用的 IDE」（徽章隨之從 ⌨️ 改為 🖥️），但 README 仍寫可同時跑十個 Claude，仍解同一個症狀，故不換首選。
- **這一列的兩個次選**：omnigent 09-22 查得 10,150★／1,609 forks（15.9%，防刷結論不變），但仍沒有任何第三方實測回報，只有規模；另有一個同名的 `revfactory/harness`（9,051★）是設計 agent team 的 meta-skill，不是首選那個。
- **監看首選的分界**：HUD 經官方 JSON event stream 運作、不額外耗 token（08-07），適合小規模；Omar 的「管到 100 個 agent」是 05-02 當時的宣稱，現版自述已改成形式化編排、09-22 查得 48★——兩個選項都很小，裝前自己看一眼活躍度。
- **額度告警：官方只能被動查**。`/usage` 看得到用量條、狀態列讀得到百分比，但不會主動叫你；官方 CLI 主動告警的需求（issue #13585，👍 124）到 09-22 仍未處理，另一條同類需求 #65292 已被官方標為不做。官方到 09-22 沒有這個功能，[[feature-radar]] 上也還沒有對應條目；有了會記在那裡。
- **額度告警的三個候選都只有星數**：Claude-Code-Usage-Monitor 8,713★ 但 2026-07-05 後未更新（表上已標）；usage-monitor-for-claude 293★、09-13 仍在更新但只有 Windows；claude-usage-widget 53★、09-21 仍在更新、跨平台，規模最小但最新。三者都未見第三方實測。
- **額度告警這一列的其他選項**：CCLimitPing（45★、09-14 仍在更新）解的是「額度一解封就自動接著跑」不是提醒，要它去下面目錄拿連結；目錄裡還有一個 2026-05-18 收錄的 agent-baton，宣稱在觸及上限前主動告警並轉移工作，但只有 Reddit 貼文、09-22 查不到可裝的頁，所以沒放進上面三格。
- **Groundtruth 只有 7★ 為什麼還是首選**：值錢的是它的做法（Stop hook 逼 agent 先出示可驗證證明才准說做完），不是使用人數；09-22 查得 7★／0 forks、07-20 後未更新，次選 Proof Loop 11★。沒有更強的替代出現前不換。
- **clarp 的政策風險**（05-21 收錄）：以本地 PTY＋唯讀 API 代理規避 6/15 起的計量計費，屬計費規避而非最佳化；企業環境安裝前先確認與 Anthropic 合約條款的相容性。
- **記憶類的分界**：brain.md 零依賴、純檔案（08-25，552★）；OzBrain 走團隊共享知識庫，是付費服務（免費 50 篇，Pro 每月 20 美元、Max 99 美元，09-22 查證）；VIR 直接萃取 session 檔進 Obsidian vault（05-23）。單機選檔案式，跨人選共享式。
- **有三個次選只有社群貼文、沒有可裝的頁**：Writ、Caliber、claudely 到 09-22 都找不到公開 repo 或產品頁，列在這裡是因為讀者提過這些需求，不是因為我們確認過它們還在。

### AI 寫久了人會不會退化（只有現象，還沒有能推薦的工具）

- 2026-04～05 被反覆提起的四個現象：**技能退化**（不再獨立解題，調試能力萎縮）、**命名漂移**（同概念出現四個名字）、**架構邊界侵蝕**（為讓測試通過直接跨邊界）、**無法獨立 debug**（程式在跑但沒有心智模型）。
- 當時被點名的幾個嘗試（`recap`、`modularity plugin`、`Mneme`）都沒累積出實測，所以上面的決策表沒有這一列。
- 官方公開方向（加速使用、更長自主 agent）與這些擔憂反向，短期不會主動回應；官方與社群的完整對照見 [[topics/official-community-gap]]。
```

> 三條「前三名」推薦細節（L68／L69／L70）**一字不改**貼回原位——它們在 `data/cell-limit-baseline.json` 內，指紋是內容雜湊，改寫即掉出基線、仍 >200 字元就會把閘弄紅，而內容今日仍成立。

## A-5 `## 🧩 Skills 速查` 與 `## 指標說明` 的六處替換

**（1）Codebase 理解組四列的證據欄**（取代 L96／L97／L98／L99 的第二格，第一格與第三格不動；L99 的 `npx skills add tt-a1i/archify -g` 保留）：

```markdown
| 🟢（判 05-02 起多來源，當時 40k★＋作者宣稱 71×；查 09-22，12.0 萬★、`/graphify` skill、本機 AST 免向量 DB） |
| ⚪（判 09-02 讀者提問查證；查 09-22，71,801★、forks 4,612、仍在更新） |
| ⚪（判 09-02 讀者提問查證；查 09-22，83,707★、forks 7,057） |
| ⚪（判 09-02 讀者提問查證；查 09-22，69,632★、forks 4,670、20 天內漲六成） |
```

**（2）移除 L108**（`| **awesome-ux-skills** | 🟡（05-08） | Nielsen＋Shape of AI 等 UX 原則技能集 |` 整列刪除，該組 5 → 4 列）。

**（3）取代 L129**：

```markdown
> Sx 2.0（skill 分享工具）與 awesome-llm-apps（百餘款應用的清單）都不對應上面任何一個用途，兩者在下方工具目錄裡；只想看哪一類現在最大，見 [[topics/skill-interest-watch]]。
```

**（4）取代 L137–L140 四列**：

```markdown
| **證據**（上方兩表） | 🟢 多來源實測 / 🟡 單一實測 / ⚪ 僅星數（未經行為佐證）；決策表括號內「判」是下判斷那天、「查」是最近一次確認專案還在的那天 |
| **採用**（下方目錄） | ✅ 廣泛採用（要有多個獨立使用回饋，不是只有星數）/ ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑 / ❌ 已放棄——與證據等級**不同軸** |
| **類型** | 多 Agent / 記憶工具 / 費用監測 / 工作流 / 整合工具 / 搜尋/診斷 / 安全工具 / IDE/終端 / Skills / 模型路由 / UI 工具 / 其他 |
| **入選標準** | HN score ≥ 30 或評論 ≥ 5 / Show HN 投稿 / 同日 2 個獨立來源；沒有公開 repo、示範站或任何可點的連結就不列——讀者裝不了的東西不該佔一列 |
```

**（5）`## 工具目錄` 節名下、表格上插一行**：

```markdown
這份目錄是上面判斷的底：每一列都點得進去，最早到 2026-04。採用符號與證據是兩條不同的軸，見上方指標說明。
```

**（6）額度告警那一列的四個工具，插在目錄最上方**（首次出現 2026-09-22，倒序後自然排在最前）：

```markdown
| [**jens-duttke/usage-monitor-for-claude**](https://github.com/jens-duttke/usage-monitor-for-claude) | 費用監測 | ⏳ | 2026-09-22 | Windows 工作列常駐的額度監看器，可自己設到幾 % 就跳提醒；293 星、53 forks、09-13 仍在更新（查證日 2026-09-22，來自讀者提問） |
| [**Maciek-roboblog/Claude-Code-Usage-Monitor**](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 費用監測 | ⏳ | 2026-09-22 | 跨平台額度監看與用盡時間預測，額度將滿時出警告；8,713 星，2026-07-05 後未更新（查證日 2026-09-22，來自讀者提問） |
| [**wavever/CCLimitPing**](https://github.com/wavever/CCLimitPing) | 費用監測 | ⏳ | 2026-09-22 | 5 小時限制解除的瞬間自動送出 continue，省掉盯盤等待；45 星、09-14 仍在更新（查證日 2026-09-22，來自讀者提問） |
| [**bozdemir/claude-usage-widget**](https://github.com/bozdemir/claude-usage-widget) | 費用監測 | ⏳ | 2026-09-22 | 跨平台額度小工具，接近上限時跳提醒；53 星、09-21 仍在更新（查證日 2026-09-22，來自讀者提問） |
```

## A-6 目錄十列改寫、43 列移除、六列倒序移位

移除清單與豁免理由見 map；十列改寫的逐字：

**只換第一格 URL 的三列（其餘四格逐字沿用原頁，以下為可直接貼上的整列）：**

```markdown
| [**Frugal Tokens**](https://github.com/dpclark4/frugal-tokens) | 費用監測 | ⏳ | 2026-08-19 | 探索跨 coding agent（含 Claude Code）的成本與用量，含 cache miss 對花費的影響；Show HN score 33，多家報導 |
| [**Graft**](https://github.com/trailhq/Graft) | 費用監測 | ⚠️ | 2026-08-15 | Claude Code hooks 削減 grep 輸出 token，宣稱降幅 42%（HN 39，跨 2 來源）；HN 討論串質疑 README 的 benchmark 段落疑似 AI 代寫，數字未經第三方覆核 |
| [**Workweave Router**](https://github.com/weave-os/router) | 模型路由 | ⚡ | 2026-06-27 | 成本感知模型路由器，作為 Anthropic/OpenAI 相容 endpoint 運作，依請求難度自動路由模型；起因 Opus 4.7 tokenizer 改版後成本大漲；實測成本降 40%+；Show HN score 181 |
```

**整列換掉的七列：**

```markdown
| [**omnigent**](https://github.com/omnigent-ai/omnigent) | 多 Agent | ⏳ | 2026-08-05 | harness 無關 meta-harness，換底層 agent（Claude Code／Codex／Cursor／Pi）不必重寫協作邏輯；2026-09-22 查得 10,150 星、forks 15.9% |
| [**episko**](https://github.com/respeak-io/episko)（原名 Cockpit） | 多 Agent | ⏳ | 2026-08-02 | Rust 打造的 Claude Code 多 Agent 監控主控台，彙整多個 agent／session／專案執行狀態於單一介面；HN score 11，2026-09-22 查得已改名並發到 v0.30.0 |
| [**Omar**](https://github.com/omar-os/omar) | 多 Agent | ⚡ | 2026-05-02 | 統一管理多個 Claude Code agent 的編排工具；05-02 收錄時的說法是「TUI 儀表板管到 100 個 agent」，2026-09-22 查得網域改為 omar.rs、repo 48★，自述已改為形式化編排 |
| [**graphify**](https://github.com/Graphify-Labs/graphify) | 記憶工具 | ✅ | 2026-05-02 | Leiden 偵測建程式碼知識圖譜，作者宣稱 71 倍 token 減少（05-02）；2026-09-22 查得 12.0 萬★、11,626 forks |
| [**ness**](https://github.com/ness-dev/ness)（原名 Harness） | 多 Agent | ⚡ | 2026-04-29 | 多 Git worktree 並行管理多個 Claude Code agent；2026-09-22 查得已改名 ness、99★，自述改為「給 agent 用的 IDE」，README 仍寫可同時跑十個 Claude |
| **claudely** | 多 Agent | ⚡ | 2026-05-04 | 保留 Claude Code 生態的前提下切換至 Ollama/LM Studio/llama.cpp，無需改主配置；2026-09-22 查不到公開 repo 或產品頁 |
| **Caliber** | 工作流 | ⚡ | 2026-05-02 | 跨工具 AI config 統一管理（CLAUDE.md/.cursor/rules/AGENTS.md）；05-02 記到 888 stars，2026-09-22 查不到公開 repo 或產品頁 |
```

> 倒序移位六列（L158／L188／L190／L195／L207／L209）**內容一字不改**，只依「首次出現」欄由新到舊重排整表；實測重排後 20 行的相對位置改變。

## A-6b 目錄裡的八處內部用語（逐字替換，其餘格不動）

| 原文 | 改成 |
|---|---|
| `11,149 星（存量盤點）` | `11,149 星` |
| `3,023 星（存量盤點）` | `3,023 星` |
| `3.03 萬星（存量盤點）` | `3.03 萬星` |
| `9.3 萬星，2025-08-31 出生，本庫首次收錄` | `9.3 萬星，2025-08-31 出生` |
| `9.2 萬星，2026-02 出生，僅星數佐證未另查證` | `9.2 萬星，2026-02 出生，只有星數佐證` |
| `累計 27.9 萬星，2025-10 出生，本庫今日首次收錄；僅星數佐證，forks／issues 未驗證，惟已見於 Reddit 使用者抱怨（間接證明有實際採用）` | `累計 27.9 萬星（08-28），2025-10 出生；只有星數佐證，forks／issues 未查，但 Reddit 上已見使用者抱怨，間接說明真有人在用` |
| `1.4k 星／188 forks，達廣泛採用（非 pipeline 進料，人工查證收錄）` | `1.4k 星／188 forks，有多個獨立的實際使用回饋` |
| 收錄註記 gstack 那條的 `增速明顯快於同類存量盤點案例` | `增速明顯快於同期其他大型專案` |

> 冷讀者的內部用語表逐行點名這幾處（「存量盤點」「本庫」「pipeline 進料」是純內部流程名）。**`check_reader_language.py` 的禁詞清單抓不到它們**——閘擋的是 ingest／lint／派工那一組。改完全頁 `存量盤點`／`本庫`／`pipeline 進料` 皆為 0 次（實測）。「查證」「收錄」兩詞在頁面其餘位置仍是合法用語，不一併掃。

## A-7 ⟨Q-01⟩ 降為普通散文（取代 L305–L306，並同批改 L124／L212）

```markdown
**一則細節**
- **Geosql 的「4 倍」只在連 Dekart 時成立**（2026-08-13 查證）：GeoSQL 讓 agent 把查詢結果經 Dekart 渲染成地圖、回看修正幾何錯誤；沒連 Dekart 時表現與一般 SQL agent 相當，先前細部數據加總不一致就是這個原因（[dekart.xyz 部落格](https://dekart.xyz/blog/claude-code-vs-aino-geospatial-agent/)、[Show HN](https://news.ycombinator.com/item?id=48829242)）。
```

同批改兩處指路（其餘文字不動）：
- L124 速查列：`…4 倍提升僅在連 Dekart 時成立` → `…4 倍提升僅在連 Dekart 時成立（見下方細節）`
- L212 目錄列：`「4 倍效能提升」機制已查證，見下方懸置細節 ⟨Q-01⟩（HN score 55）` → `「4 倍效能提升」機制已查證，見下方 Geosql 那則細節（HN score 55）`

> `iter_pending()` 對本頁回 **0 筆**（實測）——⟨Q-01⟩ 屬舊字樣殘餘，不計入 114 筆新語法標記，本次降級不動基線 106。指向 [[topics/community-tech-discussions]] 的那一句因改寫而消失，該頁在 L44 出口串仍有一條邊，非孤兒。

## A-8 `## 參考來源`（在 L315 之前插入兩條，原四條不動）

```markdown
- [[topics/skill-interest-watch]] — 這張決策表的每日副本，外加各類 GitHub 規模榜
- [[topics/community-large-codebase-workflow]] — 大型 codebase 的四條做法主線，每條線都指回本頁的症狀列
```

> **〔併〕-2** 第一條改為：`- [[topics/skill-interest-watch]] — 各類工具的 GitHub 規模榜（誰大、本週誰在漲）`

---

# B. 進規則檔

## B-0 `data/skill_interest_watch.json` 第 121 行 `caveat`（**連帶改動**，與頁面同批）

本頁砍掉 L71 的「Harness 同名提醒」、把事實接進推薦細節後，這個設定檔仍逐字留著舊 owner；`skill_interest_snapshot.py:249–250` 每天把它原樣印進總覽頁（現行 `skill-interest-watch.md:196`），而 `revfactory/harness` 仍在榜（`:202`）。`weekly.md:29` 明訂社群記者維護的就是這個設定檔（`tools_symptom`／`tools_note`／`caveat`），**不是改機器頁本身**——本波由實作者直接改設定檔，隔天的快照自動跟上。

整串替換 `categories[orchestration].caveat`：

```json
"同名提醒：決策表首選已改名 ness（ness-dev/ness，原名 Harness，多 worktree 並行管理）；榜上的 revfactory/harness（設計 agent team 的 meta-skill）不是同一個專案，裝前認清 owner。"
```

可驗：`grep -c frenchie4111 data/skill_interest_watch.json` ＝ **0**；`python scripts/check_tools_page.py` 的榜橋對帳仍 ✅（`tools_symptom` 五個字串未動，`caveat` 不在對帳範圍）。

## B-1 `.claude/reporter-rules/community/weekly.md`：決策表的時鐘

**放在「community-tech-tools 結構」節的「首選維護鐵則」三條之後（現 L21 之後），新增第四條：**

```markdown
- **證據欄帶兩個日期**：`判`＝下這個判斷的那天（不因時間改變），`查`＝最近一次確認該專案還在不在、規模多大的那天。`查` 由你在每輪策展時更新：**每輪至少把「判」距今最久的三列拿去 `gh api repos/<owner>/<repo>` 對一次**（星數、最後 push、是否改名或 archived），對完就把 `查` 改成當天並把新數字寫進括號。`查` 距今超過 60 天的列，在該輪回報裡列出來；**更新 `查` 不等於更新判斷**——首選是否更換仍照上面第一條（只在新證據時換）。頁面上只留讀者語言的一句「最後一次確認寫在證據欄的**查**」，本條文不上頁。
```

**同節「首選維護鐵則」第一條之後，補一句界定什麼算新證據：**

```markdown
  （改名、轉手、換網域、星數增減、長期沒人回訪**都不算**否定證據，只更新描述與連結。一手自述變動要分兩種：**自述已不再解這個症狀**＝否定證據，照上面第一條換首選；**自述仍解同一症狀、只是規模或形態的宣稱變了**＝不換首選，但把證據等級降到新宣稱撐得起的那一級，並在推薦細節寫明原宣稱哪一句已不在一手。2026-09-22 的 Omar 屬後者：「TUI 管 100 個 agent」在現版 README 已不存在，🟢 降 🟡，首選不動。）
```

**同節表格 `## 我卡在這裡` 那一列的紀律欄末（現 L13），補第三欄的欄位契約：**

```markdown
；第三欄的每個工具比照第二欄帶連結，並在推薦細節至少有一句寫它的證據強度——對已做過前置工作的讀者，第三欄才是主答案
```

## B-2 `.claude/reporter-rules/community/weekly.md`：目錄列的可達性與 `⚡` 的鐘

**放在「community-tech-tools 策展規則」第 4 條（汰除）之後，作為第 4b 條：**

```markdown
4b. **可達性**：目錄列一律要有可點的連結（repo、產品頁、示範站或原始貼文擇一）。第 2 條的排除條款（「無公開 repo / demo / 連結」不收錄）**回頭適用於存量列**：發現無連結的既有列，先花一次查證補上連結；補不上就移除該列（git history 留存，且多數在 `wiki/log.md` 或 archive 頁另有出處，移除前逐列確認過再動）。**存量首次清理得批次處理，逐列確認另有出處即可，不必逐列補查。** 決策表首選／次選的目錄列照第 4 條豁免，但要在簡介末寫一句「YYYY-MM-DD 查不到公開頁」，不留白裝正常。本條與第 4 條分工：第 4 條管「還在不在被人用」（❌／>30 天仍 ⏳），本條管「讀者點不點得進去」，兩者各自獨立成立即可移出。2026-09-22 第 15 波依本條一次清掉 43 列（152 → 113）。
4c. **`⚡` 的鐘**：`⚡` 過去無任何移出條件，80 列裡 74 列停在 2026-04／05。兩個訊號**同時**成立才移出：①首次出現距今 > 120 天；②`python scripts/news_mentions.py --since 8w "英文名" "中文譯名"` 零命中。決策表首選／次選豁免（同第 4 條）。一輪最多移出 10 列，剩下的下一輪再跑——避免一次清空讓讀者感到整頁被掏空。
```

## B-3 `.claude/reporter-rules/community/weekly.md`：`✅` 怎麼給

**`weekly.md` L40 是一整行（`**欄位**` 與採用符號寫在同一行），照字面取代末句會留半句殘骸。做法：L40 整行改為下面第一段，再把第二段當成它底下的一層子條列插進去（原 L41 的去重子條列保持在最後）。**

```markdown
3. **欄位** `| 工具 | 類型 | 採用 | 首次出現 | 簡介 |`：有 URL → `[**Tool**](url)`，URL 從日報原文擷取；採用預設 `⚡`，score ≥ 100 或評論 ≥ 20 維持 `⚡`
   - `✅` 要有**採用的證據**而不只是規模：至少兩筆獨立的實際使用回饋（他人文章、Reddit／HN 留言、明確的下游依賴），或 forks/stars 比例與活躍 issue 顯示真有人在用。只有星數一律不給 `✅`。給 `✅` 的列在簡介裡寫出那兩筆證據是什麼。既有 `✅` 在每輪被拿去對一手時一併重判（2026-09-22 即依此把 Harness 99★、Omar 48★ 從 `✅` 降為 `⚡`，Claude Usage Widget 因無法辨識是哪個專案而整列移除）。
   - 寫入前查表去重：同名 / 同 URL 已存在則更新該筆，不新增重複列
```

## B-4 `.claude/reporter-rules/community/weekly.md`：驗收自檢加第 4 題

**三件事一起做：① 節名（L153）「3 跳自檢題」→「4 跳自檢題」；② L155 正文的「重跑以下 3 題」→「重跑以下 4 題」；③ 第 3 題之後補第 4 題：**

```markdown
4. 「我是 Max 訂閱，沒有帳單，只想在額度快用完前被提醒」→ 應命中「額度快用完，想在斷線前被提醒」列的單一首選（驗拆痛點：**不得**命中「帳單爆了，看不到錢花在哪」列——兩列答的是事後歸因與事前告警兩件事，2026-09-22 冷讀者即卡在這裡）
```

## B-5 `.claude/reporter-rules/community/weekly.md`：倒序的自查指令

**放在「community-tech-tools 結構」表格 `## 工具目錄` 那一列的紀律欄末（現 L16）：**

```markdown
；倒序不靠眼睛，每輪收工前跑一次自查（把目錄列的「首次出現」欄由上到下取出，逐列比對前一列是否 ≥ 本列；2026-09-22 實測有 6 處違規）
```

---

# C. 不進頁面也不進規則檔，只記 `wiki/log.md`

- 43 列移除的完整名單與同一條理由，以及「43／43 皆另有出處」的機械核對結果。
- ⟨Q-01⟩ 由懸置語法降為普通散文的理由（自述已查證＝已解決態）。
- 新列開列的依據：#13585 OPEN／👍 124 ＋ #65292 not_planned ＋ 冷讀者兩波，達 `weekly.md:43` 的「≥2 筆獨立需求證據」。
- 本波未換任何首選的理由，以及 Omar 證據 🟢 → 🟡 的依據（一手自述不再宣稱該能力）。

---

# 實作單（最終版）

以評審第五節的 16 步為底，把第二輪改寫（🔴-2／🟡-2／🟡-6／🟡-10／🟡-11／🟡-13）合進去。**實作者只看這一張**，逐字內容回上面對應的 A／B 段落取。行號皆為對象頁改動前的原始行號。

0. **`.claude/reporter-rules/community/weekly.md`（B 區，必須與頁面同批）**：B-1（L21 後新增第四條；L19 後補括號，逐字用 **🔴-2 改寫版**；L13 紀律欄末補第三欄契約句）、B-2（L42 後新增 4b／4c，4b 含批次處理句與「與第 4 條分工」句）、B-3（**L40 整行改寫＋子條列**，見 B-3 說明，原去重子條列留在最後）、B-4（L153 節名、L155 正文「3 題」→「4 題」，第 3 題後補第 4 題）、B-5（L16 紀律欄末）。
    驗：`python scripts/check_rules.py` ✅；`grep -c "4b\." .claude/reporter-rules/community/weekly.md` ＝ 1。
1. **`data/skill_interest_watch.json:121` 的 `caveat` 整串替換**（B-0）。驗：`grep -c frenchie4111 data/skill_interest_watch.json` ＝ 0。
2. **標頭 L33–L34** 換 A-1（兩處都填實作當天）；**callout L36–L37** 換 A-2；**摘要 L43–L44** 換 A-3（保守版，不採〔併〕）。驗：`grep -n "本週策展"` 0 命中。
3. **`## 我卡在這裡` 整節（L48–L84）換成 A-4**。A-4 已含第二輪三處改正（新列證據格帶「判｜查」與「07-05 後未更新」、新列第三欄的 claude-usage-widget、ness 徽章 🖥️）。**症狀欄九句一字不改**；表頭四欄與分隔列不動；表上引言已是拿掉 `[[entities/claude-code]]` 的版本。
    驗：`python scripts/check_tools_page.py` exit 0。
4. **推薦細節共 14 條**照 A-4 整段貼（含拆成兩條的 ness／次選、改寫後的官方側句、三候選句與「其他選項」句）。L68／L69／L70 三條**一字不改**。
    驗：`python scripts/check_cell_limits.py --page topics/community-tech-tools` 無新增超限。
5. **速查**：移除 L108 awesome-ux-skills 整列；L96／L97／L98／L99 的**第二格**換 A-5(1) 四句（第一、三格不動，`npx skills add tt-a1i/archify -g` 保留）；L129 換 A-5(3)；L124 末補「（見下方細節）」。驗：該組 4 列、`grep -c user-query` 0。
6. **指標說明 L137–L140** 四列換 A-5(4)。驗：類型列 12 值。
7. **工具目錄**，依序：①節名與表頭之間插 A-5(5) 一句；②移除 43 列（清單見 map，逐列先確認該列確實無任何 `](` 或 `http` 再刪）；③套 10 列改寫——L201／L202／L213 用 A-6 的**整列**版本（只有第一格 URL 不同），其餘七列用 A-6 的整列；④表最上方插 A-5(6) **四列**新列；⑤全表依「首次出現」欄由新到舊重排。
    驗：目錄列數 **113**；「首次出現」欄由上到下遞減，違規 **0**（原 6 處全消）。
8. **A-6b 八處內部用語**逐字替換。驗：全頁 `存量盤點`／`本庫`／`pipeline 進料` 各 0 次。
9. **L305–L306** 換 A-7（`**懸置細節**` → `**一則細節**`，⟨Q-01⟩ 降為普通散文）；**L212** 的「見下方懸置細節 ⟨Q-01⟩」→「見下方 Geosql 那則細節」。驗：全頁 `⟨Q-01⟩` 0 命中；`check_pending_markers.py` 仍印「114 筆（基線 106，未低於）」，**舊字樣維持 41 筆不變**（⟨X-nn⟩ 短標記本就不計）。
10. **`## 參考來源`** 補 A-8 兩條（保守版）。
11. **同維護者回掃**：`wiki/topics/community-large-codebase-workflow.md:63`，「（首選 Harness）」→「（首選 ness，原名 Harness）」，Omar 不動，只改該句。驗：`check_tools_page.py` 的 spoke 對帳仍 ✅。
12. **跨維護者轉知 3 筆**：`python scripts/pending_handoffs.py open --from 社群 --to 功能` ×2（feature-radar 缺額度告警條目／`official-community-gap:78` 的 Throttle Meter 引用）、`--to 主編` ×1（`index.md:27` 補「額度快用完」），內容照 proposal §7。
13. **`wiki/log.md` append**：43 列移除的名單與理由、⟨Q-01⟩ 降級、新列開列依據（#13585 OPEN／👍 124 ＋ #65292 not_planned 兩筆官方 issue 已達 `weekly.md:43` 的 ≥2 筆獨立需求證據；**冷讀者是內部驗收，不計入需求證據**）、本波未換任何首選與 Omar 🟢→🟡 的理由。
14. **跑全部閘，最後一行原樣抄進回報**：
```
python scripts/check_tools_page.py
python scripts/check_cell_limits.py --page topics/community-tech-tools
python scripts/check_reader_language.py --page topics/community-tech-tools
python scripts/check_pending_markers.py
python scripts/gen_wiki_frontmatter.py
python scripts/check_hierarchy.py
python scripts/check_rules.py
python scripts/build_web.py
python scripts/run_tests.py
```
預期：`check_tools_page` ✅；cell 閘 `WARN: 存量基線內 4 筆／1 頁`＋`OK: 無新增超限`（⟨Q-01⟩ 降級後可能顯示 3 筆，同樣算過）；reader 閘 `OK: 無新增命中`；pending `114 筆（基線 106，未低於）`；`check_rules` ✅；`build_web.py` 錨點 WARN 不得增加；`run_tests.py` exit 0。**任一項與預期不符就停下回報，不得自行改任何基線檔。**
15. 完工時對象頁應為 **283 行、目錄 113 列、決策表 10 列、推薦細節 14 條**（設計者在 scratchpad 副本實測值）。

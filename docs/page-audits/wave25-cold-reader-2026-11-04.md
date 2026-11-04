# 冷讀者實測｜第 25 波：企業採用與選型（2026-11-04）

**讀者設定：** 在公司評估 AI 開發工具導入的資深工程師，第一次來，從 `wiki/index.md` 出發只沿 `[[連結]]` 走。

**誠實聲明：** 系統自動把專案根目錄 `CLAUDE.md`（站台目標、架構、三個動作）載進了我的 context，我沒有主動去讀。導航時刻意不用它，只靠 index 與頁內連結走。`wiki/CLAUDE.md`、`wiki/log.md`、`docs/`、`.claude/`、`news/` 都沒讀。讀頁的方式是在單一頁內列標題、用 Ctrl-F 找字。行號一律指原始 .md 檔。

**走過的頁（共 11 頁）：** index → topics/enterprise-tool-tracker → topics/competitor-landscape → topics/enterprise-cost-management → entities/pricing → topics/anthropic-business → topics/anthropic-partnerships-compute → topics/market-signals-customers → topics/anthropic-agent-stack → overview → topics/anthropic-business-risks

---

## 1. 四題逐題

### Q1 哪些大公司公開在用 Claude／Claude Code、用到多大規模？最近有誰減用或退出？

- **路徑：** index:138 → topics/enterprise-tool-tracker
- **跳數：** 1
- **結果：** ✅ 拿到
- **答案在哪：**
  - 在用的規模：enterprise-tool-tracker:46-65（近期新增／擴大）
    - JPMorgan 美國本部約 8,000 人持授權、每人每月上限 $2,000：100、169-170
    - TCS 5 萬員工部署：132
    - Barclays 目標年底開發者採用率 50%：99、168
    - Google 開放全體工程師使用：101
    - Samsung 用在晶片設計：111、177
  - 減用：Meta 的 Claude Code 使用者約 6 萬降到約 3 萬（117、162）；Microsoft 內部 Claude 支出砍掉逾三分之一（118、164-166）；Uber（142）
  - 退出：Goldman 於 11-02 禁用 Claude Code 與 GitHub（36、69、94）；Replit 有爭議（70、95、156-159）；Alibaba（123）；Lindy（124）；JPMorgan 香港（130）
  - 另一個補充數字：overview:10「Claude Code 企業大戶支出為一般用戶 20 倍」
- **卡住的原句：**
  - :40「（最新異動見頂部 callout，2026-10-16）」：callout 寫的是 2026-11-03（:35）。摘要裡的日期沒跟著更新，讓人懷疑 51 家這個計數是不是最新的。
  - :92-152 使用現況表是事件流水帳，同一家公司重複出現：Microsoft 3 列（118／138／139）、Rubrik 3 列（102／125／134）、Goldman 2 列（94／107）、Uber 2 列。想問「這家現在到底是什麼狀態」，得自己把幾列合起來看。
  - :286「Goldman Sachs、OKX 雙雙於香港被切斷……**與 06-18 JPMorgan Chase 香港分行因出口管制退出屬同類案例**」：這句跟同頁 :180 的 ⟨Q-03⟩「兩案不同源……與出口管制無關」互相矛盾，標題「[❌ 新增退出，香港出口管制]」也沒更正。

### Q2 企業在 Claude Code、GitHub Copilot、Cursor、OpenAI Codex 之間怎麼選？現在誰在搶誰的客戶？

- **路徑：** index:138 → enterprise-tool-tracker#工具競爭態勢（企業視角） → topics/competitor-landscape → topics/enterprise-cost-management:50（Ramp 指數）
- **跳數：** 2-3
- **結果：** 🟡 半拿到。「誰在搶誰」拿到了，「怎麼選」沒拿到。
- **答案在哪：**
  - 誰在搶誰：
    - Microsoft 轉向 GitHub Copilot：enterprise-tool-tracker:165、competitor-landscape:177-181
    - Replit 轉向 OpenAI：enterprise-tool-tracker:156-157
    - OpenAI 用「零資料保留」爭奪 Anthropic 企業客戶：competitor-landscape:171
    - Meta Enterprise Platform 把 Muse Code 推給企業：competitor-landscape:149
    - Copilot Fusion 宣稱勝過 Claude Code、API 成本減半：competitor-landscape:52、87-88、179
    - Cursor 推出 SDK：competitor-landscape:57
  - 採用面數字：
    - Ramp 指數 Anthropic 43.5% vs OpenAI 39.7%：enterprise-cost-management:50、anthropic-business:60
    - 各工具的企業採用數：enterprise-tool-tracker:191-197
  - 價格：competitor-landscape:95-109（Cursor、Codex 各級方案）
- **卡住的原句：**
  - competitor-landscape:82「**Codex 和 Claude Code 誰強？** 沒有單一答案」：「硬答案」一節沒有任何一條從企業採購的角度回答（管控、資料保留、席位價、合規）。
  - enterprise-tool-tracker:195-197「GitHub Copilot｜1（Microsoft）…OpenAI Codex｜2（Amazon、UiPath）…Cursor｜1（Uber）」：樣本只有 1-2 家，撐不起「選型」。而且 Codex 漏算了 Epic Games（:98 明寫 Claude Code ＋ Codex）。
  - Cursor 在雷達表裡（competitor-landscape:57），但「雷達細節」只為 🔴 級開節（:134），所以 Cursor 沒有自己的一節。企業最常拿來對比的四家裡，Cursor 的資訊最薄。
  - index:122 competitor-landscape 的鉤子寫「Meta 三層訂閱打價格戰 + 中國陣營…」，完全沒提 Copilot、Cursor、Codex。單看 index 不會想到要點進這頁問 Q2。

### Q3 我公司要導入 Claude，別家踩過哪些坑（支出上限、席位門檻、帳務、管控）？

- **路徑：** index:137 → topics/enterprise-cost-management → entities/pricing（#我的方案現在有什麼、#額度與通路的帳務坑、#方案可用性與帳務摩擦）
- **跳數：** 2
- **結果：** ✅ 拿到，但要跨兩頁自己拼起來。
- **答案在哪：**
  - 支出上限：
    - Accenture 每月 $29（此前有人單月花到 $1,000）：enterprise-cost-management:120-124
    - JPMorgan 每月 $2,000 ＋ Devspace 沙箱：enterprise-tool-tracker:169-170
    - Uber、Microsoft 燒完全年預算：enterprise-cost-management:166-176
  - 管控：
    - Spend Controls 只限 Enterprise 方案，有警示但沒有自動暫停：enterprise-cost-management:56-63
    - Code Review 可設專屬上限：enterprise-cost-management:109
  - 席位門檻：
    - Team 年繳最低 20 席、Enterprise 20 席起：pricing:72-74、185、282
    - Schwab 通路另有 20 席門檻：pricing:283
  - 帳務：
    - usage credits 一開，方案上限就不再是硬停止：pricing:76
    - 訂閱附的 API credits 不能付 Claude Code：pricing:268-269
    - Azure 市集 $17,600 帳單沒人認：pricing:271-272
    - 新創額度已暫停：pricing:274
    - $1,660 萬帳務錯誤：enterprise-cost-management:274
    - Bedrock 拿不到 Batch 折扣、AWS Start 層月上限 $500：pricing:235-236
- **卡住的原句：**
  - 在 enterprise-cost-management 頁內 Ctrl-F「席位／seat」**0 筆**。這頁的定位是「企業採用 Claude 的成本結構挑戰」，卻完全沒提 Team／Enterprise 的 20 席下限。我是靠 :112 一條順帶的 pricing 連結才找到。
  - enterprise-cost-management:56「2026-07-02 官方 Spend Controls」vs 同頁 :274「Spend Controls（07-04 上線）」、:277「07-04」：上線日期兩說，頁內沒有解釋。
  - enterprise-cost-management:43「現況（2026-10-16 更新）」：Goldman 11-02 的禁令（合規管控型的坑）沒同步過來，這頁只收「錢」的坑，「管控」的坑要回 tracker 找。

### Q4 對要做 agent 產品的人，企業端這些採用趨勢代表該押哪個生態？

- **路徑：** index（找不到對應列）→ enterprise-tool-tracker#對 agent 開發者的選型影響 → competitor-landscape:57（Cursor SDK）→ anthropic-business → anthropic-partnerships-compute#哪個合作會改到你用的 Claude → anthropic-agent-stack → overview → anthropic-business-risks
- **跳數：** 約 7
- **結果：** 🟡 半拿到，偏沒拿到。只有零散的線索，沒有任何一頁做綜合判讀。
- **答案在哪（碎片）：**
  - enterprise-tool-tracker:213-215：只說 Claude Code 與 Claude API 的成本結構不同
  - anthropic-business-risks:53「把關鍵工作流做成換得了模型供應商」
  - overview:18：Agent Skills 捐給 AAIF，逾 70 個平台整合，是 MCP 之後第二個交出去的標準
  - anthropic-partnerships-compute:43-51、101-118：三大雲同時是出資者、通路與對手，通路差異也在這裡
  - enterprise-tool-tracker:140-141、147-148：Amazon、UiPath 雙軌並行，不押單一供應商
  - anthropic-agent-stack 只答「Claude 家內用哪塊積木」（:217），不答跨生態的問題
- **卡住的原句：**
  - enterprise-tool-tracker:215「Claude Code 是工程師日常編碼工具（CLI）……同樣是採用 Anthropic，風險結構完全不同。」：標題是「對 agent 開發者的選型影響」，內容只有兩句成本對比。這頁收了企業多供應商並行、退出理由擴散、OpenAI 爭奪企業客戶這些趨勢，卻沒有在這裡做「所以你該怎麼押」的推論。
  - index 的「💻 開發實務入口」表（:24-40）沒有商業或生態相關的列，Entities／Topics 表的鉤子也沒有「押哪個生態」的字樣。

---

## 2. 入口

| 題 | index 哪一列 | 直覺嗎 |
|---|---|---|
| Q1 | :138 enterprise-tool-tracker「大型企業現在用哪套 AI 編碼工具、換過什麼」 | ✅ 很直覺，鉤子就是題目 |
| Q2 | :138（先進）＋ :122 competitor-landscape | ⚠️ :122 的鉤子是 Meta 與中國陣營的價格戰，不會聯想到 Copilot、Cursor、Codex 的企業選型 |
| Q3 | :137 enterprise-cost-management「成本結構挑戰…缺失工具」 | ✅ 直覺。但「席位門檻、帳務」其實住在 pricing，index:35 只在開發實務入口提到「要花多少」 |
| Q4 | 無 | ❌ 沒有入口。只能猜 enterprise-tool-tracker 或 anthropic-agent-stack（:31 鉤子講的是「自己跑幾小時」） |

整體來看，index 的「💻 開發實務入口」用「我想……」的句型很好用，但**商業與選型這一面沒有對應的「我想……」表**，評估導入的讀者只能逐列掃 Topics 的摘要。

---

## 3. 分不出差別的兩頁

- **topics/enterprise-tool-tracker vs topics/enterprise-cost-management**：Uber、Microsoft、Lindy、Amazon、Accenture 兩頁都有完整段落（tracker:142-143、138、124、140；cost:166-181、201-206、120-124），兩頁 Microsoft 的退出經過幾乎逐字重複。分界應該是「誰在用」對「錢怎麼管」，但讀起來兩頁都在講案例。
- **topics/market-signals-customers vs topics/enterprise-tool-tracker**：同一批事件（Accenture、Replit、Meta／Microsoft、Barclays）都有，而且**狀態不一致**。market-signals-customers:50 把 Accenture、Replit 列為「具名縮減」，tracker 標的是 Accenture ✅ 使用中（:96）、Replit ⚠️ 有爭議（:95）。另外 :50 的 Novo Nordisk 在 tracker 裡找不到。
- （次要）**topics/anthropic-business vs topics/anthropic-partnerships-compute**：母頁 :88-98 已經只剩四個「這一節現在在 X」的殼，第一次來的人會先在母頁撲空。

---

## 4. 每頁判定：百科還是雷達

| 頁 | 判定 | 理由 |
|---|---|---|
| index | 路由 | — |
| topics/enterprise-tool-tracker | 雷達（形式上像百科） | 主表其實是按日期的事件列、同公司多列；時序占 :219-347 |
| topics/competitor-landscape | 雷達 | 對手雷達、本週衝擊、時序約 400 行；「硬答案」與「定價對照」是唯一的百科段 |
| topics/enterprise-cost-management | 混合，偏百科 | 缺口表與策略表是百科，企業案例與時序是雷達 |
| entities/pricing | 百科 | 方案表、通路、乘數、帳務坑都是現在式 |
| topics/anthropic-business | 雷達＋路由殼 | 指標表是百科，其餘多為指路殼 |
| topics/anthropic-partnerships-compute | 百科（兩張表）＋雷達（時序） | — |
| topics/market-signals-customers | 雷達 | 逐則判讀 |
| topics/anthropic-business-risks | 百科偏雷達 | 風險表有「你能先做什麼」 |
| topics/anthropic-agent-stack | 百科 | 八塊積木與選型 |
| overview | 雷達 | 週報式「當前局勢」 |

---

## 5. 內部用語外洩（10 則）

1. entities/pricing:37「拆頁評估 2026-11-02：已拆（第 24 波，`docs/page-audits/ledger.md` 裁決紀錄）」
2. topics/anthropic-business:35「第 23 波……G1 約 65% 是指路句，去重列 /wiki-lint 候選」
3. topics/anthropic-business:99「指路殼四個……有 daily/ 讀者版日報（不可改的過去）錨點指入……（第 23 波 handoff）」
4. topics/market-signals-customers:36「2026-11-02 第 22 波自 [[topics/market-signals]] 拆出……」
5. topics/competitor-landscape:33「拆頁評估 2026-10-31：不拆……2026-08 時段 11 月滿 3 個月後走蒸餾」
6. topics/enterprise-cost-management:45「%% 新類型 2 筆為本輪新增，舊 13 筆分類沿用……待下次週整理覆核 %%」（寫在讀者看得到的表格格子裡）
7. topics/enterprise-cost-management:82「%% （決策表暫無對應列｜候選症狀：企業級成本能見度） %%」
8. topics/enterprise-tool-tracker:42、74、119「見 ⟨Q-03⟩」「⟨Q-01⟩」：沒有圖例說明 ⟨Q-nn⟩ 是什麼，第一次來的人看不懂
9. topics/competitor-landscape:92「數字均回溯 `news/` 原文查證；查無具體公開數字者依懸置標記語法標示」與 :115「（標 2026-08-13｜查…｜複 2026-11-11｜訊 2026-09-06）」：標／查／複／訊是內部語法
10. overview:24「`topics/market-signals` 另清掉 15 處簡體「价」」：站務維護寫進了對外的「當前局勢」

（另外：enterprise-tool-tracker:12-24 frontmatter 的 `page_role`、`signal: "健康"`、`generated_by` 如果網站會渲染，也算外洩。competitor-landscape:128「詳見 [[log]] 該日 Query 條目」把讀者導去 log。）

---

## 6. 撐不起的句子

- enterprise-tool-tracker:197「Cursor｜…｜企業級功能不如 Claude Code」：沒有來源，全頁也沒有任何功能對照。
- enterprise-tool-tracker:196「OpenAI Codex｜2（Amazon、UiPath）｜🟢 快速成長」：2 家（還漏了 Epic Games）撐不起「快速成長」。
- enterprise-tool-tracker:201「採用企業清單（Claude API，31）」：逐一數過，列出的名字只有 **30 個**。
- enterprise-tool-tracker:40「整體趨勢為 Claude API 企業與政府採用持續擴大」：同頁 :33 自己說「非市場全貌」，只靠見報案例做不出趨勢判斷。
- enterprise-tool-tracker:209「新創圈：Business Insider（2026-05-23）確認 Claude Code 已取得主導地位，Cursor 份額下滑」：5 個多月前的單一報導，被當成現況寫。
- enterprise-tool-tracker:286「與 06-18 JPMorgan Chase 香港分行因出口管制退出屬同類案例」：被同頁 :180 的 ⟨Q-03⟩ 推翻了，卻沒有改。
- enterprise-cost-management:50「Anthropic 企業採用率（43.5%…8 月指數）持續領先 OpenAI」：「持續」靠的是 3 個月前的單點指數。
- enterprise-cost-management:274「Anthropic 證實 1660 萬美元帳務錯誤」：只有 Tech Times 一家，沒附官方出處就寫「證實」。
- market-signals-customers:50「具名縮減（Meta、Microsoft、Replit、Accenture 每月 29 美元上限）」：跟 tracker 的狀態判定矛盾，Novo Nordisk 也沒有出處。
- overview:51、106「Q3 營收 168 億」vs anthropic-business:57「$170 億（2026-11-02，官方修訂 S-1）」：兩頁數字不同，也沒說明口徑差在哪。

---

## 7. 最想改的三件事

1. **index 加一張「💼 評估／導入入口」的「我想……」表**，比照開發實務入口：
   - 「誰在用、誰退出」→ tracker
   - 「四家工具怎麼選、誰搶誰」→ competitor-landscape（補一節企業選型）
   - 「導入前要知道的坑」→ enterprise-cost-management ＋ pricing#方案可用性與帳務摩擦
   - 「做 agent 產品該押誰」→ 新節
   
   同時改寫 :122 competitor-landscape 的鉤子，點名 Copilot、Cursor、Codex。
2. **enterprise-tool-tracker 分成兩層，並補上生態判讀：**
   - 頂端放「一家一列、現在狀態」的精簡表，合併 Microsoft、Rubrik、Goldman、Uber 的重複列；事件明細往下移
   - 修 :40 的日期、:201 的計數、:286 跟 Q-03 的矛盾，刪掉或補來源給 :196-197、:209
   - 把 :213-215 擴成真正的「對 agent 開發者：該押哪個生態」，整合多供應商並行（Amazon、UiPath）、risks:53 的「做成換得了供應商」、overview:18 的開放標準（MCP、Skills 交給 AAIF）、partnerships-compute 的三大雲角色，以及 Cursor SDK、OpenAI 的企業攻勢
3. **enterprise-cost-management 頁頂加一份「導入前檢查清單」**，把散在 pricing 的坑收成一處、各給連結：
   - 20 席下限
   - Spend Controls 只限 Enterprise、沒有自動暫停
   - usage credits 不是硬停止
   - 訂閱附的 API credits 不付 Claude Code
   - 雲端市集帳務沒人認
   - 合規禁用案（Goldman）
   
   同時清掉頁內三處 `%%` 備忘外洩（:45、:65、:82），統一 Spend Controls 的上線日（07-02 或 07-04）。

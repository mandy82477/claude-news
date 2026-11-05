# 冷讀者複驗（wave 25）— 企業採用四題｜2026-11-05

**聲明：** 開工時系統自動把專案根目錄 `CLAUDE.md` 載入 context（內容含「wiki 三動作」「Query 六路」等站內說明）。我沒有依它去讀任何 `wiki/` 以外的檔，也沒用 Grep 跨頁搜尋；只從 `wiki/index.md` 出發沿 `[[連結]]` 走，單頁內只用列標題與頁內找字。行號都指原始 .md 檔。

**實際開過的頁（9 頁）：** `index`、`topics/enterprise-tool-tracker`、`topics/competitor-landscape`、`topics/enterprise-cost-management`、`entities/pricing`、`topics/ai-agent-safety-product-vulns`、`topics/anthropic-business-risks`、`overview`、`topics/anthropic-partnerships-compute`

---

## 1. 四題逐題

### Q1 哪些大公司在用、規模多大；誰減用或退出 — ✅ 拿到

- **路徑：** index → topics/enterprise-tool-tracker（**1 跳**）
- **答案在哪：**
  - enterprise-tool-tracker:42：48 家，各狀態各幾家
  - enterprise-tool-tracker:44：退出理由分兩類
  - enterprise-tool-tracker:54-103：一家一列的表，有規模數字：TCS 5 萬人（:92）、JPMorgan 8,000 人持授權（:67）、Meta Claude Code 用量 6 萬→3 萬（:64）、Microsoft 支出砍逾三分之一（:65）、Barclays 目標 50%（:66）
  - 時序裡的拆解：:157-163
- **卡住的地方：** 沒有真正卡住。只有兩點小摩擦：
  - :56 Goldman 標了 ❌，但同列寫「範圍與生效時間未見」，時序 :132 又寫「僅標題可用」。讀者會問：一則只有標題的報導，就夠把狀態判成「已退出」嗎？
  - 「與 GitHub」被一起禁是什麼意思（:56），頁內沒解釋。

### Q2 Claude Code／Copilot／Cursor／Codex 怎麼選、誰在搶誰的客戶 — ◐ 半拿到

- **路徑：** index → enterprise-tool-tracker（:123 指過去）→ topics/competitor-landscape，期間回 tracker 對照（**2 跳**）
- **答案在哪：**
  - 誰搶誰：
    - Microsoft 內部轉用 Copilot（tracker:65、:161；competitor:177-181）
    - Replit 執行長說轉向 OpenAI（tracker:60、:141-144）
    - OpenAI 用「零資料保留」爭取 Anthropic 的企業客戶（competitor:171）
    - Copilot Fusion 宣稱贏過 Claude Code（competitor:52、:87）
  - 價格：competitor:102-108 列了 Cursor、Codex 的方案。但 Claude 的價格要另去 pricing 頁查，而且這張表裡訂閱制的欄位都標「不可比」。
  - 大公司多半同時用兩家以上：tracker:119
- **卡住的原句：**
  - competitor:82「**Codex 和 Claude Code 誰強？** 沒有單一答案——不同基準測不同能力面向」：沒有給企業看的判斷維度，例如管控、資料保留、席位價、IDE 綁定。
  - competitor:134「只為衝擊度 🔴 的對手開節」：Cursor 只拿到 🟡（:57），所以**四家裡唯一沒有詳細小節的就是 Cursor**，企業版功能和客戶都查不到。
  - competitor:43 摘要寫的是 Meta、Google、中國的價格戰，完全沒提 Copilot、Cursor、Codex 這三家企業最常拿來比的對手。

### Q3 導入 Claude 別家踩過的坑（支出上限、席位門檻、帳務、管控）— ✅ 拿到（散在 4 頁）

- **路徑：** index → enterprise-tool-tracker（:120-121）→ topics/enterprise-cost-management → entities/pricing（cost:221）；另從 tracker:121 → topics/ai-agent-safety-product-vulns（**4 跳**）
- **答案在哪：**
  - 支出上限：
    - 各家上限：Accenture $29（cost:120-123）、JPMorgan $2,000（tracker:67、:172）、Uber 燒光預算（cost:166-170）
    - 官方 Spend Controls 只給 Enterprise 方案，而且超過上限也不會自動暫停（cost:56-62）
  - 席位門檻：Team 年繳 20 席起、Enterprise $20／席、20 席起（pricing:72-74、:82、:185）；Schwab 那條通路的 20 席是另一回事（pricing:283）
  - 帳務：訂閱附帶的 API credits 不能付 Claude Code（pricing:268-269）；Azure 市集 $17,600 帳單（pricing:271）；新創方案已暫停（pricing:274）
  - 管控：covered models 保留 30 天、ZDR 工作區也一樣（vulns:396-397）；Palantir 要求零資料保留（tracker:57）；JPMorgan 用 Devspace 沙箱隔離（tracker:173）；Code Review 可以設封頂（cost:109）
- **卡住的原句：**
  - cost:82「**部門層級預算管控**則現有社群工具全是個人視角，本頁四缺口的企業面仍待官方 Spend Controls 細節」。這和同頁 :56-60 打架：那裡說 Spend Controls 已經有部門層、三項已結案。讀者不知道該信哪段。
  - 席位門檻與帳務坑在 pricing，cost 頁只在 :221 留一行「Anthropic 定價政策」。index:137 的鉤子也沒提席位或帳務，所以第一次來的人不會知道要去 pricing 找。

### Q4 要做 agent 產品的人該押哪個生態 — ◐ 半拿到（要自己拼）

- **路徑：** index → enterprise-tool-tracker（:115「對 agent 開發者的選型影響」）→ topics/anthropic-business-risks（tracker:122）；另從 index → overview；再從 tracker:105 → topics/anthropic-partnerships-compute（**5 跳**）
- **答案在哪（全是碎片）：**
  - 大公司不押單一供應商：tracker:119
  - 可用性不由你決定，要先備好能換供應商的工作流：tracker:122，但標了「推論」
  - 要把關鍵工作流做成能換模型供應商：business-risks:51
  - Agent Skills 已交給基金會治理，標準不再由單一廠商決定：overview:18
  - Cursor 把自家 agent 包成 SDK：competitor:57
  - 三大雲同時是出資者、通路和對手：partnerships:46-50
- **卡住的原句：**
  - tracker:117「退出不等於 Claude 不好用」與 :122「先備好換得了供應商的工作流（推論…）」已經是最接近答案的句子，但**全站沒有一段直接回答「做 agent 產品該押誰」**。
  - index 沒有任何一列對應這題，index:31 的 anthropic-agent-stack 講的是官方積木怎麼選，不是押哪個生態。

---

## 2. 入口

| 題 | index 哪一列 | 直覺嗎 |
|---|---|---|
| Q1 | :138 enterprise-tool-tracker「哪些大企業在用、減用或退出 Claude」 | ✅ 很直覺，幾乎是題目原文 |
| Q2 | 沒有直接的列。:122 competitor-landscape 的鉤子是「Meta 三層訂閱打價格戰＋中國陣營」，看不出 Copilot、Cursor、Codex 在裡面；最後是從 tracker:123 進去的 | ❌ |
| Q3 | :137 enterprise-cost-management「成本結構挑戰：Uber/Microsoft 案例、缺失工具」 | △ 支出上限找得到；席位和帳務要靠頁尾的連結轉到 pricing（:57），而 :57 的鉤子沒寫「席位門檻」 |
| Q4 | 沒有 | ❌ 只能先猜 tracker 或 overview |

## 3. 分不出差別的兩頁

**topics/enterprise-tool-tracker 與 topics/enterprise-cost-management**

- 兩頁各自完整寫了同一批公司：Uber（tracker:97／cost:166）、Microsoft（:65／:172）、Lindy（:86／:201）、Amazon（:100／:178、:195）、Accenture（:61／:120）、JPMorgan $2,000（:67／cost:123）。
- tracker:28 說「帳單怎麼控在 cost 頁」，但 tracker:120 自己就有一整段支出上限的結論。
- cost 頁的「企業案例」節其實就是另一份採用表，再加上個人開發者的案例。

次要的一對：entities/pricing 的「方案可用性與帳務摩擦」（:277-284）與 cost 頁，兩頁都在答「導入要注意什麼錢的事」。

## 4. 每頁判定

| 頁 | 判定 | 理由 |
|---|---|---|
| index | 路由 | — |
| topics/enterprise-tool-tracker | **百科** | 一家一列的現況表，時序附在後面 |
| topics/competitor-landscape | **雷達** | 衝擊度排序，本週衝擊放在最前面 |
| topics/enterprise-cost-management | **百科（但寫法像雷達）** | 案例都帶「（YYYY-MM-DD 新增）」，摘要停在 Uber 05-17 |
| entities/pricing | **百科** | — |
| topics/ai-agent-safety-product-vulns | **雷達** | 按日期新增的事件流 |
| topics/anthropic-business-risks | **雷達** | 按最後動態排的風險表 |
| overview | **雷達** | 週更局勢 |
| topics/anthropic-partnerships-compute | **百科** | 「跟三大雲各是什麼關係」是穩定的對照表 |

## 5. 內部用語外洩（10 則）

如果 `%%…%%` 在網站上會顯示，下面幾則都會被讀者看到；就算不顯示，:262、overview:24 也是正文。

1. competitor-landscape:262「是否開『對手雷達』新列待**主編裁示**：表已滿 12 列、無 ⚪ 可汰，**記者**不自行汰除 🟡」
2. competitor-landscape:128「單一外部來源、**非日報進料**，使用者 2026-07-17 手動查證，詳見 [[log]] 該日 **Query 條目**」
3. competitor-landscape:92「數字均回溯 `news/` 原文查證；查無具體公開數字者依**懸置標記語法**標示」
4. competitor-landscape:71「（**標** 2026-10-05｜**查** GLM-5.3、雙重背書｜**複** 2026-11-24）」：標／查／複的縮寫全頁沒解釋
5. overview:24「`entities/pricing` 的『通路與乘數』對官方計價頁重查後改兩項…`topics/market-signals` 另**清掉 15 處簡體『价』**」：這是維護紀錄，不是給讀者看的局勢
6. entities/pricing:37「%% 拆頁評估…已拆（**第 24 波**，`docs/page-audits/ledger.md` 裁決紀錄）%%」
7. entities/pricing:183、:185「（來源：claude.com/pricing，**diff 偵測**，…）」
8. anthropic-business-risks:66「已逾期**待 /wiki-lint 5j 處置**」；:67「2026-11-02 **第 23 波**新進」
9. enterprise-cost-management:45 表格儲存格裡夾著「%% 新類型 2 筆為**本輪新增**…**待下次週整理覆核** %%」；:215「需依 **wiki-lint 3c** 補結論」
10. enterprise-tool-tracker:205「07-06 **日報首提**（未確認）」；index:5-6「盤點用 Grep」「哲學見 `wiki/CLAUDE.md`」

## 6. 撐不起的句子

1. **overview:10 與 anthropic-business-risks:71 金額差兩個數量級，頁內沒有對帳**
   - overview:10：「2026 上半年淨損 **$807 億**」，其中「$720 億是非現金」
   - business-risks:71：「上半年營業層虧約 **6.9 億**、淨損約九成為非現金」
   - 兩個數字差兩個數量級，頁內沒有說明是不是不同指標或單位。
2. **overview 自己前後打架**：:107「（Reuters 獨家，機密草案階段，**公開版 S-1 未遞交**）」，但同頁 :10 說公開版 10-26 已上 EDGAR。
3. **tracker 與 competitor-landscape 對 Microsoft 動機說法相反**
   - enterprise-tool-tracker:117：「『自研夠強所以退』目前沒有證據」
   - competitor-landscape:181：「已查證（09-20）：自研模型取代已獲官方高層證實動機（Suleyman…）」
4. **Goldman 狀態證據不足**：enterprise-tool-tracker:56 只憑一則「僅標題可用」的報導（:132）就把 Goldman 標成 ❌ 已退出。
5. **cost 頁自相矛盾**：enterprise-cost-management:82「部門層級預算管控…仍待官方 Spend Controls 細節」，但同頁 :60 已寫 Spend Controls「＋部門層用量報表」✅。
6. **cost 頁引用過期數據**：enterprise-cost-management:50「Anthropic 企業採用率（43.5%，Ramp 8 月）**持續領先** OpenAI」。用的是 8 月的指數，11 月仍寫「持續領先」。
7. **Spotify 結論超出證據**：enterprise-cost-management:136「量化降幅 90% 恰與…理論上限一致，**屬理論策略的實際落地驗證**」，但同句又承認「僅標題與部落格摘要層級資訊」。
8. **摘要和自己的表不符**：competitor-landscape:43 摘要說「主戰場已從『誰更強』移到『誰更便宜』」，可是 :51-56 六個 🔴 裡有五個衝擊面是「能力」，只有一個是「定價」。

## 7. 最想改的三件事

1. **在 competitor-landscape 補一節「企業怎麼選」**
   - 內容：Claude Code、Copilot、Cursor、Codex 四欄，比較企業方案價、管控與資料保留、IDE 綁定，以及表上哪些具名企業各用哪家，最後一行寫「誰在搶誰」。
   - Cursor 要開詳細小節，不受「只為 🔴 開節」限制。
   - index:122 的鉤子改成會提到這四家。
2. **在 enterprise-tool-tracker 的「對 agent 開發者的選型影響」（:115）加一段收束結論**
   - 回答「做 agent 產品該押誰」：多供應商是常態，雲端通路同時是對手，MCP 和 Skills 已交給中立基金會，可用性可能被地區或政策切斷，並給「要先做到能換供應商」的具體做法。
   - index 加一列「我要做 agent 產品，該押哪個生態」指過來。
3. **把 Q3 收成一份「導入前檢查清單」，放在 enterprise-cost-management 頂端**
   - 清單內容：支出上限、席位門檻、credits 和帳務的坑、資料保留、Spend Controls 只限 Enterprise，每條連到它真正住的那一頁。
   - 同時刪掉 tracker 和 cost 頁重複的公司段落，每家只留一個家。
   - 順手修掉 §6 第 1、2、5 項的矛盾，把 `%%` 維運備忘和 §5 的用語移出讀者會看到的位置。

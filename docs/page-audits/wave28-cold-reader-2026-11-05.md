# Wave 28 冷讀者實測：Claude Sonnet 5.5（2026-11-05）

**事先聲明（context 污染）：** 系統在我開始讀之前，自動把根目錄 `CLAUDE.md`（專案說明）塞進 context；讀完 `wiki/index.md` 之後，又自動塞入 `wiki/CLAUDE.md`（wiki 規則：搜尋策略、連結慣例、三層哲學）。兩份我都沒有主動去讀。答題只用沿 `[[連結]]` 走到的 wiki 頁；那兩份規則裡的資訊（例如 `⟨Q-nn⟩` 是什麼、`%% %%` 會被剝除）我沒拿來解讀頁面。下面「內部用語」一節照一般讀者的角度判斷。

**讀者設定：** Claude Code 重度使用者，第一次來。工具只有 Read，以及在已打開的單頁內 Grep。

**入口：** `wiki/index.md` 第 48 列 `[[entities/sonnet-5-5]]`（Entities 表第一列，鉤子直接寫「取代 Sonnet 5 成為 API 預設 Sonnet」）。Q2 另走第 32 列 `[[entities/claude-code-releases]]`，也參考了第 53 列 `[[entities/opus-5-5]]` 的鉤子。

---

## Q1 Sonnet 5.5 是什麼？跟 Sonnet 5 差在哪？該不該換？ —— **拿到**

**路徑（2 跳）：**
1. index L48 → `entities/sonnet-5-5`「現況」L44–46、「你現在拿到的是什麼」L58–66、「這些數字是誰量的」L88–100
2. sonnet-5-5 L48 → `topics/model-comparison`「選型細節」L63–64、「情境推薦」L76

**卡住的原句：**
- sonnet-5-5 L77「**牌價完全不變，靠速度換效率**……『多數工作省最多 30% 成本』」：牌價沒變，成本怎麼省 30%？是 token 變少，還是 effort 預設不同？頁面沒解釋。
- sonnet-5-5 L80 與 L94 是同一句「疑似 GDPval 系列……落後 Opus 5.5 兩分……截斷」，出現兩次，讀了等於白讀。

**我的答案：** Sonnet 5.5（`claude-sonnet-5-5`）在 2026-09-28 發布，是 5.5 家族的中階模型。牌價和 Sonnet 5 一樣是 $2／$10，但快取讀取從 $0.20 降到 $0.10。知識截止日從 2026 年 1 月推到 6 月，退役不早於 2027-09-28。官方說它快逾 30%，Terminal-Bench 4.0 從 10.3% 提升到 70.6%。Sonnet 5 已列為 Legacy。該換：model-comparison L64 寫「新採用一律改用 Sonnet 5.5」。但升級前要先跑自己的回歸測試（見 Q4）。

## Q2 Claude Code（Pro／Max）現在預設跑哪個模型？能不能用 Sonnet 5.5？ —— **半**（找到答案，但四頁說法互相打架）

**路徑（4 跳）：**
1. index L48 → sonnet-5-5 L60、L70「⟨Q-01⟩ 查無官方：Sonnet 5.5 是否同步為 Claude Code CLI 預設」
2. index L53（鉤子寫「v2.1.280 起為 Claude Code 預設模型」）→ `entities/opus-5-5` L58、L64：「Pro／Max／Team／Enterprise／API 的預設 Opus」
3. index L32 → `entities/claude-code-releases` L126：「**v2.1.280** Opus 5.5 成新預設模型」；L119：v2.1.284 讓 Sonnet 5.5 成為「API 預設 Sonnet」
4. sonnet-5-5 L48 → `entities/pricing` L69：Pro 包含「全模型，**Fable 旗艦除外**」；L88：「Opus 5.5 同步為 Max 新預設」

**卡住的原句：**
- pricing L133「取代 Sonnet 5 為 **Claude Code／API 預設**」，以及 L113「Sonnet 5.5（09-28 起為預設…）」，都跟 releases L126、index L53 相反。
- opus-5-5 L160「[[entities/sonnet-5]] — **Claude Code 的整體預設**」：連結指向一個已經 Legacy 的模型。
- sonnet-5 L57「Claude Code v2.1.197 起**已將 Sonnet 5 設為預設模型**」、L78「已預設使用 Sonnet 5，無需指定」、L95：這頁的「現況」和「使用指南」仍用現在式。
- sonnet-5-5 L66「Pro／Max／Team／Enterprise 是否同步未載」：跟 pricing L69 的「Pro 全模型」對不起來。

**我的答案（拼湊、信心中等）：** Max 的預設很可能是 Opus 5.5（releases L126、pricing L88）。Pro 的預設沒有任何一頁明說。Sonnet 5.5 在 Pro／Max 應該能用：Pro 包含 Fable 以外的全部模型，`/model` 可以切換（feature-radar L14 教你用 `/model` 確認）。不過模型頁本身說「方案是否同步未載」，我無法確定。

## Q3 Sonnet 5.5 處理一百萬 token 多少錢？快取怎麼算？ —— **拿到**

**路徑（2 跳）：**
1. index L48 → sonnet-5-5 L61、L78
2. sonnet-5-5 L78 → `entities/pricing`「模型 API 定價現況」L133、「乘數」表 L244–251、「乘數細節」L258–260

**卡住的原句：**
- pricing L206「**1M context window 觸發獨立 API 計費通道**……仍會產生額外費用」：放在「當前生效的計費規則」裡，證據是一筆 2026-05 的單例。L249／L260 卻說 4.6 以後的世代 1M context 不加價。讀者無法判斷 Sonnet 5.5 用 1M context 會不會被另外收錢。
- tokenizer 差異：model-comparison L119–126 的換算表沒有 Sonnet 5.5 這一列，不知道它的 token 數會不會比舊 tokenizer 多約 30%。

**我的答案：** 每百萬 token：輸入 $2、輸出 $10；快取讀取 $0.10（×0.05）；快取寫入 5 分鐘 $2.50（×1.25）、1 小時 $4.00（×2）；Batch 半價，即 $1／$5；1M context 不加價；開資料落地（`inference_geo:"us"`）全部 ×1.1。Bedrock／Vertex 的價格由各平台自訂。

## Q4 從 Sonnet 5 換到 5.5 會壞什麼？prompt／effort 怎麼調？ —— **半**（effort 和 prompt 拿到；「會壞什麼」只拿到一個外連）

**路徑（2 跳）：**
1. index L48 → sonnet-5-5「跟它怎麼說話」L119–130、「表下細節」L75–76、L64
2. sonnet-5-5 L129 → `topics/model-comparison`「升級與退役風險」L151–152、L160；「Effort dial 細節」L94–98

**卡住的原句：**
- sonnet-5-5 L64「官方 migration guide **尚未見完整記載（原文截斷）**」與 L130「從 Sonnet 5 升上來的**五項破壞性 API 變更**不在本節，走官方 migration guide」：同一頁裡互相矛盾。L130 表示官方指南已經列出五項，本站卻一項都沒寫。
- L76 社群也說有「5 處行為差異」，跟官方的「五項」是不是同一件事？頁面沒交代。
- model-comparison L98 列了 Haiku 5.5 和 Opus 5 的預設 effort，沒有 Sonnet 5.5；L92 還寫著「Opus 5 起手用預設 high」，但現行 Opus 已經是 5.5，預設為 medium（opus-5-5 L136）。

**我的答案：** 會壞什麼：官方說有五項破壞性 API 變更，但本站沒列，要自己去讀官方 migration guide。另有單一來源報導稱有一處靜默失敗、工作階段可能被降回 Sonnet 5，都未經證實。

**怎麼調：**
- 預設 effort 同樣是 `high`，但級距已重新校準，不等於 Sonnet 5 的 `high`。agentic coding 從 `medium` 起；聊天從 `low` 或 `medium` 起。
- 用 `low` 時要加「改到可執行的程式就跑真實檢查」，否則它會跳過驗證。
- 用 `low`／`medium` 跑長任務時加「做完為止」；用 `xhigh`／`max` 時加「做完就停」，官方測得省約三分之一成本。
- 刪掉「hold all findings…」這類指示，並設 `display: "updates"`。
- 不要把使用者輸入放進 `tool_result`。

---

## 哪兩頁分不出差別

`entities/sonnet-5` vs `entities/sonnet-5-5`：
- 09-28 發布的故事（sonnet-5 L43／L123 對 sonnet-5-5 L44／L184）寫了兩次。
- 同一題「CLI 預設查無官方」也複製兩份（sonnet-5 L48–49 對 sonnet-5-5 L70–71）。
- 舊頁還留著「Claude Code 預設」的現在式（L57、L95），讀者會以為兩頁都在講「現在的預設」。

次要的一組是 `pricing` L113／L133 和 `model-comparison` L52／L76：兩頁都在答「誰是預設」，而且答案不同。

## 這頁像百科還是雷達

**偏雷達。** 「你現在拿到的是什麼」（L58–66）和「跟它怎麼說話」（L119–125）是百科式的穩定事實，也是全頁最有用的兩塊。但頁頂 callout 放的是一次 30 分鐘的事故（L37–38）；另外有三段新聞原文（L75–76、L95 HN 分數、L97 一則 0 留言的 Reddit 貼文），歷史記錄又重寫一遍（L169–190）。一半篇幅在講「誰報導了什麼」。

---

## 內部用語外洩（10 條）

1. sonnet-5-5 L60、L70「⟨Q-01⟩」：讀者不知道這是什麼代號。
2. sonnet-5-5 L70「🔎 **查無官方**（標 2026-09-28｜查 v2.1.284、Claude Code CLI 預設｜複 2026-11-10）」：「標／查／複」是編輯流程用的縮寫。
3. sonnet-5-5 L69、L73、L92、L127「**懸置細節**」「**表下細節**」：內部版面用的區塊名。
4. sonnet-5-5 L75、L76、L80、L94「不採信推算」：讀者會問「誰不採信？推算什麼？」
5. sonnet-5-5 L108–109「同步 [[feature-radar]]，2026-09-29 查核」，以及 L113「本表跟著 [[feature-radar]] 全覽表走」：講的是維護流程，不是給讀者的內容。
6. sonnet-5-5 L1–26 frontmatter 的 `inbound_links: 30`、`pending_count`、`signal: "健康"`、`attribution_count`：如果網站會把這段顯示出來，就是外洩。
7. pricing L37「%% 拆頁評估 2026-11-02：已拆（第 24 波，`docs/page-audits/ledger.md` 裁決紀錄）…正文上限 300 行 %%」：在原始 markdown 裡讀者看得到。
8. pricing L111、L115、L193「WebFetch 逐字查證」，以及 L183–185「diff 偵測」：這是工具名稱，不是來源。
9. feature-radar L18、L20「30 天時間閘」「預設值改變型」「擠下」（`%%` 註解）。
10. index L3–6「**角色：**地圖……**收：**慢變的路由事實……**不收：**快變事實」，以及 L49「↳ 子故事」：這些是寫給編輯的檔案規約，不是寫給讀者的。

## 撐不起的句子（無證據或互相矛盾）

1. **Claude Code 預設模型有五種說法：**
   - index L53 和 releases L126 說是 Opus 5.5
   - pricing L113、L133 說是 Sonnet 5.5
   - opus-5-5 L160 說是 Sonnet 5
   - sonnet-5 L57、L95 用現在式說是 Sonnet 5
   - sonnet-5-5 L60、L70 說查無官方

   而且 ⟨Q-01⟩ 說官方文件沒寫 CLI 預設，releases L126 卻引 v2.1.280 release 說「成新預設模型」。兩者要嘛互相推翻，要嘛 Q-01 該結案。
2. **sonnet-5-5 L64 對 L130：** migration guide「尚未完整記載」，同一頁又說「五項破壞性 API 變更」在 migration guide 裡。model-comparison L160 也照抄「尚不完整」。
3. **sonnet-5-5 L50「自 2026-10-01 起無新動態（2026-10-24 核）」：** 同頁 L35 寫最後新聞更新 10-25，L37 callout 是 10-25 的事故。
4. **sonnet-5-5 L66「Pro／Max 是否同步未載」：** 跟 pricing L69「Pro 全模型（Fable 除外）」矛盾。
5. **sonnet-5-5 L77：** 「牌價不變」和「省最多 30% 成本」並列，沒有說明省在哪。
6. **pricing L206：** 放在「當前生效規則」，說 1M context 會觸發額外計費，證據只有 2026-05 的一筆單例。跟 L249、L260 的「4.6 以後不加價」沒有調和，也沒說這條是指訂閱還是 API。
7. **model-comparison L92、L98：** effort 建議還以 Opus 5 為基準，沒有涵蓋 Sonnet 5.5／Opus 5.5 的新預設。
8. **sonnet-5-5 L134「1M context（沿用 Sonnet 5 規格，官方發布文未特別提及變動）」：** 用「沒提到」來推論；pricing L133 其實已經對官方查證過「支援 1M」，這邊可以直接引那條。

## 最想改的三件事

1. **把「Claude Code（各方案）現在預設哪個模型」收成一個家，其他頁指過去。** 用一張小表列方案 × 預設模型 × 查證日；pricing L113／L133、opus-5-5 L160、sonnet-5 L57／L78／L95 全部改寫或刪掉。⟨Q-01⟩ 要嘛用 releases L126 結案，要嘛把 releases 降級成「未證實」。
2. **在 sonnet-5-5 把官方 migration guide 的「五項破壞性 API 變更」逐條寫出來，**放在「從舊代升上去會壞什麼」那一格（L64），並刪掉 L64 的「原文截斷」。再把 MIXED 那條「5 處行為差異」和官方五項對照：是同一件事就合併，不是就標明。這是升級讀者最需要的一格，現在卻是空的。
3. **把頁面從雷達改回百科。** 頁頂 callout 改放「現在預設／能不能用／換了要調什麼」三行結論，不要放 30 分鐘的事故；HN 分數、0 留言 Reddit、重複兩次的「GDPval 差兩分」移進歷史或刪掉；model-comparison 的 Effort dial 節補上 Sonnet 5.5／Opus 5.5 的預設檔位。

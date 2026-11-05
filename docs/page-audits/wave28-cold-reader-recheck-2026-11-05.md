# Wave 28 冷讀者複驗：Claude Sonnet 5.5（2026-11-05）

**自動載入聲明：** 作答期間系統自動把兩份規則檔塞進 context：`CLAUDE.md`（repo 根目錄）、`wiki/CLAUDE.md`。作答沒有用到其中的資訊，只沿 `[[連結]]` 走。

**讀者設定：** Claude Code 重度使用者，第一次來。從 `wiki/index.md` 進站，只走 wikilink。

**走過的頁：** `wiki/index.md` → `wiki/entities/sonnet-5-5.md` →（`[[entities/pricing]]`、`[[topics/model-comparison]]`、`[[entities/opus-5-5]]`、`[[entities/sonnet-5]]`）。後四頁都只在頁內 Grep 後讀相關段落。

---

## 入口

- 入口在 `wiki/index.md` L48，也就是 Entities 表的第一列 `[[entities/sonnet-5-5]]`。這一列的鉤子已經寫明「Claude Code `sonnet` 別名，非預設」與「$2/$10」，一眼就知道該點哪裡。
- L49 的 `[[entities/sonnet-5]]` 就在下一列，兩列不會點錯。

## 四題

### Q1 Sonnet 5.5 是什麼？跟 Sonnet 5 比差在哪？該不該換？

- **路徑：** index L48 → sonnet-5-5 L29（一句定義）、L52「現況」（定位、快 30%、省最多 30%）、L60–69「你現在拿到的是什麼」兩代對照表、L105–114 基準表 → model-comparison L63–64（Sonnet 5「新採用一律改用 Sonnet 5.5」）
- **跳數：** 1 跳就拿到主體答案；要拿到明確的「該換」需要 2 跳
- **結果：** 拿到
- **卡住的地方：** sonnet-5-5 頁內沒有一句直接回答「該不該換」，只有 L68「官方建議遷移到 Sonnet 5.5」藏在表格格子裡。明確的結論在 model-comparison L64。
- **我的答案：** Sonnet 5.5 是現行中階模型，2026-09-28 發布，API ID 是 `claude-sonnet-5-5`。跟 Sonnet 5 比：
  - 牌價相同（$2/$10），快取讀取減半（$0.20 → $0.10）
  - context 1M／輸出 128K 不變
  - 知識截止從 Jan 2026 推到 Jun 2026
  - 官方基準全面大幅領先（Terminal-Bench 4.0 從 10.3% 到 70.6%）
  - 官方稱快 30% 以上、多數工作省最多 30%

  Sonnet 5 已列 Legacy，官方建議遷移，所以該換。換之前先對過 Q4 的破壞性清單。

### Q2 Claude Code（Pro／Max）現在預設跑哪個模型？能不能用 Sonnet 5.5？

- **路徑：** index L48 → sonnet-5-5 L41–43 頂部 callout、L50「現況」、L62 → 交叉比對 opus-5-5 L58、L64，sonnet-5 L48、L57
- **跳數：** 1 跳（callout 第一行就是答案）
- **結果：** 拿到
- **卡住的地方：** 別頁的說法跟本頁打架，交叉比對時會動搖，詳見「撐不起的句子」第 1–4 條。例如 `entities/pricing.md` L113「Sonnet 5.5（09-28 起為預設…）」。
- **我的答案：** Pro 和 Max 預設都是 Opus 5.5（2026-11-05 依官方 model-config）。可以用 Sonnet 5.5，做法是 `/model sonnet` 或 `--model`，需要 v2.1.284 以上。在 Claude Code 裡 effort 預設是 medium。被資安分類器標記的請求會自動改跑 Sonnet 5，可以在 `/config` 改成「Ask each time」。

### Q3 用 Sonnet 5.5 處理一百萬 token 多少錢？快取怎麼算？

- **路徑：** index L48 → sonnet-5-5 L63（牌價與快取四個數字）、L76 → `[[entities/pricing]]` L133、L244–249（乘數表，長脈絡不加價）、L258–259
- **跳數：** 1 跳拿到單價；要確認「1M 不加價」與 Batch，需要 2 跳
- **結果：** 拿到，但要自己算
- **卡住的地方：**
  - 沒有任何一頁給「1M token 跑一次多少錢」的算例。
  - 「1M 會不會加價」在 sonnet-5-5 頁沒講，要到 pricing L249 才找到。
  - pricing L206「1M context window 觸發獨立 API 計費通道…仍會產生額外費用」讓人不確定這條還算不算數。
- **我的答案：**
  - 牌價（每百萬 token）：輸入 $2、輸出 $10
  - 快取讀取 $0.10（×0.05）
  - 快取寫入：5 分鐘 $2.50（×1.25）、1 小時 $4（×2）
  - Batch 半價：$1／$5
  - Claude 4.6 以後的模型長脈絡不加價，所以 1M 輸入大約是 $2，全部命中快取大約是 $0.10
  - 最小可快取 prompt 是 512 token
  - 若用 `inference_geo:"us"` 資料落地，全部再乘 ×1.1

### Q4 從 Sonnet 5 換到 Sonnet 5.5 會壞什麼？prompt／effort 怎麼調？

- **路徑：** index L48 → sonnet-5-5 L44（callout 指路）→ L80–96「從 Sonnet 5 換過來會壞什麼」→ L129–141「跟它怎麼說話」
- **跳數：** 1 跳
- **結果：** 拿到
- **卡住的地方：** 沒有實質卡點。L84 把「thinking disabled 要改送 `between_tools`」和「effort 只收 low／medium／high」塞在同一條，讀第一遍以為是同一件事。
- **我的答案：** 會回 400 的有 5 項：
  - `thinking: disabled`，要改送 `between_tools`；`xhigh`／`max` 要搭 adaptive
  - `tool_choice` 設 `any` 或 `tool`，要改用 `strict` 或 structured outputs
  - 改過 system、tools 或先前訊息後回放 thinking block
  - `computer_20251124`，要改用 `computer_toolset_20260801`
  - 四個 advisor 搭檔

  不報錯但會出問題的 1 項：工具呼叫之間的文字改走 thinking block，在 `display: omitted` 下前端會變安靜。

  effort 要重新掃一輪。agentic coding 從 medium 起，聊天從 medium 或 low 起，要它少想就降一級 effort，不要靠 prompt 叫它少想。prompt 要改這幾處：
  - `low` 下它會跳過驗證，要加「跑真實檢查」那段
  - `low`／`medium` 跑長任務會中途停下來問，要加「做完為止」那段
  - `xhigh`／`max` 會自己加開 review 輪，要加「做完就停」那段
  - 刪掉「hold all findings for the final response」
  - 不要把使用者輸入塞進 `tool_result`

## 分不出差別的兩頁

`entities/sonnet-5-5`「你現在拿到的是什麼」（L60–69）與 `topics/model-comparison` 快速選型表（L52）。兩邊都列牌價、快取、context 和定位，而且 model-comparison L52 寫「API 預設」，跟 sonnet-5-5 的「不是任何方案的預設」對不上。讀者分不出哪一頁才是「它現在是什麼」的權威。

另一組是 `entities/sonnet-5` 與 `entities/sonnet-5-5`：兩頁都在講「v2.1.280 前／後誰是預設」，同一段歷史在兩頁各寫一次。

## 百科還是雷達

`entities/sonnet-5-5` 像百科。頂部 callout 加上四個穩定章節（拿到什麼、會壞什麼、數字、怎麼說話），比較像能長期查的參考頁。只有頁尾「歷史記錄」帶雷達味（HN 分數、單一 Reddit 貼文），而且已經放到最後，不干擾讀者。

`entities/pricing` 偏雷達。頂部 callout 和「方案細節」是一串帶日期的異動與更正，百科該有的結論被擠到 L128 之後。

---

## 內部用語外洩（10 條）

1. `wiki/index.md` L3–6：「**角色：** 地圖……**收：** 慢變的路由事實……**讀法：** 整讀……查詢分流見 `wiki/CLAUDE.md`「搜尋策略」」。這段是維護者守則，讀者一進門就撞上。
2. `wiki/index.md` L113：「Topics 頁面本身無「類型」欄位，故表格僅三欄……為刻意設計差異」
3. `wiki/index.md` L49 等多列：「↳ 子故事：[[entities/sonnet-5-archive]]」。「子故事」是內部分層用語。
4. `wiki/entities/pricing.md` L37：`%% 拆頁評估 2026-11-02：已拆（第 24 波，docs/page-audits/ledger.md 裁決紀錄）…正文上限 300 行… %%`。網站建置會剝除這段，但原始 md 上可見。
5. `wiki/entities/pricing.md` L107、L111、L115、L193：「WebFetch 官方定價頁逐字查證」。這是工具名稱，讀者不知道 WebFetch 是什麼。
6. `wiki/entities/pricing.md` L220：「本次改兩項——長脈絡標準價的 Haiku 5.5 例外、Fast mode 不再限第一方 API；通路五條與其餘乘數與 09-26 一致」。這是維護差異說明，不是給讀者的內容。
7. `wiki/entities/pricing.md` L259：「⚠️ Sonnet 5.5 這一檔 09-26 查證時漏列，2026-10-10 依官方 models overview 與 Sonnet 5.5 模型頁補上」
8. `wiki/entities/sonnet-5-5.md` L200：「本庫當日記為 $0.20（×0.1），2026-10-10 對官方模型頁更正」
9. `wiki/entities/pricing.md` L204：「日報 09-28／10-01 偵測到的異動屬實」，以及 L83「（Official Docs）」。前者用了內部管線用語「日報偵測」。
10. `wiki/entities/sonnet-5-5.md` L199：「當日只讀到摘要，完整 8 項官方表 2026-11-05 對原文補齊」

## 撐不起的句子（說了但沒證據，或互相矛盾）

1. **「誰是預設」四處說法打架（最嚴重）**
   - `wiki/entities/sonnet-5-5.md` L42／L62：「不是任何方案的預設（各方案預設 Opus 5.5）」
   - `wiki/entities/pricing.md` L113：「Sonnet 5.5（09-28 起為預設，同 Sonnet 5 價）」
   - `wiki/entities/pricing.md` L133：「取代 Sonnet 5 為 Claude Code／API 預設」
   - `wiki/entities/pricing.md` L134：「2026-09-28 起預設改為 Sonnet 5.5」
2. `wiki/entities/sonnet-5.md` L120：「Claude Code v2.1.284 將其設為 API 預設 Sonnet 模型……是否同步為 Claude Code CLI 本身的預設、本頁是否比照 Opus 5.5 模式改列 Legacy，官方原文均未載明」。這段跟同頁 L48、L92 以及頁首「Legacy」狀態自相矛盾，而且「Claude Code 某版設定 API 預設」在邏輯上說不通。
3. `wiki/topics/model-comparison.md` L52「現行 Sonnet，API 預設」、L230「取代 Sonnet 5 成為 Anthropic API 預設 Sonnet」。API 呼叫本來就要指定 model，「API 預設」指的是什麼沒有說明，也沒附來源。
4. **「預設 Opus」與「預設模型」混用**
   - `wiki/entities/opus-5-5.md` L58、L151：「Pro／Max／…的預設 Opus」「v2.1.280 新增 Opus 5.5 並設為預設 Opus」，講的是 `opus` 別名
   - `wiki/entities/sonnet-5-5.md` L62、`wiki/entities/sonnet-5.md` L57：「v2.1.280 前 Sonnet 5 是 Pro 的 Claude Code 預設」

   照這兩組說法，Pro 的預設是在 v2.1.280 從 Sonnet 換成 Opus。但 changelog 的引文只寫了「預設 Opus」，Pro 那一段沒有證據撐。`wiki/entities/pricing.md` L88 又只寫「Opus 5.5 同步為 Max 新預設」。
5. **快取乘數自相矛盾：** `wiki/entities/pricing.md` L135「快取命中 ×0.025（其餘模型 ×0.1）」，跟同頁 L244、L258 的「Opus 5.5 與 Sonnet 5.5 為 ×0.05」矛盾。
6. **1M 會不會加價沒有收斂：** `wiki/entities/pricing.md` L206「1M context window 觸發獨立 API 計費通道…仍會產生額外費用」引的是 2026-05-11 單一實例、沒有連結，也沒標適用哪一代模型。同頁 L249、L260 則說「Claude 4.6 以後內含 1M 且不加價」。讀者無法判斷 Claude Code 訂閱裡用 Sonnet 5.5 開 1M 會不會另外計費。
7. **推論被寫成事實：** `wiki/entities/sonnet-5-5.md` L108 基準表把「52.1%（xhigh）」當事實列出，L117 卻說「52.1% 對應 xhigh 依註腳推得」。

## 最想改的三件事

1. **把「預設」統一成一句官方說法。** 以 2026-11-05 model-config 為準，改掉 pricing L113、L133、L134，sonnet-5 L120，model-comparison L52、L230。全站分開寫「預設模型」（各方案 Opus 5.5）和「`sonnet`／`opus` 別名指向誰」，不再出現「API 預設」「預設 Opus」這類模糊字眼。
2. **在 sonnet-5-5 頁補一個「1M token 算例」，並修掉 pricing 頁兩處互斥的句子。** 算例放在「你現在拿到的是什麼」補充，內容包含：無快取、全命中快取、Batch，加一句「長脈絡不加價」並連到 `[[entities/pricing#乘數：會互相疊乘]]`。pricing 要修的兩處：L135「其餘模型 ×0.1」改成三檔說法；L206 舊的 1M 計費句標明適用世代，或移到 archive。
3. **清掉讀者看得到的維護用語。** 包括 index 頂部的角色／收／不收／讀法段落、「WebFetch」、「本庫當日記為」、「本次改兩項」、「09-26 查證時漏列」、「日報偵測到」。更正軌跡只留一句「已依官方更正（日期）」。

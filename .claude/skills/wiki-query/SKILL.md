---
name: wiki-query
description: 查 wiki 內容並照契約回答：問「wiki 裡 X 怎麼說」「最近 X 怎樣」「X 和 Y 差在哪」、要出處、或要把查證結果寫回 wiki 時使用。
---

# Wiki 查詢

Query 是本庫三個動作之一（寫入／查詢／整理，見 `./CLAUDE.md`「這是一個 LLM wiki：三個動作」）。本 skill 規定查詢怎麼走、答案怎麼交、什麼時候要把答案寫回去。

回答契約（三件套、現在／當時、懸置、找不到）、Query log 條目模板、質疑回流那一行，住 `.claude/skills/wiki-query/references/contract.md`，本檔不重述——**回答前先讀它**。

---

## 1. 分流：先選路，不要一律先讀 index

六路的完整定義住 `wiki/CLAUDE.md`「搜尋策略」，**照那裡執行，本節只做速查**：

| 問題長這樣 | 走第幾路 |
|---|---|
| 出現專有名詞、issue 編號、版本號、錯誤碼 | 1（直接 Grep `wiki/`） |
| 概念、選型、「哪頁在講 X」 | 2（`wiki/index.md` 挑頁 → 讀該頁頂部 callout） |
| 「哪些頁是某狀態／某領域／多久沒更新」 | 3（Grep 頁面標頭欄位） |
| 「最近 X 怎樣」「上週發生什麼」 | 4（`wiki/log.md` 先 Grep 日期，或 `news/`） |
| 「誰負責這頁／這頁多久更新一次」 | 5（`.claude/reporter-rules/<類別>/daily.md` 負責頁面表） |
| 「誰引用 X」「A 和 B 怎麼連」「這議題散在哪幾節」 | 6（`python scripts/wiki_graph.py`） |

一路查完沒有答案就換下一路，不要在同一路上加關鍵字硬撈。

## 2. 回答

照 `.claude/skills/wiki-query/references/contract.md`「回答契約」交答案。

## 3. 答案回流（使用者提問通道）

wiki 裡沒有、或使用者點名要查證的事實，走這條通道——**查證是入場券**：

1. 以 WebFetch／WebSearch 查**一手來源**（官方文件、官方公告、原始 repo、原始貼文）。查不到一手來源 → 只能標懸置，不得寫成事實。
2. 寫進事實該在的那一頁（判斷落點看 `.claude/reporter-rules/<類別>/daily.md` 的負責頁面表），**必標查證日＋來源連結**；寫頁前先讀 `.claude/reporter-rules/page-templates.md`（頁面格式、懸置標記語法、表格上限）與 `.claude/reporter-rules/shared.md`（書寫風格硬上限、讀者語言禁詞）。紀律見 `./CLAUDE.md`「使用者提問通道」與 `.claude/rules/collection-scope.md`。
3. `wiki/log.md` append 一筆 Query 條目（append only，模板見 `.claude/skills/wiki-query/references/contract.md`）。
4. `data/source_attribution.jsonl` append 一行，`source` 為 `user-query`，schema 見 `data/README.md`。

**不寫頁的情況**：純查詢（使用者只是要答案）、事實已經在頁上且未過期。這兩種只回答，不動檔案。

## 4. 質疑回流

使用者的問題若**揭露缺陷**（該頁答不出它該答的問題、數字沒有來源、規則有漏洞、機制從沒被執行過），除了上一節的 Query 條目，回報末尾多一行，格式見 `.claude/skills/wiki-query/references/contract.md`「質疑回流」。

判「是」者交 `/wiki-lint` 步驟 7b 評估要不要加進抽問題庫（判準見 `.claude/skills/wiki-lint-reader-acceptance/references/inquiry.md`「題庫維護」，加題須經使用者確認）。

## 5. 收尾

動過任何 wiki 頁時：

```
python scripts/check_cell_limits.py --page <頁面 slug>
python scripts/check_reader_language.py --page <頁面 slug>
```

**把實際輸出的最後一行抄進回報**，不是寫「✅ 通過」；順序固定：改完 → 跑 → 抄輸出 → 不再動那一頁。

---

## 邊界

- **由任何 session 直接執行**，不 spawn 子 agent。
- 找不到一手來源時只標懸置，不得寫成事實；`news/` 唯讀，`wiki/log.md` 只能 append。
- 收尾兩支腳本非綠不算完成；改動照 `./CLAUDE.md`「完工定義」閉迴路（測試綠／已 commit／依賴缺口已登記）。
- **commit 與否屬使用者裁決，本 skill 不自行 commit。**

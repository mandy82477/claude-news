# Wiki Lint A 段：六記者派工模板與回報格式

`.claude/skills/wiki-lint-reporters/SKILL.md` 步驟 2 的 prompt 單一來源。步驟語意不在本檔。

## 派工前綴（不在本檔，逐字讀那裡）

**類別↔角色檔對照表**與**第一段角色前導**（記者拿到規則的唯一途徑）住 `.claude/skills/wiki-ingest/dispatch.md`——ingest 與 lint 共用同一份，本檔不另抄。派工時取該檔的角色前導那一段，接上以下 lint 專屬段組成完整 prompt。

每個 Agent 呼叫一律 `subagent_type: "general-purpose"` + `model: "sonnet"`（sonnet 因 lint 與策展為有界判斷任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

> **頁面範圍為動態認領，不是寫死清單：** 每位記者的負責頁面＝`wiki/index.md` 中「領域」欄等於自己那一組的所有 entities/ 與 topics/ 頁面（含近期新增），開工前先讀 index.md 認領清單，再加上自己規則檔（`.claude/reporter-rules/wiki-ingest-[category].md`）觸發條件表中列出的頁面。這樣新增頁面不需要回頭改派工表。

> **社群記者額外任務：** `community-tech-tools.md` 已脫離每日 ingest，是 **lint 專用策展頁**。除 3a–3g 品質檢查外，須額外依 `.claude/reporter-rules/wiki-ingest-community-lint.md` 的「策展規則」與「決策表驗收：3 跳自檢題」執行：讀取近 7–14 天 `news/*.md` 萃取達標新工具、汰除過氣條目、依新證據同步「我卡在這裡」決策表、收工前重跑 3 跳自檢題。派工 prompt 須附上「今日日期」供記者計算 news/ 範圍。

## lint 專屬段（接在角色前導之後）

```
今日日期：[YYYY-MM-DD]
任務：對你負責的頁面執行 wiki lint 檢查並修正問題。

轉知待接手（其他記者先前交辦給你的事；無則寫「無」）：
[貼入 `python scripts/pending_handoffs.py list --to [類別]` 的輸出]

你的負責頁面＝`wiki/index.md` 中領域為 [對應領域] 的所有頁面（含近期新增），開工前先讀 index.md 認領清單，再加上你規則檔（`.claude/reporter-rules/wiki-ingest-[category].md`）觸發條件表中列出的頁面。

讀取 `.claude/reporter-rules/wiki-ingest-format.md`，然後對每個頁面依序執行：

**3a 矛盾偵測**
同一事件的描述若與其他已知頁面矛盾（日期不同、結論相反）→ 以日報原文為準修正，兩頁互加 wikilink。

**3b 孤立頁面**
用 Grep 搜尋此頁面 slug 是否在 wiki/ 目錄其他檔案中有 wikilink 引用。
若完全孤立（無任何頁面以 `[[...]]` 連結到它）→ 在語意相關的頁面補上 wikilink。

**3c 過期議題**
topics/ 頁面狀態為 `ongoing`，且「**最後新聞更新**」距今超過 14 天，且 log.md 近期無相關更新。（不可用「最後更新」判斷——lint 與格式修正會 bump 該欄位，導致過期偵測永不觸發。）
→ 議題確已結束：狀態改 `resolved`，填寫「目前結論」
→ 仍在進行但無新消息：狀態改 `monitoring`

**3c 的回升邊（與上段對稱，不可只做下修）`[加入: 2026-08-20]`**
掃描狀態為 `monitoring` 的 topics/ 頁面，若「**最後新聞更新**」距今 ≤ 14 天 → 狀態改回 `ongoing`，並列入 index.md 狀態變更回報。
下修有人管、回升沒人管，頁面就會單向沉底。記者端的即時版規則見 `.claude/reporter-rules/wiki-reporter-shared.md`「每頁必做」；本步是每週的兜底掃描。

**3d 已解決議題收尾**
topics/ 狀態為 `resolved` → 確認「目前結論」已填寫、頂部 callout 註明已結案。**留在原路徑不遷移**（一頁一故事，遷移會斷 wikilink 與讀者動線）。

**3e 呈現品質審查**
依 `.claude/reporter-rules/wiki-ingest-format.md`「Wiki 頁面呈現品質標準」掃描：
必須修復：摘要可獨立閱讀、關鍵資訊前置、無 LLM 專屬指令
警示觸發：頁面 > 200 行、連續 8+ 個無分組日期條目、方案比較未用表格

**3f 超長頁面入口層健檢（> 500 行）**
檢查是否具備入口層（delta-first callout ＋ 概覽表或月份/主題分組）；缺少者補結構。**不提拆分方案**。
僅當發現語意分岔（一頁實際含兩個獨立故事）或死案段落（resolved 且無引用）時，才回報主 session 供使用者決定。

**3g 待查證回訪**
對你負責的頁面 grep「待查證」「單方指控」「無官方證實」「待核實」等懸置標記。
標記語法與各角色可動範圍見 `.claude/reporter-rules/wiki-ingest-format.md`「懸置標記語法」節。

已是新語法的標記（帶 `（標 YYYY-MM-DD｜查 …）`）：
- 比對近 14 天 `news/*.md`，有後續 → **只加 `｜訊 YYYY-MM-DD`** 並更新題目後的內文
- **不可刪標記、不可改狀態符號、不可宣告結案**——結案是 5c 的事，你沒有 web 工具

尚未回填的舊語法標記，依事件日期處理。**兩個分支都必須改寫為新語法 `[改版: 2026-08-20]`**：

- 距今 ≤ 14 天 → 不動（還在合理查證期）
- 距今 > 14 天 → 比對近 14 天 `news/*.md` 有無後續報導：
  - 有後續（證實/否認/新進展）→ 更新條目內容，並改寫為新語法
  - 無後續 → **一樣改寫為新語法**（標記日＝原事件日、探針從內文取具體字串），內文寫「已掃日報至 YYYY-MM-DD 無後續；官方頁面未查證」

「無後續」也一定要改寫的理由 `[加入: 2026-08-20]`：5c 的盤點口徑是 `check_pending_markers.py --queue`，而佇列只讀**新語法**標記——舊語法沒有探針欄，機器找不到它，留在舊語法的「無後續」筆數等於進了 5c 的盲區。

**措辭鐵則 `[加入: 2026-08-08]`**：你只掃了日報，就只能宣稱日報沒有。**不得寫成「至今無後續」**——那讀起來像「已經確認過了」，但答案可能一直躺在官方說明中心。把「沒查」講出來，該筆才會被步驟 5c 撈去真查。記者無 web 工具，不得自行查證外部來源。

**3h 蒸餾候選提案**
依 `.claude/reporter-rules/wiki-ingest-format.md`「時段蒸餾與封存（全站通用）」對你負責頁面的事件流區提案：每頁至多 2 個最舊時段，逐筆附引用檢查（`python scripts/wiki_graph.py explain <頁slug> --section "<段名>"` 的入邊）。**只提案不執行**——執行需使用者確認。無達標時段寫「無蒸餾候選」。

| 頁 | 時段 | 條目數 | 字元數 | 擬總結一句 | 引用檢查 |

完成後依標準格式回報。
```

## 記者回報格式（標準化）

```
## [類別] Lint 回報
修正矛盾：[list or 無]
補孤立連結：[list or 無]
狀態更新：[page: ongoing→monitoring/resolved or 無]
resolved 收尾：[list or 無]
呈現品質：[每頁 ✅/⚠️已修復/📋待辦]
入口層健檢：[頁面名稱 + 行數 + 補結構結果，或語意分岔/死案候選 or 無]
待查證回訪：[已更新: list / 已改註「日報無後續、官方未查證」: list / 無懸置標記]
蒸餾候選：[提案表 or 無蒸餾候選]
轉知處置：[已處理 N 筆: H-id list ／ 不適用 M 筆（id＋一句理由）／ 無待接手]
index.md 狀態變更：[page: 舊狀態→新狀態 or 無]
```

> lint 專用回報格式的「轉知處置」欄必須與 `.claude/reporter-rules/wiki-reporter-shared.md` 的回報契約同步 `[加入: 2026-08-28]`（沿革檔 2026-08-28 A）。

## 5f devpractice 週彙整 prompt 首段

住 `.claude/skills/wiki-lint-sweeps/references/sweeps.md`「5f」節，本檔不重抄。

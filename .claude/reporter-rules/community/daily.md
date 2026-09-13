# Wiki Ingest — 社群記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/community/pages.md`，週更（lint）工作見 `.claude/reporter-rules/community/weekly.md`。

分類為「社群」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/community-tech-patterns.md` | 工作流模式、multi-agent 設計、最佳實踐 |
| `wiki/topics/community-tech-discussions.md` | HN / Reddit 熱門技術討論 |
| `wiki/topics/code-quality-decline.md` | 「Claude 變笨了」的三條線：官方已結案的 2026-03～04 退步、06 月起的 token 消耗異常、Opus 5 上線後的品質觀感；以及模型釘選與自我量測。**單一模型自身的社群觀感歸模型記者的 [[entities/opus-5]]，逐個 issue 的缺陷歸功能記者的 [[entities/claude-code]]，本頁只記「線」的狀態** |
| `wiki/topics/community-large-codebase-workflow.md` | 🗓️ **週更，每日 ingest 不寫此頁**——每日只在 patterns 節點標 `**主線：**` tag（見下方「主線 tag 規則」）；週更整線重寫規則見 `.claude/reporter-rules/community/weekly.md` |
| `wiki/topics/llm-wiki-pattern.md` | 日報出現 LLM wiki／Karpathy wiki 的實作或設計討論，或 [[topics/skill-interest-watch]]「LLM 知識庫／文件策展／知識傳承」類出現竄升者且該 repo 屬此模式；表格契約見 `.claude/reporter-rules/community/pages.md` |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🌐 社群 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

> `wiki/topics/community-tech-tools.md` 已改為 **lint 專用**，每日 ingest 不更新此頁。策展規則見 `.claude/reporter-rules/community/weekly.md`。

**分流鐵則：** GitHub Issues 條目屬功能記者（claude-code 已知問題）；僅當該 issue 引發跨平台討論（HN/Reddit 也在延燒）才作為 discussions 條目收錄。

**官方內容不是你的禁區 `[加入: 2026-08-16]`：** 「社群」是內容型態的類別名，不是出處篩選器——官方部落格、官方文件、Anthropic 員工具名發言，只要談的是技術討論或工作流模式，一樣是你的條目（discussions 的收錄門檻本就明列「重要人士具名表態」；patterns 的觸發條件從未限制出處）。與功能記者的界線依**它給讀者什麼**分：官方提出**可被複用的新工作流模式／agent 設計** → 你收進 patterns 並標明官方出處，與社群模式並列比較；官方講**怎麼用既有功能**（省 token、session 經營、設定建議） → 那是功能記者的 `topics/coding-workflow-guide`，你不寫。完整對照表見 `.claude/skills/wiki-ingest/references/classification.md`「分流鐵則：官方內容不是社群類的禁區」。

**產品化矩陣轉知 `[加入: 2026-07-04]`：** 發現新的 agent 工作模式（patterns 頁新增條目）時，在回報中註明「請主編轉知功能記者評估產品化矩陣新增列」；`wiki/topics/official-community-gap.md` 的矩陣由功能記者維護，社群記者不直接寫該頁。

**dev.to 條目以內容判斷、不看讚數 `[加入: 2026-07-10]`：** dev.to 走 `top=30` 抓法（過去 30 天高互動文章），但**讚數在 dev.to 幾乎不能當品質指標**——最有價值的第一手實作文讚數常只有 2–3，反而 SEO 農場文有 5–6 讚。因此 dev.to 條目一律**用內容判斷收錄，不套互動門檻對照表的數字**：

- ✅ **優先收**：「我做了 X、這是怎麼運作 / 踩了什麼坑」的第一手實作、可複用 pattern、具體工具或量化實測（歸 `community-tech-patterns.md`）
- ❌ **排除**：`Complete Guide` / `Everything you need to know` 型 SEO 農場文（常來自 `ai_made_tools`、`tokenmixai` 等內容農場帳號）；純新聞轉述（定價、發布、事件解釋——這些已由媒體/HN 來源覆蓋，dev.to 版本無獨特價值）；純帶貨 / growth hacking 自我推銷

> 判斷原則：dev.to 的獨特價值是「工程師第一手實作經驗」，不是新聞或教學索引。內容答不出「作者具體做了什麼、學到什麼機制」→ 不收。

---

## community-tech-discussions 收錄門檻 `[加入: 2026-06-28]`

此頁追蹤「思想碰撞」，訊號價值有**三個合法來源（滿足其一即可收錄）**：

| 訊號來源 | 收錄理由 | 最低門檻 |
|---------|---------|---------|
| **社群碰撞** | 多方驗證、正反交鋒 | 達對照表**低**門檻（見 `.claude/reporter-rules/shared.md` 互動門檻對照表），或同議題跨 2 個以上獨立來源（source_count ≥ 2）|
| **重要人士具名表態** | 因「誰說的」而有重量（Boris Cherny、Dario、Karpathy 等）| 具名 + 可信來源；同時回報人物記者更新對應 `entities/` 頁 |
| **重要媒體深度報導** | 因觸及面與報導深度（36Kr、Platformer、WSJ 等）| 報導本身有實質內容，非純轉載標題 |

**誠實標註原則（強制）：** 說明欄須標明訊號性質，熱度符號錨定真實信號強度，不可虛抬：

- 社群兩極化／跨平台廣泛熱議 → 🔥🔥🔥🔥+
- 單平台高互動／議題共鳴深 → 🔥🔥🔥
- 多次被引用／催生後續工具 → 🔥🔥
- **重要媒體/人士單一報導，無社群延燒 → 🔥**，且說明欄末註「（媒體報導，待社群接力）」或「（具名表態，無社群延燒）」

> 關鍵區分：🔥🔥 以上隱含「社群共鳴」，**無社群討論的單一報導不得標 🔥🔥 以上**，避免讀者誤判信號強度。
> 純標題轉載、無實質內容的媒體稿，仍不收錄。
> **這三個門檻管的是進不進 `## 最近在討論什麼`。要進 `## 現在吵到哪`，另外要過一關：這一則寫得出正反兩方各主張什麼**——寫不出就只是一則討論，不是一場爭論。

---

## community-large-codebase-workflow 主線 tag 規則（daily）`[加入: 2026-08-05，改版: 2026-08-15]`

`community-large-codebase-workflow.md` 是把 patterns 節點沉澱成四條主線的**週更**頁；patterns 收「節點」（每日 append），主線頁每週從 patterns **整線重寫**（規則見 `.claude/reporter-rules/community/weekly.md`）。**每日 ingest 不寫主線頁**——每天只看一個節點的記者，結構上只做得到「往段尾加一句」，縫合需要看完整條線再重寫，那是週更的事。

**每次為 `community-tech-patterns.md` 新增節點時，多填一個欄位：**

```
- **主線：** 並行規模 ／ Context 管理 ／ 索引記憶 ／ 除錯分工 ／ —
```

- 判準是「這個節點回答的是**大型 codebase 特有**的痛點嗎」——並行 agent 互踩／context 被工具輸出撐爆／agent 記不住跨 session 決策／多 agent 產出誰把關；小專案也會遇到的通用技巧填 `—`
- 可複選（頓號分隔）；拿不準填 `—` 並在「與既有模式的關係」寫一句理由，週更時記者會再判
- 這個欄位是週更唯一的撈料依據（`Grep "\*\*主線：\*\* [^—]"`），漏填等於該節點對主線頁不存在
- 某類節點反覆出現卻無線可歸 → 不自行開線，回報主編轉知 weekly-review 評估第五條線

---

## 官方功能的負向對照要回流 `[加入: 2026-09-05]`

社群條目若**拿某個官方功能當對照組**、宣稱替代方案在成本／準度／速度上更好（無論該條目是否達本頁收錄門檻），在回報「同步自查」欄寫一行：
`⚠️ 需主編轉知功能記者：[官方功能名] 出現負向對照（來源＋日期＋證據等級：如「單一 Reddit 貼文，未附測試方法」）`。
你不寫該功能的 entities 頁，只負責讓這則證據被看見——它結構上只會經過你手上。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄；`feature-radar 新增` 欄恆填「無」（功能條目由功能記者提報）。

---
name: wiki-lint-reader-acceptance
description: /wiki-lint D 段：讀者模擬驗收（步驟 7）與歷史質疑代打（7b）——三種目標讀者各出一題走 3 跳驗收，再從題庫抽 2 題跑探針。
disable-model-invocation: true
---

# Wiki Lint — D 段：讀者驗收與質疑代打（7、7b）

由 `.claude/skills/wiki-lint/SKILL.md` 在規則健檢之後帶起。兩步的分工：**7 出「本週熱點」的讀者題，7b 抽「考卷外」的系統質疑題。**

兩步的回報行原樣填進步驟 8 的 lint 紀錄（模板見 `.claude/skills/wiki-lint/references/log-format.md`）。

---

## 7. 讀者模擬驗收

站在三種目標讀者（先 Read `.claude/rules/collection-scope.md`「目標讀者」）的角度各出一題**本週真實會問的問題**（從近 7 天日報事件取材），模擬讀者從 `wiki/index.md` 出發：

| 讀者 | 問題類型範例 |
|------|------------|
| Claude Code 重度使用者 | 「現在該不該升版？」「X 功能壞了嗎？」 |
| AI 系統開發者 | 「Y 模式社群驗證結果如何？」「Z 的替代方案是什麼？」 |
| Anthropic 生態追蹤者 | 「W 政策事件現在進展到哪？」 |

**驗收標準：** 從 index.md 出發，**3 跳內**（index → 頁面 → 區塊）能否得到答案。

- ✅ 3 跳內找到 → 通過
- ⚠️ 找得到但超過 3 跳或散在多頁 → 修復：在最相關頁面補 callout / wikilink，或補 index.md 摘要欄
- ❌ 找不到 → 記錄至 log.md 待辦，回報使用者是否為結構性缺口

**回報格式：**
```
讀者模擬：（3 題結果：✅/⚠️ 已修復/❌ 待辦，各附一句說明）
```

## 7b. 歷史質疑代打（題庫抽問）

讀 `.claude/skills/wiki-lint-reader-acceptance/references/inquiry.md` 後執行：跑 `python scripts/inquiry_bank.py draw` 抽 2 題（seed 綁本 ISO 週，同週重跑同題），逐題執行探針、產出三態結果（✅ 附證據行／⚠️ 已修復／❌ 記待辦並回報使用者）。

> 這一步代打的是**使用者歷史質疑的已知模式**（溯源、缺席偵測、沉默質疑、讀者查找、可讀性、結構健檢、宣稱對帳、資產重用審計八種，蒸餾自 `wiki/log.md` Query 條目）；新型質疑仍靠使用者，`scripts/open_loops.py` 的人類質疑時效燈不因本步驟而熄滅。

**回報格式：**
```
質疑代打（7b）：（seed 與抽中題號，各題 ✅ 附證據行/⚠️ 修了什麼/❌ 待辦；時效燈亮時原樣轉述）
```

---

## 邊界

- 由主編（本機主 session 或雲端頂層 session）親做，不派工——出題與判斷「讀者會不會迷路」是本步的全部內容。
- 修復只能補 callout／wikilink／index 摘要欄；❌ 的結構性缺口只回報、寫進步驟 8 的待使用者確認區，不自行拆頁建頁。
- `news/` 唯讀、`log.md` 只能 append、繁體中文為主：見 `wiki/CLAUDE.md`「🚫 絕對限制」。
- 驗證閘：7 的三題與 7b 的兩題各有明確三態結果（❌ 者已留待辦）才算完。

> **沿革檔：** `docs/rules-changelog/wiki-lint.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍）

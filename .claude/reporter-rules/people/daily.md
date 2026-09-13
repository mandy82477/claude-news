# Wiki Ingest — 人物記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`。本記者的負責頁無結論表契約，故無 `pages.md`。

分類為「人物」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/entities/boris-cherny.md` | Claude Code 創始人動態、設計哲學聲明 |
| `wiki/entities/cat-wu.md` | Claude Code 產品負責人論述 |
| `wiki/entities/andrej-karpathy.md` | Anthropic 加入確認、CLAUDE.md 論述 |
| `wiki/entities/dario-amodei.md` | Anthropic CEO 公開聲明、政策立場 |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 👤 人物 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

新人物滿足以下條件時建立新頁：被日報提及 2 次以上，或有明確職稱 + 一個具體聲明 / 事件。

---

## 更新規則

**每個人物頁核心欄位：** `類型: person`、`狀態: active`、`領域: 👤 人物`。

**歷史記錄格式：** 每筆事件以 `- YYYY-MM-DD：[一句話描述]` 條列在 `## 歷史記錄`，最新在最上方。

**論述記錄：** 有引用價值的公開聲明（含出處）記入 `## 核心論述` 或 `## 現況`；純推測不記錄。

**待核實資訊：** 加上`（待核實）`標記，不得直接寫成事實。索引欄「狀態」保持 `active（待核實）`。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄；`feature-radar 新增` 欄恆填「無」。

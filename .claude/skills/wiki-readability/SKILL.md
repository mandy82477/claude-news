---
name: wiki-readability
description: 低成本可讀性掃描：單一 agent 只讀每頁開頭與結構，找出冷讀者會迷路的頁面，回報後由使用者決定修哪些。
---

# Wiki 可讀性掃描

不定期執行（建議每 2–4 週，或大量 ingest 後）。與 `.claude/commands/wiki-lint.md` 的分工：lint 檢查結構正確性（矛盾、孤立、格式標準），本 skill 只看**讀者視角的可讀性**，且刻意用最省 token 的取樣方式。

---

## 1. 派一個背景 Agent

用 **Agent tool**（`run_in_background: true`）派**一個** agent，不派六記者——可讀性問題九成暴露在頁面開頭與結構層，單一視角掃全站反而更容易發現跨頁共通毛病。

派工 prompt **逐字讀 `.claude/skills/wiki-readability/prompt.md` 貼入**（含省 token 鐵則、五項評分、輸出格式），`{TODAY}` 替換為今日日期。

## 2. 收到報告後

1. 把「最需要處理的 5 頁」與共通問題呈現給使用者，**等待確認要修哪些**
2. 依確認結果修復：單頁小修直接改；跨多頁的共通問題可派對應類別記者（見 `.claude/reporter-rules/wiki-ingest.md` 派工表）
3. 修復後在 `wiki/log.md` 末尾 append：

```
## YYYY-MM-DD 可讀性掃描

- 掃描頁數：N（✅ X / ⚠️ Y / ❌ Z）
- 已修復：（列出，若無則寫「無」）
- 使用者跳過：（列出，若無則寫「無」）
- 共通問題：（一句歸納 or 無）
```

---

## 邊界

- 由主 session 派工並收報；審查員 agent **只回報不修改**。
- 繁體中文為主；`log.md` 只能 append，`news/` 唯讀。
- 修復頁面時更新「最後更新」欄位（純格式修正不動「最後新聞更新」）。
- 本 skill 產出屬建議性質，**未經使用者確認不執行修改**；使用者確認為完成條件。

---
name: wiki-readability
description: 低成本可讀性掃描：單一 agent 只讀每頁開頭與結構，找出冷讀者會迷路的頁面，主編判定修哪些並直接修。
---

# Wiki 可讀性掃描

不定期執行（建議每 2–4 週，或大量 ingest 後）。與 `.claude/skills/wiki-lint/SKILL.md` 的分工：lint 檢查結構正確性（矛盾、孤立、格式標準），本 skill 只看**讀者視角的可讀性**，且刻意用最省 token 的取樣方式。

---

## 1. 派一個背景 Agent

用 **Agent tool**（`run_in_background: true`）派**一個** agent，不派六記者——可讀性問題九成暴露在頁面開頭與結構層，單一視角掃全站反而更容易發現跨頁共通毛病。

派工 prompt **逐字讀 `.claude/skills/wiki-readability/references/prompt.md` 貼入**（含省 token 鐵則、五項評分、輸出格式），`{TODAY}` 替換為今日日期。

## 2. 收到報告後

1. 主編逐頁判定「最需要處理的 5 頁」與共通問題修或不修，不修的寫理由
2. 判定要修的直接修：單頁小修直接改；跨多頁的共通問題可派對應類別記者（見 `.claude/skills/wiki-ingest/references/classification.md` 派工表）
3. 修復後在 `wiki/log.md` 末尾 append：

```
## YYYY-MM-DD 可讀性掃描

- 掃描頁數：N（✅ X / ⚠️ Y / ❌ Z）
- 已修復：（列出，若無則寫「無」）
- 判定不修：（列出並附理由，若無則寫「無」）
- 共通問題：（一句歸納 or 無）
```

---

## 邊界

- 由主 session 派工並收報；審查員 agent **只回報不修改**。
- 繁體中文為主；`log.md` 只能 append，`news/` 唯讀。
- 修復頁面時更新「最後更新」欄位（純格式修正不動「最後新聞更新」）。
- 修不修由主編判定；完成條件是報告每一頁都有「已修復」或「判定不修＋理由」，回報只寫做了什麼。

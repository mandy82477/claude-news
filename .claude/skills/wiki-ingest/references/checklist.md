# Wiki Ingest 彙整寫入規則與完成核對

`.claude/skills/wiki-ingest/SKILL.md` 步驟 4 與步驟 5 的格式單一來源。步驟順序不在本檔。

## 共用檔案逐檔寫入規則（步驟 4）

**`wiki/feature-radar.md`**
- 彙整模型 + 功能記者回報的所有 feature-radar 新增條目
- 依 `.claude/reporter-rules/features/pages.md` 的條目格式寫入「最新功能」區塊
- 同步更新全覽表的熱度與試用價值
- 依 `.claude/reporter-rules/features/pages.md`「⭐ 現在值得跟的三件 自動更新規則」覆寫 `## ⭐ 現在值得跟的三件` section
- 依 `.claude/reporter-rules/features/pages.md`「⚠️ 從你現在的版本升上去，會遇到什麼 自動更新規則」更新 `## ⚠️ 從你現在的版本升上去，會遇到什麼` section

**`wiki/index.md`**
- 彙整所有記者回報的 `index.md 狀態變更` 欄位，逐一更新
- 彙整所有記者回報的 `新增頁面` 欄位，在對應分類下補上新連結

**`wiki/log.md`**（append only，不可修改既有條目）
```
## YYYY-MM-DD Ingest

- 來源日報：[[news/YYYY-MM-DD]]
- 更新頁面：（彙整所有記者的「更新頁面」列表）
- 新增頁面：（彙整所有記者的「新增頁面」，若無則寫「無」）
- 摘要：（一句話說明今日主要新聞方向）
- 呈現品質：（彙整所有記者的品質審查結果；全數通過則寫「全部通過」）
- 品質備註：（若彙整時發現記者品質問題——回報含糊、漏同步自查、格式退化等——每項一行 `[類別] [問題型態一句話]`；無問題則不寫此行）
```

**`data/source_attribution.jsonl`**（append only，不可修改既有行）
- 把所有記者回報的「來源歸因」欄逐筆轉成一行 JSON append，schema：

  ```json
  {"date": "<日報日期>", "source": "<slug>", "category": "<六類別>", "page": "<wiki相對路徑不含.md>", "item_url": "...", "item_title": "..."}
  ```

  slug 對照表見 `.claude/reporter-rules/shared.md`「來源歸因回報」；schema 詳細說明見 `data/README.md`
- 記者回報「無」則該記者不寫；全部記者皆「無」則不動此檔

**`data/pending-handoffs.jsonl`**（轉知帳本，append only，透過腳本操作）
- 記者回報「轉知處置」欄的「已處理」→ 逐筆 `python scripts/pending_handoffs.py close H-xxxxxx --by [類別] --result "[一句話]"`；「不適用」→ 判斷：理由成立則 `void`，理由是「不屬我」則保留 open 並改派（重新 `open` 給正確類別後 `void` 原筆）
- 記者回報「同步自查」欄出現 `⚠️ 需主編轉知[目標類別]記者：…` 且目標是**另一位記者**（非主編自己的彙整工作）→ `python scripts/pending_handoffs.py open --from [來源類別] --to [目標類別] --page [頁面] --note "[要做什麼]"`；今日就能在同一輪派工內解決的（目標記者尚未派出）可直接附進其派工訊息並同時登帳
- 主編自己要做的（feature-radar、index、commitments）不登帳，照步驟 4 做

**`wiki/overview.md`**（視情況）
- 若有重大事件（新模型發布、重大政策變化），更新「當前局勢」段落

---

## 完成前強制核對清單（步驟 5）

**在宣告完成之前，逐項確認所有項目已完成。**

- [ ] 每個有條目的類別均已派工，記者回報已收齊
- [ ] 六記者回報的「待查證命中處置」欄皆有值（已標訊／證據不足不動／無命中，三選一，不可空白或省略）
- [ ] 六記者回報的「轉知處置」欄皆有值，且已處理者已 `close`、新轉知已 `open` 登帳（`python scripts/pending_handoffs.py list` 的結果與記者回報一致）
- [ ] feature-radar.md 已彙整更新（無新功能則標「本日無新功能」）
- [ ] wiki/index.md 狀態已全部同步（含所有記者回報的狀態變更）
- [ ] wiki/log.md 已 append 本次 ingest 紀錄（含品質審查彙整，未修改既有條目）
- [ ] data/source_attribution.jsonl 已 append 所有記者回報的來源歸因（每筆一行 JSON；全部回報「無」則跳過）
- [ ] 未在 `CLAUDE_NEWS/wiki/` 以外路徑建立或修改任何 wiki 檔案

## 完成摘要表

| 項目 | 內容 |
|------|------|
| 日報來源 | news/YYYY-MM-DD |
| 參與記者 | [有條目的類別列表] |
| 更新頁面 | [彙整列表] |
| 新增頁面 | [列出或「無」] |
| feature-radar 變動 | [功能名稱與熱度變化，或「無」] |
| 今日主要方向 | [一句話摘要] |

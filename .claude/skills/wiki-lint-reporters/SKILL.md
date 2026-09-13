---
name: wiki-lint-reporters
description: /wiki-lint A 段：載入 wiki 全貌、六記者並行 lint 派工、收報兩層核對、月度蒸餾，再處理語意分岔候選、新實體頁與 overview 改寫。
disable-model-invocation: true
---

# Wiki Lint — A 段：六記者派工與收報（步驟 1–5）

由 `.claude/skills/wiki-lint/SKILL.md` 最先帶起。**派工 prompt 全文與記者回報格式住 `.claude/skills/wiki-lint-reporters/references/dispatch.md`，派工前逐字讀它**，本檔只寫步驟。

---

## 1. 載入 wiki 全貌

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/skills/wiki-ingest/references/classification.md` — 分類表、分流鐵則與派工正典
- `.claude/reporter-rules/page-templates.md` — 頁面格式模板、欄位規則、品質標準
- `wiki/index.md` — 取得所有頁面清單
- `wiki/log.md` — 了解最近的 ingest 紀錄與活動

## 2. 並行派工（六位記者同時執行）

對每個類別呼叫 Agent tool，在**同一訊息中並行發出全部六個呼叫**。**派工前綴（類別↔角色檔對照表＋第一段角色前導）逐字讀 `.claude/skills/wiki-ingest/references/dispatch.md`**（ingest 與 lint 共用同一份，本段不另抄）；接在它後面的 lint 專屬段與記者回報格式照 `.claude/skills/wiki-lint-reporters/references/dispatch.md`。

**收報核對（自我遵守率）：** 主編收到每份回報後，執行兩層核對：

1. **形狀層**：逐項核對 3a–3h 八項 ＋ 轉知處置，**共九項是否各有明確結果**（具體頁名＋結論，而非籠統一句「全部通過」；「無」也算明確結果，但須看得出該項有被執行）。缺項或含糊者以 SendMessage 退回該記者補做，不得代填
2. **行為層抽驗（每輪至少 1 次）**：從六份回報中隨機抽 1 位記者的 1 項「已修復／已更新」宣稱，**主編親自開檔核對 diff 是否如實**（`git diff` 或直接讀該頁對應段落）。不符即退回，並在 log 記「抽驗不符：[記者][項目]」。**抽選必用擲骰，不可自由心證**：先把六份回報中所有「已修復／已更新」宣稱編號列成清單（共 N 項），再跑 `python -c "import random,datetime;iso=datetime.date.today().isocalendar();random.seed(f'{iso[0]}-W{iso[1]:02d}');print(random.randint(1, N))"` 取抽中編號（N 代入實際項數；seed 綁 ISO 週，同週重跑同結果、不可重擲換題）

核對結果（N/6 位一次過、**退回原因**、抽驗結果）記入步驟 8 log。

> 行為層抽驗的依據：**連續滿分與抓不到問題是同一枚硬幣**；對照全域 `REVIEW-PRINCIPLES.md` A1（不信回報、獨立重驗）。（沿革檔 2026-08-28 B）

**月度蒸餾（記者成長迴路）：** 僅每月第一次 lint 執行（判斷法見 `.claude/skills/wiki-lint/SKILL.md`「月度判斷法」），其餘週次輸出「非本月首次 lint，跳過月度蒸餾」。

1. grep 過去 30 天 `wiki/log.md` 的**「退回」**記錄（收報核對段落）與**「品質備註」**行（ingest 紀錄，見 `.claude/skills/wiki-ingest/references/checklist.md` 的 log 模板）
2. 按「記者類別 × 錯誤型態」統計出現次數
3. **同一型態 ≥ 2 次**者產出立法提案；僅 1 次者只列入「觀察中」清單，不立法

提案格式：
```
| 記者 | 錯誤型態 | 次數 | 建議條文 | 目標檔案與節 | 新增/改寫 |
```
- 若該錯誤**已有對應規則仍重複違反**，提案一律為**改寫既有條文使其更明確**，不新增
- 提案**向使用者確認後才寫入**；寫入依 `.claude/rules/claude-md-edit.md` 流程，完成後執行 `/review-commands` 直到零錯誤

輸出：
```
🌱 月度蒸餾（記者成長迴路）：
  立法提案（N 條）：
  | 記者 | 錯誤型態 | 次數 | 建議條文 | 目標檔案與節 | 新增/改寫 |
  觀察中（僅 1 次，K 條）：[列出或「無」]
❓ 是否採納以上提案？（全部 / 部分 / 皆否）
```

## 3. 處理語意分岔／死案歸檔候選（需使用者確認）

收齊所有記者回報後，彙整 3f 中回報的語意分岔或死案候選（若無候選，此步驟直接跳過）。以下列格式呈現並**等待使用者確認**：

```
📄 [頁面名稱]（XXX 行）發現[語意分岔 / 死案段落]

記者分析：
- [說明分岔成兩個獨立故事的具體內容，或死案段落內容與無引用佐證]

建議方案：
- [語意分岔]：拆為 [新頁面 A] / [新頁面 B]
- [死案歸檔]：歸檔至 [目標頁面]

❓ 請確認：是否同意處理？分類是否正確？命名是否OK？
```

根據使用者回應執行處理或記錄為待辦。

## 4. 建議並建立新實體頁

掃描所有頁面（可用 Grep），找出被提及 3 次以上但尚無專頁的名稱（模型、功能、人物、產品）。
→ 建立對應的 entities/ 頁面，填入目前已知資訊。
→ 在來源頁面補上 wikilink。

## 5. 更新 wiki/overview.md

重寫 `wiki/overview.md` 的內容，反映當前局勢：
- 目前最活躍的議題（ongoing topics）
- 近兩週的重大事件摘要
- 值得持續關注的趨勢

---

## 邊界

- 由主編（本機主 session 或雲端頂層 session）執行；六個派工在同一訊息並行發出，記者不可再呼叫 Agent tool 委派。
- 步驟 3 的語意分岔／死案歸檔**必須等待使用者確認才能執行**，記者只負責回報分析。
- 每次修改頁面都必須更新「最後更新」欄位；`news/` 唯讀、`log.md` 只能 append、繁體中文為主：見 `wiki/CLAUDE.md`「🚫 絕對限制」。一頁一故事：resolved 議題留在原路徑，不遷移。
- 驗證閘：六份回報各九項皆有明確結果、行為層抽驗至少 1 次且結果已記，才算本段完成。

> **沿革檔：** `docs/rules-changelog/wiki-lint.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍）

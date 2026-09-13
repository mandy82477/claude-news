---
description: 每週總指揮：依序跑週報產出（對外交付）與 wiki 週度延伸回顧（對內策展），最後統一收尾單一 push。
argument-hint: [YYYY-Wnn]
---

# Weekly — 每週總指揮

**每週只要下這一個指令。** 它依序帶起三段工作，最後統一收尾：

| 順序 | 規範檔 | 性質 | 產出 |
|---|---|---|---|
| 0 | `.claude/skills/weekly-local-catchup/SKILL.md` | 本機專屬補跑 | 5b 榜單週更、5c 清算、lint 待裁示呈報、開放迴路掃描 |
| 1 | `.claude/skills/weekly-report/SKILL.md` | 對外交付 | `weekly/YYYY-Wnn.md`（凍結存檔） |
| 2 | `.claude/skills/wiki-weekly-review/SKILL.md` | 對內策展 | `wiki/` 頁面加碼 + `wiki/log.md` |
| 3 | 本檔步驟 3 | 收尾 | commit + test + build + **單一 push** |

---

## 使用方式

- `/weekly`：跑本週（今日所在 ISO 週）
- `/weekly 2026-W30`：指定週次，`$ARGUMENTS` 原樣傳給 `/weekly-report`；`/wiki-weekly-review` 不吃週次參數，一律以今日為準

只想跑其中一段時，直接下該子指令（`/weekly-report` 或 `/wiki-weekly-review`），它們各自的收尾步驟會自己負責。

---

## 🔒 順序與邊界（不可調換、不可合併）

**執行順序固定為「週報先、策展後」**，且兩者是兩段獨立工作，不可揉成一段：確認閘相反、凍結語義衝突、帳本獨立性三者皆會被合併破壞（完整論證見沿革檔 `docs/rules-changelog/weekly.md` 2026-08-09）。

> 判斷式：**這一步會不會讓後面那步「已經知道答案」？** 會 → 順序錯了。

---

## 步驟

### 0. 本機專屬步驟補跑（先做，不可略過）

讀 `.claude/skills/weekly-local-catchup/SKILL.md` 並依其四項執行（5b/5c 等探測式補跑、lint 待裁示呈報、開放迴路掃描與三個數字）。第 3、4 項的輸出原樣抄進本指令的回報；四項產出一律併入步驟 3 的單一 push，不自行 commit。

### 1. 週報產出（對外交付）

讀 `.claude/skills/weekly-report/SKILL.md` 並依其步驟 1–5 執行，`$ARGUMENTS` 原樣傳入。

**跳過該檔的步驟 6（收尾閉迴路）**——commit / build / push 一律留到本檔步驟 3，避免兩次 push 觸發兩個 GitHub Pages 部署互相搶佔。

### 2. wiki 週度延伸回顧（對內策展）

讀 `.claude/skills/wiki-weekly-review/SKILL.md` 並依其步驟 1–5 執行（含六記者並行判斷、月度聚焦校準判斷、`wiki/reader-notes.md` 收件匣消費、彙整清單交使用者確認、依確認執行、log 記錄）。

- **使用者確認閘保留**：步驟 3 的建議清單仍須經使用者確認才可執行修改，本指令不代為決定
- **跳過該檔的步驟 6（收尾閉迴路）**——同上，留到步驟 3
- 使用者若回「都不要」，仍須照該檔規定 append log.md 那一筆

### 3. 統一收尾閉迴路

兩段都跑完後才執行。`REPO_ROOT` = `git rev-parse --show-toplevel` 所得，`PYTHON` = PATH 上的 `python`（雲端為 `python3`）：

0. **重掃涵蓋窗與預告探針（在 commit 之前，不可略過）**——重列一次 `news/` 目錄，與步驟 1 寫進週報檔尾的涵蓋窗比對：
   - **有新日報**（開工後才產出者）→ 對這幾份補跑第 (3) 段所有續盯／新開條的 `｜查證：` 關鍵字 grep。命中且足以改變某列判定 → **改判該列，並在該列與檔尾標明更正緣由**；命中但不足以改判 → 檔尾註明已補掃。**選題與深挖不回頭改**（`.claude/skills/weekly-report/SKILL.md` 步驟 5 凍結原則），補掃只修正「會讓讀者被誤導的事實判定」
   - **無新日報** → 什麼都不做，繼續第 1 步
1. commit 範圍與訊息（無變更則跳過）：`git -C REPO_ROOT add weekly/ wiki/ data/source_attribution.jsonl` → `git -C REPO_ROOT commit -m "weekly: YYYY-Wnn 週報＋週度延伸回顧"`；web commit 訊息用 `"web: rebuild YYYY-Wnn（週報＋週度回顧上站）"`
2. **其餘照 `.claude/skills/web-publish/SKILL.md` 的 `Step 4`／`Step 5` 形狀做，不另寫一套**：測試閘（`run_tests.py` 失敗 → 跳過 build 與 web commit，仍推送已完成的 commit，回報標「Tests FAILED - build skipped」）、`build_web.py` → add `web_reader/` → commit、**單一 push**、push 失敗重試（`pull --rebase` 上限 2 次）

- **`pull --rebase` 若帶進新的 `news/*.md`，回第 0 步重跑補掃**——rebase 正是新日報最常進入本機的路徑（W34 病例見沿革檔 `docs/rules-changelog/weekly.md` 2026-08-22）
- **與排程的關係**：本指令無雲端排程。`weekly/` 不與任何排程重疊；`wiki/` 會與 `weekly-wiki-lint-cloud`（每週六 03:00 UTC（台北 11:00））及 `daily-news-pipeline-cloud`（每日 12/17/22 UTC 三班，涵蓋台北 20:00 至隔日 06:00）競爭，靠上述 push 重試化解

---

## 完成回報

```
## Weekly YYYY-Wnn

- 週報：weekly/YYYY-Wnn.md（深挖題目：…）
- 延伸回顧：執行 N 項 / 使用者跳過 M 項
- 聚焦校準：（月度才有，或「非本月首次，跳過」）
- 開放迴路：需收尾 N／已跳票 M／存量遷移 K（人類質疑時效燈：✅／⚠️ N 天）
- 收尾：涵蓋窗補掃（新日報 N 份／無）｜測試 ✅／❌｜build ✅／跳過｜push ✅
```

---

## 注意事項

- 繁體中文為主
- 三段的規則以其各自的規範檔為準，本檔只負責**順序、邊界與收尾**，不重複它們的內容規範（避免兩處失步）
- 三段的收尾步驟被本檔接管——修改任一段的收尾段落時，必須同步確認本檔步驟 3 仍涵蓋其產出路徑

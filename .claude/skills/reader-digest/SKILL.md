---
name: reader-digest
description: 每日 pipeline Step 2b：取當日 wiki diff 寫 daily/ 讀者版並跑格式閘；由呼叫 /news-pipeline 的 session 在 ingest 後親自執行。
---

# Step 2b：讀者版日報（`daily/TARGET_DATE.md`）`[加入: 2026-09-12]`

**與 Step 2 一樣由呼叫 `/news-pipeline` 的 session 親自執行**（雲端則是頂層 session 一條龍做完），**排在 Step 2 wiki ingest 之後、Step 3 commit 之前**。

讀者版回答的不是「今天發生什麼」，是「**知識庫今天學到什麼、改變了什麼判斷**」。`news/TARGET_DATE.md` 照產照存（原料層，供 lint 5d／7b 溯源與各記者沉澱使用）。判準與取捨見沿革檔 2026-09-12。

格式契約（模板、機械契約字串、每條 ≤ 200 字元等條件、「不算學到」清單、主詞規則、網站版面）在 `.claude/skills/reader-digest/references/format.md`，本檔不重述。

---

## 步驟

1. **取當日 wiki diff**（就是本步的進料，不靠歸因記錄）：

   ```
   git -C REPO_ROOT diff HEAD --stat -- wiki/
   git -C REPO_ROOT diff HEAD -- wiki/<你要看的頁>
   ```

   **不需要基準 sha**：Step 2 只寫不 commit，wiki/ 的當日改動要到 Step 3 才進 git，所以本步執行時 `git diff HEAD -- wiki/` 就是今天全部的改動。若本次執行中途曾先 commit 過 wiki（如記者分批完成的 interim commit），改以那筆 commit 的前一個 sha 為基準：`git -C REPO_ROOT diff <sha> -- wiki/`。
2. **剔除不算「學到」的改動**：清單見 `.claude/skills/reader-digest/references/format.md`。
3. **寫 `daily/TARGET_DATE.md`**，格式與逐條條件全依 `.claude/skills/reader-digest/references/format.md`。
4. **長度自檢（強制）**：

   ```
   PYTHON scripts/check_reader_digest.py TARGET_DATE
   ```

   （檢查每條 ≤ 200 字元、六領域節名合法、條目恰好三段、wikilink 目標存在、事實句與總結句不含整理語；非零退出即違規，修好再收工）
5. **內規外洩自檢（強制）**：對 `daily/TARGET_DATE.md` 跑 `.claude/skills/news-digest/references/selection.md`「禁詞清單」節的 grep；另不得出現 `ingest`、`派工`、`記者`、`diff` 這類維運語——讀者看到的是知識，不是編輯部的工作流程。
6. `daily/TARGET_DATE.md` 隨 **Step 3** 一併 commit（見 `.claude/skills/web-publish/SKILL.md` 該步的 `git add` 清單），不單獨 commit、不單獨 push。

## 產出失敗時

本步失敗（寫不出來、diff 取不到）**不阻斷 pipeline**：Step 3～Step 6 照常跑，該日網站日報頁自動退回舊的 `news/` 解析結果（`build_web.py` 的退回路徑本來就是為改版日之前的歷史頁寫的），Step 6 log 記一行 `Reader digest FAILED - falling back to news/`。

---

> **沿革檔：** `docs/rules-changelog/news-pipeline-steps.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，`[加入: 2026-09-04]`）

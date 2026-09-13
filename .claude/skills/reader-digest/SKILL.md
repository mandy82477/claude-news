---
name: reader-digest
description: 每日 pipeline Step 2b：把各 wiki 頁當日 callout 投影成 daily/ 讀者版並跑格式閘；由跑 /news-pipeline 的 session 親做。
---

# Step 2b：讀者版日報（`daily/TARGET_DATE.md`）

**與 Step 2 一樣由呼叫 `/news-pipeline` 的 session 親自執行**（雲端則是頂層 session 一條龍做完），**排在 Step 2 wiki ingest 之後、Step 3 commit 之前**。

讀者版是**各頁頂部「最新動態」callout 的投影**：記者在 Step 2 把當日 delta 覆寫進頁頂 callout（括號日期＝TARGET_DATE），本步用腳本把它們按六領域原樣列出來——不重新消化、不改一字。每個事實只有一個家（頁頂 callout），日報不是第二份。`news/TARGET_DATE.md` 照產照存（原料層，供 lint 5d／7b 溯源與各記者沉澱使用）。判準與取捨見沿革檔 2026-09-12、2026-09-13 丙。

格式契約（機械契約字串、挑選規則、模板、網站版面）在 `.claude/skills/reader-digest/references/format.md`，本檔不重述。

---

## 步驟

1. **產出（機械）：**

   ```
   PYTHON scripts/build_reader_digest.py TARGET_DATE
   ```

   腳本掃 `wiki/entities/`、`wiki/topics/` 頁首，收括號日期＝TARGET_DATE 的 callout，按 frontmatter `domain` 分六節寫 `daily/TARGET_DATE.md`；零命中自動寫「今日 wiki 無新知」行。**看 WARN 行**：`domain` 缺或不在六領域、頁首 callout 沒有可解析日期的頁，腳本會點名——那是該頁的記者要修的（規則在 `.claude/reporter-rules/page-templates.md`「頂部 delta-first callout」），本步不替他改頁，只把 WARN 抄進完成摘要的「📋 待使用者裁示」。另一種 WARN 是「聚焦第 N 條的來源既不在當日歸因帳本、也未出現在今日更新的頁」——多半是記者漏收，同樣抄進待裁示，不在本步補收。腳本同時把 `news/TARGET_DATE.md` 的 📌 今日聚焦與剔重後的 ⭐ 重點話題搬到檔首（規則見 format.md「頂部兩節」）。
2. **格式閘（強制）：**

   ```
   PYTHON scripts/check_reader_digest.py TARGET_DATE
   ```

   （六領域節名合法、頁面小節指到存在的頁、callout 首行日期＝檔名日期、無散落 `>` 行；非零退出即違規，修好再收工——正常情況產生器的輸出必過，不過代表產生器與閘失步，要修腳本不是修檔）
3. **內規外洩自檢：** callout 是記者寫給讀者的，理論上已乾淨；仍對 `daily/TARGET_DATE.md` 跑 `.claude/skills/news-digest/references/selection.md`「禁詞清單」節的 grep。命中時**改該頁的 callout**（那才是家），改完重跑第 1 步。
4. `daily/TARGET_DATE.md` 隨 **Step 3** 一併 commit（見 `.claude/skills/web-publish/SKILL.md` 該步的 `git add` 清單），不單獨 commit、不單獨 push。

## 產出失敗時

本步失敗（腳本例外）**不阻斷 pipeline**：Step 3～Step 6 照常跑，該日網站日報頁自動退回舊的 `news/` 解析結果（`build_web.py` 的退回路徑本來就是為改版日之前的歷史頁寫的），Step 6 log 記一行 `Reader digest FAILED - falling back to news/`。

本步只讀已寫在磁碟上的 wiki 檔，**不依賴未 commit 的 diff**；補跑歷史日期（`/wiki-backfill`）時對該日期重跑第 1 步即可，前提是記者當天有把 callout 日期寫成該日。

---

> **沿革檔：** `docs/rules-changelog/news-pipeline-steps.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，）

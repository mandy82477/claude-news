---
paths:
  - "src/**"
  - "scripts/**"
  - ".claude/**"
  - "web_reader/assets/**"
  - ".github/workflows/**"
---
# 開發完工定義（Definition of Done）

改 pipeline、script、hook、規則檔或 web reader 程式時讀此檔。只改 `wiki/` 內容不算開發，不受本檔約束。

**改動未閉迴路不算完成。** 三者到齊才標「完成」，缺一標「進行中」：

1. **測試綠**：`python scripts/run_tests.py` 通過。`.claude/hooks/check_tests_on_stop.py`（Stop hook）會在 `src/`、`scripts/`、`.claude/hooks/`、`web_reader/assets/` 有未 commit 改動且測試未綠時擋收工；規則檔另由 `check_rules_on_stop.py` 看守。
   `web_reader/` 只有 `assets/`（手寫 CSS 與 JS）在監看範圍內；`data/`、`index.html`、`sw.js` 是 `build_web.py` 的產物，收進來會讓每次建置都強迫重跑整套測試。
2. **已 commit**：非 data 檔的改動已進 git。data 檔（`gathered_items.json`、`emitted_items.json`、`seen_urls.json`）例外。commit 一律指名路徑，`block_git_add_all.py` 擋 `git add -A` / `git add .`。
   **多 session 共用工作樹時**：進入寫入階段前在 `.claude/tree-claims/<session_id>.json` 宣告你要動的路徑前綴（`{"session":…,"paths":["wiki/"],"note":"在跑什麼"}`），`block_foreign_stage.py` 會擋下把別人宣告中的路徑 add 進你的 commit。指名路徑**不足以**防這件事——2026-09-13 有 session 指名 `wiki/` 就掃走了另一個 session 的半成品。
3. **依賴缺口已登記**：改動若依賴尚缺的憑證、服務或真解，在 `docs/workaround-register.md` 登記 owner 與複查日，不可只留在對話裡。

> **判斷式：** 這個 commit 的訊息，說得出裡面每一個檔案為什麼在嗎？說不出，你 add 太多了。

第 1、2 條有 hook 兜底，第 3 條只有人能判斷。沿革見 `docs/rules-changelog/CLAUDE.md` 2026-09-13。

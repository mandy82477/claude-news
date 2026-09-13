---
name: wiki-lint
description: 每週執行 wiki 品質檢查，修正矛盾/孤立/過期頁面，更新 overview。
---

# Wiki Lint — 總指揮

每週執行，檢查 wiki 品質並修正問題。建議在週末或週一執行。**本檔只排順序與收尾**，每段的步驟本體住各自的 skill，執行該段之前逐字讀它。

## 四段順序（A→E，依序執行，不並行）

| 段 | skill | 涵蓋步驟 |
|---|---|---|
| A | `.claude/skills/wiki-lint-reporters/SKILL.md` | 1 載入 wiki 全貌、2 六記者派工與收報兩層核對＋月度蒸餾、3 語意分岔候選、4 新實體頁、5 overview |
| B | `.claude/skills/wiki-lint-sweeps/SKILL.md` | 5a–5m 主編親做／親查的十三個掃描 |
| C | `.claude/skills/wiki-lint-rules-health/SKILL.md` | 6a–6l 規則檔健檢＋漏抓帳與規則版本戳 |
| D | `.claude/skills/wiki-lint-reader-acceptance/SKILL.md` | 7 讀者模擬驗收、7b 歷史質疑代打 |
| E | 本檔步驟 8／9／10 | 記錄 lint、更新 index、收尾閉迴路 |

- **A 必須先於 B**：B 的 5f（devpractice 週彙整）與 5k（社群三表）都要等六記者寫完才不互踩。
- **E 最後**：步驟 8 的 log 要收齊 A–D 全部回報行。
- 單段失敗不阻斷其餘段；該段回報行寫明失敗原因，並列入步驟 8 的待使用者確認區。

## 月度判斷法（A 段月度蒸餾、C 段 6g 指標二／6j 共用）

**判斷產出物，不判斷執行記錄：** 讀 `wiki/metrics.md`，本月各列的「採用驗證率」欄**尚無數值**（無列，或該欄皆為「非本月首次 lint，跳過」）→ 本輪即本月首次，執行月度項；已有數值 → 輸出「非本月首次 lint，跳過」並跳過。口徑與 `.claude/skills/wiki-weekly-review/SKILL.md`「月度加項」一致（同讀 `wiki/metrics.md`），兩者不得各用一套。

---

## 8. 記錄本次 lint

把 A–D 各段的回報行原樣填入模板，在 `wiki/log.md` 末尾 append。**模板住 `.claude/skills/wiki-lint/references/log-format.md`，寫之前逐字讀它**，不憑記憶重排欄位。

## 9. 更新 wiki/index.md

同步所有因本次 lint 造成的頁面新增、移動、狀態變更。

## 10. 收尾閉迴路：commit wiki + build web + 單一 push

**為何必要：** lint 只改 `wiki/*.md`，web build 僅發生於本步驟與 `/news-pipeline`。若跳過本步，本次修正不會出現在 web reader，得等下一次日更 pipeline 才上站。lint 結束前必須自行閉迴路（對齊 `.claude/rules/dev-done.md` 開發完工定義：測試綠 + 已 commit）。

依序執行（`REPO_ROOT` = `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS`，`PYTHON` = `C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe`）：

1. **Commit wiki 變更**（先不 push）：`git -C REPO_ROOT add wiki/` → `git -C REPO_ROOT commit -m "wiki: weekly lint YYYY-MM-DD"`（wiki 無變更則跳過 commit，續下一步）
2. **強制 web build gate**：`PYTHON REPO_ROOT\scripts\gate_web_build.py`。**擋下時的修復迴圈、放行判準與放寬邊界一律照 `.claude/skills/web-publish/SKILL.md` Step 4「gate 擋下時的修復迴圈」，本檔不另寫一套**（判準集中在腳本與該節裡，兩處才不會失步）——至多 2 輪仍擋下才跳過 build 與 web commit，仍執行步驟 4 推送已完成的 wiki commit。兩種結果都在步驟 4 的心跳紀錄抄上腳本輸出的**最後一行摘要**，不要自己改寫措辭
3. **建置 web 並 commit**：`PYTHON REPO_ROOT\scripts\build_web.py` → `git -C REPO_ROOT add web_reader/` → `git -C REPO_ROOT commit -m "web: rebuild YYYY-MM-DD（週更 lint 上站）"`
3b. **渲染層驗收（build 成功時必做）**：對本輪**改動最多的 2 頁**，看渲染後的結果，不是只看 markdown——

   - **本機**：瀏覽器實開該頁（web reader 本機路徑見 `.claude/rules/web-reader-design.md`），眼睛掃一遍：表格有沒有爆版、懸置標記 `⟨Q-nn⟩` 有沒有正常顯示、wikilink 有沒有變成裸字串
   - **雲端**（無瀏覽器）：`Read` 該頁的 build 產物（`web_reader/data/wiki/<slug>.json`），確認本輪改動的段落確實出現在產物中、且沒有被解析器吞掉
   - 發現渲染層問題 → 修 `web_reader/` 或改 wiki 寫法後重跑 build；修不掉則記入待確認區

 > **為什麼不能只信 build 綠燈**：`build_web.py` 只證明「資料層對」，不證明「讀者看到的東西對」；全域 `REVIEW-PRINCIPLES.md` 第 11 條明言 DOM／資料斷言不可替代眼睛驗收。（沿革檔 2026-08-09）

4. **心跳紀錄（無論成功／no-op／中止都必須寫）**：append 一行結果到 `src/logs/task_scheduler.log`（格式沿用該檔既有慣例，如 `[週六 YYYY/MM/DD hh:mm:ss.00] Weekly lint OK - 修 N 頁，M 項待確認，測試/build/push 結果`；no-op 寫 `Weekly lint OK (no-op) - 無頁面需修正`；中途失敗寫 `Weekly lint FAILED - <卡在哪一步>`）→ `git -C REPO_ROOT add src/logs/task_scheduler.log` → `git -C REPO_ROOT commit -m "chore: weekly lint heartbeat YYYY-MM-DD"`。**這一步是本步驟序列中唯一保證產生 commit 的步驟**——目的是讓「跑了但無事可改」與「靜默死亡」在 GitHub 上可分辨。對應每日 pipeline 的 `.claude/skills/web-publish/SKILL.md`「Step 6」（無論前面成敗都必須寫），本機與雲端行為一致。
4b. **命中帳（每輪必記）**：`python scripts/lint_health.py hits record --date YYYY-MM-DD --rules-rev <規則版本> --step 3a=N --step 3b=N … --step 7b=N`——每個執行過的步驟各一筆命中數（0 也要記，零命中才是訊號），`data/lint_step_hits.jsonl` 併入本步 push

5. **單一 push**：`git -C REPO_ROOT push`（本次所有 commit 一次推送，一次 push = 一個 Pages 部署，避免並發競爭）。**push 失敗的重試程序照 `.claude/skills/web-publish/SKILL.md` Step 5**，本檔不另寫一套

> 本步 commit 為實質改動閉迴路的一部分，**不可只留在對話裡**。心跳紀錄在中止情境下照樣執行——lint 中途放棄時，先寫 FAILED 心跳並 commit push 再結束，不可靜默離開。

---

## 邊界

- 由主編（本機主 session 或雲端頂層 session）執行；雲端的環境差異與待辦寫法見 `docs/cloud-runbooks/weekly-lint.md`，行為本體一律以四個子 skill 為準。
- 四段的「需使用者確認」項目一律只回報，收斂進步驟 8 的待使用者確認區，不自行動手。
- `news/` 唯讀、`log.md` 只能 append、繁體中文為主：見 `wiki/CLAUDE.md`「🚫 絕對限制」；wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下。
- 驗證閘：步驟 8 的 log 每一欄都有值、`gate_web_build.py` 綠（或已走完至多 2 輪修復迴圈並在心跳寫明）、單一 push 成功，才算完。

> **沿革檔：** `docs/rules-changelog/wiki-lint.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，）

# `.claude/skills/wiki-ingest/` 沿革（教訓存檔）

本檔是每日 wiki ingest 流程的歷史敘事，不是待執行規則；SKILL.md 條文處的教訓皆存於此，執行 ingest 時不必讀。

## 2026-09-13

`/wiki-ingest` 從舊 command 檔轉成 skill（`.claude/skills/wiki-ingest/`）。步驟語意、契約字串與判準逐字不動，只換家：類別↔角色檔對照表、六記者 prompt 模板、防偏誤說明、4b／4c prompt 首段移入同目錄 `dispatch.md`；共用檔案逐檔寫入規則、完成前強制核對清單、完成摘要表移入同目錄 `checklist.md`；下列兩則教訓敘事移入本檔。`$ARGUMENTS` 的日期改以 TARGET_DATE 稱呼（呼叫時傳入的參數仍是同一個值）。引用端（`.claude/skills/news-pipeline/SKILL.md`、`.claude/commands/wiki-backfill.md`、`.claude/reporter-rules/`、`.claude/skills/news-gather/`、`.claude/skills/news-digest/`、`docs/cloud-runbooks/daily.md`、`src/news_aggregator/main.py`）與 `.claude/review-registry.json` 同步改指新家。

## 2026-07-25（ingest 輸入不能只有日報）

抓料 73 則、日報收 38 則，其餘 35 則因為 ingest 的輸入只有日報，包含 61 留言與 47 留言的 GitHub Issue 在內，**沒有任何記者看過**。處置是步驟 1 強制執行 `scripts/list_digest_omissions.py`，把差集一起送進分類，原則寫成「不收可以，沒看過不行」。

## 2026-08-13（專頁定向條目不得因「跟 Claude 沒關係」而略過）

2026-08-05 Jeff Dean 等人離開 Google 創辦 Discovery Loop，因標題是 Google 視角而被 12 個來源全數漏掉 8 天。專頁定向抓來的條目標題天生不含 Claude／Anthropic——那正是它們被定向抓來的原因，因此收錄判準改用該專頁自己的觸發條件，不套用 Claude／Anthropic 關聯門檻。

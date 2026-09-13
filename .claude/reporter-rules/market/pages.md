# 投資分析記者：負責頁的表格契約

每日該做什麼在 `.claude/reporter-rules/market/daily.md`，主編層的週更結算與教材頁在 `.claude/reporter-rules/market/weekly.md`。

---

## topics/market-signals

### 結論表的歸屬：每日一張、每週兩張 `[改版: 2026-09-12]`

| 表 | 住哪頁 | 誰維護、何時 | 一列是什麼 | 欄位 |
|---|---|---|---|---|
| `## 買得到的標的` | `wiki/topics/market-signals.md`（摘要之後、判讀之前） | **你，每日**：判讀涉及上市公司時當天覆寫對應列 | 一個上市標的（主鍵＝代號）。入口：本頁有判讀提到它、或它是 Anthropic 的投資人；具名採用但無帶金額消息的上市公司不佔列，表下一句指 [[topics/enterprise-tool-tracker]] | 標的｜跟 Anthropic 的關係｜本頁判讀｜現在方向｜下一個催化劑 |
| `## 買不到的消息線（教材）` | `wiki/topics/market-lessons.md` | **主編，每週**（`/wiki-lint` 5h，見 `.claude/reporter-rules/market/weekly.md`） | 一條未上市主角的消息線（主鍵＝線名） | 線｜現在方向｜則數 · 最後一則｜下一個催化劑｜這條線的課 |
| `## 一課一課學` | `wiki/topics/market-lessons.md` | 同上 | 一課（主鍵＝課名；「複習：」開頭者不新增列，只在例題欄追加日期） | 課名｜下次怎麼認｜例題｜押對了嗎 |

你**只寫 `market-signals`**；教材頁唯讀。教材頁的兩張表從你每則判讀的「一眼」（線名、正負）、「下一個催化劑」與「一課｜課名」機械抽出，所以這三段的形狀要守住，課名 ≤ 12 字且同一課第二次出現寫「複習：課名」。

`## IPO 這條線，你要先懂的`（教材頁）是通用知識，不吃日報、記者不動；主編每週順檢它與 IPO 線最新一則是否對得上，Anthropic 公開版 S-1 出現時把「S-1 打開先看五個地方」改成對照實際文件的五句。

### `## 回顧結算`（累積，永久保留）

你每寫一則判讀就加一列 ⏳（欄值見 `.claude/reporter-rules/market/daily.md`「每日動作」第 2 步 c）；「兩週後」與「對錯」兩欄由主編於 `/wiki-lint` 5h 回填，**你不填**。已結算列永久保留（表是判準的紀錄，不是待辦清單）；表長超過 20 列時，最舊的時段依 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」處理。

### `## 追蹤中的里程碑`

每則判讀的「下一個催化劑」依 `.claude/reporter-rules/page-templates.md`「懸置標記語法」登記一筆，探針寫得出可在 `news/*.md` grep 到的字串；日報出現後續時只能加 `訊 YYYY-MM-DD`，結案屬主編。

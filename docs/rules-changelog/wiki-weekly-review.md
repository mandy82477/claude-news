# `.claude/skills/wiki-weekly-review/` 沿革（教訓存檔）

本檔是週度延伸回顧流程的歷史敘事，不是待執行規則；SKILL.md 條文處的「沿革檔 YYYY-MM-DD」皆指本檔對應段。

## 2026-09-13

`/wiki-weekly-review` 從舊 command 檔 .claude/commands/wiki-weekly-review.md 轉成 skill（`.claude/skills/wiki-weekly-review/`）。步驟語意與判準逐字不動，只換家：六記者派工 prompt 全文、月度聚焦校準 agent 規格與輸出表、彙整確認清單格式、log 條目模板移入同目錄 `dispatch.md`；月度校準判斷方式的教訓敘事移入本檔。`.claude/commands/weekly.md` 與當時的週報規格檔（今 `.claude/skills/weekly-report/SKILL.md`）的路徑引用、`.claude/review-registry.json` 的一組 sync_pair 同步改指新家；bare_references 的舊檔 line_allowlist 條目失效刪除（該檔本來就沒有裸露的根目錄規則檔引用）。

## 2026-07-16

**月度聚焦校準為何改判「產出物」而非「執行記錄」：** 舊判斷方式查「`wiki/log.md` 本月尚無週度延伸回顧記錄」，於是規則誕生前就存在的回顧記錄佔用了當月名額，導致連續三週誤跳過、校準從未實際執行。改為查 `wiki/metrics.md`「聚焦命中率」欄本月有無數值——量測機制的開關要綁在它自己的產出物上，綁在旁證上等於沒有開關。

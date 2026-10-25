# .claude/reporter-rules/safety-policy/ 沿革（教訓存檔）

本檔是安全政策記者兩份規則檔（`daily.md`／`pages.md`）的歷史敘事，不是待執行規則。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

（2026-09-13 由 `wiki-ingest-safety-policy.md` 條文旁的敘事搬入；條文一字未改。）

**2026-09-06**（兩頁同批改版）：`ai-agent-safety` 的舊條文指名 `## 事件記錄` 這一節，但該頁從來沒有這一節——條文因此改寫為「事件 prepend 進 `## 技術彙整`」並明寫本頁沒有那一節。同日另修 `anthropic-government-policy` 的一處：archive 頁反過來指著主頁 `## 攻防紀錄` 的條目，蒸餾時會斷鏈，因此加上「蒸餾前先確認 archive 沒有反指」這一句。

## 2026-10-04（攻擊表「最後動態」定義）

10-03 lint：「現在還擋不住的攻擊」表的「套件供應鏈」列沒有日期，5i 的 90 天退場判準算不出。表本身不設日期欄，補定義：最後動態＝該列在本頁事件記錄中日期最新那一則；列內看不出日期者，在表下 `%% … %%` 維運備忘逐列記下最後動態與對應事件。

## 2026-10-25（評測越界事件升格為子頁 topics/ai-eval-boundary-incidents）

W43 週度延伸回顧，安全政策記者提案、使用者「前面的你就全做吧」確認：UK AISI／Mythos 5／Anthropic 自揭評測事故整線從 `ai-agent-safety`（1,936 行、散在七處）搬到子頁 `topics/ai-eval-boundary-incidents`。理由：10-23 官方量化（43 次中 9 次越界）後同線三則跟進，且 AISI 122／10／19 與 Anthropic 43／9 兩套數字口徑需要一個固定的家。`daily.md` 負責頁面表加子頁列與每日動作一行；`pages.md` ai-agent-safety 節加「子頁路由」。

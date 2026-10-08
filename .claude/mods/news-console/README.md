# news-console（本機 mod）

只在 CLAUDE_NEWS 樹上作用（session 根有 `scripts/ingest_gate.py` 與 `wiki/log.md`）；全域載入時其他專案完全不受影響。雲端 session 不載入 mod，所以這裡的每一項都只是本機輔助——雲端也要生效的禁令一律在 `.claude/hooks/`。

## 三塊

| 塊 | 做什麼 | 在哪裡看得到 |
|---|---|---|
| 落後 origin | 開場後 1.5 秒起每 10 分鐘背景 `git fetch`；會動到 HEAD／origin 的 git 指令跑完、以及送出 prompt 附警告前，另用本機 refs 重算（不連網），合併推送後警告立刻消失；落後時 prompt 上方提示列顯示筆數與「拉取（ff-only）」按鈕（按了才拉，不自動）、送出 prompt 時附一行只有 Claude 讀得到的警告；同列報雲端班次真失敗（只讀 `origin/master` 的 `task_scheduler.log` 與 `cloud-daily-*` 分支，12Z／17Z 等料中止與冪等中止不出聲）；平常只在提示行尾端加「已同步　日報 MM-DD」 | 提示列、提示行 |
| wiki 新鮮度 | Read `wiki/**/*.md` 後在 transcript 記一行 `last_news_update` 與距今天數（不下「過期」判定，門檻待使用者裁決） | transcript 暗色行（Claude 不讀） |
| 工作樹歸屬 | Edit／Write 成功與 Bash 前後新增的髒檔記進 `$.store`，一檔一把 `p:<sessionId>:<path>`（只 set 不先 get，同 session 並行子代理不互蓋；舊格式 `touched:<sessionId>` 陣列照讀）；`git add`／`commit`（點名路徑的 commit 不算整個暫存區；`commit -a` 算全部髒檔）會納入別的活著（90 分鐘內有心跳）session 動過、本 session 沒動過的檔就 deny，只給數量、不列別人檔名 | deny 訊息、狀態行 |

## 守則

- 對工具呼叫只 `next(e)` 或 `{ deny }`：回 `{ result }` 會跳過 `.claude/settings.json` 的 PreToolUse hook（官方 mods events「Where settings hooks run in the order」）
- 不改寫工具輸入、不用 `tool.check` 放寬、不用 `$.model.*`、不起 agent、不自動 pull、按鈕不用數字熱鍵（提示列的數字熱鍵會被空 prompt 裡單打的數字觸發）
- 失敗一律放行（fail-open）：git 跑不起來就當沒資料

## 載入與驗證

需 Claude Code 2.1.287 以上。本機載入：`~/.claude/settings.json` 的 `env.CLAUDE_CODE_PLUGIN_DIRS` 指到本目錄的絕對路徑。驗證：`python scripts/run_tests.py` 的 `check_mods.py` 跑 `claude plugin validate --strict` 與 `claude plugin test`（版本不足或雲端時跳過並印 WARN）。

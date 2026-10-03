# 規則精簡對照表（hook 上線後，2026-10-03 草案，待使用者裁決）

**還沒動任何規則檔。** 本表只列「哪條禁令現在由誰硬擋、在哪裡重複、建議縮成什麼」。

## 先決條件：沒有一條已達「可刪」

刪字的門檻是**本機與雲端都確認擋得住**。目前狀態：

| 證據 | 狀態 |
|---|---|
| 本機 hook 真的擋 | ✅ 每支都在本 session 實測過（主 session 與子 agent 兩種身分） |
| hook 指令在雲端找得到 python | ⏳ `src/tests/test_settings_hooks.py` 會在下一班雲端 `run_tests` 原樣執行 settings 指令；要先 push |
| 雲端 session 真的會執行專案 settings hook | ⏳ 官方文件沒寫。使用者 2026-10-03 選被動探針：`.claude/hooks/probe_cloud_hooks.py` 在雲端每 session 第一個 Bash 前寫 `[cloud hooks-probe ACTIVE …]` 進 `task_scheduler.log`。origin 上出現這行＝證實；某班 STARTED 前沒有這行＝該班 hook 沒跑 |

所以下表「建議」欄全部是**候選**，等第三列變 ✅ 才執行。驗證做法見文末。

## 對照表

| 禁令 | 現在誰擋 | 擋的對象 | 規則檔裡出現在 | 建議 |
|---|---|---|---|---|
| `claude -p` | `block_claude_print.py`（指令）＋ `check_no_llm_calls.py`（程式碼） | 所有 session | `CLAUDE.md:34`（只此一處） | 已是單一家。可縮成一行「禁止 `claude -p` 與任何 LLM API 呼叫（hook＋閘強制）」，理由搬進 hook 訊息（已在） |
| `git add -A`／全加 | `block_git_add_all.py` | 所有 session | `.claude/rules/dev-done.md:17`、`.claude/skills/news-gather/SKILL.md:81` | 刪 news-gather:81；dev-done:17 留半句「commit 一律指名路徑（hook 強制）」 |
| stash／reset／clean／restore／checkout --／pull／rebase | `block_destructive_git.py` | 子 agent：全部寫法；主 session：整棵樹的寫法 | `.claude/reporter-rules/shared.md:13`（含 >5 行理由）、`.claude/skills/page-audit-review/SKILL.md:34`、`.claude/skills/web-publish/SKILL.md:125`（autostash） | shared.md:13 縮成一行＋保留「遇到 git 異常寫 ⚠️ 工作區異常交主編」（這是替代行為，hook 給不了）；page-audit:34 的 git 清單刪掉，留「不可再委派」以外的部分；web-publish:125 的 autostash 禁令刪，留「髒樹改走 fetch＋比對＋merge」的流程 |
| `checkout -B master`／`push HEAD:master`／force push | `block_destructive_git.py` | 所有 session | `.claude/skills/web-publish/SKILL.md:135`、`docs/cloud-runbooks/_shared.md:46` | 兩處都刪「不要做 X」與事故敘事，只留「不在 master 時推 `cloud-daily-<日期>-unmerged`」；_shared.md:46 改成指向 web-publish（runbook 只承載環境差異） |
| 寫入 `news/` | `guard_roles.py` H5 | **只有子 agent**（主 session 寫日報是合法的） | 16 處：`CLAUDE.md:17,25`、`wiki/CLAUDE.md:46`、`shared.md:11`、`wiki-ingest/SKILL.md:152`、weekly-report／wiki-lint 各 skill 的邊界節 | 只有 **shared.md:11**（記者）可縮；其餘 15 處對象是主 session，hook 不擋主 session，**不可刪** |
| 改閘腳本／基線／`--rebuild` | `guard_roles.py` H6 | 子 agent＋雲端 session | `web-publish/SKILL.md:69-72`、`shared.md:231` | shared.md:231（記者）可縮成一行；**web-publish 的硬性禁止不可刪**——本機 Phase C 預設由主 session 跑修復迴圈，hook 刻意放行本機主 session |
| 記者再委派 | `guard_roles.py` H7 | 所有子 agent | 17 處：各派工 prompt 範本（dispatch.md ×6、classification.md、sweeps.md、news-pipeline dispatch ×2）、3 個角色檔、shared.md:12、page-audit:34、wiki-ingest:150、wiki-lint-reporters:93、wiki-lint-sweeps:42 | 角色檔與 shared.md:12 留一處；派工 prompt 範本裡的「你不可再呼叫 Agent tool」可刪（hook 訊息會說）。約 −14 行 |
| 記者用 web 工具 | `guard_roles.py` H7 | 記者身分的子 agent | 27 處 | 多數**不是禁令而是流程**（「記者無 web 工具 → 標 ⚠️ 需主編查證」），刪了記者不知道替代做法。建議只把 shared.md:129 當單一家，其他頁的「記者無 web 工具，所以…」保留「所以」後半句。實際可刪很少 |
| 派記者須明寫 model 與 foreground | `guard_roles.py` H8 | 主 session 派記者／pipeline agent | 13 檔 22 行 | hook 只要求「有寫 model」、沒要求「是 sonnet」。若要讓規則縮成一處，先把 hook 改成要求 `sonnet`（需裁決）；否則維持 |
| 內容閘紅 commit wiki | `gate_wiki_commit.py` H9 | master 上所有 session | `web-publish/SKILL.md` Step 3（今天剛寫）、`page-audit-review/SKILL.md:48` | 已是新寫法，無重複可刪 |
| log／帳本只能 append | `check_append_only.py` | 只擋「寫在檔頭」 | 17 處 | **不可刪**：閘只看檔頭插入，「既有條目一字不可改」仍只有文字 |

## 估計

實際能刪的集中在記者規則（shared.md 三條）、派工 prompt 範本（約 14 行）、web-publish／_shared 的 git 禁令（約 6 行）。大宗重複（news/ 唯讀 16 處、web 工具 27 處、append-only 17 處）因為 hook 刻意不擋主 session、或條文本身帶替代流程，**不能**因 hook 而刪。

## 動手時的注意

- 先跑 `grep` 確認 `.claude/review-registry.json` 的 sync_pairs（目前 127 組）有沒有綁這些字串，刪字會讓 `check_rules.py` 紅
- 照 `.claude/rules/claude-md-edit.md`：反向查詢引用方、改完跑 `/review-commands`、沿革記 `docs/rules-changelog/`

## 雲端驗證做法（擇一，需使用者同意）

1. **被動探針**：讓 `guard_roles.py` 在 `CLAUDE_CODE_REMOTE=true` 時第一次被呼叫就 append 一行 `[cloud hooks active <時間>]` 到 `src/logs/task_scheduler.log`；雲端班收尾本來就會 commit 這個檔，下一班過後看 origin 有沒有這行即可。不花額外雲端執行，但會在 log 多一行
2. **主動探針**：建一次性 remote trigger，在雲端跑 `false && git stash` 與 `false && claude -p x`，把回應寫進 `docs/cloud-runbooks/probe-hooks-<日期>.md` 後 push（比照 2026-09-13 的 Workflow 探針）。要花一次雲端執行

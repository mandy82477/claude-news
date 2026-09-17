# 根目錄 `./CLAUDE.md` 沿革（教訓存檔）

本檔是根目錄 `./CLAUDE.md` 的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

**2026-09-14**（dev-done 的 hook 兜底補上 `web_reader/assets/`）：`dev-done.md` 的 `paths:` 從 2026-09-13 建檔起就含 `web_reader/assets/**`，正文也寫「第 1、2 條有 hook 兜底」，但 `check_tests_on_stop.py` 的 `WATCH_PREFIXES` 只有 `src/`、`scripts/`、`.claude/hooks/`——規則對自己宣告的一半範圍是失效的，整整一天沒人發現。代價當天就付了：一輪純 `web_reader/` 的排版改版未 commit 也沒測試綠，兩支 hook 都不擋，結果把導覽列改壞（品牌名與六個分頁互相重疊）推上線才被使用者看到。修法是把 `web_reader/assets/` 加進 `WATCH_PREFIXES`，只收手寫的 CSS 與 JS；`data/`、`index.html`、`sw.js` 刻意不收——那些是 `build_web.py` 每次都重寫的產物，收進來會讓每次建置都強迫重跑整套測試，那是別的 session 的收工成本。同日另立 `scripts/check_css_overrides.py`：同一輪裡「同特異度靠源順序決勝的靜默覆寫」命中六次，評審判定靠人更小心已證明無效，故機械化（D4）。反向查詢時發現 `docs/architecture-current.html` 與 `architecture-evolution.html` 兩處的監看範圍敘述已與實際不符，一併同步。

**2026-09-13**（第二輪瘦身：開發紀律出根檔、hook 接手、本站目標進根檔）：使用者裁定「只在開發模式才需要的規則不該對每個請求課稅，必須執行的步驟放 hook」。刪掉五節——「完工定義」「commit 範圍」「Skills」「Wiki 規則入口」「修改 rules 或 commands」。逐節盤點去處：commit 範圍與改規則後跑檢查早已有 `block_git_add_all.py` 與 `check_rules_on_stop.py` 兩支 hook 強制，刪文字零損失；Skills 章節由各 skill 的 description 自動載入取代；Wiki 規則入口由 `wiki/CLAUDE.md` 碰檔即載取代。完工定義三條則搬進新開的 `.claude/rules/dev-done.md`，`paths:` 綁 `src/`、`scripts/`、`.claude/`、`web_reader/assets/`、`.github/workflows/`，只在開發時載入；第 1 條「測試綠」同日機械化為 `check_tests_on_stop.py`（程式檔有未 commit 改動且 `run_tests.py` 未綠就擋收工，全綠記號 `.claude/.last-tests-ok` 讓沒改動時不重跑）。不放進 `claude-md-edit.md` 的理由：那支的 `paths:` 只綁規則檔，改 script 時不會載入，射程對不上。三處指向舊章節的引用（wiki-lint、wiki-query、workaround-register）與兩支 script 的提示訊息改指新家；`check_rules.py` 當時全綠沒抓到，因它只查裸露路徑不查章節存在。同日根檔新增「本站目標」一節：從網站「關於」頁統整讀者、三主軸與時效取捨，`README.md` 改寫為該頁的 Markdown 版，三者同源。附帶修掉 `check_skill_refs.py` 在 cp950 主控台印 `≤` 會炸、讓 `run_tests.py` 在本機整體紅的問題。

**2026-09-12**（記者規則搬家＋根檔瘦身）：`.claude/rules/` 的語意是「主 session 自動載入」，但 19 份規則檔裡有 17 份只被記者 subagent 或 lint 主編**明文 Read**——它們原本無 `paths:`，等於每個 session 無條件載入 244 KB（根檔的 21 倍），而真正需要它們的角色本來就會自己讀。故 17 份移入 `.claude/reporter-rules/`（不帶 `paths:`，那裡沒有自動載入機制），`.claude/rules/` 只留主 session 用得到、由 `paths:` 觸發的三份。

同批把根檔從 155 行壓到 64 行：根目錄 `./CLAUDE.md` 的每一行都對**每個**請求課稅，逐行問「刪掉會讓 Claude 犯錯嗎」。蒐集範圍與目標讀者移入 `.claude/rules/collection-scope.md`（`paths:` 綁爬蟲目錄，由 `/wiki-lint`、`/wiki-weekly-review` 與社群 lint 規則明文 Read）；開放迴路掃描移入 `.claude/commands/weekly.md` 步驟 0（它本來就是每週指令的事，registry 的同步配對一併改指該檔）；wiki 連結語法與絕對限制刪除（`wiki/CLAUDE.md` 碰 wiki 檔就載，原文逐字重複）；「commit 範圍」壓成兩行並改由 `.claude/hooks/block_git_add_all.py` 這支 PreToolUse hook 強制——必須每次都發生的規則不該靠 agent 記得（2026-08-29 A 那次違規者不是不知道規則，是沒想到自己正在違反它）。

**2026-08-29 A**（commit 範圍：只 add 指名路徑）：本條原本只寫在 .claude/commands/news-pipeline-steps.md（2026-09-13 已拆成四個 pipeline skill）「絕不要在補跑流程裡用 `git add -A`」，射程只到補跑流程；臨時修復工作不在射程內，於是當天出事：一個訊息為「fix: 目標日期取自耐久的 gathered_archive」的 commit，掃走了同時間另一份工作中的 `wiki/entities/pricing.md`（+43）、`wiki/topics/model-comparison.md`（+30）、`code-quality-decline.md`、`log.md`（+39）。兩層傷害：(a) commit 了半成品——那批 wiki 改動尚未修完錨點、規則也還沒移到 lint 檔；(b) 殺掉可追溯性——本專案的品質系統建立在「為什麼加這條」查得到（`log.md` Query 條目、`[加入: YYYY-MM-DD]` 標記、條文裡的「教訓來自 X 月 Y 日」），而這些考古全靠 `git log` / `git blame`。訊息錯置的 commit 讓那條路斷掉，且事後補不回來。

**2026-08-29 B**（開放迴路掃描為何印三個數字、失敗為何不得當 0）：`scripts/open_loops.py` 初版只印一個總數 229，其中 195 由舊語法盲區＋逾期懸置主導——其餘四類全部歸零，總數也只掉到 34，那不是彙整，是「盲區筆數＋雜訊」。同時 feature-radar 那一類初版用全文 `count("⏳")`，把跨層重複與圖例都算進去，實測 23 對真實 13（高報 77%），且未逾 90 天的觀望根本不算積壓。因此輸出拆成「需收尾／已跳票／存量遷移」三個數字，各答不同問題。另外懸置類掃描壞掉會拋 `PendingScanUnavailable`，此時標題印「數量未知」、總計標下界 `≥`、exit code 非 0——一支專門防低報的腳本，自己靜默回 0 就是得了它要治的病。

已知取捨：帶 `paths:` 的規則在 context compaction 後會消失，要等再次讀到匹配檔案才回來（本庫 `wiki/topics/coding-workflow-guide.md`「東西該放哪一層」表有記）。三份 `.claude/rules/` 規則檔都受影響，實務上再讀一次對應檔即恢復，不是 bug。

## 2026-09-15：collection-scope.md 蒐集範圍加「出貨前訊號」

Claude Code 程式本體裡先出現、未公告的 `CLAUDE_CODE_*` 旗標（每版至多 1 則）。理由與探針數據見 `docs/rules-changelog/wiki-ingest-features.md` 同日條目。判準句不變：只收會幫工程師更了解生態的；旗標名字本身不是承諾，故只進實驗功能頁第一階。

## 2026-09-17：查詢第 2 路的同義詞表改為查詢改寫

動到根目錄 `./CLAUDE.md` Query 條、`wiki/CLAUDE.md`「搜尋策略」第 2 路、`.claude/skills/wiki-query/`。2026-09-14 上線的同義詞表（data 目錄下的 search_aliases.json，8 組 70 詞，人工登記）三天後由使用者裁定拿掉：「我不想多維護 table」。判斷依據是全庫只有 `scripts/wiki_search.py` 讀它，而跑這支腳本的永遠是 Claude session——語意它本來就懂，靜態詞表只是多一份沒人看守、會靜默過期的資料。改法：session 先把問句改寫成二到四種說法，連同原句當參數傳入；腳本每種說法各跑一次 BM25，分數除以該說法最高分後跨說法加總。

改前改後拿真實 wiki 對照三題（多 agent 視覺化、省 token 費用、長跑 agent 忘事）。第一版融合取「各說法最好的那一次」，結果 `topics/community-pattern-trends` 與 `topics/enterprise-cost-management` 兩個正解掉出前八——只在一種說法裡第一名的頁把名額佔滿；改成加總後回來。同一輪對照還抓到一個被詞表掩蓋的舊問題：虛字表含「用」，查詢端剔除任何含虛字的 bigram，於是「費用」「用量」整個消失，「怎麼省 token 費用」只剩 `token` 一個詞；舊版靠詞表對原句做子字串比對繞過了這件事。修法是「用」只在落單時當虛字。設計取捨與剩餘缺口見 `docs/wiki-ingest-query-design.md` 第 5 節。

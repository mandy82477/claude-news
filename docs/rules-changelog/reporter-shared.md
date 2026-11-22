# .claude/reporter-rules/shared.md 沿革（教訓存檔）

本檔是 `.claude/reporter-rules/shared.md` 的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

（2026-09-13 由 原 `wiki-reporter-shared.md` 條文旁的敘事搬入；條文本身未改一字。）

**2026-11-14**（月度蒸餾五條立法，雲端 lint 判採納、本機落地）：近 30 天記者回報的重複失誤——①商業記者來源歸因 URL 欄寫「Google News 新聞連結」等佔位字（≥4 次）→ shared.md「來源歸因回報」補禁佔位字、只有轉址時填原文；②六類記者回報欄位不照契約（≥6 次）→ 只在 shared.md「回報格式」加一句逐欄自檢（單一來源，各角色檔本來就指向它，不逐檔抄）；③自述通過但未實測（W42 缺轉知處置欄、W44 3e 未驗與 3h 未跑）→ daily-contracts.md 呈現品質節加「自述通過要有實測」；④3g 改寫舊語法後儲存格超限（`ai-agent-safety-cyber:222` 209 字元、`pricing-incidents:178` 226 字元，均主編代修）→ daily-contracts.md「表格變體」加該頁必跑 `check_cell_limits.py --page`；⑤流程詞外洩讀者正文（11-13 社群、11-11 模型，主編自己也犯一次）→ shared.md「派工過程不上頁」加流程理由一律進 `%% … %%`。同日 wiki-lint-sweeps 邊界節與 wiki-ingest 步驟 3 的矛盾（6a）見 `docs/rules-changelog/wiki-lint.md` 同日段。

**2026-10-11**（記者規則拆「每日必讀」與「碰到才讀」）：近 14 天 120 次記者派工量測：`page-templates.md`（20 KB）被讀 130 次、`shared.md`（21 KB）121 次。角色檔明寫 page-templates「建頁時另讀」，記者卻每次都讀，因為其他規則指向它的「懸置標記語法」「Wiki 頁面呈現品質標準」兩節；shared.md 裡「大型頁面讀取策略」「事實更正必回掃」「待查證命中處置」「轉知接手處置」則是碰到才需要。讀進來的規則之後每一回合都被重算。
處置：那兩節原文搬到 `.claude/reporter-rules/daily-contracts.md`、那四節原文搬到 `.claude/reporter-rules/shared-when.md`，原處只留指路，條文一字未改；角色檔「開始前必讀」改為 shared.md ＋ daily-contracts.md，page-templates 回到建頁時才讀。每日固定讀量由約 41 KB 降到約 27 KB（shared.md 16 KB ＋ daily-contracts.md 11 KB）。

**2026-10-04**（派工不再指定 sonnet，使用者裁決「把必須是 sonnet 都刪掉」）：`guard_roles.py` H8 一直只要求派記者與 pipeline agent 時「有寫 model」，規則檔卻在 15 個 skill／runbook 寫死 `model: "sonnet"` 與「不需旗艦模型」的理由。全部改成「明寫 `model`」，保留「未指定會繼承主 session 模型、六記者並行足以打穿訂閱配額」這句理由；registry 的 sync_pair 與 hook 訊息同步。

**2026-10-04**（hook 已硬擋的禁令從規則檔縮掉，使用者裁決「都修掉」）：改動工作區的 git 指令、改基線與 `--rebuild`、再委派都已由 `.claude/hooks/block_destructive_git.py`、`guard_roles.py` 在本機與雲端擋下（雲端執行證據：10-03 17Z、22Z 與 10-04 01:35Z 的探針紀錄）。本檔兩條縮成一行並保留替代行為（「⚠️ 工作區異常」交主編）；派工範本裡的「你不可再呼叫 Agent tool 委派任何工作。」七處刪除，角色檔與本檔各留一處。逐條對照見 `docs/hook-rule-slimming-2026-10-03.md`。

**2026-09-05**（禁止改動工作區全域狀態的 git 指令）：功能記者為了處理自己檔案的狀態，`git stash` 後只 `checkout stash@{0} -- entities/claude-code.md` 取回自己那份，再 `git stash drop`——**模型記者的 `wiki/entities/fable-5.md` 與社群記者的兩頁技術彙整就此消失**，三份已完成的工作全部重做。當事記者全程沒有惡意也沒有偷懶，它甚至在回報裡誠實寫下「未觸碰其他記者的工作」——它真心那樣以為，因為 `git stash` 看起來只是在整理自己的桌面。**這正是為什麼本條要寫成明文禁令而不是「請小心」**：並行下的工作區共用性不是記者從自己的視角看得見的東西。

**2026-08-15**（規則檔優先於派工訊息）：`wiki-ingest-community.md`（今 `.claude/reporter-rules/community/`）當天改版為「日更只標 `**主線：**` tag、主線縫合改週更」，主編的派工卻仍要求「今日順手改寫主線頁敘事」。社群記者查了規則、擋下來並回報，是正確處置——本條把那次的正確處置寫成所有記者的預設行為，不再依賴個別記者夠不夠警覺。

**2026-09-03**（書寫風格：精煉是紀律）立法依據（冗語源頭審計）：同一事實從日報（平均 79–94 字）到 wiki 落地平均放大 4 倍，放大全發生在記者改寫層；可砍量與「關係從句（全庫 381 次）＋意涵尾巴（126 次）＋缺項自白（122 次）」高度相關，去掉三種尾巴不動任何數字與歸因。對照組：analyzer 的「每點 1–2 句」上限有效——有上限就守得住。

**2026-08**（事實更正必回掃）：一個月內同一種病出現三次——

| 日期 | 事實 | 沒回掃的後果 |
|---|---|---|
| 08-08 | Opus 5 定價由「推算值」升為官方確認 | `model-comparison`、`overview` 掛著「非官方逐字確認」12 天 |
| 08-10 | Sonnet 5 $2/$10 永久化 | 5 處仍寫「促銷 8/31 到期」，其中 `overview` 還說「促銷到期前為最佳性價比視窗」，直到 08-28 才被抓到——距那個不存在的到期日剩 3 天 |
| 08-20 | 懸置標記查實結案 | 已立法（`/wiki-lint` 5c 第 5 步的探針回掃）|

第三次已經有機制，但它**只綁在懸置標記上**（靠 metadata 的探針欄），接不到前兩種——那兩次都是純散文更正、不帶標記。本條是同一個動作的通用版：**不管更正有沒有標記，回掃都是更正的一部分。**

**2026-09-04**（為什麼把入邊擺在第一步）：原本第一步是「想出關鍵字」——那是**靠記憶列舉**，而 2026-08 的三次漏回掃全部敗在同一件事：關鍵字沒想到（促銷到期日寫成「8/31」還是「8 月底」、「推算值」還是「非官方逐字確認」，措辭一變就漏）。入邊清單不靠想像：wikilink 是引用方自己留下的指標，圖上查得到就是查得到，數量固定、可逐筆核銷。

**2026-09-06**（機械自查要附輸出行）：兩位記者同輪都宣稱自查通過，主編全庫掃描抓到 3 筆新增超限；工具沒問題，缺的是證據——這正是本庫「查過確認沒有」與「沒人查」必須長得不一樣的原則，只是先前沒套用到自己身上。

**2026-09-25**（規則瘦身第一輪：pages.md 只讀要動的節、slug 表搬到主編端）：量測九個 agent 每天開工合讀 170.7K 字元規則，其中 pages.md 佔各記者「自己的」讀量八成（features 17.4K、community 16.6K），而記者每天實際只動 1–3 頁；改為只讀該頁的節，零內容損失。shared.md 的 slug 對照表 1.3K 字元被八位記者每天各讀一次，實際是 `data/source_registry.json` 的手抄副本；改由主編在步驟 2 節錄的來源行標 slug，記者照抄。registry 條目「多來源條目的來源欄」仍以 shared.md 保留的 ＋ 規則為錨。

同日複核補記：批評者 agent 指出功能記者不直接寫 feature-radar，依「只讀要動的頁」會跳過 pages.md 的 feature-radar 節，而「新條目必補全覽表一列」「當月對帳」「熱度只住全覽表」三條就住在那裡（08-09 事故的防線）；角色檔補一句該節每日必讀。

**2026-09-25**（字元上限基線只准變緊；記者不得 rebuild）：`data/cell-limit-baseline.json` 的 `_note` 寫「棘輪只能往下轉」卻無強制。舊指紋是整格內容雜湊，存量列只改一個數字（留言數）就被判「新增」，FAIL 訊息還教人跑 `--rebuild` 轉綠；六記者並行時一人 rebuild 會把別人同時寫的新超限洗成存量。事故：`98a3b59e`（09-22）基線 928→924 但新增 2 個指紋；`8cca5fb0`（09-24）924→915 但新增 3 個（claude-code 第 224、354、362 行，改前改後字數相同，是正當的存量改寫）——兩次總數都在降，「總數不得增加」的測法一次都抓不到，必須比集合差。另查到 `96217a69`（09-09）把 `data/pending-legacy-baseline.json` 的 `max_legacy` 41→42，違反棘輪，當時無人看過。處置（使用者拍板選 B）：存量判定改為「穩定錨點＋長度不增」（錨點規則與例子住 `scripts/check_cell_limits.py` 檔頭）；`--rebuild` 只准移除／收緊，要新增須 `--allow-grow --reason` 並寫 `data/baseline-changes.jsonl`；`src/tests/test_baseline_ratchet.py` 對 HEAD 版比集合差看守三份基線；FAIL 訊息刪掉叫人 rebuild 的那句；本檔「機械自查」節加記者禁令，web-publish 修復迴圈禁止清單加基線與白名單檔。錨點失效的已知形狀：表格首格本身就是超限格且前 24 字被改寫（feature-radar、community-tech-discussions 的標題列）；同日期多列的日期鍵表格（claude-code 更新日誌）以多重集合比對，同日一列換成不更長的新列不會被抓；條列開頭 24 字內含會變的數字（全庫 3 筆，如 pricing「GitHub Issue #17432 留言數更…」）；狀態前綴超過 12 字或未以「｜」收尾；頁面改名。

**2026-09-27**（機械自查三支改四支，加 `check_pending_markers.py --page`）：09-26 ingest 內容閘抓到兩處記者問題（新頁與 index 列用舊語法「待核實」、market 探針詞 <3 字元），皆屬該腳本管轄卻不在原三支自查裡，紅落到主編身上才被發現。`--page` 語意同 `check_cell_limits.py --page`，只過濾檔案清單；全庫層級的存量棘輪與標記數看守閘是純量統計、非逐頁 keyed，頁面模式下印說明略過，非漏跑。

**2026-09-27**（prompt 審計）：以 `/claude-api prompt-audit` 對記者角色檔與規則檔做化石清理——移除正文中的沿革指路括號與日期戳、遷移相對措辭（「原節名…改名」「已於…廢止，取而代之」「lobste.rs 已移出」）、一次事故釘成的長段（模型頁日期殘留、devpractice 吃 diff 的裁決敘事）、過期的頁面行數；並修正人物／模型角色檔與懸置標記閘打架的「待核實」字樣（09-26 內容閘因此紅過一次）。書寫上限、git 全域指令禁令、回報契約刻意不動。

## 2026-10-04（page-templates：頁首第一句、蒐集邊界移到欄位最後）

10-03 冷讀者對抗輪抽 simon-willison／fable-5／yann-lecun 三頁，共通問題是前 160 字全被欄位列與收錄政策吃掉，真正的「他是誰／這是什麼」排在很後面。人物頁當天已由人物頁改版補上 `**身分：**` 等四欄；本次補兩條：非人物頁 H1 下放一句 ≤60 字的「這是什麼」，`**蒐集邊界：**` 從「領域之後」改到欄位區最後一行（10 頁一次搬完，看守只查存在、不查位置）。既有頁面的第一句不批次回補，記者下次改到該頁時補上。

**2026-11-22**（feature-radar 禁碰條款補 lint 例外）：11-21 lint 主編明文派功能記者裁剪 radar 升級變更表，與 `shared.md`「記者不可碰 `wiki/feature-radar.md`」字面衝突，只能先違規再追認。補一條例外：主編在 `/wiki-lint` 派工中明文指派裁剪 radar 某一張表時視為授權，動作只限該表、其 `%%` 備忘與表下說明句。

**2026-11-22**（11-14 對抗輪 C 修訂落地）：`docs/adversarial/2026-11-14-prompt-reviewer.md` 的 20 項（#19 三處分開計，共 22 處）逐項對現況核過再動。**落地 20 處、已解 0、不採納／延後 2 處。**

- 落地：#1 `.claude/skills/weekly-report/SKILL.md`、`.claude/skills/wiki-weekly-review/SKILL.md` 單獨執行時改走 `gate_web_build.py`，兩檔補進 `.claude/review-registry.json` 兩組 gate 看守；#2 五份 `daily.md` 與 `.claude/reporter-rules/README.md` 改九欄，`.claude/reporter-rules/shared.md` 骨架下加「欄數以骨架為準」；#3 `.claude/reporter-rules/page-lifecycle.md`「對稱規則：併回」排除封存頁／轉址殼，偵測端 `check_page_thickness.py --thin` 未上線前判準不生效；#4 同檔母頁 300 行看守範圍寫實；#5 同檔「頁面過長」門檻改 600 行並接 5o；#6 #7 `.claude/commands/pipeline-change-check.md` 指標組補 `topicRadar`／`sedimentedToday`／`bulletin`，`sourceStatus` 註記更新，文章數總量不推給 6e；#8 `.claude/rules/dev-done.md` 加第 4 條（改到產出先跑 baseline）；#9 `.claude/agents/wiki-reporter-features.md` 刪過期條目格式副本，改指 `.claude/reporter-rules/features/pages.md`；#10 三支腳本（`scripts/check_callout_coverage.py`、`scripts/check_reader_digest.py`、`scripts/check_reader_language.py`）指路改 `.claude/reporter-rules/daily-contracts.md`，registry 加規格端／消費端兩條（reviewer 原案列的 `scripts/build_reader_digest.py` 不含該節名，不列）；#11 #20 `.claude/reporter-rules/market/daily.md` 契約表補免責 callout 與線名兩列（消費端寫實際測試名 `TestRealPage::test_disclaimer_callout_is_first_callout`，原案寫的 `TestDisclaimer` 不存在）、佔位字護欄；#12 `.claude/reporter-rules/community/pages.md` 刪行號、補路由表列數硬契約（`assert` 現值已是 8 不是 7，條文寫「N＝本表現有列數」不寫死）；#13 #14 `.claude/reporter-rules/README.md` 頁數改查法、共用檔六份補 `batch-edit.md`——試點已於今日在 `docs/workaround-register.md` 結案，`.claude/reporter-rules/batch-edit.md` 首句與 README 措辭照結案現況改「選用」而非原案的「試點中」；#15 `.claude/reporter-rules/features/pages.md` 補旗標前綴硬契約，示例改完整名 `CLAUDE_CODE_DISABLE_TURN_HANDOFF`（原案把無前綴名導去「代號旗標」節，但那節收的是兩字代號，改為只說不進追蹤表）；#16 空括號殘骸手清（含 reviewer 列的四處以外又掃到的六處沿革檔行），`scripts/strip_rule_markers.py` 的 `_KIND` 補「搬入」、刪標記後收掉 `（）`／`，）`，附回歸測試 `src/tests/test_strip_rule_markers.py`（改前同輸入留 `**閘**（）：` 與 `[搬入: …]`，改後兩者皆清），重跑腳本清掉 `.claude/reporter-rules/shared.md` 與 `wiki/CLAUDE.md` 各一處搬入標記；#17 `.claude/reporter-rules/market/pages.md`、`.claude/reporter-rules/market/weekly.md` 回顧結算不走時段蒸餾；#19 `page-lifecycle.md` 警示節標題、`.claude/reporter-rules/features/daily.md` 升格列、`.claude/agents/wiki-reporter-commercial.md` 數字句。
- #19 升格列改寫而非照抄：原案「GA 升 ✅、有範圍升 ⚡」把狀態軸（正式發布）與試用價值軸（看使用案例）混成一件事，落地版改成「GA 當輪改狀態，試用價值照使用案例另判」。
- 不採納／延後：#18（5j「四表」改「五表」）——該字串被 registry 兩條 sync_pair 逐字錨定，且 `.claude/skills/wiki-lint-sweeps/references/sweeps.md` 與 `.claude/skills/wiki-lint/references/log-format.md` 都有別的 session 未 commit 的改動，混改會讓 commit 範圍說不清，留待那兩檔收乾淨後同批改字串與 registry；#16 的 `.claude/skills/web-publish/SKILL.md` 沿革行殘骸同理（該檔有別人的未 commit 改動），留一處未清。
- 報告末段「長度與注意力補充」（`.claude/reporter-rules/commercial/pages.md` 拆小標、五份讓位註記副本收斂）不在 20 項編號內，未動。

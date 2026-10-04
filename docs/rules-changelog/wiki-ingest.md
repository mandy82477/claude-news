# `.claude/skills/wiki-ingest/` 沿革（教訓存檔）

本檔是每日 wiki ingest 流程的歷史敘事，不是待執行規則；SKILL.md 條文處的教訓皆存於此，執行 ingest 時不必讀。

## 2026-09-13

`/wiki-ingest` 從舊 command 檔轉成 skill（`.claude/skills/wiki-ingest/`）。步驟語意、契約字串與判準逐字不動，只換家：類別↔角色檔對照表、六記者 prompt 模板、防偏誤說明、4b／4c prompt 首段移入同目錄 `dispatch.md`；共用檔案逐檔寫入規則、完成前強制核對清單、完成摘要表移入同目錄 `checklist.md`；下列兩則教訓敘事移入本檔。`$ARGUMENTS` 的日期改以 TARGET_DATE 稱呼（呼叫時傳入的參數仍是同一個值）。引用端（`.claude/skills/news-pipeline/SKILL.md`、`.claude/commands/wiki-backfill.md`、`.claude/reporter-rules/`、`.claude/skills/news-gather/`、`.claude/skills/news-digest/`、`docs/cloud-runbooks/daily.md`、`src/news_aggregator/main.py`）與 `.claude/review-registry.json` 同步改指新家。

## 2026-07-25（ingest 輸入不能只有日報）

抓料 73 則、日報收 38 則，其餘 35 則因為 ingest 的輸入只有日報，包含 61 留言與 47 留言的 GitHub Issue 在內，**沒有任何記者看過**。處置是步驟 1 強制執行 `scripts/list_digest_omissions.py`，把差集一起送進分類，原則寫成「不收可以，沒看過不行」。

## 2026-08-13（專頁定向條目不得因「跟 Claude 沒關係」而略過）

2026-08-05 Jeff Dean 等人離開 Google 創辦 Discovery Loop，因標題是 Google 視角而被 12 個來源全數漏掉 8 天。專頁定向抓來的條目標題天生不含 Claude／Anthropic——那正是它們被定向抓來的原因，因此收錄判準改用該專頁自己的觸發條件，不套用 Claude／Anthropic 關聯門檻。

## 2026-09-25（節錄來源行標 slug）

步驟 2 節錄格式的來源行加 `（slug：…）`，多來源各標一個；主編依 `data/source_registry.json` 填。目的：把原本住 `shared.md` 的 slug 對照表從八位記者的每日必讀移到主編一次查表，記者照抄。同輪一併把各記者角色檔的 pages.md 改為只讀要動的節，理由與量測見 `docs/rules-changelog/reporter-shared.md` 2026-09-25。

自我複核補記：搬表時發現原表帶兩個 registry 沒有的別名（「GitHub Search」→ github、「Blog」→ blog，registry 名為 Blogroll），單靠 registry 主編會標錯或標成未註冊 slug；已在 registry 對應條目加 `aliases` 欄，步驟 2 條文改為對 `name` 或 `aliases`。

## 2026-09-25（內容閘前移到 ingest；log 轉知必須對得到帳本；轉知驗負責人）

**起因。** 全套閘原本只在 Phase C web build 跑（`gate_web_build.py`），ingest 步驟 5 只跑 `check_classification_log.py`。9 月閘修 commit 有八筆（0e185357、7a57b0b3、5760a018、a02ed248、805d7262、e8d41c16、aba48824、8b87e9d0）；09-24 REPAIRED 四類（radar 儲存格超限、radar 詳細條目↔全覽表不對稱、index 舊語法懸置標記、pricing 內部用語）有三類出在主編自己寫的檔，卻由 Phase C 的修復迴圈事後補。修復迴圈也曾用加白名單轉綠（e8d41c16 往 `data/reader-language-allow.json` +6 行），綠燈看不出是修了內容還是收了例外。

同日另一條漏洞：09-24 log 模型記者那行寫「GPT-6 Astra vs Fable 評測轉知功能記者改投 model-task-leaderboard，主編登記 log 待下輪處理」，但轉知帳本當天只新開 H-694685。log 沒有腳本讀來派工，這筆交辦事實上遺失；且那頁依 `wiki/index.md` 領域欄歸模型記者，轉給功能記者本身就轉錯人。

**處置。**
- 新增 `scripts/ingest_gate.py`：從 `scripts/run_tests.py` 的 GATES 挑內容類閘（freshness、feature_radar、pending_markers、hierarchy、reader_language、cell_limits、tools_page、log_handoffs），安靜模式同 run_tests；另印 `data/*baseline*.json`、`data/*-allow.json` 相對 HEAD 的變動行數，非零醒目提示 commit 訊息要寫理由。SKILL.md 新增步驟 4½（4、4b、4c 寫完後、步驟 5 前跑，紅了主編同輪修到綠），核對清單加一條。
- 新增 `scripts/check_log_handoffs.py`（並入 run_tests GATES）：當日 `## D Ingest` 區段含「轉知」的行必須帶 `H-xxxxxx`（且在帳本裡）或寫「不登帳：<理由>」。不帶 `--date` 時只查本日起的區段——舊 log 不可改，全掃會讓 run_tests 永久紅。
- `scripts/pending_handoffs.py open` 依 `--page` 在 index 領域欄（子頁沿 frontmatter `parent`）推負責記者，`--to` 對不上 exit 1 並印出正確負責人；`--force --reason` 為逃生口，理由寫進帳本；另加 `--dry-run`。覆寫表兩頁：market-signals（領域商業、由投資分析記者維護）、feature-radar（不在目錄表，歸功能）。

## 2026-09-25（殼層摘要不得當排除依據；重複不是分類理由）

**起因。** `check_classification_log.py` 的 `MIN_SUMMARY = 20` 只量原始字數。09-24 兩則 HN Show HN 條目被討論串標記 `[dead]`／`[flagged]` 吃掉內文後，摘要只剩殼——Tokenhush 剩 `"💬 [flagged]\n\n💬 [flagged]"`（23 字）、per-step reasoning effort 剩 `"💬 [dead]\n\n💬 [flagged]"`（20 字）——兩者原始字數都過了門檻，主編以「無可讀摘要」排除，兩則標題明寫 Claude Code，wiki 全庫零命中。同輪另查到 09-22 有 5 則以「與昨日日報已完整報導重複」為理由排除；重複與否是記者的收錄門檻判斷（同一事件昨天報過還要不要再收），分類表沒有「重複」這一格，主編借用它來排除等於把記者的判斷權收走。

**處置。**
- `check_classification_log.py` 新增剝殼判斷：判摘要長度前先剝掉 `💬`／`[flagged]`／`[dead]`／`[deleted]` 與空白，剝完仍空（`_is_pure_shell`）才算殼；殼層摘要若 `categories` 為空（主編排除）→ 阻斷級，訊息「殼層摘要不得當排除依據，請以標題與 URL 判類派出」。有分類（未被排除）則放行，不再要求摘要可讀——殼層本來就只在「排除」這條路上有害。
- 同一支腳本新增 `reason` 命中 `重複|已報導|已報過|昨日|前日|前一日` → 阻斷級，訊息「重複與否屬記者收錄判斷，不是分類理由」；`重複` 用負向前瞻排除「不重複開列」這種同日單一事故合併敘述（如「與同日 status.claude.com 事件同一起事故，不重複開列」），只抓跨日「已報過／昨日」型的違規，避免把合法的同日事故合併判斷也當違規（2026-09-22 實測：8 則排除中若不排除該用法，會誤傷 1 則）。
- `classification.md`「分類紀錄」節、`dispatch.md` 3b 複核 prompt（加 `URL`／`互動` 兩欄，讓複核記者摘要是殼時能自己開連結判類）、`wiki-reporter-classify-review.md` 角色檔同步補判準。

**追加：生效日門檻。** 兩條新規則第一版寫成對任何日期都阻斷，跑 `TestRealLedger`（回放帳本既有每一天）立刻打中 09-22／09-24 兩個事故日期本身——帳本 append only，那兩天的舊排除行改不了，永久阻斷等於死鎖。改法：腳本常數 `ENFORCE_FROM = "2026-09-25"`，兩條新規則只對 `date >= ENFORCE_FROM` 的行阻斷，生效日前的舊行降為 ⚠️ 警示；新增 `--enforce-all` 旗標對任何日期強制阻斷，供追溯稽核／回放驗證用（`reason`／`summary` 是既有資料，帳本本身不追加更正行）。

**量測。** 回放三個真實日期（皆加 `--enforce-all` 因為都早於生效日）：09-24（殼層兩則）與 09-22（重複五則）新規則下皆 exit 1 且恰好點名事故裡的那幾則，不多不少；09-23（無殼層、無重複理由）維持 exit 0，無誤傷；同三日不加 `--enforce-all`（預設）皆降為警示、exit 0，證明生效日門檻確實擋住對舊帳本的阻斷。改壞驗紅：把可辨識標記集合從 `{flagged, dead, deleted}` 窄化成只認 `flagged`，09-24 混用 `[dead]` 的 per-step 那則（原始摘要剛好 20 字，等於 `MIN_SUMMARY`）不再被剝殼判為純殼、原始字數又不小於門檻，訊息完全消失（不再被點名）；純 `[flagged]` 的 Tokenhush 不受影響——證明判定確實跟著標記集合走，不是寫死的字串比對。

**已知缺口。** `data/classification-log.jsonl` 是既有資料，本輪未動它——09-22、09-24 兩個事故日期的舊排除行早於 `ENFORCE_FROM`，預設對帳只降級為警示、不阻斷派工，`TestRealLedger` 因此仍綠；但那兩天的排除理由本身沒有被更正（帳本上仍寫著「無可讀摘要」「重複」），需要主編對這兩天 append 更正行（依分類表補派或改寫排除理由）才是真正修好，本輪權責只在建立偵測機制與生效日門檻，不含歷史資料回填。

**量測。** 以新規則回放帳本既有 115 筆開立，8 筆會被擋：有的是 `--page` 填了事實出處頁而非目標頁（如 H-a8bd29 page 填 community-tech-patterns、實際要動 official-community-gap；H-c773a5 page 填 jensen-huang、實際要動 anthropic-government-policy），2 筆是要新建的頁或一次列多頁（查不到負責人），其餘可能本來就轉錯人（未逐筆裁定）。因此 checklist 同時寫明 `--page` 填目標記者要動的頁，新建頁／跨頁才用 `--force`。

## 2026-09-27 主編派工包與收報落帳改由腳本產生；新增 ingest 量測帳本

**起因：** 09-26 本機手工跑一輪量到：主編每天真正的判斷只有一張「url → 類別／排除理由」表，其餘都是機械搬運——68 行分類帳、六份節錄包（合計約 40K 字元手貼進 7 個 Agent prompt）、49 筆歸因手抄、log 條目、轉知 open／close 指令；手抄歸因最容易錯。安全政策記者收到 23 則，其中 14 則是同一事件（DC Circuit 判決）的不同媒體；另有 5 則是前一兩天已歸因過的同一篇，記者各自 grep 半天才確認。

**改動：**
- `scripts/build_ingest_packets.py`：主編只寫 routing.json（categories／reason／note／summary_override）。腳本先驗 routing（漏則、多出原料外的 URL、排除沒理由、note 以請／記得／順手／同步起句、來源未註冊），在記憶體模擬對帳，全過才 append 分類帳、內呼 check_classification_log，再產每類一份包與 `排除.md`。包裡帶齊 slug、日報段落原文、日報未收錄／專頁定向旗標、同事件聚合、已收錄比對；包頭「共 N 則（M 組）」、包尾 `END N`，超過 25K 字元切份。
- `scripts/collect_reporter_reports.py`：解析回報契約。歸因行驗 slug、頁面、當日原料後才 append；「已處理 H-xxxxxx」轉 close；「⚠️ 需主編轉知」印 open 草稿（負責人由 index 推）；包與回報做 URL 對帳並列未回應清單；輸出 log 骨架。預設 dry-run，`--apply` 才寫帳。
- SKILL.md 步驟 2–4、classification.md 分類紀錄、dispatch.md（條目節錄改貼包檔全文，3b 貼 `排除.md`）、checklist.md 隨之改寫；review-registry 新增 3 組同步配對；`data/ingest-packets/` 不進 git。
- `scripts/ingest_metrics.py` ＋ `data/ingest-metrics.jsonl`：步驟 5 收尾時從本機 subagent transcript 為每位記者 append 一行（turns、tool_uses、edits、cache_read、output、規則讀取方式與範圍、wiki 整讀、hook 回饋、是否不完整）。口徑：turns 與 token 以 message.id 去重——transcript 把一次回應拆成多筆記錄、usage 重複，逐筆加總約灌大 1.7 倍且倍數隨每輪工具數浮動，09-25 review 引用的 33.1M 即此口徑，去重後為 19.6M。找不到 transcript（雲端 routine）不寫零值行。首批回填 13 個日期、93 行。

**量測（09-26 重跑）：** 各類件數與手工帳完全一致；安全政策 23 則收成 7 組，包從 15.8K 降到 9.1K 字元；已收錄比對標出 09-24／09-25 已歸因的 5 則。

**設計取捨：** 原料的 `dedup_key` 是變更偵測鍵、`contributors` 是已被併掉的來源，靠這兩欄聚不起同一事件，故加上標題顯著詞交集 ≥2 作第三條依據，誤併時同組其他則仍保留標題與日報段落。早期歸因存的是 Google News 跳轉網址，已收錄比對改用文章 id 前綴比對。slug 只認整串相等或「名稱 / 子來源」，否則「GitHub Search」會靠字首 GitHub 蒙混。

**第一輪 review 修正（同日）：** 同事件聚合的標題規則首版（顯著詞 ≥2）在 09-24／25 原料上把 Reddit「prompt injection」貼文與 Salesforce 漏洞、「Opus 5.5 Costs 40% Less」與 Reddit 討論串等四對不同事件併在一起；改為顯著詞 ≥3（互為 contributors 時 ≥2）、詞長 ≥4、含數字與模型名一律不算，並以 09-24～09-26 三天回測人工確認零誤併（釘成測試）；主條目跨包一致（互動最高、同分取最早），同組其他則欄位齊全。收報腳本補全形分隔、段外標題結束欄位、巢狀括號、同批重複 close 去重、未回應清單改以標題／issue 編號比對；registry 兩組會假綠的配對刪除改由測試看守。Google News 摘要剝 HTML 後抓不到原文者會變成「標題 - 出版者」回聲：來源端改為回聲即空摘要、`check_classification_log._is_pure_shell` 加標題回聲判定，殼層排除閘才不會靜默失效。

## 2026-10-04（ingest checklist 專案根）

checklist 強制核對項與 SKILL 內一處仍寫 `CLAUDE_NEWS/wiki/`，改為「repo 根下的 `wiki/`」。見 claude-md-edit 沿革同日段。

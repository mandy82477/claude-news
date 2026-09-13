---
name: web-publish
description: 每日 pipeline 收尾段：commit wiki、web build gate、單一 push、寫 log；由 /news-pipeline Phase C agent 執行。
---

# 收尾與發布（Step 3 / 4 / 5 / 6）

由 `.claude/skills/news-pipeline/SKILL.md` 的 Phase C 背景 agent 讀取執行。REPO_ROOT／PYTHON／TARGET_DATE 由派工 prompt 傳入（值見 `.claude/skills/news-pipeline/references/dispatch.md`）。**本 skill 不 spawn 子 agent。**

---

## Step 3：Commit Wiki 變更（不 push）

用 Bash 執行（**先不 push**，於 Step 5 統一推送）：

```
git -C REPO_ROOT add wiki/ daily/TARGET_DATE.md data/source_attribution.jsonl data/pending-handoffs.jsonl
git -C REPO_ROOT commit -m "wiki: auto-ingest TARGET_DATE"
```

- `daily/TARGET_DATE.md` 是 Step 2b 的讀者版日報（`.claude/skills/reader-digest/SKILL.md`）；該步失敗時此檔不存在，`git add` 會報錯——改用 `git add wiki/ data/...` 略過即可
- `data/source_attribution.jsonl`（來源歸因）與 `data/pending-handoffs.jsonl`（轉知帳本）是 Step 2 主編彙整的產出，與 wiki 同批 commit；無變更時 `git add` 為 no-op
- 若 wiki 無任何變更，跳過 commit，繼續 Step 4

---

## Step 4：建置 Web Reader

**建置前先跑 web build gate（強制，內含完整測試套件）：**

```
PYTHON REPO_ROOT\scripts\gate_web_build.py
```

此腳本會代跑 `scripts/run_tests.py`，再依 `docs/known-test-gaps.json` 判定該不該擋。**不要另外自己跑 `run_tests.py` 再自行判斷**——判準集中在腳本裡，才不會兩處失步。

- **exit 0** → 放行，繼續執行 build（可能是「全綠」，也可能是「失敗但全屬已登記缺口」；後者腳本會印出放行理由）
- **exit 非 0** → **先走下方「gate 擋下時的修復迴圈」，不可直接跳過 build**；迴圈仍失敗才視同 Step 4 失敗：跳過 web build 與 web commit，但仍繼續 Step 5（推送已完成的 news / wiki commit）與 Step 6（記錄 log）

### gate 擋下時的修復迴圈 `[加入: 2026-08-26]`

你是 LLM agent，gate 印出的失敗訊息你讀得懂也多半修得好——擋下就放棄等於把「讀者今天看不到網站」當成對一個格式瑕疵的懲罰。（教訓見沿革檔 2026-08-26）

**流程（至多修 2 輪，每輪：讀失敗 → 修 → 重跑 gate）：**

1. 讀 gate 輸出，定位失敗的檢查與檔案行號（輸出通常直接給到 `頁面:行號` 或測試案例名）
2. 判斷失敗屬於哪一類，只修**允許清單**內的：

| 失敗類型 | 可否自行修復 | 修法 |
|---|---|---|
| wiki 內容格式（懸置標記語法、探針不合格、欄位缺漏、日期格式、表格對帳差一列） | ✅ | 依對應規則檔修 `wiki/` 內容本身（如探針改寫成合規字串），修完併入本次 wiki commit（`git commit --amend` 或補一個 `wiki: fix gate failure` commit） |
| 規則檔同步配對／錨點（`check_rules.py`），且是**本次 pipeline 改動造成** | ✅ | 修回一致 |
| 單元測試失敗、腳本層 bug、環境依賴缺失 | ❌ | 不修——腳本改動需要人工 review，照舊擋下並回報 |

3. 重跑 `gate_web_build.py`：exit 0 → 繼續 build，Step 6 log 在摘要行後**多記一行** `REPAIRED: <一句話：修了什麼>`；仍非 0 → 進第 2 輪；2 輪後仍失敗 → 放棄，照舊跳過 build 並在 log 記 `repair attempted, still blocked`

**硬性禁止（違反任一條就等於把 gate 拆掉）：**
- 不可修改任何 `scripts/check_*.py`、`run_tests.py`、`gate_web_build.py`
- 不可為了放行而新增 `docs/known-test-gaps.json` 條目（該檔只在人工登記 workaround 時動）
- 不可用「刪掉觸發失敗的內容」了事——探針寫錯要改對，不是把整條懸置標記刪掉；刪除等於湮滅待查證事項
- 修復只准動失敗訊息**指名**的位置，不可順手擴大改動範圍

Step 6 的 log 一律抄腳本輸出的**最後一行摘要**（例如 `測試失敗 3 案，全屬已登記缺口（feedparser-sgmllib）- web build 放行`），不要自己改寫措辭——log 是日後判斷「哪天為什麼沒上站」的唯一證據。

> **為何是 gate 而不是直接看測試結果 `[加入: 2026-08-01]`：** 過緊的 gate 用「正確性」的名義製造「可用性」的損失。放寬的邊界很嚴格：**只有登記在 `docs/known-test-gaps.json`、且錯誤訊息也對得上的失敗才放行，出現任何一個沒登記的失敗就照舊全擋**；允許清單空的時候，行為等同舊規則。（教訓見沿革檔 2026-07-31）

- 放行後依序執行（frontmatter 必須先於 build_web，兩者都吃當日已寫完的 wiki）：

```
PYTHON REPO_ROOT\scripts\enrich_attribution_publisher.py
PYTHON REPO_ROOT\scripts\gen_wiki_frontmatter.py
PYTHON REPO_ROOT\scripts\build_web.py
```

- 前兩支皆為冪等的衍生資料重算，失敗不擋 build：
  - `enrich_attribution_publisher.py` 補當日新歸因的 `publisher` 欄位（記者回報的 slug 只有斜線前半段，`google-news` 底下實際有 250+ 家出版者）
  - `gen_wiki_frontmatter.py` 重算頁面 frontmatter（入鏈數、供料數、停滯天數、signal），供 Obsidian Bases 查詢；不跑則 `wiki/_views/wiki-health.base` 的數字會停在上次生成日
- `build_web.py` 成功後繼續；若失敗，回報錯誤並跳過推送

---

## Step 5：Commit Web 並統一推送（單一 push）

先 commit web 變更，再用**單一 git push** 一次推送本次所有 commit（news + wiki + web）。

**為何單一 push：** 每次 `git push` 都會觸發一個 GitHub Pages 部署。分多次 push 時，多個部署會互相搶佔（concurrency race），最後關鍵的 web 部署可能被取消或失敗，導致線上停留舊版而 pipeline 無從得知。一次推送 = 一個部署 = 無 race。

```
git -C REPO_ROOT add web_reader/
git -C REPO_ROOT commit -m "web: rebuild TARGET_DATE"
# 統一推送本次所有 commit（一次 push 只觸發一個 Pages 部署）
git -C REPO_ROOT push
```

- 若 web build 無變更，仍須執行 `git -C REPO_ROOT push` 推送先前的 news / wiki commit
- **replay 路徑收尾（強制）`[改版: 2026-08-29]`**：本次若曾 `cp src/gathered_archive/<date>.json src/gathered_items.json`（backfill 模式，以及雲端每日班——它現在也走這條路徑），**必須在 Step 1c 之後、任何 push 之前（含中止落地的那次）**執行 `git -C REPO_ROOT checkout -- src/gathered_items.json` 還原成 repo 版本。
  - **不可等到 push 之後**：本 repo 的 `rebase.autoStash` 為 false，工作樹髒的話下方 push 重試的 `git pull --rebase` 會被 git 直接拒絕（不是衝突，是前置檢查），兩次重試必然失敗，而雲端未推送的 commit 隨容器銷毀救不回來——日報、wiki、web 全部白做
  - **不可提早到 Step 1c 之前**：`--confirm-digest` 讀的就是這個檔；Step 2 的專頁定向路由也吃它的 `topic` 欄（那是該欄唯一的來源）
  - **中止路徑也算**：cp 之後才觸發的中止（新鮮度防線、原料健康檢查 exit 2/3）同樣要先還原再 commit abort log，否則 abort log 推不上去、雲端看起來像中途死亡，把一次正確的閘門攔截誤報成靜默失敗

**push 失敗重試（強制）`[加入: 2026-07-25]`**

push 被拒最常見的原因是 non-fast-forward——GitHub Actions 的 `daily-gather` 或另一個環境在你執行期間也 push 了（Actions 排程實測延遲過 2 小時 42 分，時間緩衝不保證不撞）。**在雲端，未推送的 commit 會隨容器銷毀且下次是全新 checkout，救不回來**；本機雖然 commit 還在，仍應照同樣程序處理，兩邊行為一致。

```
git -C REPO_ROOT rev-parse --abbrev-ref HEAD   # 不是 master 就先 git checkout -B master
git -C REPO_ROOT push || {
  git -C REPO_ROOT pull --rebase origin master && git -C REPO_ROOT push
}
```

- 最多重試 **2 次**，每次都先 `pull --rebase` 再 push
- **工作樹不乾淨時不得走 `pull --rebase`** `[加入: 2026-09-06]`：本 repo `rebase.autoStash` 為 false，git 會在前置檢查就拒絕（`cannot pull with rebase: You have unstaged changes`），兩次重試必然失敗；而 `--autostash` 是**明文禁止**的——`git stash` 的作用域是整個工作區，多 session 並行時會連同別人正在寫的檔一起捲走（教訓見 `.claude/reporter-rules/shared.md`「不可執行改動工作區全域狀態的 git 指令」）。改走：

  ```
  git -C REPO_ROOT fetch origin
  git -C REPO_ROOT diff --name-only HEAD...origin/master     # 只有遠端多出來的檔
  # 與 git status 的髒檔清單比對：無交集 → 可安全 merge
  git -C REPO_ROOT merge --no-edit origin/master && git -C REPO_ROOT push
  ```

  **有交集就停手**：不 merge、不 stash、不 checkout，Step 6 log 記 `Push DEFERRED - dirty overlap`，列出重疊檔名交使用者處理。commit 還在本機不會遺失（雲端無此路徑——雲端是 fresh clone，工作樹本來就乾淨，走原 `pull --rebase` 即可）。
- 先確認在 master 上：2026-07-14 曾因 session 啟動時 `origin/master` 快取落後而處於 detached HEAD，該狀態下 push 不會更新遠端分支
- **允許自動解的衝突只有兩類**：
  1. `src/news_aggregator/emitted_items.json`——此檔有兩個寫者（GitHub Actions 加入未確認條目、pipeline 翻確認欄位）。解法固定：**放棄我方的 confirm commit、保留遠端版本**，因為日報上站遠比確認欄位重要，未確認的條目只會被重新提供一次，是良性退化。處理後標「emitted-cache 確認本次放棄，項目將於次日重新提供」
  2. **append-only 檔的 append-append 衝突 `[加入: 2026-09-03]`**——`wiki/log.md`、`data/source_attribution.jsonl` 等只會在檔尾各自新增的檔（白名單住 `scripts/resolve_append_only.py` 的 `APPEND_ONLY`，不在此重抄）。解法固定：**跑 `python scripts/resolve_append_only.py`**，它以 `git merge-file --union` 三方合併保留兩側新增（順序 base→ours→theirs），只動白名單內的檔；有任何白名單外的衝突它會 exit 1 且不動任何檔——此時走下一條 abort。成功後 `git -c core.editor=true rebase --continue` 再 push。
     > 沒有判斷成分的衝突不該逼整班重跑。（起因見沿革檔 2026-09-02）
- **其他任何檔案的衝突 → 不自行解**：`git rebase --abort`，Step 6 log 記 `Push FAILED - rebase conflict`，並列出衝突檔案清單
- 兩次都失敗 → Step 6 log 記 `Push FAILED`，完成摘要明確標示**本次產出全部未上站**，不可寫成完成

---

## Step 6：寫入 task_scheduler.log

整個 pipeline 結束後，**無論成功或失敗**，都必須 append 執行記錄至：

```
REPO_ROOT\src\logs\task_scheduler.log
```

**本步驟由 Phase C agent 執行**，Step 0/1a/1b（Phase A）與 Step 2（Phase B）的結果由呼叫 session 透過 Phase C 的 spawn prompt「已知結果」欄位傳入（見 `.claude/skills/news-pipeline/references/dispatch.md` Phase C），Phase C agent 不需重新查證，直接引用即可；Step 3/4/5 的結果則是 Phase C agent 自己執行後得知。

**例外：若 Phase A 的 Step 1a 失敗**，pipeline 不會進入 Phase C（見 Phase B 的失敗處理），此時 Step 6 log 改由呼叫 session 直接 append，格式相同。

格式（依各步驟結果填入 OK / FAILED / SKIPPED）：

```
[DATE TIME] === Agent pipeline start (TARGET_DATE) ===
[DATE TIME] Aggregator OK
[DATE TIME] Wiki ingest OK
[DATE TIME] Building web reader...
[DATE TIME] Single push done (news + wiki + web)
[DATE TIME] === Pipeline complete (agent) ===
```

- Step 0 昨日缺跑時，額外寫一行 `WARN: yesterday digest missing (YESTERDAY)`
- Step 1 失敗時，寫 `Aggregator FAILED - stopping`，之後不繼續（此情況下由呼叫 session 直接寫入，見上方例外）
- Step 2 失敗時，寫 `Wiki ingest FAILED`
- Step 2b 失敗時，寫 `Reader digest FAILED - falling back to news/`
- Step 4 gate 判定時，抄 `scripts/gate_web_build.py` 輸出的最後一行摘要（放行與擋下都要寫，例如 `測試全綠 - web build 放行`／`測試失敗含未登記案例（...）- web build 擋下`）
- Step 4 build_web 失敗時，寫 `build_web FAILED - pushing news/wiki only`
- Step 5 push 失敗時，寫 `Push FAILED`
- 時間戳使用系統當前時間（`Get-Date` 或 `date` 指令取得），格式 `[週X YYYY/MM/DD HH:MM:SS.SS]`

---

## 完成摘要

完成後輸出：

| 步驟 | 結果 |
|------|------|
| Step 0 昨日缺跑檢查 | ✅ 無缺失 / ⚠️ 昨日（YESTERDAY）日報缺失 / ⏭️ backfill 模式跳過 |
| Step 1 新聞聚合 | ✅ / ❌ |
| Step 2 Wiki Ingest | ✅ / ❌ |
| Step 2b 讀者版日報 | ✅ / ⚠️ 今日無新知（照寫空日檔）/ ❌ 退回 news/ |
| Step 3 Wiki Commit | ✅ / ⏭️ 無變更 / ❌ |
| Step 4 Web 建置 | ✅ / ❌ |
| Step 5 統一推送（news+wiki+web） | ✅ / ❌ |
| Step 6 Log 寫入 | ✅ / ❌ |
| 目標日期 | TARGET_DATE |

### 📋 待使用者裁示 `[加入: 2026-08-08]`

摘要表之後**必接**此區塊——待確認事項只寫進 `wiki/log.md` 等於沒有出口，使用者不會讀那個檔（起因見沿革檔 2026-08-08）。

作法：Grep `wiki/log.md` 中 TARGET_DATE 該次 ingest 紀錄的「📋 待使用者確認」段落，逐條轉貼成一行摘要（`- [頁面/主題]：一句話問題`）。同時 Grep 前 14 天的 ingest 紀錄，**同一議題重複出現者標「⏳ 已擱置 N 天」**置頂。

**另必接 Step 1b-3g 的截止日複查清單 `[加入: 2026-08-28]`：** 若 3g（見 `.claude/skills/news-digest/SKILL.md`）有命中（已過期或 7 天內到期），逐個截止日轉成一行 `- ⏰ [YYYY-MM-DD]（剩 N 天，M 處引用）：[事件]——需查官方原文確認日期是否仍有效`。這批與 log.md 的裁示不同源，**不可因為 log.md 沒有對應段落就省略**；3g 印「無需複查的截止日」時整段省略。

無任何未決項時寫 `- 無`，不可省略此區塊。

---

## 本 skill 的邊界

- 所有 Bash 指令使用絕對路徑，不依賴 PATH 環境變數
- Step 4 web build gate（`scripts/gate_web_build.py`）擋下時跳過 web build 與 web commit，仍須執行 Step 5 的統一 push；gate 放行（含「失敗全屬已登記缺口」）時照常 build
- Step 4（web build）失敗時跳過 web commit，但仍須執行 Step 5 的統一 push（推送已完成的 news / wiki commit）
- **所有 git push 集中在 Step 5 一次完成**；中途步驟（1b、3）一律只 commit 不 push，避免 Pages 部署並發競爭
- **Step 6 log 寫入必須執行**，即使前面步驟失敗也不能跳過
- 繁體中文輸出

---

> **沿革檔：** `docs/rules-changelog/news-pipeline-steps.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，`[加入: 2026-09-04]`）

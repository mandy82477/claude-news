---
name: news-gather
description: 每日 pipeline 抓料段：缺跑檢查、冪等閘、Python 抓取歸檔、emitted-cache 確認；由 /news-pipeline Phase A agent 執行。
---

# 抓料與閘門（Step 0 / 0b / 1a / 1c）

由 `.claude/commands/news-pipeline.md` 的 Phase A 背景 agent 讀取執行。REPO_ROOT／PYTHON／TARGET_DATE 由派工 prompt 傳入（值見該檔）。**本 skill 不 spawn 子 agent。**

同屬 Phase A 的 `Step 1b：生成日報` 在 `.claude/skills/news-digest/SKILL.md`，接在 Step 1a 之後、Step 1c 之前執行。

## 本機與雲端的行為必須一致 `[加入: 2026-07-25]`

**四個 pipeline skill（news-gather／news-digest／reader-digest／web-publish）是唯一的步驟語意來源。** 本機 `/news-pipeline` 與雲端 routine 跑出來的行為必須相同——同樣的閘門、同樣的失敗處理、同樣的重試、同樣的產物。

雲端 runbook（`docs/cloud-runbooks/daily.md`）**只允許承載環境差異**，共三類，其餘一律寫在 skill 檔：

| 允許出現在 runbook 的 | 不允許（必須寫在 skill 檔） |
|------|------|
| 環境值（路徑、`python3` vs `python.exe`、日期取得方式） | 任何閘門、檢查、重試、失敗處理邏輯 |
| 哪些步驟不適用該環境（雲端跳過 Step 1a，因抓料由 GitHub Actions 完成） | 步驟本身的做法與判準 |
| 無人值守政策（需使用者確認的動作改寫成待辦） | 需要確認的是哪些動作 |

> 判斷標準：這條規則換到另一個環境還成立嗎？成立 → 寫在 skill 檔。只在特定環境成立 → 才進 runbook。（反例見沿革檔 2026-07-25 A）

---

## Step 0：昨日缺跑檢查

**僅當 TARGET_DATE 為今日時執行**（backfill 模式，即 TARGET_DATE 非今日時跳過本步驟——補跑歷史日期時「昨天」無意義）。

計算 TARGET_DATE 的前一天 YESTERDAY，檢查 `news/YESTERDAY.md` 是否存在：
- 存在 → 一行帶過，繼續 Step 1a
- 不存在 → 記錄缺失，於完成摘要表加一列「⚠️ 昨日（YESTERDAY）日報缺失」，並提示使用者可執行 `/news-pipeline` 帶日期參數手動補跑；Step 6 log 寫入 `WARN: yesterday digest missing (YESTERDAY)`。**不自動補跑**（避免排程場景下連鎖跑兩天造成時間不可控）

---

## Step 0b：冪等閘 `[加入: 2026-07-25]`

檢查 `news/TARGET_DATE.md` 是否已存在：

- **不存在** → 正常繼續
- **已存在，且 TARGET_DATE 是今日（排程／無參數模式）** → **中止**，理由 `digest already exists`，寫入 Step 6 log 後結束。重跑會覆寫日報並讓 wiki 記者對同一批新聞重複 prepend——日報覆寫還能重生，**wiki 重複條目要人工逐頁挑，代價高得多**
- **已存在，但 TARGET_DATE 由參數明確指定（backfill 模式）** → 使用者已明示覆寫意圖，**不中止**，但在完成摘要標一行 `⚠️ 覆寫既有日報 TARGET_DATE`，並提醒 wiki ingest 可能產生重複條目、需人工核對

會觸發此閘的情境：手動觸發撞上排程、當日已補跑過、或前次執行日報已產出但後段失敗。

---

## Step 1a：新聞抓取（Python，不呼叫 LLM）

用 Bash 執行：

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main --gather-only [--date TARGET_DATE]
```

- 若 TARGET_DATE 非今日，加上 `--date TARGET_DATE`
- 成功後寫出 `src/gathered_items.json`（含 items、date、source_status）
- 若失敗（exit code 非 0），停止並回報錯誤，不繼續後續步驟

**抓完立刻歸檔（強制）`[加入: 2026-07-25]`：**

```
PYTHON REPO_ROOT\scripts\archive_gathered.py
```

把原料存一份到 `src/gathered_archive/<date>.json`（保留 14 天）。`gathered_items.json` 沒有按日分檔、每次抓料直接覆寫，沒有這份副本的話，**日報沒產出的那天、已抓到手的原料會在隔天被蓋掉，而來源視窗早已滾過去——那天就永久漏了**。GitHub Actions 的 `daily-gather` 呼叫同一支腳本，兩邊行為一致。

---

### 補跑（backfill）注意事項 `[加入: 2026-07-25]`

雲端漏跑後在本機 `/news-pipeline <date>` 補，有四個已知摩擦點：

**1. 別把 `src/gathered_items.json` commit 上去。** 補跑會**覆寫**這個檔（它沒有按日期分檔），寫進去的是補跑那天的資料。這個檔同時是雲端 routine 的輸入——雲端啟動時讀到的若不是當日資料，新鮮度防線會中止當天執行。也就是**一次本機補跑可能連帶讓當天的雲端排程空跑**。
- 只有 GitHub Actions 的 `daily-gather` 該 commit 這個檔
- 還原動作與**時機**見 `.claude/skills/web-publish/SKILL.md` `Step 5` 的「replay 路徑收尾」，此處不重複——時機是有講究的（太早會讓 Step 1c、Step 2 讀到錯的日期，太晚會讓 push 重試失效），兩處各寫一份就會失步，而失步的那一份會在無人值守時生效
- 絕不要在補跑流程裡用 `git add -A` / `git add .`

**2. 先找當日原料副本，找不到才重抓。** `src/gathered_archive/<date>.json` 是抓料當下存的原料副本（保留 14 天，由 GitHub Actions 與本機 Step 1a 各自寫入）：

- **副本存在** → **跳過 Step 1a**，直接 `cp src/gathered_archive/<date>.json src/gathered_items.json`，然後從 Step 1b 開始。這是 replay 當天的真實原料，補出來的日報與原本該產出的一致
- **副本不存在**（超過 14 天，或那天連抓料都失敗）→ 才走 Step 1a 重抓。此時要有心理準備：來源多是 RSS／API 的近期視窗，撈不到幾天前的內容。gather 的失敗補撈機制把回看窗口最多拉到 **50 小時**（約兩天），`--date` 補跑則以「目標日 00:00 UTC 到現在」為窗口再裁切回目標日——**離現在越遠，補出來的日報越空，超過兩三天基本上補不回來**。這是來源特性不是 bug；接受那幾天較稀疏，不要為了填滿而放寬收錄門檻

**3. 補跑不套用跨日去重快取**（`main.py` 明文：backfill 不碰 cache，否則會拿今日的快取去誤刪過去的項目）。因此補出來的日報**可能與前後日的日報有重複條目**，屬預期行為，wiki ingest 端由 `wiki-ingest.md` 的「確認最近是否已處理過同一份日報」把關。

**4. 補跑日報已存在時**：`Step 0b：冪等閘` 會因為你明確給了日期參數而放行覆寫，但 wiki 那邊會產生重複條目，需人工核對——見該步驟說明。

---

## Step 1b：生成日報（不在本檔案）

逐字規格見 `.claude/skills/news-digest/SKILL.md`（步驟）、`.claude/skills/news-digest/format.md`（骨架與機械契約字串）、`.claude/skills/news-digest/selection.md`（選材判準）。Phase A agent 在 Step 1a 之後接著執行該 skill，成功 commit 後才回到本檔的 Step 1c。

---

## Step 1c：確認 emitted-cache（強制，commit 成功後才執行）

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main --confirm-digest --date TARGET_DATE
```

- 把 Step 1a 篩出的項目標記 `digest_confirmed: true`；未確認的項目視同未出現過，下次重跑會重新提供、不會被永久靜默丟棄（2026-07-13 曾因日報未產出導致 25 則新聞永久漏失，詳見當日 log）
- 失敗只記警告，不影響已完成的 news commit，繼續後續步驟
- **確認結果必須進 git（強制）`[加入: 2026-07-25]`**：`--confirm-digest` 改的是 `src/news_aggregator/emitted_items.json`，這個檔不 commit 就等於沒改過——GitHub Actions 與雲端 routine 都是全新 checkout，讀的是 repo 版本。執行完 append 下列指令，讓它跟著 Step 5 的統一 push 一起上去：
  ```
  git -C REPO_ROOT add src/news_aggregator/emitted_items.json
  git -C REPO_ROOT commit -m "data: confirm emitted-cache TARGET_DATE"
  ```
  （無變更則跳過。**不要單獨 push**，一律留給 Step 5。這樣「日報上站」與「快取確認」同批推送，要嘛一起成功、要嘛一起回到未確認狀態，不會出現「確認了但日報沒上站」的不一致）
- 漏做的實際後果見沿革檔 2026-07-24

---

## Step 2：Wiki Ingest（不在本檔案）

Step 2 由呼叫 `/news-pipeline` 的 session 親自執行，**也不可包進任何背景 agent**，完整步驟見 `.claude/commands/wiki-ingest.md`（不在此重複，避免兩份副本失步）。執行方式與失敗處理原則見 `.claude/commands/news-pipeline.md` Phase B：Step 2 失敗時記錄但仍進入 Phase C（web build 不依賴 wiki）。

---

## 本 skill 的邊界

- 所有 Bash 指令使用絕對路徑，不依賴 PATH 環境變數
- Step 0 僅在 TARGET_DATE 為今日時執行；backfill 模式（TARGET_DATE 非今日）跳過
- Step 1 失敗時停止整個 pipeline（Phase A agent 立即停止，不進入 Phase B / Phase C，Step 6 log 改由呼叫 session 直接寫入）
- 中途步驟一律只 commit 不 push，所有 git push 集中在 `.claude/skills/web-publish/SKILL.md` 的 Step 5 一次完成
- 繁體中文輸出

---

> **沿革檔：** `docs/rules-changelog/news-pipeline-steps.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，`[加入: 2026-09-04]`）

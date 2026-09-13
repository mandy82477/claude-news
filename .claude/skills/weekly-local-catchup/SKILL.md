---
name: weekly-local-catchup
description: /weekly 步驟 0：補跑雲端沒做的 lint 步驟（5b/5c 等）、呈報 lint 待裁示事項、跑開放迴路掃描並回報三個數字。
---

# 本機專屬步驟補跑（`/weekly` 步驟 0）

由 `.claude/commands/weekly.md` 步驟 0 呼叫，**先做，不可略過**；產出一律併入該檔步驟 3 的單一 push，不自行 commit。

`/wiki-lint` 有幾個步驟需要「網路 ＋ LLM 同時具備」：GitHub Actions（無 LLM）做不到，雲端 routine 則**看該環境的網路白名單開到哪**——雲端環境預設是 Trusted（約 70 個網域），本專案需要的官方文件站與榜單站不在內。

**這幾步在雲端已改為探測式**（`python scripts/cloud_egress_check.py --group <組>`，見 `.claude/skills/wiki-lint-sweeps/references/sweeps.md` 各節）：探測到 OK，雲端 lint 自己就做完了，本步只會看到「已於雲端完成」；探測到未開才落到這裡。所以本步的正確心態是**補跑那些雲端真的沒做的**，不是無條件重跑一遍——先 Grep `wiki/log.md` 最近一次 lint 紀錄，看該步寫的是數字還是「雲端 egress 未開，跳過」。

依序執行，全部讀 `.claude/skills/wiki-lint-sweeps/references/sweeps.md` 的對應節，不在此重述做法：

1. **5b 跨家任務榜單週更**——雲端該步已記數字則跳過；記「雲端 egress 未開，跳過」才補跑，照 `.claude/skills/wiki-lint-sweeps/references/sweeps.md`「5b. 跨家任務榜單週更」執行（派 `general-purpose` ＋ `model: "haiku"` 抓榜）。**同理適用 5c、5e、5m**——這四步的雲端執行與否由探測決定，不再固定落到本機

2. **5c 逾期待查證清算**——照該檔「5c. 逾期待查證清算」執行，**Lane A（本輪額度 10）＋Lane B（本輪額度 8）**（`check_pending_markers.py --queue` 已內建兩條分流；Lane A 多數可免 web，但**探測判為未開時整個 5c 跳過**，本機一律可做）。務必照 5c 第 5 步做結案回掃，並把輸出的「📊 產消對帳」與末尾「⚠️ 舊語法盲區」一併抄進回報

3. **lint 待裁示事項呈報**——`Grep "待使用者確認\|待裁示" wiki/log.md` 取最近 3 次 lint 紀錄的未決事項，**直接列在 `/weekly` 的輸出裡呈給使用者**，每項標「⏳ 已擱置 N 週」。理由：那些事項只寫進 `wiki/log.md`，而**使用者不讀該檔**——不呈報等於沒提過

4. **開放迴路掃描**——跑 `python scripts/open_loops.py`，它彙整**五類**開放迴路的可見性（只報數字與最舊年齡，不合併處理權——每類仍由各自流程消化）：未 commit 的實質改動、逾複查日的 workaround（表在 `docs/workaround-register.md`）、懸置標記逾期＋舊語法盲區（處理端 `/wiki-lint` 5c）、`wiki/reader-notes.md` 的 ⏳（處理端 `/wiki-weekly-review`）、`wiki/feature-radar.md` 的 ⏳（逾期判定端 `/wiki-lint` 5a）。另附一盞「人類質疑時效燈」：`wiki/log.md` 最新 Query 條目距今 >21 天即亮 ⚠（另計不入總；已知質疑模式由 `/wiki-lint` 7b 依 `.claude/skills/wiki-lint-reader-acceptance/references/inquiry.md` 抽題代打，新型質疑仍靠使用者）。**輸出原樣抄進 `/weekly` 的回報**，同第 3 項的理由：只寫進 log 等於沒提過。日常另有 SessionStart hook 在開啟專案時提醒未 commit 的實質改動。

   輸出末尾分成**三個數字**，各答一個問題：

   | 數字 | 回答什麼 | 組成 |
   |------|---------|------|
   | **需收尾** | 這次該做完的 | 未 commit ＋ 逾期 workaround |
   | **已跳票** | 已逾自身期限的承諾（同質、可追蹤） | 逾期 workaround ＋ 逾期懸置 ＋ reader-notes ⏳ ＋ feature-radar ⏳ 逾 90 天者 |
   | **存量遷移** | 格式債，沒對讀者承諾過什麼 | 舊語法盲區（另計，不入總） |

   掃描失敗時標「數量未知」、總計印下界 `≥`、exit code 非 0，不得靜默回 0。三個數字為何不合併、失敗為何不得當 0：見沿革檔 `docs/rules-changelog/CLAUDE.md` 2026-08-29。

---

## 邊界

- 由跑 `/weekly` 的本機 session 執行；5b 抓榜派 `general-purpose` ＋ `model: "haiku"`，其餘自己做。
- 不自行 commit、不 push——四項產出一律併入 `.claude/commands/weekly.md` 步驟 3 的單一 push。
- 雲端已完成的步驟不重跑；`open_loops.py` 失敗不得靜默回 0，照上表標「數量未知」。
- 第 3、4 項的輸出**必須出現在 `/weekly` 的回報裡**才算做完，只寫進 `wiki/log.md` 不算。
- 失效模式已知並接受：哪一週沒跑 `/weekly`，這幾步那週就沒跑（沿革檔 `docs/rules-changelog/weekly.md`）。

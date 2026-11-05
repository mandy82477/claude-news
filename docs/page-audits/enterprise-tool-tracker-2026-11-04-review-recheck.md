# 第 25 波評審實作複核：topics/enterprise-tool-tracker（2026-11-05）

> 上一輪是 `enterprise-tool-tracker-2026-11-04-review.md`（🔴1–2、🟡1–4、實作單 0–9 步）。這輪對照實作 commit `61a4b77`、gen 的 `164b79d`、web 的 `14e0c91`。實作前先 merge 了 origin/master（`335a33e`）。
> 我只做了讀取和重跑，沒有 git 寫入。`build_web.py` 改到的 `web_reader/index.html`、`sw.js` 已用 `git show HEAD:` 還原。暫存檔在 `<scratchpad>/w25/recheck/`。工作樹裡有一個 `wave25-cold-reader-recheck-2026-11-05.md`，是平行的 agent 加的，不是我。

## 結論：**放行**

🔴 0、🟡 1（只有文件數字，不擋）。上一輪的 🔴1–2、🟡1–4 都落地了。已知的兩處偏離（handoff 2、ledger 列補寫）都有紀錄，結果也正確。

## 逐步表

| 步 | 判定 | 證據 |
|---|---|---|
| 0 驗原檔 | 偏離，無害 | 實作前先 merge 了 `335a33e`。`git diff --stat e90dace 335a33e` 對第 0 步的路徑只動到 `market-signals.md`（40 行），兩頁、規則檔、registry 都是 0。L90 的 Globant 句是 context 行，沒有改，所以 H-b86355 仍然成立 |
| 1 fix_review | 照做 | 落地的頁跟 `D/out` 去掉 frontmatter 前 20 行後 `diff` 為 0（兩頁）；fix 的字串都在（見抽驗） |
| 2 rebuild | 照做 | 我在 repo 跑 `verify.py <repo> <repo>/wiki`，結果是 `照搬行逐字核對 150 行；懸置標記 0→0；表 59 列/50 家 → 48 列/家（通路移出 8）`、`結論：OK`；行數 259／194 |
| 3 肉眼抽驗 | 照做 | 表內已沒有「細節見下方／下方細節」。L119–121 三句都在。Goldman L56 的工具欄是 `Claude Code；Claude AI（香港）` |
| 4 重產文件 | 照做，有一處漏 | draft 裡「細節見時序」出現 6 次（≥2）；proposal L75 已改成 150 行。漏的是 map L3，見 🟡1 |
| 5 落地 | 照做 | `pages.md`、`daily.md`、`review-registry.json` 跟 `D/tmp_after` 用 `diff -q` 比相同；gen 單獨成一個 commit（`164b79d`） |
| 6 shared.md | 照做 | L137 的新句跟評審 🟡4 逐字相同；`check_rules` 結果 ✅ |
| 7 全閘 | 照做 | 我重跑過，全部 exit 0，詳見下方「閘」 |
| 8 轉知 | 偏離（已知） | H-d43749（handoff 1）、H-b86355（評審新增 3）都在 `data/pending-handoffs.jsonl`，狀態 open，`pending_handoffs.py list` 列得出來。handoff 2（→主編 index）沒有開單，改由主編直接改 `wiki/index.md` L138 鉤子，新字跟提案 §6 第 2 列相同；ledger 第 25 列和 log 都註明了「index 主編直接改」 |
| 9 帳與收尾 | 照做 | `61a4b77` 包含 ledger 第 25 列（「實作完成待複驗」，有註明 🔴1–2、🟡1–4 已吃）、log 的 11-05 Query 條目、index、handoff 帳本、proposal／map／draft。review.md 從 `bd7ea3d` 之後沒動過，所以不必再 add。裁決紀錄第 25 波兩條在 ledger L127–128 |

## 抽驗

- **家數**：我用 `count.py` 重數主表，48 列，沒有重名；結果 ✅35／⚠️7／❌3／❓2／🔄1，跟摘要 L42 一致。排序違規 0，備註超過 120 字的 0。
- **移出 8 家都有家**（數的是 pc＝partnerships-compute 的命中數，archive＝本頁 archive 的命中數）：Cognizant pc3／archive4、Globant 1／1、DataArt 1／1、Okta 1／1、DXC 3／2、富士通 1／1、KPMG pc1、Nimble Gravity 在 pc L248 和 archive L76。表外的時序裡仍提到 Cognizant（L98、L208）、DXC（L215），這是合作敘事，不算開列。
- **補的 6 家**：Palantir L57、Schwab L59、Novo Nordisk L68、Nvidia L70、Booz Allen L71、Orion L72。字句跟上一輪核過的出處一致（product-vulns、customers、pc L165／L167／L298）。Nvidia、Booz Allen 兩列有寫「官方未回應個案」，懸置沒有複製到本頁。
- **「細節見時序」**：Epic L58、Replit L60、Meta L64、Shopify L75、ReliaQuest L76、Samsung L80。後三家在主頁 08 月總結 L196–199 都有對應的一句，並連到 archive `#2026-08`。L226 改成「Travelport+Cognizant 新增採用（見上方表）；富士通、Nimble Gravity 屬通路夥伴」。時序裡剩下的 16 處「詳見上方使用現況表」，指的都是還在表上的公司。
- **Accenture 上限句**：L120 寫「Accenture 報銷每月 $29（是否限 Claude Code 未見）」，跟表上 L61「不限特定工具」一致。
- **Goldman 工具欄**：見第 3 步。備註仍寫「禁止行員用 Claude Code 與 GitHub」。
- **選型影響 7 條**：
  - ① Meta L64、Microsoft L65 有減用數字；Google L69 是 09-15 ✅；Amazon L100 是 05-05、雙軌。
  - ② `#### 2026-10-05` 在 L156。
  - ③ Epic L58、Uber L97、UiPath L99、Amazon L100 的工具欄都有「＋X」，Notion L88 是「Claude Agents + Cursor」。
  - ④ JPMorgan L67「部分工程師每月 $2,000」、Uber L97「設用量上限」。
  - ⑤ Nvidia L70、Palantir L57、Booz Allen L71。
  - ⑥ JPMorgan L67 06-18 出口管制、OKX L77 和 Goldman 08-20 區域存取；business-risks L51 有「換得了」。
  - ⑦ competitor-landscape L177 有 `### Microsoft／GitHub`。
  - 7 條都撐得住。
- **網站**：`parse_enterprise_tracker` 結果是 enterprises 48／tools 27／matrix 48／rows 48，跟評審預期相同。

## 閘（我重跑，全部 exit 0）

- `check_hierarchy` ✅（32 個母頁）
- `check_pending_markers` ✅
- `check_wiki_freshness` OK（143 頁）
- `check_rules` ✅ 全部確定性檢查通過
- `check_cell_limits`：無新增超限
- `check_reader_language`：無新增命中
- `build_web` exit 0，輸出「斷鏈 WARN 23／錨點 WARN 0」。本頁那筆斷鏈 `[[news/2026-05-01]]` 在 `e90dace` 就有，不是這次新增的
- `run_tests` exit 0
- 閘檔：`git show --stat 61a4b77` 列出的 13 個檔都不符合 `guard_roles.py` L52–56 的 GATE_FILES。`data/pending-handoffs.jsonl` 不是閘檔

## 發現

**🟡1 proposal-map L3 還寫「155 行」**
- 評審修法後照搬行是 150 行（verify 實跑結果；proposal L75 已改）。`splice_docs.py` L19 只改了 proposal，沒碰 map 頁頭。這是我上一輪修法腳本漏掉的，只影響文件，頁面不受影響。
- 修法（Edit `docs/page-audits/enterprise-tool-tracker-2026-11-04-proposal-map.md`，命中 1 處）：
  - old：`逐字核對（155 行）`
  - new：`逐字核對（150 行，評審修法後）`

**不算發現，記一下**：
- 11-04 雲端 ingest 已經 merge 進來，沒有動到本頁。下次 ingest 第一次碰本頁時，請驗「換狀態同批重數家數」（N5 沒有閘看守）。
- 等複驗做完，ledger 第 25 列的「實作完成待複驗」要改寫成結果。

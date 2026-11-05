# 第 28 波評審複核：entities/sonnet-5-5 實作（2026-11-05，commit 6fe72bf）

> 對照：`sonnet-5-5-2026-11-05-review.md` 第四節 12 步，以及 verified 第一、五、六節。方法：逐檔看 `git show 6fe72bf` 的 diff；把設計者 `out/` 新頁和 repo 的頁面做 diff（只差 frontmatter 的 `inbound_links`）；閘在 repo 內實跑，`build_web.py` 動到的 14 個 `web_reader/` 產物已用 `git show HEAD:<path> > <path>` 還原，`git status` 乾淨。

## 一、逐步

| 步 | 判定 | 依據 |
|---|---|---|
| 1 底稿未被 ingest 動過 | 照做 | `out/` 與 repo 新頁除 frontmatter 外完全相同；`apply.py` 的斷言沒有紅 |
| 2 新頁 🔴1、🟡4–6 | 照做＋兩處偏離（接受） | L108 兩個數 ✅；L116 破折號改逗號以過 200 字上限，數字 1.7–3.2／2.3／8.2／2／11 評審重算過，都對 ✅；L117 ✅；L52「對設計很有眼光」✅；L133「首字延遲」✅；L43 改寫成「限 Anthropic API 與訂閱方案，Bedrock 等雲平台的 `sonnet` 指舊版」：對 model-config 別名表（AWS 平台 4.6、Bedrock／Google Cloud／Foundry 4.5），比評審原句更準 ✅ |
| 3 apply.py＋rules_patch | 照做 | haiku-5-5、opus-5-5、model-comparison 的 diff 與設計稿一致；`models/pages.md` 新節、`models/daily.md` 一列 |
| 4 sonnet-5 🔴3＋🟡8 | 照做 | L37、L43、L105、L57、L92 都照貼上稿；歷史 L120 沒動（歷史本來就不改）|
| 5 radar／index／overview | 照做＋額外（接受） | radar L37、L519、L523 ✅；L14、L508、L835 改名 ✅；額外改 L511「是什麼」（補「各方案預設仍是 Opus 5.5」）與 L513「為何熱」（「用 `sonnet` 別名的人不動手就會換到新模型」）：兩句都對得上 model-config ✅；index L48 ✅、L49（sonnet-5 列改「`sonnet` 別名改指」）✅；overview L33、L120 ✅ |
| 6 verified 第六節 | 照做 | commit 2b35d76，四條與評審稿相同 |
| 7 frontmatter 重產 | 照做 | 本頁與 sonnet-5 都是 `pending_count: 0`、`pending_next_review: null` |
| 8 rebuild-count | 照做 | 計數 221、指紋 221，note 是正式 reason 字串 |
| 9 閘 | 照做（評審重跑） | 見第三節；`run_tests.py` 評審沒有重跑 |
| 10 轉知 | 照做＋偏離（接受） | H-cdd17c、H-67d188 → 商業（pricing、pricing-history 屬商業，commercial/daily.md L19、L21）；H-98f7c9 → 功能（claude-code-releases 屬功能，features/daily.md L17）。三筆都用 `--from 主編`：這次查證和回掃是主編做的，`CATEGORIES` 也收「主編」，可以。radar 那筆沒開帳 ✅ |
| 11 log＋ledger | 部分漏做 | log 條目寫明「可改成每次詢問」✅；ledger 總帳列寫了「(3)『可關』更正為『改成每次詢問』」✅。**漏了**「Foundry／雲平台寫法交原考題複驗 Q2 看」那一句（`grep Foundry` 新增行＝0）→ 修法 A |
| 12 單一 commit | 照做 | 19 檔：規則兩檔、沿革、計數、handoff、ledger、log、wiki 12 頁。其中 4 頁（pricing、anthropic-business、anthropic-ipo、code-quality-decline）只改 frontmatter 的 `inbound_links`，是重產帶出來的 |

## 二、主 session 額外改動

- **models/pages.md 拿掉教訓句、沿革改記 `docs/rules-changelog/reporter-models.md`**：符合 CLAUDE.md「規則沿革，只有人讀」的分工，條文本身（「現在誰是預設」的出處限 model-config）還在。接受。
- **radar L511、L513，index L49，overview L33、L120**：都只是改「`sonnet` 別名」說法，沒有新增事實。接受。

## 三、閘（repo 內實跑）

| 閘 | 結果 |
|---|---|
| `check_cell_limits.py` | `OK: 字元上限機械閘 — 無新增超限` |
| `check_reader_language.py` | `OK: 讀者語言閘 — 無新增命中` |
| `check_pending_markers.py` | `狀態：✅ 懸置標記語法檢查通過`（221） |
| `check_rules.py` | `狀態：✅ 全部確定性檢查通過` |
| `check_hierarchy.py` | `狀態：✅ 通過（32 個母頁）` |
| `build_web.py` | exit 0；`斷鏈 WARN 23／錨點 WARN 0`（斷鏈與改前相同）；產物已還原 |

## 四、抽驗對 verified（新頁＋鄰居）

- 新頁 L62（v2.1.280 前 Pro 與 Team Standard 預設 Sonnet 5）、L74（API `high`／Claude Code 與 app `medium`）、L93（`switchModelsOnFlag: false`＝每次問）、L108／L117（第五節＋第六節註腳 ¹、²）、L113（OSWorld 2.1）：都對得上。
- sonnet-5 L57／L92（只限 Pro 與 Team Standard）對 verified 第六節第 3 條 ✅；haiku-5-5 L125「快取讀取 $0.10」對 V5 ✅；model-comparison L76、L85（各方案預設 Opus 5.5）對 verified #1 ✅。
- **殘留一處（🟡）**：model-comparison L158「逐項與**關法**見…」。官方說的是「改成每次問」，不是關掉，和 ledger 已更正的 (3) 衝突 → 修法 B。
- **殘留一處（🟡）**：index L49 sonnet-5 列「曾為預設 Sonnet（v2.1.197 起）」，範圍和已修好的 sonnet-5 L57 不一致（只限 Pro 與 Team Standard）→ 修法 C。
- 歷史段的「API 預設 Sonnet」（sonnet-5 L120、model-comparison L230）照規則不動；claude-code-releases L119、L223 等 H-98f7c9 接手。

## 五、放行

**放行**（0 🔴，3 🟡）。三條 🟡 都不阻擋複驗，建議主編在下一個 commit 一起修：

A. ledger 第 28 波總帳列「轉知 H-cdd17c、H-67d188、H-98f7c9」後面接：
```
；複驗 Q2 加看：callout「Bedrock 等雲平台的 `sonnet` 指舊版」是否讓雲平台讀者讀對（設計者 §9 最不確定的一件事）
```
B. `wiki/topics/model-comparison.md` L158，把 `逐項與關法見` 改成：
```
逐項與處理方式見
```
C. `wiki/index.md` L49，把 `曾為預設 Sonnet（v2.1.197 起）` 改成：
```
曾為 Pro 與 Team Standard 的預設 Sonnet（v2.1.197 起）
```
B、C 改完要跑 `check_cell_limits.py`（index 那一格加 14 字）。

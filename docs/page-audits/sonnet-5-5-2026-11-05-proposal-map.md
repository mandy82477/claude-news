# 第 28 波去向表：entities/sonnet-5-5（2026-11-05）

> 行號指 HEAD `e66cc9d` 原檔（190 行）。新頁全文在 `<scratchpad>/w28/design/out/wiki/entities/sonnet-5-5.md`。逐行保命交給 `check_pending_markers.py` 計數閘（223→221，只少 ⟨Q-01⟩ 與 sonnet-5 同題兩筆）與 `check_cell_limits.py`，這裡不逐行列。

## 一、逐節去向

| 節（原行） | 去向 | 依據 |
|---|---|---|
| frontmatter L1–26 | 留；`status` 同步新狀態欄；`gen_wiki_frontmatter.py` 重產（pending_count 1→0、inbound 30→29） | — |
| 標頭 L27–35 | 留；H1 下補定位句；狀態欄改成「`sonnet` 別名指向它、各方案預設 Opus 5.5」；最後更新 → 11-05；最後新聞更新不動（10-25） | page-templates L42；verified #1 |
| 使命句（新） | 標頭後、callout 前一行 | ledger 1 |
| callout L37–38（10-25 事故） | **改**：三條現況（預設／別名＋effort／換了要調什麼）；事故只留在歷史 L171、L179 | ledger 5 |
| 現況 L44 | 改寫成第 2 段（發布＋定位＋指路），內嵌的「10-10 起 Legacy」補註刪掉（家在 sonnet-5） | ledger 5；verified #9 |
| 現況 L46 | 併入第 2 段（定位一句、Haiku 一個連結） | — |
| 現況 L48 | 併入第 2 段末句 | — |
| 現況 L50「自 10-01 起無新動態」 | **砍** | ledger 5；被 10-25 推翻 |
| 現況（新）第 1 段 | 11-05 查官方：預設 Opus 5.5、`/model sonnet`、資安旗標改跑 Sonnet 5 | verified #1、#4 |
| 對照表 L56 表頭註 | 改「資料截至 2026-11-05」，出處三份 | verified |
| 對照表 L60 現在誰是預設 | 改寫為事實（⟨Q-01⟩ 結案） | ledger 3；verified #1 |
| 對照表 L61 牌價 | 補 5m／1h 快取寫入 | verified #6 |
| 對照表（新列）context 與最大輸出 | 1M／128K（Batch beta 300K），兩代同 | ledger 7；verified #8；Sonnet 5 模型頁 |
| 對照表 L62–63 | 查證日改 11-05，Sonnet 5 一欄改「Legacy，仍可用」 | verified #7 |
| 對照表 L64 會壞什麼 | 改一句數量＋指新節；出處「待補」→ What's new | ledger 2 |
| 對照表 L65 推薦 | 補官方「速度與智慧的最佳組合」 | What's new |
| 對照表 L66 方案 | 改寫為事實（Claude Code 各方案可選、各平台上架） | verified #2 |
| 懸置細節 L69–71 | **砍**（⟨Q-01⟩ 成對移除） | daily-contracts L99 |
| 表下 L75 mixed-news 降回 | 移到新節「換過來還會遇到的事」第 1、5 條（官方 fallback）；原報導留在歷史 L180 | ledger 3；verified #4 |
| 表下 L76 MIXED 5 處 | 移到新節第 5 條佐證；原報導留在歷史 L181 | ledger 2 |
| 表下 L77 牌價不變 | 留在補充第 3 條，改寫（tokenizer 相同、省在哪官方沒說）；「與 Opus 5.5 換代邏輯不同」刪 | 冷讀者 Q1 卡點 |
| 表下 L78–79 快取 | 補充第 4 條一句＋指 pricing；「本庫原記錯」更正史只留歷史 L186 | ledger 8；verified V5 |
| 表下 L80 GDPval 截斷 | **砍**（新基準表已有 1844／1846） | ledger 8 |
| 補充（新）別名看平台、兩個 effort 預設 | 新增兩條 | verified #1、#10；ledger 1「怎麼拿到」 |
| `## 從 Sonnet 5 換過來會壞什麼`（新節） | 官方 5＋1 項＋5 條 | ledger 2；N1 |
| 基準 L86–90 | 重建成 8 列 × 三模型 | ledger 4；N2 |
| 基準 L94 GDPval 截斷 | **砍** | ledger 8 |
| 基準 L95 HN 853 | 移出；HN 分數已在歷史 L183 | ledger 4 |
| 基準 L96 路透 IPO | 移出；已在歷史 L188（改指 anthropic-ipo） | ledger 4 |
| 基準 L97 Reddit | 留（訊號強度改成單一社群回報） | — |
| 基準 L98 跨家 | 留，補「官方表另列 GPT-6 Sol」 | — |
| 基準 L100「所以呢：官方僅公布一項」 | **砍**（不成立）；改成兩條表下（對 Opus 5.5 差距、註腳） | verified #5 |
| 熱度 L104–113 | 改一行指 radar | ledger 6 |
| 跟它怎麼說話 L119 | 留 | — |
| L121 effort | 去掉「預設 `high`」（家在對照表補充），其餘照留，補「較難較長的再升 high」 | What's new |
| L122–123、L125 | 照搬 | — |
| L124 hold findings／display | 留措辭面那半句，`display` 那半句改指新節 | pages.md L129 分工 |
| 表下 L129 fable 對照 | 照搬（區塊名改「補充」，N6） | — |
| 表下 L130 五項指外連 | **砍**（新節取代） | ledger 2 |
| 核心功能 L132–136 | **砍整節**：1M→對照表、v2.1.284→對照表與歷史、設計敏銳→現況 | ledger 7 |
| 相關議題 L140–150 | 留 9 條；改 L142、L143、L145、L149 鉤子；補 haiku-5-5 | 健檢卡 §3 |
| 參考來源 L152–163 | 留全部；補官方 6 份 | verified 來源 |
| 歷史表 L171–175 | 留；L172、L173 補查證結果；L175「成為 API 預設 Sonnet」改「Claude Code v2.1.284 起可選」 | opus-5 歷史條文「結果寫進事件欄」 |
| 歷史細節 L179 | 照搬 | — |
| 歷史細節 L180–181 | 「不採信推算」→（僅標題）；各加一條 11-05 查證子項 | ledger 3；shared「缺項自白」 |
| 歷史細節 L182–183 | L182 去「不採信推算」，L183 照搬 | shared |
| 歷史細節 L184 | 去「並設為 API 預設 Sonnet」 | verified #1 |
| L185 | 改：GDPval 截斷句換成「完整 8 項 11-05 補齊」 | ledger 8 |
| L186 | 10-17 定價文件句併成「Batch 半價、無方案分層，見 pricing」 | — |
| L187、L189 | 照搬 | — |
| L188 | 補 [[topics/anthropic-ipo]] | — |
| L190 | 「不採信推算」→「細節未載」 | shared |

## 二、鄰居（行號指 HEAD）

| 頁 | 行 | 去向 | 依據 |
|---|---|---|---|
| sonnet-5 | L33 | 最後更新 → 11-05 | — |
| sonnet-5 | L48–49 | 🔎 改寫為事實（兩行） | ledger 3 |
| sonnet-5 | L57、L95 | 現在式 → 過去式 | 冷讀者 §撐不起 1 |
| sonnet-5 | L78–82 | 程式區塊：註解改、`claude` 單行刪、ID 改 `claude-sonnet-5` | N5 |
| opus-5-5 | L34、L160 | 最後更新；互指句改指 sonnet-5-5 | ledger 10 |
| model-comparison（N3） | L31、L63、L76、L85、L151–152、L160 | 事實句與指路；兩列移出風險表 | daily-contracts L99 |
| haiku-5-5（N4） | L34、L67、L126、L167 | 刪兩句錯誤事實、改鉤子 | verified V5 |
| pricing、pricing-history、feature-radar | — | 轉知（draft 第四節） | 跨維護者 |

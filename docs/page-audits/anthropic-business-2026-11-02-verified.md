# 主編官方查證 — 第 23 波 topics/anthropic-business（2026-11-02）

查證工具：WebFetch anthropic.com（官方一手）、WebSearch 多家交叉（二手，標明）。**限制**：雲端 session 解析不到 `www.sec.gov`，S-1 原文無法直讀；S-1 數字一律以「多家引 S-1」標二手（第 22 波 verified 同一限制）。行號為 `wiki/topics/anthropic-business.md`（1,048 行）與 `wiki/topics/anthropic-ipo.md`（211 行）2026-11-02 原檔。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 一手／交叉 | 判定 |
|---|---|---|---|
| 1 | business L52 官方估值 $9,650 億（2026-05-28 Series H） | Reuters、Fortune、Law360、Bloomberg（經 Newsquawk）：05-28 宣布 Series H 募 $650 億、post-money $9,650 億，Altimeter／Dragoneer／Greenoaks／Sequoia 領投，含 hyperscaler 既有承諾 $150 億（Amazon $50 億） | 一致 |
| 2 | business L57 淨損 $807 億「2026-10-26 公開版 S-1 確認」，來源等級標「官方一手」 | 多家引 S-1：6 個月淨損 80,748 百萬美元，其中約 724 億是可轉換票據、衍生負債與 SAFE 的公允價值變動（非現金）；營業損失約 6.9 億；調整後營業利益約 16 億 | 數字一致；**等級要降**為「多家引 S-1」（本庫沒人讀過原文）；「這是什麼」欄補「九成是估值上升造成的非現金會計損失」 |
| 3 | business L56「獲利：連續第二季獲利（2026-09-13）」與 L57「淨損」並列 | S-1（多家引）：上半年**營業層仍虧損約 6.9 億**，**調整後**營業利益（排除股權報酬、非現金捐贈、和解費用）約 16 億 | 「連續獲利」只在調整後口徑成立；列內要寫明口徑，否則讀者以為 S-1 證實了獲利 |
| 4 | business L42「Q3 營收 168 億（2026-10-15）」vs L55 表「（2026-10-14）」 | 二手（Bloomberg、FT 等）；S-1 只到 06-30，Q3 未見一手 | 同頁日期不一；S-1 上半年營收約 162.9 億可補一列「S-1 上半年營收」（多家引 S-1） |
| 5 | business L297 SpaceX「官方 05-06 公告載 Colossus 1 全部容量，逾 300MW、22 萬顆 GPU」 | anthropic.com/news/higher-limits-spacex（2026-05-06）：「more than 300 megawatts of new capacity (over 220,000 NVIDIA GPUs) within the month」；官方頁**沒有**金額 | 一致；「每月 $12.5 億」維持媒體＋發言人口徑 |
| 6 | business L293–294 Nscale 第一筆 $450 億、第二筆約 $450 億；market-signals-compute L135「第一筆（Nscale 總合約 1,030 億美元，Anthropic 與 Microsoft 並列最大客戶）」 | 未見一手；1,030 億是 Nscale 全部客戶的總合約，450 億是 Anthropic 那一筆（推論，依兩頁上下文） | 兩頁口徑不同但不矛盾：要在 business 那列加一句「Nscale 總合約 1,030 億含 Microsoft 等客戶，Anthropic 這筆 450 億」，觀點頁照指 |
| 7 | business L53「IPO 估值預期約 $1.5 兆（10-16，較 $2 兆下修）」 | Telegraph／Reuters 引投資人；S-1 不含估值（多家分析） | 維持「一級媒體引投資人」 |
| 8 | anthropic-ipo L48「公開版 S-1 已於 10-26 提交」vs L61「需持續觀察是否有官方 S-1 遞交」、L49 上市時程「延至 10 月中」 | anthropic.com/news「Anthropic files S-1 with the SEC for proposed initial public offering」（2026-10-26）；股數、價格區間未定，filing 未生效；掛牌日官方未公布 | L61 結論與 L49 過期，要改；L49 ⟨Q-03⟩ 懸置可結：官方 10-26 公告未給日期，答案是「仍未公布」 |
| 9 | anthropic-ipo L50「10-20 S-1 首度揭露 H1 淨損 807 億（WSJ）」 | 10-20 是 WSJ 引外流草稿；10-26 公開版多家引為 80,748 百萬 | 「S-1 首度揭露」改「外流草稿首度揭露、10-26 公開版多家引同數字」 |

## 二、考題的官方錨句

- **Q1 營收多少、誰說的**：唯一官方文件是 S-1（上半年營收約 162.9 億、年增約 13 倍，多家引）；ARR 650 億、Q3 168 億都是媒體引公司。
- **Q2 合作改到我**：官方一手可證的只有 SpaceX Colossus 1（05-06，300MW＋、22 萬 GPU、提高額度）與 GSA 40% 折扣（10-27）；其餘多為媒體。
- **Q3 風險**：S-1 營業層仍虧損、九成淨損非現金；客戶集中、雲端承諾見 S-1（多家引）。
- **Q4 Google／Amazon／Microsoft**：Amazon 為 Series H 出資者之一（$50 億，多家）；Microsoft 有 $300 億 Azure 容量合作（官方 05-06 頁順帶提及）。

## 三、給設計者三句

1. 「現在的數字」表：淨損列降級為「多家引 S-1」並補非現金一句；獲利列寫明「調整後口徑」；統一 Q3 日期；可補「S-1 上半年營收」一列。
2. anthropic-ipo L49、L50、L61 三處過期或寫錯，本波一起改（同維護者子頁），⟨Q-03⟩ 結案。
3. Nscale 1,030 億 vs 450 億是「總合約 vs Anthropic 那一筆」，事實住 business 算力表一句講清楚，market-signals-compute 只指過來。

來源（二手）：[Fortune](https://fortune.com/2026/05/28/anthropic-series-h-valuation-ipo-unicorn/)、[Law360](https://law360.com/articles/2483295)、[Built In](https://builtin.com/articles/anthropic-raises-65b-series-h-965b-valuation-20260601)、[Luminix](https://www.useluminix.com/reports/company-overviews/anthropic-s1-what-the-filing-shows)；一手：[anthropic.com/news/higher-limits-spacex](https://www.anthropic.com/news/higher-limits-spacex)、anthropic.com/news（S-1 公告 10-26）。

# 主編官方查證 — 第 22 波 topics/market-signals（2026-11-02）

查證工具：WebFetch anthropic.com/news（官方一手索引）、WebSearch 多家交叉（二手，標明）。**限制**：雲端 session 解析不到 `www.sec.gov`（不在允許網域），S-1 原文無法直讀；S-1 數字一律以「多家引 S-1」標二手，等本機或放行網域後再補一手。行號為 `wiki/topics/market-signals.md` 2026-11-02 原檔（1,699 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 一手／交叉 | 判定 |
|---|---|---|---|
| 1 | L285 S-1 10-26 提交、Nasdaq「ANT」 | anthropic.com/news 列「Anthropic files S-1 with the SEC for proposed initial public offering」（2026-10-26）；多家報導 Class A、Nasdaq Global Select、22 家承銷（Goldman、Morgan Stanley 列首）、股數與價格區間未定、filing 未生效；controlled company、Class F 持 50.1% 表決權 | 一致；「掛牌時點」官方未公布（「最快 11 月中」僅單一媒體） |
| 2 | L402 WSJ「上半年淨損 807 億」判 📉 負面 | 多家引 S-1：6 個月淨損 80,748 百萬美元，其中約 724 億是可轉換票據、衍生負債與 SAFE 的公允價值變動（非現金，隨估值上升而增）；營業損失約 6.9 億（前一年約 21 億）；調整後營業利益約 16 億；SBC 22 億 | **判讀要補一句**：L402 判負面以「虧損規模」為主，但 9 成是估值上升造成的非現金會計損失；L1569 已寫「多為非現金」，同頁兩處口徑不一。不改方向（由記者判），但「為什麼這樣判」缺這個事實 |
| 3 | L315「年化成長 14 倍」 | 多家：上半年營收約 162.9 億美元，較去年同期 12 億增約 13 倍（1,300%） | 「14 倍」與「1,300%（≈14 倍）」是同一數字兩種說法，一致；L1569「約 163 億」一致 |
| 4 | L596「Q3 營收 168 億、季增 46%」（10-15，向投資人揭露） | S-1 只到 06-30；Q3 未見一手 | 維持二手；標題「為 IPO 前最後一次財務揭露」是媒體說法 |
| 5 | L181 GSA OneGov 擴大，日期 10-28 | anthropic.com/news「Expanding our partnership with GSA to bring Claude to all levels of government」**2026-10-27**；原文「a 40% discount on Claude Enterprise, Claude for Government, and the Claude API」；官方頁不用「OneGov」一詞 | **日期差一天**（10-27）；「OneGov」是媒體用語，標題可留但不得寫成官方名 |
| 6 | L447 Public Benefit Fund「捐出 5% 股權…每漲 50% 可加碼 2%」 | 官方頁（anthropic.com/news「Investing in the public benefit」10-18，本次直連 404）；多家：5% 待股東會核准、基準估值未公開、「每 50% 加 2%」部分媒體寫「董事會裁量」；基金為 Anthropic 全資的獨立法人；治理與門檻「未來幾個月公布」 | 大致一致；「捐出」不精確——是**撥入 Anthropic 全資子實體**，不是捐給外部；「待股東會表決」頁面已寫 |
| 7 | 摘要 L50「只有會進 S-1……才寫上來」 | S-1 已公開 | 使命句的時態要改：S-1 已不是「上市前唯一揭露」的未來式，而是已公開文件；之後的六類門檻應改以「會改 S-1 修正版／首份 10-Q 數字」 |

## 二、考題的官方錨句

- **Q1 IPO 走到哪**：10-26 公開 S-1（官方），未生效、價格區間未定；掛牌日官方未公布。估值預期（1.5 兆、2 兆）全是媒體轉述投資人，S-1 不含估值。
- **Q2 S-1 的壞消息**：上半年淨損 807 億但 9 成非現金；營業層虧損 6.9 億且在收斂；風險因素（生物武器、勒索、訓練暫停、資安事件）為媒體引 S-1，本次無法讀原文。
- **Q3 算力錢**：S-1 揭露的雲端承諾（Google、AWS、Broadcom、SpaceX）頁面 L300 已有，數字未能一手核；630 億 Broadcom 融資、Nscale 信用支持皆媒體。
- **Q4 買得到的標的**：本體未掛牌不可買；表上 17 檔都是間接曝險，頁面「持股佔市值極小」的說法對 Alphabet／Amazon 成立（推論，依兩家財報規模）。

## 三、給設計者三句

1. 拆頁後母頁的「現在」要以 S-1 已公開為起點改寫摘要的時態（#7），IPO 子頁的第一句結論是「S-1 已公開、未生效、價格與日期未定」。
2. 807 億判讀補「約 724 億為非現金公允價值變動」一句，口徑與 L1569 統一；GSA 改 10-27、「OneGov」標為媒體用語。
3. SEC 網域雲端不可達：S-1 數字維持「多家引 S-1」標記，不得寫成官方一手；本機 session 可補（`docs/workaround-register.md` 不需登記——非功能依賴）。

來源（二手）：[Shacknews](https://www.shacknews.com/article/151141/anthropic-claude-stock-ipo)、[FourWeekMBA](https://fourweekmba.com/ai-anthropics-s-1-shows-16-3b-half-year-revenue-up-14x/)、[Luminix](https://www.useluminix.com/reports/company-overviews/anthropic-s1-what-the-filing-shows)、[Al Jazeera](https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund)、[The Next Web](https://thenextweb.com/news/anthropic-public-benefit-fund-5-percent-shares)。

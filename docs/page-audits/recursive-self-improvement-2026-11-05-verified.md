# 主編官方查證 — 第 26 波 topics/recursive-self-improvement（2026-11-05）

查證工具：WebFetch anthropic.com（官方一手）、WebSearch 多家交叉（二手，標明）。行號為 `wiki/topics/recursive-self-improvement.md` 2026-11-05 原檔（527 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 一手／交叉 | 判定 |
|---|---|---|---|
| 1 | 量化指標表「R&D Automation Index：主導比例／完全無人監督比例 26%／0%」來源寫「dev.to（社群分析，非官方一手）…未經官方一手證實」 | **官方一手** anthropic.com/institute/measuring-pace-of-ai-development（as of August 2026）：「Claude now leads 26% of Anthropic's model R&D tasks, up from under 1% in February 2026」；「Claude is not operating fully autonomously for any measured subset of AI R&D work」 | **錯**：是官方一手，來源欄與判語要改；補「2026-02 低於 1%」這個官方起點 |
| 2 | 量化指標表「同時工作中的 agent 數量約 3 萬個」來源寫「Reddit 週熱門（轉引 dev.to）…官方原始出處未見」 | 同一官方頁：「approximately 30,000 agents doing research and engineering work at Anthropic at any one time」（限其最常用的內部平台） | **錯**：官方一手；補「僅最常用的內部平台」限定 |
| 3 | 量化指標表「Claude 負責內部下一代模型開發工作量約四分之一（25%）」09-18，Reuters／官方部落格 | Reuters 09-17 報導「Claude leads 26%」；官方頁同上 | 與 #1 是**同一個官方數字**（26%），不是「第三種指標」；兩列應併為一列，日期以官方頁發布（09-17，二手；官方頁只標「as of August 2026」）為準 |
| 4 | 摘要「工程師代碼產出提升 8×」、「Claude 佔 Anthropic 程式碼比例 80–90%」（06-04《When AI Builds Itself》） | 多家引該報告：8× 是「每季交付程式碼量」對 2021–2025；AI 撰寫比例「80% 至逾 90%，視是否計入腳本」；報告明說完整 RSI「尚未達到、非必然」，並描述三種情境（停滯／AI 自動化開發但人保有控制＝最可能／完整 RSI） | 數字一致（二手）；摘要沒寫「尚未達到」這個官方定性——冷讀者 Q1「快到了還是已發生」的官方答案就是它 |
| 5 | 「目前結論」L91 附近「2026-10-16，Anthropic Blog：METR 團隊獲員工級系統存取權，SecureBio 加入」 | anthropic.com/news 索引：「An update on independent evaluators」**2026-10-15** | 日期差一天 |
| 6 | 「目前結論」「2026-09-19，Anthropic 指定 Accenture 為首位『內嵌評估者』，承諾 10 億美元」 | anthropic.com/news「Partnering with Accenture on embedded evaluation」**2026-09-18**：雙方**各**預期 ≥$10 億／五年，Anthropic 直接出資 Accenture 的工作 | 日期差一天；「承諾 10 億美元」主詞不清（是雙方各自） |
| 7 | callout／「目前結論」末條：11-03 修訂版 S-1/A「可能迫近」內部 RSI 門檻 | 雲端解析不到 www.sec.gov；多家引 S-1/A（epyhia、Yahoo Finance、Gizmodo） | 維持「多家引 S-1/A」二手；家在本頁或 anthropic-ipo 交健檢卡判 |

## 二、考題的官方錨句

- **Q1 官方說了什麼、快到了還是已發生**：官方 06-04 報告：AI 已在加速自身開發，但完整 RSI「尚未達到、非必然」；官方 09 月量測頁：Claude 主導 26% 的模型研發任務（2 月 <1%）、**沒有任何一類研發工作是完全自主**。最新說法是 11-02～03 修訂版 S-1/A「可能迫近內部門檻、現役模型皆未跨過」（二手）。
- **Q2 可量的指標**：官方一手三個——26% 主導比例、0 完全自主、約 3 萬個同時運作的 agent（限最常用內部平台）；8× 與 80–90% 來自 06-04 報告（二手引述）。
- **Q3 跟做 agent 的人的關係**：官方量測頁提出三類量測（AI 做了多少研發、agent 動作監督得多好、算力怎麼分配），呼籲各前沿實驗室公布同樣指標——讀者能做的是拿這三類量測檢查自己的 agent 系統（推論，非官方建議）。

## 三、給設計者三句

1. 量化指標表：26%／0%／3 萬三列改為**官方一手**並附官方頁連結，09-18「四分之一」與 26% 併為一列；這是本頁最大的錯。
2. 摘要第一段補官方定性「AI 已在加速自身開發，完整 RSI 尚未達到」，回答 Q1。
3. 「目前結論」其實是 30 則帶日期的事件流，不是結論；METR 10-15、Accenture 09-18 兩個日期改正。

來源：一手 [anthropic.com/institute/measuring-pace-of-ai-development](https://www.anthropic.com/institute/measuring-pace-of-ai-development)、anthropic.com/news 索引（10-15、09-18）；二手 [SiliconANGLE](https://siliconangle.com/2026/09/17/anthropic-details-practical-metrics-to-help-monitor-the-speed-of-ai-development/)、[Inven Global](https://www.invenglobal.com/articles/22500/ai-has-begun-to-make-itself-smarter-anthropics-warning)。

## 四、補查（健檢卡 V2，2026-11-05）

- 官方 anthropic.com/news/an-update-on-independent-evaluators（**2026-10-15**）：「Last month, we committed to stronger independent, third-party assessment of our models and safety practices.」「We also signed the White House Accord on Super Intelligence.」——簽署企業同意與獨立外部稽核／評估者合作；**原文未提暫停或減速承諾**。同文列 METR（員工級存取、會公布風險評估）、SecureBio（審 08 月 Risk Report 化生武器章）、Accenture（與 Faculty，評估、紅隊、防護測試）、Hugging Face（僅早期洽談）。
- 判定：協議正式名稱是「White House Accord on Super Intelligence」、簽於 09 月（官方「last month」）；本頁「尚無任何機構正式同意協調暫停」仍成立——協議是第三方評估，不是暫停。

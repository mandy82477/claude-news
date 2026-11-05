# 主編官方查證 — 第 27 波 entities/dario-amodei（2026-11-05）

查證工具：WebFetch anthropic.com（官方一手）、WebSearch 多家交叉（二手，標明）。行號為 `wiki/entities/dario-amodei.md` 2026-11-05 原檔（213 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 一手／交叉 | 判定 |
|---|---|---|---|
| 1 | 核心論述表「2026-07-28 部落格聲明『Our position on open-weights models』：澄清從未主張禁止開源權重模型，呼籲加強對中國晶片出口管制」 | anthropic.com/news/position-open-weights-models：**2026-07-27**，署名 Dario Amodei；原文「Anthropic has never advocated for a ban on open-weights models.」支持三項：限制強力晶片與製程設備出口中國並打擊走私；打擊工業規模蒸餾；**所有夠強的模型（開源與閉源）強制安全測試** | 日期差一天（07-27）；頁面只寫了第一項，漏掉蒸餾與「開閉源都要強制安全測試」——後者正是被誤讀成「禁開源」的那條 |
| 2 | 核心論述表兩列「2026-09-13 公開撰文呼籲全球暫緩…6–12 個月」「2026-09-13 稱中國是最棘手兩難」；細節區「2026-09-13 暫緩呼籲」 | 多家（AP 系 ClickOnDetroit／News4Jax 2026-09-12、ITV 2026-09-12、VentureBeat、Newsweek）：**2026-09-12** 發表文章〈We Must Pace the Frontier〉；6–12 個月是「可能變得可行」的警告，不是已發生；承諾自家先做三步驟計畫第一步；Musk「Dario is right」、Altman 稱 OpenAI 會承諾其中一項提案 | 日期 09-12（第 26 波 RSI 頁已用 09-12，兩頁對不上即此）；文章標題本頁沒寫；「Musk、Altman 相繼表態支持」與一手轉述一致 |
| 3 | 公開批評者對照「Michael Burry 09-14（HN 09-17 轉載）」 | RSI 頁第 26 波結論層寫「Burry 稱『自利』，09-17 報導」 | 兩頁口徑不同但都說得通（發言 09-14、報導 09-17）；分工交健檢卡判，一頁寫發言日、一頁寫報導日會讓讀者以為是兩件事 |
| 4 | 現況與表「去年薪酬 1,800 萬美元」（Reuters 10-06 獨家）、「人身安全支出 275 萬美元」（Fortune 10-29） | 本次未查（非官方可證；S-1 薪酬揭露雲端讀不到 SEC） | 維持二手；若 S-1 有高管薪酬表，本機可補一手 |

## 二、考題的官方錨句

- **Q1 最近說了什麼**：一手可證的最近一篇署名文章是 07-27〈Our position on open-weights models〉；09-12〈We Must Pace the Frontier〉多家引述（本次未讀到原文頁）。之後 10 月的條目全是 Fortune／Reuters 二手（IPO、薪酬、安保）。
- **Q2 預測準不準**：本頁沒有「預測 vs 結果」的對照；「AI 寫 90% 程式碼」類說法的量測現況住 `topics/recursive-self-improvement` 量化表（官方 26% 主導、>90% 程式碼占比為 S-1 媒體轉述）。
- **Q4 立場怎麼改到產品**：一手可證的只有 07-27 文章的三項政策主張與 05-12 Code with Claude 速率翻倍（官方 05-06 SpaceX 頁提及提高額度）。

## 三、給設計者三句

1. 日期兩處改正：open-weights 07-27、減速文章 09-12（並寫出標題〈We Must Pace the Frontier〉），與 RSI 頁對齊。
2. open-weights 那列補完整三項主張，尤其「開源閉源都要強制安全測試」。
3. 批評者的日期統一用「發言日」並在 RSI 頁那邊同樣寫發言日（同維護者？若跨維護者走轉知）。

來源：一手 [anthropic.com/news/position-open-weights-models](https://www.anthropic.com/news/position-open-weights-models)；二手 [VentureBeat](https://venturebeat.com/ai/anthropic-ceo-says-ai-swarm-could-take-over-the-entire-internet-in-6-12-months-commits-to-ai-slowdown-plan)、[ClickOnDetroit／AP](https://www.clickondetroit.com/business/2026/09/12/anthropic-ceo-dario-amodei-says-ai-industry-needs-to-slow-down-for-safety/)、[ITV](https://www.itv.com/news/2026-09-12/musk-and-chatgpt-ceo-back-calls-to-slow-down-development-of-ai)。

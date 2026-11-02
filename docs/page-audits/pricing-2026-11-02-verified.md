# 主編官方查證 — 第 24 波 entities/pricing（2026-11-02）

查證工具：WebFetch 官方一手 `platform.claude.com/docs/en/about-claude/pricing`（API 定價）、`claude.com/pricing`（訂閱方案）。行號為 `wiki/entities/pricing.md` 2026-11-02 原檔（969 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 官方一手（2026-11-02） | 判定 |
|---|---|---|---|
| 1 | L57「我的方案現在有什麼」**資料截至 2026-08-22**；L64 「Max 20x $200」 | claude.com/pricing：$200 那一檔官方名稱是 **Ultra**（「10x Pro usage」）；Max 是「5x Pro usage」$100 | **過期**：方案名與倍數都變了；頁面「Max 5x／Max 20x」兩列要改為 Max（5x）／Ultra（10x） |
| 2 | L59–67 方案表「可領優惠」欄：Max／Team 皆「—」 | Max：「**$100 a month in API credits** to build on the Claude Platform」；Ultra：「**$200 a month in API credits**, up from $100 on Max」；Team：「**Up to $500 per month in pooled API credits**」；Pro、Free 無月度 API credits | **漏列**：訂閱附的月度 API 額度是讀者 Q2 的答案，全表沒有；market-signals 10-08 判讀記過「$200 與 $500 兩版本口徑不一」——官方現值是 Max $100／Ultra $200／Team 最多 $500 共用 |
| 3 | L66 Enterprise「未公開報價」 | 「$20/seat/mo billed annually, 20-seat minimum, plus usage at API rates」 | **過期**：Enterprise 已公開席位價＋用量按 API 費率 |
| 4 | L65 Team standard「$20（年繳）／$25（月繳）」；L60 Pro「$20（年繳 $17／月）」 | Team Standard $20 年繳／$25 月繳；Pro $17 年繳（$200 預付）／$20 月繳 | 一致 |
| 5 | L130–140 API 定價表：沒有 Haiku 5.5 列；L140 Haiku 4.5「**陣容中最低價**」 | 官方表：Haiku 5.5 **$0.10／$0.50**（prompt ≤100K）、$0.50／$2.50（>100K），快取命中 $0.01／$0.05；Haiku 4.5 $1／$5 | **錯**：最低價是 Haiku 5.5；Haiku 5.5 只住「還沒確定的計費變動」L169（已查證卻留在「還沒確定」表），應進主表 |
| 6 | L132 Opus 5.5 $4／$20、快取讀取 $0.20、Batch 5 折 | 一致（Batch $2／$10）；5m 快取寫入 $5、1h $8 | 一致 |
| 7 | L133 Sonnet 5.5 $2／$10、快取 $0.10、Batch $1／$5 | 一致 | 一致 |
| 8 | L134 Sonnet 5 $2／$10 | 一致；快取命中 $0.20（Sonnet 5.5 是 $0.10） | 一致 |
| 9 | L135 Fable 5.1 $10／$50、快取 ×0.025 | 快取命中 $0.25（＝×0.025）；Fable 5 快取命中 $1（×0.1） | 一致 |
| 10 | L252 資料落地 ×1.1 全類別；L256 Fast mode Opus 5.5 $8／$40、Opus 5／4.8 $10／$50；L262 Opus 4.8 fast mode 10-30 宣告淘汰、11-30 移除 | 官方：`inference_geo:"us"` 1.1x 套用所有 token 類別；Fast mode Opus 5.5 $8／$40、Opus 5／4.8 $10／$50；Opus 4.8 fast mode 移除同 CLI 2.1.316 changelog | 一致 |
| 11 | L196 Managed Agents session runtime | 官方「$0.08 USD per session-hour」、`running` 狀態計時；無 batch 模式 | 一致（頁面寫毫秒計量，官方以 session-hour 標價、`running` 才計） |

## 二、考題的官方錨句

- **Q2 方案內含什麼**：Pro $20 無月度 API 額度；Max $100 附 $100／月 API credits；Ultra $200 附 $200／月；Team 最多 $500／月共用；Enterprise $20／席年繳、20 席起、用量按 API 費率。
- **Q3 Opus 5.5 一百萬 token**：$4 輸入／$20 輸出；快取命中 $0.20；Batch 半價 $2／$10；US 資料落地 ×1.1；Bedrock 等區域端點較 global 加 10%（官方「Regional and multi-region endpoints include a 10 percent premium over global endpoints」）。
- **Q4 最近改了什麼**：Opus 4.8 fast mode 11-30 移除（不 fallback）；方案改名 Ultra 與月度 API credits（本頁未載）。

## 三、給設計者三句

1. 方案表整表重判（資料截至 08-22 已逾 70 天）：改 Max／Ultra 名稱、加「月度 API 額度」欄或列、Enterprise 公開價；「資料截至」改 2026-11-02 並附 claude.com/pricing 連結。
2. API 主表補 Haiku 5.5 兩檔、拿掉 Haiku 4.5「陣容中最低價」；「還沒確定的計費變動」裡已查證的 Haiku 5.5 列移出。
3. 這兩項都屬母頁「我現在怎麼被計費」結論層，不隨拆頁下沉。

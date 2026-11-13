---
page: "entities/pricing-incidents"
kind: "entity"
type: "policy"
status: "active（持續調整中）"
domain: "💼 商業"
last_updated: "2026-11-09"
last_news_update: "2026-11-09"
status_main: "active"
days_since_news: 4
parent: "entities/pricing"
children: "[]"
page_role: "child"
days_since_news_subtree: 4
inbound_links: 15
attribution_count: 4
attribution_last: "2026-11-09"
top_source: "google-news"
pending_count: 3
pending_overdue: 1
pending_next_review: "2026-11-24"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 計費事故：誤扣、額度異常與帳號停用

帳單出錯、額度掉得快、付了錢卻用不了——官方認了沒、現在還在不在，以及你能先做什麼；現在怎麼計費在 [[entities/pricing]]，逐條 issue 的留言數在 [[entities/claude-code-known-issues]]。

**類型：** policy
**狀態：** active（持續調整中）
**領域：** 💼 商業
**上層：** [[entities/pricing]]
**首次出現：** 2026-04-25
**最後更新：** 2026-11-09
**最後新聞更新：** 2026-11-09

> **最新動態**（2026-11-09）
> - Reuters／shattered.io 跟進確認：Anthropic 須就 Claude Max 訂閱廣告「5 倍、20 倍」用量宣稱面對訴訟程序，與 11-07 Courthouse News 報導同一裁定，詳見 [[entities/pricing-incidents#還在發生的事故]] 「Max 20x 實際用量與廣告宣稱落差」列。

---

## 還在發生的事故

**一事故一列，只收 🔴、⛔、⚖️ 三種狀態；轉 ✅／⏸ 即移出表，條目留在下方。最多 8 列：官方拒修或官方已承認的在最上，其次司法中，再來其餘未解；同一層最後動態新的在上。** 狀態五值定義（供讀者對號）：🔴 未解＝官方未公開回應、也未載明修復版本；✅ 已修＝官方確認或載明修復版本；⛔ 官方拒修＝官方已明確表態不修；⚖️ 司法中＝已進入訴訟程序；⏸ 無後續＝距最後動態逾 90 天且無新回報。

%% 維運備忘：上限、排序、「單一社群回報型」定義與移出判準見 `.claude/reporter-rules/commercial/pages.md`「pricing 事件流的上限與退場」。表只寫 issue 號，互動數的家是 entities/claude-code-known-issues。 %%

| 事故 | 狀態 | 最後動態 | 你該做的事 |
|------|------|---------|-----------|
| Anthropic Status 通報：credit purchase 入帳延遲，部分請求因餘額不足失敗 | 🔴 未解 | 2026-10-01，官方 Investigating，修復時間未載 | 失敗請求稍後重試；充值後先核對餘額再跑長任務 |
| infostealer 竊 session cookie，免密碼抽乾訂閱額度 | 🔴 未解 | 2026-09-09，官方 08-30 通知已強制登出、撤銷 token、退誤扣款 | 額度莫名見底先查有無不明登入；攻擊面見 [[topics/ai-agent-safety]] |
| 7 月帳務錯誤：南韓免費用戶收到 $16.6M 無效帳單；審計稱企業多收 $1.7M | 🔴 未解 | 2026-07-20 | 核對 7 月帳單有無異常扣款；補救方式見下方細節 |
| HERMES.md 字串觸發靜默切 API 計費 | ⛔ 官方拒修 | 2026-04-25，官方確認為 bug 但拒絕退款 | commit 訊息避開該大寫字串；已被扣費者官方不退 |
| Max 20x 實際用量與廣告宣稱落差 | ⚖️ 司法中 | 2026-11-09，Reuters／shattered.io 跟進確認 11-07 裁定（須面對訴訟程序）；另見 Issue #79773（10-21） | 依現況估算用量，不要以「20 倍」為預算基準 |
| Max 5x 續訂扣款後帳號遭停用 | 🔴 未解 | 2026-11-02，Issue #5088，官方仍無回應；同模式另見 #80872、#64480、#90531 | 續訂前保留付款證明；遭停用時留扣款紀錄向客服與發卡行申訴 |
| Max 5x 升 Max 20x 付款持續失敗、客服未回應 | 🔴 未解 | 2026-10-24，Issue #56281，延續 #55266、#55982 | 升級前備妥備援付款方式、留錯誤截圖；別反覆重試 |
| Fable 成 Max 標準模型起被誤判要先買 usage credits | 🔴 未解 | 2026-10-24，Issue #79337，07-20 起未修 | 對照 `Settings > Usage` 與帳單，於該 issue 回報佐證 |

**還在發生、沒進上表的**（同一排序，新的在前）：#16157 Max 幾乎一開工就撞上用量上限（09-17）、#38335 Max session 額度加速耗盡（09-16）；只有單一社群來源的：#62466 圖片處理失敗仍扣用量（11-02）、Reddit 用量暴增 8 倍（10-27）、Console 小數點多扣 100 倍（10-16）、成本顯示把 Haiku 5.5 算成 Opus 價（10-11）、#8327 設 API key 後組織遭停用（10-02）、#37394 Max 觸頂過快（09-21）、Reddit Max 20x 半小時 0%→100%（08-04）、Reddit Max 升級誤購 credits（07-02）。每件見下方「事故與爭議」同日條目。

表只寫 issue 號；留言數與讚數以 [[entities/claude-code-known-issues]] 為準，下方各條目裡的數字是當日快照。

**懸置細節**
- **$16.6M 帳務錯誤補救（2026-10-24 查證，媒體稱）**：南韓免費方案用戶 2026-07-07／08 收到約 $1.67M 與 $16.6M 兩張無效請求，未登記付款方式、無 API 用量。
  - Anthropic 告知該用戶是自動儲值（auto-reload）設定錯誤所致，已關閉設定並還原帳務設定；金流端扣款被拒，確認無需付款（Startup Fortune、BeInCrypto，2026-07-13）。
  - $16.6M 為何由該設定產生，Anthropic 未公開解釋；官方頁面未載此事，故無退款問題，只剩成因未明。
  - 另一件獨立事件：審計公司 Vaudit 稱檢視 60 家公司 $34M 帳單，發現約 $1.7M 多收，多家業者合計退還約八成（The Information 報導，非 Anthropic 單家數字）；Anthropic 發言人稱不對未完成請求收費、未暗中改派舊模型、未見普遍問題。兩件不可併讀。

**已結案三件（供對照）**：共用池機制（2026-08-22 官方確認）、Opus 5 定價兩說收斂（2026-08-08）、Sonnet 5 $2/$10 永久化（2026-08-10）。下方「事故與爭議」每則事故標題前的符號就是它的狀態。

---

## 事故與爭議（誤扣費、靜默計費改動、帳號安全）

#### ⚖️ 2026-11-07：法院裁定 Anthropic 須就 Claude Max 訂閱廣告是否誤導使用者的指控面對訴訟程序

- **Courthouse News（2026-11-07）**：報導稱 Anthropic 須就 Claude Max 訂閱廣告是否誤導使用者的相關指控進一步面對訴訟程序；報導未附具體案號或法官裁定全文，是否即 2026-06-16 集體訴訟（指控 Max 5x／Max 20x 實際限制遠低於廣告宣稱，見上方「還在發生的事故」⚖️ 列）未見確認，議題高度重疊（推論）。
- **同事件另一報導（The Next Web，2026-11-07，非新事實）**：同日報導「Anthropic must face Claude Max ad claims, report says」，僅標題可用，未見新增案情細節。
- **11-09 跟進（Reuters／shattered.io，非新事實）**：兩家同日報導同一裁定，Reuters 稱須就廣告「5 倍、20 倍」用量宣稱是否誤導消費者進一步面對訴訟；shattered.io 標題確認「5x, 20x Claims Proceed」。
- 均未附新增案號或裁定全文，與 11-07 Courthouse News 報導為同一事件的媒體擴散（Google News/Reuters；Google News/shattered.io）。
- **你能先做什麼**：維持既有建議——依現況估算用量，不要以廣告「20 倍」為預算基準；詳見上方「還在發生的事故」表。

#### 🔴 2026-11-02：新 GitHub Issue #62466——圖片處理失敗重複發生，仍持續扣用量

- **GitHub Issue #62466（36 則留言，2026-11-02）**：使用者回報 Claude Code 的「Image couldn't be processed」API 錯誤會重複發生，且每次失敗仍計入用量上限而非不計費；官方尚無回應（[GitHub #62466](https://github.com/anthropics/claude-code/issues/62466)）。
- **你能先做什麼**：圖片類請求失敗後，先查 `Settings > Usage` 確認是否被計費；頻繁失敗時減少圖片輸入或改以文字描述替代，直到官方修復。

#### 🔴 2026-10-27：Reddit 單一貼文回報當日用量暴增 8 倍，並稱服務端錯誤也扣付費額度、不補償（未見 Anthropic 說法）

- **[r/ClaudeAI · 週熱門](https://www.reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic/)**：使用者稱當日 Claude Code 用量暴增 8 倍，稱 Anthropic 已證實服務端錯誤一樣會消耗付費額度、不予補償；僅有標題與圖片，無官方公告連結佐證（10-27 20:34 UTC）。

#### 🔴 2026-10-24：GitHub Issue #79337 累積 77 留言——Fable 5 成 Max 標準模型當天起誤判扣點，逾三個月未修復

- **GitHub Issue #79337（77 則留言、26 👍，2026-10-24）**：自 2026-07-20 Fable 5 成為 Max 方案標準模型當天起，Claude Code 即持續誤判需額外購買 usage credits；延續 08-07 已記錄之 67 留言，互動量為今日官方 repo 單一 issue 最高（[GitHub #79337](https://github.com/anthropics/claude-code/issues/79337)）。
- **你能先做什麼**：Max 方案用戶若曾被要求額外購買 usage credits，可對照 `Settings > Usage` 與帳單，並於此 issue 回報佐證。

#### 🔴 2026-10-24：新 GitHub Issue #56281——Max 5x → Max 20x 升級付款持續失敗、客服未回應

- **GitHub Issue #56281（39 則留言，2026-10-24）**：使用者回報將 Max 5x 升級至 Max 20x 時，每次嘗試付款皆失敗、客服未回應；延續 08-02 已記錄之 Issue #55266（同類「升級操作本身無法完成」症狀，當時指出與 #10832、#50710、#43118 同源），顯示該類升級故障持續逾兩個半月未解（[GitHub #56281](https://github.com/anthropics/claude-code/issues/56281)）。
- **你能先做什麼**：升級前備妥多張付款方式備援，失敗後保留錯誤訊息截圖以加速客服申訴；官方尚無回應，避免反覆重試造成多次扣款嘗試。

#### ⚖️ 2026-10-21：新 GitHub Issue #79773——7 月已升級 Max 20x 用戶回報週用量仍按 Max 5x 甚至更低速率消耗

- **GitHub Issue #79773（31 則留言，2026-10-21）**：一名 7 月已升級 Max 20x 的用戶回報，其週用量額度仍按 Max 5x（甚至更低）速率消耗，而非應有額度；呼應既有 Max 20x 集體訴訟「實際僅 Pro 6–8 倍」的落差指控（[GitHub #79773](https://github.com/anthropics/claude-code/issues/79773)）。
- **你能先做什麼**：已升級 Max 20x 的用戶可對照自己 `Settings > Usage` 的消耗速率是否接近舊方案水準，並留意官方後續回應。

#### 🔴 2026-10-16：Hacker News 回報 Console 儲值小數點輸入 bug，$5.04 被當成 $504 刷卡扣款 100 倍

- **Hacker News（87 分，2026-10-16）**：一名在哥斯大黎加帶領開發團隊的律師事務所使用者回報，於 Anthropic Console 儲值時輸入「5.04」，因所在地區小數點輸入習慣與系統預期不同，小數點遭整段吃掉，實際刷卡金額為 **$504** 而非 **$5.04**，付款前未見任何金額確認視窗；單一使用者回報，官方未確認（[HN](https://news.ycombinator.com/item?id=50121562)）。
- **你能先做什麼**：以非美式小數點輸入習慣儲值 API 額度者，送出前應放大核對實際扣款金額，不要只信輸入框顯示的數字。

#### 🔴 2026-10-11：Reddit 回報 Claude Code 2.1.289 成本顯示把 Haiku 5.5 計成 Opus 費率

- **Reddit/r/ClaudeAI（0 留言，2026-10-11）**：使用者回報 Claude Code 2.1.289 版的內建成本顯示（cost readout）把 Haiku 5.5 用量以 Opus 費率計算，實測讀數比實際金額高達 17 倍；單一使用者回報，官方未確認，日報未見其他來源佐證。
- **你能先做什麼**：倚賴內建成本顯示控管 Haiku 5.5 支出的使用者，近期應自行核對帳單金額，不要只信這個讀數。

#### ✅ 2026-10-07：Anthropic Status 官方通報——部分組織被誤判已達花費上限而遭暫停

- **Anthropic Status（[status.claude.com/incidents/vmys9qn874h4](https://status.claude.com/incidents/vmys9qn874h4)，2026-10-07 21:23 UTC，Resolved）**：部分設有組織層花費上限的組織曾被系統誤判已達上限而遭暫停、Claude 請求被拒；官方已於 21:23 UTC 標記解決，當天受影響的團隊現在應已恢復正常。

#### 🔴 2026-10-02：GitHub Issue #8327——設定 `ANTHROPIC_API_KEY` 蓋過 Max／Pro 訂閱後遭「組織已停用」擋下

- **GitHub Issue #8327（121 則留言、22 個反應，2026-10-02）**：已有效訂閱 Pro／Max 的使用者設了 `ANTHROPIC_API_KEY` 後收到「Organization has been disabled」錯誤；日報未見官方回應（[GitHub #8327](https://github.com/anthropics/claude-code/issues/8327)）。
- **與既有規則的關係**：同一個變數蓋過訂閱路徑，但現象不同——規則區那條是改走 API 計費，本則是請求被擋；機制面見 [[entities/claude-code]] 已知問題。你能先做的：改用訂閱登入時取消該環境變數。

#### 🔴 2026-10-01：Anthropic Status 官方通報——credit purchase 入帳延遲，部分請求因餘額不足失敗

- **Anthropic Status（[status.claude.com/incidents/k0h22tsvnydg](https://status.claude.com/incidents/k0h22tsvnydg)，2026-10-01 16:20 UTC，Investigating）**：官方通報 Claude API 與 platform.claude.com 效能降級，credit purchase 入帳延遲，造成部分請求因餘額不足失敗；修復時間未載。

#### 🔴 2026-09-21：新 GitHub Issue #37394——Max Plan 用量觸頂速度異常快，與 #16157／#38335 同類回報的第三個獨立 issue

- **GitHub Issue #37394（92 則留言、43 👍，2026-09-21 查證）**：標題稱 Max Plan 用量觸頂速度異常快；互動量低於本頁已記錄之 #16157、#38335，症狀同屬「配額消耗過快」類別，官方尚無回應（[GitHub #37394](https://github.com/anthropics/claude-code/issues/37394)）。
- **與既有紀錄的關係（推論，待證實同根因）**：與 09-17 已記錄 #16157「Max 訂閱幾乎一開工就撞上用量上限」同屬一類回報，惟為不同 issue 編號、不同回報者，是否同根因未見官方交叉確認，不可合併。

#### 🔴 2026-09-17：Issue #16157 留言數增至 1,495——官方同日新增用量限制說明文件

- **GitHub Issue #16157（1,495 留言、725 👍，2026-09-17 查證）**：延續 09-06 已記錄之 1,492 留言，互動量持續攀升，仍為本頁計費／配額爭議互動量最高單則（[GitHub #16157](https://github.com/anthropics/claude-code/issues/16157)）。
- **官方同日更新說明中心「How do usage and length limits work?」**：新增用量與長度是兩種不同限制的說明，並建議暫時關閉不需要的工具／連接器以節省用量；未直接回應本 issue，狀態維持 🔴（Official Docs，2026-09-17）。

#### 🔴 2026-09-12：Max 方案 session 額度異常追蹤更新——GitHub Issue #38335 攀升至 850 留言、545 👍，重返事故總表

- **GitHub Issue #38335（850 留言、545 👍，2026-09-12 查證）**：延續 07-10 已記錄之 792 留言、08-14 已記錄之 543 👍，互動量持續攀升；問題自 2026-03-23 起未解，官方仍無回應（GitHub https://github.com/anthropics/claude-code/issues/38335）。
- **同日 2 則 Reddit 佐證（各為單一貼文，未經證實）**：r/ClaudeCode 用戶稱 5x 方案週用量達 10% 時，帳單由上週約 $140 降至本週約 $50；另一貼文質疑官方「未告知就調整了機制」。兩則均無帳號數據佐證，僅並列記錄同一疑慮方向。
- **與 09-14 換軌的關係（推論）**：週配額換軌（+50% 促銷到期、永久 +25% 接手）尚未生效，本波回報早於換軌，不能以換軌本身解釋。
- **後續（2026-09-16）**：留言數微升至 855（+5），👍 持平 545，官方仍無回應（GitHub https://github.com/anthropics/claude-code/issues/38335）。

#### 🔴 2026-09-09：TechCrunch 揭露駭客可在不竊取密碼情況下「抽乾」訂閱者用量額度

- **TechCrunch（09-08，跨 3 來源）／Startup Fortune（09-09）**：駭客可不經密碼抽乾訂閱者用量額度；僅標題可用。攻擊手法見 [[topics/ai-agent-safety]]，此處僅記帳單衝擊：讀者「觸頂」未必等於自己實際耗用（推論）（Google News/TechCrunch；Startup Fortune）。
- **官方通知：infostealer 竊 session cookie，免密碼就能抽乾額度（2026-08-30）**：官方已強制登出、撤銷竊得 token、刪存卡並退誤扣款；規模與受害戶數未公布。惡意軟體清單與攻擊面見 [[topics/ai-agent-safety]]（查證 2026-09-26）

#### ⚖️ 2026-09-08／09-09：四家媒體跟進 Max 20x 集體訴訟——The New Stack 首度點名「週用量上限」為落差機制

- **The Verge（2026-09-08）**：報導 AI 重度用戶已對 Anthropic 提起訴訟，指控訂閱方案用量宣稱具誤導性；僅標題可用。
- **Startup Fortune（2026-09-09）**：同一起訴訟的另一篇報導，聚焦 Max 20x「20 倍用量」宣稱與實際體驗的落差；僅標題可用。
- **The New Stack（09-08）**：首度點名機制——官方宣傳的「20 倍用量」實為**新設的週用量上限**（weekly ceiling）。與本頁 08-31 HN 討論、06-16 集體訴訟同屬一爭議延燒，非新指控；官方未見逐字定義（Google News/The New Stack）。
- **Engadget（2026-09-09）**：同一起訴訟第四篇報導，標題聚焦訂閱用戶已對 Anthropic 提起訴訟、爭執點在 Max 方案條款內容；僅標題可用，未見新增求償金額或案情細節，與上列三則同屬同一起訴訟的媒體擴散（Google News/Engadget）。
- **同日 Reddit 疑似相關回報（單一貼文，score 未知，未經證實）**：r/ClaudeCode 用戶（2026-09-09）稱同一天觸頂日限額兩次，第二次視窗重置約 50 分鐘後即再次觸及 100%；與本頁已記錄 09-06 GitHub Issue #16157（幾乎一開工就撞上限）症狀相似，是否同根因未見交叉確認，僅並列記錄（Reddit）。

#### 🔴 2026-09-06：GitHub Issue 累積 1,492 則留言、725 👍——Max 訂閱幾乎一開工就撞上用量上限

- **GitHub Issue #16157（1,492 留言、725 👍 reactions，2026-09-06 查證）**：Max 訂閱用戶回報幾乎一開工就撞上用量上限，留言數為本頁計費／配額爭議類目前最高（前次高點 #5088 的 184 則），是今日所有 GitHub Issue 中留言數最高者；亦同步記錄於 [[entities/claude-code]] 已知問題。
- 出處：[GitHub #16157](https://github.com/anthropics/claude-code/issues/16157)
- **與既有事件的關係（推論，待證實同源）**：症狀與本頁已記錄的多起「用量無明顯使用即耗盡」事故（08-14 Issue #38335 session 額度異常、08-04 Reddit 回報 Max 20x 半小時 0%→100%）同屬「配額計算是否準確」一類，惟本則互動規模遠超其餘各案，且問題描述為「幾乎立即觸頂」而非既有案例的「一段時間內耗盡」，是否同根因未見官方交叉確認，不可合併
- **後續（2026-09-12）**：#38335 攀升至 850 留言、545 👍，重返事故總表，見上方 09-12 條目。
- **同日 Reddit 疑似相關回報（單一貼文，score 0，非週熱門，未經證實）**：r/ClaudeCode 貼文稱收到「即將達上限」警告，但實際用量遠未接近門檻，與本則同屬「配額顯示是否準確」討論，惟訊號較弱（score 0、非週熱門標記），僅並列記錄不獨立成案（Reddit）
- 🔎 **查無官方**（標 2026-09-07｜查 GitHub #16157、usage limits｜複 2026-11-30）：官方 09-17 只新增 usage／length limits 的一般性區別，未給觸頂成因或修復時程（2026-09-26 查 `support.claude.com`）。
  - 2026-10-31 複查 [#16157](https://github.com/anthropics/claude-code/issues/16157)：仍 Open（標籤 bug、area:cost）；
    - 官方唯一實質回覆是 2026-01-26 置頂留言（稱限額未變、歸因 Opus 4.5 耗 token 更多，並調整 edge case 的 token 用量），之後僅有使用者留言，無新成因或修復時程。

#### 🔴 2026-09-04：GitHub Issue 累積 184 則留言——Max 5x 續訂扣款後帳號遭停用

- **GitHub Issue #5088（184 留言，2026-09-04 查證）**：Max 5x 續訂扣款完成後帳號隨即遭停用，無法使用已付費的方案；184 則為本頁計費爭議類目前最高（前次高點 77／67 則）。
- 出處：[GitHub #5088](https://github.com/anthropics/claude-code/issues/5088)
- **與既有事故的關係**：與 08-12 Issue #55982（升級流程 PaymentIntent 遭提前作廢）同屬「付款/帳務基礎設施層故障」而非「用量計費異常」，惟本則更嚴重——付款已扣款成功、帳號卻遭停用，使用者付了錢反而喪失服務存取權，是本頁目前記錄最直接侵害付費用戶權益的計費事故型態（推論）；機制面／官方是否回應修復詳見 [[entities/claude-code]] 已知問題，此處僅記計費/帳務面
- 🔎 **查無官方**（標 2026-09-04｜查 Max 5x、帳號停用｜複 2026-11-10）：[GitHub #5088](https://github.com/anthropics/claude-code/issues/5088) 現況（2026-09-20）——仍為 open，無 Anthropic 人員留言、無成因說明，支援信件與退款申請均未見回覆。
  - 2026-10-10 另查官方 [說明中心](https://support.claude.com/)，**未見任何關於 Max 5x 訂戶帳號停用成因或申訴流程的條目**；issue 本身本輪無法複驗（本 session 未取得 `anthropics/claude-code` 讀取授權，依規不擴權）。
- 已確認屬「付款成功後帳號隨即遭停用」的重複模式（另見 #80872、#64480、#90531），惟仍無官方就根因或修復時程表態。
- **後續（2026-11-02）**：留言數增至 190（+6），新增 69 個 👍 reactions 數據；官方仍無回應（[GitHub #5088](https://github.com/anthropics/claude-code/issues/5088)）。

#### ⚖️ 2026-08-31：HN 質疑「20x」用量宣稱的實質定義——只放大 5 小時視窗、非週上限，呼應既有 Max 20x 集體訴訟

- **Hacker News（2026-08-31 13:56 UTC）**：發文者指出，官方行銷所稱的「20x」用量提升（見 Max 20x 方案命名），實際只放大**單次 5 小時使用視窗**內的用量上限，並非字面上讀者直覺理解的「週用量整體上限的 20 倍」；發文者認為此行銷用語容易誤導，討論串中有留言提及已有針對用量宣稱的行銷不實訴訟（[HN https://news.ycombinator.com/item?id=49509882](https://news.ycombinator.com/item?id=49509882)）。
- **對照本頁既有紀錄**：Karl Kahn 於 2026-06-16 提起的集體訴訟指控 Max 20x **實際用量僅為 Pro 的 6–8 倍**、而非廣告的 20 倍（見方案細節「Max 20x 用量上限集體訴訟進行中」）。兩者是同一爭議的不同角度——訴訟問「20 倍算得對不對」，本則 HN 問「20 倍算的是哪個時間窗」，互為佐證但非同一指控，不可合併。
- **未解之處**：官方未見文件逐字定義「20x」的計算基準（5 小時視窗、日、週）；本則是否構成訴訟新增指控依據、或僅為社群側佐證討論，未見後續（單一 HN 討論串，score 未知，無主流媒體跟進）。

#### ✅ 2026-08-28：Reddit 整理十週時間軸為誤讀——查證確認官方從未承諾 Fable 5 恢復訂閱內含（結案見 [[topics/anthropic-commitments]]）

- **Reddit r/ClaudeAI（2026-08-28）**：使用者整理 Fable 5 計費爭議時間軸，指出官方曾表態 Fable 5 將恢復為訂閱內含，惟十週後 Pro 方案仍按 token 計費，情緒標記 😤。
- **官方查證結案（2026-09-20，[Claude Help Center](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)＋[官方 X 公告](https://x.com/claudeai/status/2078302415804379218)）**：Pro／Team Standard 方案從未被官方承諾恢復訂閱內含——07-20 起僅 Max／Team Premium 內含（佔週用量上限 50%）。
- Pro／Team Standard 僅獲一次性 $100 usage credit（07-20～08-02 領取，已於 09-17 到期），之後按 API 費率計費，屬官方永久性方案差異化政策，非未兌現的承諾（來源同上）。
- **與本頁定位的關係**：此為 Reddit 貼文對既有 07-20 分界的誤讀，非新計費事實；承諾兌現追蹤詳見 [[topics/anthropic-commitments]]「已結案」表 ⟨C-01⟩。
- （不列入總表：本則已結案，非現在還在發生的事故）

#### ✅ 2026-08-15：Fable 5／Opus 5 是否共用同一週用量池 → ✅ 官方確認共用，「50% 上限」是池內天花板不是額外配額（2026-08-22 查證結案）

- **Reddit r/ClaudeCode（2026-08-15）**：使用者質疑，若 Opus 5 與 Fable 5 共用同一週用量池，則 07-20 分界給 Max／Team premium 的「Fable 5 最多用到週用量 50% 且不額外收費」形同被 Opus 5 消耗架空，牴觸設計原意。
- **查證本頁既有紀錄**：07-20 分界僅明確 Fable 5 自身的計量規則（Max/Team premium 標配、Pro/Team standard 走 usage credits），**未見官方一手來源說明兩者是否共用計量池**——此為尚未回答過的問題，非既有紀錄矛盾。
- **✅ 官方答案（2026-08-22 查證）**：**共用同一池，貼文的直覺是對的，但推論的「牴觸設計」不成立。** 官方〈Claude Fable 5 on your plan〉逐字寫明 Fable 5「draws from your plan's regular weekly usage limits and uses them faster than other Claude models」，FAQ 另稱「your use of other models draws from the same usage limits and you can never use more than your weekly limit」——亦即 **50% 是同一池內的「Fable 5 最多能吃掉一半」天花板，本來就不是額外配額**。讀者要知道的實務結論：拿 Opus 5 跑滿週用量，Fable 5 那 50% 額度也跟著不見；反之亦然（來源：[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)，官方頁最後更新 2026-07-20，2026-08-22 查證；原始質疑 Reddit https://www.reddit.com/r/ClaudeCode/comments/1vozbmm/opus_5_and_fable_5_sharing_a_pool_isnt_that_a/）

#### 🔴 2026-08-14：Max 方案 session 額度自 3/23 起異常快速耗盡（本頁互動量最高配額回報）+ 社群質疑用量被暗中調降

- **GitHub Issue #38335（👍 543，2026-08-14 查證，CLI 使用情境）**：Claude Max 方案的 session 限制自 **2026-03-23** 起異常快速耗盡；543 個 👍 遠高於本頁同類回報（反應數非留言數）（GitHub https://github.com/anthropics/claude-code/issues/38335）
- 機制面見 [[entities/claude-code]] 已知問題；此處僅記配額／計費面：問題若屬實，代表配額計算自 3 月下旬起即可能有系統性異常，而非 07-20 旗艦分界後才出現的新問題（推論；根因、是否與 Issue #79337 同源均未見證實）
- **Reddit r/ClaudeCode：質疑用量配合 8/19「50% 提升永久化」而暗中調降（單一貼文，未經證實）**：使用者質疑 Anthropic 暗中調降用量，以在傳聞的「50% 用量提升」8/19 永久生效前後製造對比（score=0，Reddit RSS 無讚數非低互動指標；屬使用者推測，非事實）
- **查證本頁既有紀錄**：本頁記錄的「週用量 +50%」促銷（2026-06-15 起臨時提高、多次延長至 2026-07-19）已由 07-20 分界取代，未見與「8/19 永久化」對應的官方公告；貼文所稱「8/19」與既有時程（7/19）不吻合，可能指涉另一項本頁未記錄的官方承諾，或屬時程誤記；具體指控查證見下方標記（Reddit r/ClaudeCode，2026-08-14）
- **✅ 08-18 官方公告部分澄清（是「延長至 8/31」，非「永久化」）**：08-18 官方公告證實「週用量 +50%」促銷持續延長中，**並未如本頁此前誤記般已於 07-19 失效**——貼文對促銷仍生效的直覺並非空穴來風。惟官方措辭為暫時延長至 **2026-08-31**，非永久政策。
- 已查證（2026-09-20，[Anthropic 官方公告](https://www.anthropic.com/news/higher-limits-spacex)）｜**「暗中調降以製造對比」指控大方向成立**：09-14 官方公告將「臨時 +50%」（延長至 08-31）收回、改為「永久 +25%」，換算對比 08-31 前水位**淨減少約 17%**。
- 社群質疑「只講調升、淡化淨減少」誤導，Anthropic 員工承認溝通可更清楚；與原猜測（8/19 前後降量）時間點略有出入，惟「降量搭配正面話術」核心指控方向獲證實。

#### 🔴 2026-08-12：升級方案付款流程新爆計費 bug——PaymentIntent 於確認完成前遭提前作廢

- **GitHub Issue #55982（77 留言、👍 26 反應，2026-08-12 查證）**：升級方案時付款流程失敗——PaymentIntent 在使用者確認付款前即被後端 `void_invoice` 作廢，導致升級無法完成；77 留言已達高互動標準，是本頁互動量最高的付款類 bug（GitHub https://github.com/anthropics/claude-code/issues/55982）
- **同日 Reddit 疑似相關回報（單一貼文，未經證實）**：r/ClaudeCode 用戶回報帳戶已有既有 credits，系統仍要求重新輸入付款資訊；是否與上述 PaymentIntent 作廢同源未見證實，各自獨立記錄（Reddit https://www.reddit.com/r/ClaudeCode/comments/1vm9chm/claude_asking_me_for_payment_details_to_use/）
- **與既有事故的關係（推論）**：本頁已記錄多起用量點數／帳務異常（08-07 Issue #79337、07-20 南韓 $16.7M 帳單等），本次首度集中在「升級付款流程本身失敗」而非「用量計費異常」，屬付款基礎設施層級的新故障面向

#### 🔴 2026-08-07：Fable 5 Max 方案用量點數異常追蹤更新——留言數攀升至 67，延燒逾 18 天

- **GitHub Issue #79337 互動量持續攀升**：**67 留言**（08-07 查證，較 07-25 的 42 留言攀升），延續追蹤自 07-20 Fable 5 成為 Max 標準模型第一天起爆發的用量點數異常，含此前記錄的「靜默降級 Opus 4.8」細節。**與既有事件的關係**：問題延燒逾 18 天，橫跨官方 07-20 Status「Max 誤判、重啟可解決」定性與 07-24（13 reactions）、07-25（42 留言、15 reactions）多輪查證；留言數持續攀升顯示影響擴大而非收斂，是本頁追蹤時間最長的未解計費／配額爭議（推論；官方是否修復、與「誤判」定性的關係均未見新公告釐清）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 🔴 2026-08-04：Reddit 回報 Max 20x 用量在未使用期間半小時內從 0% 衝到 100%，疑似配額計算異常

- **Reddit r/ClaudeAI 週熱門回報**：Max 20x 用量在**未使用 Claude 的情況下**半小時內從 0% 攀升至 100%（週熱門，2026-08-04）。**與既有已知問題的關聯（推論，待證實同源）**：症狀與 [[entities/claude-code]] 已記錄的 GitHub Issue #41788〈Max 20 plan: rate limit 100% exhausted within ~70 minutes after reset〉（版本迴歸 bug）高度相似，皆為用量在短時間、無明顯使用下被耗盡；兩者是否同根因、同批受影響用戶均未見交叉確認，不可合併（Reddit https://www.reddit.com/r/ClaudeAI/comments/1vf6i4y/max_20x_usage_went_from_0_to_100_in_half_an_hour/）

#### 🔴 2026-08-02：Max 5x → Max 20x 訂閱升級持續失敗，與此前三起已知 issue 同源

- **GitHub Issue #55266**：Max 5x 升級至 Max 20x 失敗，系統回報「Unable to update subscription」；Issue 標題指此問題與此前三起 issue（#10832、#50710、#43118）「same pattern as」，暗示升級流程存在持續性而非一次性的系統問題。**與既有事件的關係**：本頁已多次記錄 Max 計費爭議（06-16 集體訴訟、07-02 升級介面誤導扣費、07-24/25 Fable 5 用量點數異常），本則獨立於「用量計量」之外，聚焦「升級操作本身無法完成」；長期未解可能直接阻擋用戶轉向高階方案，衝擊訂閱轉換率與客服負擔（推論；受影響規模、issue 建立時間、官方回應未見細節）（GitHub https://github.com/anthropics/claude-code/issues/55266）

#### 🔴 2026-07-25：Fable 5 Max 方案異常追蹤更新——留言數攀升至 42，新增「靜默降級 Opus 4.8」細節

- **GitHub Issue #79337 互動量攀升 + 新增技術細節**：**42 留言、15 reactions**（07-25 查證，較 07-24 的 13 reactions 明顯攀升）。新增回報細節：受影響用戶反映系統除要求額外購買用量點數外，還會**靜默降級為 Opus 4.8**執行請求，使用者可能不知情地以為仍在用 Fable 5，實際計費與模型能力已改變。逾 5 天未見官方修復或說明，與 07-20 官方 Status「Max 誤判、重啟可解決」的定性落差持續擴大（推論，待官方回應）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 🔴 2026-07-24：Fable 5 Max 方案計費/配額執行異常持續逾 4 天未解（追蹤 07-20 誤判事件後續）

- **GitHub Issue #79337：Fable 5 成為 Max 標準模型後仍被要求額外用量點數**：13 reactions（2026-07-24 01:16 UTC 查證）。自 07-20 Fable 5 成為 Max 標準模型第一天起，Claude Code 反而要求額外購買 usage credits 才能使用，持續至少 4 天。**與既有事件的關係**：07-20 官方 Status 事件（tnypgb2jbqnq）將此類現象定性為「Max 方案誤判」、建議重啟即可解決；本 Issue 顯示問題未如官方所述經重啟消失。可能是（a）另一個持續性的配額執行 bug、或（b）官方「誤判已修正」的範圍未涵蓋此類個案，待官方釐清（推論，不可認定為同一根因或已解決）（GitHub https://github.com/anthropics/claude-code/issues/79337）

#### 🔴 2026-07-20：南韓用戶收到 $16.7M 帳單疑似故障，與 07-12/13 已證實帳務錯誤規模相近

- **KED Global：南韓用戶收到 $16.7M 帳單**：報導一名南韓用戶收到疑似系統故障產生的 **$16.7 百萬美元**帳單（Google News/KED Global）。**推論，待證實**：金額與 07-12/13 已記錄的 Anthropic 證實 1660 萬美元帳務錯誤（Tech Times）高度接近，但原文摘要遭 RSS 截斷、未見報導連結兩起事件，**不可認定為同一事件**。
- **10-24 補**：BeInCrypto、Startup Fortune 的 $16.6M 即南韓免費用戶個案，與本則極可能同一人，連結仍屬間接。
- （狀態隨 07-12/13 條，推論為同一筆已證實錯誤的個案）

#### ✅ 2026-07-20：Fable 5 免費期到期後社群反映存取異常，含官方已證實的 Max 誤判事件

- **Reddit r/ClaudeAI：Max 方案用戶反映無法使用 Fable 5**：Reddit 用戶（score 0，Reddit RSS 抓取機制下分數不可信、僅單一來源）反映 Max 方案疑似無法存取 Fable 5。**與官方 Status 事件吻合**：時間點與 Anthropic Status 頁面同日（07-20 07:35 UTC）公告的「Max 方案用戶被誤判需使用點數才能存取 Fable 5」事件吻合，官方已確認為誤判並建議受影響用戶重啟；官方事件細節詳見 [[entities/claude-code]]（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v1g5yy/so_i_cant_use_fable_with_my_max_plan_ey/；Anthropic Status https://status.claude.com/incidents/tnypgb2jbqnq）
- **Reddit r/ClaudeAI：App 內 Pro 方案顯示異常消失（單一回報，未經證實）**：另一則 Reddit 貼文（score 0，僅單一來源）反映 App 內 Pro 方案顯示異常消失/變動，原因不明。**注意**：與上則 Max 誤判事件同日出現，但官方 Status 頁面僅證實 Max 方案誤判一事，本則 Pro 方案異常未見官方對應公告或其他來源佐證，暫不推論兩者為同一根因，僅並列記錄待後續查證（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v1hiu8/anthropic_nuked_the_pro_plans_on_the_app_for_some/）

#### 🔴 2026-07-12/13：Anthropic 證實 1660 萬美元帳務錯誤，稽核發現企業多收 170 萬美元

- **官方證實大規模帳務錯誤**：Tech Times 報導（20260712，於 07-13 日報顯示）Anthropic 證實一筆 1660 萬美元的帳務錯誤，稽核人員另發現企業客戶被多收 170 萬美元。**對信任度的意涵**：此前多次帳務爭議（HERMES.md bug、Max 升級誤導扣費、儀表板 0% 用量仍收費等）均為個案或社群自行發現，本次是官方證實的具體金額規模最大案例，可能強化企業客戶對 Anthropic 計費系統可靠性的疑慮，尤其在企業支出控管（spend controls）功能剛於 07-04 推出、企業成本敏感度已因競品定價戰而升高的背景下（推論）；具體受影響企業名單、退款機制未見報導（Tech Times https://www.techtimes.com/articles/320266/20260712/anthropic-confirms-166m-billing-error-auditors-find-17m-enterprise-overcharges.htm）

#### 🔴 2026-07-02：Max 升級誤扣費案例 + 客服/退款流程爭議

- **長期 Max 用戶反映升級介面誤導、退款無門**：Reddit r/ClaudeAI（score 未標，07/02 05:44 UTC）一則熱門貼文指出，長期 Max 用戶 5 月底將方案從 $100/月升級到 $200/月時，介面誤導其誤購 $200 credits（而非升級訂閱本身），事後找不到有效退款客服管道，一個多月問題未解決，貼文標題直指「Claude 客服是幾乎所有科技公司中最差的」。**對留存的意涵**：這是繼 [[topics/code-quality-decline]] 用戶退款訴求、6/16 Max 集體訴訟之後，另一起具體指向「客服/退款流程缺失」而非「模型能力」的留存風險案例；升級付費流程的 UX 缺陷若造成非自願扣費，可能加劇既有集體訴訟的輿論壓力（推論）（Reddit https://www.reddit.com/r/ClaudeAI/comments/1uliph2/claude_truly_has_the_worst_customer_support_out/）
- **企業合作層級（Select vs Preferred）資訊不透明**：同日 Reddit r/ClaudeAI 另有使用者詢問 Anthropic 企業認證 Select 與 Preferred 合作層級的具體差異（純提問，無官方或社群解答內容）；此分級用語亦見於 [[topics/anthropic-business]] 6/30 DataArt「精選（Select）合作夥伴」條目，但兩層級的權益/門檻差異目前無公開資料，待補充（Reddit https://www.reddit.com/r/ClaudeAI/comments/1ulj6r4/partnership_levels_select_vs_preferred/）

**2026-06 事故**：隱私政策新增年齡／身份驗證條款（07-08 生效）、加州用戶帳號遭盜刷產生歐元計費（06-24，⏸ 逾 90 天無後續）。原始條目見 [[entities/pricing-archive#2026-06]]。

**2026-05 事故**：Claude Code 定價溝通混亂事件（05-20，✅ Simon Willison 分析）、Pro 方案 0% 用量仍遭收費（05-11，⏸ 1M context window 觸發 API 計費通道）、提示快取窗口悄悄縮短（05-05，⏸ 未公告）。完整記錄見 [[entities/pricing-archive#2026-05]]。

**2026-04 事故**：Token 費用預估靜默翻倍（04-29，⏸ 逾 90 天無後續）、Opus「圍牆內圍牆」事件已修正（04-28，✅）、HERMES.md 靜默計費 bug 官方確認但拒絕退款（04-25，⛔）。原始條目見 [[entities/pricing-archive#2026-04]]。

## 配額與速率

#### 2026-10-30：Reddit 回報 Anthropic 已將 Max5、Max20 方案改名，並取消 Max20 的 5 小時用量窗口限制（改名屬實；5 小時限制僅對 Ultra 驗證帳號取消，官方已查證）

- **[r/ClaudeAI · 週熱門](https://www.reddit.com/r/ClaudeAI/comments/1xjlvlc/anthropic_renames_max5_and_max20_and_removes_5h/)**：貼文稱方案已改名、Max20 的 5 小時用量窗口限制已取消；僅有標題與圖片，無官方公告連結佐證（10-30 17:34 UTC）。
- **2026-11-02 對官方方案頁查證**：改名屬實——$200 一檔現名 Ultra（Pro 的 10 倍用量），$100 的 Max 為 5 倍；5 小時窗：方案頁載 Ultra 驗證帳號無 5 小時上限，見 [[entities/pricing#我的方案現在有什麼]]。
- **2026-11-08 複查官方說明**：[claude.com/pricing](https://claude.com/pricing) 載 Max（$100）為 Pro 5 倍、仍有 5 小時額度，Ultra（$200）「No 5-hour limit」並註明僅限驗證帳號。
  - [support.claude.com〈Using Claude Code with your Pro or Max plan〉](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)載 Pro／Max 有 5 小時 session 上限與週上限，「verified Ultra accounts don't have a five-hour session limit」。
  - **結論**：Reddit 貼文「Max20 改名、5 小時限制取消」半對——改名為 Ultra 屬實；取消並非全面，僅限驗證帳號，未驗證帳號可能有暫時性 session 上限；週上限仍在。

#### 2026-10-14：官方再次更新《How do usage and length limits work?》——觸頂後續說明改為「升級方案後新上限立即生效」

- **Official Docs 變更偵測（2026-10-14）**：觸頂後續說明從「可升級方案，搭配 usage credits…」改為「升級後新上限立即生效」（頁面字數 6964→7021）。
- **讀者判讀**：新措辭把「升級方案」的效果單獨講清楚——升級後新上限立即生效，不必依賴 usage credits；與 2026-10-09 三頁同步改版（移除「過渡到額度計費需明確同意」措辭，見下方 10-09 條目）屬同一份文件的持續調整，非新規則。

#### 2026-09-06：Mashable 引述 Reddit：多則貼文稱付費方案可用量遠低於宣傳（媒體＋多則社群回報，官方頁面未查證）

- **Mashable**：報導引述 Reddit 使用者反映，Claude 付費方案實際可用量低於官方宣傳；僅標題可用，具體方案別、對照數字未見報導（Google News/Mashable）。
- **[r/ClaudeCode「Cancelled my 20x Max subscription」](https://www.reddit.com/r/ClaudeCode/comments/1w8vgxh/cancelled_my_20x_max_subscription/)**：使用者稱取消一份 20x Max 訂閱、改用 OpenAI 的 Astra；稱 Fable 上限為總用量 50%（本頁已載為官方規則）、Fable token 效率不佳（個人觀感，未附測試方法）。
- **[r/ClaudeCode「Why cancelling subscriptions now will matter」](https://www.reddit.com/r/ClaudeCode/comments/1w8vs8e/why_cancelling_subscriptions_now_will_matter/)**：作者臆測用量限制變快與 Anthropic 即將 IPO 有關，稱公司或藉此對投資人「做帳面數字」。**純屬個人推測、無佐證，本頁不採信此因果關係**，僅記錄為情緒訊號。
- **與既有時序的關係**：09-14 起週配額換軌（+50% 促銷 09-13 到期、由永久 +25% 接手，換算後水位降約 17%，見「當前生效的計費規則」）**尚未生效**（今日 09-06）；本波抱怨若屬實，時間點早於官方換軌，不能以換軌本身解釋，具體成因未見報導。

#### 2026-08-21：Reddit 回報本次配額重置後 token 分配出現明顯變化（單一貼文，2026-08-21 指控，已掃日報至 2026-09-06 無後續；官方頁面未查證）

- **r/ClaudeCode（2026-08-21 09:26 UTC）**：使用者回報本次配額重置後，token 分配出現明顯變化，貼文未附具體帳號數據、變化方向（增加或減少）或方案別；Reddit RSS 抓取 score 恆為 0，非真實低互動指標，亦未見「週熱門」標記，暫不視為已具系統性訊號強度的個案。
- **與既有配額異常回報的呼應（推論）**：與本頁已記錄之多起配額/用量異常回報（如 08-14 Max 方案 session 額度異常耗盡、08-12「用量限制遭調降」疑慮）同屬「使用者感受配額被調整、官方未公告」的重複性模式，惟本則未提供具體方案別或變化方向，訊號強度較既有紀錄更弱。
- **配額重置機制是否有變動**：僅單一 Reddit 回報（https://www.reddit.com/r/ClaudeCode/comments/1vubdkb/huge_change_in_token_allocation_this_reset/），官方至今無對應公告。

#### 2026-08-12：官方文件釐清 usage limits 與 length limits 為兩種不同機制；同日再現「用量限制遭調降？」社群疑慮（單一貼文，2026-08-12 指控，已掃日報至 2026-09-06 無後續；官方頁面未查證）

- **官方 Help Center：《How do usage and length limits work?》（2026-08-12 查證）**：官方文件說明 usage limits（隨對話長度、複雜度、啟用功能、模型、effort 等級等變動的「額度」）與 length limits（單則訊息／對話長度上限）是兩種不同概念；不同方案（Pro／Max／Team 等）的額度規則亦不同。此文件首度明確說明 usage limits 具動態性，而非固定額度（來源：[How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)）
- **同日 Reddit 疑慮（單一貼文，未經證實）**：r/ClaudeCode 用戶反映近幾天用量額度消耗速度明顯變快，詢問是否遭調降限額；無官方回應佐證，亦未見其他來源佐證（Reddit https://www.reddit.com/r/ClaudeCode/comments/1vm9135/did_anthropic_decreased_the_usage_limit/）
- **與官方文件的潛在關聯（推論，非官方回應）**：若 usage limits 確實隨對話複雜度／effort 等級動態變動（見上方官方說明），使用者感受到的「額度消耗變快」有可能源於任務型態改變而非官方調降限額；惟官方文件未直接回應本則貼文的具體指控，限額本身是否曾調整不可視為已解釋。

#### 2026-07-22：Reddit 週熱門質疑 Anthropic 宣稱的用量提升未反映於實際體驗（單一貼文，2026-07-22 指控，已掃日報至 2026-08-14 無後續；官方頁面未查證）

- **r/ClaudeAI 週熱門貼文**：標題稱「Anthropic Claims 50% usage boost that doesn't exist」，質疑官方宣稱的 50% 用量提升未反映在使用體驗；純圖片型貼文，無帳號數據或官方公告連結佐證。**與既有 +50% 促銷的關係（推論，待證實）**：不確定指涉的是本頁已記錄、07-19 到期的「週配額 +50% 過渡期促銷」，或另一項未見於日報的官方宣稱；若為前者，則與 05-16 已記錄的「Max 20x 用量上限未生效（數學實證）」同屬「官方宣告與實際體驗落差」的重複模式。本則達 Reddit 週熱門「低」門檻但無數據佐證，僅記錄為該落差模式的又一社群訊號（Reddit https://www.reddit.com/r/ClaudeAI/comments/1v3d8iz/anthropic_claims_50_usage_boost_that_doesnt_exist/）

#### 2026-07-16：週用量配額疑似再度提前重置（單一回報，2026-07-16 指控，已掃日報至 2026-08-14 無後續；官方頁面未查證）

- **Reddit r/ClaudeCode 回報週用量提前重置**：一位 Max 用戶回報週用量原約 41%、正常重置日為週二，當日卻提前歸零。單一回報，Reddit RSS 下 score 恆為 0（不代表真實互動量），未標「週熱門」，近 14 天日報無其他來源佐證，暫不升級為系統性訊號（Reddit https://www.reddit.com/r/ClaudeCode/comments/1uxzlyx/did_anyone_elses_claude_code_weekly_usage_reset/）
- **與既有現象呼應**：與 2026-05-16 記錄的「週用量配額意外提前重置（bug 或後端調整）」方向一致，顯示此類配額計時異常非單一事件，近兩個月至少兩次獨立回報（推論，無法確認是否同一根因）

#### 2026-07-07～10：Max 方案額度異常快速耗盡、token 消耗增加 3–5 倍（持續發酵，官方無回應）

- **GitHub Issue #38335（792 留言，2026-07-10 查證）**：反映 Max 方案 CLI session 額度自 2026-03-23 起異常快速耗盡，為近期社群互動量最高的計費類 issue 之一；留言數 07-08（790）→ 07-09（791）→ 07-10（792）持續微幅增加，社群互動已趨於高原期，官方仍無明確回應（GitHub https://github.com/anthropics/claude-code/issues/38335）
- **GitHub Issue #41506（54 留言/29 讚）**：反映 Max（$100/月）方案 token 消耗自 3 月底起增加約 3–5 倍，未見對應功能或用量增加可解釋此漲幅（GitHub https://github.com/anthropics/claude-code/issues/41506）
- **Reddit r/ClaudeAI：「Claude Max 20x: Why did 27% of one session consume 7% of my entire weekly limit?」（2026-07-09）**：使用者具體質疑單一 session 中 27% 的時間消耗掉整週額度 7%，用量計量比例明顯失衡，與 GitHub #38335 反映的異常耗盡現象方向一致
- **Reddit r/ClaudeCode：「Claude Max (20x) weekly limit exhausted in less than a day」**：使用者回報週額度不到一天即用盡（Reddit https://www.reddit.com/r/ClaudeCode/comments/1uqs99q/）
- **對留存的意涵**：多則獨立訊號（2 個高互動 GitHub issue + 2 則 Reddit 貼文）方向一致，指向 Max 方案的用量計量或消耗速率可能存在系統性異常，而非個案；與既有 06-16 Max 集體訴訟（廣告 20 倍實測僅 6–8 倍）同屬「用量承諾與實際體驗落差」的信任問題，Anthropic 至今（07-09）尚未提供官方解釋或修復時程（推論）
- **正面反例（同期出現）**：Reddit r/ClaudeAI · 週熱門（2026-07-09）「5 hour and weekly limits have been reset. Thanks Anthropic!」一則貼文回報 5 小時與週用量額度已被重置並表達感謝；與上述額度異常耗盡投訴同期出現，方向相反，可能反映用戶端因帳號、時段或所屬方案不同而體驗分化，非全面性的正面或負面訊號（推論）
- **後續（2026-09-12）**：#38335 攀升至 850 留言、545 👍，另有 2 則 Reddit 貼文佐證，升級至「事故與爭議」並重返事故總表，見該處 09-12 條目。

**2026-06 配額事故**：社群集體反映 Claude Code 配額再次縮減（06-30，無官方公告、幅度不明）。原始條目見 [[entities/pricing-archive#2026-06]]。

**2026-05 配額事故**：臨時用量提升優惠＋企業帳單三倍警訊（05-19）、Max 20x 上限未生效數學實證＋促銷時序整理（05-16）、Opus API 速率悄悄調降（05-10）、SpaceX 算力到位速率翻倍（05-07–09）。原始條目見 [[entities/pricing-archive#2026-05]]。

## 灰色市場與轉售現象

- 조선일보報導中國境內存在規避封鎖使用 Claude 的黑市交易，顯示官方封鎖未完全阻絕當地需求，規模與定價未見報導（Google News/조선일보，2026-10-04）；地緣政治執法面見 [[topics/ai-agent-safety]]。（區域存取政策本身的動態見 [[topics/anthropic-government-policy]]「現在有哪幾條線在動」第 1 列）
- 轉售商以最高 90% 折扣轉賣 Claude／Codex API 存取權，違反 Anthropic 消費者條款（禁止 resell、禁止分享帳號憑證）。
- 灰市管道「Poison Claude」已被兩獨立媒體證實會讓中間營運者讀取客戶傳送的全部 prompt——安全事件細節與可信度評估見 [[topics/ai-agent-safety]]。
- 🔎 **查無官方**（標 2026-08-10｜查 [[topics/ai-agent-safety]]、resale scope｜複 2026-11-24）｜轉售規模與個案執法回應均未見官方或媒體佐證。10-24 查官方：[商業條款](https://www.anthropic.com/legal/commercial-terms) D.4(a) 禁止未經核准的 resell；[Transparency Hub](https://www.anthropic.com/transparency) 未見轉售執法統計。08-29 `訊` 為探針假命中，已移除。

---

## 相關

- [[entities/pricing]]：母頁，現在怎麼計費、三路分流
- [[entities/pricing-history]]：價格、方案與促銷的沿革
- [[entities/claude-code-known-issues]]：逐條 issue 與互動數
- [[topics/code-quality-decline]]：token 消耗變多的三種解釋
- [[topics/community-cost]]：自己的設定吃掉多少額度、怎麼擋
- [[topics/ai-agent-safety]]：額度被盜用的攻擊面
- [[entities/pricing-archive]]：2026-04～06 的原始條目

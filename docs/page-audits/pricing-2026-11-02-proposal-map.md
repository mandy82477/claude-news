# 第 24 波 proposal-map：entities/pricing 逐節去向（2026-11-02）

> 行號一律指設計 commit `933a34d` 的原檔（pricing 969 行／archive 116 行）。逐行帳在 `<scratchpad>/w24/design/accounting.txt`（`split.py` 斷言 1–969 每行恰消費一次），本檔由 `make_map.py` 從它生成。
> 去向代號：**母**＝`entities/pricing`；**incidents**＝`entities/pricing-incidents`（新）；**history**＝`entities/pricing-history`（新）；**archive**＝`entities/pricing-archive`（既有）。

## 一、逐節去向

| 節（原行） | 行數 | 去向 | 改了什麼 |
|---|---|---|---|
| frontmatter、標題、標頭 L1–34 | 34 | 母 | 標題下插使命句（第 3 波定稿＋半句路由）；最後更新 11-02 |
| `%%` 拆頁評估 L35 | 1 | 母 | 改寫為「已拆」一行，記下一刀（API 塊） |
| callout L37–39 | 3 | 母 | 改寫：改名 11-02 對官方查證屬實＋兩條指路；原兩則 Reddit 隨事實去 incidents callout |
| 現況 L41–51 | 9 | 母 | 五段併兩段：09-14 換軌改過去式、Max／Ultra 倍數（官方 11-02）、計費切割一句指 archive；「你的選項」併入第二段 |
| （新）往下鑽：帳單出錯與價格沿革 | 9 | 母 | 路由表兩列（答什麼、最後動態）＋archive 一句 |
| 我的方案現在有什麼：表頭 L57、表 L61–67 | 8 | 母 | **整表重判**：Max／Ultra（10x）、「可領優惠」放月度 API credits（不付 Claude Code）、Pro 無、Team 共用池、Enterprise $20／席＋API 費率；資料截至 11-02 |
| usage credits 警語 L69、到期時分 L71 | 2 | 母（L69 縮成指路）／砍（L71） | 本文住生效規則 L201 |
| 方案細節 L73–99 | 27 | 母 | 砍 L79–80（＝L200）、L83（＝L214）、L84（archive 06-26 已更正）、L85（＝L215）；L86 改正「未見最低席位數」、Enterprise 公開價 |
| 一小時／一個月 L103–125 | 23 | 母 | L117「Opus 5 的 142／160 小時」→「Opus 5.5 的 172／200 小時」（推算，同表口徑） |
| 模型 API 定價 L128–154 | 27 | 母 | 補 Haiku 5.5 列（兩檔＋快取）；L140 刪「陣容中最低價」；L144 刪「僅 Claude API」與研究預覽兩句，改指乘數細節 |
| 還沒確定 L157–176 | 20 | 母 | 移出 ✅ 三列（L164／166／169）與過期 L168；新增 Ultra 5 小時窗列；L165 複查日 11-10；表下收 L602 懸置（裁決 6）；砍 L174、L176（已收斂，家在方案表／API 表／haiku-5-5） |
| 當前生效的計費規則 L180–219 | 40 | 母 | 砍 L192（09-13 到期促銷）、L194（＝L43）；L202、L212 指路改子頁；L219 點名兩項失效規則 |
| 通路與乘數、帳務坑、可用性 L223–289 | 67 | 母 | L279 指路改 history；L286 去互動數、錨點改 incidents |
| 事故現在還在發生嗎 L293–318 | 26 | 母（節名＋三路分流）／incidents（表與懸置細節） | 母頁留同名節：三路分流表＋known-issues 一句＋`### 事故與爭議（…）` 指路殼（daily/2026-10-24 錨點）；表搬 incidents `## 還在發生的事故`：上限 8、照條文排序、表下可見一行、互動數去掉；L297 砍、L299 死路徑改指 pages.md；L307 #38335 排第 9 移表下；L318 砍（分流取代） |
| 省錢一句 L322 | 1 | 母 | 不動 |
| 重要政策變動紀錄 h2＋導語 L326–329 | 4 | 砍 | 事件流分家，各子頁自有 h2 |
| 灰色市場與轉售 L330–336 | 7 | incidents | h3→h2 |
| 事故與爭議 L337–544 | 208 | incidents（06-24 條→archive） | h3→h2；L339 標題依證據等級改寫；L531 去「見計費切割風波」；`%% 未列入總表 %%` 舊備忘 17 行砍；06-24 條蒸進 archive `## 2026-06`，原位留一行總結 |
| 定價與促銷 L545–788 | 244 | history | h3→h2；L602 懸置回母頁、原位留指路一行；07／08 月不在本波 |
| 配額與速率 L789–846 | 58 | incidents（06-30 條→archive） | h3→h2；L794 改寫為 11-02 查證結果；L795 `%%` 待查證砍（verified #1 已答）；06-30 條蒸進 archive |
| 計費切割風波 L847–948 | 102 | archive `## 計費切割風波` | 死案歸檔（使用者 09-06 裁決）：h3→h2 改短名＋一行導語；L849 凍結 `%%` 砍；其餘照搬 |
| 成本案例與優化 L949–954 | 6 | history | h3→h2（裁決 (1)） |
| 相關議題、參考來源 L955–969 | 15 | 母 | 相關議題加兩子頁 |
| archive 原檔 116 行 | — | archive | 一字不刪；L34 最後更新、L37 callout 改指兩子頁；`## 2026-06` 依日期插入 06-30、06-24 兩條；檔尾新節 `## 計費切割風波` |

## 二、事件流逐則歸頁（每個 `####` 標題；L 號＝原檔）

| 行 | 去向 | 標題（前 50 字） |
|---|---|---|
| L339 | incidents（改） | 🔴 2026-10-27：Reddit 回報當日用量暴增 8 倍，稱 Anthropic 已證實服務 |
| L345 | incidents | 🔴 2026-10-24：GitHub Issue #79337 累積 77 留言——Fable 5 |
| L352 | incidents | 🔴 2026-10-24：新 GitHub Issue #56281——Max 5x → Max 2 |
| L359 | incidents | ⚖️ 2026-10-21：新 GitHub Issue #79773——7 月已升級 Max 20 |
| L364 | incidents | 🔴 2026-10-16：Hacker News 回報 Console 儲值小數點輸入 bug，$5 |
| L371 | incidents | 🔴 2026-10-11：Reddit 回報 Claude Code 2.1.289 成本顯示把 H |
| L378 | incidents | ✅ 2026-10-07：Anthropic Status 官方通報——部分組織被誤判已達花費上限而 |
| L382 | incidents | 🔴 2026-10-02：GitHub Issue #8327——設定 `ANTHROPIC_API |
| L389 | incidents | 🔴 2026-10-01：Anthropic Status 官方通報——credit purchas |
| L395 | incidents | 🔴 2026-09-21：新 GitHub Issue #37394——Max Plan 用量觸頂速 |
| L402 | incidents | 🔴 2026-09-17：Issue #16157 留言數增至 1,495——官方同日新增用量限制說 |
| L407 | incidents | 🔴 2026-09-12：Max 方案 session 額度異常追蹤更新——GitHub Issue |
| L416 | incidents | 🔴 2026-09-09：TechCrunch 揭露駭客可在不竊取密碼情況下「抽乾」訂閱者用量額度 |
| L423 | incidents | ⚖️ 2026-09-08／09-09：四家媒體跟進 Max 20x 集體訴訟——The New S |
| L431 | incidents | 🔴 2026-09-06：GitHub Issue 累積 1,492 則留言、725 👍——Max  |
| L442 | incidents | 🔴 2026-09-04：GitHub Issue 累積 184 則留言——Max 5x 續訂扣款後 |
| L453 | incidents | ⚖️ 2026-08-31：HN 質疑「20x」用量宣稱的實質定義——只放大 5 小時視窗、非週上限 |
| L459 | incidents | ⛔ 2026-08-28：Reddit 整理十週時間軸為誤讀——查證確認官方從未承諾 Fable 5 |
| L467 | incidents | ✅ 2026-08-15：Fable 5／Opus 5 是否共用同一週用量池 → ✅ 官方確認共用， |
| L473 | incidents | 🔴 2026-08-14：Max 方案 session 額度自 3/23 起異常快速耗盡（本頁互動量 |
| L484 | incidents | 🔴 2026-08-12：升級方案付款流程新爆計費 bug——PaymentIntent 於確認完成 |
| L491 | incidents | 🔴 2026-08-07：Fable 5 Max 方案用量點數異常追蹤更新——留言數攀升至 67，延 |
| L496 | incidents | 🔴 2026-08-04：Reddit 回報 Max 20x 用量在未使用期間半小時內從 0% 衝到 |
| L501 | incidents | 🔴 2026-08-02：Max 5x → Max 20x 訂閱升級持續失敗，與此前三起已知 iss |
| L506 | incidents | 🔴 2026-07-25：Fable 5 Max 方案異常追蹤更新——留言數攀升至 42，新增「靜默 |
| L510 | incidents | 🔴 2026-07-24：Fable 5 Max 方案計費/配額執行異常持續逾 4 天未解（追蹤 0 |
| L514 | incidents | 🔴 2026-07-20：南韓用戶收到 $16.7M 帳單疑似故障，與 07-12/13 已證實帳務 |
| L520 | incidents | ✅ 2026-07-20：Fable 5 免費期到期後社群反映存取異常，含官方已證實的 Max 誤判 |
| L525 | incidents | 🔴 2026-07-12/13：Anthropic 證實 1660 萬美元帳務錯誤，稽核發現企業多收 |
| L529 | incidents | 🔴 2026-07-02：Max 升級誤扣費案例 + 客服/退款流程爭議 |
| L535 | archive | ⏸ 2026-06-24：隱私政策更新 + 帳號盜刷事件 |
| L547 | history | 2026-10-31：GitHub Issue #47509 升至 195 👍、70 留言——Tea |
| L551 | history | 2026-10-16：官方 API 定價頁格式改版，Fast mode 拿掉「research pr |
| L557 | history | 2026-10-14：官方 API 定價頁 Managed Agents 範例模型從 Opus 5  |
| L563 | history | 2026-10-10：官方 Plans & Pricing 頁新增「$100–$200/月 API  |
| L570 | history | 2026-10-09：官方說明中心三頁同步改版——usage credits 機制拿掉「需明確同意」 |
| L577 | history | 2026-10-06：Anthropic 擴大 Claude Startups 計畫，媒體稱合格新創 |
| L587 | history | 2026-10-05：Sonnet 4.5 退役日 2026-11-30 經官方查證屬實 |
| L592 | history | 2026-09-28：Claude Sonnet 5.5 上線，牌價 $2/$10 per Mtok |
| L598 | history | 2026-09-23：Claude Code cloud sessions 上線，新用戶最高可領 $ |
| L601 | history | ❓ 2026-09-23：Opus 5.5 上線同時傳「實驗性用量上限重置」機制 |
| L604 | history | 2026-09-22／23：Claude Opus 5.5 發布，牌價 $4/$20 per Mto |
| L610 | history | 2026-09-19：GitHub Issue #47509 互動量持續攀升至 151 👍、46 留 |
| L614 | history | 2026-09-14：官方說明中心確認週用量換軌已如期發生，並澄清不影響 5 小時用量上限 |
| L620 | history | 2026-09-06：GitHub Issue #47509（133 👍、35 留言）——使用者提案 |
| L625 | history | 2026-09-05：官方定價頁再爆大改版（新增110+／移除168+段）；同日媒體稱「Anthro |
| L634 | history | 2026-09-02：官方更正週用量促銷延長至 09-13（非如期於 08-31 終止）；定價文件新 |
| L640 | history | 2026-08-29：官方公告週配額改版——09-14 起標準週配額永久 +25%，但 08-31  |
| L648 | history | 2026-08-21：官方查證更正——3,500 萬美元為 Defender Advantage F |
| L655 | history | 2026-08-21：Techzine 報導 Anthropic 允許企業將 AI 資料存放於自有雲 |
| L661 | history | 2026-08-20：路透社／彭博社（消息人士）報導 Anthropic 計畫調整企業資料保留政策（ |
| L668 | history | 2026-08-19：DevOps.com 稱「暫時性用量提升」當晚到期，與週用量 +50% 促銷延 |
| L673 | history | 2026-08-18：Claude Code 週用量 +50% 促銷再度延長至 2026-08-31 |
| L679 | history | 2026-08-17：印度盧比定價訴求 GitHub Issue #17432 留言數再攀升，Cla |
| L685 | history | 2026-08-10：Claude Sonnet 5 入門定價 $2/$10 永久化，9/1 漲至  |
| L693 | history | 2026-08-11：官方文件補充 usage credits 僅限網頁版開通，pricing 頁確 |
| L698 | history | 2026-08-08：官方 Help Center 查證，07-18～21 四方矛盾報導收斂（✅ 已 |
| L707 | history | 2026-08-01：XDA 報導多數用戶未留意 Fable 5 免費促銷已悄悄改變計費方式（媒體視 |
| L711 | history | 2026-07-29：印度盧比定價訴求 GitHub Issue #17432 互動持續攀升，距官方 |
| L717 | history | 2026-07-24：Claude Opus 5 發布，官方稱定價為 Fable 5 的一半，與此前 |
| L721 | history | 2026-07-21：Reddit 週熱門回顧 Fable 5 免費期延長史，社群觀察指向 Max／ |
| L727 | history | 2026-07-19：免費期到期日當天，Fable 5 存取政策再添兩則標題層級報導，仍未消解矛盾 |
| L733 | history | 2026-07-18：Fable 5 存取政策訊號分歧——「收緊限制」vs「設為永久」同日並存 |
| L739 | history | 2026-07-17：交易員押注 Fable 5 免費期將第四度延長（市場猜測，非官方，07-18  |
| L745 | history | 2026-07-13/14：印度盧比在地化定價正式推出，回應長期社群訴求（重大） |
| L751 | history | 2026-07-12：週用量 +50% 促銷再延長至 7/19，Fable 5 免費期同步順延 |
| L758 | history | 2026-07-10：Wired 報導聚焦「Anthropic 要消費者為 Fable 5 付費」 |
| L762 | history | 2026-07-07～08：Fable 5 免費使用期限再延長 5 天至 7 月 12 日 |
| L766 | history | 2026-07-04：企業版 Claude 支出控管（spend controls）功能上線 |
| L770 | history | 2026-07-03：印度盧比定價需求（✅ 已於 2026-07-13 獲官方回應，見上方 07-1 |
| L775 | history | 2026-07-02：第三方實測確認 Sonnet 5 促銷定價，籲設為預設路由模型 |
| L780 | history | 2026-07-01：Claude Sonnet 5 促銷定價 + Fable 5 計費架構調整 |
| L791 | incidents | 2026-10-30：Reddit 回報 Anthropic 已將 Max5、Max20 方案改名， |
| L797 | incidents | 2026-10-14：官方再次更新《How do usage and length limits w |
| L802 | incidents | 2026-09-06：Mashable 引述 Reddit：多則貼文稱付費方案可用量遠低於宣傳（媒體 |
| L809 | incidents | 2026-08-21：Reddit 回報本次配額重置後 token 分配出現明顯變化（單一貼文，20 |
| L815 | incidents | 2026-08-12：官方文件釐清 usage limits 與 length limits 為兩種 |
| L821 | incidents | 2026-07-22：Reddit 週熱門質疑 Anthropic 宣稱的用量提升未反映於實際體驗（ |
| L825 | incidents | 2026-07-16：週用量配額疑似再度提前重置（單一回報，2026-07-16 指控，已掃日報至  |
| L830 | incidents | 2026-07-07～10：Max 方案額度異常快速耗盡、token 消耗增加 3–5 倍（持續發酵 |
| L840 | archive | 2026-06-30：配額再次縮減（社群反映，Anthropic 無官方公告） |
| L851 | archive | 2026-06-18：Agent SDK 計費持續觀望中，B2B 定價差距引發分析 |
| L857 | archive | 2026-06-17：Ars Technica 深度報導計費暫停始末 |
| L862 | archive | 2026-06-16：Agent SDK 計費政策暫停 + Claude Max 集體訴訟 |
| L868 | archive | 2026-05-21：6/15 計費影響持續發酵，社群替代方案成熟 |
| L875 | archive | 2026-05-17：`claude -p` 計費衝擊持續、多帳號架構合規紅線 |
| L880 | archive | 2026-05-15：6/15 計費變更社群反應、第三方工具衝擊、官方回應 |
| L888 | archive | 2026-05-14：正式宣布 Programmatic 計費分離 |
| L895 | archive | 2026-04-25：第三方 Agentic 工具配額限制 |
| L899 | archive | 原定計費架構設計（2026-05-14 公告，2026-06-16 暫停，保留供歷史參考） |

合計：{'incidents': 38, 'archive': 11, 'history': 41}；母頁不留原檔任何 `####`（archive＝計費切割 9 則＋事故×06、配額×06 各 1 則）。

## 三、砍與結構行（每行一個理由；保命：無一行是懸置標記）

| 行 | 理由 | 原文（前 50 字） |
|---|---|---|
| L71 | 09-13／09-17 時分：兩到期點已過，讀者無用 | > **09-13／09-17 兩個到期時點的時分**（23:59 PT）為多家媒體引官方公告的一致 |
| L72 | 09-13／09-17 時分：兩到期點已過，讀者無用 |  |
| L79 | 與 L200 重複：旗艦分界定義、過渡 credit，L200 為家 | - **旗艦分界的官方定義（2026-07-20 生效）**：Max 方案、Team premium |
| L80 | 與 L200 重複：旗艦分界定義、過渡 credit，L200 為家 | - **Pro／Team standard 過渡 credit（2026-08-22 官方查證，先前 |
| L83 | 與 L214 重複：印度定價，L214 為家 | - **印度在地化定價**：Pro 為 **Rs 2,000／月**（2026-07-13 生效，首 |
| L84 | 06-26 Max 5x 誤植 $50 的更正：方案表已載 $100，更正原文在 archive 2026-06-26 條 | - **Max 5x 月費曾記載矛盾**：06-26 Reddit 貼文誤植 $50，已依 2026 |
| L85 | 與 L215 重複：Karl Kahn 訴訟，L215 為家 | - **Max 20x 用量上限集體訴訟進行中**：Karl Kahn 訴訟（2026-06-16  |
| L164 | ✅ 已查證：每月 API credits，家在方案表「可領優惠」與帳務坑第 1 條 | ／ Max／Team 新增「每月 API credits」 ／ ✅ 2026-10-24 對官方校正 |
| L166 | ✅ 已查證：Free 不含 Opus，家在方案細節 L96 | ／ Free 不含 Opus 5.5、Pro 可用 ／ ✅ 2026-10-17 查證官方方案表：O |
| L168 | 09-13／09-17 時分：到期點已過 | ／ 09-13／09-17 到期時分（23:59 PT） ／ 多家媒體轉述一致，官方說明中心原文未取 |
| L169 | ✅ 已查證：Haiku 5.5 牌價，家在 API 表新列 | ／ Haiku 5.5 精確 $/Mtok 牌價 ／ ✅ 已查證（2026-10-11 官方定價頁） |
| L174 | API credits 歧異已收斂，家在方案表與帳務坑；經過在 history 10-10 條 | **Max／Team 每月 API credits 細節**：用途限 Claude Platform |
| L175 | API credits 歧異已收斂，家在方案表與帳務坑；經過在 history 10-10 條 |  |
| L176 | Haiku 5.5 定價細節，家在 API 表新列與 haiku-5-5#實付成本 | **Haiku 5.5 定價細節**：官方定價頁 2026-10-09 查證已新增「依 prompt |
| L192 | 失效規則：+50% 促銷 09-13 到期；經過在 history 09-02／08-29 條，L219 點名 | - **✅ 2026-09-13 到期（更正：非如期於 08-31 終止）｜Claude Code  |
| L194 | 與 L43 現況重複；官方連結併入現況 | - **✅ 官方說明中心 2026-09-14 確認換軌如期發生，5 小時上限計算方式不受影響**： |
| L297 | %% 舊判準複寫：判準的家是 pages.md | %% 維運備忘：⚖️ 在判決或撤訴前一律留表，官方曾公開承認過的事故也不因時間轉 ⏸（改標 ⛔ 或維 |
| L298 | %% 舊判準複寫：判準的家是 pages.md |  |
| L307 | #38335 列：排序後第 9，移到表下「沒進上表」一行；條目在 09-12／08-14 | ／ Max 方案 session 額度自 3 月起異常加速耗盡 ／ 🔴 未解 ／ 2026-09-1 |
| L318 | 「帳單變多」單路指 cqd → 母頁三路分流取代 | **帳單變多但找不到原因？** 若操作沒有異常、用量卻仍在漲，另一種可能是同樣工作消耗的 token |
| L325 | 「重要政策變動紀錄」h2 與導語：事件流分家到兩子頁，各有自己的 h2 |  |
| L326 | 「重要政策變動紀錄」h2 與導語：事件流分家到兩子頁，各有自己的 h2 | ## 重要政策變動紀錄 |
| L327 | 「重要政策變動紀錄」h2 與導語：事件流分家到兩子頁，各有自己的 h2 |  |
| L328 | 「重要政策變動紀錄」h2 與導語：事件流分家到兩子頁，各有自己的 h2 | 依主題分組，各組內日期倒序（最新在上）。 |
| L329 | 「重要政策變動紀錄」h2 與導語：事件流分家到兩子頁，各有自己的 h2 |  |
| L343 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-11-01；單一社群回報型 🔴（Reddit RSS score |
| L350 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-10-24；單一社群回報型 🔴（77 留言／26 👍），互動量低 |
| L357 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-10-24；單一社群回報型 🔴（39 留言），互動量低於現有 6 |
| L369 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-10-16；單一社群回報型🔴，單一 HN 貼文無跨來源佐證，互動 |
| L376 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-10-11；單一社群回報型🔴，0 留言無跨來源佐證，優先序低於現 |
| L387 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-10-04；單一社群回報型 🔴 %% |
| L393 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 維運備忘：2026-10-04 起列入總表，讓位者為 #5088（單一社群回報型 🔴，最後動態 |
| L400 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 維運備忘：互動量（92 留言）低於總表現有全部 6 列，不觸發換手；未列入總表：表滿載，202 |
| L414 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 維運備忘：互動量與跨來源佐證均已超過 #55982（08-12，77 留言），依留表優先序重返 |
| L421 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 維運備忘：未列入事故總表，表滿載，2026-09-09 %% |
| L451 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入總表：表滿載，2026-10-04 %% |
| L482 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | - %% 維運備忘：未列入事故總表，表滿載，2026-09-06 %% |
| L489 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 維運備忘：未列入事故總表，表滿載，2026-09-12（讓位予 #38335） %% |
| L494 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | %% 未列入事故總表：2026-09-07，讓位給 #16157（表滿載換手） %% |
| L499 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | - %% 維運備忘：未列入事故總表，表滿載，2026-09-06 %% |
| L504 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | - %% 維運備忘：未列入事故總表，表滿載，2026-09-06 %% |
| L533 | %% 舊式「未列入總表」備忘：改由表下讀者可見一行列出，pages.md 新條文 | - %% 維運備忘：未列入事故總表，表滿載，2026-09-06 %% |
| L795 | %% 待查證：verified #1 已答 | %% 待主編查證官方說明中心：Max5／Max20 改名、Max20 5 小時上限是否取消；查實後覆 |
| L849 | %% 凍結到 2027-03-05：使用者 09-06 裁決歸檔，裁決 2 | %% 維運備忘：本節已凍結，只減不增；到期日 2027-03-05（本日 +180 天），屆時複查政 |
| L850 | %% 凍結到 2027-03-05：使用者 09-06 裁決歸檔，裁決 2 |  |

結構行（空行與分隔線）：L177、L319、L324、L344、L351、L358、L370、L377、L388、L394、L401、L415、L422、L452、L540、L844

## 四、cell 閘搬家逐筆（`moves.py --md` 原樣；本機 `--rebuild --allow-grow` 用）

改後子樹命中 62 筆，全部配回 `entities/pricing` 舊基線同類型同錨點、長度不超；其中 57 筆換了頁名（母頁 5 筆留原頁名，不增紅）。配不回 0，改前槽位未用 6（被砍或改短的舊超限條目）。

|---|---|---|---|---|---|---|
| 1 | pricing | 85 | list_item | Free／Pro 功能組成（2026-0 | 241 | entities/pricing 241 |
| 2 | pricing | 90 | list_item | usage credits 僅可在網頁版 | 281 | entities/pricing 281 |
| 3 | pricing | 188 | list_item | ✅ 2026-09-14 已生效（官方文 | 502 | entities/pricing 502 |
| 4 | pricing | 194 | list_item | ✅ 2026-07-20 生效｜旗艦模型 | 526 | entities/pricing 526 |
| 5 | pricing | 195 | list_item | ⚠️ usage credits 開啟後 | 231 | entities/pricing 231 |
| 6 | pricing-history | 154 | list_item | Official Docs（suppor | 390 | entities/pricing 390 |
| 7 | pricing-history | 155 | list_item | Official Docs（platfo | 491 | entities/pricing 491 |
| 8 | pricing-history | 156 | list_item | GitHub Issue #17432  | 338 | entities/pricing 338 |
| 9 | pricing-history | 160 | list_item | 官方公告：Anthropic 官方（Bl | 209 | entities/pricing 209 |
| 10 | pricing-history | 161 | list_item | 對讀者的實際影響（換算） | 202 | entities/pricing 202 |
| 11 | pricing-history | 164 | list_item | 08-31 跟進（非新事實，社群／媒體評 | 349 | entities/pricing 349 |
| 12 | pricing-history | 177 | list_item | 企業資料存放於自有雲端環境——官方已確認 | 280 | entities/pricing 280 |
| 13 | pricing-history | 184 | list_item | 企業資料保留政策調整——官方版本為 EF | 328 | entities/pricing 328 |
| 14 | pricing-history | 193 | list_item | 官方確認再延長：Hacker News  | 287 | entities/pricing 287 |
| 15 | pricing-history | 194 | list_item | 更正本頁既有記錄：本頁 07-12 條目 | 262 | entities/pricing 262 |
| 16 | pricing-history | 195 | list_item | Geeky Gadgets | 345 | entities/pricing 345 |
| 17 | pricing-history | 205 | list_item | 官方公告：Anthropic 官方帳號宣 | 212 | entities/pricing 212 |
| 18 | pricing-history | 219 | list_item | 官方結論（Claude Fable 5  | 371 | entities/pricing 371 |
| 19 | pricing-history | 221 | list_item | 一次性 credit 金額 ✅ 已於 2 | 356 | entities/pricing 356 |
| 20 | pricing-history | 222 | list_item | usage credits 的隱性風險（ | 222 | entities/pricing 222 |
| 21 | pricing-history | 227 | list_item | XDA：免費促銷附帶靜默計費異動，多數用 | 361 | entities/pricing 361 |
| 22 | pricing-history | 232 | list_item | 與已回應事實的張力（非官方政策異動） | 252 | entities/pricing 252 |
| 23 | pricing-history | 237 | list_item | 官方公告：Anthropic 發布 Cl | 507 | entities/pricing 507 |
| 24 | pricing-history | 241 | list_item | 延期歷史彙整 + Max/Team Pr | 367 | entities/pricing 367 |
| 25 | pricing-history | 243 | list_item | 07-17 早期信號（回溯記錄） | 235 | entities/pricing 235 |
| 26 | pricing-history | 247 | list_item | Tech Times | 413 | entities/pricing 413 |
| 27 | pricing-history | 248 | list_item | Dawn：「併入 Max、Team Pr | 269 | entities/pricing 269 |
| 28 | pricing-history | 253 | list_item | 收緊限制方向：Startup Fortu | 486 | entities/pricing 486 |
| 29 | pricing-history | 261 | list_item | 對既有延長序列的意涵（推論） | 285 | entities/pricing 285 |
| 30 | pricing-history | 265 | list_item | 官方推出印度盧比計價，Pro 方案 Rs | 509 | entities/pricing 509 |
| 31 | pricing-history | 266 | list_item | API 定價跨供應商比較難度浮上檯面（T | 224 | entities/pricing 224 |
| 32 | pricing-history | 267 | list_item | 社群對 Fable 5 訂閱去留持續揣測 | 409 | entities/pricing 409 |
| 33 | pricing-history | 271 | list_item | 官方公告：Anthropic 官方公告（ | 220 | entities/pricing 220 |
| 34 | pricing-history | 273 | list_item | 競爭角度（推論）：Google News | 201 | entities/pricing 201 |
| 35 | pricing-history | 278 | list_item | 媒體視角補充，非新政策 | 253 | entities/pricing 253 |
| 36 | pricing-history | 282 | list_item | 官方延長免費期：Times of Ind | 619 | entities/pricing 619 |
| 37 | pricing-history | 286 | list_item | 官方推出企業支出控管功能 | 499 | entities/pricing 499 |
| 38 | pricing-history | 290 | list_item | GitHub Issue 要求 INR  | 422 | entities/pricing 422 |
| 39 | pricing-history | 295 | list_item | dev.to 第一手定價實測 | 284 | entities/pricing 284 |
| 40 | pricing-history | 300 | list_item | Claude Sonnet 5 促銷定價 | 242 | entities/pricing 242 |
| 41 | pricing-history | 301 | list_item | Fable 5 計費架構調整 | 501 | entities/pricing 501 |
| 42 | pricing-incidents | 165 | list_item | 與既有事故的關係：與 08-12 Iss | 210 | entities/pricing 210 |
| 43 | pricing-incidents | 172 | list_item | Hacker News（2026-08- | 224 | entities/pricing 224 |
| 44 | pricing-incidents | 188 | list_item | ✅ 官方答案（2026-08-22 查證 | 598 | entities/pricing 598 |
| 45 | pricing-incidents | 202 | list_item | GitHub Issue #55982（ | 213 | entities/pricing 213 |
| 46 | pricing-incidents | 203 | list_item | 同日 Reddit 疑似相關回報（單一貼 | 219 | entities/pricing 219 |
| 47 | pricing-incidents | 208 | list_item | GitHub Issue #79337  | 378 | entities/pricing 378 |
| 48 | pricing-incidents | 212 | list_item | Reddit r/ClaudeAI 週熱 | 411 | entities/pricing 411 |
| 49 | pricing-incidents | 216 | list_item | GitHub Issue #55266 | 401 | entities/pricing 401 |
| 50 | pricing-incidents | 220 | list_item | GitHub Issue #79337  | 318 | entities/pricing 318 |
| 51 | pricing-incidents | 224 | list_item | GitHub Issue #79337 | 403 | entities/pricing 403 |
| 52 | pricing-incidents | 228 | list_item | KED Global | 203 | entities/pricing 203 |
| 53 | pricing-incidents | 234 | list_item | Reddit r/ClaudeAI | 434 | entities/pricing 434 |
| 54 | pricing-incidents | 235 | list_item | Reddit r/ClaudeAI | 321 | entities/pricing 321 |
| 55 | pricing-incidents | 239 | list_item | 官方證實大規模帳務錯誤 | 455 | entities/pricing 455 |
| 56 | pricing-incidents | 243 | list_item | 長期 Max 用戶反映升級介面誤導、退款 | 455 | entities/pricing 473 |
| 57 | pricing-incidents | 244 | list_item | 企業合作層級（Select vs Pre | 318 | entities/pricing 318 |
| 58 | pricing-incidents | 279 | list_item | 官方 Help Center | 271 | entities/pricing 271 |
| 59 | pricing-incidents | 285 | list_item | r/ClaudeAI 週熱門貼文 | 420 | entities/pricing 420 |
| 60 | pricing-incidents | 289 | list_item | Reddit r/ClaudeCode  | 255 | entities/pricing 255 |
| 61 | pricing-incidents | 294 | list_item | GitHub Issue #38335（ | 242 | entities/pricing 242 |
| 62 | pricing-incidents | 299 | list_item | 正面反例（同期出現） | 201 | entities/pricing 201 |


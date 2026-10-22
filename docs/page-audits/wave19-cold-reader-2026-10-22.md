# Wave 19 冷讀者實測（2026-10-22）

讀者：第一次來、用 Claude Code 寫程式的工程師；只從 `wiki/index.md` 沿 `[[連結]]` 走。跳數：index＝第 1 跳，每開一個新頁 +1；同頁捲動／頁內 Grep 不算。

## 四題結果

| 題 | 路徑 | 跳數 | 結果 |
|---|---|---|---|
| Q1 CLAUDE.md 放什麼／多長／何時加 | index → coding-workflow-guide §1 | 2 | 拿到 |
| Q2 讓它自己驗證、不假完成 | index → coding-workflow-guide §9 → 同頁 §6 | 2 | 拿到 |
| Q3 code review 官方入口與價錢 | index → coding-workflow-guide §5 → enterprise-cost-management「LLM code review 一次多少錢」 | 3 | 半 |
| Q4 先寫規格還是直接開工 | index（無對應列，猜 coding-workflow-guide）→ coding-workflow-guide「我想問的是」表 → §3 | 2 | 拿到（入口靠猜） |

## 每題

**Q1** 答案：小專案一個 root CLAUDE.md；放 Claude 猜不到的指令、與預設不同的 style、測試指令、repo 慣例、架構決策、環境怪癖、陷阱；不放逐檔描述、讀 code 就知道的事、標準慣例、常變資訊。目標 200 行內，逐行問「刪了會不會出錯」。Claude 同一件事錯兩次就寫進去；程序性內容改 skill，必須 100% 執行的改 hook。
- 證據：coding-workflow-guide L125、L143–145、L173–174、L180–189、L135、L193–206
- 卡住：L147「官方兩頁在這裡措辭衝突」——要自己讀調和說法 L148；L585 又說「官方 `/doctor` 建議砍掉」目錄結構，和 L147 歸給 `best-practices` 的說法對不上，不知道到底是哪份文件講的。

**Q2** 答案：要求它出示證據（測試輸出、跑的指令與回傳、截圖）；四級階梯：同 prompt 內自跑檢查 → `/goal` 設可量測完成條件（由另一個模型判定）→ `Stop` hook 跑 script 不過不放行 → 驗證 subagent。`/goal` 評估者不跑工具，要真閉環得靠 Stop hook。
- 證據：coding-workflow-guide L547、L462–469、L557、L208
- 卡住：index L29 指「第 9 段」，但核心步驟在第 6 段（L458–469），第 9 段 L551 才說「其餘見第 6 段」，多繞一次。L465 說 `/goal`「decided by a fresh model」、L557 又說它「不跑工具」——兩處要合起來讀才懂限制。

**Q3** 答案：本機 `/code-review`（一般用量）、`/code-review ultra`（Pro/Max 各 3 次免費，之後 $5–25）、GitHub App Code Review（按 token 扣組織 usage credits，無單價，要自己試跑算平均，Team/Enterprise）、`/security-review`；另兩個是安全掃描外掛。整體基準 $13/開發者/活躍日。
- 證據：coding-workflow-guide L423–432；enterprise-cost-management L100–111
- 卡住：coding-workflow-guide L419「官方有六個入口，而且成本是明碼標價的」與 index L31「官方六個入口＋明價」——但主力 GitHub App 恰好「無固定單價」（L427），Claude Security 那列 L430 全是「—」；「明價」說過頭。GitHub App 需 Team/Enterprise 只寫在第二頁 L100，第一頁表格沒寫。ultrareview「$5–25」看不出由什麼決定。

**Q4** 答案：官方流程 Explore → Plan → Implement → Commit；「diff 一句話講得完就跳過 plan」，方法不確定、改多個檔、不熟該段 code 時才規劃。好規格要自足：點名檔案與介面、寫出不做什麼、結尾附端到端驗證；寫完換新 session 執行。社群 spec-driven 有反證（約 10 倍慢）。切幾塊沒有判準。
- 證據：coding-workflow-guide L353–359、L367–371、L379、L388
- 卡住：index 💻 入口表（L24–35）沒有「規劃／規格」這一列，只能猜去手冊；手冊 L68 的表才找到。

## 入口

全部從 index「💻 開發實務入口」表進：Q1 用 L26、Q2 用 L29、Q3 用 L31（三列字面直接對上問題）。Q4 沒有對應列，從 L26/L29 都指同一本手冊推測它在裡面。

## 分不出差別的兩頁

- `topics/community-tech-tools` vs `topics/skill-interest-watch`（index L27/L28、L115/L116）：都是「社群工具、該裝哪個」，一個「決策表」一個「規模榜」，鉤子要讀兩遍才懂一個講該不該裝、一個講星數。
- `topics/community-tech-patterns` vs `topics/community-pattern-trends`（L117/L119）：「做法總覽」vs「收斂成的方向」，從名字分不出；再加 `community-large-codebase-workflow`（L118）也自稱「主線」。（未開頁，僅依 index 判斷。）

## 百科 vs 雷達

- coding-workflow-guide 是百科（查「怎麼做」），但混進雷達：L40–41 最新動態講五小時額度回應做完（和開發流程無關）、L45–51「本週 coding 亮點」、L283 用量 vs 長度限制、L285 v2.1.299 環境變數、L473–475 特定模型 effort 預設。
- enterprise-cost-management：L98–114 是百科（估法），L34–35 callout 與 L118 起企業案例是雷達/新聞。

## 內部用語外洩

1. index L3–6「角色／收／不收／讀法」「慢變的路由事實」「盤點用 Grep」「見 `wiki/CLAUDE.md`」——寫給維護者。
2. index L104「Topics 頁面本身無「類型」欄位…為刻意設計差異」——讀者不需要知道。
3. index L22「整理後沉澱到這幾頁」「每週整理」——流程語。
4. coding-workflow-guide L36「（重寫 2026-08-08）」。
5. coding-workflow-guide L51「檢查日…其餘候選…屬他頁，不入本段」。
6. coding-workflow-guide L98「`[已補：庫內證據]`」「`[社群面待補]`」「萃取」「條目」——標籤是編輯狀態。
7. coding-workflow-guide L509「本庫 08-29 因 30 天無後續採用回饋已…移除追蹤」。
8. coding-workflow-guide L541「這條診斷順序全站原本沒有一頁明寫…此處補上」——修訂說明。
9. enterprise-cost-management L45、L65、L82 的 `%% 維運備忘 %%`（原始 md 可見；網站若已剝除則不計）。
10. coding-workflow-guide L1–25 frontmatter（`inbound_links`、`signal: 健康`、`attribution_count`）——原始檔第一眼看到的是這些。

## 撐不起的句子

- coding-workflow-guide L529「社群的「CLAUDE.md 管理」是少數達 ✅ 成熟的類別」——無判準無來源，且 L535 同段說這題「全庫零證據」。
- L377「爭議多平台延燒（🔥🔥🔥🔥🔥）」——火焰數無數字。
- L404「規則遵循率從機率性變成 100%」——單一作者，無樣本數。
- L555「顯著降低執行後靜默失敗率」——無數字。
- L111「大幅減少」——無數字。
- L38「官方文件有 185 頁」——L599 自承索引原文已失效。
- enterprise-cost-management L88「實測可削減成本達 90%」——該格無來源。

## 最想改的三件事

1. index 💻 入口表補「改動大要先規劃還是直接做 → coding-workflow-guide 第 3 段」一列；L29 改指「第 6、9 段」。
2. 手冊第 5 段把「review 入口」與「寫時安全掃描」分開，每個入口一行寫清方案門檻＋價錢（GitHub App 直接寫「無單價、Team/Enterprise、試跑估」），拿掉「明價」說法（L419、index L31）。
3. 手冊把雷達內容（L40–51、L283、L285、L473–475）移到頁尾的日期區塊，正文去掉編輯狀態語（L36、L51、L98 標籤、L509、L541）。另：頁內錨點寫法不一致（L48 `#4-實際動手寫--錯誤何時被攔` vs L73 `#4-實際動手寫-錯誤何時被攔已補庫內證據`；L47 vs L74 同樣），疑有壞錨點，未驗證。

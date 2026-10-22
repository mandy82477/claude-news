# Wave 19 冷讀者複驗 — 2026-10-22

讀者設定：第一次來、用 Claude Code 寫程式的工程師；只從 `wiki/index.md` 出發沿 `[[連結]]` 走；index 算第 1 跳，同頁捲動、頁內錨點與頁內 Grep 不算跳。（注意：讀 index 時系統自動帶入了 `wiki/CLAUDE.md`，我沒有拿它來找路。）

## 四題結果

| 題 | 路徑 | 跳數 | 結果 |
|---|---|---|---|
| Q1 CLAUDE.md 放什麼／多長／何時加 | index → coding-workflow-guide §1 | 2 | 拿到 |
| Q2 讓它自己驗證、不假完成 | index → coding-workflow-guide §6＋§9 | 2 | 拿到 |
| Q3 code review 官方入口／一次多少錢 | index → coding-workflow-guide §5（→ enterprise-cost-management「LLM code review 一次多少錢」選讀） | 2（3） | 拿到（2 跳已夠；第 3 跳只補 GitHub App 的估法細節） |
| Q4 先寫規格還是直接開工 | index → coding-workflow-guide §3 | 2 | 拿到 |

## 每題

**Q1** 答案：至少一份 root `CLAUDE.md`；repo 大了就每個 package 各一份，或改用 `.claude/rules/`；多步驟程序做成 skill。放「Claude 猜不到的」（指令、與預設不同的 style、測試指令、慣例、陷阱）；不放逐檔描述、讀 code 就知道的東西。長度：目標 ≤200 行，或逐行問「刪了它會不會出錯」。什麼時候加：同一件事弄錯兩次就加，重複出現的 review 意見也算。
- 證據：guide L116–126、L134–136、L164–165、L171、L180。
- 卡住：L138「官方三頁在這裡說法不一」——要讀完 L138–139 才知道分界是「讀 code 推不推得出」，結論先講、衝突後講會比較好。「何時往裡面加」與 §7「改動之後怎麼讓 CLAUDE.md 跟上」（L65、L480）兩條路由字面很像，我一度以為答案在 §7。

**Q2** 答案：要它出示證據（測試輸出、跑過的指令和回傳值），不要只說成功；驗證階梯有四級：同一個 prompt 叫它自驗 → `/goal` 設可量測的完成條件 → `Stop` hook 跑 script，不過就不放行 → 驗證 subagent。`/goal` 的評估者不跑工具，Claude 沒說出口的它抓不到。
- 證據：guide L447、L451–454、L456、L534、L538、L544。
- 卡住：答案拆在 §6 和 §9，L538 又把 §6 的四級重講了一遍；兩段讀起來是同一件事，我不確定該以哪段為主。L453「連續擋 8 次後 Claude Code 會強制結束，要檢查 `stop_hook_active`」——沒說要檢查什麼、為什麼要檢查。

**Q3** 答案：四個入口——`/code-review`（本機，算一般用量）、`/code-review ultra`（Pro／Max 各 3 次免費，之後每次約 $5–25）、GitHub App Code Review（限 Team／Enterprise，按 token 計，沒有單價）、`/security-review`（本機，算一般用量）。參考值：每位開發者每個活躍日約 $13。
- 證據：guide L410、L414–419、L421；enterprise-cost-management L100–111。
- 卡住：L410「四個 review 入口……另有兩個邊寫邊掃的安全外掛」，但表裡第四列是 `/security-review`，第 423 行又冒出「Claude Security 外掛」——安全類到底哪個算入口、哪個不算，讀完還是糊。L421「每個活躍日約 $13、每月 $150–250」沒有來源也沒有查證日。

**Q4** 答案：官方的判準是「能用一句話描述 diff 就跳過 plan」；改到多個檔、不確定做法、不熟這段 code 時才規劃。typo、改名這類小事直接做。規格要能自足（點名檔案和介面、寫明不做什麼、最後一步是端到端驗證），寫完開新 session 再實作。
- 證據：guide L344、L346、L348、L350、L358、L362。
- 卡住：L379「切幾塊」沒有答案（頁面自己也承認）。L366–377 社群反證很長，對「官方怎麼判斷」這題是多讀的。

## 入口

從 index L26–32 的「💻 開發實務入口」表進來。Q1 走 L26，Q4 走 L27，Q2 走 L30，Q3 走 L32——四列都直接寫「去 coding-workflow-guide 第 N 段」，問句的字面就能對上。L28 也有「它說做完了沒做」，但標的是**社群首選**，L30 標**官方**，題目要官方做法所以選 L30。

## 分不出差別的兩頁（只看 index 的描述，沒點進去）

1. **coding-workflow-guide vs community-large-codebase-workflow**：L26「接手 repo」和 L33「大型 codebase 做法主線」；guide 第 2a 段也在講接手大 repo（guide L52、L231）。
2. **community-tech-tools vs community-tech-patterns**（L116 vs L118）：一個叫「工具」、一個叫「做法」，guide 的社群段兩頁都會引用（L395、L402、L468），從描述看不出哪個問題該去哪頁。

## 百科還是雷達

- coding-workflow-guide 主體是百科（照階段講怎麼做），但夾著雷達：L42–43 的帶日期 callout、L623–629「本週 coding 亮點」、L276 v2.1.299 旗標、L209 v2.1.304、L588–589 部落格附 HN 分數、L460 Sonnet 5.5 low effort 的提醒。
- enterprise-cost-management 混得最嚴重：L98–112 是百科型的計費說明，夾在 L120 起的帶日期企業案例和 L244–300 的時間軸之間。
- index 的 Entities 摘要也混了快變的新聞，例如 L44 的分數、L131 的淨損數字。

## 內部用語外洩

1. index L3–6「角色：地圖／收：／不收：／讀法：整讀」，還指向 `wiki/CLAUDE.md`、`news/`
2. index L105「Topics 頁面本身無「類型」欄位……為刻意設計差異」
3. guide L1–25 frontmatter：`inbound_links`、`attribution_count`、`signal: "健康"`、`pending_*`、`generated_by`
4. guide L6–7 與 L35–36 日期打架：frontmatter 寫 10-17／10-15，正文寫 10-22／10-22
5. guide L87「九段用同一把尺」——講的是評分方法，不是讀者要的內容
6. guide L89「整理自本站社群頁」、L90「本站來源自 2026-04-25 起」
7. guide L139「本頁歸納，官方未明說」——這句是好的，但「本頁」措辭偏編輯視角（輕微）
8. guide L629、L674 的 `%% %%` 維運註解（網站會剝掉，原始 md 看得到）
9. enterprise-cost-management L244、L260 的「[新增具名企業]」「[第三個獨立量化來源]」編輯標籤

## 撐不起的句子

- guide L87「第 6 段社群雖空」——但 L466–472 明明有三則社群做法。
- guide L104「自己 review —— 多一層，不是少一層」——沒有出處，也沒有理由。
- guide L160「這點有實證支持」——依據是 14 個 repo 的觀察，L580 自己也承認樣本有偏差。
- guide L421「每位開發者每個活躍日約 $13、每月 $150–250」——沒有來源也沒有日期。
- guide L256「意思是它不會比你貴」——推論寫成了定論（雖然小節標了「推論」）。

## 最想改的三件事

1. **Q2 收成一個家**：§9 L538 改成一句話加錨點連回 §6，並把「要它出示證據」（L534）搬進 §6 當第 0 級，讀者只讀一段就能拿到答案。
2. **§5 入口表講清楚**：「四個入口」要和表的列對齊；`/security-review` 和 Claude Security 外掛的關係寫成一句；L421 的 $13 補上來源與查證日。
3. **雷達內容移出百科頁**：L42–43 的 callout 和 L623–629「本週亮點」移到 feature-radar，或改成不帶日期的常駐說明；同時對齊 frontmatter 與正文的「最後更新」日期（L6–7 vs L35–36）。

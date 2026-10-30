# 主編官方查證 — 第 20 波 topics/ai-agent-safety（2026-10-30）

查證工具：`gh api`（issues／releases／timeline）、`npm view` dist-tags、WebFetch 官方一手頁（anthropic.com、raw CHANGELOG.md）、CSA 研究註記（二手，標明）、HN Algolia API。行號為 `wiki/topics/ai-agent-safety.md` 2026-10-30 原檔（2,057 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 官方一手 | 判定 |
|---|---|---|---|
| 1 | L62 `bash -c` 包 `rm` 繞過：「2.1.288 已修；stable 標籤仍指 2.1.285（mixed-news 單一來源）」 | CHANGELOG 2.1.287「Fixed a dangerous `rm` … losing its always-ask safeguard」、2.1.288「Fixed a dangerous `rm` … inside a `bash -c` or `sh -c` script」；`npm view @anthropic-ai/claude-code dist-tags` 2026-10-30：stable＝**2.1.308**、latest＝2.1.312、next＝2.1.314 | **過期**。stable 已含修正 ≥22 天。此列應降 ✅ 並依規則退場或改寫為「已修、stable 已含」；同頁 L598（10-17 查證「stable 指 2.1.292」）與 `entities/claude-code` L670（仍寫 2.1.285）三處不一致，冷讀者亦抓到 |
| 2 | L224 shattered.io／The Register：「2.1.311 在 skip permissions 模式下移除 `rm` 阻擋」 | `gh api releases/tags/v2.1.311` 全文無任何 rm 條目；2.1.309「Changed the dangerous `rm` and `rmdir` prompt in bypass permissions mode in the Desktop app and VS Code to **deny the command at once** with a rewrite hint」——方向是更嚴、不是移除 | **與官方 changelog 不符**。該則標 🔎 查無官方且附反證；不得進首屏表 |
| 3 | L458／L464 GitHub #43713 `autoAllowBashIfSandboxed` 失效（10-11 新增；懸置「官方是否承認為 bug」逾期） | Issue **closed 2026-08-19 by bcherny（Anthropic）**：「this was a real gap, and it has been fixed. Since v2.1.139: with `sandbox.enabled: true` and `autoAllowBashIfSandboxed: true`, commands the static analyzer can't fully prove safe … now auto-approve instead of prompting — the sandbox is treated as the security boundary」；41 留言、84 👍；10-11 的「活動」是 bot 自動鎖定 | **懸置可結案 ✅**。10-11 新增那則本身是誤判訊號（抓到的是 bot 鎖定）；條目改寫為「08-19 官方確認已修（v2.1.139 起）」，懸置關閉 |
| 4 | L64 惡意 `.git` 設定檔（❓；「誰會遇到：clone 或開啟他人 repo 的人」） | Manifold Security「GitSpawn」09-02 揭露（CSA 09-04 研究註記，二手）：Claude Code `core.fsmonitor` 變體 **v2.1.196 已修**（2.1.193 仍中）；第二變體（ultrareview）至 2.1.252 **未修**；「a normal `git clone` … does not reproduce this risk」，需 zip／共享資料夾／同步雲端夾帶 `.git`；無在野利用報導 | **部分修補＋受害面寫錯**。狀態 ❓→🔴 部分修補（與 `entities/claude-code` 一致，解冷讀者矛盾）；「誰會遇到」改「以壓縮檔／共享夾收到含 `.git` 的 repo 的人；正常 clone 不受影響」；「你能先做什麼」的「clone 完先看 `.git/config`」改為「解壓或同步來的 repo 先看」 |
| 5 | L65 deny-list 繞過（🔴；「2026-09-11 Show HN 揭露，公開 repo 展示 8 種繞過手法」） | HN Algolia：「Show HN: I bypassed my Claude Code deny-list 8 ways; only an allow-list held」2026-09-11，**1 分、0 留言**，repo danielhagever/agent-guardrails-kit；Anthropic 官方對 deny-list 的立場見 2026-03 回應（二手引述）「deny rules are not designed as a security barrier against adversarial command construction」；50 子命令繞過 2.1.90（04-06）已修 | **來源強度不足以撐首屏列**。事實成立但訊號為 1 分 0 留言；建議「官方擋到哪」補官方 03 月立場（與 Auto 模式同型：不是安全邊界），列是否留首屏交裁決 |
| 6 | L80 CVP 三層（10-06）；「The Hacker News 稱 Glasswing 藉此已找出 129,000 個漏洞，為目前唯一公開量化成效數字」；L542 Glasswing 寫成「資安公司」 | anthropic.com/news/cyber-verification-program（2026-10-06）：三層 Defense／Red Team／Specialized；模型 Opus 5.5、Sonnet 5.5、Mythos 5.1「and new models moving forward」；Defense 開放組織**與個人**（「individual researchers with a track record of reported vulnerabilities」），Red Team「organizations only; individual researchers are not eligible」；數字**官方自述**：Glasswing 夥伴 04–07 月「at least 129,000 verified software vulnerabilities」、Anthropic 自掃開源 04–10 月另 5,500、合計逾 33,000 critical／high；CyScenarioBench（Opus 5.5，50 trials）：無存取全擋、Defense 擋 46/50、Red Team 0 擋 34/50 完成；審核「Defense 數天、Red Team 數週」；區域醫院為 Defense 範例 | **出處升級**：129,000 是官方數字，不是 THN 轉述，且不是「唯一」（另有 5,500／33,000／46-50）。L542「資安公司」**錯**——Project Glasswing 是 Anthropic 自己的計畫，10-08 官方「merged Project Glasswing into our expanded CVP」。Q4「我能申請嗎」官方答案：個人只能 Defense |
| 7 | L485 Cyber Mission（10-09 新增） | anthropic.com/news/anthropic-cyber-mission 2026-10-08：CIDP 11 創始夥伴（Accenture、Booz Allen、CrowdStrike、Deloitte、Dragos、Hitachi、Insane Cyber、Nozomi Networks、Palo Alto Networks、PwC、Rockwell Automation）；OSS Scanner 免費、opt-in、「reports are model-generated and sent without human review」、預期 true-positive >90%、「meant for projects with the capacity to keep up」；官方頁**無** $1,000 責任上限字句（二手傳） | 一致；日期以 10-08 為準。責任上限若頁面有寫須標二手 |
| 8 | L438／L445 自我複製研究（10-13 新增；懸置「月數、9 種硬體全名單、緩解」） | anthropic.com/research/self-replicating-ai 2026-10-12：「months away from being capable enough to self-replicate on commercial IoT devices」「If small models improve at their historical rate, they'll match this capability level by the end of this year」；「a 9B model got inference running on **8 of the 9 hardware types**」（官方文點名 Jetson Nano、Mac、RTX 4090、Orange Pi、Android TV box，未列滿九種）；實機 15 台 $55 Android TV box 跑 Gemma4-26B-A4B；8 節點 redroid 模擬網做端對端；≤30B 可完成多數單步但串不起來；GLM-5.2 端對端 8/8（5 次中 4 次）；緩解：ISP 流量監看、蜜罐、隔離＋通知、製造商安全預設 | **懸置可大部分結案**：月數＝「今年底」、緩解有四條；九種硬體全名單官方未列，這一項留 🔎 查無官方 |
| 9 | L199／L84 GitHub #53223（31 留言、10+ 回報） | open；31 留言；5 👍；labels bug／area:security；updated 10-28 | 一致 |
| 10 | L188 GitHub #81138 email 進 prompt | open；19 留言；75 👍；label bug | 一致（可補 👍 數） |
| 11 | L355 GitHub #84352 CVP 誤擋 201 留言 👍29 | open；201 留言；29 👍 | 一致 |
| 12 | L70 Downloads 資料夾指令檔（❓） | 未找到 Anthropic／OpenAI 回應；僅 Penligent 等二手技術文 | 維持 ❓ |
| 13 | L82 Haiku 5.5 注入防禦 83.2%→7.1% | 10-24 已查證 Transparency Hub | 不重查 |

## 二、考題的官方錨句

- **Q1 提示注入官方擋到哪**：官方立場仍是 Auto 模式與 deny-list 皆「非安全邊界」（08-07 blog；03 月 deny-list 回應）；沙箱是官方指定的安全邊界（#43713 bcherny 原句「the sandbox is treated as the security boundary」）。頁面「拿什麼擋」應以這句為錨。
- **Q2 版本要不要避**：stable 2.1.308 已含 2.1.287／288 的 rm 修正與 2.1.292「PreToolUse hook approvals and auto mode bypassing the permission prompt」安全修正；GitSpawn 第二變體仍開。答案一句：「升到 stable 即可，解壓來的 repo 先看 `.git/config`」。
- **Q3 官方承認的在野濫用**：本頁沒有一條「官方承認」欄；冷讀者指出官方 09 月威脅情報報告住 `anthropic-government-policy` L685。本波未另查該報告（屬鄰頁），交設計者決定是否在 (c) 群加「官方承認」欄並指過去。
- **Q4 CVP 能不能申請**：個人→Defense；組織→三層；審核數天／數週；使用政策與 CVP 關係官方頁未提，L541「使用政策全面收緊」缺一手支撐（冷讀者亦指同頁 10-08 條目推翻它）。

## 三、逾期懸置處置

| 行 | 處置 |
|---|---|
| L385 HTTP header 注入（10-16） | 未查（跨類別非 Claude 專屬）；交設計者依「跨類別」群判去向 |
| L435 The Register 批評（10-14） | 未查；同上，論述層 |
| L445 自我複製（10-13） | **結案大半**：改寫為官方數字（見第 8 列），只留「九種硬體全名單」一項 🔎 |
| L455 MCP SDK 劫持登入（10-13） | 未查到官方 advisory；維持 ❓，複查日往後推 |
| L464 #43713（10-11） | **結案 ✅**（見第 3 列） |

## 四、給設計者三句

1. 首屏 11 列至少三列狀態過期或寫錯（rm 列應 ✅ 退場、`.git` 列改部分修補且受害面縮窄、deny-list 列來源只有 1 分 0 留言）：拆頁前先把表修對，母頁的使命「現在什麼會打到你」才站得住。
2. 「官方擋到哪」有一句一手錨句可用：沙箱是官方指定的安全邊界，Auto 與 deny-list 都不是——這句能同時服務 Q1、Q2，應住母頁而不是任何子頁。
3. (d) 官方防護群的數字全部有一手（CVP 129,000／5,500／33,000／46-50、Cyber Mission 11 夥伴、自我複製 8/9 與 8/8），寫子頁時直接引官方頁，不再經 THN／mixed-news；L542 Glasswing 的錯要一併修。

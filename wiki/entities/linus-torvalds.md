---
page: "entities/linus-torvalds"
kind: "entity"
type: "person"
status: "active"
domain: "👤 人物"
last_updated: "2026-10-18"
last_news_update: "2026-10-18"
status_main: "active"
days_since_news: 2
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 2
inbound_links: 4
attribution_count: 6
attribution_last: "2026-10-18"
top_source: "google-news"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-28"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Linus Torvalds

**類型：** person
**狀態：** active
**領域：** 👤 人物
**身分：** Linux 核心創造者
**與 Anthropic：** 外部觀察者
**職能：** 工程產品
**為何追蹤：** Linux 核心維護者具名使用 Claude Code 開發 kernel 分支
**首次出現：** 2026-10-12
**最後更新：** 2026-10-20
**最後新聞更新：** 2026-10-20

> **最新動態**（2026-10-20）
> Hacker News 轉載 The New Stack 完整報導：這個擱置 18 個月的 page cache 效能瓶頸，10-patch 分支合成測試跑出 23 倍吞吐量提升，但審查發現 race condition；Torvalds 提醒真實環境增益會遠小於測試數字。

---

## 現況

Linus 在送上 Linux 核心信件列表的 patch cover letter 親口寫道：「程式碼、測試程式、前述審查與這份文字的初稿，都是在我的指示下用 LLM coding assistant（Claude Code）完成的，效能測量是在我自己的機器上跑的」（[StartupFortune](https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files/)，2026-10-13）。這個 patch 修的是多執行緒同時讀同一檔案時，頁快取（page cache）的參照計數效能瓶頸。

- **後續**：patch 能否合併進主線、競態條件是否修正，待追蹤
- **2026-10-19**：Hacker News（16分）轉載 The New Stack 完整報導，揭露此 10-patch 分支原為擱置 18 個月的 page cache 效能瓶頸，合成測試跑出 23 倍吞吐量提升；Torvalds 提醒真實環境增益遠小於測試數字
- **2026-10-15**：GBHackers 報導標題稱 Claude Code 協助他處理長期的 kernel 記憶體效能瓶頸（僅標題；[GBHackers News](https://news.google.com/rss/articles/CBMisgFBVV95cUxQekNxOXU5bTUyR2JqM1NfWjFXVjhidjlFY3h2YXdoSFQ1WFQ3NzlIMFhXeW5XQ2dEeWl3SmV5bFN3OWp2X0ZzRWtiOHA4WFVpRndBTGpKNUNjZ0pXZEUtbEE3a0xYVk1GYmhOZ3NCY2JGbmZRTnBCczFYaHloU2dJbk44TmcwR2h4cTB4TjM0aVlfSFI5MVltSDZ6RFJMWmkzRGN0aEg1dTlweTg4SmFYVGNn0gG3AUFVX3lxTE9QOVlvdWg1ZG1Ca2VUUkdJTDJhMEc3aDEwWXZMTTVETmQtVVJTc21aaW1CX3VhSGZfbU0xU00tbW5ma0NkcHhBNHBJVVR6U0ZfZmxxYmY1Znhtb0Z2NWZocGlxWG5rdkNfUU5uUERJVTBDV0x2RnFIR2dzTXVIek9MTjhXY3l3SXBOUHRBajFJTF9JMGJvTVJQM19RVWM1Nlg4LWZKQWJPUXBISjQ2Q2RXdGduMlRidw?oc=5)）
- **2026-10-08／10-14**：布拉格 Linux Maintainers Summit 後，核心社群取消 `Assisted-by` 揭露要求；Torvalds 稱禁 AI 工具「utterly stupid」，如同禁編譯器（[The Register](https://www.theregister.com/ai-and-ml/2026/10/14/linux-kernel-devs-drop-obligatory-confession-of-ai-tool-usage/5303140)、[PC Gamer](https://www.pcgamer.com/software/linux/linux-kernel-drops-ai-contribution-disclosure-rule-as-linus-torvalds-says-banning-the-tech-would-be-utterly-stupid/)、[heise](https://www.heise.de/en/news/Linux-may-drop-AI-code-labels-Torvalds-uses-LLMs-too-11490773.html)）
- **2026-10-14**：審查者在 patch 中發現一處競態條件（race condition）（[The New Stack](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBWNVVYdFVjSlNnZUd1SkhrMk5XQzJ2ajhWLTFGbm5Wbk9HalI2R3BMYjRFQlRITnc0LWxKMWJTeXZod0t6OFBsd1kySWxmaEUzdkRwWFNGd2ZJOHJ3aF9UXw?oc=5)）；同日 36Kr 稱效能提升 3 倍，單一中國媒體轉述、尚待查證（[36Kr](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1Sejh2bUFBMmZGTzR5QWhaSThBRFl2OTNuSVJfdGhnOEQxWGlqY0xPRDNuejVoX1dyVjZsR3NwSEV0NEJGVDBmNTZkU1hXRUVmNmFJ?oc=5)）
- **2026-10-13**：分支整理成 patch 貼上核心信件列表，附上述 cover letter（[StartupFortune](https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files/)）
- **2026-10-12**：重新整理 `torvalds/linux.git` 時意外出現分支 `noref-filemap-read-with-llm`（[Phoronix](https://www.phoronix.com/news/Linus-Torvalds-Claude-Code)）

## 相關議題

- [[entities/claude-code]] — 本次具名使用的工具
- [[topics/community-tech-discussions]] — 重量級開源維護者對 AI 貢獻的規範立場：Torvalds 要求貢獻者懂自己送的程式碼，不禁工具

## 參考來源

- [Linus Torvalds shares his thoughts on Anti-AI coding rules](https://www.reddit.com/r/ClaudeCode/comments/1x8a8e5/linus_torvalds_shares_his_thoughts_on_antiai/) — Reddit／r/ClaudeCode，2026-10-17（轉貼下列報導）
- [Linux kernel devs drop obligatory confession of AI tool usage](https://www.theregister.com/ai-and-ml/2026/10/14/linux-kernel-devs-drop-obligatory-confession-of-ai-tool-usage/5303140) — The Register，2026-10-14
- [Linux kernel drops AI contribution disclosure rule as Linus Torvalds says banning the tech would be utterly stupid](https://www.pcgamer.com/software/linux/linux-kernel-drops-ai-contribution-disclosure-rule-as-linus-torvalds-says-banning-the-tech-would-be-utterly-stupid/) — PC Gamer
- [Linux may drop AI code labels: Torvalds uses LLMs too](https://www.heise.de/en/news/Linux-may-drop-AI-code-labels-Torvalds-uses-LLMs-too-11490773.html) — heise
- [Claude Code Helps Linux Creator Address Longstanding Kernel Memory Performance Bottleneck](https://news.google.com/rss/articles/CBMisgFBVV95cUxQekNxOXU5bTUyR2JqM1NfWjFXVjhidjlFY3h2YXdoSFQ1WFQ3NzlIMFhXeW5XQ2dEeWl3SmV5bFN3OWp2X0ZzRWtiOHA4WFVpRndBTGpKNUNjZ0pXZEUtbEE3a0xYVk1GYmhOZ3NCY2JGbmZRTnBCczFYaHloU2dJbk44TmcwR2h4cTB4TjM0aVlfSFI5MVltSDZ6RFJMWmkzRGN0aEg1dTlweTg4SmFYVGNn0gG3AUFVX3lxTE9QOVlvdWg1ZG1Ca2VUUkdJTDJhMEc3aDEwWXZMTTVETmQtVVJTc21aaW1CX3VhSGZfbU0xU00tbW5ma0NkcHhBNHBJVVR6U0ZfZmxxYmY1Znhtb0Z2NWZocGlxWG5rdkNfUU5uUERJVTBDV0x2RnFIR2dzTXVIek9MTjhXY3l3SXBOUHRBajFJTF9JMGJvTVJQM19RVWM1Nlg4LWZKQWJPUXBISjQ2Q2RXdGduMlRidw?oc=5) — Google News／GBHackers News，2026-10-15
- [Linus Torvalds used Claude Code to rewrite how Linux reads cached files](https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files/) — Hacker News／StartupFortune，2026-10-13
- [Linus Torvalds Embraces AI: Writing Linux Kernel Code with Claude Code Delivers 3X Performance Surge](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1Sejh2bUFBMmZGTzR5QWhaSThBRFl2OTNuSVJfdGhnOEQxWGlqY0xPRDNuejVoX1dyVjZsR3NwSEV0NEJGVDBmNTZkU1hXRUVmNmFJ?oc=5) — Google News／36Kr，2026-10-14
- [Linus Torvalds Working on a Hefty Linux Kernel Improvement with Claude Code](https://www.phoronix.com/news/Linus-Torvalds-Claude-Code) — Hacker News／Phoronix，2026-10-12
- [Torvalds use Claude for bottleneck fix, but race discovered](https://thenewstack.io/torvalds-claude-code-kernel/) — Hacker News（16分）／The New Stack，2026-10-18
- [Quoting Linus Torvalds](https://simonwillison.net/2026/Aug/22/linus-torvalds/) — Blog／Simon Willison，2026-08-22（背景：未點名工具的除錯發言）
- [Linus Torvalds let Claude Code fix the Linux page cache. Then reviewers found a race.](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBWNVVYdFVjSlNnZUd1SkhrMk5XQzJ2ajhWLTFGbm5Wbk9HalI2R3BMYjRFQlRITnc0LWxKMWJTeXZod0t6OFBsd1kySWxmaEUzdkRwWFNGd2ZJOHJ3aF9UXw?oc=5) — Google News／The New Stack，2026-10-14

## 歷史記錄

- 2026-10-19：Hacker News（16分）轉載 The New Stack 完整報導，揭露此 10-patch 分支原為擱置 18 個月的 page cache 效能瓶頸，合成測試跑出 23 倍吞吐量提升，Torvalds 提醒真實環境增益遠小於測試數字（來源：Hacker News／The New Stack）
- 2026-10-17：r/ClaudeCode 轉貼 Torvalds 對反 AI 編碼規則的表態，原始脈絡見下條（2026-10-18 查證；來源：Reddit／r/ClaudeCode、The Register）
- 2026-10-15：GBHackers 報導標題稱 Claude Code 協助 Linus 處理長期的 kernel 記憶體效能瓶頸（僅標題）（來源：Google News／GBHackers News）
- 2026-10-14：核心社群取消 `Assisted-by` 揭露要求，Torvalds 稱禁 AI 工具「utterly stupid」，如同禁編譯器或文字編輯器（來源：The Register、PC Gamer、heise）
- 2026-10-14：這個已送上 Linux 核心信件列表的 Claude Code 協作分支，審查者發現其中一處競態條件（race condition），能否進主線待追蹤修正是否補上（來源：Google News／The New Stack）
- 2026-10-14：❓ **待查證**（標 2026-10-14｜查 36Kr、3X Performance Surge）｜**36Kr 稱 kernel 分支效能提升達 3 倍**：36Kr 報導稱該 Claude Code 協作分支效能實測提升達 3 倍，為單一中國媒體轉述，尚未見 Linus 本人或其他來源證實具體數字（來源：Google News／36Kr）
- 2026-10-13：這個 Claude Code 協作分支正式整理成 patch 貼上 Linux 核心信件列表，Linus 在 cover letter 親自寫下程式碼、測試程式與效能測量皆在自己指示下用 Claude Code 完成、在自己機器上測得（來源：Hacker News／StartupFortune）
- 2026-10-12：重新整理 `torvalds/linux.git` 時意外發現新分支 `noref-filemap-read-with-llm`；Phoronix 判讀為使用 Claude Code 開發 kernel 新功能，與他過去僅在主線推 master 的習慣不同（來源：Hacker News／Phoronix）
- 2026-10-08：布拉格 Linux Maintainers Summit 討論 AI 貢獻；Torvalds 要求貢獻者懂自己送的程式碼，人類仍須負 `Signed-off-by` 責任，AI agent 不能簽（來源：The Register、heise）
- 2026-08-22：Simon Willison 部落格轉引其 commit 訊息，稱某次「地獄等級」除錯過程主要靠 AI 完成繁瑣工作，未點名具體工具（來源：Blog／Simon Willison）

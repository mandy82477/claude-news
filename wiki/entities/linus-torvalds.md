---
page: "entities/linus-torvalds"
kind: "entity"
type: "person"
status: "active"
domain: "👤 人物"
last_updated: "2026-10-15"
last_news_update: "2026-10-15"
status_main: "active"
days_since_news: 1
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 1
inbound_links: 2
attribution_count: 3
attribution_last: "2026-10-15"
top_source: "google-news"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-28"
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
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
**最後更新：** 2026-10-15
**最後新聞更新：** 2026-10-15

> **審查揭露競態條件**（2026-10-15）
> 送上核心信件列表的 Claude Code 協作 patch，審查者發現其中一處競態條件，能否進主線待追蹤修正。

---

## 現況

這個已送上 Linux 核心信件列表的 Claude Code 協作分支，審查者發現其中一處競態條件（race condition），能否進主線待追蹤修正是否補上（2026-10-14，The New Stack）。

36Kr 報導稱這個分支效能實測提升達 3 倍，為單一中國媒體轉述，尚無 Linus 本人或其他來源佐證這個數字（2026-10-14，詳見下方歷史記錄的懸置標記）。

## 相關議題

- [[entities/claude-code]] — 本次具名使用的工具

## 參考來源

- [Linus Torvalds used Claude Code to rewrite how Linux reads cached files](https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files/) — Hacker News／StartupFortune，2026-10-13
- [Linus Torvalds Embraces AI: Writing Linux Kernel Code with Claude Code Delivers 3X Performance Surge](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1Sejh2bUFBMmZGTzR5QWhaSThBRFl2OTNuSVJfdGhnOEQxWGlqY0xPRDNuejVoX1dyVjZsR3NwSEV0NEJGVDBmNTZkU1hXRUVmNmFJ?oc=5) — Google News／36Kr，2026-10-14
- [Linus Torvalds Working on a Hefty Linux Kernel Improvement with Claude Code](https://www.phoronix.com/news/Linus-Torvalds-Claude-Code) — Hacker News／Phoronix，2026-10-12
- [Quoting Linus Torvalds](https://simonwillison.net/2026/Aug/22/linus-torvalds/) — Blog／Simon Willison，2026-08-22（背景：未點名工具的除錯發言）
- [Linus Torvalds let Claude Code fix the Linux page cache. Then reviewers found a race.](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBWNVVYdFVjSlNnZUd1SkhrMk5XQzJ2ajhWLTFGbm5Wbk9HalI2R3BMYjRFQlRITnc0LWxKMWJTeXZod0t6OFBsd1kySWxmaEUzdkRwWFNGd2ZJOHJ3aF9UXw?oc=5) — Google News／The New Stack，2026-10-14

## 歷史記錄

- 2026-10-14：這個已送上 Linux 核心信件列表的 Claude Code 協作分支，審查者發現其中一處競態條件（race condition），能否進主線待追蹤修正是否補上（來源：Google News／The New Stack）
- 2026-10-14：❓ **待查證**（標 2026-10-14｜查 36Kr、3X Performance Surge）｜**36Kr 稱 kernel 分支效能提升達 3 倍**：36Kr 報導稱該 Claude Code 協作分支效能實測提升達 3 倍，為單一中國媒體轉述，尚未見 Linus 本人或其他來源證實具體數字（來源：Google News／36Kr）
- 2026-10-13：這個 Claude Code 協作分支正式整理成 patch 貼上 Linux 核心信件列表，Linus 在 cover letter 親自寫下程式碼、測試程式與效能測量皆在自己指示下用 Claude Code 完成、在自己機器上測得（來源：Hacker News／StartupFortune）
- 2026-10-12：重新整理 `torvalds/linux.git` 時意外發現新分支 `noref-filemap-read-with-llm`；Phoronix 判讀為使用 Claude Code 開發 kernel 新功能，與他過去僅在主線推 master 的習慣不同（來源：Hacker News／Phoronix）
- 2026-08-22：Simon Willison 部落格轉引其 commit 訊息，稱某次「地獄等級」除錯過程主要靠 AI 完成繁瑣工作，未點名具體工具（來源：Blog／Simon Willison）

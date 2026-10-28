## 開發實務 記者回報
基準線：113fc54 → 696d26f
候選：8 筆（entities/claude-code ×2、topics/ai-agent-safety ×1、topics/community-guardrails ×2、topics/community-memory ×1、topics/community-tech-discussions ×1、topics/anthropic-business ×1）

補充說明（供主編參考，非回報契約必填）：
- 今日 `data/ingest-packets/2026-10-28/` 無「開發實務.md」，只做每日撿候選（daily.md 步驟 1、2、4、5），未動 `wiki/topics/coding-workflow-guide.md` 整頁，步驟 3 不適用。
- 8 筆候選已 append 進 `data/devpractice-candidates.jsonl`，等週更 `devpractice_diff.py pending` 落地；基準線已用 `devpractice_diff.py mark` 推進到 HEAD（696d26ff6f95dbfbb84ff1977dd57ac8d5b5daa6）。
- 盤點範圍：今日基準線以來 wiki/ 新增共約 70 個頁面區塊（entities/*、topics/* 的 frontmatter 計數列與正文）；排除純 `days_since_news`／`inbound_links` 等 frontmatter 計數更新、互動數（留言／讚）成長但事實不變的既有已知問題列（如 #53247 Windows Silo、#76248 git proxy、#44243 Slack 多 workspace，均查證過往已記錄，僅計數更新非新事實）、與 coding 無關的融資／人事／政策／模型評測／競品動態、單一來源 0 互動且無法對應到可行動建議的薄證據（如 opus-5-5 分類器誤觸、Reddit 德文切換類推）。
- 已收 8 筆理由：#97074（claude -p 額度耗用倍率，成本實務）、v2.1.311 疑似移除 skip-permissions 下 rm 阻擋（❓ 待查證但直接影響安全操作假設）、Downloads 資料夾攻擊面二次來源確認（可行動緩解）、兩則規格驅動開發／Hooks自動化社群工具變體、一則記憶管理工具、一則 Simon Willison 模型能力拐點觀察、一則官方隱私文件按讚可能進訓練（直接行為指引）。

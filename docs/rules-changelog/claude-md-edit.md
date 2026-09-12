# .claude/rules/claude-md-edit.md 沿革（教訓存檔）

本檔是 `.claude/rules/claude-md-edit.md` 的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

**2026-09-04**（機械契約字串住固定區，立法依據）：該日 prompt review 六個 🔴 有五個是「規格改了、機器沒跟」——契約字串散在散文裡，改文案順手就改斷（聚焦連結格式、`素材涵蓋窗`、判準凍結比對各中一次）。字串住固定表＋registry 雙看守後，這類失效在 commit 前就會紅。初版配對過度假設 `scan_open_forecasts` 吃小標，實查只吃表頭，已修正——契約登記本身也要對照實況，不能照規格想像。

**2026-09-12**（rules 檔必須有 `paths:`）：實測無 `paths:` 的規則檔會在每個 session 無條件載入——當時 `.claude/rules/` 有 19 檔合計 244 KB，為根目錄主設定檔的 21 倍，且全部無範圍。處置：記者規則搬至 `.claude/reporter-rules/`（明文 Read、不需 `paths:`），留在 `.claude/rules/` 的三檔各加 `paths:`，`src/tests/test_rules_frontmatter.py` 看守。同日本檔自身也依「教訓敘事進沿革檔」條文把兩段敘事移到這裡，並補上條文標記約定與 Stop hook 說明。

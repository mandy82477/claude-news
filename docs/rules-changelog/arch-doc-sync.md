# `.claude/skills/arch-doc-sync/` 沿革（教訓存檔）

本檔是架構文件同步流程的歷史敘事，不是待執行規則；SKILL.md 條文處的「沿革檔 YYYY-MM-DD」皆指本檔對應段。

## 2026-09-13

`/arch-doc-sync` 從舊 command 檔 .claude/commands/arch-doc-sync.md 轉成 skill（`.claude/skills/arch-doc-sync/`）。步驟語意與判準逐字不動，只換家：三份文件分工表、`.dgm-*`／`.event-*` class 契約、驗證 A／B 檢查表移入同目錄 `contract.md`；原「為什麼需要這個 skill」段、六條不變式的立法理由與「快速心法」移入本檔，SKILL.md 每條不變式只留判準句＋一句指本檔。

## 2026-07-05/06

**為什麼需要這個流程：** 架構文件會過期，而過期的架構圖比沒有更糟（會誤導）。2026-07-05/06 重建這套文件時踩過的坑，全部固化成流程的強制檢查，下次不必重新流血。

六條不變式的由來：

1. **charset meta 必備**——漏 `<meta charset="utf-8">` 會整頁中文亂碼，而且**不產生 console error**：肉眼不看那一頁就永遠不知道，機械檢查是唯一的網。
2. **設計 token 單一來源**——顏色／字體／圓角寫死在 HTML 裡，兩頁就會各自漂移；集中在 `docs/architecture.css` 的 `:root` 才能一改兩頁同步。
3. **獨立驗證**——class 名打錯時樣式會 fallback 成無樣式，版面「看起來只是有點怪」，肉眼與「已完成」回報都擋不住；必須親自查渲染後的實際值。
4. **派工要重驗最終狀態**——併發／委派會讓中間狀態與最終狀態不一致，當時曾發生兩個 agent 並行覆蓋同一檔；故機械檢查與驗證不能也外包，主 session 要重驗 disk 上的最終檔。
5. **先事實來源、後 HTML**——`src/DesignDocument/Design Diagram.md` 是現況的單一事實來源，HTML 是它的視圖；反過來改會讓兩者漂移且無從判定誰對。
6. **原 React 備份唯讀**——`docs/architecture-evolution-react.bak.html` 是舊版備份，拿它當範本會把已淘汰的結構複製回現行頁。

**快速心法：** 系統變了 → 先問「這是**現況變動**還是**里程碑**？」→ 改 Design Diagram.md → current 頁跟上（里程碑才動 evolution 頁）→ 五項強制檢查 → commit。設計要動只碰 `docs/architecture.css`。

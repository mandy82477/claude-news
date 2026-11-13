"""主控台編碼防護：stdout／stderr 編不出的字元改以 `?` 取代，而不是拋 UnicodeEncodeError。

根因：Windows 預設主控台編碼是 cp950，編不出 emoji（🟠、⏰、⚠️ 等）與部分符號（≥、≤）。
腳本的輸出又大量含 emoji（報告標記）或 wiki 內容（頁名、警告文字）。print 當下拋例外：
輕則整支腳本在印報告時當掉（2026-11-14 實測 scan_expiring_deadlines.py 每日 Step 3 截止日
複查本機當掉＝複查靜默跳過），重則被外層 `except Exception` 吞成別的錯誤
（2026-11-08 build_web 把 print 失敗誤報成「頁面解析失敗」）。

用法：在腳本入口（`if __name__ == "__main__":` 內或 main() 開頭）呼叫一次 make_console_safe()。
不依賴 PYTHONUTF8／PYTHONIOENCODING 環境變數，不要求使用者改設定。
只改「編不出時怎麼辦」，不改編碼本身，所以不影響能正常編碼的輸出。
"""
import sys


def make_console_safe() -> None:
    """stdout／stderr 改成「編不出的字元以 ? 取代」。沒有 reconfigure 的串流（被測試換成
    StringIO 等）原樣放過。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")

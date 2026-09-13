"""`gen_wiki_frontmatter.py` 的旗標看守——不認得的旗標不得變成一次全庫寫入。

死因（2026-09-13）：有記者想看說明而跑 `gen_wiki_frontmatter.py --help`。本檔當時
以 `"--dry-run" in argv` 這種子字串比對讀參數，既沒有 `--help`、也不擋未知參數，
於是 `--help` 走到預設路徑，把 76 個頁面的 frontmatter 全庫改寫（事後逐一還原）。

這是一類 bug，不是一次事故：`--dry-rnu` 打錯一個字母、`--page xxx` 這種不存在的
模式，全都會被靜默當成「照預設跑」。**一個會寫入的腳本，把打錯的旗標當成同意，
是最壞的預設。** 本測試釘住兩件事：`--help` 只印說明、未知旗標要擋下，兩者都不寫入。
"""
import io
import unittest
from unittest.mock import patch

from tests._helpers import load_script_module

gen = load_script_module("gen_wiki_frontmatter")


class _Capture(io.StringIO):
    def flush(self):  # noqa: D102 - StringIO.flush 已足夠，這裡只是明示介面
        pass


class TestFlagGuard(unittest.TestCase):
    def _run(self, argv):
        """跑 main()，並確保它沒有走到任何寫入路徑。

        寫入路徑一律經過 Path.write_text；把它換成會炸的替身，
        真的寫下去就會在這裡失敗，而不是安靜地改壞整個 wiki。
        """
        buf = _Capture()

        def _explode(*a, **kw):
            raise AssertionError("不該寫入任何檔案")

        with patch.object(gen, "_stdout", return_value=buf), \
             patch("pathlib.Path.write_text", _explode):
            code = gen.main(argv)
        return code, buf.getvalue()

    def test_help_prints_usage_and_writes_nothing(self):
        for flag in ("--help", "-h"):
            with self.subTest(flag=flag):
                code, out = self._run(["gen_wiki_frontmatter.py", flag])
                self.assertEqual(code, 0, f"{flag} 應以 0 結束")
                self.assertIn("用法：", out)
                self.assertIn("--dry-run", out, "說明必須告訴讀者有唯讀模式可用")

    def test_unknown_flag_is_rejected_not_silently_ignored(self):
        code, out = self._run(["gen_wiki_frontmatter.py", "--dry-rnu"])
        self.assertEqual(code, 2, "未知旗標必須以非 0 結束，否則打錯字＝全庫寫入")
        self.assertIn("未知參數", out)
        self.assertIn("--dry-rnu", out, "要指名是哪個旗標不認得，不能只說『錯了』")

    def test_usage_states_that_the_default_writes_everything(self):
        """說明本身要講清楚預設會寫入——這才是當初那位記者需要看到的那句。"""
        _, out = self._run(["gen_wiki_frontmatter.py", "--help"])
        self.assertIn("寫入全庫", out)


if __name__ == "__main__":
    unittest.main()

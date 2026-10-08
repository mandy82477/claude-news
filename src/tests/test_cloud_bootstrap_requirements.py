"""cloud_bootstrap 的套件清單要跟 src/requirements_news.txt 同步。

2026-10-07 雲端映像不再預裝 requests；bootstrap 當時寫死只裝 dotenv、feedparser，
`--confirm-digest` 撞 ModuleNotFoundError、測試大片紅、網站跳過。守兩件事：
需求檔每一項都會被檢查／安裝，缺一項時真的會呼叫 pip 裝它。
"""
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
import cloud_bootstrap as cb  # noqa: E402


class RequirementsTest(unittest.TestCase):
    def test_every_requirement_is_covered(self):
        specs = [s for _, s in cb.PIP_PACKAGES]
        lines = [l.split("#")[0].strip() for l in cb.REQUIREMENTS.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(specs, [l for l in lines if l])
        names = dict((s.split(">")[0], m) for m, s in cb.PIP_PACKAGES)
        self.assertEqual(names["python-dotenv"], "dotenv")
        self.assertEqual(names["requests"], "requests")

    def test_parses_specs_comments_and_extras(self):
        with TemporaryDirectory() as d:
            p = Path(d) / "req.txt"
            p.write_text("# c\nfoo-bar>=1.0  # why\nbaz[x]==2\n\nQux\n", encoding="utf-8")
            self.assertEqual(cb._requirements(p), [("foo_bar", "foo-bar>=1.0"), ("baz", "baz[x]==2"), ("qux", "Qux")])
            self.assertEqual(cb._requirements(Path(d) / "missing.txt")[0][0], "dotenv")

    def test_missing_module_is_installed(self):
        calls = []
        with mock.patch.object(cb, "PIP_PACKAGES", [("requests", "requests>=2.31.0")]), \
             mock.patch.object(cb, "_have", side_effect=[False, True]), \
             mock.patch.object(cb, "_pip", side_effect=lambda *a: calls.append(a) or True), \
             mock.patch("builtins.print"):
            cb.ensure_pip_packages()
        self.assertEqual(calls, [("install", "requests>=2.31.0")])


if __name__ == "__main__":
    unittest.main()

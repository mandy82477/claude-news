"""列表卡片的「最新一句」不得帶懸置標記的機器括號。

`latest_headline()` 取時序首條當卡片主文；時序條目若是待查證項，前面會掛
`⟨Q-nn⟩ ❓ 待查證（標 日期｜查 關鍵字｜複 日期）：`——括號是給掃描器與記者的 metadata，
2026-10-03 在「你可能也想看」卡片上整句露出。讀者只需要「待查證」＋題目。
同時釘住 parse_wiki 的 pageRole：前端用它分流子頁（封存／併回殼／真子題）。
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("build_web", REPO_ROOT / "scripts" / "build_web.py")
build_web = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_web)


class TestLatestHeadline(unittest.TestCase):
    def test_strips_pending_machine_brackets(self):
        raw = ("# 頁\n\n## 歷史記錄\n\n"
               "- 2026-09-23：⟨Q-04⟩ ❓ **待查證**（標 2026-09-21｜查 Opus 5.5｜複 2026-10-05）｜"
               "單一部落格稱 Opus 5.5 週二發布\n")
        h = build_web.latest_headline(raw)
        self.assertNotIn("⟨Q-", h)
        self.assertNotIn("（標 ", h)
        self.assertIn("待查證", h)
        self.assertIn("單一部落格稱 Opus 5.5 週二發布", h)

    def test_plain_headline_untouched(self):
        raw = "# 頁\n\n## 歷史記錄\n\n- 2026-09-01：v2.0 發布（來源：Changelog）\n"
        self.assertEqual(build_web.latest_headline(raw), "v2.0 發布（來源：Changelog）")


class TestPageRole(unittest.TestCase):
    def _parse(self, stem: str, body: str) -> dict:
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / f"{stem}.md"
            f.write_text(body, encoding="utf-8")
            return build_web.parse_wiki(f, "entity")

    def test_roles(self):
        head = "# 頁\n\n**領域：** 👤 人物\n**上層：** [[topics/hub]]\n"
        self.assertEqual(self._parse("x", head + "\n已併回 [[topics/hub]]。\n")["pageRole"], "redirect")
        self.assertEqual(self._parse("x-archive", head + "\n封存。\n")["pageRole"], "archive")
        self.assertEqual(self._parse("x", head + "\n正文。\n")["pageRole"], "child")
        self.assertEqual(self._parse("x", "# 頁\n\n**領域：** 👤 人物\n\n正文。\n")["pageRole"], "")


if __name__ == "__main__":
    unittest.main()

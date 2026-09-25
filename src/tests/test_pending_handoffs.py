"""Tests for scripts/pending_handoffs.py — 記者間轉知帳本。

守的是四件事：開立冪等、結案是 append 不是改寫、只列 open、派工附件無則印「無」。
"""
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

ph = load_script_module("pending_handoffs")


class TestLedger(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.path = Path(self._tmp.name) / "pending-handoffs.jsonl"

    def tearDown(self):
        self._tmp.cleanup()

    def test_open_is_idempotent_and_close_appends(self):
        a = ph.open_handoff("社群", "功能", "topics/official-community-gap", "評估矩陣新增列：X",
                            opened="2026-08-15", path=self.path)
        b = ph.open_handoff("社群", "功能", "topics/official-community-gap", "評估矩陣新增列：X",
                            opened="2026-08-15", path=self.path)
        self.assertEqual(a, b)
        self.assertEqual(len(self.path.read_text(encoding="utf-8").splitlines()), 1)
        self.assertEqual(len(ph.open_items(self.path)), 1)

        ph.close_handoff(a, "功能", "已補列", closed="2026-08-16", path=self.path)
        lines = self.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2, "結案必須 append 新行，不可改寫開立行")
        self.assertEqual(ph.open_items(self.path), [])
        self.assertEqual(ph.load(self.path)[a]["status"], "done")
        with self.assertRaises(SystemExit):
            ph.close_handoff(a, "功能", "再結一次", path=self.path)

    def test_same_category_rejected(self):
        with self.assertRaises(SystemExit):
            ph.open_handoff("功能", "功能", "x", "n", path=self.path)

    def test_render_groups_by_target_and_flags_stale(self):
        self.assertEqual(ph.render([]), "無")
        ph.open_handoff("安全政策", "功能", "entities/claude-code", "issue #1 併入已知問題",
                        opened="2026-07-20", path=self.path)
        ph.open_handoff("模型", "商業", "entities/pricing", "新模型定價待記", opened="2026-08-14",
                        path=self.path)
        text = ph.render(ph.open_items(self.path), today=date(2026, 8, 15))
        self.assertIn("→ 功能 記者", text)
        self.assertIn("→ 商業 記者", text)
        self.assertIn("⚠️ 逾 14 天", text)
        self.assertEqual(text.count("⚠️ 逾 14 天"), 1)
        only = ph.render(ph.open_items(self.path, to="人物"))
        self.assertEqual(only, "無")


INDEX = """## Entities

| 頁面 | 類型 | 領域 | 狀態 | 摘要 |
|------|------|------|------|------|
| [[entities/opus-5-5]] | model | 🤖 模型 | active | x |

## Topics

| 頁面 | 領域 | 狀態 | 摘要 |
|------|------|------|------|
| [[topics/model-task-leaderboard]] | 🤖 模型 | ongoing | x |
| [[topics/anthropic-government-policy]] | 🏛️ 政策/安全 | ongoing | x |
| [[topics/market-signals]] | 💼 商業 | ongoing | x |
"""


class TestOwner(unittest.TestCase):
    """open 的負責人驗證：index 領域欄 → 類別；子頁沿 frontmatter parent 往上。"""

    def setUp(self):
        self._tmp = TemporaryDirectory()
        root = Path(self._tmp.name)
        self.index = root / "index.md"
        self.index.write_text(INDEX, encoding="utf-8")
        self.wiki = root
        (root / "entities").mkdir()
        (root / "entities" / "chris-olah.md").write_text(
            '---\npage: "entities/chris-olah"\nparent: "topics/anthropic-government-policy"\n---\n# x\n',
            encoding="utf-8")
        (root / "entities" / "orphan.md").write_text("---\nparent: null\n---\n# x\n", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def owner(self, page):
        return ph.owner_of(page, index_path=self.index, wiki_dir=self.wiki)[0]

    def test_index_domain_column_maps_to_category(self):
        self.assertEqual(self.owner("topics/model-task-leaderboard"), "模型")
        self.assertEqual(self.owner("entities/opus-5-5"), "模型")
        self.assertEqual(self.owner("topics/anthropic-government-policy"), "安全政策")

    def test_page_spelling_is_normalized(self):
        for spelling in ("wiki/topics/model-task-leaderboard.md", "[[topics/model-task-leaderboard]]",
                         "topics/model-task-leaderboard#節"):
            self.assertEqual(self.owner(spelling), "模型", spelling)

    def test_child_page_falls_back_to_parent(self):
        owner, trail = ph.owner_of("entities/chris-olah", index_path=self.index, wiki_dir=self.wiki)
        self.assertEqual(owner, "安全政策")
        self.assertEqual(trail, ["entities/chris-olah", "topics/anthropic-government-policy"])

    def test_override_and_unknown(self):
        self.assertEqual(self.owner("topics/market-signals"), "投資分析")
        self.assertIsNone(self.owner("entities/orphan"))
        self.assertIsNone(self.owner("entities/does-not-exist"))

    def test_real_index_model_task_leaderboard_is_models(self):
        """09-24 事故頁：模型記者把它轉給功能，但領域欄歸模型。"""
        self.assertEqual(ph.owner_of("topics/model-task-leaderboard")[0], "模型")


class TestOpenCli(unittest.TestCase):
    """CLI 一律 --dry-run 或被擋下，不寫真帳本。"""

    def run_cli(self, *args):
        import contextlib
        import io
        err, out = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            code = ph.main(["open", *args])
        return code, out.getvalue(), err.getvalue()

    def test_wrong_owner_exits_1_and_names_owner(self):
        before = ph.LEDGER.read_bytes() if ph.LEDGER.exists() else b""
        code, _, err = self.run_cli("--from", "模型", "--to", "功能", "--page",
                                    "topics/model-task-leaderboard", "--note", "x")
        self.assertEqual(code, 1)
        self.assertIn("「模型」", err)
        after = ph.LEDGER.read_bytes() if ph.LEDGER.exists() else b""
        self.assertEqual(before, after, "驗證失敗不可寫帳本")

    def test_right_owner_dry_run_passes(self):
        code, out, _ = self.run_cli("--from", "功能", "--to", "模型", "--page",
                                    "topics/model-task-leaderboard", "--note", "x", "--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("dry-run", out)

    def test_force_requires_reason(self):
        code, _, err = self.run_cli("--from", "模型", "--to", "功能", "--page",
                                    "topics/model-task-leaderboard", "--note", "x", "--force", "--dry-run")
        self.assertEqual(code, 1)
        self.assertIn("--reason", err)
        code, _, _ = self.run_cli("--from", "模型", "--to", "功能", "--page", "topics/model-task-leaderboard",
                                  "--note", "x", "--force", "--reason", "新建頁", "--dry-run")
        self.assertEqual(code, 0)

    def test_force_reason_written_to_ledger(self):
        with TemporaryDirectory() as d:
            p = Path(d) / "l.jsonl"
            hid = ph.open_handoff("商業", "人物", "entities/new", "建頁", opened="2026-09-25", path=p,
                                  extra={"force_reason": "新建頁"})
            self.assertEqual(ph.load(p)[hid]["force_reason"], "新建頁")


if __name__ == "__main__":
    unittest.main()

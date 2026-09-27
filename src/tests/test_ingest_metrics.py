"""ingest 量測帳本：每位記者的輪數／token／讀了什麼，改動前後要比得起來。

夾具 fixtures/ingest_metrics/projects/sess-fixture/subagents/ 是凍結的迷你 transcript，
記錄形狀照真實 subagent transcript（一次 API 回應拆成多筆 assistant 記錄、同份 usage）：
- agent-features：功能記者 09-26，30 行，含 rule／wiki 各種讀法、3 次編輯、3 則 hook 回饋
- agent-classify：分類複核記者，用「今日日期」寫法
- agent-audit：同目錄的頁面健檢 agent，prompt 內有日期也提到「功能」記者——不得被收
- agent-models-0925：別日的模型記者——不得被收進 09-26
每條測試對應一個改壞就該紅的點。
"""
import hashlib
import io
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tests._helpers import FIXTURES_DIR, REPO_ROOT, load_script_module

mod = load_script_module("ingest_metrics")

PROJECTS = FIXTURES_DIR / "ingest_metrics" / "projects"
SUB = PROJECTS / "sess-fixture" / "subagents"
D = "2026-09-26"


def _lines(rel):
    return len((REPO_ROOT / rel).read_text(encoding="utf-8").splitlines())


def _run(*argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = mod.main(list(argv))
    return code, buf.getvalue()


def _features(rows):
    [r] = [r for r in rows if r["role"] == "功能"]
    return r


class TestIdentify(unittest.TestCase):
    def test_only_reporters_on_date(self):
        rows = mod.collect(D, [SUB])
        self.assertEqual(sorted(r["agent_file"] for r in rows),
                         ["agent-classify.jsonl", "agent-features.jsonl"])

    def test_role_names(self):
        self.assertEqual(mod.identify("你是 CLAUDE_NEWS wiki 的「開發實務（devpractice）」記者。\n今日日報日期：2026-09-26"),
                         ("devpractice", D))
        self.assertEqual(mod.identify("你是 CLAUDE_NEWS wiki 的「投資分析（market）」記者。\n今日日報日期：2026-09-26"),
                         ("market", D))
        self.assertEqual(mod.identify("你是 CLAUDE_NEWS wiki 的分類複核記者。\n今日日期：2026-09-26"), ("分類複核", D))

    def test_no_date_declaration_not_matched(self):
        self.assertIsNone(mod.identify("你是 CLAUDE_NEWS wiki 的「功能」記者。\n條目……"))

    def test_role_only_on_first_line(self):
        self.assertIsNone(mod.identify("你是頁面健檢員。\n你是 CLAUDE_NEWS wiki 的「功能」記者\n今日日報日期：2026-09-26"))


class TestCounts(unittest.TestCase):
    def setUp(self):
        self.r = _features(mod.collect(D, [SUB]))

    def test_tool_uses_and_edits(self):
        self.assertEqual(self.r["tool_uses"]["total"], 11)
        self.assertEqual(self.r["tool_uses"]["by_tool"],
                         {"Bash": 4, "Edit": 2, "Grep": 1, "Read": 3, "Write": 1})
        self.assertEqual(self.r["edits"], 3)

    def test_turns_dedup_split_records(self):
        """一次回應拆成多筆記錄：turns 算 message.id，逐筆數另存。"""
        self.assertEqual(self.r["turns"], 12)
        self.assertEqual(self.r["assistant_records"], 14)

    def test_tokens_counted_once_per_message(self):
        # 逐筆加總會是 85,000（m1、m6 各多算一次）；output 取每則最大值不是加總
        self.assertEqual(self.r["cache_read"], 78000)
        self.assertEqual(self.r["cache_create"], 2200)
        self.assertEqual(self.r["output_tokens"], 795)

    def test_duration_hooks_complete(self):
        self.assertEqual(self.r["duration_s"], 290)
        self.assertEqual(self.r["hook_feedback"], 3)
        self.assertFalse(self.r["incomplete"])

    def test_rule_reads(self):
        rr = self.r["rule_reads"]
        self.assertIn({"file": ".claude/agents/wiki-reporter-features.md", "method": "Read"}, rr)
        self.assertIn({"file": ".claude/reporter-rules/shared.md", "method": "Bash-cat"}, rr)
        self.assertIn({"file": ".claude/reporter-rules/features/pages.md", "method": "Bash-sed",
                       "range": [1, 160]}, rr)
        self.assertIn({"file": ".claude/reporter-rules/features/pages.md", "method": "Grep"}, rr)

    def test_wiki_full_reads(self):
        got = {(w["file"], w["method"]): w["lines"] for w in self.r["wiki_full_reads"]}
        self.assertEqual(got, {
            ("wiki/entities/claude-code.md", "Bash-cat"): _lines("wiki/entities/claude-code.md"),
            ("wiki/feature-radar.md", "Read"): _lines("wiki/feature-radar.md"),
        })  # offset/limit 的 Read 與管線接走的 grep 不算全讀


class TestParsing(unittest.TestCase):
    def test_sed_range_and_cat(self):
        got = mod.bash_reads("cd x && sed -n '1,160p' .claude/reporter-rules/community/pages.md && cat wiki/a.md | head -3")
        self.assertEqual(got[0], {"path": ".claude/reporter-rules/community/pages.md", "method": "Bash-sed",
                                  "range": [1, 160], "piped": False})
        self.assertEqual(got[1], {"path": "wiki/a.md", "method": "Bash-cat", "piped": True})

    def test_absolute_windows_paths(self):
        abs_wiki = str(REPO_ROOT / "wiki" / "entities" / "claude-code.md")
        self.assertEqual(mod.wiki_path(abs_wiki), "wiki/entities/claude-code.md")
        self.assertIsNone(mod.wiki_path(str(REPO_ROOT / "web_reader" / "wiki" / "x.md")))
        self.assertEqual(mod.rule_path(r"C:\x\CLAUDE_NEWS\.claude\reporter-rules\shared.md"),
                         ".claude/reporter-rules/shared.md")

    def test_synthetic_cat_record_counts_wiki_full_read(self):
        with tempfile.TemporaryDirectory() as td:
            src = (SUB / "agent-features.jsonl").read_text(encoding="utf-8").splitlines()
            rec = {"type": "assistant", "message": {"id": "syn", "content": [
                {"type": "tool_use", "id": "syn1", "name": "Bash",
                 "input": {"command": "cat wiki/entities/claude-code.md"}}], "usage": {}}}
            src.insert(2, json.dumps(rec, ensure_ascii=False))
            p = Path(td) / "agent-syn.jsonl"
            p.write_text("\n".join(src) + "\n", encoding="utf-8")
            r = mod.measure(p, "功能", D)
            cats = [w for w in r["wiki_full_reads"] if w["method"] == "Bash-cat"]
            self.assertEqual(len(cats), 2)
            self.assertEqual(cats[0]["lines"], _lines("wiki/entities/claude-code.md"))


class TestIncomplete(unittest.TestCase):
    def _trunc(self, td, drop=20, extra=None):
        lines = (SUB / "agent-features.jsonl").read_text(encoding="utf-8").splitlines()
        lines = lines[:-drop] if drop else lines
        if extra:
            lines.append(extra)
        d = Path(td) / "s" / "subagents"
        d.mkdir(parents=True)
        (d / "agent-features.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
        return d

    def test_truncated_flagged(self):
        with tempfile.TemporaryDirectory() as td:
            r = _features(mod.collect(D, [self._trunc(td)]))
            self.assertTrue(r["incomplete"])
            self.assertLess(r["tool_uses"]["total"], 11)  # 數字變小，但帶了旗標
            code, out = _run("--date", D, "--session-dir", str(Path(td) / "s"),
                             "--ledger", str(Path(td) / "l.jsonl"))
            self.assertIn("不完整", out)
            [row] = [json.loads(x) for x in (Path(td) / "l.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertTrue(row["incomplete"])

    def test_bad_json_line_flagged(self):
        with tempfile.TemporaryDirectory() as td:
            r = _features(mod.collect(D, [self._trunc(td, drop=0, extra='{"type": "assist')]))
            self.assertTrue(r["incomplete"])


class TestCli(unittest.TestCase):
    def test_missing_dir_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = Path(td) / "l.jsonl"
            ledger.write_text('{"x": 1}\n', encoding="utf-8")
            before = hashlib.sha256(ledger.read_bytes()).hexdigest()
            code, out = _run("--date", D, "--projects-root", str(Path(td) / "nope"), "--ledger", str(ledger))
            self.assertEqual(code, 0)
            self.assertIn("無 transcript", out)
            self.assertEqual(hashlib.sha256(ledger.read_bytes()).hexdigest(), before)
            code, out = _run("--date", D, "--session-dir", str(Path(td) / "nope"), "--ledger", str(ledger))
            self.assertIn("無 transcript", out)
            self.assertEqual(hashlib.sha256(ledger.read_bytes()).hexdigest(), before)

    def test_no_reporter_on_date_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = Path(td) / "l.jsonl"
            code, out = _run("--date", "2026-01-01", "--projects-root", str(PROJECTS), "--ledger", str(ledger))
            self.assertEqual(code, 0)
            self.assertIn("無 transcript", out)
            self.assertFalse(ledger.exists())

    def test_idempotent_rerun(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = Path(td) / "l.jsonl"
            _run("--date", D, "--projects-root", str(PROJECTS), "--ledger", str(ledger))
            n1 = len(ledger.read_text(encoding="utf-8").splitlines())
            _run("--date", D, "--projects-root", str(PROJECTS), "--ledger", str(ledger))
            self.assertEqual(n1, 2)
            self.assertEqual(len(ledger.read_text(encoding="utf-8").splitlines()), n1)

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = Path(td) / "l.jsonl"
            code, out = _run("--date", D, "--projects-root", str(PROJECTS), "--ledger", str(ledger), "--dry-run")
            self.assertEqual(code, 0)
            self.assertFalse(ledger.exists())
            self.assertIn("功能", out)

    def test_incomplete_then_complete_appends(self):
        """跑到一半量過一次（不完整），跑完再量要能補一行完整的；之後再跑不再長。"""
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "s" / "subagents"
            d.mkdir(parents=True)
            full = (SUB / "agent-features.jsonl").read_text(encoding="utf-8").splitlines()
            f = d / "agent-features.jsonl"
            f.write_text("\n".join(full[:-20]) + "\n", encoding="utf-8")
            ledger = Path(td) / "l.jsonl"
            args = ("--date", D, "--session-dir", str(Path(td) / "s"), "--ledger", str(ledger))
            _run(*args)
            f.write_text("\n".join(full) + "\n", encoding="utf-8")
            _run(*args)
            _run(*args)
            rows = [json.loads(x) for x in ledger.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([r["incomplete"] for r in rows], [True, False])

    def test_run_index_for_same_role(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "s" / "subagents"
            d.mkdir(parents=True)
            shutil.copy(SUB / "agent-features.jsonl", d / "agent-features.jsonl")
            shutil.copy(SUB / "agent-features.jsonl", d / "agent-features-rerun.jsonl")
            rows = [r for r in mod.collect(D, [d]) if r["role"] == "功能"]
            self.assertEqual(sorted(r["run_index"] for r in rows), [1, 2])

    def test_default_projects_root_encoding(self):
        p = mod.default_projects_root(Path(r"C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS"))
        self.assertEqual(p.name, "C--Users-Mandy-CLAUDE-OBSIDIAN-ObsidianLab-CLAUDE-NEWS")


if __name__ == "__main__":
    unittest.main()

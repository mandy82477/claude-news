"""`.claude/hooks/guard_roles.py` 與 `_identity.py`：依身分擋越權動作（H5–H8）。

身分是這支 hook 的地基：主 session 修日報、改閘腳本是合法的開發，同樣的動作由
記者或雲端 session 做就是越權。所以本檔先驗身分判定，再驗每條規則的兩側。
"""
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
HOOKS = REPO / ".claude" / "hooks"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HOOKS / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ident = _load("_identity")
mod = _load("guard_roles")

REPORTER_PROMPT = "你是 CLAUDE_NEWS wiki 的「功能」記者。開工前先 Read `.claude/agents/wiki-reporter-features.md`"
PIPELINE_PROMPT = "你是 Claude News Pipeline Agent（Phase A）。"


class _Env(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.get(k) for k in ("CLAUDE_PROJECT_DIR", "CLAUDE_CODE_REMOTE")}
        os.environ["CLAUDE_PROJECT_DIR"] = str(REPO)
        os.environ.pop("CLAUDE_CODE_REMOTE", None)
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        for k, v in self._saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        self.tmp.cleanup()

    def subagent_payload(self, prompt, tool, tool_input, agent_id="a1"):
        """照 2026-10-03 實測的配置造一份子 agent transcript：<session>/subagents/agent-<id>.jsonl。"""
        tp = Path(self.tmp.name) / "sess.jsonl"
        sub = Path(self.tmp.name) / "sess" / "subagents"
        sub.mkdir(parents=True, exist_ok=True)
        rec = {"type": "user", "message": {"role": "user", "content": prompt}, "agentId": agent_id}
        (sub / f"agent-{agent_id}.jsonl").write_text(json.dumps(rec, ensure_ascii=False) + "\n", encoding="utf-8")
        return {"tool_name": tool, "tool_input": tool_input, "cwd": str(REPO), "transcript_path": str(tp),
                "agent_id": agent_id, "agent_type": "general-purpose"}

    def main_payload(self, tool, tool_input):
        return {"tool_name": tool, "tool_input": tool_input, "cwd": str(REPO)}


class TestIdentity(_Env):
    def test_roles(self):
        self.assertEqual(ident.role({"tool_name": "Bash"}), "main")
        self.assertEqual(ident.role(self.subagent_payload(REPORTER_PROMPT, "Bash", {})), "reporter")
        self.assertEqual(ident.role(self.subagent_payload(PIPELINE_PROMPT, "Bash", {}, "a2")), "pipeline")
        self.assertEqual(ident.role(self.subagent_payload("幫我找檔案", "Bash", {}, "a3")), "subagent")

    def test_missing_transcript_is_strict(self):
        """找不到 transcript 時當一般子 agent（嚴），不當 pipeline（寬）。"""
        p = {"agent_id": "zz", "transcript_path": str(Path(self.tmp.name) / "nope.jsonl")}
        self.assertEqual(ident.role(p), "subagent")

    def test_content_as_block_list(self):
        self.assertEqual(ident.role_from_prompt(None, "wiki-reporter-models"), "reporter")


class TestH5News(_Env):
    def test_reporter_cannot_write_news(self):
        for tool, ti in (
            ("Write", {"file_path": str(REPO / "news" / "2026-10-03.md")}),
            ("Edit", {"file_path": "news/2026-10-03.md"}),
            ("Bash", {"command": "sed -i 's/a/b/' news/2026-10-03.md"}),
            ("Bash", {"command": "echo x >> news/2026-10-03.md"}),
        ):
            with self.subTest(tool=tool, ti=ti):
                self.assertIsNotNone(mod.decide(self.subagent_payload(REPORTER_PROMPT, tool, ti)))

    def test_main_and_pipeline_can_write_news(self):
        ti = {"file_path": str(REPO / "news" / "2026-10-03.md")}
        self.assertIsNone(mod.decide(self.main_payload("Write", ti)))
        self.assertIsNone(mod.decide(self.subagent_payload(PIPELINE_PROMPT, "Write", ti)))

    def test_reporter_can_write_own_wiki_page(self):
        ti = {"file_path": str(REPO / "wiki" / "entities" / "claude-code.md")}
        self.assertIsNone(mod.decide(self.subagent_payload(REPORTER_PROMPT, "Edit", ti)))
        self.assertIsNone(mod.decide(self.subagent_payload(REPORTER_PROMPT, "Bash", {"command": "grep -n x news/2026-10-03.md"})))


class TestH6Gates(_Env):
    GATE_PATHS = ("scripts/check_cell_limits.py", "scripts/run_tests.py", "scripts/gate_web_build.py",
                  "data/cell-limit-baseline.json", "data/reader-language-allow.json",
                  "data/baseline-changes.jsonl", "docs/known-test-gaps.json")

    def test_subagents_blocked(self):
        for prompt in (REPORTER_PROMPT, PIPELINE_PROMPT, "一般任務"):
            for rel in self.GATE_PATHS:
                with self.subTest(prompt=prompt[:10], rel=rel):
                    p = self.subagent_payload(prompt, "Edit", {"file_path": str(REPO / rel)})
                    self.assertIsNotNone(mod.decide(p))

    def test_local_main_may_develop(self):
        for rel in self.GATE_PATHS:
            with self.subTest(rel=rel):
                self.assertIsNone(mod.decide(self.main_payload("Edit", {"file_path": str(REPO / rel)})))
        self.assertIsNone(mod.decide(self.main_payload("Bash", {"command": "python scripts/check_cell_limits.py --rebuild"})))

    def test_cloud_main_blocked(self):
        os.environ["CLAUDE_CODE_REMOTE"] = "true"
        self.assertIsNotNone(mod.decide(self.main_payload("Edit", {"file_path": str(REPO / "scripts/check_rules.py")})))
        self.assertIsNotNone(mod.decide(self.main_payload("Bash", {"command": "python3 scripts/check_cell_limits.py --rebuild"})))
        self.assertIsNotNone(mod.decide(self.main_payload("Bash", {"command": "python3 x.py --allow-grow=3"})))
        self.assertIsNone(mod.decide(self.main_payload("Bash", {"command": "python3 scripts/check_cell_limits.py"})))
        self.assertIsNone(mod.decide(self.main_payload("Edit", {"file_path": str(REPO / "wiki/log.md")})))

    def test_subagent_rebuild_flag_blocked(self):
        p = self.subagent_payload(REPORTER_PROMPT, "Bash", {"command": "python scripts/check_cell_limits.py --rebuild"})
        self.assertIsNotNone(mod.decide(p))


class TestH7H8Agent(_Env):
    def test_subagent_cannot_delegate(self):
        for prompt in (REPORTER_PROMPT, PIPELINE_PROMPT, "一般任務"):
            with self.subTest(prompt=prompt[:10]):
                p = self.subagent_payload(prompt, "Agent", {"prompt": "幫我做", "model": "haiku"})
                self.assertIsNotNone(mod.decide(p))

    def test_reporter_dispatch_needs_model_and_foreground(self):
        base = {"prompt": REPORTER_PROMPT, "subagent_type": "general-purpose"}
        self.assertIsNotNone(mod.decide(self.main_payload("Agent", {**base, "run_in_background": False})))
        self.assertIsNotNone(mod.decide(self.main_payload("Agent", {**base, "model": "sonnet"})))
        self.assertIsNotNone(mod.decide(self.main_payload("Agent", {**base, "model": "sonnet", "run_in_background": True})))
        self.assertIsNone(mod.decide(self.main_payload("Agent", {**base, "model": "sonnet", "run_in_background": False})))

    def test_pipeline_dispatch_needs_model_background_ok(self):
        base = {"prompt": PIPELINE_PROMPT, "run_in_background": True}
        self.assertIsNotNone(mod.decide(self.main_payload("Agent", base)))
        self.assertIsNone(mod.decide(self.main_payload("Agent", {**base, "model": "sonnet"})))

    def test_other_dispatch_untouched(self):
        self.assertIsNone(mod.decide(self.main_payload("Agent", {"prompt": "找出所有 hook", "subagent_type": "Explore"})))


class TestMainContract(_Env):
    def test_exit_codes(self):
        def run(payload):
            old = sys.stdin, sys.stderr
            sys.stdin, sys.stderr = io.StringIO(json.dumps(payload)), io.StringIO()
            try:
                return mod.main()
            finally:
                sys.stdin, sys.stderr = old

        self.assertEqual(run(self.subagent_payload(REPORTER_PROMPT, "Write", {"file_path": "news/x.md"})), 2)
        self.assertEqual(run(self.main_payload("Write", {"file_path": "news/x.md"})), 0)
        self.assertEqual(run({"tool_name": "Read", "tool_input": {"file_path": "news/x.md"}, "agent_id": "a"}), 0)
        sys.stdin = io.StringIO("not json")
        try:
            self.assertEqual(mod.main(), 0)
        finally:
            sys.stdin = sys.__stdin__


if __name__ == "__main__":
    unittest.main()

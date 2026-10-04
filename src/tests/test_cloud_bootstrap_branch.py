"""cloud_bootstrap.ensure_on_master() 的判準測試。

用真的 git 倉庫重現雲端容器的起始狀態：HEAD detached 在 origin/master 最新 commit、
本機 master 停在舊 commit（2026-09-29 17:00 班就是這樣起跑，後續臨場修補被 Auto Mode
擋下、整班推不上去）。重點守兩個方向：該歸位時歸位，會丟東西時絕不動手。
"""
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
import cloud_bootstrap as cb  # noqa: E402


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr}")
    return r.stdout.strip()


def commit(repo: Path, name: str) -> str:
    (repo / name).write_text(name, encoding="utf-8")
    git(repo, "add", name)
    git(repo, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", name)
    return git(repo, "rev-parse", "HEAD")


def cloud_like_clone(tmp: Path) -> tuple[Path, Path]:
    """origin 有 old→new 兩個 commit；clone 的本機 master 停在 old、HEAD detached 在 new。"""
    work = tmp / "seed"
    work.mkdir()
    git(work, "init", "-q", "-b", "master")
    commit(work, "old")
    origin = tmp / "origin.git"
    git(tmp, "clone", "-q", "--bare", str(work), str(origin))
    clone = tmp / "clone"
    git(tmp, "clone", "-q", str(origin), str(clone))
    new = commit(work, "new")
    git(work, "push", "-q", str(origin), "master")
    git(clone, "fetch", "-q", "origin")
    git(clone, "checkout", "-q", "--detach", new)  # 本機 master 仍停在 old
    return clone, work


class TestEnsureOnMaster(unittest.TestCase):
    def test_detached_at_origin_tip_is_moved_to_master(self):
        with TemporaryDirectory() as t:
            clone, _ = cloud_like_clone(Path(t))
            self.assertEqual(cb.ensure_on_master(clone), "switched")
            self.assertEqual(git(clone, "symbolic-ref", "--short", "HEAD"), "master")
            self.assertEqual(git(clone, "rev-parse", "master"), git(clone, "rev-parse", "origin/master"))
            self.assertEqual(git(clone, "rev-parse", "--abbrev-ref", "master@{upstream}"), "origin/master")

    def test_detached_behind_origin_is_moved_to_latest(self):
        # 容器起跑後 origin 又前進（例如 GH Actions 剛推了抓料）：HEAD 是祖先，仍可安全歸位
        with TemporaryDirectory() as t:
            clone, work = cloud_like_clone(Path(t))
            newer = commit(work, "newer")
            git(work, "push", "-q", str(Path(t) / "origin.git"), "master")
            self.assertEqual(cb.ensure_on_master(clone), "switched")
            self.assertEqual(git(clone, "rev-parse", "HEAD"), newer)

    def test_local_commit_on_detached_head_is_never_discarded(self):
        # 17:00 班的情況：已在 detached HEAD 上 commit 了 STARTED——那個 commit 不得被丟
        with TemporaryDirectory() as t:
            clone, _ = cloud_like_clone(Path(t))
            mine = commit(clone, "started")
            self.assertEqual(cb.ensure_on_master(clone), "diverged")
            self.assertEqual(git(clone, "rev-parse", "HEAD"), mine)

    def test_uncommitted_append_is_carried_onto_master(self):
        # 2026-10-03：雲端探針 hook 在 bootstrap 之前往 task_scheduler.log 寫一行，舊判準
        # 「工作樹髒就不歸位」讓 17Z、22Z、隔天 watchdog 三班卡在 detached HEAD、全推不上 master
        with TemporaryDirectory() as t:
            clone, _ = cloud_like_clone(Path(t))
            (clone / "new").write_text("new\n[cloud hooks-probe ACTIVE x]\n", encoding="utf-8")
            self.assertEqual(cb.ensure_on_master(clone), "switched")
            self.assertEqual(git(clone, "symbolic-ref", "--short", "HEAD"), "master")
            self.assertIn("hooks-probe", (clone / "new").read_text(encoding="utf-8"))

    def test_dirty_file_that_origin_would_overwrite_is_left_alone(self):
        # HEAD 落後 origin、且改動的檔 origin 也改過：checkout 會拒絕，改動與 HEAD 都不得被動
        with TemporaryDirectory() as t:
            clone, work = cloud_like_clone(Path(t))
            (work / "new").write_text("origin moved", encoding="utf-8")
            git(work, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qam", "move")
            git(work, "push", "-q", str(Path(t) / "origin.git"), "master")
            (clone / "new").write_text("my edit", encoding="utf-8")
            head = git(clone, "rev-parse", "HEAD")
            self.assertEqual(cb.ensure_on_master(clone), "dirty")
            self.assertEqual(git(clone, "rev-parse", "HEAD"), head)
            self.assertEqual((clone / "new").read_text(encoding="utf-8"), "my edit")

    def test_already_on_master_is_noop(self):
        with TemporaryDirectory() as t:
            clone, _ = cloud_like_clone(Path(t))
            git(clone, "checkout", "-q", "master")
            before = git(clone, "rev-parse", "HEAD")
            self.assertEqual(cb.ensure_on_master(clone), "on-master")
            self.assertEqual(git(clone, "rev-parse", "HEAD"), before)

    def test_other_branch_is_not_switched(self):
        with TemporaryDirectory() as t:
            clone, _ = cloud_like_clone(Path(t))
            git(clone, "checkout", "-q", "-b", "feature")
            self.assertEqual(cb.ensure_on_master(clone), "other-branch")
            self.assertEqual(git(clone, "symbolic-ref", "--short", "HEAD"), "feature")

    def test_not_a_repo_does_not_raise(self):
        with TemporaryDirectory() as t:
            self.assertIn(cb.ensure_on_master(Path(t)), {"dirty", "fetch-failed", "error", "diverged", "checkout-failed"})


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Stop hook: while a long run is active, do not let the coordinator end with unsaved work.

Active only when reports/RUN_STATE.md contains "status: running". Fails open.
"""

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=10)
    return result.stdout.strip() if result.returncode == 0 else ""


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except (ValueError, OSError):
        event = {}
    state = ROOT / "reports/RUN_STATE.md"
    if event.get("loop_count", 0) >= 1 or not state.is_file():
        print("{}")
        return
    if "status: running" not in state.read_text():
        print("{}")
        return
    problems = []
    if git("status", "--porcelain"):
        problems.append("uncommitted changes")
    ahead = git("rev-list", "--count", "@{u}..HEAD")
    if ahead and ahead != "0":
        problems.append(f"{ahead} unpushed commit(s)")
    if not problems:
        print("{}")
        return
    message = (
        "reports/RUN_STATE.md says a long run is still running, and the repository has "
        + " and ".join(problems)
        + ". Before stopping: run `python3 scripts/story.py check`, commit the intended project "
        "files, push, and update reports/RUN_STATE.md (the exact next step, or `status: stopped` / "
        "`status: finished` with the reason). If the run is complete, write the morning report."
    )
    print(json.dumps({"followup_message": message}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("{}")

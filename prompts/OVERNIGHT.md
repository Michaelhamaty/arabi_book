# Overnight / long-running coordinator runbook

The coordinator is the agent in the user's chat. It does not write or review
chapters itself. It launches a **fresh subagent for each role**, checks their
work with the scripts, commits and pushes each stage, and writes a morning
report. The user's request (for example "develop chapters 004–008") authorizes
the delegation, provisional acceptance, and routine commits and pushes for that
run.

## Before starting

1. `git status`, current branch, remote. Integrate remote work with a normal
   fetch and merge or rebase of local unpushed commits only; never force-push.
   Do not proceed over uncommitted work you did not make: report it.
2. `python3 scripts/story.py check` and
   `python3 -m unittest discover -s tests -v` must pass.
3. Note the target range and cap (default: the requested chapters; never more
   than eight chapters in one run).

## Checkpoint file and resuming

Persistent run memory lives in the repository, not in the chat:

- `reports/RUN_STATE.md` is the resume point. Create it at the start with
  `status: running`, the target range, and a stage table. After every stage,
  update it (stage done, commit hash, model used, **exact next step**) and commit
  it with that stage. At the end, set `status: finished` or `status: stopped`
  with the reason.
- The project stop hook (`.cursor/hooks.json` → `.cursor/hooks/run-checkpoint.py`)
  reads that file. While it says `status: running`, the coordinator cannot end a
  turn with uncommitted or unpushed work without being told to save first.
- A new chat resumes by reading `reports/RUN_STATE.md`, running
  `story.py check`, and continuing from the recorded next step. Registry status
  plus `review.md` sections show exactly how far each chapter got.

Template:

```text
# Run state
status: running
range: 004–005
started: YYYY-MM-DD HH:MM
| chapter | stage | result | commit | model |
| --- | --- | --- | --- | --- |
next: 004 planner
notes:
```

## Usage limits and model fallback

No agent can see the user's remaining usage reliably, so protection comes from
saving often: commit and push after **every** stage, and keep `RUN_STATE.md`
current, so a cutoff loses at most the stage in progress. A half-finished stage
is redone from its start, using the registry status as the guide.

If a subagent launch fails with a usage, quota, or rate-limit error, or the user
has said usage is nearly gone, relaunch that same stage with
`model: "grok-4.7-high"` (authorized by the user on 2026-11-10). Record the model
in `RUN_STATE.md`, add `Model: Grok 4.7 (fallback)` at the top of that stage's
section in `review.md`, and list every fallback stage in the morning report under
**Needs Claude review**. The next day, a Claude agent re-runs the language and
story reviews for those chapters under the corrections procedure in
`prompts/ACCEPTANCE.md`. If the fallback also fails, save and stop.

## Per-chapter loop

Run chapters strictly in order. Each stage is a new subagent (Cursor `Task`,
`subagent_type: generalPurpose`; leave the model unset unless the user names
one). Each subagent prompt must be self-contained: the workspace path, the
chapter ID, the role prompt file to follow, and a line telling it that it has a
fresh context and must read the packet files itself. Never paste the previous
agent's opinions into the next reviewer's prompt beyond what is in the files.

| Stage | Role prompt | Coordinator verification | Commit message |
|---|---|---|---|
| 1 | `prompts/PLANNER.md` | brief exists; registry `brief_ready`; check passes | `Plan Chapter NNN brief` |
| 2 | `prompts/WRITER.md` | `arabizi_review`; check passes; read the chapter's opening and ending | `Draft Chapter NNN Arabizi` |
| 3 | `prompts/LANGUAGE_REVIEWER.md` | `## Language review` appended; check passes | `Language review for Chapter NNN` |
| 4 | `prompts/STORY_REVIEWER.md` | `ready_for_author` with a matching hash, or `revision_needed` | `Story review for Chapter NNN` |
| 5 | `prompts/ARCHIVIST.md` | `provisionally_accepted`; markers advanced; check and tests pass | `Provisionally settle Chapter NNN and update memory` |

Push after every commit. If the story reviewer returns `revision_needed`, launch
a fresh writer in revision mode, then fresh language and story reviewers again.
Allow at most **two** revision loops per chapter.

The coordinator may make small mechanical fixes itself (a JSON typo, a stale
marker) but must record them in the morning report. It must not rewrite
prose; send prose problems back through the revision loop.

## Revision batches

To revise several settled chapters at once (as with 001–003 under C007), set
them to `arabizi_review` and keep their `acceptance_history`. Language and
story reviewers may then run in parallel, one per chapter, but each edits only
its own chapter and `review.md` and must not touch the registry; the
coordinator records the passing hashes. While any chapter in the batch has
check errors, packets refuse to print, so tell parallel reviewers to read the
packet inputs listed in `scripts/story.py`. One archivist then rebuilds memory
for the whole batch in order.

## Stop conditions

Stop the run, commit what is safe, and write the report when:

- a check or test fails and one mechanical fix does not clear it;
- a chapter fails story review after two revision loops;
- the next chapter needs a fact only the user can supply (a real-family
  detail, the UAB program, a boundary question);
- a push fails (keep the local commits; never claim a push succeeded);
- the requested range or the cap is reached.

## Morning report

Create `reports/YYYY-MM-DD.md` (the run's date) and commit it last:

- chapters produced, titles, dates covered, word counts, and hashes;
- a one-paragraph spoiler summary of each and what changed;
- the most important reviewer fixes and any remaining language doubts;
- new characters and durable facts added to the master;
- decisions taken under delegated authority, open questions for the user;
- commits pushed, and anything that failed or was stopped;
- models used per stage, and a **Needs Claude review** list for fallback stages;
- how to respond: "I accept 004–008", "Revise 006: ...", or "Reject 007
  because ..." (see `prompts/ACCEPTANCE.md`).

## Starting prompt for the user

> Develop chapters 004–008 with the overnight workflow in
> `prompts/OVERNIGHT.md`. Use fresh agents for each role, commit and push each
> stage, and leave me a morning report.

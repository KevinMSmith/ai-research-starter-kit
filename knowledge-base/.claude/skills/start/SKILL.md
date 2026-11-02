---
name: start
description: Open a session on this knowledge base. Reads the resume point and the rules, checks that raw/ is unchanged, lists what is new in the inbox, and reports in one screen.
disable-model-invocation: true
argument-hint: "[what to do first]"
---

# Open the session

1. Read `PROGRESS.md`, then `AGENTS.md`. Read the last block of the newest file in `log/` when the resume point refers
   to it.
2. If `PROGRESS.md` lists set-up steps for the agent (a new project), carry them out first, in order, with the
   author, and skip the rest of this list until they are done. Otherwise run `git status --short` and
   `git log --oneline -5`; name anything uncommitted in the report, and never commit it without asking.
3. Run `python tools/deposit.py verify`. If it reports a problem, stop and explain it before anything else.
4. List the inbox (the folder in `tools/config.py`): the files that are not yet deposited (compare with the original
   names in `raw/MANIFEST.md`). A file is deposited only when the author names it or says it is there for that purpose.
5. Report in one screen, in plain sentences: where the work stands, what the last session did, the author's open items,
   what is new in the inbox, and the result of the check. Then do what the author asked ($ARGUMENTS), or wait.

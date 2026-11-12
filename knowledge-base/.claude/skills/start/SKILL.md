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
   `git log --oneline -5`. If files are left uncommitted, check whether the session that left them has ended: none of
   the files, and no Claude Code conversation for this folder (in `~/.claude/projects/`), has changed in the last
   hour. If so, commit the leftover files by name (`git commit -- <paths>`), in a commit of their own whose message
   says that an earlier session left them, and say so in the report. Otherwise name the files in the report and
   leave them alone, because another session may still be working on them.
3. Run `python tools/deposit.py verify`. If it reports a problem, explain it first in the report, then continue with
   the work that does not depend on the affected files.
4. List the inbox (the folder in `tools/config.py`): the files that are not yet deposited (compare with the original
   names in `raw/MANIFEST.md`). Files in this project's inbox are for deposit. Deposit what contributes, with the
   deposit skill, and list in the report what was left out and why.
5. Report in one screen, in plain sentences: where the work stands, what the last session did, the author's open items,
   what is new in the inbox, and the result of the check. Then do what the author asked ($ARGUMENTS), or wait.

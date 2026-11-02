---
name: close
description: Use when a unit of work is complete, before the session ends. Appends the log block, rewrites the one-screen resume point, checks raw/, commits and pushes.
---

# Close a unit of work

The record lives in the files, not in the conversation. A session that ends without this step leaves the next one
without its memory.

1. **The log block.** Append to `log/<YYYY-MM>.md` (create the month's file if needed) one block in the shape of
   `templates/log-block.md`: what was asked, what was read, what was produced, the decisions taken without asking
   (each with how to undo it), what the author does next, and what is open.
2. **The resume point.** Rewrite `PROGRESS.md`: where the work is, what was verified, the author's open items, the
   agent's open items. It stays one screen.
3. **The rules.** If the author corrected the same thing twice in this session, add the rule to `AGENTS.md` with its
   reason, and the decision to `DECISIONS.md`.
4. **Check.** `python tools/deposit.py verify`; `git status --short` shows only what this unit changed.
5. **Commit and push**: one commit with a message that says what and why; `git push` if a remote exists.
6. **Hand over**: what was done, what the author does first, and any question for the author with a recommendation.

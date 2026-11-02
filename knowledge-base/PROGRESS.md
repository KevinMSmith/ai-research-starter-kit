# Progress — the resume point

A new session reads this file first, then `AGENTS.md`. It stays one screen and is rewritten at the end of every
session, never appended to. The history is in `log/`.

## Where the work is

- The knowledge base was copied from the starter kit's template. The set-up below has not been done yet.

## Verified

- Nothing yet: the set-up below ends with the check of the guard hook.

## Open, the author's

1. Answer the agent's set-up questions (below).
2. Then put the first files in the inbox: a few recent meeting transcripts, the key documents, and one dictation that
   explains what the project is about and what you want from it.

## Open, the agent's: the set-up, in this order, before anything else

Explain each step in plain words before you take it, and ask one question at a time, each with a suggested answer.
If the author declines a step, or a step fails, leave it in this list marked as open, say why, and go on with the next.

1. **The questions.** Ask the author: the project's full title (the folder's name is its short form); one paragraph
   on what the project is and what it should produce; who must never be named in it (for example students, residents, patients); and where the inbox should be (suggest
   `C:\dev\inbox\<project name>` on Windows, `~/dev/inbox/<project name>` on macOS). Explain that the inbox is the
   folder where new material waits, under its original names, until it is deposited.
2. **The blanks.** Fill in, from the answers: `AGENTS.md` (the project's title and paragraph, rule 7 on who is never
   named, and the section "The author": offer, as the suggested answer, what the author's own instructions in the user
   folder say about them, and ask the author to confirm or change it), `README.md` (the name
   and today's date), and `tools/config.py` (the inbox path). Create the inbox folder. Leave a blank the author cannot
   answer yet, and say which ones are left.
3. **Python's name.** Run `python --version`. If only `python3` or only `py` works, change `"command": "python"` to that
   name in `.claude/settings.json`, which starts the guard hook, and tell the author why; Claude Code asks the author
   to approve a change to that file.
4. **Git.** Explain in two sentences: Git keeps every earlier version of every file in the project, so nothing written
   is ever lost; a commit is one saved step in that history, with a sentence that says what changed. Run `git init`.
   If `git config user.name` or `user.email` is empty, ask for the author's name and e-mail, and set them with
   `git config --global` (they then apply to every project of the author's), or without `--global` for this project
   only if the author prefers. Commit everything with the message "Set up
   the knowledge base from the starter kit". Offer, but do not push for, a private copy on GitHub as a backup, later.
5. **The guard.** Explain: `raw/` will hold the originals, and the guard hook stops the agent from ever changing them.
   Use the Write tool to create `raw/guard-test.md`. Claude Code must refuse it with the message that `raw/` holds the
   originals; tell the author that this refusal is the right result. If the file is created instead, delete it, stop,
   and tell the author: the guard is not running, and `raw/` is unprotected until it is fixed (`tools/README.md`, "If
   the guard does not run"). Then run `python tools/deposit.py verify`, which should say "no deposits yet, and nothing else in raw/".
6. **Close.** Rewrite this file: remove this set-up list, record under "Verified" that the guard refused the write
   (with the date), and set the next items: deposit the files the author names, render them and write a card for each
   (`/deposit`); then read all the cards and report what the material covers, what it claims without support, and what
   is missing that only the author can supply, as a list of questions to dictate answers to. Write the first log
   block and commit (`/close`).

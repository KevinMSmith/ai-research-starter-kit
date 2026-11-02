# tools — the scripts

Run from the project folder, in the terminal of VS Code or by the agent. They need Python 3.10 or later.

| Script | What it does | Needs |
|---|---|---|
| `deposit.py` | `add` copies a file from the inbox into `raw/` under its ID, checksums it and lists it in `raw/MANIFEST.md`; `verify` proves that nothing in `raw/` has changed; `next <CLASS>` gives the next free ID | nothing beyond Python |
| `extract.py` | renders each deposit to plain text with numbered paragraphs in `sources/<ID>.md`; replaces speaker names in Teams transcripts with "Speaker 1", "Speaker 2" unless told otherwise | `python -m pip install pypdf python-docx python-pptx openpyxl`, once, for PDF, Word, PowerPoint and Excel files |
| `transcribe.py` | transcribes a recording (m4a from a phone, mp3, wav, mp4) on this computer, with the speakers labelled, and writes a `.vtt` file in the layout of a Teams transcript and a `.txt` file with one paragraph per speaker turn beside the recording; nothing is uploaded | ffmpeg and NVIDIA's NeMo-Speech.cpp with its two models (about 800 MB, downloaded once); the script's description at its top says how to get them, and guide 01 says what to ask the agent |
| `config.py` | the one setting: the inbox folder | |
| `hooks/guard_raw.py` | the guard hook: Claude Code runs it before every edit and every shell command, and it refuses any that would change `raw/` | nothing beyond Python; switched on in `.claude/settings.json` |

## If the guard does not run

Claude Code starts the guard as `python` with the script's path (`.claude/settings.json`), with no shell in between,
so it does not need Git Bash. Two things can still stop it, and both are fixed in `.claude/settings.json`:

- **The command `python` is not found.** On a Mac, Python is often installed as `python3` only: change `"command":
  "python"` to `"command": "python3"`. On Windows, if `python` opens the Microsoft Store, use `"command": "py"`.
- **The setting was not read.** A folder that VS Code has not trusted runs in Restricted Mode, and the project's
  settings are not used; trust the folder and start a new conversation.

Then repeat the check in `PROGRESS.md`: the agent's attempt to write `raw/guard-test.md` must be refused.

Why the direct form: a guard written as a command for Git Bash (`"shell": "bash"`) was tested on 1 November 2026 on a
Windows laptop with Git for Windows installed in the user's own folder. When Claude Code could not find Git Bash, the
older version 2.1.248 let the edit into `raw/` through without a word, and version 2.1.314 blocked every edit. The
direct form refused the write to `raw/` and allowed a write to `kb/` in both versions.


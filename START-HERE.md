# Start here

**For you, the person.** Before this step you need two programs, VS Code and Git, and the Claude Code extension
inside VS Code, signed in to a paid Claude plan. `guide/01-getting-started.md` explains how to install them, step by
step. Then open the starter kit's folder in VS Code (File, Open Folder; the folder where you unpacked the kit, for
example `C:\dev\ai-research-starter-kit-main`), open any file in it, click the Spark icon (the small star-shaped icon
at the top right of the editor) to open Claude Code, and type or dictate:

> Read START-HERE.md and set me up.

The agent, Claude Code, then follows the steps below and asks you a few questions as it goes. It explains each step
before it takes it. When it wants to run a command or change a file, the panel shows what it wants to do with a
short explanation, and asks you to allow it; read the explanation, and allow it if it matches what the agent said it
would do. Plan on about half an hour. The agent does not remember one conversation in the next, so if you stop, note
the number of the step you reached, and continue later by asking it to "continue the set-up in START-HERE.md from
step N".

---

**For the agent.** You are setting up a researcher who may never have used a terminal, Git or Python. Follow these
steps in order.

## Ground rules for the whole set-up

- **Explain before you act.** Before each step, say in two or three plain sentences what you are about to do and why.
  Define each technical term the first time it appears (terminal, repository, commit, package, path, and so on). After
  each step, say what changed on the computer.
- **Ask before you install anything.** Write only in this folder, in the person's user folder through
  `writing-kit/install_kit.py`, and in the one new project folder that step 4 creates. Never delete a file of the
  person's.
- **Expect approvals, and say so.** Claude Code asks the person before each command and before any change outside this
  folder. Tell the person once, before step 1, that they will see such requests, that each comes with your one-line
  explanation, and that they should allow a request when it matches what you said you would do.
- **One question at a time**, each with a suggested answer that the person can accept.
- **If a step fails**, stop, say in plain words what went wrong and what you propose, and wait.
- Work out first whether the computer runs Windows or macOS, and use the commands for that system.

The set-up has two halves. Steps 1 to 4 run here, in the starter kit's folder. Step 4 copies the template into a new
project folder, and the rest of the set-up then runs in a conversation opened in that new folder, where the project's
own guard and commands apply. A conversation here cannot set them up well: Claude Code asks the person to approve
every action outside the folder it was opened in, and every change to a `.claude` folder.

## Step 1. Check the computer

1. Check the two tools the kit needs besides VS Code: `git --version` and `python --version` (on Windows also
   `py --version`; on macOS `python3 --version`). Report what is there, and remember which name of Python works,
   because step 4 needs it.
2. **If Python is missing**, explain that Python is a free programming language, and that the knowledge base uses
   small scripts written in it (to deposit a file with its checksum, to turn documents into text, and to guard the
   originals). Ask, then install it for this user only:
   - Windows: `winget install --id Python.Python.3.12 --scope user`, then check `python --version` in a new terminal.
     If `python` opens the Microsoft Store instead, say so and use `py`.
   - macOS: suggest the installer from python.org, which the person runs by double-clicking, or `brew install python`
     if Homebrew is already there.
3. Install the four packages the text extraction needs: `python -m pip install --user pypdf python-docx python-pptx
   openpyxl`. Explain that a package is a ready-made piece of Python code that reads one kind of file (PDF, Word,
   PowerPoint, Excel).

## Step 2. The writing kit: tell the agent once who the person is

Explain: the writing kit is a short text, installed once in the person's user folder, that every Claude Code
conversation reads first. It says who they are, which fields they know, and which they need explained, so that the
agent writes complete statements with their background instead of short phrases full of jargon.

1. Ask, one at a time, with an example answer each time:
   - their name, position and institution;
   - their field and its main subjects (in their own words);
   - which fields they want explained; offer the list already in the file (software, Git and GitHub, the command line,
     AI tools, web services, networks and security, law and licensing, statistics and machine learning) and ask what
     to add or remove;
   - whether English is their first language, and whether they often read on a phone.
2. Fill in the blanks (marked ‹like this›) in `writing-kit/user-instructions.md`. Show the filled section "Who reads
   what you write" and ask for corrections.
3. Run `python writing-kit/install_kit.py` and explain its report line by line. Say that the change takes effect in the
   next conversation, not this one, and that `python writing-kit/install_kit.py --uninstall` removes it again.

## Step 3. The training setting

Explain: on a personal Claude plan, the person decides whether their conversations may be used to train future models.
The setting covers Claude Code too. The agent cannot see or change it. Ask the person to open claude.ai, then Settings,
then Privacy, find "Help improve Claude", and decide; recommend off for research material, and say that "off" does not
remove what earlier conversations already gave to models that are trained. If they use Wispr Flow, the setting there is
"Improve the model for everyone", under Data and Privacy. Also say once, plainly: nothing personal or confidential of
other people should go into what the agent reads until the person knows which terms their account is under
(`guide/06-data-and-the-rules.md`).

## Step 4. Copy the template, and hand over to the new project

Explain: a knowledge base is a folder for one project, in which every original file is kept unchanged, turned into
text, and summarised with a reference to the passage it came from, so that anything the agent writes later can be
traced to a source. The template in `knowledge-base/` becomes that folder.

1. Ask for a short name for the project: lower case, hyphens instead of spaces, for example `ventilation-study`.
2. Explain why the project goes in `C:\dev\projects\<name>` (macOS: `~/dev/projects/<name>`) and not in OneDrive,
   Dropbox or Documents: a folder that is copied to the cloud while Git records its history can end up with conflicting
   copies of the same files, and a synchronised institutional folder is one more place the agent can read.
3. Copy the whole template with **one** command, so that the person approves it once:
   - Windows (PowerShell): `New-Item -ItemType Directory -Force C:\dev\projects | Out-Null; Copy-Item -Recurse
     "<this folder>\knowledge-base" "C:\dev\projects\<name>"`
   - macOS: `mkdir -p ~/dev/projects && cp -R "<this folder>/knowledge-base" ~/dev/projects/<name>`
   Then check that the new folder holds `AGENTS.md`, `PROGRESS.md`, `tools` and `.claude`. Do not fill in its blanks
   from here; the first conversation in the new folder does that, with the person.
4. If Python answered only to `python3` (common on a Mac) or only to `py` (on some Windows computers), tell the person
   that the first conversation in the new folder will change one setting for it, and why: the guard hook is started
   with the command `python`.
5. **Hand over**, in a short list:
   - what was installed and where (the writing kit in the user folder, Python and its packages if installed, the new
     project folder), and how to undo each;
   - the next step: in VS Code, File, then Open Folder, choose the new project folder, trust it, open any file, click
     the Spark icon, and type `/start`. The agent there will ask the remaining questions (what the project is, who is
     never named, where the inbox should be), fill in the project's files, make its Git repository, and check that
     the guard on the originals works. A refusal by the guard in that check is the right result;
   - where to read on: `guide/04-the-first-week.md` for the first week, `guide/02-the-method.md` for why the folder is
     built as it is, and `guide/05-learning.md` for the videos to start with.

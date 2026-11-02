# A starter kit for working with an AI agent in research

*For colleagues who want to work the way I described in the seminar "Working with an AI agent in research" (DTU,
3 November 2026). You do not need to know how to program. Until August 2026 I did not know Python, had never used VS
Code, and did not know how to download a project from GitHub. Everything in this kit was made in conversation with the
agent. The agent also sets the kit up for you, and it explains each step in plain words before it takes it.*

Kevin Michael Smith, DTU, November 2026

## What you are looking at

This page is a **repository** on **GitHub**. A repository is a project folder that is kept together with a record of
every change made to it. GitHub is a website that keeps such folders online, so that others can read and download
them. The list of folders and files at the top of the page is the kit itself. The text you are reading now is the
kit's README, the introduction that GitHub shows below the list.

You do not need a GitHub account to read or download anything here. Most files in the kit have names ending in `.md`.
They are **Markdown** files: plain text with a few marks for headings, bold type and lists, which GitHub shows
formatted. Click any link in this text, or any name in the list at the top, to read that file in your browser. The
browser's Back button brings you back here. You can read everything on a phone, but steps 2 to 5 below need the
computer you will work on.

## What the kit is for

An **AI agent** is an AI program that does more than answer in a chat window. It reads the files in a folder on your
computer, writes and changes them when you ask, and runs small programs for you. **Claude Code**, made by the company
Anthropic, is such an agent. It runs inside **VS Code** (Visual Studio Code), Microsoft's free program for reading and
editing files. Claude Code is installed as an **extension**, an add-on program inside VS Code. You use it in the
**Claude Code panel**, a column at the side of the VS Code window, where you type or dictate in ordinary sentences.
The **Spark icon**, a small star-shaped icon that appears at the top right of the window when a file is open, opens
that panel.

The kit sets you up to do three things with Claude Code.

1. **Keep one knowledge base for each project.** A knowledge base is a folder that keeps every original file of a
   project unchanged: meeting transcripts, documents, papers, data and your own dictated notes. The agent turns each
   original into text, and writes summary pages in which every statement points to the passage it came from. You can
   then put a question to the knowledge base before a meeting, and check each part of the answer against its source.
2. **Capture what is not written down.** Much of what a project knows is said in meetings and never written. The kit
   shows how to transcribe meetings: with Teams, with Meetily (a program that transcribes a meeting in a room), or
   with the kit's own transcription script. It also shows how to dictate your own reasoning with Wispr Flow, a program
   that turns speech into text wherever you can type. The agent then reads what was said and what you think, not only
   what was written.
3. **Make the agent write for you.** Left to itself, an agent often writes short phrases full of jargon. The writing
   kit tells it once who you are and which fields it must explain to you. It then writes complete statements with
   their background.

## What you need before you start

- **A computer with Windows or macOS.** On a DTU laptop, try the installers in guide 01 first. According to their
  makers, VS Code and the Claude Code extension install without administrator rights, which are the rights to install
  programs for every user of a computer. If an installer is blocked, ask DTU's IT support to install VS Code and Git
  for you.
- **A paid Claude plan.** The free plan does not include Claude Code. My recommendation for the first weeks is the Pro
  plan, at 20 US dollars a month, which you buy at claude.ai/upgrade. The section "What it costs" below gives the other
  plans.
- **About two hours**, which you can split over several days. Reading takes about ten minutes, installing about an
  hour (most of it waiting for installers), and the set-up with the agent about half an hour.
- **No programming.** You will see commands and file names on the screen, because the agent shows you what it is about
  to do. You do not need to write them or understand them in advance. The agent explains each one before it runs it,
  and you can always ask it, in your own words, what something means.

## The steps, in order

The five steps below are this README's own. Guide 01 and the set-up file have numbered steps of their own, so this
text names the file whenever it means one of those.

### Step 1. Read about data and the rules (about ten minutes)

Read [guide 06, "Data, privacy and the rules"](guide/06-data-and-the-rules.md) first. It explains which contract
applies to a personal Claude plan: Anthropic's consumer terms, its contract for private customers. It also explains
what those terms mean for the material you may let the agent read. The short version is this: keep other people's
personal or confidential material out of the agent's reach until you know which terms your account is under. This
step comes first because it decides what you may put into your first knowledge base.

### Step 2. Download the kit and unpack it (about five minutes)

1. At the top of this page, above the list of files, click the green button marked **Code**. In the menu that opens,
   click **Download ZIP**. Your browser saves a file named `ai-research-starter-kit-main.zip` in your Downloads folder.
   A zip file is a single file that holds many files and folders packed together.
2. Unpack the zip file. VS Code and the agent cannot work with files that are still packed inside it.
   - **On Windows**, open your Downloads folder in File Explorer, right-click the zip file, and choose **Extract
     All...**. A window opens with a box that shows where the files will go. Click in that box, delete the text in it,
     type `C:\dev`, and click **Extract**. Windows puts the kit in the folder `C:\dev\ai-research-starter-kit-main`.
   - **On a Mac**, double-click the zip file in your Downloads folder. The Mac unpacks it into a folder named
     `ai-research-starter-kit-main` next to it (Safari may already have done this for you). Move that folder into a
     folder named `dev` in your home folder, so that you can find it again.

This folder is the **kit's folder**, and the guides call it that. Later, the set-up makes a second folder for your own
projects: `C:\dev\projects` on Windows, `dev/projects` in your home folder on a Mac. The kit's folder stays as it is,
and you can open it again whenever you want to read a guide.

### Step 3. Install the tools (about an hour)

Follow [guide 01, "Getting started"](guide/01-getting-started.md). It is written for someone who has never used a
terminal, the window in which commands are typed. Steps 1 to 3 of guide 01 install VS Code, Git and the Claude Code
extension. Git is the program that keeps every earlier version of every file, and the agent uses it for you. Step 4 of
guide 01 opens the kit's folder in VS Code. Steps 5 and 6 of guide 01 open the Claude Code panel and sign you in to
your Claude account.

You do not need to install Python, the programming language in which the kit's small programs are written. If your
computer does not have it, the agent installs it during the set-up, after asking you. If that is blocked on a DTU
laptop, ask DTU's IT support to install Python.

### Step 4. Let the agent set you up (about half an hour)

Guide 01 ends with the kit's folder open in VS Code and the Claude Code panel open beside it. If the panel is closed,
click any file in the list of files on the left of the VS Code window. Then click the Spark icon at the top right.
Type or dictate this in the box at the bottom of the panel, and press Enter:

> Read START-HERE.md and set me up.

[START-HERE.md](START-HERE.md) is a set of instructions written for the agent, not for you. The agent follows them
with you, in this order:

1. It checks what is installed on your computer, and installs Python if it is missing.
2. It asks your name, your field, and which fields you want explained to you. It then installs the writing kit, so that
   every later conversation knows how to write for you.
3. It asks you to decide whether Anthropic may use your conversations to train its future models, that is, to improve
   later versions of Claude with them. You find the setting on the Claude website: claude.ai, then Settings, then
   Privacy, then "Help improve Claude". The agent recommends switching it off for research material, so that the
   material is not used for training.
4. It makes your first knowledge base: a new folder for your first project, copied from the kit's template.

While the agent works, the panel often stops and asks your permission. It asks before each command that the agent
wants to run. It also asks before each change to a file outside the kit's folder. Each request shows the agent's
one-line explanation of what it wants to do, and offers a choice:

- Choose the plain **yes** when the request matches what the agent said it would do. It allows this one action only.
- Leave any option that adds "don't ask again" until you know the agent better. It allows the same kind of action from
  then on without asking.
- If you are unsure, choose **no**, and ask the agent in your own words what the command does and why it is needed.

The set-up ends by sending you to your new project's folder. In VS Code, click **File**, then **Open Folder...**, and
choose the folder the agent names, for example `C:\dev\projects\ventilation-study`. Trust the folder when VS Code asks
(step 4 of guide 01 shows how), open the Claude Code panel, and type `/start`. A word that begins with `/` is a
**command**: a short name for a set of written instructions that the kit gives the agent. `/start` completes the
project's set-up, and tests that the agent cannot change your original files.

### Step 5. The first week

Follow [guide 04, "The first week"](guide/04-the-first-week.md). It gives the first five days, each one or two short
conversations with the agent, with the words to type or dictate. Each conversation starts with `/start`, which makes
the agent read where the work stands. Each ends with `/close`, which makes the agent write a record of the day's work
and save it in the project's history. Guide 04 introduces the other commands as you need them:

- `/deposit` adds a new file, such as a transcript or a paper, to the knowledge base.
- `/integrate` updates the summary pages from the files deposited since the last time.
- `/ask` answers a question from the knowledge base, with the source of every statement.

## What is in the kit

You can read every file here on GitHub before you download anything. In VS Code, the same files appear in the list of
files on the left of the window. To see a Markdown file there with its headings and bold type, open it and press
`Ctrl+Shift+V` (`Cmd+Shift+V` on a Mac).

| Part | What it is |
|---|---|
| [START-HERE.md](START-HERE.md) | The instructions that the agent follows to set you up (step 4 above). You do not need to read them, but you may. |
| [guide/01-getting-started.md](guide/01-getting-started.md) | How to install VS Code, Git and Claude Code, step by step, with a table of what to do when something does not work. It also covers the programs for dictation and transcription, which can wait. |
| [guide/02-the-method.md](guide/02-the-method.md) | Why the knowledge base is built as it is: why originals are kept unchanged, and why every statement is traced to its source. About fifteen minutes to read. |
| [guide/03-the-writing-kit.md](guide/03-the-writing-kit.md) | What the writing kit does, and how to change it to suit you. About five minutes. |
| [guide/04-the-first-week.md](guide/04-the-first-week.md) | The first five days after the set-up, with the words to type or dictate (step 5 above). |
| [guide/05-learning.md](guide/05-learning.md) | The few sources I learn from, and the videos to start with. About five minutes, then 8 to 14 minutes for each video. |
| [guide/06-data-and-the-rules.md](guide/06-data-and-the-rules.md) | What the agent can reach on your computer, what the rules say, and what to decide before you give it other people's material (step 1 above). |
| [prompts.md](prompts.md) | Requests to the agent that have worked well for me, ready to copy and adapt. Among them: investigating an idea, making a report in two messages (a plan first, then the text), and reviewing what the agent made. |
| [knowledge-base/](knowledge-base/) | The template for a project's knowledge base, which the set-up copies once for each new project. It holds empty folders, each with a short description, and a rules file with blanks that the agent fills in with you. It also holds the five commands, four small programs, and a file with its one setting (all described below). |
| [writing-kit/](writing-kit/) | Four short files that tell the agent how to write for you, and the small program that installs them in your user folder (the folder that Windows or macOS keeps for your own files and settings). |
| [LICENSE.md](LICENSE.md) | The licences: what you may do with the kit. |

The kit's small programs are **Python scripts**: text files of instructions in the Python language, which the agent
runs for you. You never need to run them yourself. There are five. Four are in each knowledge base, in its folder
`tools`:

- `deposit.py` copies a new file into the folder of originals and records its **checksum**, a fingerprint of the
  file's content that shows later whether it has changed.
- `extract.py` turns PDF, Word, PowerPoint and Excel files into plain text that the agent can read.
- `guard_raw.py` stops the agent from changing or deleting an original.
- `transcribe.py` transcribes a recording of a meeting, with the speakers told apart. Its speech models run on your own
  computer, so the recording is not sent anywhere.

The fifth, `install_kit.py` in the writing kit, installs the writing kit in your user folder. One more Python file in
each knowledge base, `config.py`, is not a program. It holds the knowledge base's one setting: where its **inbox** is,
the folder in which new files wait until the agent deposits them.

## What it costs

| Item | Cost |
|---|---|
| VS Code, Git, Python, and Meetily's free edition | free |
| Claude, Pro plan (needed for Claude Code; my recommendation to start) | 20 US dollars a month |
| Claude, Max plan (for daily heavy use) | 100 US dollars a month |
| Claude, Ultra plan (the most use; Anthropic called it "Max 20x" until 30 October 2026, and older pages still use that name) | 200 US dollars a month |
| Wispr Flow, for dictation | a free plan with a weekly limit on words; the paid plan, Wispr Flow Pro, costs 15 US dollars a month, and half that with an education e-mail address, such as a university's |

Anthropic's plans differ in how much use they allow each week. The prices are those that Anthropic's and Wispr's
pages showed on 31 October 2026.

## If you get stuck

- **Ask the agent.** Describe what you see in your own words, or paste the message on the screen, and ask what it
  means and what to do. Once the writing kit is installed, `/plain` asks the agent to explain its last answer again in
  plain words.
- **Look in guide 01.** Its section "If something does not work", near the end, lists the error messages that
  newcomers meet most often, with what to do about each.
- **Ask me**, if you are at DTU.

## Sharing it, and its licence

You may copy the kit, change it and pass it on, inside DTU or outside it. The kit was written with Claude Code, in
conversation with me, from public advice and my own experience. The texts (the guides, the templates, the rules and
the instructions for the agent) are under the Creative Commons Attribution 4.0 licence. The Python scripts (the files
whose names end in `.py`) are under the MIT licence. [LICENSE.md](LICENSE.md) gives both. A licence is the author's
written permission for others to copy and reuse a work, with its conditions. The conditions of these two are few:
credit the author, and keep the licence with what you pass on. For the texts, also say if you changed them.

## What is left out on purpose

Nothing of my own projects is in the kit: no transcript, note or page of mine. The kit holds the method, not the
content. It is also deliberately small: five scripts, five commands for the agent, and one rules file for each
project. Add to it what your own material needs, when you need it. The agent can help you with that too.

## Terms used

- **AI agent**: an AI program that reads and changes the files in a folder on your computer and runs small programs
  for you, when you ask. Here, Claude Code.
- **Checksum**: a short code computed from a file's content. It changes if the file changes, so it shows that an
  original is still as it was.
- **Claude Code panel**: the column at the side of the VS Code window in which you talk to Claude Code.
- **Command**: in the Claude Code panel, a word that begins with `/`, such as `/start`. It is the short name of a set
  of written instructions that the kit gives the agent.
- **Extension**: an add-on program installed inside VS Code. Claude Code is one.
- **Git**: the program that keeps every earlier version of every file in a project. The agent uses it for you.
- **GitHub**: a website that keeps repositories online.
- **Inbox**: the folder in which new files wait until the agent deposits them in a knowledge base.
- **Kit's folder**: the folder into which you unpacked the kit, for example `C:\dev\ai-research-starter-kit-main`.
- **Knowledge base**: one project's folder, in which every original is kept unchanged and every statement the agent
  writes is traced to its source.
- **Markdown**: plain text with a few marks for headings, bold type and lists. Files in Markdown end in `.md`.
- **Python**: a programming language. The kit's five small programs are written in it.
- **Repository**: a project folder kept together with the record of every change made to it.
- **Spark icon**: the small star-shaped icon that opens the Claude Code panel. It appears at the top right of the VS
  Code window when a file is open.
- **Terminal**: a window in which commands are typed. The agent uses it for you.
- **VS Code** (Visual Studio Code): Microsoft's free program for reading and editing files, in which Claude Code runs.
- **Zip file**: a single file that holds many files and folders packed together. It must be unpacked before use.

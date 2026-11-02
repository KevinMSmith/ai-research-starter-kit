# 3. The writing kit: making the agent write for you

*What the writing kit does, how it is installed, and how to make it fit you. About five minutes to read.*

## The problem it solves

An AI agent writes, by default, for someone who already knows what it knows. Its reports and summaries are often
correct but hard to use: short, choppy statements full of terms from software or from your own project, with no
background to interpret them by. An example of the kind of sentence it writes:

> "Server mode exits after ~10 min offline; phone loses session."

(a note about the program that links a home computer to a phone), and what a newcomer to the subject needs instead:

> "If my home computer is offline for about ten minutes, the program that links it to my phone stops, and the phone
> loses the conversation."

The second version is not longer for the sake of it. It names each thing and gives the background, so that it can be
understood on the first reading.

## What it is

Four small files, installed once in your user folder, so that they apply in every project on the computer. On
Windows, your user folder is `C:\Users\<you>`, where `<you>` is your user name; on a Mac it is `/Users/<you>`. The
files go into its subfolder `.claude`, the folder in which Claude Code keeps its settings. An **output style** is a text
that Claude Code adds to its instructions for every answer; a **skill** is a written procedure the agent follows when
you type its command; and an **agent** in this table is a second, separate AI helper with one job:

| File | Where it is installed | What it does |
|---|---|---|
| `user-instructions.md` | `C:\Users\<you>\.claude\CLAUDE.md` (the file every Claude Code conversation reads first) | says who you are, which fields you know, which you need explained, and twelve rules for writing for you |
| `output-styles/plain-teaching.md` | `C:\Users\<you>\.claude\output-styles\`, and set as the default style | adds the same rules, with an example, to every answer in the conversation |
| `skills/plain/SKILL.md` | `C:\Users\<you>\.claude\skills\plain\` | the command `/plain`: "explain that again, for a newcomer", for the previous answer or a named document |
| `agents/second-reader.md` | `C:\Users\<you>\.claude\agents\` | an agent that reads a finished document as a newcomer and lists what it could not follow; it never edits |


## How to install it

The easy way: ask the agent to do it with you (`START-HERE.md` in the starter kit's folder, step 2). It asks for your
name, your field and the fields you want explained, fills in the blanks in `user-instructions.md`, and runs the install
script. By hand: fill in every blank marked ‹like this› in `writing-kit/user-instructions.md`. Then open VS Code's
terminal (the menu **Terminal**, then **New Terminal**: a text window at the bottom of VS Code in which you type a
command and press Enter), check that it shows the starter kit's folder, type the following line, and press Enter:

    python writing-kit/install_kit.py

The script keeps anything already in your `CLAUDE.md` and in your settings file
(`C:\Users\<you>\.claude\settings.json`), and makes a dated backup copy of the settings file first. The same line with
` --check` added at the end shows what is installed; with ` --uninstall` it removes it all again. A change takes
effect in the next conversation, not the current one: open a new conversation in the Claude Code panel.

## How to make it yours

- **Edit `writing-kit/user-instructions.md` and run the script again** whenever you want to change something. Do not
  edit the installed copy: the next installation would overwrite it.
- **The section "Who reads what you write" matters most.** Name your field precisely, so that the agent does not
  explain your own terms to you, and name the fields you want explained.
- **When an answer is still hard to follow, type `/plain`.** The agent explains the same content again, with the terms
  defined and the background given.
- **When the agent uses an invented word for a standard thing**, add it to the table "Terms never to use" at the end
  of `user-instructions.md`, with the standard term, and reinstall.
- **Before you send a long document to someone**, ask: "Ask the second-reader agent to read this; the reader already
  knows ‹what they know›." Fix what it finds that is real. Telling it what the reader knows matters: without that line,
  about a third of what it lists are terms the reader knows well (a test on 31 October 2026, on two guides written for
  the author of this kit).

## What it does not do

It changes how the agent writes for you, not how it works: code, commands, file contents and numbers stay exact. It
does not apply to records meant for the agent itself, such as cards and indexes, which stay compact. And it does not
replace a project's own rules: a project that writes for students, for example, keeps its own way of writing in its
rules file, `AGENTS.md`, which the agent follows where the two differ.

## Terms used

- **Output style**: a text that Claude Code adds to its instructions for every answer in a conversation.
- **Skill**: a written procedure the agent follows when you type its command, such as `/plain`.
- **Terminal**: a text window, here at the bottom of VS Code, in which you type a command and press Enter.
- **User folder**: your own folder on the computer, `C:\Users\<you>` on Windows, where `<you>` is your user name.

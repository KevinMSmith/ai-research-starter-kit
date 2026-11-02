# A starter kit for working with an AI agent in research

*For colleagues who want to work the way I described in the seminar "Working with an AI agent in research" (DTU,
3 November 2026). You do not need to know how to program. Until August 2026 I did not know Python, had never used VS
Code, and did not know how to clone a repository from GitHub; everything in this kit was made in conversation with
the agent.*

Kevin Michael Smith, DTU, November 2026

## What it is for

An **AI agent** is an AI program that does not only answer in a chat window: it reads the files in a folder on your
computer, writes and changes them when you ask, and runs small programs for you, explaining what it does. **Claude
Code**, made by the company Anthropic, is such an agent; it runs inside **VS Code**, Microsoft's free editor for files.
The kit sets you up to do three things with it:

1. **Keep one knowledge base per project**: a folder that holds every original (transcripts, documents, papers, data,
   your own dictations) unchanged, turns each into text, and lets the agent write pages and products in which every
   statement is traced to its source.
2. **Capture what is not written down**: transcribe meetings (Teams; or Meetily, a program that records the sound in a
   room and turns it into text on your own computer) and dictate your reasoning (Wispr Flow, a program that turns
   speech into text wherever you type), so that the agent works from the whole of what you know.
3. **Make the agent write for you**: complete statements with their background, every term from outside your field
   explained, instead of short phrases full of jargon.

## What is in it

| Part | What it is |
|---|---|
| `START-HERE.md` | the set-up, which the agent carries out with you: you say "Read START-HERE.md and set me up" |
| `guide/01-getting-started.md` | installing VS Code, Git, Claude Code, Wispr Flow and Meetily, step by step, before the set-up |
| `guide/02-the-method.md` | why the knowledge base is built the way it is |
| `guide/03-the-writing-kit.md` | what the writing kit does, and how to make it yours |
| `guide/04-the-first-week.md` | the first five days, with the words to type or dictate |
| `guide/05-learning.md` | the few sources I learn from, with the videos to start with |
| `guide/06-data-and-the-rules.md` | what to settle about data, privacy and the rules before the first session |
| `prompts.md` | prompts that work |
| `knowledge-base/` | the template of a knowledge base: the folder that the set-up copies once for each new project, with its scripts (among them `tools/transcribe.py`, which transcribes a recording on your own computer) |
| `writing-kit/` | the writing kit: four short files that tell the agent how to write for you, and the script that installs them |

## The order

1. Read `guide/06-data-and-the-rules.md` (eight minutes). It explains that a personal Claude plan comes with the
   provider's consumer terms (its contract for private customers), and what that means for the material you may give
   the agent to read.
2. Install the tools with `guide/01-getting-started.md` (about an hour, most of it waiting for installers).
3. Download the kit from its page, https://github.com/KevinMSmith/ai-research-starter-kit: press the green "Code"
   button and choose "Download ZIP". Unpack the zip file into a folder you can find again, for example
   `C:\dev\starter-kit`. Open that folder in VS Code,
   open Claude Code, and say: "Read START-HERE.md and set me up." (About half an hour.)
4. Follow `guide/04-the-first-week.md`.

## What it costs

VS Code, Git, Python and Meetily's free edition cost nothing. Claude Code needs a paid subscription to Claude (the
free plan does not include it). Anthropic's plans are called Pro, Max and Ultra and differ in how much use they allow
per week. The Pro plan (20 US dollars a month) is enough to start; daily heavy use needs the Max plan (100 US dollars a
month) or the Ultra plan (200 US dollars a month; Anthropic renamed its former "Max 20x" plan "Ultra" on 30 October
2026). Wispr Flow has a free plan with a limit on the words per week (its home page says 2 000; its pricing page now
gives no number), and its paid plan, Wispr Flow Pro, is half price with an education e-mail address. Prices as the
makers' pages showed them on 31 October 2026, in US dollars.

## Sharing it, and its licence

You may copy the kit, change it and pass it on, inside DTU or outside it. The kit was written with Claude Code, in
conversation with me, from public advice and my own experience. The texts (the guides, the templates, the rules and
the instructions for the agent) are under the Creative Commons Attribution 4.0 licence, and the Python scripts (the
files whose names end in `.py`) are under the MIT licence. `LICENSE.md` gives both. A licence is the author's written permission for others to copy and
reuse a work, with its conditions. Both of these licences ask only that the author is credited.

## What is left out on purpose

Nothing of my own projects is in the kit: no transcript, note or page of mine. The kit holds the method, not the
content. It is also deliberately small: five scripts, five commands for the agent (`/start`, `/deposit`,
`/integrate`, `/ask` and `/close`, which you type in the Claude Code panel; guide 04 shows when), and one rules file
per project. Add to it what your own material needs, when you need it.

# 4. The first week

*What to do in the first week after the set-up, day by day, with the words to type or dictate. Each day is one or two
short conversations with the agent. Each starts with `/start` and ends with `/close`: commands that come with the
template, which you type in the Claude Code panel. `/start` makes the agent read where the work stands and check the
originals; `/close` makes it write the day's record and save the step in the project's history. `/ask` and `/plain`,
used below, are commands of the same kind. The last section is a review of the set-up after about a month.*

## Before day 1

The set-up (`START-HERE.md`) has made your project folder, its inbox, and the writing kit. Open the project folder in
VS Code (File, Open Folder), and open Claude Code there. Every conversation about this project starts in this folder,
because that is where the agent finds the rules file and the guard.

## Day 1: the first deposits

1. Put into the inbox two or three recent meeting transcripts, the three or four documents that define the project (a
   proposal, a report, a plan), and a few of the papers it rests on.
2. Dictate for five to ten minutes: open Notepad, dictate with Wispr Flow (or type), and save the file in the inbox.
   Say what the project is, what it should produce, what you believe and what you are unsure of. Do not tidy it.
3. In Claude Code: `/start`, then:

   > Deposit everything in the inbox. Read each file and write its card. Tell me what each one holds that matters
   > for the project.

   (A card is the agent's index of one source, every item with the paragraph it came from; guide 02 explains it.)

4. Read the agent's report. Then `/close`.

## Day 2: what is missing

> Read all the cards. Tell me what the material covers, what it claims without support, where the sources disagree,
> and what is missing that only I can supply. End with a list of questions for me to dictate answers to.

Read the list of questions first. It is the most useful thing the agent writes in the first week, because it shows what
is in your head and nowhere else.

## Day 3: dictate against the questions

Dictate your answers into the inbox, one file each time you dictate. Then:

> Deposit the new dictation and write its card. Where it changes or contradicts an earlier source, say so.

## Day 4: the first pages

> Integrate the cards into the knowledge base. Show me the pages you would write before you write more than ten.

The agent writes the first pages in `kb/` (the folder of curated pages), each statement with its source. Open two or three of them and read them as
a reviewer would: is every number's basis given, is anything stated that you never said? Tell it what is wrong.

## Day 5: ask it something

Before your next meeting on the project:

> /ask What do we know about ‹the subject of the meeting›, and what is still open?

A knowledge base that is never asked anything is an archive. Asking it before meetings is what makes it useful, and
shows where its sources are weak or missing.

## Habits from then on

- **Every meeting transcribed, every useful e-mail saved, into the inbox the same day.** Save an e-mail as an .eml
  file, the plain form of a mail message with its headers and body, because that is the one mail format the kit's
  scripts read. In the new Outlook for Windows and in Outlook on the web, right-click the message and choose Save as,
  or drag it into the inbox folder; either gives an .eml file (a Microsoft Q&A answer and CodeTwo's knowledge base,
  both third-party pages, say so; Microsoft's own pages describe only how to open one). Classic Outlook's Save As
  gives its own .msg format, which the scripts do not read; choose Text Only there, or use Outlook on the web. When
  several messages of one thread would get the same name, add each message's date to the end of its name. Download
  a Teams transcript from the meeting's chat after the meeting (the organiser can download it as a .vtt file).
  Deposit once a week, or when you need the material.
- **Correct by dictation, and when you correct the same thing twice:** "Make that a rule, with the reason, where it
  will act." The agent chooses the skill, the setting or `AGENTS.md`, and tells you which.
- **One task, one conversation.** Start with `/start`, end with `/close`, and begin the next task in a new
  conversation.
- **Judge the product.** Open the document, the slides or the table before you read the agent's account of it.
- **Ask for the decisions.** "List every decision you took without asking, each with your recommendation and the
  reason, so that I strike only those I disagree with."

## After a month

After about a month, the set-up will not fit your work exactly. Some folders of the template will still be empty,
some steps you will be doing by hand every week, and some corrections you will have made more than once. Ask the
agent to look at how the knowledge base has actually been used, and to propose changes:

> Read the log, PROGRESS.md, DECISIONS.md and the folder tree of this project. Tell me which folders and which skills
> I have not used, which steps I keep doing by hand, and which corrections I have made more than once. Propose what to
> remove, what to add to the rules file, and what to make a skill, each with its reason. Change nothing until I agree.

Strike the proposals you disagree with, as with any other list of decisions. Repeat the review when the work changes,
for example when a project moves from collecting material to writing. If you use Johannes Wildfeuer's kit, its skill
"workflow health" does the same job across all your projects.

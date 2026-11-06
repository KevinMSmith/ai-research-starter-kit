# 2. The method: why the knowledge base is built the way it is

*For a researcher who wants to understand the method before using it. About fifteen minutes to read. The template in
`knowledge-base/` (the part of this starter kit that the set-up copies to become each project's folder) puts all of it
into practice; this guide says why each part is there.*

## The idea in one paragraph

An AI agent is an AI program that works on the files in a folder on your computer: it reads them, writes and changes
them when you ask, and runs small programs for you. An agent such as Claude Code can read, summarise, compare,
calculate and draft at a speed no person can match, but it can only work from what it is given, and it fills any gap
fluently. The method answers both facts. You give it the
whole of what you know, including the part that is written down nowhere. And you keep that material in a folder
where every original stays unchanged and every statement the agent writes can be traced back to the passage it rests
on. That folder is the **knowledge base**: one per project, made of plain text files, kept under version control (a
record of every change, so nothing is lost), and read and written by the agent under rules you write down once.

The pattern of an unchanged layer of sources, a layer the agent writes, and a rules file was published by Andrej
Karpathy (a founding member of OpenAI) on 4 April 2026, in a short public note on GitHub titled "LLM Wiki". LLM stands
for large language model, the kind of AI behind Claude; a wiki is a set of linked pages. The template adds what
research material needs: a checksum on each original (a fingerprint that shows whether the file has changed), a guard
hook that enforces the rule that originals are never changed, a card per source, and the label "Inferred" for
everything the agent concluded itself rather than read in a source. It is a starting point, to be adapted to what you
need.

## Three habits come first

**Most of what a researcher knows is not in their documents.** It is in meetings, lectures and conversations, and in
their head. The documents are already files; the other two become files only if you make them so.

1. **Transcribe every meeting and lecture.** On Teams, the organiser can download the transcript after the meeting
   (Teams shows every participant that it is transcribing). For a meeting in a room, a local transcription program
   such as Meetily records the computer's audio and transcribes it on the computer itself; the paid version separates
   the speakers. Tell the people present that the meeting is transcribed and why. A local program shows them nothing,
   so telling them is your duty.
2. **Dictate.** Whenever you have more than a few sentences to say, say them: the first idea for a concept, your
   reaction to a draft page by page, a correction, the reasoning behind a decision. A dictation program such as Wispr
   Flow turns speech into text wherever the cursor is, and keeps a personal dictionary of the names and terms of your
   field. Do not edit what it writes; the agent reads through the errors. Your reasoning, in your own words, is what
   lets the agent write your argument instead of a generic one.
3. **Put everything into the project's inbox at once**: transcripts, dictations, e-mails (saved from the mail
   program as .eml files, the plain form of a mail message, which is the one mail format the kit's scripts read),
   papers, reports, data. The inbox is an ordinary folder outside the knowledge base, where files keep their original
   names until they are deposited. When several messages of one thread would get the same name, add each message's
   date to the end of its name.

## The folder, layer by layer

Everything flows one way, and nothing downstream is written without a trace back to an original.

| Layer | What it holds | Who writes it | Changes? |
|---|---|---|---|
| inbox (outside) | files as they arrive, under their original names | you | yes |
| `raw/` | the originals, each under a short permanent ID, with a checksum | you, through the deposit script | never |
| `sources/` | each original as plain text with numbered paragraphs, and one card per source | a script, and the agent | made again from `raw/` |
| `kb/` | the curated knowledge: pages on one subject each, every statement with its source | the agent, under the rules | yes, with footnotes |
| `products/` | papers, reports, slides, teaching material | the agent and you | rebuilt after every correction |

**The deposit.** When you say a file in the inbox should go into the knowledge base, the agent runs a small script (a
short program written in Python, which the agent runs for you) that copies it into `raw/` under an ID such as `M04`
(the fourth meeting) or `K02` (your second dictation), and writes its checksum into the list `raw/MANIFEST.md`. A checksum is a fingerprint of the file's bytes: change one byte and the fingerprint
changes, so a check can prove later that nothing in `raw/` has been altered. The letters of the ID say what a thing is
and how much weight it carries: your dictation (`K`) states your position, a paper (`R`) its published claim, a
colleague's slides (`C`) only context.

**The sources and the cards.** A second script turns each original (PDF, Word, PowerPoint, Excel, a Teams transcript,
an e-mail) into plain text with numbered paragraphs, so that a passage can be cited as `M04¶12`, paragraph 12 of meeting 4 (¶ is the paragraph sign). Then the agent writes a
**card** for each source, from that source alone. The card lists what the source holds, item by item, each with its
paragraph number. It keeps three things apart: what was proposed, what was decided, and where people disagreed. A card
is an index: whenever a later page needs a reason or a number, the agent goes back to the passage itself.

**The curated pages.** From the cards, the agent writes pages in `kb/` on one subject each: how a system works, a
decision and its reasons, a measured result, the assumptions behind a calculation, the open questions. The types of
page are not fixed in advance; a type gets its own folder when its third page would be written, because a structure
invented before the material has been read is usually wrong.

## The rules, and why each exists

The rules file, `AGENTS.md`, is the file the agent reads at the start of every conversation. The template's rules
each exist because an agent gets the thing wrong without them.

- **Deposit, never edit.** An original is never changed; a correction is made downstream, and a later version of a
  document is a new deposit beside the old one. *Why:* everything the agent writes must be traceable to something it
  was given, a year later as much as today.
- **A guard hook, not only a rule.** A rule in a text file is something the agent reads, and in a long session it can
  be forgotten. So a small script, the **guard hook**, runs before every edit and every command the agent makes, and
  refuses any that would change `raw/`. (A hook is a script that Claude Code runs automatically before each action.)
  The agent cannot get round it by forgetting.
- **Every claim says what it rests on.** Every factual statement in `kb/` carries a footnote to the passage that said
  it (a note at the foot of the page, such as `M04¶12`), or sits under a heading "Inferred". There is no third option. *Why:* the failure of a capable model is not that it
  knows too little, but that it fills gaps smoothly; this rule makes each gap visible where it would do harm.
- **Every number carries its basis**: measured, simulated, calculated, a design value, estimated, or stated by
  someone. A figure measured in one building for one season, and the same figure scaled up to a national market, are
  both legitimate and not the same kind of claim.
- **The later word wins.** When you change your mind, the later dictation stands, the change is recorded with its
  date, and the earlier text is kept and marked as replaced.
- **People by role.** A participant is named by their role in the project, never assessed, and anyone who has not
  agreed (students, residents) is never named. What the agent reads is sent to the provider's servers, and an opinion
  about a named person is personal data under the GDPR (the General Data Protection Regulation of the European Union).
- **Judge the product.** A slide deck is opened and read slide by slide, a text is read, a calculation is
  recalculated, before it is called done.
- **Test a check that finds nothing.** When the agent writes a search or a filter of its own ("which rooms exceed
  1 000 ppm?") and it returns nothing, it first runs it on a case that should be found. A filter with a wrong sign
  and a filter that finds no case give the same empty answer.
- **Ask before the git commands that lose work.** The template's settings make the agent ask you before it runs the
  few Git commands that throw away work no commit has saved, or rewrite what is on GitHub (`git reset --hard`,
  `git clean`, a forced push, among others). Say no unless you asked for it.

## How a round of work runs

A round starts when you dictate: what you believe, what you want to know, what you want made. The agent then works:
it sends questions that need online sources to **background agents** (copies of itself that research one question each
and write one file each, with the address and date of every source); it reads, calculates, drafts and builds; and it
writes down every decision it took on your behalf, each with a recommendation and its reason. You then **open the
product first, not the plan**, and say what is wrong, by dictation. You strike only the decisions you disagree with.
Then the next round.

**Corrections become rules, the same day.** When you correct the same thing twice, ask the agent to make it a rule,
with its reason. A rule that lives only in a conversation is lost when the conversation ends; a rule in a file is read
by every later conversation. The agent puts the rule where it will act: a step of one task (depositing, writing a
page) goes into that task's skill, which is read only when the task runs; a rule a script could enforce becomes a
setting or a hook, after your yes; only a rule for all ordinary work goes into `AGENTS.md`. The reason is that
`AGENTS.md` is read in every conversation, and a file crowded with rules that apply only now and then is followed less
reliably. Anthropic suggests about 200 lines as a rough guide (Claude Code documentation, "How Claude remembers your
project", read 6 November 2026); a longer file is fine when its rules all apply to ordinary work.

## Why the files are the memory

A conversation with the agent ends and is forgotten; the next conversation starts empty. The method therefore keeps the
memory in the folder, in four files the agent reads and writes:

- `PROGRESS.md`, the **resume point**: one screen that says where the work stands, what was checked, and what is open.
  It is rewritten at the end of every session, never added to.
- `log/`, the **log**: one short block per session, added at the end, never changed: the history.
- `DECISIONS.md`: every decision with its date and reason, and what it replaced.
- `AGENTS.md`: the rules, which grow from your corrections.

So the practice is **one task, one conversation**, where a conversation is one session with the agent in the Claude
Code panel. A conversation starts with the command `/start`, which you type in the panel (it comes with the template):
the agent reads the resume point and checks the originals. It ends with `/close`: the agent writes the log block,
rewrites the resume point and saves the step in the project's history. The next task starts in a new conversation. A short, focused conversation gives better
answers and uses less of your plan's allowance, and nothing is lost because the files hold it.

## What it costs, and what it does not do

It costs a subscription (Claude's Pro plan at 20 US dollars a month is enough to start; heavy use needs the Max plan
at 100 US dollars or the Ultra plan at 200 US dollars a month; Anthropic's prices on 31 October 2026), your habit of recording and dictating, and your time to read what the agent
makes. In my judgement it does not save time overall, and no measurement I know of shows that it does: the time moves from
writing to reading and dictating, and the reading is where the quality comes from. It does not need a developer: the agent writes and runs the scripts, and
explains them when you ask.

## Terms used

- **Knowledge base**: the project's folder of plain text files, which the agent reads and writes under written rules.
- **Original**: a file as you received or made it (a transcript, a paper, a dictation), deposited unchanged in `raw/`.
- **Checksum**: a fingerprint computed from a file's bytes, which changes if a single byte of the file changes.
- **Card**: the agent's index of one source, every item with the number of the paragraph it comes from.
- **Hook**: a small script that Claude Code runs before each action of the agent, and which can refuse the action.
- **Version control (Git)**: a record of every change to every file, so that any earlier state can be recovered.
- **Background agent**: a copy of the agent that researches one question on its own and writes one file.
- **Agent**: an AI program that reads and changes the files in a folder and runs small programs when you ask; here,
  Claude Code.
- **Inbox**: the folder outside the knowledge base where new material waits until it is deposited.
- **.eml file**: a mail message saved as plain text with its headers and body, which is the one mail format the kit's
  scripts read.
- **Deposit**: copying an original into `raw/` under a permanent ID, with its checksum recorded.
- **Script**: a short program; the template's are written in Python, and the agent runs them for you.
- **Inferred**: the heading under which the agent writes what it concluded itself, as opposed to what a source says.
- **Rules file**: `AGENTS.md`, the file the agent reads at the start of every conversation in the project.
- **Conversation**: one session with the agent in the Claude Code panel; the next task starts a new one.

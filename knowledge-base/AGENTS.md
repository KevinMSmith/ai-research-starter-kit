# ‹Project name› — the knowledge base

‹One paragraph, kept current: what this project is, who it is for, what it should produce, and where it stands.
For example: "A knowledge base for the research project X, 2026 to 2028: the meetings, the documents, the data and my
reasoning, so that papers, reports and teaching material can be written from it with every claim traced to a source.">

The state of the work is `PROGRESS.md`, one screen, read first. The session log is `log/`, one file a month,
append-only. The plans are in `plan/`. The decisions, with their dates and reasons, are in `DECISIONS.md`.

## Layers

Everything flows one way: from the inbox, to the originals, to the rendered sources, to the curated knowledge, to the
products. Nothing downstream is written without a trace back to an original.

    inbox          outside the repository (tools/config.py): files under their original names, as they arrive
    raw/           the originals, deposited under IDs; never edited; every file checksummed in raw/MANIFEST.md
    sources/       each original rendered to plain text with numbered paragraphs (<ID>.md), and one card per
                   source (sources/cards/<ID>.md): an index of what the source holds, with an anchor on every item
    kb/            the curated knowledge: pages by type, every factual statement footnoted to a source or marked inferred
    products/      what is made from the knowledge base: papers, reports, slides, teaching material
    research/      third-party research by background agents, one file per question, with an index
    plan/          plans and briefs
    log/           the session log, one file a month
    templates/     the shapes of a card, a page, a log block and a research brief
    tools/         the scripts: deposit, extract, and the guard hook

| Layer | Who writes it | Changes? |
|---|---|---|
| `raw/` | the author, through `tools/deposit.py` | never |
| `sources/<ID>.md` | `tools/extract.py` | made again from `raw/`, never edited by hand |
| `sources/cards/` | the agent, one card per source, from that source only | corrected when wrong |
| `kb/` | the agent, under the rules below | yes, with footnotes |
| `products/` | the agent and the author, from `kb/` and the sources | rebuilt after every correction |

## Deposit convention

A deposit copies a file from the inbox into `raw/` under a short permanent ID (`python tools/deposit.py add "<file>"
<ID> "<what it is>"`). The ID's letters say what the thing is and how much weight it carries; its number is the order
in which it arrived. `python tools/deposit.py next K` gives the next free number.

| Class | What it is | Weight |
|---|---|---|
| `K` | a dictation of the author's: an idea, a reaction to a draft, a correction | the author's position; a later dictation wins over an earlier one |
| `M` | a meeting or a lecture: its transcript, with its slides under the same ID | what was said, by role |
| `E` | an e-mail thread | what was written |
| `D` | a document: a report, a proposal, a note, a drawing | as its author and date warrant |
| `R` | a paper or a book chapter | the published claim |
| `X` | data: a spreadsheet, a measurement series, a model or its results | measured or simulated, as labelled |
| `S` | a standard or another licensed text | read; never redistributed or published in full; a product may quote a short clause with its reference |
| `C` | what a colleague wrote or said | cited with the colleague's name when used, unless the owner of this repository says it is context only (read for background, not cited) |
| ‹add a class› | ‹when a third item of a new kind arrives› | |

A later version of a deposited document is a new entry beside the old one (`D04-r2`); the difference between the two
is itself a finding.

## Rules in force

Each rule exists because an agent gets it wrong without it.

1. **Deposit, never edit.** Nothing in `raw/` is edited, renamed or deleted. A correction is made downstream. *Why:*
   everything the agent writes must be traceable to something it was given; an unchanged, checksummed original is what
   keeps "where does this come from?" answerable a year later. The guard hook (`tools/hooks/guard_raw.py`) refuses any
   tool call that would change `raw/`, because a rule that has to be remembered is forgotten in a long session.
2. **Every claim says what it rests on.** Every factual, numerical or contractual statement in `kb/` and in a product
   carries a footnote to the passage that said it (`M03¶12`), or sits under a heading `### Inferred`. There is no third
   option. *Why:* a capable model fills gaps fluently; this rule makes every gap visible.
3. **Stated and inferred stay apart.** A reason a person gave is quoted or footnoted; a reason the agent reconstructed
   is marked as the agent's. *Why:* an inference presented as the author's position will be repeated as the author's.
4. **Every number carries its basis**: measured, simulated, calculated, design value, estimated, or stated by someone,
   with the source or the derivation. *Why:* a measured figure from one case and an estimate scaled from it are both
   legitimate and not the same kind of claim.
5. **The later word wins.** When a later dictation or decision contradicts an earlier one, the later one stands, the
   conflict is recorded in `DECISIONS.md`, and the earlier text is kept, marked as superseded. Never average two
   positions.
6. **Only what is sure.** A figure from a standard, a regulation or a datasheet is checked against the deposited
   document before it enters a product. A number from memory is a number to check.
7. **People.** People are named as the sources name them. ‹Who is never named in this project, for example students,
   residents, patients, or anyone who has not agreed.› A name is withheld only by a rule the author set. ‹Where the
   project needs it: people are never assessed. *Why:* what the agent reads is sent to the provider, and an opinion
   about a named person is personal data under the GDPR.›
8. **One home per fact.** Each fact lives on one page of `kb/`; every other mention links to it. No page has a word
   limit; a page is as long as its content needs.
9. **A folder or a page type is made when its third entry would be written**, not before. *Why:* a structure invented
   before the material has been read is wrong.
10. **The product is judged, not the plan.** A slide deck is rendered and read, a text is built and read, a
    calculation is recalculated, before it is called done.
11. **A check that finds nothing is tested first.** Before the agent reports that a search, a filter or a
    classification it wrote found nothing ("no room exceeds the limit"), it runs the check on a case that should
    trigger it. *Why:* a check that cannot fire and a check that finds no case give the same empty answer.
12. ‹Add each correction the author makes twice, the same day, with its reason.›

## Terms in force

The standard names of things in this project, and the words never to use for them. A term enters this table when the
author corrects one.

| Write | Never write | Note |
|---|---|---|
| | | |

## Working process

1. **A session starts with `/start`**: it reads `PROGRESS.md` and this file, checks `raw/` (`python tools/deposit.py
   verify`), and lists what is new in the inbox.
2. **One unit of work, one session.** A new task starts in a new conversation, which reads the resume point instead of
   the old conversation. *Why:* a focused conversation answers better and costs less, and the files hold the memory.
3. **Commit after each unit of work**, with a message that says what and why. Git keeps every earlier version.
4. **A session ends with `/close`**: one block appended to the month's file in `log/`, `PROGRESS.md` rewritten (never
   appended to, one screen), a commit, and a push when a remote exists.
5. **A correction becomes a rule the same day, in the place where it will act.** When the author corrects the same
   thing twice, the rule goes where it fires at the right moment: a step of one task (depositing, integrating, closing)
   goes into that skill; a rule that a script could enforce (a folder never written, a command never run) is proposed
   to the author as a hook or a setting; only a rule for ordinary work comes into this file, as one line with its
   reason. The story of the correction goes into `DECISIONS.md`. *Why:* every line of this file is read in every
   session, and a file full of rules that apply only now and then is followed less reliably. Anthropic suggests
   about 200 lines as a rough guide; it is not a limit.
6. **Research is fanned out.** A question that needs online sources goes to a background agent with a brief in
   `plan/` that names the one file it writes in `research/`; it quotes every source with its address and the date read,
   marks what it could not verify, and runs no git command. The session reads the file and writes its index line.

## The author

‹Name, position and field. What the author knows well and what must be explained to them. How they like to work: for
example "recommend per decision so that I strike only what I disagree with". The way the agent writes for the author
in general is set once for all projects by the writing kit, in the user folder; only what is particular to this
project goes here.›

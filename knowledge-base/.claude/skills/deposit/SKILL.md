---
name: deposit
description: Use when the author says a file is in the inbox for this knowledge base, or names one to deposit: a transcript, a dictation, a document, an e-mail, a paper, data. Deposits it into raw/ under the next ID, renders it to text, writes its card, and commits.
---

# Deposit: from the inbox into raw/, rendered, carded, committed

`raw/` holds the originals, and the guard hook refuses any direct write to it. A deposit goes through
`tools/deposit.py`, which copies the file under its ID, checksums it and lists it in `raw/MANIFEST.md`.

1. **Identify.** For each file: what it is, its date, its ID class from the table in `AGENTS.md`, and the next number
   (`python tools/deposit.py next <CLASS>`). A later version of a deposited document is `<ID>-r2`. If the class is not
   clear, ask the author in one sentence, with a recommendation.
2. **Deposit.** `python tools/deposit.py add "<file name in the inbox>" <ID> "<what it is, in one line>"`, then
   `python tools/deposit.py verify`.
3. **Render.** `python tools/extract.py <ID>`. If a package is missing, the script names the command that installs
   it; ask before installing. A kind of file the script does not render is read directly if possible.
4. **Card.** Read `sources/<ID>.md` and nothing else, and write `sources/cards/<ID>.md` from `templates/card.md`: what
   the source holds, item by item, each with its anchor (`¶n`); what was proposed, decided and disagreed, kept apart;
   every number with its unit and basis; the questions it raises. Write "None" under an empty heading. A card is as
   long as the source's content needs. Quote nothing longer than a phrase.
5. **Commit** with a message that names the ID and what it is, for example "Deposit M04: project meeting of
   3 November 2026, transcript and card".
6. **Report** in two or three sentences what the source holds that is new for the project, and anything in it that
   contradicts an earlier source.

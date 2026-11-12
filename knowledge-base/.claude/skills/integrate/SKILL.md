---
name: integrate
description: Use when the author asks to update the knowledge base from new sources, or after several deposits. Reads the new cards and the current kb/, and writes or updates the pages in kb/ under the rules of AGENTS.md, with every statement footnoted or marked inferred.
---

# Integrate: from the cards into kb/

1. **Find what is new**: the cards written since the last integration (the last log block says which IDs were
   integrated). Read them, and read `kb/index.md`.
2. **Plan before writing.** List for the author which pages you would add or change and why, in a short table. If the
   change is small (a few pages), go on. If it adds a new type of page, or more than about ten pages, show the table
   and wait. In an unattended session, write the table into the log block instead and continue; the author strikes
   afterwards what they disagree with.
3. **Write.** Go back to the source passage whenever the card is not enough, above all for a reason, a number or a
   disagreement. Every factual statement gets a footnote to its passage (`M03¶12`); what you conclude yourself goes
   under `### Inferred`. Keep stated and inferred reasons apart. Each fact has one home; elsewhere, link to it. When a
   later source contradicts an earlier one, the later one wins, the conflict goes into `DECISIONS.md` if it concerns a
   decision, and the earlier statement is marked as superseded, not deleted.
4. **Make a page type when its third page would be written**, not before (`AGENTS.md`, rule 9).
5. **Update `kb/index.md`**, commit, and name in the log block the IDs that were integrated.

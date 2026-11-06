# Prompts that work

*Words to type or dictate to the agent, collected from the practice behind this starter kit. Change the words in
‹brackets›. Dictating them works as well as typing.*

## Investigating an idea

> I am interested in ‹subject›. This is what I believe: ‹…›. This is what I am curious about: ‹…›. Send background
> agents to find out what is known about it from reliable sources, each with the address and the date of every source.
> Work through this calculation: ‹…›. Then tell me where the idea holds, where it does not, and what you would ask me.

The pattern behind it, in the words of the researcher who uses it: go and research, simulate, calculate, "until the
results get to a place where I feel comfortable with the idea and I get some pushback, and then I'll dictate again."

## Making a product in two messages

1. > Read ‹the sources or pages› and plan ‹the report, the paper section, the slides›. Write the outline and the
   > sources each part will use, and stop there for my review.
2. > ‹Your corrections, dictated.› Now write it to the plan, and list at the end every decision you took, each with
   > your recommendation and the reason.

For slides: "Make it as a Slides artifact (a deck on a page at claude.ai that colleagues can open, comment on and edit),
with clear design, little text on each slide because the room should listen, not read, and the explanation in the
speaker notes." Export it to PowerPoint or PDF from the page when it is good.

## Reviewing what it made

> I have read ‹the product›. Here is what is wrong: ‹…›. Answer every point in a table that names the place and says
> what changed. "Fixed" is not an answer.

## Checking the claims before it leaves

> Start a background agent that did not write ‹the product›. Have it check every cited claim against the passage it
> cites, and every number against its source, and list each mismatch with its place in the text and the passage.

An agent defends the text it wrote; a fresh one, which sees only the text and the sources, finds what the writer no
longer sees. You decide what to change.

## Turning a correction into a rule

> This is the second time I have corrected ‹…›. Make it a rule, with the reason, in the place where it will act (a
> skill, a setting, or AGENTS.md), and add the decision to DECISIONS.md.

## When an answer is hard to follow

> /plain

or, for a document: `/plain ‹file›`.

## Before sending a document to someone

> Ask the second-reader agent to read ‹file›. The reader already knows ‹…›. Then fix what it finds that is real.

## A long task while you are away

> Work on ‹task› without input from me. Keep a record as you go in plan/‹file›, and commit after each step. Do only
> what can be undone. At the end, list the fewest questions I need to answer, each with your recommendation.

## Research by background agents

> Write a brief in plan/ for these questions: ‹…›. Then send one background agent per question; each writes one file
> in research/, quotes every source with its address and date, marks what it could not verify, and runs no git
> command. Read each file when it is done and write its line in research/README.md.

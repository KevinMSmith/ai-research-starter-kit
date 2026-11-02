# 5. Learning: a few reliable sources are enough

*The sources I learn from, with the videos to start with. About five minutes to read; the videos are 8 to 14 minutes
each. Facts as of 31 October 2026, from the channels' public video lists and the makers' pages.*

## Why only a few

A new model, tool or "next big thing" appears every week, and following all of it is impossible and unnecessary.
Choose a few sources you trust, one for each need, and ignore the rest. You will not miss what matters, and you will
not feel that you have to keep up with everything. These three cover what I need: how things work, where the field is
going, and how to work with an agent.

## How things work: IBM Technology

**youtube.com/@IBMTechnology**, IBM's own educational channel (1.83 million subscribers). Six days a week it posts an
explainer of about ten minutes in which one or two of IBM's engineers draw on a glass board while they talk, on how
language models, AI agents, retrieval, security and programming with AI work. It is hard to go wrong with any of them.
Two presenters give most of the explainers: **Martin Keen**, an IBM Master Inventor, whose videos draw the most
viewers, and **Jeff Crume**, an IBM Distinguished Engineer, whose videos have been viewed more than fifteen million
times. Two cautions: the videos sometimes mention IBM's own products, and since August 2026 most descriptions say that
AI helped write the transcript and the description.

Start with these five, all from August to October 2026:

| Video | Presenter | Minutes | What it explains |
|---|---|---|---|
| [AI Simplified: 6 Concepts You Need to Know About Modern AI](https://www.youtube.com/watch?v=mUw27wG7uFA) | Jeff Crume | 9 | six basic terms (the language model, training, retrieval, an agent's tools, MCP or the Model Context Protocol, which is a standard way to connect an agent to tools, and the system prompt) through a comparison with a person |
| [AI Model vs Agentic Harness: What Actually Drives AI](https://www.youtube.com/watch?v=ZELPNFXJ4_o) | Martin Keen | 9 | why the same model behaves differently in different products: an agent is the model plus the program around it, with its tools, memory and a loop of plan, act and check |
| [Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know](https://www.youtube.com/watch?v=X4FVEEegCbk) | Martin Keen | 9 | four ways to give an agent knowledge it lacks, with a rule of thumb for each |
| [Context Engineering for AI Agents: 4 Failure Modes to Avoid](https://www.youtube.com/watch?v=BwXremQ-i6I) | Martin Keen | 10 | why more text in front of an agent can make it less reliable, and four fixes |
| [Understanding AI Agent Hallucination in AI Systems](https://www.youtube.com/watch?v=bNRhppHct54) | Brianne Zavala | 11 | why a model states wrong things with confidence, and four remedies, among them grounding it in your own sources |

And one older classic: [How Large Language Models Work](https://www.youtube.com/watch?v=5sLYAQS9sWQ) (Martin Keen,
2023, 6 minutes), viewed 1.7 million times.

## Where the field is going: AI Explained

**youtube.com/@aiexplained-official** (457 000 subscribers), made by Philip, who gives only his first name. Two to four
videos a month, about half an hour each. He reads the **system card** (the report a maker publishes with a new model,
on its tests and its risks) and the papers behind every major release, and links them under each video, so you can
check what he says. He also keeps his own test of reasoning, **SimpleBench**: 204 everyday questions, all but ten kept
private so that no model can be trained on the answers. Nine people set the human baseline at 83.7 percent; in October
2026, for the first time, three models scored above it. He is careful about prediction: on 12 October 2026 he said
that "the next 18 months are still definitely hard to predict in my eyes". Watch his newest video when a major model
is released; he has a free newsletter, Signal to Noise, as well.

## How to work with an agent: Matt Pocock

**youtube.com/@mattpocockuk** (428 000 subscribers), and **aihero.dev**. Matt Pocock teaches programmers to work with
AI agents. His collection of skills for Claude Code, `mattpocock/skills` on GitHub, was started in February 2026 and is
the 14th most-starred project on all of GitHub (308 289 stars on 31 October 2026). His approach is planning first,
with the human in the loop: the agent interviews you one decision at a time, with a recommended answer for each; the
answers become a written plan; the plan is cut into small steps; and you check each result. He gives the reason
himself: "no one knows exactly what they want" until they are questioned, an agent left alone fills the gaps with
silent guesses, and the AI is "a kind of tactical programmer … You need someone thinking on the strategic level. And
that's you." He does not call this "spec-driven development"; he criticises that idea, in which a specification is
turned into code that nobody reads.

He writes for programmers, but two of his videos suit anyone:

| Video | Date | Minutes | What it explains |
|---|---|---|---|
| [Never Trust An LLM](https://www.youtube.com/watch?v=9VNG0h4pLh0) | March 2026 | 14 | why a language model states false things confidently, and how to work round it: give it the documents, tell it to search, and read the sources yourself; no code |
| [I was an AI skeptic. Then I tried plan mode](https://www.youtube.com/watch?v=WNx-s-RxVxk) | January 2026 | 12 | why he plans with the agent before it changes anything, and why the planning helps the person as much as the agent (the part from 5:11 to 8:05 shows code and can be skipped) |

His skills, his newsletter and his videos are free; his courses are paid (an AI coding course at 299 US dollars).

## Why it matters

In 2025 many people concluded that AI had peaked; Gartner's hype cycle that year placed generative AI in its "trough of
disillusionment". The sources above showed something else coming: models that reason step by step before they answer,
agents that use tools, and what NVIDIA calls three scaling laws, by which a model improves with more training, with
more training after the first, and with more computation while it answers. Independent measurements of 2026 (METR)
still show no slowdown in the length of task an agent can finish, which has doubled about every four months since
2023. Nobody can say how long that lasts; but it is a reason to plan for tools that keep getting better.

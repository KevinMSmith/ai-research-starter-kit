# sources — the originals as text, and one card per source

`<ID>.md` is the original rendered to plain text by `python tools/extract.py`, with numbered paragraphs, so that a
passage can be cited as `<ID>¶<n>`. It is never edited by hand; it is rendered again.

`cards/<ID>.md` is the card the agent writes for each source, from that source alone (template: `templates/card.md`):
an index of what the source holds, each item with its anchor. A card indexes the source and never replaces it: a page
in `kb/` that states a reason or a number goes back to the passage itself.

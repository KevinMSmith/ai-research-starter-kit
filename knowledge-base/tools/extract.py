"""Render the originals in raw/ to plain text in sources/, with numbered paragraphs, so that they can be read and cited.

    python tools/extract.py            render every deposit that has no rendering yet
    python tools/extract.py K03 D12    render (again) only these IDs

Each deposit <ID> becomes sources/<ID>.md: a short header, then the text, one paragraph per numbered line (¶1, ¶2 ...).
A page in kb/ cites a passage as <ID>¶<n>, for example M03¶12 for paragraph 12 of meeting 3. sources/ can always be
made again from raw/, so a rendering is never edited by hand; a fault in it is fixed here, in the script.

What each kind of file becomes:
  .pdf            the text of each page (pypdf); a scanned PDF without a text layer gives nothing, and says so
  .docx           paragraphs and tables (python-docx)
  .pptx           each slide's text and its speaker notes, under a heading per slide (python-pptx)
  .xlsx           each sheet, one paragraph per row, a computed cell with its formula (openpyxl)
  .vtt            a Teams transcript: its cues joined into paragraphs. Speaker names are REMOVED unless the
                  option --keep-speakers is given, so that no name from a meeting reaches the agent by default
  .eml            the headers and the plain text of an e-mail
  .txt .md .csv   copied, one paragraph per block of lines
  anything else   listed in the header as not rendered; the agent reads it directly if it can

The four packages for the first four kinds are installed once with:
    python -m pip install pypdf python-docx python-pptx openpyxl
"""
import datetime
import email
import email.policy
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW, SOURCES = os.path.join(ROOT, "raw"), os.path.join(ROOT, "sources")
MANIFEST = os.path.join(RAW, "MANIFEST.md")
ROW_RE = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \| (.*?) \| (.*?) \|")
MISSING = "python -m pip install pypdf python-docx python-pptx openpyxl"


def need(module):
    try:
        return __import__(module)
    except ImportError:
        sys.exit(f"the package for this kind of file is not installed. Install the four packages once with:\n    {MISSING}")


def blocks(text):
    return [b.strip() for b in re.split(r"\n\s*\n", text.replace("\r\n", "\n")) if b.strip()]


def pdf(path):
    pypdf = need("pypdf")
    out = []
    for i, page in enumerate(pypdf.PdfReader(path).pages, 1):
        t = page.extract_text() or ""
        out.append(("h", f"Page {i}"))
        out += [("p", b) for b in blocks(t)] or [("p", "(no text layer on this page)")]
    return out


def docx(path):
    need("docx")
    import docx as d
    doc = d.Document(path)
    out = [("p", p.text) for p in doc.paragraphs if p.text.strip()]
    for n, table in enumerate(doc.tables, 1):
        out.append(("h", f"Table {n}"))
        for row in table.rows:
            out.append(("p", " | ".join(c.text.strip() for c in row.cells)))
    return out


def pptx(path):
    need("pptx")
    from pptx import Presentation
    out = []
    for i, slide in enumerate(Presentation(path).slides, 1):
        out.append(("h", f"Slide {i}"))
        for shape in slide.shapes:
            if shape.has_text_frame and shape.text_frame.text.strip():
                out.append(("p", shape.text_frame.text.strip()))
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip():
            out.append(("p", "Notes: " + slide.notes_slide.notes_text_frame.text.strip()))
    return out


def xlsx(path):
    openpyxl = need("openpyxl")
    values = openpyxl.load_workbook(path, data_only=True)
    formulas = openpyxl.load_workbook(path, data_only=False)
    out = []
    for ws in values.worksheets:
        out.append(("h", f"Sheet {ws.title}"))
        wf = formulas[ws.title]
        for row in wf.iter_rows():
            cells = []
            for fc in row:
                f = fc.value
                if f is None:
                    continue
                v = ws[fc.coordinate].value
                if isinstance(f, str) and f.startswith("="):
                    shown = "(not calculated: open and save the file in Excel)" if v is None else v
                    cells.append(f"{fc.coordinate} = {shown} (formula {f})")
                else:
                    cells.append(f"{fc.coordinate} = {f}")
            if cells:
                out.append(("p", "; ".join(cells)))
    return out


def vtt(path, keep):
    text = open(path, encoding="utf-8-sig", errors="replace").read()
    turns, last = [], None
    for cue in re.split(r"\n\s*\n", text):
        lines = [l for l in cue.splitlines() if l.strip() and "-->" not in l and l.strip() != "WEBVTT" and not l.strip().isdigit()]
        if not lines:
            continue
        line = " ".join(lines)
        m = re.match(r"<v ([^>]+)>(.*?)(</v>)?$", line)
        speaker, said = (m.group(1), m.group(2)) if m else (None, line)
        said = re.sub(r"<[^>]+>", "", said).strip()
        if speaker == last and turns:
            turns[-1][1] += " " + said
        else:
            turns.append([speaker, said])
            last = speaker
    labels = {}
    out = []
    for speaker, said in turns:
        if keep and speaker:
            out.append(("p", f"{speaker}: {said}"))
        elif speaker:
            labels.setdefault(speaker, f"Speaker {len(labels) + 1}")
            out.append(("p", f"{labels[speaker]}: {said}"))
        else:
            out.append(("p", said))
    return out


def eml(path):
    msg = email.message_from_binary_file(open(path, "rb"), policy=email.policy.default)
    out = [("p", f"{h}: {msg[h]}") for h in ("From", "To", "Cc", "Date", "Subject") if msg[h]]
    body = msg.get_body(preferencelist=("plain",))
    if body:
        out += [("p", b) for b in blocks(body.get_content())]
    return out


def plain(path):
    return [("p", b) for b in blocks(open(path, encoding="utf-8-sig", errors="replace").read())]


def render(id_, dest, original, what, keep):
    path = os.path.join(ROOT, dest)
    ext = os.path.splitext(path)[1].lower()
    readers = {".pdf": pdf, ".docx": docx, ".pptx": pptx, ".xlsx": xlsx, ".eml": eml,
               ".txt": plain, ".md": plain, ".csv": plain}
    if ext == ".vtt":
        items = vtt(path, keep)
    elif ext in readers:
        items = readers[ext](path)
    else:
        items = None
    today = datetime.date.today().isoformat()
    lines = [f"# {id_}: {what}", "",
             f"Rendered from `{dest}` (originally *{original}*) by `tools/extract.py` on {today}. "
             f"Cite a passage as {id_}¶<n>. Never edit this file; render it again instead.", ""]
    if items is None:
        lines.append(f"Not rendered: the script does not read {ext} files. The agent reads the original directly if it can.")
    else:
        n = 0
        for kind, text in items:
            if kind == "h":
                lines += [f"## {text}", ""]
            else:
                n += 1
                lines += [f"¶{n} {text}", ""]
    os.makedirs(SOURCES, exist_ok=True)
    with open(os.path.join(SOURCES, f"{id_}.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"rendered {id_} -> sources/{id_}.md")


def main():
    args = sys.argv[1:]
    keep = "--keep-speakers" in args
    wanted = {a.upper() for a in args if not a.startswith("--")}
    if not os.path.exists(MANIFEST):
        print("no deposits yet")
        return 0
    for line in open(MANIFEST, encoding="utf-8"):
        m = ROW_RE.match(line)
        if not m:
            continue
        id_, dest, original, what = m.groups()
        if wanted and id_ not in wanted:
            continue
        if not wanted and os.path.exists(os.path.join(SOURCES, f"{id_}.md")):
            continue
        render(id_, dest, original, what, keep)
    return 0


if __name__ == "__main__":
    sys.exit(main())

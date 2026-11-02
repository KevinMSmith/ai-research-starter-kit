"""Deposit a file into raw/, and keep raw/MANIFEST.md, the record that proves raw/ is unchanged.

    python tools/deposit.py add "<file>" <ID> "<what it is>"   copy the file into raw/ under its ID, hash it, list it
    python tools/deposit.py verify                             re-hash raw/; report anything changed, missing or unlisted
    python tools/deposit.py next <CLASS>                       print the next free ID of a class (M, D, K, R, ...)

<file> is a full path, or a file name in the inbox folder set in tools/config.py. The copy in raw/ is named
<ID>-<original name in lower case, spaces as hyphens>, so the ID comes first and the original name stays readable.

The manifest is a table with one row per deposit: the ID, the path in raw/, the original name, what it is, the date,
the size and the SHA-256 checksum. A checksum is a fingerprint of the file's bytes: if a single byte changes, the
checksum changes, so `verify` can prove that nothing in raw/ has been edited since it was deposited. Nothing is ever
removed from the manifest. A later version of a document is deposited as a new entry with -r2 after its ID (D04-r2),
and both files stay.

This script writes raw/ from Python, which the guard hook (tools/hooks/guard_raw.py) does not see; the agent's own
editing tools cannot write there. Standard library only.
"""
import datetime
import hashlib
import os
import re
import shutil
import sys

from config import INBOX

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
MANIFEST = os.path.join(RAW, "MANIFEST.md")
NOT_DEPOSITS = {".gitkeep", "MANIFEST.md", "README.md"}
ID_RE = re.compile(r"^[A-Z]{1,3}\d{2,4}(-r\d+)?$")
ROW_RE = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \| (.*?) \| (.*?) \| (\d{4}-\d{2}-\d{2}) \| ([\d,]+) \| `([0-9a-f]{64})` \|$")

HEADER = """# Deposit manifest

Every file in `raw/` and where it came from. A deposit is a deliberate act: once a file is listed here it is never
edited, renamed or deleted. The SHA-256 checksum is the fingerprint that proves the deposited copy still matches what
was deposited. Written by `python tools/deposit.py add`; checked by `python tools/deposit.py verify`.

| ID | Path in `raw/` | Original name | What it is | Deposited | Bytes | SHA-256 |
|---|---|---|---|---|---|---|
"""


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rows():
    if not os.path.exists(MANIFEST):
        return []
    out = []
    for line in open(MANIFEST, encoding="utf-8"):
        m = ROW_RE.match(line.rstrip("\n"))
        if m:
            out.append(m.groups())
    return out


def slug(name):
    stem, ext = os.path.splitext(os.path.basename(name))
    stem = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")[:60] or "file"
    return stem + ext.lower()


def add(src, id_, what):
    if not ID_RE.match(id_):
        sys.exit(f"'{id_}' is not an ID: one to three capital letters and a number, for example K03 or D12 (AGENTS.md)")
    if not os.path.isabs(src) and not os.path.exists(src):
        src = os.path.join(INBOX, src)
    if not os.path.isfile(src):
        sys.exit(f"no such file: {src}")
    existing = rows()
    if any(r[0] == id_ for r in existing):
        sys.exit(f"{id_} is already deposited; a later version is {id_}-r2, or take the next ID (deposit.py next)")
    digest = sha256(src)
    for r in existing:
        if r[6] == digest:
            sys.exit(f"this file is already deposited, as {r[0]} ({r[1]}); nothing done")
    if "|" in what:
        sys.exit("the description may not contain the character |")
    dest = f"raw/{id_}-{slug(src)}"
    os.makedirs(RAW, exist_ok=True)
    shutil.copy2(src, os.path.join(ROOT, dest))
    if sha256(os.path.join(ROOT, dest)) != digest:
        sys.exit("the copy does not match the original; nothing listed. Try again.")
    if not os.path.exists(MANIFEST):
        with open(MANIFEST, "w", encoding="utf-8", newline="\n") as f:
            f.write(HEADER)
    size = os.path.getsize(src)
    today = datetime.date.today().isoformat()
    with open(MANIFEST, "a", encoding="utf-8", newline="\n") as f:
        f.write(f"| `{id_}` | `{dest}` | {os.path.basename(src)} | {what} | {today} | {size:,} | `{digest}` |\n")
    print(f"deposited {os.path.basename(src)} as {id_}: {dest} ({size:,} bytes)")
    return 0


def verify():
    listed = rows()
    bad = 0
    for id_, dest, *_, digest in listed:
        path = os.path.join(ROOT, dest)
        if not os.path.exists(path):
            print(f"MISSING FROM raw/          {dest}")
            bad += 1
        elif sha256(path) != digest:
            print(f"CHANGED SINCE DEPOSIT      {dest}")
            bad += 1
    on_disk = {os.path.relpath(os.path.join(dp, fn), ROOT).replace("\\", "/")
               for dp, _, fns in os.walk(RAW) for fn in fns if fn not in NOT_DEPOSITS}
    for extra in sorted(on_disk - {r[1] for r in listed}):
        print(f"IN raw/ BUT NOT DEPOSITED  {extra}")
        bad += 1
    if bad:
        print(f"{bad} problem(s) in raw/")
    elif not listed:
        print("no deposits yet, and nothing else in raw/")
    else:
        print(f"raw/ intact: {len(listed)} deposits, every checksum matches")
    return 1 if bad else 0


def next_id(cls):
    nums = [int(m.group(1)) for r in rows() for m in [re.match(re.escape(cls) + r"(\d+)", r[0])] if m]
    print(f"{cls}{max(nums, default=0) + 1:02d}")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["add"] and len(a) == 4:
        sys.exit(add(a[1], a[2], a[3]))
    if a[:1] == ["next"] and len(a) == 2:
        sys.exit(next_id(a[1].upper()))
    if a in ([], ["verify"]):
        sys.exit(verify())
    print(__doc__)
    sys.exit(2)

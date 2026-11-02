#!/usr/bin/env python3
r"""Install the writing kit of the starter kit into the user folder of this machine.

The writing kit makes the agent write plainly for you: in complete statements with their background, with every term
from outside your field explained (guide/03-the-writing-kit.md explains each part). This script puts its files where
Claude Code (and Codex, if it is installed) reads them, so that they apply in every project on the machine:

  1. Your instructions (writing-kit/user-instructions.md, with the blanks filled in) go into ~/.claude/CLAUDE.md,
     between two marker lines; anything else already in that file is kept. The same is done in ~/.codex/AGENTS.md if
     the folder ~/.codex exists.
  2. The output style "Plain teaching" is copied to ~/.claude/output-styles/.
  3. The command /plain is copied to ~/.claude/skills/plain/, and the second-reader agent to ~/.claude/agents/.
  4. "outputStyle": "Plain teaching" is set in ~/.claude/settings.json; every other setting is kept, and a dated
     backup copy of the file is made first.

~ is your user folder (C:\Users\<you> on Windows). Run the script again after editing any of these files: it
replaces what it installed before. Open a new conversation in Claude Code afterwards for the change to take effect.

  python writing-kit/install_kit.py              install, or update after an edit
  python writing-kit/install_kit.py --check      show what is installed and what differs; change nothing
  python writing-kit/install_kit.py --uninstall  remove what this script installed (the backups of settings.json stay)

Standard library only; runs on Windows, macOS and Linux. Adapted from the script in the repository
ai-research-workflows, tested there on 31 October 2026.
"""
import argparse
import datetime
import json
import shutil
from pathlib import Path

KIT = Path(__file__).resolve().parent
HOME = Path.home()
CLAUDE = HOME / ".claude"
CODEX = HOME / ".codex"

STYLE_NAME = "Plain teaching"
BEGIN = ("<!-- BEGIN writing kit (installed by writing-kit/install_kit.py from the starter kit; "
         "edit writing-kit/user-instructions.md there, not here) -->")
END = "<!-- END writing kit -->"

# (file in kit/, destination under ~/.claude/)
COPIES = [
    ("output-styles/plain-teaching.md", "output-styles/plain-teaching.md"),
    ("skills/plain/SKILL.md", "skills/plain/SKILL.md"),
    ("agents/second-reader.md", "agents/second-reader.md"),
]


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def block():
    body = read(KIT / "user-instructions.md").strip()
    return f"{BEGIN}\n{body}\n{END}"


def split(text):
    """Return the text before the block, the block, and the text after it; the block is empty if absent."""
    i, j = text.find(BEGIN), text.find(END)
    if i < 0 or j < i:
        return text, "", ""
    j += len(END)
    return text[:i], text[i:j], text[j:]


def instructions(path, mode):
    old = read(path)
    before, current, after = split(old)
    if mode == "check":
        state = "absent" if not current else ("up to date" if current == block() else "differs from the master")
        print(f"  instructions in {path}: {state}")
        return
    if mode == "uninstall":
        if not current:
            print(f"  instructions in {path}: not installed, nothing to remove")
            return
        new = (before.rstrip() + "\n\n" + after.lstrip()).strip()
    elif current:
        new = before + block() + after
    else:
        new = (old.rstrip() + "\n\n" if old.strip() else "") + block()
    new = new.strip() + "\n" if new.strip() else ""
    if new == old:
        print(f"  instructions in {path}: already up to date")
    elif not new:
        path.unlink()
        print(f"  instructions in {path}: removed (the file held nothing else, so it was deleted)")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(new, encoding="utf-8")
        print(f"  instructions in {path}: {'removed' if mode == 'uninstall' else 'written'}")


def copies(mode):
    for src, dst in COPIES:
        s, d = KIT / src, CLAUDE / dst
        if mode == "check":
            state = "absent" if not d.exists() else ("up to date" if d.read_bytes() == s.read_bytes() else "differs")
            print(f"  {d}: {state}")
        elif mode == "uninstall":
            if d.exists():
                d.unlink()
                if not any(d.parent.iterdir()) and d.parent.name not in ("agents", "output-styles", "skills"):
                    d.parent.rmdir()
                print(f"  {d}: removed")
        else:
            d.parent.mkdir(parents=True, exist_ok=True)
            same = d.exists() and d.read_bytes() == s.read_bytes()
            if not same:
                shutil.copyfile(s, d)
            print(f"  {d}: {'already up to date' if same else 'copied'}")


def setting(mode):
    path = CLAUDE / "settings.json"
    data = json.loads(read(path) or "{}")
    current = data.get("outputStyle")
    if mode == "check":
        print(f"  outputStyle in {path}: {current!r}")
        return
    if mode == "uninstall":
        if current != STYLE_NAME:
            print(f"  outputStyle in {path}: {current!r}, left as it is")
            return
        del data["outputStyle"]
    else:
        if current == STYLE_NAME:
            print(f"  outputStyle in {path}: already {STYLE_NAME!r}")
            return
        if current:
            print(f"  outputStyle in {path}: was {current!r}, replaced")
        data["outputStyle"] = STYLE_NAME
    if path.exists():
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copyfile(path, path.with_name(f"settings.json.bak-{stamp}"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  outputStyle in {path}: {'removed' if mode == 'uninstall' else 'set to ' + repr(STYLE_NAME)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="show what is installed; change nothing")
    group.add_argument("--uninstall", action="store_true", help="remove what this script installed")
    args = ap.parse_args()
    mode = "check" if args.check else "uninstall" if args.uninstall else "install"
    if mode == "install" and "‹" in read(KIT / "user-instructions.md"):
        raise SystemExit("writing-kit/user-instructions.md still has blanks marked ‹like this›. Fill them in "
                         "(or ask the agent to do it with you), then run this script again. Nothing was installed.")
    print(f"Writing kit, {mode}, on this machine (user folder {HOME}):")
    instructions(CLAUDE / "CLAUDE.md", mode)
    if CODEX.exists():
        instructions(CODEX / "AGENTS.md", mode)
    else:
        print(f"  Codex is not installed here ({CODEX} does not exist); skipped")
    copies(mode)
    setting(mode)
    if mode != "check":
        print("Restart Claude Code (or open a new session) for the change to take effect.")


if __name__ == "__main__":
    main()

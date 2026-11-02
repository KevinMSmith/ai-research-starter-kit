"""Guard hook: refuse any tool call by the agent that would change raw/.

Claude Code runs this script before every file edit and every shell command (the setting is in .claude/settings.json).
It receives the planned tool call as JSON on its input. Exit code 2, with a reason, refuses the call and shows the
reason to the agent; exit code 0 lets the call through. raw/ holds the originals and is never changed (AGENTS.md): a
deposit goes through tools/deposit.py, which writes from Python and is not a tool call this hook sees.

A rule written in AGENTS.md is read by the agent and can be forgotten in a long session; this hook cannot be.

Test by hand (it should print the refusal and exit with 2):
    echo {"tool_name":"Write","tool_input":{"file_path":"raw/x.md"}} | python tools/hooks/guard_raw.py
Standard library only. Adapted from the course repository's hook, tested there since 12 October 2026.
"""
import json
import os
import re
import sys

GUARDED = ("raw",)
RULE = ("{g}/ holds the originals and is never edited, renamed, overwritten or deleted (AGENTS.md). "
        "A deposit goes through `python tools/deposit.py add`; a correction is made downstream, in sources/ or kb/.")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tool = data.get("tool_name", "") or ""
    ti = data.get("tool_input", {}) or {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    root = os.path.normcase(os.path.abspath(root))

    def guarded(path):
        if not path:
            return None
        p = os.path.normcase(os.path.abspath(os.path.join(root, path)))
        for g in GUARDED:
            gdir = os.path.join(root, g)
            if p == gdir or p.startswith(gdir + os.sep):
                return g
        return None

    def refuse(g):
        sys.stderr.write(RULE.format(g=g))
        return 2

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        g = guarded(ti.get("file_path") or ti.get("notebook_path") or "")
        return refuse(g) if g else 0

    if tool in ("Bash", "PowerShell"):
        cmd = ti.get("command", "") or ""
        token = r'(?:(?<=\s)|(?<=["\'(])|^)(?:\.[\\/])?(raw)[\\/]'
        root_pat = r'[\\/]'.join(re.escape(part) for part in re.split(r'[\\/]', root) if part)
        absolute = root_pat + r'[\\/](raw)(?:[\\/]|\b)'
        verbs = (r'(?<![\w-])(rm|rmdir|del|erase|Remove-Item|ri|mv|move|Move-Item|mi|ren|rename|Rename-Item|rni|'
                 r'git\s+(?:rm|mv)|Clear-Content|clc|Set-Content|sc|Add-Content|ac|Out-File|Tee-Object|tee|'
                 r'truncate|sed\s+-i|touch|New-Item)\b')
        copies = r'(?<![\w-])(cp|copy|Copy-Item|cpi|xcopy|robocopy)\b'
        # each statement is judged on its own: the verb and the guarded path must sit in the same segment
        for seg in re.split(r'[;\n|]|&&|\|\|', cmd):
            hit = re.search(token, seg, re.I) or re.search(absolute, seg, re.I)
            if not hit:
                continue
            g = hit.group(1).lower()
            if re.search(verbs, seg, re.I):
                return refuse(g)
            if re.search(r'>>?\s*["\']?(?:\.[\\/])?(raw)[\\/]', seg, re.I) or re.search(r'>>?\s*["\']?' + absolute, seg, re.I):
                return refuse(g)
            if re.search(copies, seg, re.I):
                tokens = re.findall(r'"[^"]+"|\'[^\']+\'|\S+', seg)
                last = tokens[-1].strip('"\'') if tokens else ""
                if guarded(last) or re.match(r'(?:\.[\\/])?(raw)[\\/]', last, re.I):
                    return refuse(g)
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

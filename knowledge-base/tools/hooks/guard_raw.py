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

# A blocked word counts only as the command word of a command, so `grep -i "move" raw/MANIFEST.md`, which only
# reads, is no longer refused (plan 22 of ai-research-workflows, item B6, 12 November 2026).
VERBS = {"rm", "rmdir", "del", "erase", "remove-item", "ri", "mv", "move", "move-item", "mi", "ren", "rename",
         "rename-item", "rni", "clear-content", "clc", "set-content", "sc", "add-content", "ac", "out-file",
         "tee-object", "tee", "truncate", "touch", "new-item"}
COPIES = {"cp", "copy", "copy-item", "cpi", "xcopy", "robocopy"}
SPLIT = r'\|\||&&|[;\n|]|(?<![<>&])&(?![>&])'              # ; && || | & and new lines end a command
STARTS = r'\$\(|[`(){}]|\s-(?:exec|execdir|ok|okdir)(?=\s)'  # a command also starts after $( ` ( { and find -exec
WRAPPERS = {"sudo", "env", "xargs", "time", "nohup", "nice", "exec", "command", "builtin", "stdbuf", "timeout",
            "ionice", "then", "do", "else", "elif", "if", "while", "until", "!"}
WRAPPER_ARG = {"sudo": {"-u", "-g", "-C", "-D", "-h", "-p", "-r", "-t", "-U", "-T"},  # options that take a value
               "xargs": {"-I", "-n", "-P", "-L", "-s", "-d", "-E", "-a"}, "env": {"-u", "-C", "-S"},
               "nice": {"-n"}, "timeout": {"-s", "-k"}, "time": {"-f", "-o"}, "ionice": {"-c", "-n", "-p"}}
SHELLS = {"bash", "sh", "zsh", "dash", "ksh", "eval", "cmd", "pwsh", "powershell"}


def command_words(text, depth=0):
    """(command word, the words after it) for each command in a shell line, quotes removed.

    The command word is the first word after VAR=value assignments and wrappers such as sudo, env, xargs, time
    and nohup. Commands inside $( ), backquotes, ( ), { }, find -exec and bash -c "..." count as well.
    """
    found = []
    for stmt in re.split(SPLIT, text):
        for piece in re.split(STARTS, stmt):
            words = [re.sub(r'["\']', '', w) for w in re.findall(r'(?:[^\s"\']+|"[^"]*"|\'[^\']*\')+', piece)]
            i = 0
            while i < len(words):
                if re.match(r'[A-Za-z_]\w*=', words[i]):
                    i += 1
                elif words[i].lower() in WRAPPERS:
                    takes = WRAPPER_ARG.get(words[i].lower(), ())
                    i += 1
                    while i < len(words) and (words[i].startswith("-") or re.match(r'[\d.]+[smhd]?$', words[i])):
                        i += 2 if words[i] in takes else 1
                else:
                    break
            if i >= len(words):
                continue
            name = re.sub(r'\.exe$', '', re.split(r'[\\/]', words[i].lstrip("\\"))[-1].lower())
            args = words[i + 1:]
            found.append((name, args))
            if name in SHELLS and depth < 20:
                inner = " ".join(a for a in args if not re.match(r'-|/[ck]$', a, re.I))
                found.extend(command_words(inner, depth + 1))
    return found


def changes_files(name, args):
    """True when this command word changes or removes files (the copy commands are judged by their target)."""
    if name in VERBS:
        return True
    if name == "sed":
        return any(a == "--in-place" or a.startswith("--in-place=") or re.match(r'-[^-]*i', a) for a in args)
    if name == "git":
        i = 0
        while i < len(args) and args[i].startswith("-"):
            i += 2 if args[i] in ("-C", "-c", "--git-dir", "--work-tree", "--namespace") else 1
        return i < len(args) and args[i].lower() in ("rm", "mv")
    return False


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
        token = r'(?:(?<=\s)|(?<=["\'(>])|^)(?:\.[\\/])?(raw)[\\/]'
        root_pat = r'[\\/]'.join(re.escape(part) for part in re.split(r'[\\/]', root) if part)
        absolute = root_pat + r'[\\/](raw)(?:[\\/]|\b)'
        # each statement is judged on its own: the verb and the guarded path must sit in the same segment
        for seg in re.split(SPLIT, cmd):
            hit = re.search(token, seg, re.I) or re.search(absolute, seg, re.I)
            if not hit:
                continue
            g = hit.group(1).lower()
            words = command_words(seg)
            if any(changes_files(name, args) for name, args in words):
                return refuse(g)
            if re.search(r'>>?\s*["\']?(?:\.[\\/])?(raw)[\\/]', seg, re.I) or re.search(r'>>?\s*["\']?[\\/]?' + absolute, seg, re.I):
                return refuse(g)
            if any(name in COPIES for name, _ in words):
                tokens = re.findall(r'"[^"]+"|\'[^\']+\'|\S+', seg)
                last = tokens[-1].strip('"\'') if tokens else ""
                if guarded(last) or re.match(r'(?:\.[\\/])?(raw)[\\/]', last, re.I):
                    return refuse(g)
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

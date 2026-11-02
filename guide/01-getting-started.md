# 1. Getting started: installing the tools

*Step by step, for someone who has never used a terminal. About an hour, most of it waiting for installers. The steps
are those the makers document (Microsoft for VS Code, Anthropic for Claude Code, the Git project, Wispr and Meetily),
as their pages read on 31 October 2026. Steps 1 to 6 are needed before the set-up; dictation, transcription and a
GitHub account can wait. After step 6 you hand over to the agent, Claude Code: an AI program that reads the files in a
folder, changes them when you ask, and runs small programs for you. `START-HERE.md` then does the rest with you,
including installing Python (the programming language of the kit's small scripts) if your computer lacks it.*

## Before you start

- **A paid Claude plan.** The free plan does not include Claude Code. The Pro plan (20 US dollars a month, or 17 a
  month paid for a year) is enough to start; daily heavy use needs the Max plan (100 US dollars a month) or the Ultra
  plan (200 US dollars a month, called Max 20x until 30 October 2026). Subscribe at claude.ai/upgrade. Read
  `guide/06-data-and-the-rules.md` first: a personal plan comes with Anthropic's consumer terms, its contract for
  private customers, and under those terms you should keep other people's personal or confidential material out of
  what the agent reads until DTU has said otherwise.
- **A DTU laptop.** DTU's page on software (15 October 2026) says that extra software comes from the DTU Software
  Center or the Company Portal, and that anything else needs a request to IT support. VS Code's recommended installer
  and the Claude Code extension need no administrator rights (the right to install programs for every user of the
  computer), according to their makers. Try the installers first; if one is blocked, ask IT support for VS Code and
  Git for Windows.
- **Where your projects will live**: `C:\dev\projects` on Windows (`~/dev/projects` on a Mac, where `~` means your
  home folder), not in OneDrive, Dropbox or Documents. A folder that is copied to the cloud while Git records its
  history can end up with conflicting copies of the same files, and a synchronised DTU folder is one more place the
  agent can read. The set-up creates the folder for you.

## Step 1. Install VS Code

VS Code (Visual Studio Code) is Microsoft's free editor: a program for reading and editing files, with a side panel
in which Claude Code runs.

- **Windows**: download the **User setup** from code.visualstudio.com and run it. Microsoft: "The User setup is the
  recommended installation for most people because it does not require administrator permissions". Click through the
  installer with the default choices. One page asks about "GitHub Copilot CLI": choose "Don't add the copilot
  command", because Copilot is Microsoft's separate paid assistant and is not needed.
- **Mac**: download VS Code for macOS, open the `.dmg` file, and drag `Visual Studio Code.app` into the Applications
  folder.

## Step 2. Install Git

Git is the program that keeps every earlier version of every file in a project, so that nothing is ever lost. You will
not need to learn it: the agent uses it for you. Anthropic's guide for new users: "You won't need to learn Git
yourself."

- **Windows**: download Git for Windows from git-scm.com/downloads/win and run it. "Click Next on each screen to accept
  the defaults. The installer has many screens, but you don't need to change anything." Keep the recommended option on
  the screen "Adjusting your PATH environment" (PATH is the list of folders in which Windows looks for a program).
- **Mac**: open the program Terminal and type `xcode-select --install`, which installs Apple's free programming tools,
  Git among them.

## Step 3. Install the Claude Code extension

An extension is an add-on program inside VS Code. Open VS Code, press `Ctrl+Shift+X` (`Cmd+Shift+X` on a Mac) to open
the Extensions view, search for **Claude Code**, and click **Install**. Choose the one published by Anthropic. If it
does not appear after installing, close and reopen VS Code. The extension carries its own copy of Claude Code, so
nothing else needs installing.

## Step 4. Open a folder, and trust it

Unpack the starter kit into a folder you can find again, as step 2 of the README describes (on Windows,
`C:\dev\ai-research-starter-kit-main`), and open that folder with **File**, then **Open Folder...**. VS Code opens a
new folder in **Restricted Mode**, a safety mode for unfamiliar files, and shows a banner across the top. Claude Code
does not work in Restricted Mode. Trusting a folder lets VS Code and its extensions work with the files in it, so trust
only folders you know. Click **Manage** in the banner, then the **Trust** button. You do this once for each folder.

## Step 5. Open Claude Code

Open any file in the folder (click `README.md` in the list on the left). A small star-shaped icon, which Anthropic
calls the **Spark icon**, then appears at the top right of the editor; click it. The icon shows only when a file is
open. The same icon also sits in the column of icons on the left edge of the window, and the words **✻ Claude
Code** at the bottom right of the window do the same thing; all three open the same panel. The panel that opens is the conversation with
the agent; you type, or dictate, into the box at its bottom.

## Step 6. Sign in

The first time, the panel shows a sign-in screen. Click **Sign in** and finish in the browser with your claude.ai
account. Then a checklist called "Learn Claude Code" appears; you can work through it or close it.

Two things to know at this point:

- **The permission mode**, shown below the box you type in, decides when the agent asks before it acts. It starts in
  **Auto**, in which a second AI program checks each action (each file it changes and each command it runs) and the
  agent does not ask you about most of them. **Manual** makes it ask before each change and most commands; **Plan**
  makes it describe what it will do and wait. For the first week, choose **Manual**: you see each step, and the
  agent's one-line explanation of it, before you allow it; switch to Auto when you are used to it.
- **Use this panel, not VS Code's own chat window.** VS Code has a chat window of its own, which can also run
  "Claude", but that one is paid through a GitHub Copilot subscription or a pay-per-use account, not through your
  Claude plan (Microsoft's page "Third-party agents in VS Code", 28 October 2026).

**You are now ready for the set-up.** In the Claude Code panel, type or say: "Read START-HERE.md and set me up." The
agent installs Python if it is missing, the writing kit, and your first knowledge base, explaining each step.

## Dictation: Wispr Flow

Wispr Flow turns speech into text in any program: hold a key, speak, release, and the text appears where the cursor
is. Its personal dictionary keeps the names and terms of your field right, in Danish and English.

- **Install**: download it from wisprflow.ai. On Windows, run the installer and start Flow from the Start menu; its
  icon appears at the right end of the taskbar. On a Mac, drag it into Applications and give it access to the
  microphone and to Accessibility (the permission that lets it type into other programs). Sign in with your e-mail.
- **The key**: on Windows, press Caps Lock, or press Ctrl and the Windows key together (you choose one of the two in
  the settings); on a Mac, the fn key.
- **First**: choose your languages under "My languages", add your field's names and terms to the dictionary, and
  switch off "Improve the model for everyone" under Data and Privacy; otherwise the maker uses your dictations to
  improve its programs. Either way, the audio is turned into text on the maker's computers in the United States, so do
  not dictate other people's personal details.
- **Cost**: a free plan with a weekly limit of words (2 000 words a week, according to its home page; the pricing page
  now says only "Limited words per week"). The paid plan, Wispr Flow Pro, costs 15 US dollars a month, and half that
  with an education e-mail address.
- **An alternative inside Claude Code**: the Claude Code panel has a microphone button of its own, with Danish among
  its twenty languages, and its use does not count against your plan's limits. It types only into the Claude Code box,
  whereas Wispr Flow types anywhere.

## Transcription: Teams, and Meetily for a room

- **On Teams**, start the transcription in the meeting; afterwards, the organiser downloads the transcript as a VTT
  file (a text file with times and speakers). Teams tells everyone that the meeting is transcribed.
- **In a room**, Meetily, a program for transcribing meetings, records the computer's audio and turns it into text on
  the computer itself; nothing is uploaded.
  The free Community edition transcribes; Meetily Pro (120 US dollars a year, one computer per licence, a 14-day free
  trial) also separates and names the speakers. Download it from Meetily's releases page (on Windows the file ending
  in `x64-setup.exe`, the installer for ordinary 64-bit Windows computers; on a Mac the ready installer works only on
  Macs with Apple's own M-series processors). Meetily shows the people in the room nothing, so tell them at the start
  that the meeting is transcribed and why: a recording of people's speech is personal data under the GDPR, and the
  people recorded must be told (guide 06).
- **A recording you already have** (a phone on the table, a lecture), with the speakers labelled: the script
  `tools/transcribe.py` in each knowledge base transcribes it on your own computer with two free models from NVIDIA,
  Parakeet TDT 0.6B v3 for the words (25 European languages, Danish and English among them) and Nemotron 3
  Diarization for who spoke when. It needs two free programs, ffmpeg (which converts audio formats) and NVIDIA's
  NeMo-Speech.cpp (which runs the models), and the models themselves, about 800 MB, downloaded once. Ask the agent:
  "Install what tools/transcribe.py needs, as its description says, and test it on a short recording." Then say
  "transcribe meeting.m4a with tools/transcribe.py". On a laptop without a graphics card, a 17.5-minute meeting of four
  people took 7.5 minutes (measured on 1 November 2026), so an hour takes about 26 minutes. The speakers come out as
  Speaker 1, Speaker 2 and so on; tell the agent who is who.
- Every transcript goes the same day into the project's **inbox**, the folder where new material waits until the agent
  deposits it in the knowledge base; the same day, because a transcript left on the desktop is forgotten.

## A GitHub account (later, when you want a backup)

GitHub is a website that keeps a copy of a project's history. A free account needs only an e-mail address
(github.com/signup) and includes unlimited private repositories, which only you can see. You do not need it to start;
ask the agent to set it up when you want an online backup of a project. Keep any repository that holds other people's
words private.

## If something does not work

| What you see | What to do |
|---|---|
| The extension seems missing after installing | Close and reopen VS Code, or open the command box with `Ctrl+Shift+P` and run "Developer: Reload Window" |
| No Spark icon at the top right | Open a file first; or click "✻ Claude Code" at the bottom right of the window |
| The panel does nothing, and a banner says Restricted Mode | Click **Manage** in the banner, then **Trust** |
| "API Error: 403 Request not allowed" after signing in | The service refused the request. Check that your paid plan is active at claude.ai/settings. If it is, ask DTU's IT support: "Does DTU's network route traffic to claude.ai through a proxy (a server that forwards and filters web traffic) that blocks Claude Code?" |
| "SSL certificate verification failed" | The agent cannot reach Anthropic, possibly because the network checks encrypted connections with its own certificate (an electronic proof of identity). Ask IT support: "Claude Code reports SSL certificate verification failed; which certificate file should it use, and can you set it with the setting `NODE_EXTRA_CA_CERTS`?" (the setting Anthropic's error page names) |
| Asked to sign in again ("Not logged in · Please run /login") | Type `/login` in the Claude Code box (a word that starts with `/` is a command to Claude Code itself) and sign in again. Check that the computer's clock is right: a wrong clock makes the sign-in look expired |
| "You've hit your session limit · resets …" | Your plan allows a certain amount of use in each five-hour period and each week; wait until the time shown. Type `/usage` to see how much is left |
| "Git not found" in VS Code | Install Git (step 2), then restart VS Code |

## Terms used

- **VS Code**: Microsoft's free editor, in which Claude Code runs as an extension.
- **Extension**: an add-on program installed inside VS Code.
- **Git**: the program that records every version of every file in a project.
- **Restricted Mode**: VS Code's safety mode for a newly opened folder, in which extensions such as Claude Code are
  switched off until you trust the folder.
- **Permission mode**: the setting that decides when the agent asks before it acts.
- **Repository**: a project folder whose history Git keeps; on GitHub, the online copy of it.
- **Agent**: an AI program that reads and changes files and runs programs on your computer when you ask; here, Claude
  Code.
- **Spark icon**: the small star-shaped icon that opens the Claude Code panel.
- **Inbox**: the folder where new material waits until the agent deposits it in the knowledge base.

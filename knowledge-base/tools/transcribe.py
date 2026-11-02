r"""Transcribe a recording of a meeting or a lecture on this computer, with the speakers labelled.

What it does: converts any audio or video file (m4a from a phone, mp3, wav, mp4, ...) to 16 kHz mono WAV with ffmpeg;
finds who spoke when over the whole recording with NVIDIA's Nemotron 3 Diarization (up to eight speakers); cuts the
recording into pieces of about five minutes at pauses; transcribes the pieces with NVIDIA's Parakeet TDT 0.6B v3
(25 European languages, Danish and English among them, detected automatically); gives each word to the speaker who is
talking at the word's midpoint (the rule in NVIDIA's own example); and writes, next to the recording:

    <name>.vtt   WebVTT, one cue per sentence or pause, the speaker in a <v Speaker N> span (the Teams layout)
    <name>.txt   one paragraph per speaker turn, with its start time

Nothing is sent anywhere: both models run on this computer through NVIDIA's NeMo-Speech.cpp. The models are downloaded
once from Hugging Face (`nemo-speech pull parakeet-tdt`, `nemo-speech pull nemotron-3-diarization`); no token is needed.

What it needs: Python 3.9 or later (standard library only); ffmpeg; NeMo-Speech.cpp 0.3.0 or later
(https://github.com/NVIDIA/NeMo-Speech.cpp/releases), found from --nemo, the NEMO_SPEECH variable, the PATH, or
C:\dev\nemo-speech\*\bin\nemo-speech.exe.

Usage:
    python tools/transcribe.py meeting.m4a
    python tools/transcribe.py meeting.m4a --names "Anna,Bo"
    python tools/transcribe.py lecture.mp4 --out-dir C:\dev\inbox\my-project --force

--names replaces Speaker 1, 2, ... in the order in which they first speak. The speaker labels are anonymous: the
models know voices, not people. (Favouring given terms, NeMo-Speech.cpp's --speech-context, is ignored for Parakeet:
it needs a separate language model.)

Measured on 1 November 2026 on an Intel Core Ultra 7 265U laptop on battery, no graphics card: a 17.5-minute meeting of
four people (AMI ES2004a, one table microphone, as m4a) took 7.5 minutes, 88 seconds of it for the speakers; four
speakers found.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, tempfile, time

CHUNK_S = 300.0      # target length of a transcription piece
SEARCH_S = 60.0      # how far from the target a cut may move to land in a pause
MIN_GAP_S = 0.3      # the shortest pause that counts as a place to cut


def find_nemo(arg):
    for cand in (arg, os.environ.get("NEMO_SPEECH"), shutil.which("nemo-speech")):
        if cand and os.path.isfile(cand):
            return cand
    found = sorted(glob.glob(r"C:\dev\nemo-speech\*\bin\nemo-speech.exe"))
    if found:
        return found[-1]
    sys.exit("NeMo-Speech.cpp not found: give --nemo PATH, set NEMO_SPEECH, or unpack it under C:\\dev\\nemo-speech")


def find_ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    found = glob.glob(os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WinGet", "Packages", "Gyan.FFmpeg*",
                                   "*", "bin", "ffmpeg.exe"))
    if found:
        return found[0]
    sys.exit("ffmpeg not found: install it (winget install Gyan.FFmpeg) or put it on the PATH")


def run(cmd, what):
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        sys.exit(f"{what} failed (exit {p.returncode}):\n{p.stderr[-3000:]}")
    return p.stdout


def duration(ffmpeg, wav):
    out = subprocess.run([ffmpeg, "-hide_banner", "-i", wav], capture_output=True, text=True, errors="replace").stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0


def read_rttm(path):
    segs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            p = line.split()
            if len(p) >= 8 and p[0] == "SPEAKER":
                start, dur = float(p[3]), float(p[4])
                segs.append((start, start + dur, p[7]))
    return sorted(segs)


def cut_points(segs, total):
    """Cut times near every CHUNK_S, each moved to the middle of the nearest pause where nobody speaks."""
    merged = []
    for s, e, _ in segs:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    gaps = [(merged[i][1], merged[i + 1][0]) for i in range(len(merged) - 1) if merged[i + 1][0] - merged[i][1] >= MIN_GAP_S]
    cuts, t = [], CHUNK_S
    while t < total - CHUNK_S / 3:
        near = [g for g in gaps if abs((g[0] + g[1]) / 2 - t) <= SEARCH_S and (g[0] + g[1]) / 2 > (cuts[-1] if cuts else 0) + 30]
        c = min(near, key=lambda g: abs((g[0] + g[1]) / 2 - t)) if near else None
        cuts.append((c[0] + c[1]) / 2 if c else t)
        t = cuts[-1] + CHUNK_S
    return [0.0] + cuts + [total]


def words_from_json(obj):
    """Every dict that carries a word and its start and end time, wherever the output nests it."""
    out = []
    def walk(x):
        if isinstance(x, dict):
            w = x.get("word", x.get("text"))
            s = x.get("start", x.get("start_time", x.get("begin")))
            e = x.get("end", x.get("end_time"))
            if isinstance(w, str) and isinstance(s, (int, float)) and isinstance(e, (int, float)) and " " not in w.strip():
                out.append((float(s), float(e), w.strip()))
                return
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(obj)
    return sorted(out)


def speaker_of(s, e, segs, prev):
    best, best_ov = None, 0.0
    for a, b, spk in segs:
        if a > e:
            break
        ov = min(b, e) - max(a, s)
        if ov > best_ov:
            best, best_ov = spk, ov
    if best:
        return best
    mid = (s + e) / 2
    near = min(segs, key=lambda g: min(abs(g[0] - mid), abs(g[1] - mid)), default=None)
    if near and min(abs(near[0] - mid), abs(near[1] - mid)) <= 1.0:
        return near[2]
    return prev


def ts(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("audio")
    ap.add_argument("--out-dir", help="where to write the .vtt and .txt (default: beside the recording)")
    ap.add_argument("--names", help="comma-separated names for Speaker 1, 2, ... in order of first speaking")
    ap.add_argument("--nemo", help="path to nemo-speech.exe")
    ap.add_argument("--device", default="auto", help="auto, cpu, cuda, vulkan or metal (default: auto)")
    ap.add_argument("--force", action="store_true", help="replace existing output files")
    a = ap.parse_args()

    src = os.path.abspath(a.audio)
    if not os.path.isfile(src):
        sys.exit(f"not found: {src}")
    out_dir = os.path.abspath(a.out_dir or os.path.dirname(src))
    stem = os.path.splitext(os.path.basename(src))[0]
    vtt_path, txt_path = os.path.join(out_dir, stem + ".vtt"), os.path.join(out_dir, stem + ".txt")
    for p in (vtt_path, txt_path):
        if os.path.exists(p) and not a.force:
            sys.exit(f"exists: {p} (give --force to replace it)")
    nemo, ffmpeg = find_nemo(a.nemo), find_ffmpeg()
    t0 = time.time()

    with tempfile.TemporaryDirectory(prefix="transcribe-") as tmp:
        full = os.path.join(tmp, "full.wav")
        run([ffmpeg, "-hide_banner", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", full], "ffmpeg")
        total = duration(ffmpeg, full)
        print(f"recording: {total / 60:.1f} min; finding the speakers ...", flush=True)

        rttm = os.path.join(tmp, "full.rttm")
        # v3-offline: 30-second chunks; the default low-latency streaming geometry is about ten times slower on a CPU
        run([nemo, "diarize", full, "--model", "nemotron-3-diarization", "--preset", "v3-offline", "--device", a.device,
             "--format", "rttm", "--output", rttm, "--quiet"], "diarization")
        segs = read_rttm(rttm)
        t1 = time.time()

        cuts = cut_points(segs, total)
        pieces = os.path.join(tmp, "pieces")
        os.makedirs(pieces)
        for i in range(len(cuts) - 1):
            run([ffmpeg, "-hide_banner", "-loglevel", "error", "-i", full, "-ss", f"{cuts[i]:.3f}", "-to", f"{cuts[i + 1]:.3f}",
                 "-c", "copy", os.path.join(pieces, f"p{i:03d}.wav")], "ffmpeg cut")
        print(f"speakers found in {t1 - t0:.0f} s; transcribing {len(cuts) - 1} pieces ...", flush=True)

        asr = os.path.join(tmp, "asr")
        cmd = [nemo, "transcribe", pieces, "--model", "parakeet-tdt", "--device", a.device, "--format", "json",
               "--output-dir", asr, "--quiet"]
        run(cmd, "transcription")
        words = []
        for i in range(len(cuts) - 1):
            hits = glob.glob(os.path.join(asr, f"p{i:03d}*"))
            if not hits:
                sys.exit(f"no transcription output for piece {i}")
            with open(hits[0], encoding="utf-8") as f:
                words += [(s + cuts[i], e + cuts[i], w) for s, e, w in words_from_json(json.load(f))]

    # speakers numbered in order of first speaking, as the model also orders them
    order, labels, prev = [], [], None
    for s, e, w in words:
        spk = speaker_of(s, e, segs, prev)
        prev = spk
        if spk is not None and spk not in order:
            order.append(spk)
        labels.append(spk)
    names = [n.strip() for n in a.names.split(",")] if a.names else []
    def name(spk):
        if spk is None:
            return "Unknown"
        k = order.index(spk)
        return names[k] if k < len(names) and names[k] else f"Speaker {k + 1}"

    turns = []   # [speaker, start, end, [words]]
    for (s, e, w), spk in zip(words, labels):
        if turns and turns[-1][0] == spk:
            turns[-1][2] = e
            turns[-1][3].append((s, e, w))
        else:
            turns.append([spk, s, e, [(s, e, w)]])

    os.makedirs(out_dir, exist_ok=True)
    note = (f"NOTE Transcribed on this computer by tools/transcribe.py on {time.strftime('%Y-%m-%d')} from "
            f"{os.path.basename(src)}: NVIDIA Parakeet TDT 0.6B v3 (words) and Nemotron 3 Diarization (speakers), "
            f"through NeMo-Speech.cpp. Speaker labels are anonymous unless named with --names.")
    with open(vtt_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("WEBVTT\n\n" + note + "\n\n")
        for spk, _, _, ws in turns:
            cue = []
            for j, (s, e, w) in enumerate(ws):
                cue.append((s, e, w))
                nxt = ws[j + 1][0] if j + 1 < len(ws) else None
                long_enough = e - cue[0][0] >= 4.0 and w[-1:] in ".?!"
                if nxt is None or long_enough or e - cue[0][0] >= 12.0 or nxt - e > 1.0:
                    f.write(f"{ts(cue[0][0])} --> {ts(cue[-1][1])}\n<v {name(spk)}>{' '.join(x[2] for x in cue)}\n\n")
                    cue = []
    with open(txt_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(note[5:] + "\n\n")
        for spk, s, _, ws in turns:
            f.write(f"[{ts(s)[:8]}] {name(spk)}: {' '.join(x[2] for x in ws)}\n\n")

    took = time.time() - t0
    print(f"{len(order)} speakers, {len(words)} words, {len(turns)} turns; {took / 60:.1f} min for "
          f"{total / 60:.1f} min of audio\nwrote {vtt_path}\nwrote {txt_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Turn pre-2021 Wikipedia article wikitext into plain-prose blocks of 100-250 words.

usage: chunk_human.py <dir of .wiki> <outdir>
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1])
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)


def to_prose(s):
    s = re.sub(r"<ref[^>]*/>", "", s)
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<gallery.*?</gallery>", "", s, flags=re.S)
    s = re.sub(r"\{\|.*?\|\}", "", s, flags=re.S)          # tables
    for _ in range(4):
        s = re.sub(r"\{\{[^{}]*\}\}", "", s)               # templates, infoboxes
    s = re.sub(r"\[\[(?:File|Image|Category):[^\]]*\]\]", "", s, flags=re.I)
    s = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\]", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"'''?", "", s)
    s = re.sub(r"&nbsp;", " ", s)
    lines = []
    for line in s.splitlines():
        t = line.strip()
        if not t or t.startswith(("=", "*", "#", ":", "|", "!", ";")):
            continue
        lines.append(t)
    return lines


n = 0
for f in sorted(src.glob("*.wiki")):
    paras = to_prose(f.read_text(encoding="utf-8"))
    block, wc = [], 0
    for p in paras:
        w = len(re.findall(r"[A-Za-z']+", p))
        if w < 15:
            continue
        block.append(p)
        wc += w
        if wc >= 120:
            n += 1
            (out / f"{f.stem[:24]}-{n:03d}.txt").write_text("\n\n".join(block), encoding="utf-8")
            block, wc = [], 0
    if wc >= 60:
        n += 1
        (out / f"{f.stem[:24]}-{n:03d}.txt").write_text("\n\n".join(block), encoding="utf-8")
print(f"wrote {n} blocks")

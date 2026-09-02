#!/usr/bin/env python3
"""Split Wikipedia:Signs of AI writing wikitext into a calibration corpus.

Positives: the page's quoted AI-generated examples ({{cot}}..{{cob}}, {{blockquote}},
{{quote frame}}, the *new* side of {{textdiff}}). These are editor-confirmed AI text.
Negatives: the page's own editorial prose, written by human Wikipedia editors.

Writes pos/NNN.txt and neg/NNN.txt with wiki markup stripped.
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(sys.argv[2])
(out / "pos").mkdir(parents=True, exist_ok=True)
(out / "neg").mkdir(parents=True, exist_ok=True)


def strip_markup(s):
    s = re.sub(r"<ref[^>]*/>", "", s)
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<syntaxhighlight[^>]*>|</syntaxhighlight>|<nowiki>|</nowiki>|<code>|</code>", "", s)
    s = re.sub(r"\{\{(?:highlight|hl)\|([^|}]*)(?:\|[^}]*)?\}\}", r"\1", s)
    s = re.sub(r"\{\{fake section\|level=\d\|([^}]*)\}\}", r"\n\1\n", s)
    s = re.sub(r"\{\{(?:xt|strong|em|code)\|([^}]*)\}\}", r"\1", s)
    # remaining templates, possibly nested one level
    for _ in range(3):
        s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    s = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\]", "", s)
    s = re.sub(r"'''?", "", s)
    s = re.sub(r"^[=]+.*[=]+\s*$", "", s, flags=re.M)
    s = re.sub(r"^\*+\s*", "", s, flags=re.M)
    s = s.replace("[...]", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


pos_blocks = []
# {{cot|...}} ... {{cob}}
for m in re.finditer(r"\{\{cot\|[^\n]*\}\}\n(.*?)\{\{cob\}\}", src, flags=re.S):
    pos_blocks.append(m.group(1))
# {{blockquote|text=...|title=...}} and {{blockquote|...|From ...}}
for m in re.finditer(r"\{\{blockquote\|(?:text=)?(.*?)\n?\|(?:title=)?From ", src, flags=re.S):
    pos_blocks.append(m.group(1))
# {{quote frame| ... |From ...}}
for m in re.finditer(r"\{\{quote frame\|\n?(.*?)\n\|From ", src, flags=re.S):
    pos_blocks.append(m.group(1))
# textdiff: {{textdiff|old|new}} -> new side is the AI edit
for m in re.finditer(r"\{\{textdiff\|(.*?)\|(.*?)\}\}", src, flags=re.S):
    pos_blocks.append(m.group(2))

# Negatives: remove all the positive blocks, tmbox watch lists, and section
# headers; keep what remains between "==Content==" and "== See also ==".
neg_src = src
neg_src = re.sub(r"\{\{cot\|[^\n]*\}\}\n.*?\{\{cob\}\}", "", neg_src, flags=re.S)
neg_src = re.sub(r"\{\{blockquote\|.*?\}\}\n", "", neg_src, flags=re.S)
neg_src = re.sub(r"\{\{quote frame\|.*?\n\}\}", "", neg_src, flags=re.S)
neg_src = re.sub(r"\{\{textdiff\|.*?\}\}", "", neg_src, flags=re.S)
neg_src = re.sub(r"\{\{tmbox\|.*?\}\} ?\}\}", "", neg_src, flags=re.S)
neg_src = re.sub(r"\{\{tmbox\|.*?\}\}", "", neg_src, flags=re.S)
neg_src = re.sub(r"\{\{sidebox\|.*?\n\}\}", "", neg_src, flags=re.S)
start = neg_src.find("==Content==")
end = neg_src.find("== See also ==")
neg_src = neg_src[start:end]
# split editorial prose into level-3 sections so block sizes are comparable
neg_blocks = re.split(r"^=+[^=\n]+=+\s*$", neg_src, flags=re.M)

MIN_WORDS = 40
n = 0
for b in pos_blocks:
    t = strip_markup(b)
    if len(re.findall(r"[A-Za-z']+", t)) >= MIN_WORDS:
        n += 1
        (out / "pos" / f"{n:03d}.txt").write_text(t, encoding="utf-8")
print(f"positives: {n} blocks (of {len(pos_blocks)} candidates)")

n = 0
for b in neg_blocks:
    t = strip_markup(b)
    if len(re.findall(r"[A-Za-z']+", t)) >= MIN_WORDS:
        n += 1
        (out / "neg" / f"{n:03d}.txt").write_text(t, encoding="utf-8")
print(f"negatives: {n} blocks (of {len(neg_blocks)} candidates)")

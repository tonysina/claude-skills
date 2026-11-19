#!/usr/bin/env python3
"""Look up words in, or check text against, ASD-STE100 Simplified Technical English (Issue 9).

  python3 ste_dict.py lookup WORD [WORD ...]
  python3 ste_dict.py check [--mode auto|procedure|descriptive] [--terms TERMS.md ...]
                            [--compare ORIGINAL] FILE
  python3 ste_dict.py verify REPORT ORIGINAL      (quoted originals in the report exist)
  python3 ste_dict.py selftest

check reads plain text or Markdown (FILE, or - for stdin). It reports word findings
from the dictionary and structure findings from the writing rules, each with its
line number. Exit status: 0 = no findings, 1 = findings, 2 = usage error.

--compare adds a CHANGE REPORT: findings the rewrite fixed, kept, and introduced.

--mode sets the sentence limit: procedure = 20 words (rule 5.1), descriptive = 25
(rule 6.3). auto (default) uses 20 for instructions and 25 for other sentences.

Reads ../data/ste100-issue9.txt (bundled). If it is missing, it is rebuilt with
pdftotext from the PDF at $STE100_PDF (default ~/Downloads/ASD-STE100_ISSUE9.pdf).
"""
import os
import re
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
PDF = Path(os.environ.get("STE100_PDF", "~/Downloads/ASD-STE100_ISSUE9.pdf")).expanduser()
CACHE = SKILL / "data" / "ste100-issue9.txt"
POS = r"(?:n|v|adj|adv|prep|conj|pron|art)"
HEAD_POS = re.compile(rf"^(\S+(?: \S+)*) \(({POS})\),?(?=\s|$)")
NEXT_POS = re.compile(rf"^\(({POS})\)")
ALT = re.compile(rf"\b([A-Z][A-Z'-]*(?: [A-Z][A-Z'-]*)*) \(({POS}|TN|TV)\)")
NOISE = re.compile(r"^(Word\b|\(part of speech\)|Issue 9|Page |2025-|ASD.STE100|\s*Blank Page)")
# Comparative/superlative and verb forms: "PUSHES,", "IS, WAS", "(also ARE, WERE)", "(BRIGHTER,", "BRIGHTEST)"
FORMS = re.compile(r"\(?(?:also )?([A-Z][A-Z'-]*(?:,\s*[A-Z][A-Z'-]*)*),?\)?,?(?=\s|$)")
# The PDF sets these symbols in a symbol font that pdftotext maps to private-use code points.
SYMBOLS = str.maketrans({"": "°", "": "Ω", "": "″", "": "."})
PAGE_FURNITURE = re.compile(
    r"^(Issue 9\b.*Page [A-Z0-9]+-[A-Z0-9-]+|Page [A-Z0-9]+-[A-Z0-9-]+\s.*Issue 9|2025-01-15"
    r"|ASD.STE100 Simplified Technical English|Blank Page)$")
DICT_HEADER = re.compile(r"^(Word\s+Approved meaning/|\(part of speech\)\s+ALTERNATIVES)")

# ---------------------------------------------------------------- dictionary


def clean(raw):
    """Remove pdftotext page furniture and the Highlights change log; fix symbol-font glyphs."""
    lines = [l.rstrip() for l in raw.translate(SYMBOLS).replace("\f", "\n").split("\n")]
    hi = next(i for i, l in enumerate(lines) if l.strip() == "Highlights")
    toc = next(i for i, l in enumerate(lines) if l.strip() == "Table of contents")
    lines = lines[:hi] + lines[toc:]
    dict_start = max(i for i, l in enumerate(lines) if l.startswith("A (art)"))
    out = []
    for i, l in enumerate(lines):
        t = l.strip()
        if PAGE_FURNITURE.match(t) or (i >= dict_start and DICT_HEADER.match(t)):
            continue
        if not t and (not out or not out[-1]):
            continue
        out.append(l)
    return "\n".join(out) + "\n"


def text():
    if not CACHE.exists():
        if not PDF.exists():
            sys.exit(f"STE100 PDF not found at {PDF}. Set STE100_PDF to its path.")
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        out = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                             capture_output=True, text=True, check=True).stdout
        CACHE.write_text(clean(out))
    return CACHE.read_text()


def parse(raw):
    """Return list of entries: {head, pos, approved, forms, lines}."""
    lines = raw.splitlines()
    # The dictionary body starts at the last "A (art)" entry (earlier hits are intro examples).
    start = max(i for i, l in enumerate(lines) if l.startswith("A (art)"))
    entries, cur = [], None
    for i in range(start, len(lines)):
        line = lines[i]
        if not line.strip() or NOISE.match(line.strip()):
            continue
        first = re.split(r"\s{2,}", line.strip())[0]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        head = pos = None
        if line[0] != " ":
            m = HEAD_POS.match(first)
            if m:
                head, pos = m.group(1), m.group(2)
            elif NEXT_POS.match(nxt):
                head, pos = first, NEXT_POS.match(nxt).group(1)
            elif first[0].islower() and first != line.strip():
                head = first  # multi-word unapproved phrase without a part of speech
            elif cur and cur["approved"] and FORMS.match(first):
                cur["forms"] += [f.lower() for f in re.findall(r"[A-Z][A-Z'-]*", FORMS.match(first).group(1))]
        if head:
            cur = {"head": head, "pos": pos, "approved": head[0].isupper(),
                   "forms": [], "lines": []}
            entries.append(cur)
        if cur:
            cur["lines"].append(line)
    return entries


def index(entries):
    for e in entries:
        note = " ".join(" ".join(e["lines"]).split()).lower()
        e["tn_ok"] = not e["approved"] and bool(re.search(r"technical\s+(noun|verb)", note))
    idx = {}
    for e in entries:
        for key in [e["head"].lower(), *e["forms"]]:
            idx.setdefault(key, []).append(e)
    return idx


def candidates(word):
    yield word
    for suf, rep in (("'s", ""), ("ies", "y"), ("es", ""), ("s", ""), ("ied", "y"), ("ed", ""),
                     ("ed", "e"), ("d", ""), ("ing", ""), ("ing", "e"), ("ly", "")):
        if word.endswith(suf) and len(word) > len(suf) + 2:
            stem = word[: -len(suf)]
            yield stem + rep
            if suf in ("ed", "ing") and len(stem) > 2 and stem[-1] == stem[-2] and stem[-1] not in "aeiouls":
                yield stem[:-1]  # doubled consonant: chipped -> chip, plugged -> plug


IRREGULAR_BASE = {"driven": "drive", "given": "give", "taken": "take", "written": "write", "broken": "break",
                  "chosen": "choose", "frozen": "freeze", "hidden": "hide", "shaken": "shake", "spoken": "speak",
                  "stolen": "steal", "thrown": "throw", "worn": "wear", "torn": "tear", "drawn": "draw",
                  "grown": "grow", "flown": "fly", "risen": "rise", "fallen": "fall", "forgotten": "forget",
                  "bitten": "bite", "eaten": "eat", "beaten": "beat", "ridden": "ride", "woken": "wake",
                  "drove": "drive", "gave": "give", "took": "take", "wrote": "write", "broke": "break",
                  "chose": "choose", "froze": "freeze", "threw": "throw", "wore": "wear", "tore": "tear",
                  "drew": "draw", "grew": "grow", "flew": "fly", "rose": "rise", "fell": "fall", "ate": "eat",
                  "began": "begin", "begun": "begin", "sank": "sink", "sunk": "sink", "swung": "swing",
                  "stuck": "stick", "struck": "strike", "sought": "seek", "fought": "fight", "bound": "bind",
                  "wound": "wind", "dug": "dig", "spun": "spin", "slid": "slide", "bent": "bend", "lent": "lend"}


def hits_for(idx, word):
    hits = next((idx[c] for c in candidates(word) if c in idx), None)
    if hits:
        return hits
    if word in IRREGULAR_BASE and IRREGULAR_BASE[word] in idx:
        return idx[IRREGULAR_BASE[word]]
    return comparative(idx, word)


def comparative(idx, word):
    """Comparatives and superlatives of adjectives: bigger, finer, greatest, fainter."""
    for suf in ("iest", "ier", "est", "er"):
        if word.endswith(suf) and len(word) > len(suf) + 2:
            stem = word[: -len(suf)]
            for base in (stem + "y" if suf.startswith("i") else stem, stem + "e", stem[:-1]):
                adj = [e for e in idx.get(base, []) if e["pos"] in ("adj", "adv")]
                if adj:
                    return adj
    return None


def alternatives(e):
    return list(dict.fromkeys(f"{w} ({p})" for w, p in ALT.findall("\n".join(e["lines"]))))


def describe(e):
    tag = "APPROVED" if e["approved"] else "NOT APPROVED"
    pos = f" ({e['pos']})" if e["pos"] else ""
    if e["approved"]:
        return f"{tag}: {e['head']}{pos}"
    return f"{tag}: {e['head']}{pos} -> use {', '.join(alternatives(e)) or '(see lookup)'}"


def lookup(idx, words, terms=None):
    terms = terms or {}
    for w in words:
        key = " ".join(tokens(w))
        term = terms.get(key) or next((terms[c] for c in candidates(key) if c in terms), None)
        if term:
            print(f"== TERM ({term['tag']}) in {term['src']}: {w} is allowed as {term['tag']}"
                  + (f". Not: {', '.join(term['not'])}" if term["not"] else ""))
        hits = hits_for(idx, w.lower())
        if not hits and term:
            print()
            continue
        if not hits:
            print(f"== {w}: not in dictionary (allowed only as a technical noun/verb, rules 1.5/1.12)\n")
            continue
        for e in hits:
            print("== " + describe(e))
            print("\n".join(e["lines"]) + "\n")


class Lexicon:
    """Facts derived from the dictionary that the structure checks need."""

    def __init__(self, idx):
        self.idx = idx
        verbs = [e for es in idx.values() for e in es if e["pos"] == "v"]
        # base forms of all verbs, approved or not ("check", "utilize", "push")
        self.verb_base = {e["head"].lower() for e in verbs if " " not in e["head"]}
        # past participles: the third listed form of an approved verb (WRITE: WRITES, WROTE, WRITTEN)
        self.participles = {e["forms"][2] for e in verbs if e["approved"] and len(e["forms"]) >= 3}
        self.participles |= set(IRREGULAR_PARTICIPLES.split())
        self.ing_ok = {k for k, es in idx.items() if k.endswith("ing") and any(e["approved"] for e in es)}
        # irregular forms ("has" -> "have") from the approved entries' form lists
        self.lemma = {k: e["head"].lower() for k, es in idx.items() for e in es if k in e["forms"]}

    def is_participle(self, w):
        return w in self.participles or (w.endswith("ed") and not w.endswith("eed") and len(w) > 4)

    def is_verb_stem(self, w):
        return any(c in self.verb_base for c in candidates(w))


IRREGULAR_PARTICIPLES = (
    "been done gone made taken given seen known shown written built sent set kept held left put "
    "found told brought bought caught taught thought got gotten begun broken chosen driven eaten "
    "fallen forgotten frozen hidden ridden risen run shaken spoken stolen thrown torn worn woken "
    "withdrawn understood undone overridden rewritten rebuilt reset split shut hit cut read paid lost won")

# ---------------------------------------------------------------- term files


def tokens(s):
    return [re.sub(r"'s$", "", w.lower()) for w in re.findall(r"[A-Za-z][A-Za-z'-]*", s)]


def term_files(start_dirs):
    """Bundled terms/*.md, then the nearest ste-terms.md above each start dir (up to the git root)."""
    files = sorted((SKILL / "terms").glob("*.md"))
    for d in start_dirs:
        for p in [d, *d.parents]:
            if (p / "ste-terms.md").is_file():
                files.append(p / "ste-terms.md")
                break
            if (p / ".git").exists():
                break
    return list(dict.fromkeys(f.resolve() for f in files))


def parse_terms(text, source):
    """Lines like '- repository (TN): a Git repository. Not: repo, codebase'."""
    terms = {}
    pat = r"^\s*[-*]\s+(.+?)\s+\(((?:TN|TV)(?:,\s*(?:TN|TV))?)\)(?::\s*(.*))?$"
    for m in re.finditer(pat, text, re.M):
        note = m.group(3) or ""
        nots = re.search(r"\bNot:\s*(.+?)\.?\s*$", note)
        terms[" ".join(tokens(m.group(1)))] = {
            "tag": m.group(2).replace(" ", ""), "src": source,
            "not": [" ".join(tokens(n)) for n in nots.group(1).split(",")] if nots else []}
    return terms


def find_terms(lower, terms):
    """Map each word position covered by a term to that term, longest match first."""
    covered = {}
    longest = max((len(k.split()) for k in terms), default=0)
    for n in range(longest, 0, -1):
        for i in range(len(lower) - n + 1):
            if any(j in covered for j in range(i, i + n)):
                continue
            for c in candidates(lower[i + n - 1]):
                key = " ".join(lower[i:i + n - 1] + [c])
                if key in terms:
                    for j in range(i, i + n):
                        covered[j] = key
                    break
    return covered

# ---------------------------------------------------------------- Markdown to sentences

NOTICE = re.compile(r"^(?:>\s*)?(?:\*\*|__)?(?:\[!)?(NOTE|WARNING|CAUTION|DANGER|IMPORTANT|TIP)\b\]?(?:\*\*|__)?:?\s*", re.I)
LIST_ITEM = re.compile(r"^\s*(?:[-*+•]|\d+[.)]|[A-Z][.)](?=\s+[A-Z])|\(\d+\)|\([a-z]\))\s+")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])|(?<=:)\s*\n")


def mask(src):
    """Blank out text the rules do not apply to, keeping line numbers. Masked spans become "_0_",
    which counts as one word and is not a token (rule 8.6: quoted text, labels, code)."""
    def blank(m):
        return "\n" * m.group().count("\n")
    src = re.sub(r"\A---\n.*?\n---\n", blank, src, flags=re.S)          # YAML frontmatter
    src = re.sub(r"^[ \t]*(```|~~~).*?^[ \t]*\1[^\n]*$", blank, src, flags=re.S | re.M)
    src = re.sub(r"<!--.*?-->", blank, src, flags=re.S)
    src = re.sub(r"^[ \t]*\{%-?\s*(?:end)?\w+[^%\n]*%\}[ \t]*$", "", src, flags=re.M)  # Liquid block tags
    src = re.sub(r"\{%.*?%\}|\{\{.*?\}\}", " _0_ ", src)
    src = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", src)                    # images
    src = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", src)                  # links keep their text
    src = re.sub(r"https?://\S+|`[^`\n]*`|\"[^\"\n]*\"|“[^”\n]*”", " _0_ ", src)
    src = re.sub(r"\*\*[^*\n]+\*\*|__[^_\n]+__", " _0_ ", src)           # bold = UI label
    src = re.sub(r"</?[a-zA-Z][^>]*>", " ", src)
    return re.sub(r"\*\*|__|(?<!\w)[*_](?=\S)|(?<=\S)[*_](?!\w)", "", src)


def sentences(src):
    """Yield dicts: line, kind (heading/list/table/para), notice, para (id), text."""
    lines = mask(src).split("\n")
    blocks, cur = [], None   # block = consecutive lines of one paragraph, list item, heading, or row
    for n, raw in enumerate(lines, 1):
        line = raw.strip()
        quoted = line.startswith(">")
        line = re.sub(r"^>\s?", "", line).strip()
        if not line:
            cur = None
            continue
        if line.startswith("#"):
            kind, line = "heading", line.lstrip("#").strip()
        elif line.startswith("|"):
            if re.fullmatch(r"[|:\-\s]+", line):
                continue
            for cell in filter(None, (c.strip() for c in line.strip("|").split("|"))):
                blocks.append({"line": n, "kind": "table", "text": cell, "notice": None})
            cur = None
            continue
        elif LIST_ITEM.match(line):
            kind, line = "list", LIST_ITEM.sub("", line)
        elif cur and cur["kind"] in ("para", "list") and (cur["quoted"] == quoted):
            cur["text"] += "\n" + line
            continue
        else:
            kind = "para"
        m = NOTICE.match(line)
        notice = m.group(1).upper() if m else (cur["notice"] if cur and quoted else None)
        if m:
            line = line[m.end():]
        cur = {"line": n, "kind": kind, "text": line, "notice": notice, "quoted": quoted}
        blocks.append(cur)
    for p, b in enumerate(blocks):
        start = 0
        for part in SENTENCE_END.split(b["text"]):
            off = b["text"].find(part, start)
            start = off + len(part)
            if part.strip(" \n:"):
                yield {"line": b["line"] + b["text"][:off].count("\n"), "kind": b["kind"],
                       "notice": b["notice"], "para": p, "text": " ".join(part.split())}

# ---------------------------------------------------------------- structure rules

BE = {"am", "is", "are", "was", "were", "be", "been", "being", "isn't", "aren't", "wasn't", "weren't"}
HAVE = {"has", "have", "had", "having"}
MODALS = {"can", "could", "must", "will", "shall", "should", "would", "may", "might"}
SKIP_ADV = {"not", "also", "then", "now", "first", "next", "always", "never", "only", "still", "just",
            "already", "usually", "automatically", "immediately", "carefully", "again", "all", "both"}
COND = {"if", "when", "before", "after", "while", "until", "unless", "during", "to", "for", "in",
        "on", "at", "with", "from", "as", "once"}
LEAD = {"then", "also", "now", "next", "first", "finally", "again", "carefully", "immediately",
        "optionally", "please", "and"}
OBJECT_START = {"the", "a", "an", "it", "them", "this", "these", "that", "those", "your", "all",
                "each", "one", "two", "its"}
FUNCTION = {"the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "at", "by", "from",
            "is", "are", "was", "were", "be", "it", "this", "that", "these", "those", "you", "your",
            "not", "no", "if", "when", "then", "as", "can", "must", "will", "do", "does", "all"}
UNITS = (r"(?:%|°[CF]?|ms|s|sec|seconds?|min|minutes?|h|hours?|days?|weeks?|months?|years?|mm|cm|m|km|"
         r"ft|kg|g|lb|V|W|kW|Hz|kHz|MHz|GHz|kPa|psi|bar|KB|MB|GB|TB|px|°C|°F)")
PHRASAL = {"set up": "install, configure, prepare", "log in": "type your credentials, connect",
           "log on": "connect", "log out": "disconnect", "sign in": "connect",
           "sign up": "make an account", "sign out": "disconnect", "fill in": "type, write",
           "fill out": "complete", "find out": "find, identify", "look up": "find",
           "back up": "make a copy of", "roll back": "go back to, revert (TV)",
           "start up": "start", "check in": "commit (TV)", "check out": "use `git switch`",
           "pick up": "get", "bring up": "show, open", "clean up": "clean, remove",
           "break down": "divide", "plug in": "connect", "write down": "record, write",
           "spin up": "start", "roll out": "release, deploy", "opt in": "select",
           "opt out": "clear the selection", "figure out": "find, identify", "point out": "show",
           "carry on": "continue", "end up": "become, stop", "make up": "be", "give off": "release, emit (TV)",
           "come across": "find", "turn into": "become", "run out": "become empty"}
CONDITION_AFTER = re.compile(r",?\s\b(if|before)\b\s", re.I)  # "when"/"after" trail correctly in STE too
VERBAL_BEFORE = {"before", "after", "when", "while", "by", "without", "for", "of", "in", "on", "from", "about",
                 "instead", "avoid", "start", "stop", "continue", "prevent"}
CLAUSE_VERBS = re.compile(r"\b(make sure|makes sure|show|shows|tell|tells|recommend|recommends)\b(?:\s+(?:you|us|them))?\s+(?!that\b)(\w+)", re.I)
NUMBER_WORDS = set("zero one two three four five six seven eight nine ten eleven twelve twenty thirty "
                   "forty fifty hundred thousand million first second third fourth fifth half".split())
NOT_CHECKED = ("1.3 meaning, 1.9 short TN, 2.1-2.2 noun clusters, 3.3, 3.6 passive without a named agent, 3.7 verb for action, "
               "4.3 lists, 4.4 connecting words, 4.5 articles, 5.2 one instruction, 5.4 other conditions, "
               "6.1-6.2 structure, 6.4-6.5 paragraph topics, 8.2 hyphens, 8.3 parentheses, 9.1-9.2, "
               "GR-1 \"that\" after other verbs, GR-2 \"with\", GR-3/GR-4 pronouns, GR-5 false friends, GR-7 inclusive language")
LATIN = re.compile(r"\b(e\.g\.|i\.e\.|etc\.|cf\.|viz\.|vs\.|et al\.|N\.B\.)", re.I)
CONTRACTION = re.compile(r"\b\w+n't\b|\b\w+'(?:re|ve|ll|d|m)\b|\b(?:it|that|there|here|what|who|where|let|he|she)'s\b", re.I)
BRITISH = ((r"our$", "or"), (r"ise$", "ize"), (r"ised$", "ized"), (r"ising$", "izing"),
           (r"isation$", "ization"), (r"yse$", "yze"), (r"tre$", "ter"), (r"lled$", "led"),
           (r"lling$", "ling"), (r"ogue$", "og"), (r"ence$", "ense"))


def word_count(text):
    """Rule 8.5-8.7: parentheses, numbers with units, and hyphenated words count as one word."""
    t = re.sub(r"\([^)]*\)", " _0_ ", text)
    t = re.sub(rf"\b\d[\d.,]*\s*{UNITS}(?=\W|$)", " _0_ ", t)
    return len([w for w in t.split() if re.search(r"\w", w)])


def imperative(words, lex, terms):
    """True when the sentence gives an instruction: optional leading condition, then a base-form verb."""
    w = [x.lower() for x in words]
    if w and w[0] in COND and "," in " ".join(words):
        cut = next(i for i, x in enumerate(words) if x.endswith(","))
        w = w[cut + 1:]
    while w and w[0] in LEAD:
        w = w[1:]
    if len(w) >= 2 and w[0] in ("do", "don't") and w[1] in ("not", "a", "the", "this", "these", "an"):
        return True
    if not w or (len(w) > 1 and (w[1] in BE | HAVE | MODALS)):
        return False
    first = w[0].strip(",.:")
    return first in lex.verb_base or "TV" in terms.get(first, {}).get("tag", "")


def structure(sents, lex, terms, mode):
    """Yield (line, rule, severity, message). severity: error = must fix, check = decide."""
    paras = {}
    for s in sents:
        words = s["text"].split()
        low = [re.sub(r"[^\w'-]", "", x.lower()) for x in words]
        imp = imperative(words, lex, terms)
        ln = s["line"]
        if s["kind"] == "para":
            paras.setdefault(s["para"], []).append(s)
        if s["kind"] not in ("heading", "table"):
            procedural = mode == "procedure" or (mode == "auto" and imp)
            limit, rule = (20, "5.1") if procedural else (25, "6.3")
            n = word_count(s["text"])
            if n > limit:
                kind = "instruction" if procedural else "descriptive sentence"
                yield ln, rule, "error", f"{n} words ({kind}, max {limit}): \"{s['text'][:70]}...\""
        if mode == "descriptive" and imp and not s["notice"]:
            yield ln, "6", "check", f"Instruction in descriptive text: \"{s['text'][:60]}\""
        if imp and s["kind"] != "heading":
            m = CONDITION_AFTER.search(s["text"])
            if m and m.start() > 0:
                yield ln, "5.4", "check", f"Condition after the instruction (\"{m.group(1)} ...\"). If the reader must know it first, start with it: \"{m.group(1).capitalize()} ..., <instruction>.\""
        for m in CLAUSE_VERBS.finditer(s["text"]):
            after = [x.lower().strip(".,") for x in s["text"][m.end(2):].split()[:5]]
            if m.group(2).lower() in ("if", "how", "which", "what", "when", "where", "who", "why"):
                continue  # the clause already has its conjunction: "shows if it can merge"
            if "to" in after[:4] and m.group(1).lower() in ("tell", "tells"):
                continue  # "tell two persons to ..." takes an infinitive, not a clause
            if m.group(1).lower() in ("make sure", "makes sure") or any(x in BE | MODALS for x in after):
                yield ln, "GR-1", "check", f"Add \"that\" after \"{m.group(1)}\" to show where the new clause starts."
        if mode == "procedure" and not imp and not s["notice"] and s["kind"] in ("list", "para") \
                and not (low and low[0] in COND):
            yield ln, "5.3", "check", f"Procedure step without a command: \"{s['text'][:60]}\""
        if s["notice"] == "NOTE" and imp:
            yield ln, "5.5", "error", f"A note must not give an instruction: \"{s['text'][:60]}\""
        for i, w in enumerate(low):
            nxt = [x for x in low[i + 1:i + 5] if x not in SKIP_ADV and not x.endswith("ly")]
            if not nxt:
                continue
            noun_after = len(nxt) > 1 and nxt[0] != "been" and nxt[1].isalpha() and \
                nxt[1] not in DETERMINERS | OBJECT_START | PREPS | {"by", "and", "or"}
            if w in HAVE and lex.is_participle(nxt[0]) and nxt[0] != "to" and not noun_after:
                group = " ".join([w, nxt[0]] + (nxt[1:2] if nxt[0] == "been" and len(nxt) > 1 else []))
                yield ln, "3.2", "error", f"Perfect tense \"{group}\". Use the simple past or present."
            elif w in BE and nxt[0].endswith("ing") and len(nxt[0]) > 4 and nxt[0] not in lex.ing_ok:
                if nxt[0] == "going" and len(nxt) > 1 and nxt[1] == "to":
                    yield ln, "3.2", "error", f"\"{w} going to\". Use the simple future (will)."
                else:
                    yield ln, "3.2", "error", f"Progressive tense \"{w} {nxt[0]}\". Use the simple present or past."
            elif w in MODALS and nxt[0] in ("have", "be", "been") and len(nxt) > 1 and (
                    lex.is_participle(nxt[1]) or nxt[1].endswith("ing") or nxt[1] == "able"):
                yield ln, "3.4", "error", f"Complex verb \"{w} {nxt[0]} {nxt[1]}\". Use one simple verb form."
            elif w in BE and nxt[0] == "to" and len(nxt) > 2 and nxt[1] == "be":
                yield ln, "3.4", "error", f"Complex verb \"{w} to be {nxt[2]}\". Use an instruction or one simple verb form."
            elif w in BE and lex.is_participle(nxt[0]) and w != "being" and not (i and low[i - 1] in HAVE | MODALS):
                agent = "by" in low[i + 2:i + 5]
                if agent:
                    yield ln, "3.6", "error", f"Passive with a known agent \"{w} {nxt[0]} by ...\". Use the active voice."
            verbal = (i and low[i - 1] in VERBAL_BEFORE) or i == 0 or (
                i + 1 < len(low) and low[i + 1] in DETERMINERS | OBJECT_START)
            if w.endswith("ing") and w not in lex.ing_ok and not (i and low[i - 1] in BE) and verbal \
                    and (lex.is_verb_stem(w[:-3]) or w[:-3] + "e" in lex.verb_base):
                yield ln, "3.5", "check", f"\"{w}\": use -ing only in a technical noun or as a modifier in one."
        for p, alt in PHRASAL.items():
            m = re.search(rf"(\w+\s+)?\b{p.split()[0]}\w*\s+{p.split()[1]}\b", s["text"], re.I)
            if m and (m.group(1) or "").strip().lower() not in DETERMINERS:  # "the logs in" is a noun
                yield ln, "9.3", "error", f"Phrasal verb \"{p}\". Use one verb: {alt}."
        for m in CONTRACTION.finditer(s["text"]):
            yield ln, "4.2", "error", f"Contraction \"{m.group()}\". Write the words in full."
        for m in re.finditer(r"\babout\s+(\d[\d.,]*|one|two|three|four|five|six|seven|eight|nine|ten)\b", s["text"], re.I):
            yield ln, "1.3", "error", f"\"{m.group()}\": ABOUT means \"concerned with\" only. For a quantity, use APPROXIMATELY."
        for m in LATIN.finditer(s["text"]):
            yield ln, "GR-6", "error", f"Latin abbreviation \"{m.group()}\". Write \"for example\", \"that is\", or a list."
        if ";" in s["text"]:
            yield ln, "8.1", "error", "Semicolon. Write two sentences."
        if s["notice"] in ("WARNING", "CAUTION") and s["kind"] != "heading":
            group = [x for x in sents if x["para"] == s["para"]]
            if s is group[0]:
                if not imperative(words, lex, terms) and low and low[0] not in COND:
                    yield ln, "7.2", "error", f"{s['notice']}: start with a clear command or condition."
                if len(group) < 2:
                    yield ln, "7.3", "error", f"{s['notice']}: add a sentence that tells the risk or the result."
    for p, group in paras.items():
        if len(group) > 6 and not any(s["notice"] for s in group):
            yield group[0]["line"], "6.6", "error", f"Paragraph has {len(group)} sentences (max 6)."


VERB_BEFORE = {"to", "can", "could", "must", "will", "shall", "should", "would", "may", "might", "do", "does",
               "did", "not", "you", "we", "they", "i", "he", "she", "don't", "cannot", "and", "then", "or"}
PARTICLES = {"on", "off", "up", "down", "in", "out", "back", "away", "over", "into", "onto"}


DETERMINERS = {"the", "a", "an", "this", "these", "that", "those", "your", "its", "all", "each", "some", "any",
               "no", "every", "both", "many", "more", "most", "other", "another", "their", "our", "his", "her",
               "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
PREPS = {"in", "on", "at", "from", "to", "into", "onto", "with", "for", "by", "through", "across", "along",
         "against", "between", "under", "over", "above", "below", "around", "about", "off", "out", "up",
         "down", "away", "back", "of"}


def verb_slots(text, lex):
    """Positions (as in tokens()) where a word is used as a verb. Signals, from strongest:
    after "to" or a modal, pronoun, or "do not" ("to pump", "you pump", "do not clamp");
    a command at the start of a clause, followed by an object, particle, or preposition
    ("Bolt the cover", "If ..., adhere to the rules"); a verb after a noun subject, followed by
    an object or preposition ("The bin abuts the surface"). Other positions read as nouns:
    after a determiner or another verb ("the fuel sample", "supply power")."""
    raw = re.findall(r"[A-Za-z][A-Za-z'-]*|\d+|[,;:.!?()]", text)
    words = [(i, re.sub(r"'s$", "", t.lower())) for i, t in enumerate(raw) if t[0].isalpha()]
    slots = set()
    for n, (i, w) in enumerate(words):
        prev = raw[i - 1].lower() if i else "."
        nxt = raw[i + 1].lower() if i + 1 < len(raw) else "."
        follows = nxt in OBJECT_START or nxt in PARTICLES or nxt in PREPS or nxt in DETERMINERS
        before_prev = raw[i - 2].lower() if i > 1 else "."
        prev_is_verb = any(c in lex.verb_base for c in candidates(prev)) and before_prev not in DETERMINERS
        if prev == "to":
            if nxt not in ",.;:!?)":
                slots.add(n)
        elif prev in VERB_BEFORE - {"and", "then", "or"} | {"it"}:
            slots.add(n)
        elif prev in ",;:.!?(" or prev in LEAD or prev in ("and", "then", "or"):
            # a command starts the clause, unless the word is a subject: "Fuel collects", "Water in fuel"
            nxt_is_verb = nxt in BE | MODALS | HAVE or (nxt.endswith("s") and nxt[:-1] in lex.verb_base)
            plural = w.endswith("s") and not w.endswith("ss")
            if follows and nxt not in PREPS - {"to"} or nxt.endswith("ing") or (
                    nxt[:1].isalpha() and not nxt_is_verb and not plural and nxt not in ("and", "or")):
                slots.add(n)
        elif follows and prev not in DETERMINERS and prev not in PREPS and not prev.isdigit() \
                and not prev_is_verb and (not w.endswith("s") or nxt in DETERMINERS | OBJECT_START):
            slots.add(n)  # an -s form needs an object to read as a verb: "abuts the", not "bolts on"
        elif nxt in ",.;:!?)" or nxt.endswith("ly") or nxt in ("again", "overboard", "open", "closed"):
            # a verb that ends its clause after a noun subject: "the values differ", "the disk bursts"
            prev_adj = any(e["pos"] in ("adj", "adv") for e in (hits_for(lex.idx, prev) or []))
            subject = prev.endswith("s") and not prev.endswith("ss")
            if subject and prev not in DETERMINERS | PREPS and not prev_adj and not prev_is_verb:
                slots.add(n)
    return slots


def american(word, idx, terms):
    for pat, rep in BRITISH:
        alt = re.sub(pat, rep, word)
        if alt != word and (hits_for(idx, alt) or alt in terms):
            return alt
    return None

# ---------------------------------------------------------------- check


def analyze(idx, src, terms, mode="auto"):
    """Return the findings as data: words, structure, used terms, unknown words, sentences."""
    lex = Lexicon(idx)
    sents = list(sentences(src))
    forbidden = {n: t for t, v in terms.items() for n in v["not"] if n}
    word_flags, unknown, used, spelling, tn_nouns = {}, {}, {}, {}, {}

    def flag(key, line, hits, term=None, note=None):
        f = word_flags.setdefault(key, {"lines": [], "hits": hits, "term": term, "note": note})
        if line not in f["lines"]:
            f["lines"].append(line)

    for s in sents:
        low = tokens(s["text"])
        verbs_here = verb_slots(s["text"], lex)
        covered = find_terms(low, {**terms, **{k: None for k in forbidden}})
        for i, key in list(covered.items()):
            if key in forbidden:
                t = forbidden[key]
                flag(key, s["line"], [], note=f"1.11: use \"{t}\", not \"{key}\" ({terms[t]['src']})")
                covered[i] = None
        for n in (3, 2):  # unapproved phrases, also inflected: "has to", "carried out"
            for i in range(len(low) - n + 1):
                if i in covered:
                    continue
                rest = " ".join(low[i + 1:i + n])
                for first in dict.fromkeys([*candidates(low[i]), lex.lemma.get(low[i], "")]):
                    hits = [e for e in idx.get(f"{first} {rest}", []) if not e["approved"]]
                    if hits:
                        flag(" ".join(low[i:i + n]), s["line"], hits)
                        covered.update({j: None for j in range(i, i + n)})
                        break
        for i, w in enumerate(low):
            term = covered.get(i)
            if i in covered and term is None:
                continue
            hits = hits_for(idx, w)
            if term:
                used[term] = terms[term]["tag"]
                # keep the dictionary flag: the term may be allowed only as another part of speech
                if hits and not all(e["approved"] for e in hits) and len(term.split()) == 1:
                    flag(w, s["line"], hits, term=term)
            elif hits and w.endswith("er") and not any(c in idx for c in candidates(w)) \
                    and w not in IRREGULAR_BASE and comparative(idx, w) is not None \
                    and not ((i + 1 < len(low) and low[i + 1] == "than") or
                             (i and low[i - 1] in BE | {"much", "even", "no", "any", "a", "little", "become", "becomes"})):
                unknown.setdefault(w, s["line"])  # "damper", "holder": a noun, not a comparative
            elif w in ("been", "being"):
                flag(w, s["line"], [], note="1.4: not an approved form of BE (use IS, ARE, WAS, WERE)")
            elif w in NUMBER_WORDS or len(w) == 1:  # single letters are identifiers (step A, -a)
                continue
            elif "'" in w:
                continue  # contractions are reported by rule 4.2
            elif not hits:
                alt = american(w, idx, terms)
                if alt:
                    spelling.setdefault(w, (alt, s["line"]))
                else:
                    unknown.setdefault(w, s["line"])
            elif all(not e["approved"] and e["pos"] == "adj" for e in hits) and (
                    i + 1 >= len(low) or low[i + 1] in PREPS | BE | MODALS | {"and", "or", "that", "is"}) \
                    and not (i and low[i - 1] in BE | {"very", "more", "most", "too", "so", "not", "become",
                                                       "becomes", "seem", "seems", "remain", "remains"}):
                tn_nouns.setdefault(w, s["line"])  # rule 1.6: rejected only as an adjective; used as a noun here
            elif all(not e["approved"] and e["pos"] == "v" for e in hits) and w.endswith("ing") \
                    and w not in {e["head"].lower() for e in hits} and i not in verbs_here:
                flag(w, s["line"], hits)  # rule 3.5: OK only inside a technical noun ("switching relay")
                word_flags[w]["ing_modifier"] = True
            elif all(not e["approved"] and e["pos"] == "v" for e in hits) and i not in verbs_here \
                    and not (w.endswith("ed") and w not in {e["head"].lower() for e in hits}):
                tn_nouns.setdefault(w, s["line"])  # rule 1.6: only the verb is not approved; the noun is a TN
            elif not all(e["approved"] for e in hits):
                flag(w, s["line"], hits)

    findings = sorted(set(structure(sents, lex, terms, mode)), key=lambda f: (f[0], f[1]))
    findings += [(ln, "1.14", "error", f"Use American spelling \"{alt}\", not \"{w}\".")
                 for w, (alt, ln) in spelling.items()]
    findings.sort(key=lambda f: (f[0], f[1]))

    return {"words": word_flags, "structure": findings, "used": used, "unknown": unknown, "tn_nouns": tn_nouns,
            "sentences": [s["text"] for s in sents]}


def render(res, terms, files, mode):
    word_flags, findings, used, unknown = res["words"], res["structure"], res["used"], res["unknown"]
    bundled = SKILL / "terms"
    names = [f.name if f.parent == bundled else str(f) for f in files]
    print(f"Mode: {mode}. Term files: {', '.join(names) or 'none'}")
    if all(f.parent == bundled for f in files):
        print("  (no project ste-terms.md found)")

    if word_flags:
        print("\nWORDS")
        width = max(len(k) for k in word_flags) + 2
        for key, f in word_flags.items():
            if f["note"]:
                detail = f["note"]
            else:
                ok = sorted({e["pos"] or "-" for e in f["hits"] if e["approved"]})
                bad = [e for e in f["hits"] if not e["approved"]]
                parts = [f"OK as {'/'.join(ok)}"] if ok else []
                parts += [f"not as {e['pos'] or 'phrase'} -> {', '.join(alternatives(e)) or 'see lookup'}" for e in bad]
                if f.get("ing_modifier"):
                    parts.append("-ing form: OK only as part of a technical noun (3.5), otherwise use the alternative")
                if any(e.get("tn_ok") for e in f["hits"]):
                    parts.append("the dictionary allows it as a technical noun or verb in some meanings (see lookup)")
                if f["term"]:
                    tag = terms[f["term"]]["tag"]
                    parts.append(f"TERM ({tag}) in {terms[f['term']]['src']}: OK only as {tag}")
                detail = "; ".join(parts)
            print(f"  {key:<{width}}{detail}\n  {'':<{width}}lines: {', '.join(map(str, f['lines']))}")
    if findings:
        print("\nSTRUCTURE")
        for ln, rule, sev, msg in findings:
            print(f"  L{ln:<4}{rule:<6}{sev:<7}{msg}")
    if used:
        print("\nTERMS USED (TN = noun only, TV = verb only)")
        print("  " + ", ".join(f"{t} ({tag})" for t, tag in sorted(used.items())))
    if res["tn_nouns"]:
        print("\nNOUNS USED AS TECHNICAL NOUNS (the dictionary rejects only the verb; rule 1.6. Never use them as verbs)")
        print("  " + ", ".join(sorted(res["tn_nouns"])))
    if unknown:
        print("\nNOT IN DICTIONARY (keep only technical nouns, technical verbs, or proper nouns)")
        print("  " + ", ".join(sorted(unknown)))
    errors = sum(1 for f in findings if f[2] == "error")
    checks = len(findings) - errors
    print(f"\nSUMMARY: {len(word_flags)} word findings, {errors} structure errors, {checks} to check, "
          f"{len(unknown)} words not in dictionary")
    print("\nNOT CHECKED (check these by reading; see references/rules.md):\n  " + NOT_CHECKED)
    return 1 if word_flags or findings else 0


def check(idx, src, terms, files, mode="auto"):
    return render(analyze(idx, src, terms, mode), terms, files, mode)


def hard(key, f):
    """A word finding that no use can make correct: not approved in any part of speech, not a term,
    and not offered by its own entry as a technical noun or verb (list (v) -> LIST (TN))."""
    own_term = any(a.lower() in (f"{key} (tn)", f"{key} (tv)") for e in f["hits"] for a in alternatives(e))
    if f.get("ing_modifier"):
        return False
    tn_note = any(e.get("tn_ok") for e in f["hits"])
    return bool(f["note"]) or not (f["term"] or own_term or tn_note or any(e["approved"] for e in f["hits"]))


def compare(idx, before_src, after_src, terms, mode):
    """CHANGE REPORT: what the rewrite fixed, kept, and introduced, computed from both texts."""
    b, a = analyze(idx, before_src, terms, mode), analyze(idx, after_src, terms, mode)
    print("\nCHANGE REPORT (original -> rewrite)")
    sb, sa = b["sentences"], a["sentences"]
    same = sum(1 for s in sa if s in set(sb))
    print(f"  Sentences: {len(sb)} -> {len(sa)} ({len(sa) - same} new or rewritten, {same} unchanged)")
    bw, aw = set(b["words"]), set(a["words"])
    words = {**b["words"], **a["words"]}

    def names(keys):  # "*" marks a part-of-speech reminder: the word is approved or a term in some use
        return ", ".join(k + ("" if hard(k, words[k]) else "*") for k in sorted(keys))
    print(f"  Word findings: {len(bw)} -> {len(aw)}   (* = approved in another part of speech, or a term: check the use)")
    for label, keys in (("fixed", bw - aw), ("kept", bw & aw), ("NEW", aw - bw)):
        if keys:
            print(f"    {label + ':':<7}{names(keys)}")
    count = lambda res: {r: sum(1 for f in res["structure"] if f[1] == r) for r in {f[1] for f in res["structure"]}}
    cb, ca = count(b), count(a)
    rules = sorted(set(cb) | set(ca), key=lambda r: (r.startswith("GR"), [int(x) for x in re.findall(r"\d+", r)]))
    print(f"  Structure findings: {len(b['structure'])} -> {len(a['structure'])}")
    for r in rules:
        print(f"    {r:<6}{cb.get(r, 0)} -> {ca.get(r, 0)}" + ("   NEW" if not cb.get(r) else ""))
    stem = lambda w: re.sub(r"(?<=[^s])s$", "", w)  # "permissions" and "permission" are one word
    ub, ua = {stem(w) for w in b["unknown"]}, {stem(w) for w in a["unknown"]}
    if ua - ub:
        print("  Words added that are not in the dictionary (decide: TN, TV, or replace): " + ", ".join(sorted(ua - ub)))
    if ub - ua:
        print("  Words removed that were not in the dictionary: " + ", ".join(sorted(ub - ua)))

# ---------------------------------------------------------------- selftest


def verify(report, original):
    """Each quoted original in a report ('changed: "X" -> "Y"') must occur in the original text."""
    norm = lambda s: " ".join(re.sub(r"[*_`“”\"]", "", s).lower().split())
    src, missing, found = norm(original), [], 0
    for q in re.findall(r"changed:\s*\"([^\"]+)\"\s*(?:->|→|-&gt;)", report):
        parts = [x for x in re.split(r"\.\.\.|…", norm(q)) if x.strip()]
        if all(x.strip() in src for x in parts):
            found += 1
        else:
            missing.append(q)
    print(f"VERIFY: {found} quoted originals found, {len(missing)} not found in the original")
    for q in missing:
        print(f'  NOT IN ORIGINAL: "{q}"  (correct this line of the report)')
    return 1 if missing else 0


def selftest(idx):
    import contextlib
    import io
    assert any(e["approved"] for e in idx["push"]), "PUSH should be approved"
    assert "pushed" in idx, "PUSHED should be indexed as a form"
    assert not any(e["approved"] for e in idx["abandon"]), "abandon is not approved"
    assert "GO (v)" in describe(idx["abandon"][0])
    assert "LIST (TN)" in alternatives(next(e for e in idx["list"] if e["pos"] == "v"))
    assert not idx["carry out"][0]["approved"]
    assert "are" in idx and "been" not in idx, "BE has ARE but no past participle"
    assert any(e["approved"] for e in idx["higher"]), "comparative forms must be indexed"
    raw = text()
    assert not re.search("[-]", raw), "symbol-font glyphs must be mapped"
    assert not any(PAGE_FURNITURE.match(l.strip()) for l in raw.splitlines()), "page furniture left"
    assert "degree (°)" in raw
    terms = parse_terms("- pull request (TN): x\n- commit (TN, TV)\n* gitignore (TN)\n"
                        "- repository (TN): a Git repository. Not: repo, code base\n- no tag here\n", "t")
    assert set(terms) == {"pull request", "commit", "gitignore", "repository"}
    assert terms["repository"]["not"] == ["repo", "code base"] and terms["commit"]["tag"] == "TN,TV"
    cov = find_terms(tokens("Open two pull requests and commit the .gitignore file"), terms)
    assert cov == {2: "pull request", 3: "pull request", 5: "commit", 7: "gitignore"}, cov
    assert word_count("Set the pressure to 30 kPa (approximately) in the well-known valve.") == 10
    lex = Lexicon(idx)
    assert "written" in lex.participles and "given" in lex.participles and "missing" in lex.ing_ok

    # (text, expected rule ids or word keys, ids that must not appear)
    cases = [
        ("Claude has to merge it. They carried out the test.", {"has to", "carried out"}, set()),
        ("The token has been generated.", {"3.2", "been"}, {"3.6"}),
        ("The connector's cable is long.", set(), {"GR-8"}),
        ("The system is running the test.", {"3.2"}, set()),
        ("The valve is opened by the operator.", {"3.6:error"}, set()),
        ("A fuel pump is installed in zone 10.", set(), {"3.6"}),
        ("The part must have been removed.", {"3.4"}, set()),
        ("The volume control can be adjusted.", {"3.4"}, {"3.6"}),
        ("The seat is to be installed first.", {"3.4"}, set()),
        ("It's necessary to use the tool, e.g. a wrench.", {"4.2", "GR-6"}, set()),
        ("Note: Do not remove the cover.", {"5.5"}, set()),
        ("Note: The cover is hot.", set(), {"5.5"}),
        ("WARNING: Do not touch the hot surface.", {"7.3"}, set()),
        ("WARNING: Do not touch the hot surface. It can burn you.", set(), {"7.3", "7.2"}),
        ("Set up the server; then log in.", {"9.3", "8.1"}, set()),
        ("Select the colour of the cable.", {"1.14"}, set()),
        ("Use the tool to tighten the nut. " * 1 + "Make sure that the remaining fluid is missing.", set(), {"3.5", "3.2"}),
        ("Commit the code base to the repo.", {"code base", "repo"}, set()),
        ("These areas have specified damage limits.", set(), {"3.2"}),
        ("The operator has adjusted the linkage.", {"3.2"}, set()),
        ("Hold the logs in their position.", set(), {"9.3"}),
        ("The existing workflows can stop.", {"existing"}, set()),
        ("This takes about 30 seconds.", {"1.3"}, set()),
        ("For data about the circuit breakers, refer to the list.", set(), {"1.3"}),
        ("Take care when installing the nuts.", {"3.5"}, set()),
        ("Adjust the door operating rod.", set(), {"3.5"}),
        ("Pump the fuel into the tank.", {"pump"}, set()),
        ("Check that valves do not bind.", {"bind"}, set()),
        ("Combine water and glycol.", {"combine"}, set()),
        ("If the values differ, do the test again.", {"differ"}, set()),
        ("Fuel collects in the sump.", set(), {"fuel"}),
        ("Bolts attach the panel to the frame.", set(), {"bolts"}),
        ("Install the retainer bolts on the retainer.", set(), {"bolts"}),
        ("If there is a fire, operate the crash switches.", set(), {"switches"}),
        ("Put a cover on the outlet port.", set(), {"port"}),
        ("A value of 2 mm is acceptable.", {"acceptable"}, set()),
        ("Remove the wing tip brake from the port wing.", {"port"}, set()),
        ("Start the fuel pump. Do not bolt the cover.", {"bolt"}, {"pump", "fuel"}),
        ("If the enamel is chipped, replace the unit.", {"chipped"}, set()),
        ("The pressure is greater than 200 psi.", {"greater"}, set()),
        ("The damper prevents sudden movement of the control.", set(), {"damper"}),
        ("When you are doing this procedure, obey the precautions.", {"3.2"}, set()),
        ("When the surface is dry, apply the primer.", set(), {"5.4"}),
        ("Stop the test if the light comes on.", {"5.4"}, set()),
        ("Be careful when you remove the control unit.", set(), {"5.4"}),
        ("Make sure the valve is open.", {"GR-1"}, set()),
        ("The gauge shows that the reservoir is full.", set(), {"GR-1"}),
        ("The app shows if it can merge the branch.", set(), {"GR-1"}),
        ("This compound can give off poisonous fumes.", {"9.3"}, set()),
        ("```\nverify; it's done\n```\nUse `don't` here.", set(), {"8.1", "4.2"}),
        ("Click **Create Pull Request**. Then use two flags.", set(), {"create"}),
        ("Remove the screws that attach the cover to the forward part of the housing when "
         "the system is in operation and the power is off.", {"5.1"}, set()),
        ("The system supplies power to the forward part of the housing when the engine operates "
         "and the generator is in the correct condition.", set(), {"5.1", "6.3"}),
    ]
    for src, want, avoid in cases:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            check(idx, src, terms, [], "auto")
        out = buf.getvalue()
        got = set(re.findall(r"^  L\d+\s+(\S+)\s+(error|check)", out, re.M))
        ids = {r for r, _ in got} | {f"{r}:{s}" for r, s in got}
        ids |= {m.strip() for m in re.findall(r"^  ([a-z][\w' -]*?) {2,}\S", out, re.M)}
        assert want <= ids and not (avoid & ids), f"{src!r}\nwant {want} avoid {avoid}\n{out}"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        check(idx, "---\ntitle: x\n---\n\n{% webui %}\n\n```\ncode\n```\n\n{% endwebui %}\n\nUtilize the tool.\n", {}, [])
    assert re.search(r"utilize .*\n\s+lines: 13\b", buf.getvalue()), "line numbers must match the file\n" + buf.getvalue()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        compare(idx, "Utilize the tool; it's ready, e.g. now. Verify the widget.", "Use the tool. It is ready. Verify the gizmo.", {}, "auto")
    out = buf.getvalue()
    assert re.search(r"fixed: +.*\butilize\b", out) and "e, g" not in out and re.search(r"kept: +.*\bverify\b", out), out
    assert re.search(r"NEW: +use\*", out), out
    assert re.search(r"8\.1\s+1 -> 0\n.*GR-6\s+1 -> 0", out) and "not in the dictionary (decide" in out and "gizmo" in out, out
    with contextlib.redirect_stdout(io.StringIO()):
        good = verify('- 5.4 - changed: "Apply the **primer** ... is dry" -> "When ..."', "Apply the primer when the surface is dry.")
        bad = verify('- 5.2 - changed: "make the token and keep it" -> "Make."', "Make the token. Keep it safe.")
    assert good == 0 and bad == 1, "verify must find invented quotes"
    print(f"selftest ok: {len(idx)} keys, {len(cases)} rule cases, line numbers exact, compare report, verify")


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("lookup", "check", "selftest", "verify"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    idx = index(parse(text()))
    cmd, args = args[0], args[1:]
    if cmd == "selftest":
        selftest(idx)
    elif cmd == "verify":
        if len(args) != 2 or not all(Path(a).is_file() for a in args):
            sys.exit("verify needs: REPORT ORIGINAL")
        sys.exit(verify(Path(args[0]).read_text(), Path(args[1]).read_text()))
    elif cmd == "lookup":
        terms = {}
        for f in term_files([Path.cwd()]):
            terms.update(parse_terms(f.read_text(), f.name))
        lookup(idx, args, terms)
    else:
        extra, mode, original = [], "auto", None
        while any(f in args for f in ("--terms", "--mode", "--compare")):
            flag = next(f for f in ("--terms", "--mode", "--compare") if f in args)
            i = args.index(flag)
            if i + 1 >= len(args):
                sys.exit(f"{flag} needs a value")
            if flag == "--mode":
                mode = args[i + 1]
                if mode not in ("auto", "procedure", "descriptive"):
                    sys.exit("--mode must be auto, procedure, or descriptive")
            elif flag == "--compare":
                if not Path(args[i + 1]).is_file():
                    sys.exit("--compare needs the path of the original file")
                original = Path(args[i + 1]).read_text()
            elif not Path(args[i + 1]).is_file():
                sys.exit("--terms needs the path of an existing terms file")
            else:
                extra.append(Path(args[i + 1]).resolve())
            del args[i:i + 2]
        stdin = not args or args[0] == "-"
        src = sys.stdin.read() if stdin else Path(args[0]).read_text()
        starts = [Path.cwd()] + ([] if stdin else [Path(args[0]).resolve().parent])
        files = list(dict.fromkeys(term_files(starts) + extra))
        terms = {}
        for f in files:
            terms.update(parse_terms(f.read_text(), f.name))  # project file loads last and wins
        status = check(idx, src, terms, files, mode)
        if original is not None:
            compare(idx, original, src, terms, mode)
        sys.exit(status)


if __name__ == "__main__":
    main()

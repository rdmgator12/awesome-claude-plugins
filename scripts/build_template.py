#!/usr/bin/env python3
"""One-time: derive README.template.md from the current README.md.

Replaces ONLY the machine-generated regions with placeholders — every count
and every category entry block — and leaves all prose (header, explainers,
Plugin of the Week, How to install, marketplaces, Related) verbatim. After
this runs once, the template is the hand-edited prose layer and plugins.json
is the data layer; generate_readme.py merges them.
"""

import json, re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
DATA = json.load(open(REPO / "data" / "plugins.json"))
OUT = REPO / "README.template.md"

CATS = DATA["categories"]
lines = README.read_text().splitlines()

# literal count substitutions (current live numbers -> placeholders)
COUNT_SUBS = [
    ("**Total plugins:** 333", "**Total plugins:** {{TOTAL}}"),
    (
        "Claude Code (273) · Cowork (128) · both (68)",
        "Claude Code ({{CC}}) · Cowork ({{COWORK}}) · both ({{BOTH}})",
    ),
    ("**Categories:** 28", "**Categories:** {{NCAT}}"),
    (
        "**~273 of the entries below run here.**",
        "**~{{CC}} of the entries below run here.**",
    ),
    (
        "**128 entries run here; 68 run on both.**",
        "**{{COWORK}} entries run here; {{BOTH}} run on both.**",
    ),
]

out, i = [], 0
entry_re = re.compile(
    r"^- \[[^\]]+\]\([^)]+\).*\((Claude Code, Cowork|Claude Code|Cowork)\)\s*$"
)
while i < len(lines):
    l = lines[i]
    m = re.match(r"^## (.+)$", l)
    if m and m.group(1).strip() in CATS:
        cat = m.group(1).strip()
        out.append(l)
        i += 1
        # keep any leading blank lines, then swallow the contiguous entry run into one placeholder
        while i < len(lines) and lines[i].strip() == "":
            out.append(lines[i])
            i += 1
        placed = False
        while i < len(lines) and not re.match(r"^## ", lines[i]):
            if entry_re.match(lines[i]):
                if not placed:
                    out.append(f"{{{{ENTRIES:{cat}}}}}")
                    placed = True
                i += 1  # drop original entry line
            else:
                out.append(lines[i])
                i += 1
        continue
    for a, b in COUNT_SUBS:
        if a in l:
            l = l.replace(a, b)
    out.append(l)
    i += 1

OUT.write_text("\n".join(out) + "\n")
print(f"wrote {OUT} ({len(out)} lines)")

#!/usr/bin/env python3
"""Generate README.md (+ INSTALL.md) from data/plugins.json + README.template.md.

data/plugins.json is the single source of truth for entries and counts; the
template holds all prose. Counts are computed here, so the stats line and the
body can never disagree.

    python3 scripts/generate_readme.py            # regenerate README.md + INSTALL.md
    python3 scripts/generate_readme.py --check     # verify both are up to date (CI)

Install commands are NOT inlined into the README: awesome-lint requires each
list item to end with punctuation, which a trailing `install` code span breaks.
They live in INSTALL.md instead, generated from the same `slug` field, so the
README stays awesome-lint-clean and canonical-listing-eligible.
"""

import json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = json.load(open(REPO / "data" / "plugins.json"))
TEMPLATE = (REPO / "README.template.md").read_text()
README = REPO / "README.md"
INSTALL = REPO / "INSTALL.md"


def sort_key(name):
    return re.sub(r"[^a-z0-9 ]", "", name.lower()).strip()


def render_entry(p):
    a = " **`A`**" if p["anthropic"] else ""
    desc = p["description"].rstrip(".") + "."
    uc = p["use_case"].rstrip(".") + "." if p["use_case"] else ""
    surface = ", ".join(p["surfaces"])
    line = f"- [{p['name']}]({p['url']}){a} - {desc}"
    if uc:
        line += f" *Use case: {uc}*"
    line += f" ({surface})"
    return line


# group + sort
by_cat = {c: [] for c in DATA["categories"]}
for p in DATA["plugins"]:
    by_cat[p["category"]].append(p)
for c in by_cat:
    by_cat[c].sort(key=lambda p: sort_key(p["name"]))

plugins = DATA["plugins"]
TOTAL = len(plugins)
CC = sum(1 for p in plugins if "Claude Code" in p["surfaces"])
COWORK = sum(1 for p in plugins if "Cowork" in p["surfaces"])
BOTH = sum(1 for p in plugins if len(p["surfaces"]) > 1)
NCAT = len([c for c in DATA["categories"] if by_cat[c]])

# ---- README ----
out = TEMPLATE
for k, v in {
    "{{TOTAL}}": TOTAL,
    "{{CC}}": CC,
    "{{COWORK}}": COWORK,
    "{{BOTH}}": BOTH,
    "{{NCAT}}": NCAT,
}.items():
    out = out.replace(k, str(v))
for c in DATA["categories"]:
    out = out.replace(
        f"{{{{ENTRIES:{c}}}}}", "\n".join(render_entry(p) for p in by_cat[c])
    )
leftover = re.findall(r"\{\{[^}]+\}\}", out)
if leftover:
    sys.exit(f"UNFILLED placeholders: {set(leftover)}")

# ---- INSTALL.md (Claude Code plugins with an official-marketplace slug) ----
installable = sorted(
    [p for p in plugins if "Claude Code" in p["surfaces"] and p.get("slug")],
    key=lambda p: sort_key(p["name"]),
)
lines = [
    "# Install commands",
    "",
    "One-line install for every Claude Code plugin in the official "
    "`claude-plugins-official` marketplace (auto-installed on startup). "
    "Generated from [`data/plugins.json`](data/plugins.json) — do not edit by hand.",
    "",
    "```",
    "/plugin install <name>@claude-plugins-official",
    "```",
    "",
    f"{len(installable)} plugins:",
    "",
    "| Plugin | Category | Install |",
    "| --- | --- | --- |",
]
for p in installable:
    lines.append(
        f"| {p['name']} | {p['category']} | `/plugin install {p['slug']}@claude-plugins-official` |"
    )
install_md = "\n".join(lines) + "\n"

if "--check" in sys.argv:
    stale = []
    if README.read_text() != out:
        stale.append("README.md")
    if not INSTALL.exists() or INSTALL.read_text() != install_md:
        stale.append("INSTALL.md")
    if stale:
        sys.exit(
            f"OUT OF DATE ({', '.join(stale)}) — run: python3 scripts/generate_readme.py"
        )
    print("README.md and INSTALL.md are up to date.")
else:
    README.write_text(out)
    INSTALL.write_text(install_md)
    print(
        f"wrote README.md — {TOTAL} plugins | CC {CC} · Cowork {COWORK} · both {BOTH} | {NCAT} categories"
    )
    print(f"wrote INSTALL.md — {len(installable)} installable plugins")

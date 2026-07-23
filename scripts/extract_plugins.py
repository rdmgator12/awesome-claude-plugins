#!/usr/bin/env python3
"""One-time extractor: current README.md -> data/plugins.json (the new source of truth).

Parses every category entry into structured data and matches each to its
claude-plugins-official manifest slug (for install commands). Run once to
bootstrap the data file; after that, edit plugins.json directly and use
generate_readme.py.
"""

import json, re, sys, unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
MANIFEST = (
    Path(sys.argv[1]) if len(sys.argv) > 1 else None
)  # optional marketplace.json for slugs
OUT = REPO / "data" / "plugins.json"

META_SECTIONS = {
    "Contents",
    "How to install",
    "Custom Plugins",
    "Plugin Marketplaces",
    "Related",
}
entry_re = re.compile(
    r"^- \[([^\]]+)\]\(([^)]+)\)(\s*\*\*`A`\*\*)?\s*-\s*(.*?)\s*\((Claude Code, Cowork|Claude Code|Cowork)\)\s*$"
)


def slugify(s):
    s = unicodedata.normalize("NFKC", s).lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]", "", s)


# suffix-stripping canon for slug matching (mirrors reconcile logic)
SUFFIXES = [
    "agentskills",
    "developerkit",
    "skills",
    "skill",
    "plugin",
    "mcpserver",
    "mcp",
    "lsp",
    "toolkit",
    "forcreativity",
    "agent",
    "cli",
    "development",
    "best",
    "practices",
    "cc",
]


def canon(s):
    b = slugify(s)
    changed = True
    while changed:
        changed = False
        for suf in SUFFIXES:
            if b.endswith(suf) and len(b) > len(suf) + 2:
                b = b[: -len(suf)]
                changed = True
    return b


# ---- optional manifest slug index ----
slug_by_canon = {}
if MANIFEST and MANIFEST.exists():
    for p in json.load(open(MANIFEST)).get("plugins", []):
        slug_by_canon.setdefault(canon(p["name"]), p["name"])
    # hand aliases where canon still misses (README name -> manifest slug)
    ALIAS = {
        "clsp": "csharp-lsp",
        "oracleaidataplatformdatabricksmigrator": "oracle-ai-data-platform-workbench-databricks-migrator",
        "oracleaidataplatformsparkconnectors": "oracle-ai-data-platform-workbench-spark-connectors",
        "oracleaidataplatformworkbench": "oracle-ai-data-platform-workbench-engineer-agent",
        "unrealengineskills": "unreal-engine-skills-for-claude-code",
        "pagerdutyprecommitriskscore": "pagerduty",
        "golspgopls": "gopls-lsp",
        "javalspeclipsejdtls": "jdtls-lsp",
        "cloudsqlformysql": "cloud-sql-mysql",
        "cloudsqlforpostgresql": "cloud-sql-postgresql",
        "cloudsqlforsqlserver": "cloud-sql-sqlserver",
        "firestore": "firestore-native",
        "oracledatabase": "oracledb",
        "apollographql": "apollo-skills",
        "endorlabs": "ai-plugins",
        "aikidosecurity": "aikido",
        "tdengineidmp": "idmp-plugin",
        "youcom": "youdotcom-agent-skills",
        "plugindevelopertoolkit": "plugin-dev",
        "sapmobiledevelopmentkit": "sap-mdk-server",
        "sapcdscap": "cds-mcp",
        "producttrackingskills": "producttracking",
    }


def manifest_slug(name):
    c = canon(name)
    if c in slug_by_canon:
        return slug_by_canon[c]
    if MANIFEST and MANIFEST.exists():
        return ALIAS.get(slugify(name)) or ALIAS.get(c)
    return None


# ---- parse README ----
plugins, categories = [], []
cur = None
for i, raw in enumerate(README.read_text().splitlines(), 1):
    m = re.match(r"^## (.+)$", raw)
    if m:
        cur = m.group(1).strip()
        if cur not in META_SECTIONS and cur not in categories:
            categories.append(cur)
        continue
    if cur in META_SECTIONS or cur is None:
        continue
    em = entry_re.match(raw)
    if em:
        name, url, A, desc, surf = (
            em.group(1),
            em.group(2),
            bool(em.group(3)),
            em.group(4),
            em.group(5),
        )
        surfaces = [s.strip() for s in surf.split(",")]
        slug = manifest_slug(name) if "Claude Code" in surfaces else None
        plugins.append(
            {
                "name": name,
                "url": url,
                "category": cur,
                "surfaces": surfaces,
                "anthropic": A,
                "slug": slug,  # official-marketplace slug for install command (null if not applicable)
                "description": desc,
                "use_case": None,  # split below
            }
        )

# split description "<desc> *Use case: <uc>*"
uc_re = re.compile(r"^(.*?)\s*\*Use case:\s*(.*?)\*\s*$")
for p in plugins:
    m = uc_re.match(p["description"])
    if m:
        p["description"], p["use_case"] = m.group(1).strip(), m.group(2).strip()
    else:
        p["use_case"] = ""

OUT.parent.mkdir(exist_ok=True)
json.dump(
    {"categories": categories, "plugins": plugins},
    open(OUT, "w"),
    indent=2,
    ensure_ascii=False,
)
matched = sum(1 for p in plugins if p["slug"])
cc = sum(1 for p in plugins if "Claude Code" in p["surfaces"])
print(f"extracted {len(plugins)} plugins, {len(categories)} categories")
print(f"Claude Code entries: {cc}  |  matched to a manifest slug: {matched}")
print(f"wrote {OUT}")

# Awesome List for Claude Plugins: [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0](https://img.shields.io/badge/License-CC0-blue.svg)](LICENSE) [![Last Commit](https://img.shields.io/github/last-commit/rdmgator12/awesome-claude-plugins)](https://github.com/rdmgator12/awesome-claude-plugins/commits/main)

> A free, community-maintained directory of plugins in Anthropic's official [Claude Plugins catalog](https://claude.com/plugins/) — installable bundles of skills, MCP servers, slash commands, sub-agents, and hooks that extend Claude Code and Cowork with one-command installation.

> [!NOTE]
> **This is a free, independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC.** "Claude," "Claude Code," and "Cowork" are trademarks of Anthropic PBC. Each plugin is the property of its respective owner. This list is published under the CC0 license shown in the badge above — public domain, free to copy, fork, redistribute.

**Last updated:** July 23, 2026 | **Total plugins:** {{TOTAL}} | **Surfaces:** Claude Code ({{CC}}) · Cowork ({{COWORK}}) · both ({{BOTH}}) | **Categories:** {{NCAT}}

Plugins originated in Claude Code (October 2025) as packaged, versioned, shareable directories that bundle skills, MCP server references, slash commands, sub-agents, hooks, and LSP servers into a single installable unit. As of v2.1.129 (May 6, 2026), Anthropic runs the **Official Claude Plugins Directory** (`claude-plugins-official`) — a curated, vetted catalog auto-installed on Claude Code startup. Plugins also extend **Cowork**, Anthropic's agentic workspace, with role-class workflow bundles (Productivity, Design, Marketing, etc.) used by knowledge workers inside isolated VM environments.

For more information, see the [Plugins overview](https://claude.com/docs/plugins/overview), [plugin marketplaces guide](https://code.claude.com/docs/en/plugin-marketplaces), [submission form](https://claude.com/plugins#submit), and the [official Anthropic marketplace repo](https://github.com/anthropics/claude-plugins-official) (renamed from `claude-plugins-public`; the old URL still redirects).

Plugins marked with **`A`** are built and verified by Anthropic. Each entry ends with a surface tag: `(Claude Code)`, `(Cowork)`, or `(Claude Code, Cowork)`.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> [!NOTE]
> ### Two surfaces, one list — why this is bigger than the claude.ai plugin browser
>
> Plugins run on two surfaces, and this list catalogs **both** — the surface tag on every entry tells you where each one is available:
>
> - **Claude Code** (the developer CLI) — its marketplace (`claude-plugins-official`) is the *full* catalog, auto-installed on startup and dominated by developer and infrastructure plugins: language servers, cloud (AWS/GCP/Azure/Oracle), databases, CI/CD, security, and code tooling. **~{{CC}} of the entries below run here.**
> - **Cowork** (Anthropic's agentic workspace inside claude.ai) — its plugin library surfaces a **curated business/role subset**: CRM, finance, marketing, design, data dashboards, the Anthropic role bundles, and — new this week — full **Legal** (12 role-specialized plugins) and **Healthcare / life-sciences** verticals. **{{COWORK}} entries run here; {{BOTH}} run on both.**
>
> So the plugin browser in the **claude.ai desktop app shows far fewer plugins than this list** — it's the Cowork storefront, not the whole catalog. Developer and infrastructure plugins don't appear there because they target a coding environment, not a Cowork VM. If a plugin you expected is missing from the desktop app, it's almost certainly a Claude Code–only entry.
>
> *Scope note: counts here track the official `claude-plugins-official` marketplace plus the Cowork directory. A handful of plugins ship from partner marketplaces (e.g. `techwolf-ai/ai-first-toolkit`) and appear in the public Claude Plugins catalog but not the official marketplace manifest; those are added individually as they're found.*

> [!IMPORTANT]
> ### Plugin vs Connector vs MCP vs Custom Plugin
>
> These four concepts overlap and confuse people. Here's the clean mental model:
>
> - **MCP (Model Context Protocol)** is the open standard. Servers expose tools, prompts, and resources; clients call them. Spec at [modelcontextprotocol.io](https://modelcontextprotocol.io).
> - **MCP server** is any running server implementing MCP. Remote MCP servers (internet-hosted, OAuth) work on every Claude surface; local MCP servers (stdio) work only in Claude Desktop and Claude Code.
> - **Connector** is an MCP server listed in Anthropic's [Connectors Directory](https://claude.com/partners/mcp) — reviewed by Anthropic, named-card UI, cross-surface (Claude.ai, Desktop, Mobile, Cowork, Code). Tracked in [awesome-claude-connectors](https://github.com/rdmgator12/awesome-claude-connectors).
> - **Custom Connector** is an MCP server you add yourself via Settings → "Add custom connector" with a URL. Same runtime as directory connectors; no Anthropic review; appears as "Custom".
> - **Plugin** is a packaged bundle that can contain any combination of skills, MCP server references, slash commands, sub-agents, hooks, and LSP servers. Versioned, semver, one-command install via `/plugin install`. Works on Claude Code and Cowork. **This list covers plugins.**
> - **Plugin Marketplace** is a Git repo or URL hosting `.claude-plugin/marketplace.json` that catalogs plugins. The official Anthropic marketplace (`claude-plugins-official`) is auto-installed on Claude Code startup.
> - **Custom Plugin** is a plugin you build and install from a local directory, your own Git repo, or a private marketplace. Same components as directory plugins; no Anthropic review. Install via `/plugin install`, `--plugin-dir`, or `--plugin-url`.
>
> Mental model: **Connector** = "Claude can call your API" (tool surface). **Plugin** = "Claude knows how to use your product" (workflow + tools + skills). **MCP** = the protocol both speak. Most partners ship both — a remote MCP server (connector) and a plugin that wraps it with skills and slash commands.

> [!TIP]
> ### Plugin of the Week — July 23, 2026
>
> **Litigation Legal** · *Legal*
>
> The story this week is a vertical, not a single plugin: Cowork gained an entire **Legal practice suite** — twelve role-specialized, Anthropic-built plugins covering Litigation, Corporate, IP, Employment, Privacy, Regulatory, Commercial, Product, and AI Governance work, plus Law Student, Legal Clinic (built within ABA Formal Op. 512), and a security-gated Legal Builder Hub. Litigation Legal headlines it: it manages the matter portfolio — deadlines, holds, demands, outside counsel — and does the production work too, from patent and civil claim charts to chronologies, deposition prep, privilege logs, and brief drafts, adapting to in-house, firm, or solo practice. Landing alongside it is a deep **Healthcare and life-sciences** cohort — Claude for Healthcare (prior auth, ICD-10-CM coding, FHIR) and a research bench of Open Targets, Owkin, Synapse, ToolUniverse, scvi-tools, Medidata, Cortellis, BioRender, ChEMBL, and more. This is the largest single reconcile in the list's history: **+54 plugins (279 → 333)**, almost all of it Cowork's business and professional verticals rather than the developer marketplace, which added a smaller wave of its own (New Relic, MLflow, GrowthBook, GitKraken, DeepEval, CrowdSec, Browser Use, and Anthropic's own Claude Security and Receipts). No plugins were removed: three that left the official manifest (Adspirer, SearchFit, Product Tracking) remain live in Cowork and were re-tagged Cowork-only rather than dropped. Listed under Legal below.

---

## Contents

- [How to install](#how-to-install)
- [AI Development and Agents](#ai-development-and-agents)
- [Browser Automation](#browser-automation)
- [Business Operations](#business-operations)
- [Cloud and Infrastructure](#cloud-and-infrastructure)
- [Code Quality and Review](#code-quality-and-review)
- [Communication and Messaging](#communication-and-messaging)
- [CRM and Sales](#crm-and-sales)
- [Customer Support](#customer-support)
- [Data and Databases](#data-and-databases)
- [Design and Creative](#design-and-creative)
- [Developer Workflows](#developer-workflows)
- [Documentation](#documentation)
- [Education and Learning](#education-and-learning)
- [Engineering and Product](#engineering-and-product)
- [Finance and Accounting](#finance-and-accounting)
- [Healthcare and Life Sciences](#healthcare-and-life-sciences)
- [Human Resources](#human-resources)
- [Language Servers](#language-servers)
- [Legal](#legal)
- [Marketing and Web](#marketing-and-web)
- [Observability and Monitoring](#observability-and-monitoring)
- [Output Styles](#output-styles)
- [Payments and Billing](#payments-and-billing)
- [Platforms and SaaS](#platforms-and-saas)
- [Productivity and Documents](#productivity-and-documents)
- [Project Management](#project-management)
- [Security](#security)
- [Skills Authoring](#skills-authoring)
- [Custom Plugins](#custom-plugins)
- [Plugin Marketplaces](#plugin-marketplaces)
- [Related](#related)

---

## How to install

Inside Claude Code, type `/plugin` to open the Plugin Manager. The official Anthropic marketplace (`claude-plugins-official`) is auto-installed on startup, so most plugins below are one command away:

```
/plugin install <plugin-name>@claude-plugins-official
```

For plugins from other marketplaces, add the marketplace first:

```
/plugin marketplace add owner/repo
/plugin install <plugin-name>
```

To load a plugin from a local directory or remote `.zip` (for one-off testing or private builds):

```
claude --plugin-dir /path/to/plugin
claude --plugin-url https://example.com/plugin.zip
```

In Cowork, plugins appear in the workspace's plugin manager — connect the marketplace once per workspace and enable plugins per project.

## AI Development and Agents

{{ENTRIES:AI Development and Agents}}

## Browser Automation

{{ENTRIES:Browser Automation}}

## Business Operations

{{ENTRIES:Business Operations}}

## Cloud and Infrastructure

{{ENTRIES:Cloud and Infrastructure}}

## Code Quality and Review

{{ENTRIES:Code Quality and Review}}

## Communication and Messaging

{{ENTRIES:Communication and Messaging}}

## CRM and Sales

{{ENTRIES:CRM and Sales}}

## Customer Support

{{ENTRIES:Customer Support}}

## Data and Databases

{{ENTRIES:Data and Databases}}

## Design and Creative

{{ENTRIES:Design and Creative}}

## Developer Workflows

{{ENTRIES:Developer Workflows}}

## Documentation

{{ENTRIES:Documentation}}

## Education and Learning

{{ENTRIES:Education and Learning}}

## Engineering and Product

{{ENTRIES:Engineering and Product}}

## Finance and Accounting

{{ENTRIES:Finance and Accounting}}

## Healthcare and Life Sciences

{{ENTRIES:Healthcare and Life Sciences}}

## Human Resources

{{ENTRIES:Human Resources}}

## Language Servers

{{ENTRIES:Language Servers}}

## Legal

{{ENTRIES:Legal}}

## Marketing and Web

{{ENTRIES:Marketing and Web}}

## Observability and Monitoring

{{ENTRIES:Observability and Monitoring}}

## Output Styles

{{ENTRIES:Output Styles}}

## Payments and Billing

{{ENTRIES:Payments and Billing}}

## Platforms and SaaS

{{ENTRIES:Platforms and SaaS}}

## Productivity and Documents

{{ENTRIES:Productivity and Documents}}

## Project Management

{{ENTRIES:Project Management}}

## Security

{{ENTRIES:Security}}

## Skills Authoring

{{ENTRIES:Skills Authoring}}

## Custom Plugins

You can install plugins outside the official directory. Custom plugins are not reviewed by Anthropic — install only from sources you trust.

**From a local directory:** `claude --plugin-dir /path/to/plugin` loads a plugin in the current session.

**From a URL:** `claude --plugin-url https://example.com/plugin.zip` fetches and loads a plugin archive.

**From a Git repo:** `/plugin marketplace add owner/repo` followed by `/plugin install <name>` installs via a personal marketplace.

**From a private marketplace:** configure required marketplaces in your repository's `.claude/settings.json` for team-wide plugin distribution.

For complete authoring guidance, see the Plugin Developer Toolkit entry in the Skills Authoring section above, or the Plugins overview linked in the header.

## Plugin Marketplaces

A plugin marketplace is a Git repo or URL hosting `.claude-plugin/marketplace.json` that catalogs available plugins. Anyone can run one. Notable marketplaces:

- [claude-plugins-official](https://github.com/anthropics/claude-plugins-public#readme) - Anthropic's curated, vetted marketplace, auto-installed on Claude Code startup. *Use case: First-stop discovery; install with `/plugin install <name>@claude-plugins-official`.*
- [claude-code-plugins (Anthropic demo)](https://github.com/anthropics/claude-code) - Anthropic's example marketplace of reference plugins demonstrating the plugin system. *Use case: Plugin format examples, integration patterns; install with `/plugin marketplace add anthropics/claude-code`.*
- [NotFair](https://github.com/nowork-studio/NotFair) - Open-source SEO, GEO, Google Ads, and Meta Ads skills for Claude Code (18 skills, MIT). *Install with `/plugin marketplace add nowork-studio/NotFair`.*
- [Seth Hobson's sub-agents](https://github.com/wshobson/agents) - 80+ specialized sub-agents packaged as a plugin collection.
- [ClaudePluginHub](https://www.claudepluginhub.com) - Community-maintained third-party plugin discovery hub indexing marketplaces and individual plugins outside the official directory.

## Related

- [awesome-claude-connectors](https://github.com/rdmgator12/awesome-claude-connectors) - Anthropic Claude connectors directory (841 entries) — the MCP-server layer that plugins often bundle.
- [awesome-grok-connectors](https://github.com/rdmgator12/awesome-grok-connectors) - xAI Grok connectors directory.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Community-maintained directory of MCP servers across all clients.
- [awesome-perplexity-connectors](https://github.com/rdmgator12/Perplexity-Connectors-awesome-list-) - Perplexity AI connectors directory.
- [awesome-mistral-connectors](https://github.com/rdmgator12/awesome-mistral-connectors) - Mistral Le Chat connectors directory.
- [awesome-lm-studio-connectors](https://github.com/rdmgator12/awesome-lm-studio-connectors) - LM Studio plugins and integrations directory.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps) - OpenAI ChatGPT apps and connectors directory.
- [awesome-gemini-extensions](https://github.com/rdmgator12/Gemini-Awesome-List-) - Google Gemini CLI extensions directory.
- [awesome-lovable-connectors](https://github.com/rdmgator12/awesome-lovable-connectors) - Lovable platform connectors directory.
- [awesome-healthcare-mcp-servers](https://github.com/rdmgator12/awesome-healthcare-mcp-servers) - Healthcare-focused MCP servers directory.

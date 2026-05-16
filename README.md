# Awesome List for Claude Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A directory of plugins in Anthropic's official [Claude Plugins catalog](https://claude.com/plugins/) — installable bundles of skills, MCP servers, slash commands, sub-agents, and hooks that extend Claude Code and Cowork with one-command installation.

**Last updated:** May 16, 2026 | **Total plugins:** 140+ | **Surfaces:** Claude Code · Cowork | **Categories:** 25+

Plugins originated in Claude Code (October 2025) as packaged, versioned, shareable directories that bundle skills, MCP server references, slash commands, sub-agents, hooks, and LSP servers into a single installable unit. As of v2.1.129 (May 6, 2026), Anthropic runs the **Official Claude Plugins Directory** (`claude-plugins-official`) — a curated, vetted catalog auto-installed on Claude Code startup. Plugins also extend **Cowork**, Anthropic's agentic workspace, with role-class workflow bundles (Productivity, Design, Marketing, etc.) used by knowledge workers inside isolated VM environments.

For more information, see the [Plugins overview](https://claude.com/docs/plugins/overview), [plugin marketplaces guide](https://code.claude.com/docs/en/plugin-marketplaces), [submission form](https://claude.com/plugins#submit), and the [official Anthropic marketplace repo](https://github.com/anthropics/claude-plugins-public).

Plugins marked with **`A`** are built and verified by Anthropic. Each entry ends with a surface tag: `(Claude Code)`, `(Cowork)`, or `(Claude Code, Cowork)`.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> This is an independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC. "Claude" and related marks are the property of Anthropic PBC. Each plugin is the property of its respective owner.

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
> - **Plugin Marketplace** is a git repo or URL hosting `.claude-plugin/marketplace.json` that catalogs plugins. The official Anthropic marketplace (`claude-plugins-official`) is auto-installed on Claude Code startup.
> - **Custom Plugin** is a plugin you build and install from a local directory, your own git repo, or a private marketplace. Same components as directory plugins; no Anthropic review. Install via `/plugin install`, `--plugin-dir`, or `--plugin-url`.
>
> Mental model: **Connector** = "Claude can call your API" (tool surface). **Plugin** = "Claude knows how to use your product" (workflow + tools + skills). **MCP** = the protocol both speak. Most partners ship both — a remote MCP server (connector) and a plugin that wraps it with skills and slash commands.

> [!TIP]
> ### Plugin of the Week — May 16, 2026
>
> **[Frontend Design](https://claude.com/plugins/frontend-design)** · *Design and Creative* · **`A`**
>
> The most-installed third-party-ready plugin built by Anthropic for Claude Code (732K+ installs and climbing). Frontend Design isn't a tool wrapper — it's a *taste cartridge*. The skill ships with a curated design vocabulary that pushes generated frontends past the generic-AI-aesthetic floor: real type hierarchies, intentional spacing, distinctive component composition. For builders who use Claude Code to ship Lovable, Vercel, or Next.js apps and have noticed how default LLM frontends all converge to the same shadcn-flavored beige, this plugin is the antidote. Composes naturally with the `impeccable`, `critique`, `polish`, and `delight` skills if you're running a multi-pass design workflow. The deeper signal: with 700K+ installs, Frontend Design demonstrates that *skill-bundles-as-product* — not MCP servers, not slash commands, but curated design taste — is now a distribution category. The plugin format is doing the same thing for AI design that npm packages did for utility libraries.

---

## Contents

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

## AI Development and Agents

- [Agent SDK Dev](https://claude.com/plugins#agent-sdk-dev) **`A`** - Development kit for working with the Claude Agent SDK. *Use case: Scaffolding agents, validating SDK usage, testing agent workflows locally.* (Claude Code)
- [atomic-agents](https://github.com/BrainBlend-AI/atomic-agents) - Build AI agents with the Atomic Agents framework. *Use case: Multi-agent system development, best-practice validation, agent tool orchestration.* (Claude Code)
- [GoodMem](https://goodmem.ai) - AI memory infrastructure with Python SDK and MCP tools for managing embedders, spaces, and memories. *Use case: Long-term agent memory, semantic memory recall, embedding management via chat.* (Claude Code)
- [Hugging Face Skills](https://huggingface.co) - Build, train, evaluate, and use open source AI models, datasets, and Spaces from Hugging Face. *Use case: Model exploration, dataset selection, running inference on hosted models.* (Claude Code)
- [Remember](https://claude.com/plugins#remember) - Continuous memory for Claude Code that extracts, summarizes, and compresses conversations into tiered daily logs. *Use case: Long-running project memory, daily session continuity, conversation archival.* (Claude Code)


## Browser Automation

- [Chrome DevTools](https://developer.chrome.com/docs/devtools) - Control and inspect a live Chrome browser from your coding agent, record performance traces, and analyze network requests. *Use case: Web app debugging, performance profiling, network capture for reproduction cases.* (Claude Code)
- [Playwright](https://playwright.dev) - Browser automation and end-to-end testing MCP server by Microsoft. *Use case: E2E test authoring, web scraping with form interaction, screenshot-based visual regression, headless workflow automation.* (Claude Code)


## Business Operations

- [Enterprise Search](https://claude.com/plugins#enterprise-search) **`A`** - Search across all of your company's tools in one place — email, chat, documents, and wikis without switching between apps. *Use case: Cross-tool knowledge retrieval, finding decisions across Slack/email/Drive, answering "where did we discuss X" questions.* (Cowork)
- [Operations](https://claude.com/plugins#operations) **`A`** - Optimize business operations including vendor management, process documentation, change management, capacity planning, and compliance tracking. *Use case: Vendor onboarding, SOP authoring, ops dashboards, audit prep.* (Cowork)
- [Small Business](https://claude.com/plugins#small-business) **`A`** - Pre-built small business workflows including payroll planning, month-end close, weekly briefs, and growth campaigns using QuickBooks, PayPal, HubSpot, and related tools. *Use case: Solo founder ops, bookkeeping triage, weekly business reviews, growth-campaign coordination.* (Cowork)


## Cloud and Infrastructure

- [AWS Serverless](https://aws.amazon.com/serverless) - Design, build, deploy, test, and debug serverless applications using AWS Lambda, API Gateway, DynamoDB, and related services. *Use case: Lambda authoring, SAM template generation, serverless local testing.* (Claude Code)
- [cloudflare](https://www.cloudflare.com) - Skills for the Cloudflare developer platform covering Workers, Durable Objects, Agents SDK, MCP servers, Wrangler CLI, and Worker testing. *Use case: Edge function development, Durable Object design, Workers deployment, Cloudflare-hosted MCP servers.* (Claude Code)
- [Deploy on AWS](https://aws.amazon.com) - Deploy applications to AWS with architecture recommendations, cost estimates, and infrastructure-as-code deployment. *Use case: Greenfield AWS deployments, architecture review, cost-aware service selection.* (Claude Code)
- [Firebase](https://firebase.google.com) - MCP integration for managing Firestore, authentication, Functions, hosting, and storage. *Use case: Mobile-backend operations, real-time database management, Firebase rules editing.* (Claude Code)
- [Netlify Skills](https://www.netlify.com) - Netlify platform skills for functions, edge functions, blobs, database, image CDN, forms, config, and CLI workflows. *Use case: JAMstack deployment, edge function development, Netlify forms and config tuning.* (Claude Code)
- [Railway](https://railway.app) - Deploy and manage apps, databases, and infrastructure on Railway covering project setup, deploys, and environment configuration. *Use case: Quick app deploys, database provisioning, env-var management.* (Claude Code)
- [terraform](https://www.terraform.io) - MCP server for advanced infrastructure-as-code automation and Terraform-ecosystem integration. *Use case: HCL authoring, state-file inspection, provider exploration.* (Claude Code)
- [Vercel](https://vercel.com) - Integration to manage deployments, builds, logs, domains, and frontend infrastructure. *Use case: Next.js deployment workflows, build-log triage, domain configuration, edge function management.* (Claude Code)
- [Wix](https://www.wix.com) - Build, manage, and deploy Wix sites and apps with CLI skills for dashboard extensions, backend APIs, and site widgets. *Use case: Wix custom-app development, dashboard extension authoring, widget shipping.* (Claude Code)


## Code Quality and Review

- [Aikido Security](https://www.aikido.dev) - Security scanning for SAST, secrets, and IaC vulnerability detection via Aikido MCP server. *Use case: Pre-commit security scan, secrets-leak detection, IaC misconfiguration triage.* (Claude Code)
- [Code Review](https://claude.com/plugins#code-review) **`A`** - AI code review with specialized agents and confidence-based filtering for pull requests. *Use case: PR review automation, multi-agent code analysis, confidence-weighted feedback.* (Claude Code)
- [Code Simplifier](https://claude.com/plugins#code-simplifier) **`A`** - Code clarity agent that simplifies and refines recently modified code while preserving functionality and consistency. *Use case: Post-edit cleanup, complexity reduction, dead-code elimination after refactors.* (Claude Code)
- [CodeRabbit](https://www.coderabbit.ai) - AI code review with 40+ analyzers, AST parsing, security checks, and auto-integrated project guidelines. *Use case: PR review with deep linting, security-aware diff analysis, project-guideline enforcement.* (Claude Code)
- [Greptile](https://www.greptile.com) - AI-powered codebase search to query repositories in natural language to find code, understand dependencies, and explore architecture. *Use case: Cross-repo code search, dependency tracing, architecture discovery in unfamiliar codebases.* (Claude Code)
- [Optibot Code Review](https://www.optibot.dev) - AI code review that catches production bugs, business-logic issues, and security vulnerabilities. *Use case: Pre-merge production-bug detection, business-logic regression hunting, security pass on diffs.* (Claude Code)
- [PR Review Toolkit](https://claude.com/plugins#pr-review-toolkit) **`A`** - PR review agents for comments, tests, errors, types, quality, and simplification. *Use case: Multi-axis PR review, test-coverage check, type-correctness validation in pull requests.* (Claude Code)
- [Qodo Skills](https://www.qodo.ai) - AI agents that integrate code quality, testing, security, and compliance checks into your SDLC. *Use case: Test generation, code-quality gates, compliance scanning in CI.* (Claude Code)
- [session-report](https://claude.com/plugins#session-report) **`A`** - Generate an explorable HTML report of Claude Code session usage including tokens, cache efficiency, subagents, skills, and tool calls. *Use case: Session retrospection, cache-hit analysis, subagent usage audit.* (Claude Code)
- [sonarqube](https://www.sonarsource.com/products/sonarqube) - Automatically enforce SonarQube code quality and security in the agent coding loop. *Use case: Quality-gate enforcement, SAST scanning, code-smell detection inline with edits.* (Claude Code)
- [Sourcegraph](https://sourcegraph.com) - Search code across codebases, trace references, analyze refactor impact, investigate incidents, and run security sweeps. *Use case: Cross-repo refactor planning, incident investigation, security sweep on call paths.* (Claude Code)


## Communication and Messaging

- [Circleback](https://circleback.ai) - Conversational-context integration for searching and accessing meetings, emails, and calendar events. *Use case: Pulling meeting context into current work, finding action items from past calls.* (Claude Code)
- [discord](https://discord.com) - Messaging bridge with built-in access control, pairing, allowlists, and policy management. *Use case: Discord server moderation from Claude, allowlisted Discord posting, policy-controlled bot workflows.* (Claude Code)
- [fakechat](https://claude.com/plugins#fakechat) - Localhost web chat for testing channel notification flows with no tokens, access control, or third-party services. *Use case: Local notification testing, channel-integration development without external dependencies.* (Claude Code)
- [iMessage](https://claude.com/plugins#imessage) - Messaging bridge with built-in access control that reads chat.db directly and sends via AppleScript. *Use case: macOS-only iMessage automation, allowlisted texting workflows, message-history search.* (Claude Code)
- [Slack](https://slack.com) **`A`** - Official Slack MCP server for interactive and collaborative workflows including surfacing insights, drafting messages, and engaging teams from Claude Cowork. *Use case: Slack-message drafting, channel-thread summarization, async standups, in-Slack analysis.* (Claude Code, Cowork)
- [telegram](https://telegram.org) - Messaging bridge with built-in access control, pairing, and policy management. *Use case: Telegram bot workflows, allowlisted messaging, channel automation.* (Claude Code)
- [Zoom](https://zoom.us) - Plan, build, and debug Zoom integrations across REST APIs, Meeting SDK, Video SDK, webhooks, bots, and MCP workflows. *Use case: Zoom app development, meeting recording retrieval, transcript access, AI-powered Zoom experiences.* (Claude Code, Cowork)


## CRM and Sales

- [Apollo](https://www.apollo.io) - Prospect, enrich leads, and load outreach sequences with Apollo.io. *Use case: B2B prospect discovery, lead enrichment from chat, outreach-sequence loading.* (Cowork)
- [Common Room](https://www.commonroom.io) - Turn Common Room into your GTM copilot — research accounts and contacts, prep for calls, and draft personalized outreach across email, LinkedIn, and phone. *Use case: Call prep, account research, multi-channel outreach drafting.* (Cowork)
- [Sales](https://claude.com/plugins#sales) **`A`** - Prospect, craft outreach, build deal strategy, prep for calls, manage pipeline, and write personalized messaging. *Use case: Pipeline management, prospect research, personalized cold outreach.* (Cowork)
- [ZoomInfo](https://www.zoominfo.com) - Search companies and contacts, enrich leads, find lookalikes, and get AI-ranked contact recommendations with pre-built B2B sales workflows. *Use case: B2B prospect enrichment, lookalike-account discovery, AI-ranked contact targeting.* (Cowork)


## Customer Support

- [Customer Support](https://claude.com/plugins#customer-support) **`A`** - Triage tickets, draft responses, escalate issues, build knowledge base, research customer context, and turn resolved issues into self-service content. *Use case: Support-ticket triage, response drafting, knowledge-base content generation.* (Cowork)
- [Intercom](https://www.intercom.com) - Integration to search conversations, analyze customer support patterns, and look up contacts and companies. *Use case: Customer-conversation analytics, support-pattern detection, real-time customer-data lookup.* (Claude Code, Cowork)


## Data and Databases

- [Atlan](https://atlan.com) - Data catalog plugin with semantic search, lineage traversal, glossary management, and data-quality rules via the Atlan MCP server. *Use case: Data discovery, lineage exploration, glossary management, data-quality rule authoring.* (Cowork)
- [Bigdata.com](https://bigdata.com) - Official Bigdata.com plugin providing financial research, analytics, and intelligence tools powered by the Bigdata MCP. *Use case: Equity research, financial-data analytics, market intelligence queries.* (Cowork)
- [CockroachDB](https://www.cockroachlabs.com) - Distributed SQL plugin to explore schemas, write optimized SQL, debug queries, and manage distributed database clusters. *Use case: Distributed SQL development, query plan analysis, multi-region schema design.* (Cowork)
- [Daloopa](https://daloopa.com) - Financial analysis skills powered by Daloopa's institutional-grade data. *Use case: Equity research with structured financials, model-building from validated data, earnings-quality analysis.* (Cowork)
- [Data](https://claude.com/plugins#data-cowork) **`A`** - Write SQL, explore datasets, generate insights, build visualizations and dashboards, and turn raw data into clear stories. *Use case: Ad-hoc SQL, dashboard authoring, stakeholder-facing data storytelling.* (Claude Code, Cowork)
- [Data Engineering](https://claude.com/plugins#data-engineering) - Warehouse and pipeline workflows covering warehouse exploration, pipeline authoring, and Airflow integration. *Use case: ETL development, warehouse schema exploration, Airflow DAG authoring.* (Claude Code)
- [LSEG](https://www.lseg.com) - Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build macro dashboards using LSEG financial data and analytics. *Use case: Fixed-income analysis, FX strategy work, options valuation, macro-research dashboards.* (Cowork)
- [mongodb](https://www.mongodb.com) - Official MongoDB plugin with MCP server and skills for connecting, exploring data, managing collections, and optimizing queries. *Use case: MongoDB query authoring, schema design, aggregation-pipeline optimization.* (Claude Code)
- [Pinecone](https://www.pinecone.io) - Vector database integration for managing indexes, querying, and rapid prototyping. *Use case: Vector-search prototyping, RAG pipeline development, index management.* (Claude Code)
- [PlanetScale](https://planetscale.com) - Authenticated hosted MCP server for PlanetScale organizations, databases, branches, schema, and Insights. *Use case: Database branching, slow-query analysis, schema migration on serverless MySQL/Postgres.* (Claude Code, Cowork)
- [Prisma](https://www.prisma.io) - MCP integration for Postgres database management, schema migrations, SQL queries, and connection string management. *Use case: Prisma schema authoring, migration generation, Postgres data interaction.* (Claude Code, Cowork)
- [S&P Global](https://www.spglobal.com) - Financial data and analytics including company tearsheets, earnings previews, and transaction summaries via Kensho. *Use case: Equity tear-sheet generation, earnings-preview drafting, M&A transaction analysis.* (Cowork)
- [Supabase](https://supabase.com) - MCP integration for database operations, authentication, storage, and real-time features. *Use case: Postgres backend management, auth flow development, real-time subscription debugging.* (Claude Code)


## Design and Creative

- [Adobe for Creativity](https://www.adobe.com/creativecloud.html) - Adobe Creative Cloud tools for images, vectors, design, and video covering Photoshop, Illustrator, Premiere, and Express. *Use case: Multi-asset editing, platform-adapted exports, multi-step creative workflows from chat.* (Cowork)
- [Brand Voice](https://www.tribe.ai) - Discover your brand voice from existing documents and conversations, generate enforceable guidelines, and validate AI-generated content. *Use case: Brand-voice extraction, content validation against tone, guideline authoring.* (Cowork)
- [Cloudinary](https://cloudinary.com) - Integration to manage assets, apply transformations, and optimize media through natural conversation. *Use case: Image-transformation development, video-optimization pipelines, asset library management.* (Cowork)
- [Design](https://claude.com/plugins#design) **`A`** - Accelerate design workflows including critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. *Use case: Design critique, design-system component authoring, accessibility audit, design-to-dev handoff specs.* (Cowork)
- [Figma](https://www.figma.com) - Design platform integration to access design files, extract component information, read design tokens, and translate designs into code. *Use case: Design-token export, component-to-code translation, design-file inspection from dev workflow.* (Claude Code, Cowork)
- [Frontend Design](https://claude.com/plugins#frontend-design) **`A`** - Craft production-grade frontends with distinctive design that avoids generic AI aesthetics. *Use case: Landing-page design, app-shell composition, distinctive component design, anti-shadcn-default polish.* (Claude Code)
- [Miro](https://miro.com) - Secure access to Miro boards to read board context, create diagrams, and generate code with enterprise-grade security. *Use case: Whiteboard-to-code workflows, architecture-diagram authoring, board-context retrieval.* (Cowork)
- [Playground](https://claude.com/plugins#playground) **`A`** - Interactive HTML playgrounds with visual controls, live preview, and prompt output including design, data, concept map, and critique templates. *Use case: Live design iteration, prompt-output visualization, concept-map authoring, in-chat critique surfaces.* (Claude Code)
- [Sanity](https://www.sanity.io) - Content platform integration with MCP server, agent skills, and slash commands for content authoring, GROQ query building, schema design, and Visual Editing. *Use case: GROQ query optimization, schema design, Visual Editing setup, structured-content authoring.* (Cowork)


## Developer Workflows

- [CLAUDE.md Management](https://claude.com/plugins#claude-md-management) **`A`** - Maintain CLAUDE.md by auditing quality, capturing learnings, and keeping project memory current. *Use case: CLAUDE.md hygiene, learning capture, project-memory refresh after major changes.* (Claude Code)
- [Claude Code Setup](https://claude.com/plugins#claude-code-setup) **`A`** - Analyze codebases and recommend tailored Claude Code automations including hooks, skills, MCP servers, and subagents. *Use case: First-time Claude Code setup on an unfamiliar repo, automation discovery, configuration audit.* (Claude Code)
- [Commit Commands](https://claude.com/plugins#commit-commands) **`A`** - Commands for git commit workflows including commit, push, and PR creation. *Use case: Commit-message generation, PR creation, conventional-commit enforcement.* (Claude Code)
- [Feature Dev](https://claude.com/plugins#feature-dev) **`A`** - Feature development workflow with agents for exploration, design, and review. *Use case: New-feature scoping, multi-phase development workflow, design-then-review cadence.* (Claude Code)
- [Hookify](https://claude.com/plugins#hookify) **`A`** - Create custom hooks via markdown to prevent unwanted behaviors from conversation patterns or explicit instructions. *Use case: Behavioral guardrail authoring, custom Stop hooks, pattern-based hook generation.* (Claude Code)
- [Ralph Loop](https://claude.com/plugins#ralph-loop) **`A`** - Interactive AI loops for iterative development using the Ralph Wiggum technique where Claude works on tasks repeatedly until completion. *Use case: Stubborn-task iteration, /loop-driven development, autonomous task completion.* (Claude Code)
- [Superpowers](https://github.com/superpowers-org/superpowers) - Brainstorming, subagent development with code review, debugging, TDD, and skill authoring. *Use case: Broad-spectrum developer enhancement, TDD workflow, skill-authoring scaffolds.* (Claude Code)


## Documentation

- [Context7](https://context7.com) - Upstash Context7 MCP server for live documentation lookup that pulls version-specific docs and code examples from source repos. *Use case: Version-correct library lookups, current-API documentation in context, eliminating training-data drift on fast-moving libraries.* (Claude Code)
- [Microsoft Docs](https://learn.microsoft.com) - Access official Microsoft documentation, API references, and code samples for Azure, .NET, Windows, and more. *Use case: Azure SDK lookup, .NET API reference, Windows-specific implementation patterns.* (Claude Code)
- [mintlify](https://mintlify.com) - Build documentation with Mintlify covering MDX conversion, content modification, and automated updates. *Use case: Docs migration to Mintlify, automated docs-as-code workflows, MDX authoring.* (Claude Code)
- [shopify-ai-toolkit](https://shopify.dev) - Shopify's AI Toolkit with 18 development skills for building on the Shopify platform including documentation search, theme development, and app development. *Use case: Shopify theme work, Shopify app development, Liquid-template authoring.* (Claude Code)


## Engineering and Product

- [Engineering](https://claude.com/plugins#engineering) **`A`** - Streamline engineering workflows including standups, code review, architecture decisions, incident response, and technical documentation. *Use case: Engineering standups, architecture-decision documentation, incident post-mortems.* (Cowork)
- [Product Management](https://claude.com/plugins#product-management) **`A`** - Write feature specs, plan roadmaps, synthesize user research, keep stakeholders updated, and stay ahead of competitive landscape. *Use case: Spec authoring, roadmap planning, research synthesis, competitive monitoring.* (Cowork)
- [Product Tracking Skills](https://accoil.com) - AI agent skills that make SaaS products data-ready by scanning codebases, building tracking plans, and generating instrumentation code. *Use case: Product-analytics instrumentation, tracking-plan generation, event-schema design.* (Claude Code, Cowork)


## Finance and Accounting

- [Finance](https://claude.com/plugins#finance) **`A`** - Streamline finance and accounting workflows from journal entries and reconciliation to financial statements, variance analysis, audit prep, and month-end close. *Use case: Month-end close, variance analysis, audit prep, journal-entry triage.* (Cowork)


## Healthcare and Life Sciences

- [Bio Research](https://claude.com/plugins#bio-research) **`A`** - Connect to preclinical research tools and databases including literature search, genomics analysis, and target prioritization. *Use case: Early-stage life sciences R&D, target discovery, preclinical literature synthesis.* (Cowork)


## Human Resources

- [Human Resources](https://claude.com/plugins#human-resources) **`A`** - Streamline people operations including recruiting, onboarding, performance reviews, compensation analysis, and policy guidance. *Use case: Recruiting workflows, performance-review drafting, compensation benchmarking, HR-policy lookups.* (Cowork)


## Language Servers

- [C# LSP](https://claude.com/plugins#csharp-lsp) **`A`** - C# language server for code intelligence. *Use case: C#/.NET autocomplete, type checking, refactoring support inside Claude Code.* (Claude Code)
- [Clangd LSP](https://claude.com/plugins#clangd-lsp) **`A`** - C/C++ language server (clangd) for code intelligence. *Use case: C/C++ autocomplete, diagnostics, cross-reference navigation.* (Claude Code)
- [Elixir LS](https://claude.com/plugins#elixir-ls) - ElixirLS code intelligence and diagnostics for .ex, .exs, and .heex files. *Use case: Elixir/Phoenix development, HEEx template editing.* (Claude Code)
- [Go LSP (gopls)](https://claude.com/plugins#go-lsp) **`A`** - Go language server for code intelligence and refactoring. *Use case: Go autocomplete, refactor-rename support, package navigation.* (Claude Code)
- [Java LSP (Eclipse JDT.LS)](https://claude.com/plugins#java-lsp) **`A`** - Java language server (Eclipse JDT.LS) for code intelligence. *Use case: Java autocomplete, type checking, JDT-powered refactoring.* (Claude Code)
- [Kotlin LSP](https://claude.com/plugins#kotlin-lsp) **`A`** - Kotlin language server for code intelligence. *Use case: Kotlin autocomplete, Android development, multiplatform Kotlin work.* (Claude Code)
- [Lua LSP](https://claude.com/plugins#lua-lsp) **`A`** - Lua language server for code intelligence. *Use case: Lua scripting, Neovim configuration, game-engine Lua editing.* (Claude Code)
- [PHP LSP](https://claude.com/plugins#php-lsp) **`A`** - PHP language server (Intelephense) for code intelligence. *Use case: PHP autocomplete, Laravel/Symfony development, type-inference assistance.* (Claude Code)
- [Pyright LSP](https://claude.com/plugins#pyright-lsp) **`A`** - Python language server (Pyright) for type checking and code intelligence. *Use case: Python type checking, autocomplete, strict-mode type inference.* (Claude Code)
- [Ruby LSP](https://claude.com/plugins#ruby-lsp) **`A`** - Ruby language server for code intelligence and analysis. *Use case: Ruby/Rails autocomplete, diagnostic feedback, refactor support.* (Claude Code)
- [Rust Analyzer LSP](https://claude.com/plugins#rust-analyzer-lsp) **`A`** - Rust language server for code intelligence and analysis. *Use case: Rust autocomplete, type inference, refactor-rename support.* (Claude Code)
- [Serena](https://github.com/oraios/serena) - Semantic code analysis MCP server for intelligent code understanding, refactoring, and navigation via language server protocol. *Use case: Cross-language semantic code search, intelligent refactoring, deep code understanding.* (Claude Code)
- [Swift LSP](https://claude.com/plugins#swift-lsp) **`A`** - Swift language server (SourceKit-LSP) for code intelligence. *Use case: Swift/iOS development, SwiftUI autocomplete, Apple-platform code intelligence.* (Claude Code)
- [TypeScript LSP](https://claude.com/plugins#typescript-lsp) **`A`** - TypeScript/JavaScript language server for enhanced code intelligence. *Use case: TS/JS autocomplete, type inference, refactor-rename across files.* (Claude Code)


## Legal

- [Legal](https://claude.com/plugins#legal) **`A`** - Speed up contract review, NDA triage, and compliance workflows for in-house legal teams including legal-brief drafting and precedent research. *Use case: Contract redlining, NDA triage, precedent research, compliance-workflow drafting.* (Cowork)
- [LegalZoom](https://www.legalzoom.com) - AI reviews legal documents for risks and advises when to hire an attorney, with connections to legal professionals. *Use case: Initial legal-document risk review, escalation triggers for human-attorney involvement.* (Claude Code)


## Marketing and Web

- [Adspirer Ads Agent](https://www.adspirer.com) - Cross-platform ad management for Google Ads, Meta Ads, TikTok Ads, and LinkedIn Ads with 91 tools for keyword research, campaign creation, and optimization. *Use case: Cross-platform ad campaign authoring, keyword research, budget optimization across ad networks.* (Claude Code, Cowork)
- [Bright Data](https://brightdata.com) - Web scraping, Google search, structured data extraction, and 60+ MCP tools covering Web Unlocker, SERP API, Web Scraper API, and Browser API. *Use case: Scraping bot-protected sites, structured Google SERP results, large-scale data extraction.* (Cowork)
- [Firecrawl](https://www.firecrawl.dev) - Convert websites to LLM-ready markdown or data with scraping, crawling, and structured extraction. *Use case: RAG-corpus building, structured site extraction, AI-friendly web data preparation.* (Claude Code)
- [Marketing](https://claude.com/plugins#marketing) **`A`** - Create content, plan campaigns, and analyze performance across marketing channels with brand-voice consistency and competitor tracking. *Use case: Content authoring, campaign planning, brand-voice enforcement, competitor monitoring.* (Cowork)
- [Nimble](https://nimbleway.com) - Web data toolkit for search, extract, map, crawl, and structured data agents. *Use case: Structured web data harvesting, SERP extraction, site mapping for crawl-aware AI agents.* (Cowork)
- [Postiz](https://postiz.com) - Social media automation CLI for scheduling posts, managing integrations, uploading media, and tracking analytics across 28+ platforms. *Use case: Cross-platform social scheduling, content distribution, analytics rollups for marketers.* (Claude Code, Cowork)
- [SearchFit SEO](https://searchfit.ai) - AI-powered SEO toolkit for auditing websites, planning content strategy, optimizing pages, generating schema markup, and tracking AI visibility. *Use case: SEO audit on any site, content-cluster planning, schema-markup generation, AI-search visibility tracking.* (Claude Code, Cowork)


## Observability and Monitoring

- [PagerDuty Pre-Commit Risk Score](https://www.pagerduty.com) - Score pre-commit diffs against PagerDuty incident history to surface deployment risk before shipping. *Use case: Risk-aware commit gating, incident-history-informed code review, pre-deploy safety checks.* (Claude Code)
- [PostHog](https://posthog.com) - Connect to PostHog to query analytics, manage flags, run A/B tests, track errors, and analyze LLM costs via natural language. *Use case: Product-analytics queries, feature-flag management, A/B test analysis, LLM cost tracking.* (Claude Code)
- [Sentry](https://sentry.io) - Error monitoring to access error reports, analyze stack traces, search issues, and debug production errors. *Use case: Production-error triage, stack-trace analysis, issue prioritization from chat.* (Claude Code)


## Output Styles

- [Explanatory Output Style](https://claude.com/plugins#explanatory-output-style) **`A`** - Adds educational insights on implementation choices and codebase patterns to mimic the deprecated Explanatory style. *Use case: Learning-mode coding, teaching-team-members workflow, explanatory commenting style.* (Claude Code)
- [Learning Output Style](https://claude.com/plugins#learning-output-style) **`A`** - Interactive learning mode that requests meaningful code contributions at key decision points. *Use case: Pair-programming-style learning, deliberate-practice coding, junior-developer ramp.* (Claude Code)


## Payments and Billing

- [RevenueCat](https://www.revenuecat.com) - Manage RevenueCat in-app purchase backend directly from your development workflow. *Use case: Subscription product configuration, entitlement management, IAP backend tuning.* (Claude Code)
- [Stripe](https://stripe.com) - Development plugin for payments, billing, subscriptions, and Stripe API integration. *Use case: Stripe API exploration, payment-flow development, subscription-product configuration.* (Claude Code)


## Platforms and SaaS

- [Amazon Location Service](https://aws.amazon.com/location) - Integrate Amazon Location Service for maps, geocoding, routing, and geospatial features with authentication and SDKs. *Use case: Maps integration in apps, geocoding flows, routing/directions APIs.* (Claude Code)
- [Box](https://www.box.com) - Search files, organize folders, collaborate with teams, and use Box AI to answer questions, summarize documents, and extract data. *Use case: Enterprise file management, Box AI document Q&A, folder organization automation.* (Claude Code, Cowork)
- [expo](https://expo.dev) - Official Expo skills for building, deploying, upgrading, and debugging React Native apps with Expo. *Use case: Expo app development, EAS build configuration, React Native debugging.* (Claude Code)
- [Fastly Agent Toolkit](https://www.fastly.com) - Fastly development tools and platform skills for VCL, edge functions, and CDN configuration. *Use case: Fastly edge function development, VCL authoring, CDN configuration.* (Claude Code, Cowork)
- [Laravel Boost](https://laravel.com) - Laravel MCP server for intelligent Artisan commands, Eloquent queries, routing, migrations, and framework-specific code generation. *Use case: Laravel app development, Eloquent query authoring, Artisan command exploration.* (Claude Code)
- [postman](https://www.postman.com) - Full API lifecycle management to sync collections, generate client code, discover APIs, run tests, and create requests. *Use case: API exploration, client SDK generation from collections, API test authoring.* (Claude Code)


## Productivity and Documents

- [PDF Viewer](https://claude.com/plugins#pdf-viewer) **`A`** - View, annotate, and sign PDFs in a live interactive viewer with markup, form-fill, approval stamps, and signature placement. *Use case: Contract review with annotations, PDF form filling, signature workflows, approval stamping.* (Cowork)
- [Productivity](https://claude.com/plugins#productivity) **`A`** - Manage tasks, plan your day, and build memory of important work context by syncing with calendar, email, and chat. *Use case: Daily planning, task management, cross-tool context building, calendar/email/chat synthesis.* (Cowork)


## Project Management

- [Asana](https://asana.com) - Integration to create and manage tasks, search projects, update assignments, and track progress. *Use case: Task creation from chat, project-progress reporting, assignment management.* (Claude Code, Cowork)
- [Atlassian](https://www.atlassian.com) - Connect to Jira and Confluence to search and create issues, access docs, manage sprints, and integrate development workflows. *Use case: Jira ticket management, Confluence doc search, sprint planning from chat.* (Claude Code, Cowork)
- [GitHub](https://github.com) - Official GitHub MCP server for repository management including issues, PRs, code review, and GitHub API access. *Use case: PR management, issue creation and triage, code search across repos.* (Claude Code, Cowork)
- [GitLab](https://gitlab.com) - Integration for repositories, merge requests, CI/CD pipelines, issues, and wikis with full DevOps lifecycle access. *Use case: GitLab MR workflows, CI/CD pipeline debugging, GitLab wiki management.* (Claude Code)
- [Linear](https://linear.app) - Integration to create issues, manage projects, update statuses, search workspaces, and streamline development workflow. *Use case: Issue creation, sprint management, workspace search.* (Claude Code, Cowork)


## Security

- [Endor Labs](https://www.endorlabs.com) - Set up endorctl and use Endor Labs to scan, prioritize, and fix security risks across the software supply chain. *Use case: SCA scanning, supply-chain risk prioritization, dependency-vulnerability remediation.* (Claude Code)
- [Security Guidance](https://claude.com/plugins#security-guidance) **`A`** - Security hook that warns about command injection, XSS, and unsafe code patterns when editing files. *Use case: In-editor security guardrails, OWASP-pattern detection, real-time vulnerability prevention.* (Claude Code)
- [Semgrep](https://semgrep.dev) - Catch security vulnerabilities in real-time and guide secure code authoring. *Use case: SAST scanning, custom-rule authoring, secure-by-default code generation.* (Claude Code)
- [Sonatype Guide](https://www.sonatype.com) - MCP for supply chain intelligence and dependency security analysis with vulnerability detection and version recommendations. *Use case: Dependency vulnerability scanning, version-recommendation lookup, supply-chain risk analysis.* (Claude Code)


## Skills Authoring

- [MCP Server Dev](https://claude.com/plugins#mcp-server-dev) **`A`** - Design and build MCP servers covering deployment (HTTP, MCPB, local), tools, auth, and interactive apps. *Use case: MCP server scaffolding, OAuth flow design, MCPB packaging.* (Claude Code)
- [Plugin Developer Toolkit](https://claude.com/plugins#plugin-developer-toolkit) **`A`** - Plugin development toolkit with 7 expert skills for hooks, MCP, commands, agents, validation, and best practices. *Use case: Plugin scaffolding, validation against the plugin schema, marketplace authoring.* (Claude Code)
- [Skill Creator](https://claude.com/plugins#skill-creator) **`A`** - Create, improve, and measure skills covering creation, updating, evaluation, and benchmarking performance. *Use case: Skill authoring, skill-performance evaluation, benchmarking before publishing.* (Claude Code)


## Custom Plugins

You can install plugins outside the official directory. Custom plugins are not reviewed by Anthropic — install only from sources you trust.

**From a local directory:** `claude --plugin-dir /path/to/plugin` loads a plugin in the current session.

**From a URL:** `claude --plugin-url https://example.com/plugin.zip` fetches and loads a plugin archive.

**From a git repo:** `/plugin marketplace add owner/repo` followed by `/plugin install <name>` installs via a personal marketplace.

**From a private marketplace:** configure required marketplaces in your repository's `.claude/settings.json` for team-wide plugin distribution.

For complete authoring guidance, see the Plugin Developer Toolkit entry in the Skills Authoring section above, or the Plugins overview linked in the header.


## Plugin Marketplaces

A plugin marketplace is a git repo or URL hosting `.claude-plugin/marketplace.json` that catalogs available plugins. Anyone can run one. Notable marketplaces:

- [claude-plugins-official](https://github.com/anthropics/claude-plugins-public#readme) - Anthropic's curated, vetted marketplace, auto-installed on Claude Code startup. *Use case: First-stop discovery; install with `/plugin install <name>@claude-plugins-official`.*
- [claude-code-plugins (Anthropic demo)](https://github.com/anthropics/claude-code) - Anthropic's example marketplace of reference plugins demonstrating the plugin system. *Use case: Plugin format examples, integration patterns; install with `/plugin marketplace add anthropics/claude-code`.*
- [Dan Ávila's marketplace](https://github.com/danavila/claude-code-plugins) - Community plugins for DevOps automation, documentation generation, project management, and testing suites.
- [Seth Hobson's sub-agents](https://github.com/wshobson/agents) - 80+ specialized sub-agents packaged as a plugin collection.


## Related

- [awesome-claude-connectors](https://github.com/rdmgator12/awesome-claude-connectors) - Anthropic Claude connectors directory (398+ entries) — the MCP-server layer that plugins often bundle.
- [awesome-grok-connectors](https://github.com/rdmgator12/awesome-grok-connectors) - xAI Grok connectors directory.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Community-maintained directory of MCP servers across all clients.
- [awesome-perplexity-connectors](https://github.com/rdmgator12/Perplexity-Connectors-awesome-list-) - Perplexity AI connectors directory.
- [awesome-mistral-connectors](https://github.com/rdmgator12/awesome-mistral-connectors) - Mistral Le Chat connectors directory.
- [awesome-lm-studio-connectors](https://github.com/rdmgator12/awesome-lm-studio-connectors) - LM Studio plugins and integrations directory.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps) - OpenAI ChatGPT apps and connectors directory.
- [awesome-gemini-extensions](https://github.com/rdmgator12/Gemini-Awesome-List-) - Google Gemini CLI extensions directory.
- [awesome-lovable-connectors](https://github.com/rdmgator12/awesome-lovable-connectors) - Lovable platform connectors directory.
- [awesome-healthcare-mcp-servers](https://github.com/rdmgator12/awesome-healthcare-mcp-servers) - Healthcare-focused MCP servers directory.

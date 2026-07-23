# Awesome List for Claude Plugins: [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0](https://img.shields.io/badge/License-CC0-blue.svg)](LICENSE) [![Last Commit](https://img.shields.io/github/last-commit/rdmgator12/awesome-claude-plugins)](https://github.com/rdmgator12/awesome-claude-plugins/commits/main)

> A free, community-maintained directory of plugins in Anthropic's official [Claude Plugins catalog](https://claude.com/plugins/) — installable bundles of skills, MCP servers, slash commands, sub-agents, and hooks that extend Claude Code and Cowork with one-command installation.

> [!NOTE]
> **This is a free, independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC.** "Claude," "Claude Code," and "Cowork" are trademarks of Anthropic PBC. Each plugin is the property of its respective owner. This list is published under the CC0 license shown in the badge above — public domain, free to copy, fork, redistribute.

**Last updated:** July 23, 2026 | **Total plugins:** 333 | **Surfaces:** Claude Code (273) · Cowork (128) · both (68) | **Categories:** 28

Plugins originated in Claude Code (October 2025) as packaged, versioned, shareable directories that bundle skills, MCP server references, slash commands, sub-agents, hooks, and LSP servers into a single installable unit. As of v2.1.129 (May 6, 2026), Anthropic runs the **Official Claude Plugins Directory** (`claude-plugins-official`) — a curated, vetted catalog auto-installed on Claude Code startup. Plugins also extend **Cowork**, Anthropic's agentic workspace, with role-class workflow bundles (Productivity, Design, Marketing, etc.) used by knowledge workers inside isolated VM environments.

For more information, see the [Plugins overview](https://claude.com/docs/plugins/overview), [plugin marketplaces guide](https://code.claude.com/docs/en/plugin-marketplaces), [submission form](https://claude.com/plugins#submit), and the [official Anthropic marketplace repo](https://github.com/anthropics/claude-plugins-official) (renamed from `claude-plugins-public`; the old URL still redirects).

Plugins marked with **`A`** are built and verified by Anthropic. Each entry ends with a surface tag: `(Claude Code)`, `(Cowork)`, or `(Claude Code, Cowork)`.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> [!NOTE]
> ### Two surfaces, one list — why this is bigger than the claude.ai plugin browser
>
> Plugins run on two surfaces, and this list catalogs **both** — the surface tag on every entry tells you where each one is available:
>
> - **Claude Code** (the developer CLI) — its marketplace (`claude-plugins-official`) is the *full* catalog, auto-installed on startup and dominated by developer and infrastructure plugins: language servers, cloud (AWS/GCP/Azure/Oracle), databases, CI/CD, security, and code tooling. **~273 of the entries below run here.**
> - **Cowork** (Anthropic's agentic workspace inside claude.ai) — its plugin library surfaces a **curated business/role subset**: CRM, finance, marketing, design, data dashboards, the Anthropic role bundles, and — new this week — full **Legal** (12 role-specialized plugins) and **Healthcare / life-sciences** verticals. **128 entries run here; 68 run on both.**
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

- [Agent SDK Dev](https://claude.com/plugins#agent-sdk-dev) **`A`** - Development kit for working with the Claude Agent SDK. *Use case: Scaffolding agents, validating SDK usage, testing agent workflows locally.* (Claude Code)
- [Agentforce ADLC](https://www.salesforce.com/agentforce) - Author, scaffold, deploy, test, and optimize Agentforce .agent files through the Agent Development Life Cycle. *Use case: Agentforce agent authoring, .agent scaffolding, agent testing and tuning.* (Claude Code)
- [AI-Firstify](https://ai-first.techwolf.ai) - Audit, re-engineer, or bootstrap any codebase to align with TechWolf's 9 AI-first design principles and 7 design patterns. *Use case: AI-first codebase audit, project re-engineering, greenfield AI-first scaffolding.* (Claude Code, Cowork)
- [AMD Skills](https://developer.amd.com) - AMD's verified agent skills for routing image and audio through local AI on Ryzen AI, serving LLMs on Instinct GPUs with vLLM, and analyzing GPU workloads. *Use case: Local Ryzen AI inference, vLLM model serving on Instinct GPUs, GPU workload analysis.* (Claude Code)
- [atomic-agents](https://github.com/BrainBlend-AI/atomic-agents) - Build AI agents with the Atomic Agents framework. *Use case: Multi-agent system development, best-practice validation, agent tool orchestration.* (Claude Code)
- [AWS Agents](https://aws.amazon.com/bedrock/agentcore/) - Build, deploy, and operate AI agents on AWS with Amazon Bedrock AgentCore, covering tools, memory, policies, and evaluation. *Use case: Bedrock agent scaffolding, agent memory and policy wiring, production agent hardening.* (Claude Code)
- [DataRobot Agent Skills](https://datarobot.com) - Train, deploy, predict, monitor, and explain ML models with DataRobot, including App Framework CI/CD. *Use case: AutoML model training, deployment monitoring, model-explainability reports.* (Claude Code, Cowork)
- [DeepEval](https://github.com/confident-ai/deepeval) - Add DeepEval evaluations, tracing, datasets, and Confident AI reports with iterative improvement loops to AI applications. *Use case: LLM output evaluation, test-dataset authoring, agent-quality regression tracking.* (Claude Code)
- [Domino Data Lab](https://www.domino.ai) - Operate the full Domino Data Lab platform across workspaces, jobs, model deployment, experiment tracking, and GenAI tracing. *Use case: Enterprise MLOps, experiment tracking, Spark/Ray/Dask job orchestration.* (Claude Code)
- [Exa](https://exa.ai) - Run AI web search, deep research, and content extraction with MCP tools and research skills. *Use case: Web-search grounding, multi-source research, page-content extraction for RAG.* (Claude Code, Cowork)
- [FiftyOne](https://voxel51.com) - Build high-quality datasets and computer-vision models by visualizing data, finding duplicates, running inference, and evaluating predictions. *Use case: CV dataset curation, model-error analysis, duplicate and edge-case discovery.* (Claude Code)
- [GoodMem](https://goodmem.ai) - AI memory infrastructure with Python SDK and MCP tools for managing embedders, spaces, and memories. *Use case: Long-term agent memory, semantic memory recall, embedding management via chat.* (Claude Code)
- [Hugging Face Skills](https://huggingface.co) - Build, train, evaluate, and use open source AI models, datasets, and Spaces from Hugging Face. *Use case: Model exploration, dataset selection, running inference on hosted models.* (Claude Code)
- [NVIDIA Skills](https://github.com/NVIDIA/skills) - Tackle accelerated-computing workflows, starting with cuOpt vehicle-routing optimization (VRP, TSP, PDP). *Use case: Route optimization, vehicle-routing problems, GPU-accelerated solver work.* (Claude Code)
- [Output.ai](https://output.ai) - Develop AI workflows with specialist agents for planning, building, debugging, and reviewing on the Output.ai platform. *Use case: Output SDK workflow scaffolding, workflow debugging, prompt authoring.* (Claude Code)
- [Pixeltable](https://docs.pixeltable.com) - Build multimodal AI applications with tables, computed columns, embedding search, UDFs, and tool-calling agents across 25+ AI provider integrations. *Use case: Multimodal data infrastructure, embedding-search pipelines, agent tool-calling over media tables.* (Claude Code, Cowork)
- [Pydantic AI](https://ai.pydantic.dev) - Write accurate agent code with up-to-date patterns for tools, structured output, streaming, and multi-agent apps. *Use case: Type-safe agent authoring, structured-output design, multi-agent orchestration.* (Claude Code)
- [Remember](https://github.com/Digital-Process-Tools/claude-remember) - Continuous memory for Claude Code that extracts, summarizes, and compresses conversations into tiered daily logs. *Use case: Long-running project memory, daily session continuity, conversation archival.* (Claude Code)
- [SageMaker AI](https://aws.amazon.com/sagemaker/) - Build, train, and deploy ML models with deep Amazon SageMaker expertise across the service surface. *Use case: Model training pipelines, endpoint deployment, SageMaker feature engineering.* (Claude Code)
- [Tavily](https://www.tavily.com) - Build AI applications with real-time web data using Tavily's search, extract, crawl, and research APIs. *Use case: Web-search grounding, structured extraction, research-agent data feeds.* (Claude Code, Cowork)
- [Together AI Skills](https://www.together.ai) - Run inference, training, embeddings, audio, video, images, function calling, and infrastructure on Together AI. *Use case: Open-model inference, fine-tuning jobs, batch inference and evaluations.* (Claude Code)
- [You.com Agent Skills](https://you.com) - Search the web, research with citations, and extract content with guided framework integrations. *Use case: Cited web research, search-augmented agents, content extraction across SDKs.* (Claude Code)

## Browser Automation

- [Browser Use](https://browser-use.com) - Give Claude a real Chrome or a Browser Use Cloud browser for browsing, scraping, form-filling, testing, and web-workflow automation. *Use case: Web scraping and data extraction, form automation, site testing with a real browser.* (Claude Code, Cowork)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools) - Control and inspect a live Chrome browser from your coding agent, record performance traces, and analyze network requests. *Use case: Web app debugging, performance profiling, network capture for reproduction cases.* (Claude Code)
- [Playwright](https://playwright.dev) - Browser automation and end-to-end testing MCP server by Microsoft. *Use case: E2E test authoring, web scraping with form interaction, screenshot-based visual regression, headless workflow automation.* (Claude Code)
- [TinyFish](https://www.tinyfish.ai) - Web infrastructure for AI agents, including web search, URL-to-markdown fetching, and browser automation for navigating sites and extracting structured data. *Use case: Send a browser agent to fill out a web form and extract structured data from a target site.* (Cowork)

## Business Operations

- [Enterprise Search](https://claude.com/plugins#enterprise-search) **`A`** - Search across all of your company's tools in one place — email, chat, documents, and wikis without switching between apps. *Use case: Cross-tool knowledge retrieval, finding decisions across Slack/email/Drive, answering "where did we discuss X" questions.* (Cowork)
- [Operations](https://claude.com/plugins#operations) **`A`** - Optimize business operations including vendor management, process documentation, change management, capacity planning, and compliance tracking. *Use case: Vendor onboarding, SOP authoring, ops dashboards, audit prep.* (Cowork)
- [Small Business](https://claude.com/plugins#small-business) **`A`** - Pre-built small business workflows including payroll planning, month-end close, weekly briefs, and growth campaigns using QuickBooks, PayPal, HubSpot, and related tools. *Use case: Solo founder ops, bookkeeping triage, weekly business reviews, growth-campaign coordination.* (Cowork)

## Cloud and Infrastructure

- [AWS Amplify](https://docs.amplify.aws/) - Build full-stack apps with AWS Amplify Gen 2 covering auth, data models, storage, GraphQL APIs, and Lambda functions. *Use case: Amplify Gen 2 scaffolding, GraphQL data modeling, auth flow setup.* (Claude Code)
- [AWS Core](https://aws.amazon.com/developer/) - Build, deploy, and operate applications on AWS with infrastructure-as-code authoring and core-service skills. *Use case: AWS IaC authoring, core-service usage, common-task automation.* (Claude Code)
- [AWS Dev Toolkit](https://github.com/aws-samples/sample-claude-code-plugins-for-startups) - Use 34 skills, 11 agents, and 3 MCP servers for building, migrating, and reviewing AWS architecture. *Use case: AWS architecture review, migration planning, multi-service development.* (Claude Code)
- [AWS Serverless](https://aws.amazon.com/serverless) - Design, build, deploy, test, and debug serverless applications using AWS Lambda, API Gateway, DynamoDB, and related services. *Use case: Lambda authoring, SAM template generation, serverless local testing.* (Claude Code)
- [AWS Startup Advisor](https://aws.amazon.com/startups/) - Get personalized AWS architecture, cost, security, and migration guidance for startups, including Activate credits eligibility. *Use case: Day-one account setup, startup architecture review, cost optimization.* (Claude Code)
- [AWS Transform](https://aws.amazon.com/transform/) - Migrate and modernize codebases to AWS including .NET, mainframe COBOL, VMware, SQL Server, and language and SDK upgrades. *Use case: NET-to-.NET 8 migration, COBOL-to-Java modernization, SDK upgrades.* (Claude Code)
- [Azure](https://azure.microsoft.com) - Turn Claude into an Azure expert with the Azure MCP server and skills to list resources, validate deployments, and optimize costs across 50+ services. *Use case: Azure resource inventory, deployment validation, cost optimization.* (Claude Code)
- [Cloudflare](https://www.cloudflare.com) - Skills for the Cloudflare developer platform covering Workers, Durable Objects, Agents SDK, MCP servers, Wrangler CLI, and Worker testing. *Use case: Edge function development, Durable Object design, Workers deployment, Cloudflare-hosted MCP servers.* (Claude Code)
- [Deploy on AWS](https://aws.amazon.com) - Deploy applications to AWS with architecture recommendations, cost estimates, and infrastructure-as-code deployment. *Use case: Greenfield AWS deployments, architecture review, cost-aware service selection.* (Claude Code)
- [Firebase](https://firebase.google.com) - MCP integration for managing Firestore, authentication, Functions, hosting, and storage. *Use case: Mobile-backend operations, real-time database management, Firebase rules editing.* (Claude Code)
- [Hostinger](https://www.hostinger.com) - Deploy, manage, and monitor Hostinger services covering websites, domains, ecommerce, email marketing, and VPS with OAuth or API-token auth. *Use case: Website deployment, domain management, VPS operations from chat.* (Claude Code)
- [Migration to AWS](https://aws.amazon.com/cloud-migration/) - Plan a migration from GCP and OpenAI/Gemini workloads to AWS by analyzing IaC, app code, and billing to design an architecture. *Use case: GCP-to-AWS migration planning, AI-provider mapping to Bedrock, cost estimation.* (Claude Code)
- [Netlify Skills](https://www.netlify.com) - Netlify platform skills for functions, edge functions, blobs, database, image CDN, forms, config, and CLI workflows. *Use case: JAMstack deployment, edge function development, Netlify forms and config tuning.* (Claude Code)
- [Railway](https://railway.app) - Deploy and manage apps, databases, and infrastructure on Railway covering project setup, deploys, and environment configuration. *Use case: Quick app deploys, database provisioning, env-var management.* (Claude Code)
- [Render](https://render.com) - Deploy, debug, and monitor applications on Render with skills, an agent, slash commands, and a render.yaml validation hook. *Use case: Render deploys, config validation pre-push, production debugging.* (Claude Code)
- [Terraform](https://www.terraform.io) - MCP server for advanced infrastructure-as-code automation and Terraform-ecosystem integration. *Use case: HCL authoring, state-file inspection, provider exploration.* (Claude Code)
- [Val Town](https://val.town) - Build and deploy on Val Town with HTTP vals, cron jobs, SQLite, email, OAuth, and React UI. *Use case: Serverless function deployment, scheduled jobs, lightweight full-stack vals.* (Claude Code, Cowork)
- [Vercel](https://vercel.com) - Integration to manage deployments, builds, logs, domains, and frontend infrastructure. *Use case: Next.js deployment workflows, build-log triage, domain configuration, edge function management.* (Claude Code)
- [Wix](https://www.wix.com) - Build, manage, and deploy Wix sites and apps with CLI skills for dashboard extensions, backend APIs, and site widgets. *Use case: Wix custom-app development, dashboard extension authoring, widget shipping.* (Claude Code, Cowork)

## Code Quality and Review

- [Aikido Security](https://www.aikido.dev) - Security scanning for SAST, secrets, and IaC vulnerability detection via Aikido MCP server. *Use case: Pre-commit security scan, secrets-leak detection, IaC misconfiguration triage.* (Claude Code)
- [Code Review](https://claude.com/plugins#code-review) **`A`** - AI code review with specialized agents and confidence-based filtering for pull requests. *Use case: PR review automation, multi-agent code analysis, confidence-weighted feedback.* (Claude Code)
- [Code Simplifier](https://claude.com/plugins#code-simplifier) **`A`** - Code clarity agent that simplifies and refines recently modified code while preserving functionality and consistency. *Use case: Post-edit cleanup, complexity reduction, dead-code elimination after refactors.* (Claude Code)
- [CodeRabbit](https://www.coderabbit.ai) - AI code review with 40+ analyzers, AST parsing, security checks, and auto-integrated project guidelines. *Use case: PR review with deep linting, security-aware diff analysis, project-guideline enforcement.* (Claude Code)
- [Greptile](https://www.greptile.com) - AI-powered codebase search to query repositories in natural language to find code, understand dependencies, and explore architecture. *Use case: Cross-repo code search, dependency tracing, architecture discovery in unfamiliar codebases.* (Claude Code)
- [Lumen](https://github.com/ory/lumen) - Run precise local semantic code search via MCP, indexing your codebase with Go AST parsing and embedding with Ollama or LM Studio. *Use case: Local semantic code search, AST-aware symbol lookup, on-device vector code search.* (Claude Code)
- [Optibot Code Review](https://getoptimal.ai) - AI code review that catches production bugs, business-logic issues, and security vulnerabilities. *Use case: Pre-merge production-bug detection, business-logic regression hunting, security pass on diffs.* (Claude Code)
- [PR Review Toolkit](https://claude.com/plugins#pr-review-toolkit) **`A`** - PR review agents for comments, tests, errors, types, quality, and simplification. *Use case: Multi-axis PR review, test-coverage check, type-correctness validation in pull requests.* (Claude Code)
- [Qodo Skills](https://www.qodo.ai) - AI agents that integrate code quality, testing, security, and compliance checks into your SDLC. *Use case: Test generation, code-quality gates, compliance scanning in CI.* (Claude Code, Cowork)
- [session-report](https://claude.com/plugins#session-report) **`A`** - Generate an explorable HTML report of Claude Code session usage including tokens, cache efficiency, subagents, skills, and tool calls. *Use case: Session retrospection, cache-hit analysis, subagent usage audit.* (Claude Code)
- [sonarqube](https://www.sonarsource.com/products/sonarqube) - Automatically enforce SonarQube code quality and security in the agent coding loop. *Use case: Quality-gate enforcement, SAST scanning, code-smell detection inline with edits.* (Claude Code)
- [Sourcegraph](https://sourcegraph.com) - Search code across codebases, trace references, analyze refactor impact, investigate incidents, and run security sweeps. *Use case: Cross-repo refactor planning, incident investigation, security sweep on call paths.* (Claude Code)

## Communication and Messaging

- [Circleback](https://circleback.ai) - Conversational-context integration for searching and accessing meetings, emails, and calendar events. *Use case: Pulling meeting context into current work, finding action items from past calls.* (Claude Code)
- [discord](https://discord.com) - Messaging bridge with built-in access control, pairing, allowlists, and policy management. *Use case: Discord server moderation from Claude, allowlisted Discord posting, policy-controlled bot workflows.* (Claude Code)
- [fakechat](https://claude.com/plugins#fakechat) - Localhost web chat for testing channel notification flows with no tokens, access control, or third-party services. *Use case: Local notification testing, channel-integration development without external dependencies.* (Claude Code)
- [iMessage](https://claude.com/plugins#imessage) - Messaging bridge with built-in access control that reads chat.db directly and sends via AppleScript. *Use case: macOS-only iMessage automation, allowlisted texting workflows, message-history search.* (Claude Code)
- [Resend](https://resend.com) - Send and receive email with Resend covering API integration, agent inbox, CLI, React Email components, and deliverability. *Use case: Transactional email integration, React Email templating, agent inbox workflows.* (Claude Code)
- [Slack](https://slack.com) **`A`** - Official Slack MCP server with skills and slash commands for searching messages, sending communications, managing canvases, and surfacing channel insights. *Use case: Slack-message drafting, channel-thread summarization, async standups, in-Slack analysis.* (Claude Code, Cowork)
- [telegram](https://telegram.org) - Messaging bridge with built-in access control, pairing, and policy management. *Use case: Telegram bot workflows, allowlisted messaging, channel automation.* (Claude Code)
- [Twilio developer kit](https://www.twilio.com) - Procedural knowledge for AI coding agents on which Twilio APIs to use, in what order, and what to avoid, across SMS, Voice, WhatsApp, Verify, SendGrid, and 30+ products. *Use case: Twilio messaging and voice integration, SendGrid email workflows, compliance-aware comms.* (Claude Code, Cowork)
- [Zoom](https://zoom.us) - Plan, build, and debug Zoom integrations across REST APIs, Meeting SDK, Video SDK, webhooks, bots, and MCP workflows. *Use case: Zoom app development, meeting recording retrieval, transcript access, AI-powered Zoom experiences.* (Claude Code, Cowork)

## CRM and Sales

- [Apollo](https://www.apollo.io) - Prospect, enrich leads, and load outreach sequences with Apollo.io. *Use case: B2B prospect discovery, lead enrichment from chat, outreach-sequence loading.* (Claude Code, Cowork)
- [Carta crm](https://carta.com/product-updates/crm-plugin/) - Manage the Carta CRM conversationally to search, add, update, and enrich investors, companies, contacts, deals, notes, and fundraisings. *Use case: dealflow and pipeline management, investor and LP record updates, company enrichment from websites, fundraising-round tracking.* (Claude Code, Cowork)
- [Common Room](https://www.commonroom.io) - Turn Common Room into your GTM copilot — research accounts and contacts, prep for calls, and draft personalized outreach across email, LinkedIn, and phone. *Use case: Call prep, account research, multi-channel outreach drafting.* (Cowork)
- [Hunter](https://hunter.io) - Find and verify professional email addresses, search contacts by domain, and enrich company data. *Use case: Email discovery, contact verification, domain-based prospecting.* (Claude Code)
- [Lusha](https://www.lusha.com) - Prospect, enrich, and build call-ready lead lists with verified phone numbers, company signals, and lookalike targeting. *Use case: Lead-list building, contact enrichment, lookalike-account targeting.* (Claude Code, Cowork)
- [monday CRM](https://monday.com/crm) - Run your CRM in plain language to build pipelines, ranked deal briefings, and forecast dashboards, and turn meeting notes into deal updates. *Use case: Pipeline building, ranked deal briefings, CRM data cleanup.* (Claude Code, Cowork)
- [Sales](https://claude.com/plugins#sales) **`A`** - Prospect, craft outreach, build deal strategy, prep for calls, manage pipeline, and write personalized messaging. *Use case: Pipeline management, prospect research, personalized cold outreach.* (Cowork)
- [Vibe Prospecting](https://www.vibeprospecting.ai) - Search, match, enrich, filter, and export live B2B prospects through natural-language GTM workflows. *Use case: lead-list building, CRM enrichment, executive discovery, multi-step prospecting automation.* (Claude Code, Cowork)
- [ZoomInfo](https://www.zoominfo.com) - Search companies and contacts, enrich leads, find lookalikes, and get AI-ranked contact recommendations with pre-built B2B sales workflows. *Use case: B2B prospect enrichment, lookalike-account discovery, AI-ranked contact targeting.* (Claude Code, Cowork)

## Customer Support

- [Customer Support](https://claude.com/plugins#customer-support) **`A`** - Triage tickets, draft responses, escalate issues, build knowledge base, research customer context, and turn resolved issues into self-service content. *Use case: Support-ticket triage, response drafting, knowledge-base content generation.* (Cowork)
- [Intercom](https://www.intercom.com) - Integration to search conversations, analyze customer support patterns, and look up contacts and companies. *Use case: Customer-conversation analytics, support-pattern detection, real-time customer-data lookup.* (Claude Code, Cowork)

## Data and Databases

- [Airtable](https://www.airtable.com) - Database and operations layer for agents, with shared visual surfaces and sync integrations via the official Airtable MCP server. *Use case: base and schema creation, record management, multiplayer grid/kanban/calendar collaboration, syncing to Jira/Salesforce/Zendesk.* (Claude Code, Cowork)
- [AlloyDB](https://cloud.google.com/alloydb) - Create, connect, and interact with an AlloyDB for PostgreSQL database and its data. *Use case: AlloyDB provisioning, PostgreSQL-compatible queries, data exploration.* (Claude Code)
- [AlloyDB Omni](https://cloud.google.com/alloydb/omni) - Create, connect, and interact with an AlloyDB Omni database and its data. *Use case: Self-managed AlloyDB Omni setup, local PostgreSQL-compatible queries, data access.* (Claude Code)
- [altimate-code](https://www.altimate.ai) - Delegates dbt and warehouse work to the altimate-code CLI agent with 100+ data tools for SQL analysis, column-level lineage, and dbt development. *Use case: dbt model development, column-level lineage tracing, SQL analysis over a warehouse.* (Claude Code)
- [Astronomer Data Agents](https://www.astronomer.io) - Engineer Apache Airflow and Astronomer pipelines, authoring DAGs, debugging failures, tracing lineage, and migrating Airflow 2 to 3. *Use case: Airflow DAG authoring, pipeline debugging, Airflow 2-to-3 migration.* (Claude Code)
- [Atlan](https://atlan.com) - Data catalog plugin with semantic search, lineage traversal, glossary management, and data-quality rules via the Atlan MCP server. *Use case: Data discovery, lineage exploration, glossary management, data-quality rule authoring.* (Claude Code, Cowork)
- [AWS Data Analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/) - Build data lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena. *Use case: Data-lake setup, Glue ETL authoring, Athena querying.* (Claude Code)
- [Azure Cosmos DB Assistant](https://azure.microsoft.com/products/cosmos-db) - Get expert help with Azure Cosmos DB data modeling, query optimization, performance tuning, and best practices. *Use case: Cosmos DB data modeling, request-unit optimization, query tuning.* (Claude Code)
- [Azure SQL Developer](https://github.com/microsoft/azure-sql-database-container) - Run the Azure SQL Database engine locally in a container and teach the agent to connect, migrate, and query it. *Use case: Local Azure SQL development, containerized DB testing, migration authoring.* (Claude Code)
- [Bigdata.com](https://bigdata.com) - Official Bigdata.com plugin providing financial research, analytics, and intelligence tools powered by the Bigdata MCP. *Use case: Equity research, financial-data analytics, market intelligence queries.* (Claude Code, Cowork)
- [BigQuery Data Analytics](https://cloud.google.com/bigquery) - Connect, query, and generate data insights for BigQuery datasets. *Use case: BigQuery SQL authoring, dataset exploration, analytics insight generation.* (Claude Code)
- [ClickHouse](https://clickhouse.com) - Connect to ClickHouse Cloud, browse services and schemas, run read-only SQL, and monitor backups and costs. *Use case: ClickHouse analytics queries, service monitoring, ClickPipe inspection.* (Claude Code, Cowork)
- [ClickHouse Best Practices](https://clickhouse.com/docs/best-practices) - Apply 28 prioritized best-practice rules for ClickHouse schema design, query optimization, and data ingestion. *Use case: ClickHouse schema review, query optimization, ingestion tuning.* (Claude Code)
- [Cloud SQL for MySQL](https://cloud.google.com/sql/docs/mysql) - Connect and interact with a Cloud SQL for MySQL database and its data. *Use case: Cloud SQL MySQL queries, schema inspection, managed-database access.* (Claude Code)
- [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres) - Create, connect, and interact with a Cloud SQL for PostgreSQL database. *Use case: Cloud SQL PostgreSQL provisioning, query authoring, data exploration.* (Claude Code)
- [Cloud SQL for SQL Server](https://cloud.google.com/sql/docs/sqlserver) - Connect to Cloud SQL for SQL Server and work with its data. *Use case: Cloud SQL Server queries, schema inspection, managed-instance access.* (Claude Code)
- [CockroachDB](https://www.cockroachlabs.com) - Distributed SQL plugin to explore schemas, write optimized SQL, debug queries, and manage distributed database clusters. *Use case: Distributed SQL development, query plan analysis, multi-region schema design.* (Claude Code, Cowork)
- [Convex](https://convex.dev) - Develop a Convex backend covering schema design, real-time features, auth, file storage, scheduled jobs, and AI agents. *Use case: Convex schema authoring, real-time backend development, runtime-error monitoring.* (Claude Code)
- [Daloopa](https://daloopa.com) - Financial analysis skills powered by Daloopa's institutional-grade data. *Use case: Equity research with structured financials, model-building from validated data, earnings-quality analysis.* (Cowork)
- [Data](https://claude.com/plugins#data-cowork) **`A`** - Write SQL, explore datasets, generate insights, build visualizations and dashboards, and turn raw data into clear stories. *Use case: Ad-hoc SQL, dashboard authoring, stakeholder-facing data storytelling.* (Claude Code, Cowork)
- [Data Agent Kit Starter Pack](https://github.com/gemini-cli-extensions/data-agent-kit-starter-pack) - Architect GCP data pipelines, transform data with dbt, and orchestrate Spark and BigQuery notebooks via natural language. *Use case: GCP pipeline design, dbt transformations, cross-service data orchestration.* (Claude Code)
- [Data Engineering](https://github.com/astronomer/agents) - Warehouse and pipeline workflows covering warehouse exploration, pipeline authoring, and Airflow integration. *Use case: ETL development, warehouse schema exploration, Airflow DAG authoring.* (Claude Code)
- [Databases on AWS](https://aws.amazon.com/products/databases/) - Get expert guidance across the AWS database portfolio covering schema design, queries, migrations, and database selection. *Use case: AWS database selection, schema design, cross-engine migration.* (Claude Code)
- [Databricks](https://developers.databricks.com) - First-party Databricks skills spanning the CLI, Apps, Lakebase, Model Serving, Lakeflow Jobs, Spark Declarative Pipelines, and Declarative Automation Bundles. *Use case: Databricks pipeline authoring, model serving, classic-to-serverless migration.* (Claude Code)
- [DataHub Skills](https://datahub.com) - Plan connectors, search the catalog, enrich metadata, trace lineage, and manage data quality with DataHub. *Use case: Metadata cataloging, lineage tracing, data-quality rule setup.* (Claude Code)
- [Dataproc](https://cloud.google.com/dataproc) - Manage Dataproc clusters and jobs. *Use case: Spark and Hadoop cluster management, job submission, Dataproc orchestration.* (Claude Code)
- [Dataverse](https://powerplatform.microsoft.com/en-us/dataverse/) - Build on, analyze, and manage Microsoft Dataverse with the Dataverse MCP, PAC CLI, and Python SDK. *Use case: Dataverse table modeling, PAC CLI automation, Dynamics data access.* (Claude Code)
- [DuckDB Skills](https://duckdb.org) - Read any data file, attach and query DuckDB databases, search docs, and manage extensions. *Use case: Local analytical queries, ad-hoc file analysis, DuckLake and DuckDB workflows.* (Claude Code)
- [Firestore](https://cloud.google.com/firestore) - Connect and interact with Firestore databases, collections, and documents. *Use case: Firestore document CRUD, collection queries, NoSQL data exploration.* (Claude Code)
- [Knowledge Catalog](https://cloud.google.com/dataplex) - Discover, manage, monitor, and govern data and AI artifacts across your data platform. *Use case: Data-artifact discovery, governance, catalog monitoring.* (Claude Code)
- [Looker](https://cloud.google.com/looker) - Connect to Looker and interact with your data using LookML. *Use case: LookML modeling, Looker exploration, BI query authoring.* (Claude Code)
- [LSEG](https://www.lseg.com) - Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build macro dashboards using LSEG financial data and analytics. *Use case: Fixed-income analysis, FX strategy work, options valuation, macro-research dashboards.* (Cowork)
- [MongoDB](https://www.mongodb.com) - Official MongoDB plugin with MCP server and skills for connecting, exploring data, managing collections, and optimizing queries. *Use case: MongoDB query authoring, schema design, aggregation-pipeline optimization.* (Claude Code)
- [Neon](https://neon.tech) - Manage Neon PostgreSQL projects and databases through its skill and MCP server. *Use case: Serverless PostgreSQL branching, Neon project management, schema migrations.* (Claude Code)
- [Oracle AI Data Platform Databricks Migrator](https://github.com/oracle-samples/oracle-aidp-samples) - Drive the Oracle AIDP Databricks Migration Toolkit in natural language, planning and executing automated Databricks-to-AIDP migrations of notebooks, jobs, schedules, and catalog DDL. *Use case: Databricks-to-AIDP migration, dependency rewrite, cell-by-cell execute-verify-fix on a live cluster.* (Claude Code)
- [Oracle AI Data Platform Spark Connectors](https://docs.oracle.com/en/cloud/paas/ai-data-platform/index.html) - Connect Spark to Oracle Autonomous DB, Fusion ERP, OCI Streaming, Iceberg, and external systems with 18 connector skills. *Use case: Spark source connectivity, Iceberg and ADB ingestion, cross-system data loading.* (Claude Code)
- [Oracle AI Data Platform Workbench](https://www.oracle.com/data-platform/) - Operate a Spark/Delta lakehouse in natural language across discovery, Spark SQL, pipelines, governance, and MLOps with 37 skills. *Use case: Lakehouse SQL generation, pipeline authoring, Delta governance and time-travel.* (Claude Code)
- [Oracle Database](https://www.oracle.com/database) - Connect, query, and interact with Oracle Databases and their data. *Use case: Oracle SQL authoring, schema inspection, database interaction.* (Claude Code)
- [Pigment](https://www.pigment.com) - Analyze business data and build custom Pigment models, metrics, and boards through natural language. *Use case: Business planning models, metric authoring, board building.* (Claude Code)
- [Pinecone](https://www.pinecone.io) - Vector database integration for managing indexes, querying, and rapid prototyping. *Use case: Vector-search prototyping, RAG pipeline development, index management.* (Claude Code)
- [PlanetScale](https://planetscale.com) - Authenticated hosted MCP server for PlanetScale organizations, databases, branches, schema, and Insights. *Use case: Database branching, slow-query analysis, schema migration on serverless MySQL/Postgres.* (Claude Code, Cowork)
- [Preset CLI Skills](https://www.preset.io) - Drive Apache Superset and Preset from the `sup` CLI for shell, scripting, and CI/CD workflows. *Use case: Superset/Preset automation, BI-asset CI/CD, scripted dashboard management.* (Claude Code)
- [Prisma](https://www.prisma.io) - MCP integration for PostgreSQL database management, schema migrations, SQL queries, and connection string management. *Use case: Prisma schema authoring, migration generation, PostgreSQL data interaction.* (Claude Code, Cowork)
- [Qdrant Skills](https://qdrant.tech) - Scale, tune, and monitor Qdrant vector search and improve search quality across multi-language SDKs. *Use case: Vector-search tuning, index optimization, RAG retrieval quality.* (Claude Code, Cowork)
- [Redis Development](https://redis.io) - Apply best practices for Redis data structures, query engine, vector search, caching, and performance. *Use case: Redis data modeling, caching strategy, vector-search setup.* (Claude Code)
- [Rill](https://www.rilldata.com) - Develop and query projects in the Rill business-intelligence platform. *Use case: Rill dashboard development, metrics-layer authoring, BI querying.* (Claude Code)
- [SAP HANA CLI](https://github.com/SAP-samples/hana-cli-claude-plugin) - Work SAP HANA Cloud and on-premise databases with 150+ tools covering queries, import/export, data-quality profiling, schema comparison, backups, and performance monitoring. *Use case: HANA query authoring, schema comparison, backup and performance operations.* (Claude Code)
- [Snowflake Cortex Code](https://www.snowflake.com) - Route Snowflake prompts to Cortex Code for execution, with commands for code review and task delegation. *Use case: Snowflake SQL execution, Cortex Code delegation, in-warehouse code review.* (Claude Code)
- [S&P Global](https://www.spglobal.com) - Financial data and analytics including company tearsheets, earnings previews, and transaction summaries via Kensho. *Use case: Equity tear-sheet generation, earnings-preview drafting, M&A transaction analysis.* (Cowork)
- [Spanner](https://cloud.google.com/spanner) - Connect and interact with Spanner data using natural language. *Use case: Spanner SQL queries, distributed-schema design, data exploration.* (Claude Code)
- [Supabase](https://supabase.com) - MCP integration for database operations, authentication, storage, and real-time features. *Use case: PostgreSQL backend management, auth flow development, real-time subscription debugging.* (Claude Code)
- [TDengine IDMP](https://github.com/taosdata/agent-skills) - Packaged skills for TDengine's industrial data management platform covering discovery, schema inspection, and safe operational workflows. *Use case: Industrial time-series data discovery, schema inspection, guarded operational tasks.* (Claude Code)
- [VSQL Extension Builder](https://villagesql.com) - Build a VillageSQL extension for MySQL end-to-end through a 7-phase persona-driven workflow. *Use case: Porting PostgreSQL extensions to MySQL, MySQL extension scaffolding.* (Claude Code)
- [Zilliz](https://zilliz.com) - Manage Zilliz Cloud with 14 skills for cluster lifecycle, collection schema, vector search, index tuning, and backups. *Use case: Zilliz cluster lifecycle, vector-collection schema, index tuning.* (Claude Code)

## Design and Creative

- [Adobe for Creativity](https://creativecloud.adobe.com) - Adobe Creative Cloud tools for images, vectors, design, and video covering Photoshop, Illustrator, Premiere, and Express. *Use case: Multi-asset editing, platform-adapted exports, multi-step creative workflows from chat.* (Claude Code, Cowork)
- [Brand Voice](https://www.tribe.ai) - Discover your brand voice from existing documents and conversations, generate enforceable guidelines, and validate AI-generated content. *Use case: Brand-voice extraction, content validation against tone, guideline authoring.* (Cowork)
- [Canva](https://www.canva.com) - Create, edit, review, resize, and brand-check Canva designs with the Canva MCP server. *Use case: Design generation from chat, brand-compliance checks, batch resizing for platforms.* (Claude Code, Cowork)
- [Cloudinary](https://cloudinary.com) - Integration to manage assets, apply transformations, and optimize media through natural conversation. *Use case: Image-transformation development, video-optimization pipelines, asset library management.* (Claude Code, Cowork)
- [Design](https://claude.com/plugins#design) **`A`** - Accelerate design workflows including critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. *Use case: Design critique, design-system component authoring, accessibility audit, design-to-dev handoff specs.* (Cowork)
- [Figma](https://www.figma.com) - Design platform integration to access design files, extract component information, read design tokens, and translate designs into code. *Use case: Design-token export, component-to-code translation, design-file inspection from dev workflow.* (Claude Code, Cowork)
- [Frontend Design](https://claude.com/plugins#frontend-design) **`A`** - Craft production-grade frontends with distinctive design that avoids generic AI aesthetics. *Use case: Landing-page design, app-shell composition, distinctive component design, anti-shadcn-default polish.* (Claude Code)
- [HyperFrames](https://hyperframes.heygen.com) - Write HTML and render video with GSAP animations, captions, voiceovers, and website-to-video capture, by HeyGen. *Use case: Programmatic video composition, animated explainers, website-to-video capture.* (Claude Code)
- [Miro](https://miro.com) - Secure access to Miro boards to read board context, create diagrams, and generate code with enterprise-grade security. *Use case: Whiteboard-to-code workflows, architecture-diagram authoring, board-context retrieval.* (Claude Code, Cowork)
- [Playground](https://claude.com/plugins#playground) **`A`** - Interactive HTML playgrounds with visual controls, live preview, and prompt output including design, data, concept map, and critique templates. *Use case: Live design iteration, prompt-output visualization, concept-map authoring, in-chat critique surfaces.* (Claude Code)
- [Runway API](https://runwayml.com) - Generate videos, images, and audio at scale across seedance2, gen4.5, veo3, and more. *Use case: Batch ad-video generation, product videos, creative iteration at scale.* (Claude Code)
- [Sanity](https://www.sanity.io) - Content platform integration with MCP server, agent skills, and slash commands for content authoring, GROQ query building, schema design, and Visual Editing. *Use case: GROQ query optimization, schema design, Visual Editing setup, structured-content authoring.* (Claude Code, Cowork)
- [Save to Spotify](https://open.spotify.com) - Create polished audio episodes with TTS narration, timelines, and cover images, then save them to Spotify. *Use case: Podcast-episode generation, TTS narration, Spotify publishing.* (Claude Code)
- [UI Theme Designer](https://github.com/SAP/ui-theme-designer-plugins-for-coding-agents) - SAP's plugin for working with UI Theme Designer, bundling how-to and conceptual skills for theming on SAP BTP. *Use case: SAP BTP theming, UI Theme Designer how-to lookups, theme-question answering.* (Claude Code)

## Developer Workflows

- [Apollo GraphQL](https://www.apollographql.com) - Build with Apollo Client, Server, Federation, Connectors, Router, Rover CLI, and the Apollo MCP server. *Use case: GraphQL schema design, federation setup, query optimization.* (Claude Code)
- [Buildkite](https://buildkite.com) - Use official Buildkite skills for pipelines, migration, preflight, agent runtime, CLI, and API. *Use case: CI/CD pipeline authoring, build debugging, Buildkite agent setup.* (Claude Code, Cowork)
- [CKEditor](https://ckeditor.com) - Install, configure, and integrate CKEditor 5, free and premium, into any JavaScript project. *Use case: Rich-text editor integration, CKEditor 5 configuration, plugin setup in a web app.* (Claude Code)
- [Claude Code Setup](https://claude.com/plugins#claude-code-setup) **`A`** - Analyze codebases and recommend tailored Claude Code automations including hooks, skills, MCP servers, and subagents. *Use case: First-time Claude Code setup on an unfamiliar repo, automation discovery, configuration audit.* (Claude Code)
- [CLAUDE.md Management](https://claude.com/plugins#claude-md-management) **`A`** - Maintain CLAUDE.md by auditing quality, capturing learnings, and keeping project memory current. *Use case: CLAUDE.md hygiene, learning capture, project-memory refresh after major changes.* (Claude Code)
- [Code Modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) **`A`** - Modernize legacy codebases such as COBOL, legacy Java/C++, and monoliths with a structured assess, map, extract, and transform workflow. *Use case: Legacy-code assessment, business-rule extraction, staged modernization.* (Claude Code)
- [Commit Commands](https://claude.com/plugins#commit-commands) **`A`** - Commands for Git commit workflows including commit, push, and PR creation. *Use case: Commit-message generation, PR creation, conventional-commit enforcement.* (Claude Code)
- [CWC Makers](https://claude.com/cwc-makers) **`A`** - Onboard a Code-with-Claude Makers Cardputer with one command that clones the repo, flashes firmware, and installs the Claude Buddy app. *Use case: Cardputer setup, UIFlow firmware flashing, maker-project onboarding.* (Claude Code)
- [Desktop commander](https://desktopcommander.app) - MCP server for terminal commands, process management, and file operations across text, code, PDF, DOCX, Excel, images, and structured data. *Use case: Local terminal automation, multi-format file editing, long-running process management from Claude.* (Claude Code, Cowork)
- [Feature Dev](https://claude.com/plugins#feature-dev) **`A`** - Feature development workflow with agents for exploration, design, and review. *Use case: New-feature scoping, multi-phase development workflow, design-then-review cadence.* (Claude Code)
- [Forge Skills](https://developer.atlassian.com/platform/forge) - Scaffold and deploy Atlassian Forge apps, build Teamwork Graph connectors for Rovo, and debug systematically. *Use case: Forge app scaffolding, Rovo connector development, pre-deploy review.* (Claude Code)
- [GitKraken](https://www.gitkraken.com) - Gives Claude access to real Git and project context — commits, branches, pull requests, and issues across GitHub, GitLab, Azure DevOps, Bitbucket, and Jira. *Use case: Cross-repo Git context, PR and issue lookup, branch and commit history queries.* (Claude Code, Cowork)
- [Hookify](https://claude.com/plugins#hookify) **`A`** - Create custom hooks via markdown to prevent unwanted behaviors from conversation patterns or explicit instructions. *Use case: Behavioral guardrail authoring, custom Stop hooks, pattern-based hook generation.* (Claude Code)
- [Liquid Skills](https://shopify.dev/docs/api/liquid) - Apply Liquid fundamentals, CSS/JS/HTML standards, and WCAG accessibility patterns for Shopify themes. *Use case: Liquid theme coding, accessibility compliance, theme coding standards.* (Claude Code)
- [Mergify](https://mergify.com) - Skills for the Mergify CLI covering merge queues, stacked pull requests, Test Insights, merge protections, and configuration. *Use case: Merge-queue management, stacked-PR workflows, flaky-test triage and quarantine.* (Claude Code)
- [Modern Web Guidance](https://goo.gle/modern-web-guidance) - Keep a coding agent current with the latest web platform best practices, maintained by the Google Chrome team. *Use case: Up-to-date web-standards guidance, baseline-feature checks, modern-API adoption.* (Claude Code, Cowork)
- [NetSuite SuiteCloud](https://www.netsuite.com) - Author SuiteCloud Development Framework objects, UIF single-page-app components, and AI Service Connector integrations. *Use case: SDF object authoring, SuiteCloud customization, NetSuite AI connector setup.* (Claude Code)
- [Qt Development Skills](https://www.qt.io) - Review and write Qt C++/QML code and generate Qt documentation. *Use case: QML coding, Qt C++ review, Qt code documentation.* (Claude Code, Cowork)
- [Quarkus Agent](https://quarkus.io) - Create, manage, and interact with Quarkus applications covering scaffolding, dev mode, extensions, and docs search. *Use case: Quarkus project scaffolding, dev-mode lifecycle, extension management.* (Claude Code)
- [Ralph Loop](https://claude.com/plugins#ralph-loop) **`A`** - Interactive AI loops for iterative development using the Ralph Wiggum technique where Claude works on tasks repeatedly until completion. *Use case: Stubborn-task iteration, /loop-driven development, autonomous task completion.* (Claude Code)
- [SAP CDS / CAP](https://cap.cloud.sap) - Develop SAP Cloud Application Programming Model (CAP) projects with CDS model and CAP documentation search. *Use case: CAP project development, CDS model search, CAP documentation lookup.* (Claude Code)
- [SAP Fiori](https://github.com/SAP/open-ux-tools/tree/main/packages/fiori-mcp-server) - Build and modify SAP Fiori applications with AI assistance. *Use case: Fiori app development, UI adaptation, Fiori tooling automation.* (Claude Code)
- [SAP Mobile Development Kit](https://help.sap.com/docs/MDK) - Build and modify SAP Mobile Development Kit apps with schema lookups, action validation, rule editing, and scaffolding. *Use case: MDK app scaffolding, action validation, rule editing.* (Claude Code)
- [Servicenow sdk](https://developer.servicenow.com) - Create, edit, and deploy ServiceNow applications with the Fluent SDK through Claude, building and managing ServiceNow apps, workflows, and agents. *Use case: ServiceNow app development, Fluent SDK scaffolding, workflow and agent deployment.* (Claude Code, Cowork)
- [Superpowers](https://github.com/obra/superpowers) - Brainstorming, subagent development with code review, debugging, TDD, and skill authoring. *Use case: Broad-spectrum developer enhancement, TDD workflow, skill-authoring scaffolds.* (Claude Code)
- [TeamCity CLI](https://www.jetbrains.com/teamcity) - Drive TeamCity CI/CD via the teamcity CLI to explore builds, view logs, start jobs, and manage queues and agents. *Use case: TeamCity build inspection, job triggering, agent and queue management.* (Claude Code)
- [UI5](https://ui5.sap.com/) - Create and validate SAPUI5/OpenUI5 projects, access API docs, run the UI5 linter, and follow best practices. *Use case: UI5 project creation, linter-driven validation, API-doc lookup.* (Claude Code)
- [UI5 Modernization](https://github.com/UI5/plugins-coding-agents/tree/main/plugins/ui5-modernization) - Complete toolkit with workflow and specialized fix patterns for modernizing SAPUI5/OpenUI5 applications. *Use case: Legacy UI5 modernization, automated fix patterns, staged upgrade workflow.* (Claude Code)
- [UI5 TypeScript Conversion](https://github.com/UI5/plugins-coding-agents) - Convert JavaScript-based UI5 projects to TypeScript. *Use case: UI5 JS-to-TS migration, type-safe view controllers, incremental conversion.* (Claude Code)
- [Unreal Engine Skills](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) - Control Unreal Editor from Claude Code via MCP with hundreds of tools across 30+ toolsets covering actors, blueprints, materials, Niagara, Sequencer, widgets, and automation testing, by Epic Games. *Use case: Agentic game development, editor automation, blueprint and level scripting from chat.* (Claude Code)

## Documentation

- [Context7](https://context7.com) - Upstash Context7 MCP server for live documentation lookup that pulls version-specific docs and code examples from source repos. *Use case: Version-correct library lookups, current-API documentation in context, eliminating training-data drift on fast-moving libraries.* (Claude Code)
- [Microsoft Docs](https://learn.microsoft.com) - Access official Microsoft documentation, API references, and code samples for Azure, .NET, Windows, and more. *Use case: Azure SDK lookup, .NET API reference, Windows-specific implementation patterns.* (Claude Code)
- [mintlify](https://mintlify.com) - Build documentation with Mintlify covering MDX conversion, content modification, and automated updates. *Use case: Docs migration to Mintlify, automated docs-as-code workflows, MDX authoring.* (Claude Code)
- [shopify-ai-toolkit](https://shopify.dev) - Shopify's AI Toolkit with 18 development skills for building on the Shopify platform including documentation search, theme development, and app development. *Use case: Shopify theme work, Shopify app development, Liquid-template authoring.* (Claude Code)

## Education and Learning

- [Learn with Coursera](https://www.coursera.org) - Turn any learning intent into a personalized Coursera path — asks topic, familiarity, and preferred format, searches the catalog, and returns the right course, hands-on project, short video, or live roleplay. Requires the Coursera connector for catalog tools. *Use case: Personalized course discovery, skill-path planning, matching learning format to the goal.* (Claude Code, Cowork)
- [Math Olympiad](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad) **`A`** - Solve competition math (IMO, Putnam, USAMO) with adversarial verification that attacks proofs to catch errors self-verification misses. *Use case: Olympiad proof solving, adversarial proof verification, calibrated abstention.* (Claude Code)

## Engineering and Product

- [Engineering](https://claude.com/plugins#engineering) **`A`** - Streamline engineering workflows including standups, code review, architecture decisions, incident response, and technical documentation. *Use case: Engineering standups, architecture-decision documentation, incident post-mortems.* (Cowork)
- [Product Management](https://claude.com/plugins#product-management) **`A`** - Write feature specs, plan roadmaps, synthesize user research, keep stakeholders updated, and stay ahead of competitive landscape. *Use case: Spec authoring, roadmap planning, research synthesis, competitive monitoring.* (Cowork)
- [Product Tracking Skills](https://accoil.com) - AI agent skills that make SaaS products data-ready by scanning codebases, building tracking plans, and generating instrumentation code. *Use case: Product-analytics instrumentation, tracking-plan generation, event-schema design.* (Cowork)

## Finance and Accounting

- [Airwallex AgentOS](https://www.airwallex.com) - Orchestrate global financial infrastructure in plain language including invoices from purchase orders, supplier onboarding, and multi-currency cash position. *Use case: Invoice automation, supplier onboarding, multi-currency cash management.* (Claude Code, Cowork)
- [Carta cap table](https://carta.com/equity-management/cap-table/) - Query cap tables, grants, SAFEs, 409A valuations, and waterfall scenarios via the Carta MCP server. *Use case: fully-diluted ownership breakdowns, 409A expiry checks, SAFE conversion math, exit waterfall modeling.* (Claude Code, Cowork)
- [Carta investors](https://carta.com/fund-management/fund-administration/) - Query fund and investor data, performance benchmarks, regulatory reporting, and AGM decks via the Carta MCP server. *Use case: fund performance benchmarking, Form ADV regulatory reporting, AGM deck generation, portfolio tearsheet PDFs.* (Claude Code, Cowork)
- [Finance](https://claude.com/plugins#finance) **`A`** - Streamline finance and accounting workflows from journal entries and reconciliation to financial statements, variance analysis, audit prep, and month-end close. *Use case: Month-end close, variance analysis, audit prep, journal-entry triage.* (Cowork)
- [Grasp](https://www.grasp-ai.com) - AI analyst platform for investment banking, private equity, and consulting deal work, automating company lookup, buyer/target screening, and market research. *Use case: Build a prioritized list of acquisition targets and buyers for an M&A deal from a natural-language brief.* (Cowork)

## Healthcare and Life Sciences

- [10x Genomics](https://www.10xgenomics.com) - Single-cell and spatial genomics platform whose Cloud MCP exposes analysis data and workflows. *Use case: Pull single-cell sequencing analysis results from the 10x Genomics Cloud into a research workflow.* (Cowork)
- [AdisInsight](https://adisinsight.springer.com) - Springer Nature drug-development pipeline, clinical-trial, and deals intelligence via MCP. *Use case: Check the development stage and trial history of a competitor's drug candidate.* (Cowork)
- [Bio Research](https://claude.com/plugins#bio-research) **`A`** - Connect to preclinical research tools and databases including literature search, genomics analysis, and target prioritization. *Use case: Early-stage life sciences R&D, target discovery, preclinical literature synthesis.* (Cowork)
- [BioRender](https://www.biorender.com) - Create and access scientific illustrations through the BioRender MCP server. *Use case: Build a publication-ready figure illustrating an experimental workflow.* (Cowork)
- [bioRxiv](https://www.biorxiv.org) - Access bioRxiv and medRxiv preprint data. *Use case: Search recent preprints on a specific biology topic before peer review is complete.* (Cowork)
- [Boltz](https://boltz.bio) - Predict structures, screen molecules and proteins, and design binders. *Use case: Protein-structure prediction, molecular screening, binder design.* (Claude Code)
- [ChEMBL](https://www.ebi.ac.uk/chembl) - Query the ChEMBL database of bioactive molecules and drug-discovery data. *Use case: Look up bioactivity and target data for a candidate compound.* (Cowork)
- [Claude for Healthcare](https://claude.com/plugins#claude-for-healthcare) **`A`** - Prior authorization, ICD-10-CM medical coding, clinical-trial protocols, and FHIR development, with CMS Coverage, ICD-10, NPI Registry, Clinical Trials, and PubMed connected. *Use case: Prior-auth drafting, ICD-10-CM coding, clinical-trial protocol and FHIR work.* (Cowork)
- [Clinical Trials](https://clinicaltrials.gov) - ClinicalTrials.gov is the U.S. National Library of Medicine's public registry of FDA-regulated clinical studies. *Use case: Search for actively recruiting trials for a specific condition and location.* (Cowork)
- [Consensus](https://consensus.app) - AI-powered search across peer-reviewed scientific research papers. *Use case: Find and summarize the peer-reviewed evidence on a specific research question.* (Cowork)
- [Cortellis](https://clarivate.com/life-sciences-healthcare/cortellis) - Clarivate's Cortellis platform provides expert-curated global pharmaceutical regulatory intelligence and life-sciences data across 80+ markets. *Use case: Track global regulatory changes and requirements while preparing a drug submission dossier for multiple markets.* (Cowork)
- [Instrument Data to Allotrope](https://www.allotrope.org) - The Allotrope Foundation maintains open data standards, including the Allotrope Simple Model (ASM), for representing laboratory instrument data. *Use case: Convert raw output from a lab instrument into standardized ASM format for downstream data analysis and sharing.* (Cowork)
- [Medidata](https://www.medidata.com) - Clinical-trial platform help and predictive site ranking through Medidata's MCP connector. *Use case: Query Medidata's platform help and predictive site-ranking data while planning enrollment for a clinical trial.* (Cowork)
- [Nextflow](https://www.nextflow.io) - Run nf-core bioinformatics pipelines such as rnaseq, sarek, and atacseq on local or public sequencing data. *Use case: Run an nf-core rnaseq or sarek pipeline against public GEO or SRA sequencing data on a local or cloud cluster.* (Cowork)
- [Open Targets](https://www.opentargets.org) - Drug-target discovery and prioritization across the Open Targets platform. *Use case: Prioritize candidate drug targets for a disease of interest by reviewing genetic association and tractability evidence.* (Cowork)
- [Owkin](https://www.owkin.com) - Interact with AI agents built for biology from Owkin. *Use case: Consult Owkin's AI agents while formulating a hypothesis about a disease mechanism during early-stage drug discovery.* (Cowork)
- [scvi-tools](https://scvi-tools.org) - Deep-learning toolkit for single-cell omics analysis. *Use case: Integrate multiple single-cell RNA-seq datasets and correct for batch effects using an scVI model.* (Cowork)
- [Single-Cell RNA QC](https://www.sc-best-practices.org) - Single-cell best practices is an open community reference, maintained under the scverse ecosystem, documenting current best practices for single-cell omics data analysis, including quality control. *Use case: Filter low-quality cells and doublets from a new single-cell RNA-seq dataset following the documented QC workflow.* (Cowork)
- [Synapse](https://www.synapse.org) - Sage Bionetworks collaborative research data management on Synapse.org. *Use case: Share a processed genomics dataset and its analysis code with collaborators on a multi-institution research project.* (Cowork)
- [ToolUniverse](https://github.com/mims-harvard/ToolUniverse) - A large library of scientific tools and AI agents for research and discovery, from MIMS Harvard. *Use case: Assemble an AI agent that queries multiple biomedical databases and tools to investigate a drug-target hypothesis.* (Cowork)
- [Wiley Scholar Gateway](https://www.wiley.com/en-us/research/scholar-gateway-connect-claude-mistral-ai) - Scholar Gateway is Wiley's MCP connector giving AI assistants grounded access to millions of peer-reviewed Wiley journal articles with citations and DOI links. *Use case: Pull cited, peer-reviewed literature from Wiley journals directly into a grant proposal or literature review draft.* (Cowork)

## Human Resources

- [Human Resources](https://claude.com/plugins#human-resources) **`A`** - Streamline people operations including recruiting, onboarding, performance reviews, compensation analysis, and policy guidance. *Use case: Recruiting workflows, performance-review drafting, compensation benchmarking, HR-policy lookups.* (Cowork)

## Language Servers

- [C# LSP](https://claude.com/plugins#csharp-lsp) **`A`** - C# language server for code intelligence. *Use case: C#/.NET autocomplete, type checking, refactoring support inside Claude Code.* (Claude Code)
- [Clangd LSP](https://claude.com/plugins#clangd-lsp) **`A`** - C/C++ language server (clangd) for code intelligence. *Use case: C/C++ autocomplete, diagnostics, cross-reference navigation.* (Claude Code)
- [Elixir LS](https://github.com/elixir-lsp/elixir-ls) - ElixirLS code intelligence and diagnostics for .ex, .exs, and .heex files. *Use case: Elixir/Phoenix development, HEEx template editing.* (Claude Code)
- [Go LSP (gopls)](https://claude.com/plugins#go-lsp) **`A`** - Go language server for code intelligence and refactoring. *Use case: Go autocomplete, refactor-rename support, package navigation.* (Claude Code)
- [Java LSP (Eclipse JDT.LS)](https://claude.com/plugins#java-lsp) **`A`** - Java language server (Eclipse JDT.LS) for code intelligence. *Use case: Java autocomplete, type checking, JDT-powered refactoring.* (Claude Code)
- [Kotlin LSP](https://claude.com/plugins#kotlin-lsp) **`A`** - Kotlin language server for code intelligence. *Use case: Kotlin autocomplete, Android development, multiplatform Kotlin work.* (Claude Code)
- [Liquid LSP](https://shopify.dev/docs/storefronts/themes/tools/cli) - Integrate an LSP for Shopify Liquid templates via the Shopify CLI theme language server. *Use case: Liquid autocomplete, theme-template diagnostics, Liquid navigation.* (Claude Code)
- [Lua LSP](https://claude.com/plugins#lua-lsp) **`A`** - Lua language server for code intelligence. *Use case: Lua scripting, Neovim configuration, game-engine Lua editing.* (Claude Code)
- [PHP LSP](https://claude.com/plugins#php-lsp) **`A`** - PHP language server (Intelephense) for code intelligence. *Use case: PHP autocomplete, Laravel/Symfony development, type-inference assistance.* (Claude Code)
- [Pyright LSP](https://claude.com/plugins#pyright-lsp) **`A`** - Python language server (Pyright) for type checking and code intelligence. *Use case: Python type checking, autocomplete, strict-mode type inference.* (Claude Code)
- [Ruby LSP](https://claude.com/plugins#ruby-lsp) **`A`** - Ruby language server for code intelligence and analysis. *Use case: Ruby/Rails autocomplete, diagnostic feedback, refactor support.* (Claude Code)
- [Rust Analyzer LSP](https://claude.com/plugins#rust-analyzer-lsp) **`A`** - Rust language server for code intelligence and analysis. *Use case: Rust autocomplete, type inference, refactor-rename support.* (Claude Code)
- [Serena](https://github.com/oraios/serena) - Semantic code analysis MCP server for intelligent code understanding, refactoring, and navigation via language server protocol. *Use case: Cross-language semantic code search, intelligent refactoring, deep code understanding.* (Claude Code)
- [Swift LSP](https://claude.com/plugins#swift-lsp) **`A`** - Swift language server (SourceKit-LSP) for code intelligence. *Use case: Swift/iOS development, SwiftUI autocomplete, Apple-platform code intelligence.* (Claude Code)
- [TypeScript LSP](https://claude.com/plugins#typescript-lsp) **`A`** - TypeScript/JavaScript language server for enhanced code intelligence. *Use case: TS/JS autocomplete, type inference, refactor-rename across files.* (Claude Code)

## Legal

- [AI Governance Legal](https://claude.com/plugins#ai-governance-legal) **`A`** - Triage proposed AI use cases against your registry, run impact assessments across regimes in scope, review vendor AI terms, and keep AI policy current with practice. *Use case: AI use-case triage, AI impact assessments, vendor AI-terms review.* (Cowork)
- [CoCounsel Legal](https://legal.thomsonreuters.com/en/products/cocounsel-legal) - Thomson Reuters Westlaw Deep Research reports with inline, linked citations to Westlaw and Practical Law. *Use case: Get a cited legal research memo answering a specific statutory question.* (Cowork)
- [Commercial Legal](https://claude.com/plugins#commercial-legal) **`A`** - Review vendor agreements, NDAs, and SaaS subscriptions against your playbook, track renewals and cancel-by deadlines, and route escalations to the right approver. *Use case: Vendor-contract review, renewal-deadline tracking, escalation routing.* (Cowork)
- [Corporate Legal](https://claude.com/plugins#corporate-legal) **`A`** - Run M&A diligence at scale with cited tabular review, build disclosure schedules and closing checklists, draft board consents, and track entity compliance across jurisdictions. *Use case: M&A diligence review, disclosure-schedule building, board-consent drafting.* (Cowork)
- [Employment Legal](https://claude.com/plugins#employment-legal) **`A`** - Review hires and terminations for jurisdiction-specific risk, classify workers against the controlling state test, track leave deadlines, and draft policies with state supplements. *Use case: Termination risk review, worker-classification tests, leave-deadline tracking.* (Cowork)
- [IP Legal](https://claude.com/plugins#ip-legal) **`A`** - Run first-pass trademark clearance and freedom-to-operate triage, screen invention disclosures, draft cease-and-desist and DMCA letters, and track registration renewals. *Use case: Trademark clearance, invention-disclosure screening, cease-and-desist drafting.* (Cowork)
- [Law Student](https://claude.com/plugins#law-student) **`A`** - Drill Socratically, brief cases, build outlines, run jurisdiction-tuned bar prep, and grade IRAC practice without writing the work for the student. *Use case: Case briefing, outline building, bar-prep drilling and IRAC grading.* (Cowork)
- [Legal](https://claude.com/plugins#legal) **`A`** - Speed up contract review, NDA triage, and compliance workflows for in-house legal teams including legal-brief drafting and precedent research. *Use case: Contract redlining, NDA triage, precedent research, compliance-workflow drafting.* (Cowork)
- [Legal Builder Hub](https://claude.com/plugins#legal-builder-hub) **`A`** - Find, evaluate, and install community legal skills with a security-review gate before anything lands in your environment. *Use case: Legal-skill discovery, security-gated installation, community-skill evaluation.* (Cowork)
- [Legal Clinic](https://claude.com/plugins#legal-clinic) **`A`** - Set up a clinic, onboard students, run structured intake, track deadlines with malpractice-aware caution, and hand off cases at semester end within ABA Formal Op. 512. *Use case: Clinic setup, structured client intake, deadline tracking and case handoff.* (Cowork)
- [LegalZoom](https://www.legalzoom.com) - AI reviews legal documents for risks and advises when to hire an attorney, with connections to legal professionals. *Use case: Initial legal-document risk review, escalation triggers for human-attorney involvement.* (Claude Code)
- [Litigation Legal](https://claude.com/plugins#litigation-legal) **`A`** - Manage the litigation portfolio — matters, deadlines, holds, demands, and outside counsel — and produce claim charts, chronologies, depo prep, privilege logs, and brief drafts. *Use case: Litigation-portfolio management, claim-chart building, deposition prep.* (Cowork)
- [Privacy Legal](https://claude.com/plugins#privacy-legal) **`A`** - Triage processing activities, generate PIAs, review DPAs as controller or processor, draft DSAR responses within statutory timelines, and monitor policy drift. *Use case: PIA generation, DPA review, DSAR-response drafting.* (Cowork)
- [Product Legal](https://claude.com/plugins#product-legal) **`A`** - Review product launches against your risk calibration, answer is-this-a-problem questions quickly, check marketing copy for claims needing substantiation, and flag launches needing legal review. *Use case: Product-launch legal review, marketing-claim substantiation checks, risk flagging.* (Cowork)
- [Regulatory Legal](https://claude.com/plugins#regulatory-legal) **`A`** - Watch regulatory feeds, diff new rules against your policy library, track comment deadlines and open gaps, and write a weekly regulatory digest. *Use case: Regulatory-feed monitoring, rule-to-policy diffing, comment-deadline tracking.* (Cowork)

## Marketing and Web

- [Adspirer Ads Agent](https://www.adspirer.com) - Cross-platform ad management for Google Ads, Meta Ads, TikTok Ads, and LinkedIn Ads with 91 tools for keyword research, campaign creation, and optimization. *Use case: Cross-platform ad campaign authoring, keyword research, budget optimization across ad networks.* (Cowork)
- [B12](https://www.b12.io) - Generate and edit a B12 website from a brief description using Claude's browser access. *Use case: Generate a small-business website from a short description and then refine it live.* (Cowork)
- [Bright Data](https://brightdata.com) - Web scraping, Google search, structured data extraction, and 60+ MCP tools covering Web Unlocker, SERP API, Web Scraper API, and Browser API. *Use case: Scraping bot-protected sites, structured Google SERP results, large-scale data extraction.* (Claude Code, Cowork)
- [Build with WordPress](https://wordpress.com) - Craft production-grade WordPress sites and applications, from themes and plugins to commerce and deployment. *Use case: WordPress site building, theme and plugin development, commerce setup and deployment.* (Claude Code)
- [Firecrawl](https://www.firecrawl.dev) - Convert websites to LLM-ready markdown or data with scraping, crawling, and structured extraction. *Use case: RAG-corpus building, structured site extraction, AI-friendly web data preparation.* (Claude Code)
- [Marketing](https://claude.com/plugins#marketing) **`A`** - Create content, plan campaigns, and analyze performance across marketing channels with brand-voice consistency and competitor tracking. *Use case: Content authoring, campaign planning, brand-voice enforcement, competitor monitoring.* (Cowork)
- [Nimble](https://nimbleway.com) - Web data toolkit for search, extract, map, crawl, and structured data agents. *Use case: Structured web data harvesting, SERP extraction, site mapping for crawl-aware AI agents.* (Claude Code, Cowork)
- [Postiz](https://postiz.com) - Social media automation CLI for scheduling posts, managing integrations, uploading media, and tracking analytics across 28+ platforms. *Use case: Cross-platform social scheduling, content distribution, analytics rollups for marketers.* (Claude Code, Cowork)
- [SearchFit SEO](https://searchfit.ai) - AI-powered SEO toolkit for auditing websites, planning content strategy, optimizing pages, generating schema markup, and tracking AI visibility. *Use case: SEO audit on any site, content-cluster planning, schema-markup generation, AI-search visibility tracking.* (Cowork)
- [Spotify Ads API](https://ads.spotify.com) - Manage Spotify ad campaigns in natural language to create campaigns, ad sets, and ads, pull reports, and handle OAuth. *Use case: Spotify campaign creation, ad-set management, performance reporting.* (Claude Code)
- [Windsor.ai](https://windsor.ai) - Query marketing, sales, CRM, ecommerce, finance, and analytics data from 325+ business sources. *Use case: Cross-platform marketing data, CRM and analytics querying, GTM data consolidation.* (Claude Code)
- [Zyte Web Data](https://www.zyte.com) - Web scraping skills powered by the Zyte API to scrape sites, generate and run Scrapy spiders, define extraction schemas, and ship to Scrapy Cloud. *Use case: Scrapy spider generation, extraction-schema design, managed crawling at scale.* (Claude Code)

## Observability and Monitoring

- [Amplitude](https://amplitude.com) - Act as an expert analyst to instrument events, discover opportunities, analyze charts, manage experiments, and understand users. *Use case: Product-analytics instrumentation, funnel analysis, experiment management.* (Claude Code)
- [CodSpeed](https://codspeed.io) - Surface benchmarking results, flamegraphs, and performance comparisons via the CodSpeed MCP. *Use case: Benchmark analysis, flamegraph profiling, regression detection.* (Claude Code)
- [Confidence](https://confidence.spotify.com) - Access feature flags, experiments, and migration tools. *Use case: Feature-flag management, experiment analysis, flag migration.* (Claude Code)
- [Dash0](https://www.dash0.com) - Capture Claude Code sessions as OpenTelemetry traces covering tool calls, LLM invocations, token usage, and errors. *Use case: Session tracing, token-usage monitoring, OTel-backed observability.* (Claude Code)
- [Datadog](https://www.datadoghq.com) - Query Datadog logs, metrics, traces, and dashboards through natural conversation via a preconfigured MCP server. *Use case: Log and metric querying, trace investigation, dashboard exploration.* (Claude Code, Cowork)
- [Fullstory](https://www.fullstory.com) - Query behavioral analytics, session replays, and customer-experience insights. *Use case: Session-replay analysis, behavioral analytics, UX-issue discovery.* (Claude Code)
- [Grafana Assistant](https://grafana.com/docs/grafana-cloud/assistant/) - Skills and rules for developing and using the Grafana Assistant app and CLI. *Use case: Grafana Assistant workflows, assistant-CLI automation.* (Claude Code, Cowork)
- [Grafana Cloud MCP](https://grafana.com/products/cloud/) - Hosted MCP server for AI-assisted Grafana Cloud observability with no local installation required. *Use case: Grafana Cloud queries, hosted observability access, zero-install setup.* (Claude Code, Cowork)
- [Grafana MCP](https://github.com/grafana/mcp-grafana) - MCP server for AI-assisted Grafana dashboard, datasource, alerting, and incident management. *Use case: Dashboard authoring, alert-rule management, incident investigation.* (Claude Code)
- [GrowthBook](https://growthbook.io) - Agent skills for the full GrowthBook feature-flag and experimentation lifecycle. *Use case: Feature-flag management, experiment setup, A/B test analysis.* (Claude Code, Cowork)
- [Honeycomb](https://www.honeycomb.io) - Skills, agents, and workflows for Honeycomb observability covering query patterns, production investigations, SLOs, and OpenTelemetry instrumentation. *Use case: Production investigations, SLO management, OTel instrumentation, Beeline migration.* (Claude Code, Cowork)
- [Langfuse](https://langfuse.com) - Add observability for Claude Code covering tracing, prompt management, and evaluation for LLM engineering. *Use case: LLM tracing, prompt versioning, evaluation runs.* (Claude Code, Cowork)
- [Langfuse Observability](https://github.com/langfuse/claude-observability-plugin) - Capture and export traces, spans, and session telemetry from Claude Code to Langfuse. *Use case: LLM monitoring, trace export, session debugging.* (Claude Code)
- [Logfire](https://logfire.pydantic.dev) - Add observability to Python apps with auto-instrumentation for FastAPI, httpx, asyncpg, and SQLAlchemy. *Use case: Python app instrumentation, request tracing, query monitoring.* (Claude Code)
- [LogRocket](https://logrocket.com) - Query session replays, metrics, issues, and user behavior in natural language. *Use case: Frontend session-replay analysis, error triage, user-behavior insight.* (Claude Code)
- [MLflow](https://mlflow.org) - Trace, evaluate, and improve AI agents with MLflow across the instrument, trace, evaluate, and iterate loop. *Use case: Agent tracing, evaluation runs, experiment tracking for LLM apps.* (Claude Code)
- [New Relic](https://newrelic.com) - Observability for Claude Code — investigate APM performance, analyze cloud costs, debug Kubernetes, and write NRQL queries. *Use case: APM performance investigation, NRQL query authoring, Kubernetes debugging.* (Claude Code)
- [PagerDuty Pre-Commit Risk Score](https://www.pagerduty.com) - Score pre-commit diffs against PagerDuty incident history to surface deployment risk before shipping. *Use case: Risk-aware commit gating, incident-history-informed code review, pre-deploy safety checks.* (Claude Code)
- [PostHog](https://posthog.com) - Connect to PostHog to query analytics, manage flags, run A/B tests, track errors, and analyze LLM costs via natural language. *Use case: Product-analytics queries, feature-flag management, A/B test analysis, LLM cost tracking.* (Claude Code)
- [Rootly](https://rootly.com) - Manage incidents end to end covering deploy safety, incident response, on-call management, and retrospectives. *Use case: Incident response, on-call coordination, retrospective authoring.* (Claude Code)
- [Sentry](https://sentry.io) - Error monitoring to access error reports, analyze stack traces, search issues, and debug production errors. *Use case: Production-error triage, stack-trace analysis, issue prioritization from chat.* (Claude Code)
- [Sentry CLI](https://docs.sentry.io/product/cli) - Interact with Sentry from the command line using the Sentry CLI. *Use case: Release management, source-map upload, CLI-driven issue triage.* (Claude Code)
- [SigNoz](https://signoz.io) - Open-source observability — MCP setup, docs, queries, dashboards, and alerts. *Use case: Set up a dashboard with alerts to track application latency and error rates.* (Cowork)

## Output Styles

- [Explanatory Output Style](https://claude.com/plugins#explanatory-output-style) **`A`** - Adds educational insights on implementation choices and codebase patterns to mimic the deprecated Explanatory style. *Use case: Learning-mode coding, teaching-team-members workflow, explanatory commenting style.* (Claude Code)
- [Learning Output Style](https://claude.com/plugins#learning-output-style) **`A`** - Interactive learning mode that requests meaningful code contributions at key decision points. *Use case: Pair-programming-style learning, deliberate-practice coding, junior-developer ramp.* (Claude Code)

## Payments and Billing

- [Circle](https://www.circle.com) - Ship stablecoin apps faster with USDC payments, cross-chain transfers, wallets, and smart contracts, plus an MCP server. *Use case: USDC payment integration, cross-chain transfers, programmable-wallet development.* (Claude Code)
- [Mercado Pago](https://www.mercadopago.com) - Integrate payments, webhooks, test setup, and review, pulling endpoints live from the official MCP. *Use case: Payment-flow integration, webhook setup, checkout testing.* (Claude Code)
- [RevenueCat](https://www.revenuecat.com) - Manage RevenueCat in-app purchase backend directly from your development workflow. *Use case: Subscription product configuration, entitlement management, IAP backend tuning.* (Claude Code)
- [Stripe](https://stripe.com) - Development plugin for payments, billing, subscriptions, and Stripe API integration. *Use case: Stripe API exploration, payment-flow development, subscription-product configuration.* (Claude Code)
- [SumUp](https://www.sumup.com) - Integrate payments across terminal and online checkout, covering POS apps, online checkout, and Cloud API reader control. *Use case: POS app development, online checkout, card-reader control.* (Claude Code)

## Platforms and SaaS

- [Amazon Location Service](https://aws.amazon.com/location) - Integrate Amazon Location Service for maps, geocoding, routing, and geospatial features with authentication and SDKs. *Use case: Maps integration in apps, geocoding flows, routing/directions APIs.* (Claude Code)
- [Appwrite](https://appwrite.io) - Use SDK skills, MCP servers, and deployment commands for the open-source backend platform. *Use case: Backend-as-a-service setup, Appwrite SDK development, function deployment.* (Claude Code)
- [Base44](https://base44.com) - Build and deploy full-stack apps with CLI project management and JavaScript/TypeScript SDK development. *Use case: Full-stack app scaffolding, Base44 SDK development, deployment.* (Claude Code, Cowork)
- [Box](https://www.box.com) - Search files, organize folders, collaborate with teams, and use Box AI to answer questions, summarize documents, and extract data. *Use case: Enterprise file management, Box AI document Q&A, folder organization automation.* (Claude Code, Cowork)
- [Dropbox](https://www.dropbox.com) - Search, organize, and save generated content to Dropbox, create sharing links, and ground Claude's answers in your files — respecting your existing Dropbox permissions. *Use case: File search across Dropbox, saving generated artifacts back to Dropbox, share-link creation, grounding answers in stored documents.* (Claude Code, Cowork)
- [Expo](https://expo.dev) - Official Expo skills for building, deploying, upgrading, and debugging React Native apps with Expo. *Use case: Expo app development, EAS build configuration, React Native debugging.* (Claude Code)
- [Fastly Agent Toolkit](https://www.fastly.com) - Fastly development tools and platform skills for VCL, edge functions, and CDN configuration. *Use case: Fastly edge function development, VCL authoring, CDN configuration.* (Claude Code, Cowork)
- [Laravel Boost](https://laravel.com) - Laravel MCP server for intelligent Artisan commands, Eloquent queries, routing, migrations, and framework-specific code generation. *Use case: Laravel app development, Eloquent query authoring, Artisan command exploration.* (Claude Code)
- [Lovable](https://lovable.dev) - Build, iterate on, deploy, and manage apps with the official MCP server and build and database commands. *Use case: App generation, iterative editing, deploy and publish with credit safety.* (Claude Code)
- [Mapbox](https://www.mapbox.com) - Build location-aware apps with skills and MCP servers covering geospatial tools, style management, and web and mobile patterns. *Use case: Maps integration, custom style management, geospatial app development.* (Claude Code)
- [Postman](https://www.postman.com) - Full API lifecycle management to sync collections, generate client code, discover APIs, run tests, and create requests. *Use case: API exploration, client SDK generation from collections, API test authoring.* (Claude Code)
- [Zapier](https://zapier.com) - Connect 8,000+ apps to your AI workflow by discovering, enabling, and executing Zapier actions directly from your client. *Use case: Cross-app automation, no-code integration bridging, executing actions across SaaS tools without writing each integration.* (Claude Code, Cowork)

## Productivity and Documents

- [Carbone](https://carbone.io) - Official Carbone templating reference covering tags, loops, conditions, formatters, and all output formats including DOCX, XLSX, PPTX, and PDF. *Use case: Document-template authoring, report generation, multi-format document output.* (Claude Code, Cowork)
- [Notion](https://www.notion.so) - Search pages, create and update documents, and manage databases in your workspace. *Use case: Notion doc authoring, database management, knowledge-base search.* (Claude Code)
- [PDF Viewer](https://claude.com/plugins#pdf-viewer) **`A`** - View, annotate, and sign PDFs in a live interactive viewer with markup, form-fill, approval stamps, and signature placement. *Use case: Contract review with annotations, PDF form filling, signature workflows, approval stamping.* (Cowork)
- [Productivity](https://claude.com/plugins#productivity) **`A`** - Manage tasks, plan your day, and build memory of important work context by syncing with calendar, email, and chat. *Use case: Daily planning, task management, cross-tool context building, calendar/email/chat synthesis.* (Cowork)
- [Project Artifact](https://claude.com/plugins#project-artifact) **`A`** - Generate and publish a living project status page as a shareable claude.ai artifact, redeploying the same URL with each refresh. *Use case: Stakeholder-facing project status, living progress reports, delta-only updates.* (Claude Code)
- [Receipts](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/receipts) - A personal Claude Code impact report for justifying usage to a manager or a self-review, covering what you shipped and which projects it went to. *Use case: Usage self-review, manager-facing impact summary, per-project contribution report.* (Claude Code)

## Project Management

- [Asana](https://asana.com) - Integration to create and manage tasks, search projects, update assignments, and track progress. *Use case: Task creation from chat, project-progress reporting, assignment management.* (Claude Code, Cowork)
- [Atlassian](https://www.atlassian.com) - Connect to Jira and Confluence to search and create issues, access docs, manage sprints, and integrate development workflows. *Use case: Jira ticket management, Confluence doc search, sprint planning from chat.* (Claude Code, Cowork)
- [GitHub](https://github.com) - Official GitHub MCP server for repository management including issues, PRs, code review, and GitHub API access. *Use case: PR management, issue creation and triage, code search across repos.* (Claude Code, Cowork)
- [GitLab](https://gitlab.com) - Integration for repositories, merge requests, CI/CD pipelines, issues, and wikis with full DevOps lifecycle access. *Use case: GitLab MR workflows, CI/CD pipeline debugging, GitLab wiki management.* (Claude Code)
- [Linear](https://linear.app) - Integration to create issues, manage projects, update statuses, search workspaces, and streamline development workflow. *Use case: Issue creation, sprint management, workspace search.* (Claude Code, Cowork)
- [monday.com](https://monday.com) - Official plugin to manage boards, items, docs, and forms across work management, CRM, dev, service, and campaigns with full read/write via OAuth. *Use case: Board and item management, work-management automation, form and doc handling.* (Cowork)

## Security

- [42Crunch API Security Testing](https://42crunch.com) - Audit OpenAPI specs, detect OWASP API vulnerabilities including BOLA/BFLA, and apply AI-powered fixes in an audit-scan-remediate loop. *Use case: OpenAPI security audit, BOLA/BFLA detection, API-spec remediation.* (Claude Code)
- [Auth0](https://auth0.com) - Add authentication to any app by detecting the framework and scaffolding login, logout, sessions, and protected routes. *Use case: Auth0 SDK integration, login and session setup, protected-route scaffolding.* (Claude Code, Cowork)
- [AWS Agents for DevSecOps](https://aws.amazon.com/security/) - Investigate incidents, review code, run UAT, scan for vulnerabilities, and run pen tests with AWS DevOps and Security Agents. *Use case: Incident investigation, security code review, automated penetration testing.* (Claude Code)
- [Claude Security](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-security) - Deep vulnerability scanning of your own code run entirely inside a Claude Code session at a chosen effort tier, with every finding challenged before it is reported. *Use case: In-session security scan of a codebase, effort-tiered vulnerability review, false-positive-resistant findings.* (Claude Code, Cowork)
- [CrowdSec](https://www.crowdsec.net) - Install, configure, operate, and debug CrowdSec across cscli, LAPI/CAPI, the hub, bouncers, and WAF/AppSec on bare-metal, Docker, and Kubernetes. *Use case: CrowdSec deployment, bouncer configuration, WAF and AppSec debugging.* (Claude Code)
- [CrowdStrike Falcon Foundry](https://www.crowdstrike.com) - Build cybersecurity apps on the Falcon platform covering UI, collections, functions, workflows, and API integration. *Use case: Falcon Foundry app development, security-workflow authoring, collections design.* (Claude Code)
- [Duende](https://duendesoftware.com) - Implement OAuth/OIDC, IdentityServer, token management, ASP.NET Core auth, and BFF patterns for secure identity. *Use case: IdentityServer setup, OIDC flow design, BFF authentication.* (Claude Code)
- [Endor Labs](https://www.endorlabs.com) - Set up endorctl and use Endor Labs to scan, prioritize, and fix security risks across the software supply chain. *Use case: SCA scanning, supply-chain risk prioritization, dependency-vulnerability remediation.* (Claude Code)
- [JFrog](https://jfrog.com) - Use the JFrog Platform for Artifactory repos, security findings and exposures, Catalog package safety, and administration. *Use case: Artifact management, dependency-exposure triage, package-safety checks.* (Claude Code)
- [NightVision](https://nightviz.ai) - Run DAST and API discovery to find exploitable vulnerabilities in web applications and REST APIs. *Use case: Dynamic application security testing, API discovery, exploitable-vuln detection.* (Claude Code)
- [Security Guidance](https://claude.com/plugins#security-guidance) **`A`** - Security hook that warns about command injection, XSS, and unsafe code patterns when editing files. *Use case: In-editor security guardrails, OWASP-pattern detection, real-time vulnerability prevention.* (Claude Code)
- [Semgrep](https://semgrep.dev) - Catch security vulnerabilities in real-time and guide secure code authoring. *Use case: SAST scanning, custom-rule authoring, secure-by-default code generation.* (Claude Code)
- [Sonatype Guide](https://www.sonatype.com) - MCP for supply chain intelligence and dependency security analysis with vulnerability detection and version recommendations. *Use case: Dependency vulnerability scanning, version-recommendation lookup, supply-chain risk analysis.* (Claude Code)
- [StackHawk API](https://docs.stackhawk.com/ai-security) - Query the StackHawk platform API for security-posture reporting, findings analysis, and application management. *Use case: Security-posture reporting, findings triage, app inventory queries.* (Claude Code, Cowork)
- [StackHawk HawkScan](https://www.stackhawk.com) - Configure, run, and interpret HawkScan DAST results, generating stackhawk.yml configs and turning findings into prioritized fix tasks. *Use case: DAST scan setup, stackhawk.yml generation, security-finding remediation planning.* (Claude Code, Cowork)
- [Vanta](https://www.vanta.com) - Connect Claude to Vanta's security and compliance platform via the Vanta MCP server to list failing compliance tests and get test-specific remediation. *Use case: Compliance test triage, SOC 2/ISO remediation workflows, security-control gap analysis from chat.* (Claude Code, Cowork)
- [WorkOS](https://workos.com) - Wire up AuthKit, SSO, Directory Sync, RBAC, Vault, Audit Logs, and migrations. *Use case: Enterprise SSO setup, SCIM directory sync, RBAC implementation.* (Claude Code)
- [Zscaler](https://www.zscaler.com) - Run zero-trust security operations and policy management via an MCP server. *Use case: Zero-trust policy management, security-posture queries, Zscaler operations.* (Claude Code)

## Skills Authoring

- [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) - Create MCP Apps with the MCP Apps SDK. *Use case: MCP app scaffolding, interactive MCP UI development, MCP Apps SDK usage.* (Claude Code)
- [MCP Server Dev](https://claude.com/plugins#mcp-server-dev) **`A`** - Design and build MCP servers covering deployment (HTTP, MCPB, local), tools, auth, and interactive apps. *Use case: MCP server scaffolding, OAuth flow design, MCPB packaging.* (Claude Code)
- [MCP Tunnels](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-tunnels) **`A`** - Connect Claude to a private MCP server through an Anthropic MCP tunnel, including the Docker Compose quickstart. *Use case: Private MCP server access, tunnel setup, secure MCP proxying.* (Claude Code)
- [Plugin Developer Toolkit](https://claude.com/plugins#plugin-developer-toolkit) **`A`** - Plugin development toolkit with 7 expert skills for hooks, MCP, commands, agents, validation, and best practices. *Use case: Plugin scaffolding, validation against the plugin schema, marketplace authoring.* (Claude Code)
- [Skill Creator](https://claude.com/plugins#skill-creator) **`A`** - Create, improve, and measure skills covering creation, updating, evaluation, and benchmarking performance. *Use case: Skill authoring, skill-performance evaluation, benchmarking before publishing.* (Claude Code)

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

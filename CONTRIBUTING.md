# Contributing

This list tracks every plugin available in [Anthropic's official Claude Plugins catalog](https://claude.com/plugins) — plugins for **Claude Code** (developer workflows) and **Cowork** (knowledge-work agentic workspace). Contributions welcome.

> **This is a free, independent, community-maintained project. Not affiliated with, endorsed by, or sponsored by Anthropic PBC.** "Claude," "Claude Code," and "Cowork" are trademarks of Anthropic PBC. Each plugin is the property of its respective owner. Contributions are made under the project's [CC0](LICENSE) license — public domain dedication.

## What You Can Contribute

### New Plugins
When Anthropic publishes new plugins to claude.com/plugins, submit a PR adding them to the appropriate category with a description and use case.

### Improved Descriptions
If a description or use case is missing detail or could be more helpful, submit a PR with a better one.

### Category Corrections
If a plugin is in the wrong category, submit a PR moving it.

### Field Reports
Tested a plugin and have real-world notes? Add a brief field report below the plugin entry:

```markdown
- [Plugin Name](https://link) - Description. *Use case: ...*
  > **Field report:** One paragraph on what worked, what didn't, what surprised you. Be specific.
```

## Entry format

Each entry must follow this exact format and live in the appropriate category, alphabetized:

```
- [Plugin Name](https://link) - One-sentence description ending with a period. *Use case: Concrete usage scenario, second scenario.* (Surface)
```

- **Surface** is one of: `(Claude Code)`, `(Cowork)`, `(Claude Code, Cowork)` — a plugin is tagged for every surface it appears on (the official `claude-plugins-official` manifest is the Claude Code surface; the in-app Cowork plugin catalog is the Cowork surface)
- Anthropic-verified plugins get a trailing **`A`** marker before the surface tag

```
- [Plugin Name](https://link) **`A`** - Description. *Use case: ...* (Claude Code)
```

## Guidelines

- One PR per change unless closely related.
- Keep descriptions concise — one sentence for the description, one for the use case.
- Use cases should be specific and practical, not marketing copy.
- Only add plugins that are publicly listed at [claude.com/plugins](https://claude.com/plugins). For general MCP servers not yet packaged as plugins, see [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers).
- Maintain alphabetical order within categories.
- Don't include install counts — they're volatile. The "Last updated" header is the snapshot.

### Removing vs. re-tagging

A plugin is **removed** only when it disappears from *every* surface it was listed on. If it merely leaves one surface but remains on another — e.g. it drops out of the official `claude-plugins-official` manifest but is still live in the Cowork catalog — **re-tag** it to the surface(s) where it survives rather than deleting the entry. Absence from a single surface is a surface change, not a delisting. (This mirrors the two-surface removal rule used in [awesome-claude-connectors](https://github.com/rdmgator12/awesome-claude-connectors).)

## Weekly Updates

This list is updated weekly to stay in sync with claude.com/plugins. If you notice plugins added to the directory that aren't listed here, please open an issue or PR.

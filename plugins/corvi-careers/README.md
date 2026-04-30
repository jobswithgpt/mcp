# Corvi Careers Plugin

Corvi Careers lets Codex and other MCP-capable clients search jobs through the public Corvi Careers MCP server.

## Install in Codex

Install **Corvi Careers** from the Codex plugin marketplace, then start a conversation and ask for job searches, job summaries, or role comparisons.

Example prompts:

- Find software engineering jobs near San Francisco.
- Search remote AI engineering roles.
- Find senior backend roles posted in the last 30 days.
- Summarize this job posting and list the key requirements.

## What It Can Do

The plugin can:

- Search job listings by keyword, title, company, location, job type, seniority, recency, and related filters
- Resolve city or region names into Corvi Careers location identifiers
- Summarize job results with title, company, location, level, type, posting date, salary when available, and application URL

## Manual MCP Setup

Manual setup is only needed if your MCP client does not install plugins through the Codex marketplace.

### Endpoint

Use the Streamable HTTP MCP endpoint:

```text
https://corvi.careers/mcp
```

For clients that expect a local stdio MCP server, use `mcp-remote`:

```json
{
  "mcpServers": {
    "corvi-careers": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://corvi.careers/mcp"
      ]
    }
  }
}
```

## Plugin Contents

This plugin includes:

- `.codex-plugin/plugin.json` for plugin metadata
- `.mcp.json` for MCP server configuration
- `skills/corvi-careers/SKILL.md` for job-search workflow guidance
- `assets/` for plugin icon and logo assets

## Marketplace Entry

Catalog maintainers can publish the plugin directory as:

```text
plugins/corvi-careers
```

The marketplace entry should point to:

```json
{
  "name": "corvi-careers",
  "source": {
    "source": "local",
    "path": "./plugins/corvi-careers"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

## MCP Tools

The MCP server currently exposes:

- `location_autocomplete` - resolve location names into Corvi Careers location identifiers
- `search_jobs` - search job listings by keywords, locations, company, title, job type, level, recency, and related filters

Typical workflow:

1. Call `location_autocomplete` for a city or region.
2. Use the returned `geonameid` with `search_jobs`.
3. Present results with title, company, location, level, type, posting date, salary when available, and application URL.

## Test Commands

Initialize the MCP server:

```sh
curl -X POST -N \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  https://corvi.careers/mcp \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"0.1.0"}}}'
```

List tools:

```sh
curl -X POST -N \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  https://corvi.careers/mcp \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```

Search a location:

```sh
curl -X POST -N \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  https://corvi.careers/mcp \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"location_autocomplete","arguments":{"query":"San Francisco","limit":3,"include_country":true}}}'
```

## Support

Website: https://corvi.careers

Support: support@corvi.careers

Repository: https://github.com/jobswithgpt/mcp

License: MIT

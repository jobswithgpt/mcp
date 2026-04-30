# Corvi Careers MCP Marketplace

This repository publishes the **Corvi Careers** Codex plugin marketplace entry and plugin package.

Corvi Careers lets Codex and other MCP-capable clients search jobs through the public Corvi Careers MCP server.

## Install in Codex

Add this repository as a Codex plugin marketplace/catalog source:

```text
https://github.com/jobswithgpt/mcp
```

Then install **Corvi Careers** from the Codex plugin marketplace UI.

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/corvi-careers/
```

The marketplace file registers the Corvi Careers plugin and points Codex to:

```text
./plugins/corvi-careers
```

## Direct MCP Endpoint

For MCP clients that support remote Streamable HTTP directly:

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

## Plugin Documentation

See the plugin README:

```text
plugins/corvi-careers/README.md
```

## Support

Website: https://corvi.careers

Support: support@corvi.careers

License: MIT

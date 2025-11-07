# MCP Create Server

[![NPM version](http://img.shields.io/npm/v/mcp.svg?style=flat-square)](https://www.npmjs.org/package/mcp)

A dynamic MCP server management service that creates, runs, and manages Model Context Protocol (MCP) servers dynamically. This service itself functions as an MCP server and launches/manages other MCP servers as child processes, enabling a flexible MCP ecosystem.

<a href="https://glama.ai/mcp/servers/@jobswithgpt/mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@jobswithgpt/mcp/badge" alt="jobswithgpt MCP server" />
</a>

## Key Features

...

### Configuring Claude Desktop as an MCP Client
1. If you have PRO account, you can directly add as hosted MCP connector (https://jobswithgpt.com/mcp)
2. If you have a free account, you can add a proxy to the hosted MCP.
#### 1. Prerequisites

* **Claude Desktop Free** (installed)
* **Node.js ≥ 18** (for `npx`)


#### 2. Create or Edit Claude Config

Locate (or create) the Claude Desktop config file:

* **macOS:**
  `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows:**
  `%APPDATA%\Claude\claude_desktop_config.json`

---

#### 3. Add Local Proxy Definition

Insert this JSON:

```json
{
  "mcpServers": {
    "jobswithgpt": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://jobswithgpt.com/mcp"
      ]
    }
  }
}
```

---

#### 4. Restart Claude Desktop

Quit Claude Desktop completely and reopen it.

Your new server **jobswithgpt** should appear in the **paperclip menu** under Tools.


### OpenAI instructions
OpenAI can directly use the server hosted MCP server (https://jobswithgpt.com/mcp)

```python
import asyncio
from agents import Agent, Runner
from agents.mcp.server import MCPServerStreamableHttp
import json

MCP_URL = "https://jobswithgpt.com/mcp"  # your FastMCP streamable HTTP endpoint

async def main():
    async with MCPServerStreamableHttp(params={"url": MCP_URL}, name="jobswithgpt") as server:
        agent = Agent(
            name="jobs-mcp-local",
            mcp_servers=[server],
            instructions=(
                "Use the MCP server tools. First call location_autocomplete to get a geonameid "
                "for 'Seattle', then call search_jobs with keywords=['python'] and that geonameid."
            ),
        )
        res = await Runner.run(agent, "Find machine learning jobs in san francisco.")
        print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```
#### Example output
```
Here are some Python developer job opportunities in San Francisco:

1. Software Engineer - Backend, Product Engineering at Baton
   [Apply here](https://job-boards.greenhouse.io/baton/jobs/4011483007)

2. Senior Backend Engineer at Stellic
   [Apply here](https://job-boards.greenhouse.io/stellic/jobs/4705805007)

3. Software Engineer - Backend at Julius AI
   [Apply here](https://jobs.ashbyhq.com/julius/75f8ef44-4fa4-46fa-b416-c7b697078eca)
etc
```
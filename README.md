### Configuring Claude Desktop as an MCP Client
1. Install uv with python version > 3.12 for your OS.
2. Install the mcp server - easy!
```
uv run mcp install server.py
```
```
mcp % uv run mcp install server.py
Using CPython 3.12.3
Creating virtual environment at: .venv
Installed 27 packages in 23ms
[06/02/25 11:25:38] INFO     Added server 'jobswithgpt_search' to  claude.py:143
                             Claude config                                      
                    INFO     Successfully installed                   cli.py:504
                             jobswithgpt_search in Claude app                   
mcp % 
```
```
Example query: "Find ML jobs in SF"
```

### OpenAI instructions
OpenAI can directly use the server hosted MCP server (https://jobswithgpt.com/mcp/)

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

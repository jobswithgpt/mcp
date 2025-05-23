## Summary
You can connect to MCP server at `https://jobswithgpt.com/mcp/` to both Claude Desktop (as a local MCP client) and the OpenAI Responses API (as a remote MCP tool).  
---

### Configuring Claude Desktop as an MCP Client  
Paste under `"mcpServers"`:

```json
{
  "mcpServers": {
    "jobswithgpt": {
      "command": "curl",
      "args": [
        "-X", "POST",
        "-H", "Content-Type: application/json",
        "https://jobswithgpt.com/mcp/"
      ]
    }
  }
}

### OpenAI instructions

```python
import openai

client = openai.OpenAI()

resp = client.responses.create(
    model="gpt-4.1-mini",
    tools=[
        {
            "type": "mcp",
            "server_label": "jobswithgpt",
            "server_url": "https://jobswithgpt.com/mcp/",
            "require_approval": {
                "never": {
                    "tool_names": ["search_jobs"]
                }
            }
        },
    ],
    input="find jobs for python devs in sf"
)

print(resp.output_text)
```
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

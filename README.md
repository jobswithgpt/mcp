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

### OpenAI instructions
OpenAI can directly use the server hosted MCP server (https://jobswithgpt.com/mcp/)

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

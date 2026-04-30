# Corvi Careers for OpenClaw

Corvi Careers is an OpenClaw skill for searching remote and onsite jobs through the public Corvi Careers MCP server.

## Install MCP Server

Register the Corvi Careers MCP endpoint:

```sh
openclaw mcp set corvi-careers '{"url":"https://corvi.careers/mcp"}'
```

If your OpenClaw runtime needs a local stdio MCP process, use `mcp-remote`:

```sh
openclaw mcp set corvi-careers '{"command":"npx","args":["-y","mcp-remote@latest","https://corvi.careers/mcp"]}'
```

Check the saved definition:

```sh
openclaw mcp show corvi-careers --json
```

## What It Provides

- Job search by keyword, title, company, location, job type, seniority, recency, and related filters
- Location autocomplete for city and region searches
- Job result summaries with title, company, location, level, type, posting date, salary when available, and application URL

## Example Prompts

- Find software engineering jobs near San Francisco.
- Search remote AI engineering roles.
- Find senior backend roles posted in the last 30 days.
- Summarize this job posting and list the key requirements.

## MCP Endpoint

```text
https://corvi.careers/mcp
```

## Support

Website: https://corvi.careers

Support: support@corvi.careers

Repository: https://github.com/jobswithgpt/mcp

License: MIT


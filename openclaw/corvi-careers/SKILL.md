---
name: corvi-careers
description: Search jobs and summarize job postings through the Corvi Careers MCP server.
---

# Corvi Careers

Use this skill when the user wants to search for jobs, compare roles, explore career opportunities, or summarize job postings.

## Setup

Before using this skill, add the Corvi Careers MCP server to OpenClaw:

```sh
openclaw mcp set corvi-careers '{"url":"https://corvi.careers/mcp"}'
```

If the active OpenClaw runtime does not support remote MCP servers directly, use the stdio wrapper:

```sh
openclaw mcp set corvi-careers '{"command":"npx","args":["-y","mcp-remote@latest","https://corvi.careers/mcp"]}'
```

Confirm the server is registered:

```sh
openclaw mcp show corvi-careers --json
```

## Workflow

1. Use `location_autocomplete` to resolve location names such as cities, regions, or metro areas.
2. Use `search_jobs` with returned `geonameid` values and the user's job-search constraints.
3. Ask for missing constraints only when they materially affect the result, such as remote preference, location, role type, seniority, keywords, company, or recency.
4. Present job results with title, company, location, level, type, posting date, salary when available, and application URL.
5. When summarizing a posting, focus on responsibilities, required qualifications, preferred qualifications, compensation when available, and likely fit considerations.
6. Do not invent job details that are not returned by the MCP tools.

## Available MCP Tools

- `location_autocomplete` - resolve location names into Corvi Careers location identifiers.
- `search_jobs` - search job listings by keywords, locations, companies, titles, job types, levels, categories, distance, recency, and query text.

## Example Requests

- Find software engineering jobs near San Francisco.
- Search remote AI engineering roles.
- Find senior backend roles posted in the last 30 days.
- Summarize this job posting and list the key requirements.


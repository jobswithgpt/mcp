from typing import Any, List, Dict
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("jobswithgpt_search")

API_URL = "https://jobswithgpt.com/api/search/"

@mcp.tool()
async def search(
    keywords: List[str],
    locations: List[Dict[str, Any]],
    titles: List[str],
    distance: int,
    page: int
) -> Dict[str, Any]:
    """
    Proxy to JobsWithGPT search API.
    Args:
        keywords: list of keyword strings
        locations: list of dicts with keys name, admin1_code, country_code, remote (bool)
        titles: list of title strings
        distance: integer distance in meters
        page: integer page number
    Returns:
        Parsed JSON response from JobsWithGPT API
    """
    payload = {
        "keywords": keywords,
        "locations": locations,
        "titles": titles,
        "distance": distance,
        "page": page
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json=payload, timeout=30.0)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")

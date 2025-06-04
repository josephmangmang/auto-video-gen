import os
from typing import List, Optional

import requests


def find_gifs(lines: List[str], api_key: Optional[str] = None) -> List[Optional[str]]:
    """Search Giphy for gifs matching each line.

    Args:
        lines: List of script lines.
        api_key: Giphy API key. If not provided, environment variable GIPHY_API_KEY is used.

    Returns:
        List of gif URLs (mp4 format if available). None if search failed.
    """
    api_key = api_key or os.getenv("GIPHY_API_KEY")
    if not api_key:
        return [None for _ in lines]

    urls = []
    for line in lines:
        params = {
            "api_key": api_key,
            "q": line,
            "limit": 1,
            "rating": "pg",
        }
        try:
            resp = requests.get("https://api.giphy.com/v1/gifs/search", params=params, timeout=10)
            data = resp.json()
            gif = data.get("data", [{}])[0]
            mp4_url = gif.get("images", {}).get("original", {}).get("mp4")
            urls.append(mp4_url)
        except Exception:
            urls.append(None)
    return urls

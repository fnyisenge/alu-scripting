#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced.project:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=5
        )
    except requests.RequestException:
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    if not posts:
        print("None")
        return

    for post in posts:
        print(post.get("data", {}).get("title"))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        top_ten(sys.argv[1])

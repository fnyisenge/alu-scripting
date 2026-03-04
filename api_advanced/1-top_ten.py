#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom"}
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    # If subreddit does not exist or request fails
    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data")

    # If no data or no posts
    if not data or not data.get("children"):
        print("None")
        return

    for post in data.get("children"):
        print(post.get("data").get("title"))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        top_ten(sys.argv[1])

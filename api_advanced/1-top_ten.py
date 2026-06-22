#!/usr/bin/python3
"""Query Reddit API and return subreddit subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/reddit_user)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)

    except Exception:
        return 0

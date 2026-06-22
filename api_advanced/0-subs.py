#!/usr/bin/python3
"""Returns the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API and return subscriber count."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:reddit.api:v1.0 (by /u/user)"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            return 0

        return response.json().get("data").get("subscribers", 0)

    except Exception:
        return 0

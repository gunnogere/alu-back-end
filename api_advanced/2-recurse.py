#!/usr/bin/python3
"""Recursively retrieves all hot article titles from a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot posts for a subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/reddit_user)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    hot_list.extend(
        post.get("data", {}).get("title")
        for post in posts
    )

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)

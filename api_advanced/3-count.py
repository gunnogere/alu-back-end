#!/usr/bin/python3
"""Recursively counts keywords in hot Reddit article titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print counts of keywords found in hot article titles."""
    if counts is None:
        counts = {}

        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)

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
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title_words = post.get("data", {}).get(
            "title", ""
        ).lower().split()

        for title_word in title_words:
            if title_word in counts:
                counts[title_word] += 1

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))

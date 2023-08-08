#!/usr/bin/python3

"""This script contains a function that queries the Reddit API
and returns the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    with requests.get(url, allow_redirects=False) as resp:
        if resp.status_code == 200:
            subscribers = resp.json().get('data').get('subscribers')
        else:
            subscribers = 0
    return subscribers

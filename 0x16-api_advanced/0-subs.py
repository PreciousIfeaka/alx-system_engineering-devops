#!/usr/bin/python3

"""This script contains a function that queries the Reddit API
and returns the number of subscribers of a subreddit
"""

import requests
import sys


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    with requests.get(url, allow_redirects=False) as resp:
        if resp.status_code == 200:
            subscribers = resp.json().get('data').get('subscribers')
            return (subscribers)
        else:
            return (0)

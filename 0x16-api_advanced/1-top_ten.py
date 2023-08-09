#!/usr/bin/python3

"""This script queries the reddit api and prints
the titles of the first 10 host posts for a given subreddit
"""

import requests
import sys


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    with requests.get(url, allow_redirects=False,
                      params={'limit': 10}) as resp:
        if resp.status_code == 200:
            s_list = resp.json().get('data').get('children')
            for key in s_list:
                topic = key.get('data').get('title')
                print(topic)
        else:
            print(None)

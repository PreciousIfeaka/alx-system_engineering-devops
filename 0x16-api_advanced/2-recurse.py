#!/usr/bin/python3

"""This script queries the reddit api and prints
the titles of the first 10 host posts for a given subreddit
"""

import sys
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    with requests.get(url, params=params, allow_redirects=False) as resp:
        if resp.status_code == 200:
            nex_t = resp.json().get('data').get('after')
            if nex_t is not None:
                after = nex_t
                recurse(subreddit, hot_list)
            s_list = resp.json().get('data').get('children')

            for topic in s_list:
                hot_list.append(topic.get('data').get('title'))
            return hot_list
        else:
            return None
        """The whole idea of this algorithm is to recursively
        loop though each pages(as a result of pagination) and at the
        same time, use a for loop to obtain the titles of the hot topics
        """

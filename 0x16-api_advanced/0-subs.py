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
            return (subscribers)
        else:
            return (0)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
    listed for a given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'app'}
    params = {'limit': 9}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != requests.codes.ok:
        print(None)
        return
    response = response.json()
    if "data" in response and "children" in response.get("data"):
        for post in response.get("data").get("children"):
            print(post["data"]["title"])
    else:
        print(None)

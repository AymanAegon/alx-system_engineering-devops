#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'YourAppName/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    response = response.json()
    if "data" in response and "subscribers" in response["data"]:
        return response["data"]["subscribers"]
    return 0
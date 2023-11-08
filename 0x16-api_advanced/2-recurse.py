#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of
    all hot articles for a given subreddit """
    header = {'User-Agent': 'app'}
    url = 'http://www.reddit.com/r/{}/hot.json'
    url = url.format(subreddit)
    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=header).json()
    if "data" in response and "children" in response.get("data"):
        posts = response.get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if len(hot_list) == 0:
            return None
        if 'after' in response['data']:
            return recurse(subreddit, hot_list, response['data']['after'])
        return hot_list
    else:
        return None

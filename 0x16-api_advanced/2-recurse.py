#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after_party=None):
    """ returns a list containing the titles of
    all hot articles for a given subreddit """
    header = {'User-Agent': 'fake'}
    param = {'after': after_party}
    url = 'http://www.reddit.com/r/{}/hot.json?after={}'
    url = url.format(subreddit, after_party)
    r = requests.get(url, headers=header)
    if r.status_code == requests.codes.ok:
        x = r.json().get('data').get('children')
        after_party = r.json().get('data').get('after')
        for page in x:
            hot_list.append(page.get('data').get('title'))
        if len(hot_list) == 0:
            return None
        if after_party is None:
            return hot_list
        return recurse(subreddit, hot_list, after_party)
    else:
        return None
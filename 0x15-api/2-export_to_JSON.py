#!/usr/bin/python3
"""
export data in the json format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    s = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user = requests.get(s).json()
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    obj = {}
    arr = []
    for todo in response.json():
        if (todo.get("userId") == int(argv[1])):
            obj["task"] = todo.get("title")
            obj["completed"] = todo.get("completed")
            obj["username"] = user.get("username")
            arr.append(obj.copy())

    data = {str(argv[1]): arr}
    filename = argv[1] + '.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)

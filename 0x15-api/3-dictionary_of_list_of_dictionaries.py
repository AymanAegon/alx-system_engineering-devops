#!/usr/bin/python3
"""
export data in the json format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    arr = []
    data = {}
    for user in users:
        for todo in response.json():
            if (todo.get("userId") == user.get("id")):
                obj = {}
                obj["username"] = user.get("username")
                obj["task"] = todo.get("title")
                obj["completed"] = todo.get("completed")
                arr.append(obj.copy())
        data[user.get("id")] = arr

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)

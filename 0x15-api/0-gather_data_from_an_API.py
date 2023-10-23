#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
from sys import argv
import requests


if __name__ == "__main__":
    s = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user = requests.get(s).json()
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    c = 0
    n = 0
    arr = []
    for todo in response.json():
        if (todo.get("userId") == int(argv[1])):
            n += 1
            if (todo.get("completed") == True):
                arr.append(todo.get("title"))
                c += 1

    print(f"Employee {user.get('name')} is done with tasks({c}/{n})")
    for title in arr:
        print("\t " + title)

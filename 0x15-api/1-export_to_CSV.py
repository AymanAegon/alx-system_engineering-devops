#!/usr/bin/python3
"""
export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    s = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user = requests.get(s).json()
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    arr = [argv[1], user.get("username")]
    data = []
    for todo in response.json():
        if todo.get("userId") == int(argv[1]):
            arr.append(str(todo.get("completed")))
            arr.append(todo.get("title"))
            data.append(arr)
            arr = [argv[1], user.get("username")]

    filename = argv[1] + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

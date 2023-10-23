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

    filename = argv[1] + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for todo in response.json():
            if todo.get("userId") == int(argv[1]):
                completed = str(todo.get("completed"))
                writer.writerow({"USER_ID": argv[1],
                                 "USERNAME": user.get("username"),
                                 "TASK_COMPLETED_STATUS": completed,
                                 "TASK_TITLE": todo.get("title")})

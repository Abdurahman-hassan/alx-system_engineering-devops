#!/usr/bin/python3
"""Gather data from an API"""
import csv
from sys import argv

import requests

if __name__ == "__main__":
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    user = response.json()
    username = user.get('username')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    todos = response.json()

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get('completed'),
                todo.get('title')
            ])

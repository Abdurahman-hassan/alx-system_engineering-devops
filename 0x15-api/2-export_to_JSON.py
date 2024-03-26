#!/usr/bin/python3
"""Gather data from an API"""
import json
from sys import argv

import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(url)
    user = response.json()
    username = user.get('username')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    todos = response.json()

    with open(f'{argv[1]}.json', 'w') as jsonfile:
        json.dump({argv[1]: [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username
        } for todo in todos]}, jsonfile)

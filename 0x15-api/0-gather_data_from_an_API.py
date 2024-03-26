#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(url)
    user = response.json()
    name = user.get('name')
    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    todos = response.json()
    done = [todo for todo in todos if todo.get('completed') is True]
    print(f'\t Employee {name} is done with tasks({len(done)}/{len(todos)}):')
    for todo in done:
        print('\t {}'.format(todo.get('title')))

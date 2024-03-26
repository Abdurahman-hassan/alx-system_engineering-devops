#!/usr/bin/python3
"""Gather data from an API"""

import json

import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    user_dict = {}
    for user in users:
        user_id = user.get('id')
        url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        response = requests.get(url)
        todos = response.json()
        user_dict[user_id] = [{
            'username': user.get('username'),
            'task': todo.get('title'),
            'completed': todo.get('completed')
        } for todo in todos]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_dict, jsonfile)

#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    user = response.json()
    name = user.get('name')
    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    todos = response.json()
    with open(f'{argv[1]}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                argv[1],
                name,
                todo.get('completed'),
                todo.get('title')
            ])

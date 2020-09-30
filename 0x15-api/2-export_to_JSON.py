#!/usr/bin/python3
""" script that given a emplyee ID, return info about todo list
"""
if __name__ == '__main__':

    import requests
    from sys import argv
    import json

    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    username = resp.json().get('username')
    resp = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    data = resp.json()

    export = {}
    export['{}'.format(argv[1])] = []
    for task in data:
        export['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
            
            
        })
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(export, file)

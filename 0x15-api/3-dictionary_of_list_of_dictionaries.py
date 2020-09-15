#!/usr/bin/python3
""" script that given a emplyee ID, return info about todo list
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    all_id = set()
    res = requests.get('https://jsonplaceholder.typicode.com/post')
    data = res.json()
    for user in data:
        all_id.add(user.get('userId'))
    
    export = {}
    for user in all_id:
        res = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user))
        username = res.json().get('username')
        res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user))
        data = res.json()
        export['{}'.format(user)] = []
        for task in data:
            export['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })

    with open('todo_all_employees.json', mode='w') as file:
        json.dump({int(x): export[x] for x in export.keys()}, file, sort_keys=True)

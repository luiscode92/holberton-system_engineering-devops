#!/usr/bin/python3
""" script that given a emplyee ID, return info about todo list
"""

import requests
from sys import argv

resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format([argv[1]))
name

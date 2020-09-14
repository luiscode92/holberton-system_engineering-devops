#!/usr/bin/python3
""" script that given a emplyee ID, return a csv file
"""
import requests
from sys import argv
import csv


if __name__ == '__main__':
    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    username = resp.json().get('username')
    resp = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    data = resp.json()

    with open('{}.csv'.format(argv[1]), mode='w') as File:
        writer = csv.writer(File, delimeter=',' quotechar='"', quoting=csv.QUOTE_ALL)

        for task in data:
            writer.writerow([argv[1], username, task.get('completed'), task.get('title')])

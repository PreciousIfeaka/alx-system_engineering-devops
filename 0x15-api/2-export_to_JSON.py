#!/usr/bin/python3

"""This script uses REST API, accepts an employee ID as an argument and
retuns inforation about his/her TODO progress
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id = argv[1]
    url1 = f'https://jsonplaceholder.typicode.com/users/{id}'
    url2 = f'https://jsonplaceholder.typicode.com/todos?userId={id}'

    resp = requests.get(url1)
    name = resp.json().get("username")

    res = requests.get(url2)
    res = res.json()
    if name:
        lists = []
        newDict = {}
        filename = f'{id}.json'

        for user in res:
            doneOrNot = user.get('completed')
            title = user.get('title')
            row = {'task': title, 'completed': doneOrNot, 'username': name}
            lists.append(row)
        newDict[id] = lists
        json_object = json.dumps(newDict)
        with open(filename, 'w') as outputfile:
            outputfile.write(json_object)

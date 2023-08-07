#!/usr/bin/python3

"""This script uses REST API, accepts an employee ID as an argument and
retuns inforation about his/her TODO progress
"""

if __name__ == "__main__":
    import json
    import requests

    url1 = 'https://jsonplaceholder.typicode.com/users'

    resp = requests.get(url1)
    resp = resp.json()

    newDict = {}
    filename = 'jazz.json'

    for userData in resp:
        lists = []
        name = userData.get("username")
        id = userData.get('id')

        url2 = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
        res = requests.get(url2).json()
        for users in res:
            doneOrNot = users.get('completed')
            title = users.get('title')
            row = {'username': name, 'task': title, 'completed': doneOrNot}
            lists.append(row)
        newDict[id] = lists
    json_object = json.dumps(newDict)
    with open(filename, 'w') as outputfile:
        outputfile.write(json_object)

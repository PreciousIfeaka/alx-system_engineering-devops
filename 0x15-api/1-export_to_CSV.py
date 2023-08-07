#!/usr/bin/python3

"""This script uses REST API, accepts an employee ID as an argument and
retuns inforation about his/her TODO progress
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    id = argv[1]
    url1 = f'https://jsonplaceholder.typicode.com/users/{id}'
    url2 = f'https://jsonplaceholder.typicode.com/todos?userId={id}'

    resp = requests.get(url1)
    name = resp.json().get("name")

    res = requests.get(url2)
    res = res.json()
    if name:
        lists = []
        fields = ['id', 'name', 'completed', 'title']
        filename = f'{id}.csv'
        csvfile = open(filename, 'w')
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields,
                                   quoting=csv.QUOTE_ALL)

        for user in res:
            doneOrNot = user.get('completed')
            title = user.get('title')

            row = {'id': id, 'name': name, 'completed': doneOrNot,
                   'title': title}
            lists.append(row)
        csvwriter.writerows(lists)

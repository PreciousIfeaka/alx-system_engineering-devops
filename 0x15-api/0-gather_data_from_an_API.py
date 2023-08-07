#!/usr/bin/python3

"""This script uses REST API, accepts an employee ID as an argument and
retuns inforation about his/her TODO progress
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    url1 = f'https://jsonplaceholder.typicode.com/users/{id}'
    url2 = f'https://jsonplaceholder.typicode.com/todos?userId={id}'

    with requests.get(url1) as resp:
        name = resp.json().get("name")

    with requests.get(url2) as res:
        res = res.json()
        if name:
            tasks = len(res)
            count = 0
            for user in res:
                if user.get('completed') is True:
                    count += 1
            print(f"Employee {name} is done with tasks({count}/{tasks}):")

            for user in res:
                if user.get('completed') is True:
                    print("\t {}".format(user.get('title')))

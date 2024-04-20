#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]

    params = {
        "userId": userId
    }
    user = requests.get(f"{url}users/{userId}").json()
    todos = requests.get(f"{url}todos/", params=params).json()

    completed = []
    for todo in todos:
        if todo.get("completed"):
            completed.append(todo.get("title"))

    print(f"Employee {user.get('name')} is done with tasks"
          f"({len(completed)}/{len(todos)}):")
    for task in completed:
        print(f"\t{task}")

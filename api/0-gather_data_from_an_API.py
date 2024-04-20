#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    params = {
        "userId": sys.argv[1]
    }
    user = requests.get(f"{url}users/", params=params).json()
    todos = requests.get(f"{url}todos/", params=params).json()

    completed = []
    for todo in todos:
        if todo.get("completed"):
            completed.append(todo.get("title"))

    print(f"Employee {user.get("name")} is done with tasks({len(completed)}/{len(todos)}):")
    for task in completed:
        print("\ttask")

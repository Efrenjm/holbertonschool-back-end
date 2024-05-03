#!/usr/bin/python3
"""extend Python script to export data in the JSON format
"""
import json
import requests
import sys


def export_to_json_dicts():
    """Records of all tasks from all employees
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    response_users = requests.get(f"{base_url}/users")
    response_users_json = response_users.json()
    response_todos = requests.get(f"{base_url}/todos")
    response_todos_json = response_todos.json()
    datadict = {}
    for index in range(len(response_users_json)):
        USERNAME = response_users_json[index]["username"]
        USER_ID = response_users_json[index]["id"]
        valuelist = []
        for index in range(len(response_todos_json)):
            if USER_ID == response_todos_json[index]["userId"]:
                TASK_COMPLETED_STATUS = response_todos_json[index]["completed"]
                TASK_TITLE = response_todos_json[index]["title"]
                valuedict = {
                    "username": f"{USERNAME}",
                    "task": f"{TASK_TITLE}",
                    "completed": TASK_COMPLETED_STATUS
                }
                valuelist.append(valuedict.copy())
        datadict[f"{USER_ID}"] = valuelist

    with open("todo_all_employees.json", "w") as file:
        json.dump(datadict, file)
    file.close()


if __name__ == "__main__":
    export_to_json_dicts()
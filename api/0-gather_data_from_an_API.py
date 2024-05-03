#!/usr/bin/python3
"""returns information about his/her todo list progress.
"""
import requests
import sys


def Gather_data(arg1):
    base_url = "https://jsonplaceholder.typicode.com/"
    response_users = requests.get(
        f"{base_url}/users"
        )
    response_users_json = response_users.json()
    listofids = []
    for index in range(len(response_users_json)):
        for key in response_users_json[index]:
            if key == "id":
                listofids.append(
                    response_users_json[index]["id"]
                )

    if arg1 in listofids:
        TOTAL_NUMBER_OF_TASKS = 0 
        NUMBER_OF_DONE_TASKS = 0
        response_todos = requests.get(f"{base_url}/todos")
        response_todos_json = response_todos.json()
        for index in range(len(response_users_json)):
            if response_users_json[index]["id"] == arg1:
                EMPLOYEE_NAME = response_users_json[index][
                    "name"
                ]

        for index in range(len(response_todos_json)):
            if response_todos_json[index]["userId"] == arg1:
                TOTAL_NUMBER_OF_TASKS += 1
                if response_todos_json[index]["completed"] is True:
                    NUMBER_OF_DONE_TASKS += 1
        print(
            f"Employee {EMPLOYEE_NAME} is \
done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for index in range(len(response_todos_json)):
            if response_todos_json[index]["userId"] == arg1:
                if response_todos_json[index]["completed"] is True:
                    TASK_TITLE = f"\t {response_todos_json[index]['title']}"
                    print(TASK_TITLE)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg1 = int(sys.argv[1])
        Gather_data(arg1)

#!/usr/bin/python3
"""extend Python script to export data in the CSV format
"""
import requests
import sys


def export_to_csv(USER_ID):
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

    USER_ID = int(sys.argv[1])
    if USER_ID in listofids:
        response_todos = requests.get(f"{base_url}/todos")
        response_todos_json = response_todos.json()
        for index in range(len(response_users_json)):
            if response_users_json[index]["id"] == USER_ID:
                USERNAME = response_users_json[index]["username"]

        with open(f"{USER_ID}.csv", "w", newline="") as file:

            for index in range(len(response_todos_json)):
                if response_todos_json[index]["userId"] == USER_ID:
                    rtjson = response_todos_json[index]
                    TASK_COMPLETED_STATUS = rtjson["completed"]
                    TASK_TITLE = response_todos_json[index]["title"]
                    file.write(
                        f'"{USER_ID}","{USERNAME}",\
"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"\n'
                    )
        file.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        USER_ID = int(sys.argv[1])
        export_to_csv(USER_ID)
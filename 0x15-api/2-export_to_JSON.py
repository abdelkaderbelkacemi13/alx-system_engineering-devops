#!/usr/bin/python3
""" A python script that exports data
    in format of a JSON file
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    employee_username = employee.get("username")
    todo_tasks = requests.get(base_url + "todos", params={
        "userId": sys.argv[1]}).json()
# prepare data
    employee_data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            }
            for task in todo_tasks
            ]
        }
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(employee_data, jsonfile)

#!/usr/bin/python3
"""a python script that uses an API to display 
    information about employees usen ID
"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todo_tasks = requests.get(base_url + "todos", params={
        "userId": sys.argv[1]}).json()

    completed_tasks = [task.get(
        "title") for task in todo_tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed_tasks), len(todo_tasks)))
    [print("\t {}".format(t_title)) for t_title in completed_tasks]

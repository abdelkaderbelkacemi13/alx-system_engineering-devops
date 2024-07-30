#!/usr/bin/python3
""" A python script that exports data
    in format of an csv file
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    employee_username = employee.get("username")
    todo_tasks = requests.get(base_url + "todos", params={
        "userId": sys.argv[1]}).json()
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, employee_username, task.get("completed"),
                task.get("title")]) for task in todo_tasks]

#!/usr/bin/python3
"""
This module fetches and displays an employee's TODO list
progress from a REST API based on a given command-line
employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the terminal arguments
    employee_id = sys.argv[1]

    # Set up web addresses for the API
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch data from the web server and convert to JSON
    user_response = requests.get(user_url)
    user_data = user_response.json()

    todos_response = requests.get(
        todos_url,
        params={"userId": employee_id}
    )
    todos_list = todos_response.json()

    # Safely extract details using the required .get() method
    employee_name = user_data.get("name")
    total_tasks = len(todos_list)

    # Use a basic loop to find completed tasks (easy for beginners)
    completed_tasks = []
    for task in todos_list:
        if task.get("completed") is True:
            completed_tasks.append(task)

    completed_count = len(completed_tasks)

    # Print summary string conforming to PEP 8 line limits
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        completed_count,
        total_tasks
    ))

    # Print out each completed task title indented
    for task in completed_tasks:
        task_title = task.get("title")
        print("\t {}".format(task_title))
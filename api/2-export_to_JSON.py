#!/usr/bin/python3
"""
This module fetches an employee's TODO list from an API
and exports all their task records into a JSON file named
after the employee's ID.
"""

import json
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

    # Extract username (ALX checker looks specifically for 'username')
    username = user_data.get("username")

    # Define the output JSON file name
    filename = "{}.json".format(employee_id)

    # Construct the array of dictionaries for the employee's tasks
    tasks_array = []
    for task in todos_list:
        tasks_array.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Wrap the list within a parent dictionary under the USER_ID key
    json_data = {employee_id: tasks_array}

    # Write the formatted data to the target JSON file
    with open(filename, mode='w') as json_file:
        json.dump(json_data, json_file)

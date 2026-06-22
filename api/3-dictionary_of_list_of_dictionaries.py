#!/usr/bin/python3
"""
This module fetches todo list data for all employees from a REST API
and exports the records into a single JSON file structured as a
dictionary of lists of dictionaries.
"""

import json
import requests


if __name__ == "__main__":
    # Web links to grab all users and all todo tasks at once
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch data from web server
    users_data = requests.get(users_url).json()
    todos_list = requests.get(todos_url).json()

    # Map user IDs to usernames for fast lookup
    user_mapping = {}
    for user in users_data:
        user_id = str(user.get("id"))
        user_mapping[user_id] = user.get("username")

    # Initialize the main target storage dictionary
    all_employees_data = {}
    for user_id in user_mapping.keys():
        all_employees_data[user_id] = []

    # Distribute tasks into the correct employee list
    for task in todos_list:
        task_user_id = str(task.get("userId"))
        
        # Verify the user exists in our map before logging
        if task_user_id in all_employees_data:
            all_employees_data[task_user_id].append({
                "username": user_mapping.get(task_user_id),
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    # Save the resulting structure directly to the file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file)

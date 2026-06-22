#!/usr/bin/python3
"""
This module fetches an employee's TODO list from an API
and exports all their task records into a CSV file named
after the employee's ID.
"""

import csv
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

    # Define the output CSV file name
    filename = "{}.csv".format(employee_id)

    # Open the file for writing and build the CSV structure
    with open(filename, mode='w', newline='') as csv_file:
        # QUOTE_ALL ensures every single column gets wrapped in double quotes
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Loop through every task belonging to this employee
        for task in todos_list:
            task_completed = task.get("completed")
            task_title = task.get("title")

            # Write the required row layout
            writer.writerow([
                employee_id,
                username,
                task_completed,
                task_title
            ])

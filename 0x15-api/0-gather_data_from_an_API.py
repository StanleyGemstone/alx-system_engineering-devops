#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""
import sys
import requests

def get_todo_by_id(todo_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos/{todo_id}"

    try:
        # Fetch the TODO data
        response = requests.get(todo_url)
        response.raise_for_status()  # Raise an exception for non-successful status codes
        todo_data = response.json()

        # Display the data
        print(todo_data)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Accept TODO ID as a parameter from the command line

    if len(sys.argv) != 2:
        print("Usage: python script.py <todo_id>")
        sys.exit(1)

    todo_id = int(sys.argv[1])
    get_todo_by_id(todo_id)


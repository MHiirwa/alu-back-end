#!/usr/bin/python3
"""
Script to fetch and display completed todos for a specific user
from JSONPlaceholder API
"""

import requests
import sys


def main():
    """Main function to fetch and display user todos"""
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)
    
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Error: User ID must be an integer")
        sys.exit(1)

    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    completed = [t for t in todos if t.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    main()

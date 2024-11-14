#!/usr/bin/python3
"""script that adds all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file')\
        .save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file')\
        .load_from_json_file

    filename = "add_item.json"

try:
    # Load the existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    items = []

# Add all arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)

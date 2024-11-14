#!/usr/bin/python3
"""script that adds all arguments to a Python list and save them to a file."""
import sys


save_to_json_file = __import__('5-save_to_json_file.py')\
        .save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py')\
        .load_from_json_file


try:
    # Load the list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, an empty list is created
    items = []

# Add all arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the 
save_to_json_file(items, filename)

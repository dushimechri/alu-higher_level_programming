#!/usr/bin/python3
"""
This module provides a function to return the\
        JSON representation of an object.
"""


import json


def to_json_string(my_obj):
    """
    Returns returns an object represented by a JSON string

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.load(my_obj)

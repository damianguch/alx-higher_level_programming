#!/usr/bin/python3
"""
Module ontains function that returns python data structure(object) from
JSON string
"""


def from_json_string(my_str):
    """Returns python data structure from JSON string
    Args:
        my_str: json string representation
    Return:
        python object
    """
    import json

    return json.loads(my_str)

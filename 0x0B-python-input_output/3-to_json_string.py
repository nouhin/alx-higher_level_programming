#!/usr/bin/python3
"""Module to convert object to JSON string"""


def to_json_string(my_obj):
    """Function to convert object to JSON string"""
    import json
    return json.dumps(my_obj)

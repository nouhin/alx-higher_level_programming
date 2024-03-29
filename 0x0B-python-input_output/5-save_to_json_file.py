#!/usr/bin/python3
"""Defines a function that writes an object to a text file using JSON"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

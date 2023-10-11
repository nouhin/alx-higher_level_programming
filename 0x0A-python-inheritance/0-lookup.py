#!/usr/bin/python3
"""Specifies a function that looks up object attributes."""


def lookup(obj):
    """Return a list of an object's available attributes.

    Args:
        obj (any): The object to look up.

    Returns:
        list: A list of the object's available attributes.
    """
    return dir(obj)

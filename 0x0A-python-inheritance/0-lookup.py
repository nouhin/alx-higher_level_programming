#!/usr/bin/python3
"""Defines a function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """Fetches a list of attributes that are accessible in an object."""
    return dir(obj)

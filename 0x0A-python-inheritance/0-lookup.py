#!/usr/bin/python3
"""Defines a function that looks up object attributes."""


def lookup(obj):
    """Fetches a list of attributes that are accessible in an object."""
    return dir(obj)

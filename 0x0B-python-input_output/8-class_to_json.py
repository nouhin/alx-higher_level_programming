#!/usr/bin/python3
"""Defines a function"""


def class_to_json(obj):
    """Return the dictionary repr of a class"""
    return obj.__dict__

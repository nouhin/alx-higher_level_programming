#!/usr/bin/python3
"""Defines a function that append a given text to a given file"""


def append_write(filename="", text=""):
    """Appends a text to a file"""
    if not isinstance(filename, str) or filename or filename == '':
        raise ValueError("filename must a non empty string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

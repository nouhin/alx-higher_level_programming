#!/usr/bin/python3
"""Defines a function that writes a string to a text file (UTF8) and returns
the number of characters written"""


def write_file(filename="", text=""):
    """Writes given etxt to a given file"""
    if not isinstance(filename, str) or not filename or filename == "":
        raise ValueError("filename must be a non empty string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

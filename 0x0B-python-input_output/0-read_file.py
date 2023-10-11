#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout""
    Args:
        filename: name of the file
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    if not filename or filename == "":
        raise ValueError("filename is empty")
    with open(filename, encoding='utf-8') as f:
        data = f.read()
    print(data, end='')

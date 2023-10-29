#!/usr/bin/python3
def magic_string():
    """Function that returns a string “BestSchool” n times."""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")

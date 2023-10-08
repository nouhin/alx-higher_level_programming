#!/usr/bin/python3
"""Prints ineteger"""


def safe_print_integer(value):
    """Functions that prints an integer

    Args:
        value (int): integer to print
    """
    is_integer = False
    try:
        print("{:d}".format(value))
        is_integer = True
    except Exception as err:
        print(f"Unexpecetd {err}")
    return is_integer

#!/usr/bin/python3
"""Prints ineteger"""


def safe_print_integer(value):
    """Functions that prints an integer

    Args:
        value (int): integer to print
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print(f"Unexpecetd {err}")
        return False

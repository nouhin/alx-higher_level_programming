#!/usr/bin/python3
"""Defines a function that divides 2 integers and prints the result"""


def safe_print_division(a, b):
    """Function thqt divides two integers"""
    ans = None
    try:
        ans = a / b
    except Exception:
        pass
    finally:
        print("{}".format(ans))
    return ans

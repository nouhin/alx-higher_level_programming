#!/usr/bin/python3
""" Function that prints x elements of a list. """


def safe_print_list(my_list=[], x=0):
    """Function that prints x elements of a list.

    Args:
        my_list (list): List to print.
        x (int): Number of elements to print.
    """
    n = 0
    try:
        for i in my_list[:x]:
            n += 1
            print(i, end="")
        print()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    return n

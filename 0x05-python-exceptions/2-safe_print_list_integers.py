#!/usr/bin/python3
"""Prints first x integer elements in a given list"""


def safe_print_list_integers(my_list=[], x=0):
    """Functions that prints first x integer elements in a given list

    Args:
        my_list (list): list to print
        x (int): number of elements to print

    Returns:
        int: number of elements printed
    """
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            pass
    print()
    return n

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Args:
        my_list: a list
    Return:
        print elements in reverse order
    """
    my_list_rev = [my_list[-i] for i in range(1, len(my_list) + 1)]
    print(*my_list_rev, sep="\n", end="")

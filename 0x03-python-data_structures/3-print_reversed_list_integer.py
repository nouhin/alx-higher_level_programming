#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Args:
        my_list: a list
    Return:
        print elements in reverse order
    """
    for i in my_list[::-1]:
        print("{:d}".format(i))

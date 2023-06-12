#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    Args:
        my_list
    Returns:
        reversed list
    '''
    if my_list is not None:
        for i in my_list[::-1]:
            print("{:d}".format(i))

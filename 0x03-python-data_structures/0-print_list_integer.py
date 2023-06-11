#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Args:
        my_list: list of integers

    Return:
        No return
    """
    li = ["{:d}".format(i) for i in my_list]
    print("\n".join(li)) if len(li) > 0 else None

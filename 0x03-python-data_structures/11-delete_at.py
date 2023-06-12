#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Args:
        my_list: a list
        idx: int, the index at which the element must be deleted
    Returns:
        list with deleted element
    """
    if (0 <= idx < len(my_list)) and (my_list is not None):
        del my_list[idx]
    return my_list

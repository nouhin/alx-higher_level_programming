#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Args:
        my_list: a list
        idx: index at which element should be replace
        element: element to replace with
    Return:
        new list with replaced element
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list

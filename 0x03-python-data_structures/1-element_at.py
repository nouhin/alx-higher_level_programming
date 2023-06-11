#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Args:
        my_list: a list
        idx: index at which we want to retrieve teh element
    Returns:
        element at index idx
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]

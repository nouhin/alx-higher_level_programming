#!/usr/bin/python3
"""Divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list_1 (list): list of integers
        my_list_2 (list): list of integers
        list_length (int): length of lists

    Returns:
        list: list of quotients
    """
    ans = []
    try:
        for i in range(list_length):
            ans.append(my_list_1[i] / my_list_2[i])
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return ans

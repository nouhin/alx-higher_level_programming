#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Function that replaces or adds key/value in a dictionary."""
    return a_dictionary.update({key: value}) or a_dictionary

#!/usr/bin/python3
"""Defines a subclass of the built-in list class named MyList."""


class MyList(list):
    """A subclass of the builtin list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))

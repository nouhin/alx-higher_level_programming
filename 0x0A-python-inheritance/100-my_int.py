#!/usr/bin/python3
"""Defines a class MyInt that is a subclass of int."""


class MyInt(int):
    """Represent a subclass of int."""

    def __eq__(self, value):
        """Overrides the == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides the != operator with == behavior."""
        return self.real == value

#!/usr/bin/python3
"""Defines a secured class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new instance attributes,
    """

    __slots__ = ["first_name"]

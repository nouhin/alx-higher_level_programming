#!/usr/bin/python3
"""Raises a name exception with a message."""


def raise_exception_msg(message=""):
    """Raises a name exception with a message.

    Args:
        message (str, optional): message to raise. Defaults to "".
    """
    raise NameError(message)

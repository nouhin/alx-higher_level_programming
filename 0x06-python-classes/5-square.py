#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a suqare"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def area(self):
        """Computes the area of a square"""
        return self.__size**2

    def my_print(self):
        """Displays a square to stdout"""
        if self.size > 0:
            nline = '\n'
            print(f"{('#'*self.__size + nline)*self.__size}")
        else:
            print()

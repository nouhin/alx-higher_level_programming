#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a suqare"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(n, int) for n in value) or not all(n >= 0
                                                              for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of a square"""
        return self.__size**2

    def my_print(self):
        """Displays a square to stdout"""
        if self.size > 0:
            nline = '\n'
            print(f"{('#'*self.__size + nline)*self.__size}", end='')
        else:
            print()

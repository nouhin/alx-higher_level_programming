#!/usr/bin/python3
"""This script defines a Rectangle class."""


class Rectangle:
    """This class models a rectangle. It defines corresponding methods and attributes.

    Attributes:
        number_of_instances (int): Counts the instances of Rectangle objects.
        print_symbol (any): The symbol used to depict the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructs a Rectangle instance.

        Args:
            width (int): Defines the width of the rectangle.
            height (int): Defines the height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Manage the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """Manage the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """Calculates the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """Determines the Rectangle with the larger area.

        Args:
            rect1 (Rectangle): The first Rectangle object.
            rect2 (Rectangle): The second Rectangle object.
        Raises:
            TypeError: If either rect1 or rect2 is not a Rectangle.
        """
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect1.area() >= rect2.area():
            return (rect1)
        return (rect2)

    @classmethod
    def square(cls, size=0):
        """Constructs a new Rectangle with width and height equal to size.

        Args:
            size (int): The equal width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Generates a printable string representation of the Rectangle.

        The rectangle is represented using the print_symbol character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_str = []
        for i in range(self.__height):
            [
                rect_str.append(str(self.print_symbol))
                for j in range(self.__width)
            ]
            if i != self.__height - 1:
                rect_str.append("\n")
        return ("".join(rect_str))

    def __repr__(self):
        """Generates a formal string representation of the Rectangle."""
        rect_str = "Rectangle(" + str(self.__width)
        rect_str += ", " + str(self.__height) + ")"
        return (rect_str)

    def __del__(self):
        """Called when a Rectangle instance is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

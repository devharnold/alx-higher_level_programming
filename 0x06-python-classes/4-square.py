#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Class of a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """instance of the square
        Args:
            size (int): size of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """square's area
        Returns:
            Area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of the square
        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
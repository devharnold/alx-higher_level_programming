#!/usr/bin/python3
"""defines a class Square"""

class Square:
    """Class of a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of the square
        Returns:
            Nothing
        """
        self.size = size

    def area(self):
        """Finds the square's area
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
            value (int): size of the square
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

    def my_print(self):
        """print square
        Returns:
            Nothing
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
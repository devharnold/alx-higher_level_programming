#!/usr/bin/python3

"""Superclass BaseGeometry Subclass Rectangle and import"""
Rectangle = __import__('9-rectanlge').Rectangle

"""class Square"""
class Square(Rectangle):
    """created the class inititalize the objects and work out"""
    def __init__(self, size):
        """instance of the square"
        use of self.integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of the square
        return the private instance ** 2"""
        return self.__size ** 2

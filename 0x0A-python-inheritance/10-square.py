#!/usr/bin/python3

"""Superclass BaseGeometry Subclass Rectangle"""
Rectangle = __import__('9-rectanlge').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        """instance of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of the square"""
        return self.__size ** 2

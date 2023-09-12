#!/usr/bin/python3

"""Superclass BaseGeometry Subclass Rectangle"""
Rectangle = __import__('9-rectanlge').Rectangle

class Square(Rectangle):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """area of the square"""
        return self.__size ** 2

#!/usr/bin/python3

"""Import BaseGeometry from file 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class Rectangle
"""

class Rectangle(BaseGeometry):
    """class rectangle created"""
    def __init__(self, width, height):
        """definition of class rectangle
        together with self.integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """private instances"""

        self.__width = width
        self.__height = height
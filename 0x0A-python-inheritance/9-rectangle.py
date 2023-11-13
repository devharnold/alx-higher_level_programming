#!/usr/bin/python3

"""Import BaseGeometry from 7-base_geometry"""
BaseGeometry=__import__('7-base_geometry').BaseGeometry

"""class Rectangle"""
class Rectangle(BaseGeometry):
    """class created"""
    def __init__(self, width, height):
        """definition of the class instances used
        we have the self.integer_validators
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """private instances"""
        self.__width = width
        self.__height = height

    def area(self):
            """definition of the area function"""
            return self.__width * self.__height
        
    def __str__ (self):
            """definition and use of the magic method '__str__' """
            return '[Rectangle]' + str(self.__width) + '/' + str(self.__height)
#!/usr/bin/python3

"""import Rectangle from 9-rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

"""class Square"""
class Square(Rectangle):
    """initialize the objects of the class rectangle
    use different functions such the magic methods
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """define the area() function"""
        return self.__size ** 2

    def __str__(self):
        """the magic method __str__"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
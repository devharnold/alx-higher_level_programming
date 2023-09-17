#!/usr/bin/python3
"""Definition of a Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Representation of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle
        Args:
           width (int): width of this new rectangle
           height (int): height of this new rectangle
           x (int): the x axis -> x coordinate of this rectangle
           y (int): the y axis -> y coordinate of this rectangle
           id (int): id of the rectangle
        Raises:
            TypeError: when the width and height are not int
            ValueError: when width or height <= 0
            ValueError: when either x or y < 0
            TypeError: when either x or y is not int
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self):
        if type(value) != int:
            raise TypeError("Must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """get the y coordinate"""
        return self.__y

    @y.setter
    def y(self):
        if type(value) != int:
            raise TypeError("Must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__y = value

    @property
    def x(self):
        """get the y coordinate"""
        return self.__x

    @x.setter
    def y(self):
        if type(value) != int:
            raise TypeError("Must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__x = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.height, self.x, self.y, self.width)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
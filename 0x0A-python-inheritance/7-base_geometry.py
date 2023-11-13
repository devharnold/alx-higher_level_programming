#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    A super class to implements geometrical shapes
    """

    def area(self):
        """
        Raises an exception when you call this function
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Checks a integer value

        Args:
            name (str): The name of the value.
            value (int): The value.

        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is less than or equal to zero.
        """

        if type(value) is not int:
            """if the type(value) is not int -> raise TypeError"""
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            """if value is less than 0 raise valueError"""
            raise ValueError(name + ' must be greater than 0')
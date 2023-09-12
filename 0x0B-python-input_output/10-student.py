#!/usr/bin/python3
"""class Student."""


class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
        """Init new Student.
        Args:
            first_name (str): first name.
            last_name (str): last name.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary rep of the Student.
        If attrs is a list of strings, represent only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
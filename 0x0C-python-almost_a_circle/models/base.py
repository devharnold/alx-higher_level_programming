#!/usr/bin/python3
"""Define a base model class"""
import json
import csv
import turtle


class Base:
    """Represent base model. The base will act as 'base' 
    for all other classes.
    Attributes:
    __nb_objects (int): Number of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a fresh/new base
        Args:
        id (int) : id of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
#!/usr/bin/python3
"""
Class_to_json function
"""

def class_to_json(obj):
    """return dictionary description a data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
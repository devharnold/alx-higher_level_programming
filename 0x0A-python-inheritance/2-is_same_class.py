#!/usr/bin/python3

"""is_same_class"""

def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object
    """

    if type(obj) == a_class:
        return True
    
    """   
    Returns:
        `True` if the object is exactly an instance of the
        specified class; otherwise `False`
    """
    return False
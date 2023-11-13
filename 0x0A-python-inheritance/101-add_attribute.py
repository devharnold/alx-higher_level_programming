#!/usr/bin/python3

"""Adding attributes to objects"""
def add_attribute(obj, attr, value):
    """Add attr to obj.
    Args:
        obj : object adding an attribute to
        attr : name of attribute to add on object
        value : the output
    Raise :
        TypeError
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("failed to add new attribute!")
    
    setattr(obj, attr, value)

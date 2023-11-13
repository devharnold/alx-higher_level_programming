#!/usr/bin/python3

"""inherits_from -> function definition"""

def inherits_from(obj, a_class):
    """Returns true if obj is a subclass of a_class, else false"""
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
#!/usr/bin/python3

"""class MyInt"""
class MyInt(int):
    """definition of new class items used, args, kwargs"""
    def __new__(cls, *args, **kwargs):
        """returns super(result of top)"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)
    
    def __eq__(self, other):
        """definition of __eq__ function"""
        """!= -> =="""
        return int(self) != other
    
    def __ne__(self, other):
        """== -> !="""
        return int(self) == other

#!/usr/bin/python3
"""Define a class for inherited cheking object"""

def is_kind_of_class(obj, a_class):
    """check object is an instance or inherited instance"""
    if isinstance(obj, a_class):
        return True
    return False

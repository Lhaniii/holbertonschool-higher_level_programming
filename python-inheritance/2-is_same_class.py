#!/usr/bin/python3
"""Define a class for cheking object"""


def is_same_class(obj, a_class):
    """check object is in same instance"""
    if type(obj) == a_class:
        return True
    return False

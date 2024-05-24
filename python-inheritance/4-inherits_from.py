#!/usr/bin/python3
"""Defines an inherited class checking function"""

def inherits_from(obj, a_class):
    """checks an object is inherited instance of class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

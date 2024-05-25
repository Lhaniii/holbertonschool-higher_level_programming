#!/usr/bin/python3
"""Defines empty class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """print square"""

    def __init__(self, size):
        """ init new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

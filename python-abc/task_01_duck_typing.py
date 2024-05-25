#!/usr/bin/env python3
""" Abstract Class """

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """Define Class shape"""
    @abstractmethod
    def area(self):
        """Def area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
         """def perimeter of shape"""
         pass

class Circle(Shape):
    """class print Circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """def area of the Circle"""
        return abs(math.pi * self.radius**2)

    def perimeter(self):
        """def perimeter of the Circle"""
        return abs(2 * math.pi * self.radius)

class Rectangle(Shape):
    """class print Rectangle"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """def the area of the Rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """ def the perimeter of rectangle"""
        return (2 * (self.width + self.height))

def shape_info(Shape):
    """ print the area and perimeter of shape"""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")

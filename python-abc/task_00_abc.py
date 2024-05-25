#!/usr/bin/env python3
""" Define classe of animal """


from abc import ABC, abstractmethod

class Animal(ABC):
    """define class animal"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """define class Dog based of class Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """define class cat based of class animal"""
    def sound(self):
        return "Meow"

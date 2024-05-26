#!/usr/bin/python3

class Fish:
    """Define class fish"""
    def swim(self):
        """The method to swim of fish"""
        print("The fish lives in water")

class Bird:
    """Define class bird."""
    def fly(self):
        """The method to fly for bird"""
        print("The bird is flying")

    def habitat(self):
        """The method describes habitat of bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Define class FlyingFish"""
    def fly(self):
        """The method to fly fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """The method to swim of fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """The method descrubes habitat of FlyingFish"""
        print("The flying fish lives both in water and the sky!")

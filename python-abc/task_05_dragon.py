#!/usr/bin/env python3


class SwimMixin:
    """Define class SwimMixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """define class FlyMiwin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Define class dragon"""
    def roar(self):
        print("The dragon roars!")

    def spit_fire(self):
        print("The dragon spits fire!")

    def observe(self):
        print("The dragon observes!")

    def attack(self):
        print("The dragon attacks!")

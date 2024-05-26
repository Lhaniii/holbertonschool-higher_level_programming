#!/usr/bin/python3
"""Define class CountedIterator"""


class CountedIterator:
    """Define class countedIterator"""
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the count"""
        return self.counter

    def __next__(self):
        """Override the next"""
        try:
            i = next(self.iterator)
            self.counter =+ 1
            return i 
        except StopIteration:
            raise StopIteration

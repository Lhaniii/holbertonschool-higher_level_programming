#!/usr/bin/python3
"""Define class CountedIterator"""


class CountedIterator:
    """Define class countedIterator count number of iteration"""
    def __init__(self, some_iterable):
        """init the counter for iteration"""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the count"""
        return self.counter

    def __next__(self):
        """the next method to increment counter"""
        try:
            i = next(self.iterator)
            self.counter =+ 1
            return i 
        except StopIteration:
            raise StopIteration

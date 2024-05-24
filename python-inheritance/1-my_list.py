#!/usr/bin/python3
"""Define inherited list"""


class MyList(list):
    """define class list"""

    def print_sorted(self):
        """Print a list"""
        print(sorted(self))

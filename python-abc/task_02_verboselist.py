#!/usr/bin/python3
class VerboseList(list):
    """
    define Verboselist"""
    def append(self, item):
        """Append item in the list and print message"""
        super().append(item)
        print("added [{}] to the list.".format(item))

    def extend(self, item):
        """extends list with given item and print message."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove first occurence of item"""
        print("Removed [{}] form the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        """removes and returns item specifi and print a message"""
        print("Popped [{}] from the list.".format(item))
        return item

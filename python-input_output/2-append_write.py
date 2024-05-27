#!/usr/bin/python3
"""Defines file-appending function"""


def append_write(filename="", text=""):
    """Append string to the end of utf8"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

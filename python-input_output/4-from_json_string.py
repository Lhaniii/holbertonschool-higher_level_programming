#!/usr/bin/python3
"""Defines JSON-STRING function."""
import json


def from_json_string(my_str):
    """Return python object of json string."""
    return json.loads(my_str)

#!/usr/bin/python3
"""Define JSON save function"""
import json


def save_to_json_file(my_obj, filename):
    """def save to jsonfile"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

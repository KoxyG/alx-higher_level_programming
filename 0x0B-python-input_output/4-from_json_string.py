#!/usr/bin/python3
"""This module defines a JSON representation to object function"""
import json


def from_json_string(my_str):
    """Returns the Python object representation oof a JSON string"""
    return json.loads(my_str)

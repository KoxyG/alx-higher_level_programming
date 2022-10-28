#!/usr/bin/python3
"""This module defines a JSON file reading function"""
import json


def load_from_json_file(filename):
    """"creates a Python object from a given JSON file"""
    with open(filename) as f:
        return json.loads(f)

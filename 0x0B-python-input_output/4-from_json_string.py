#!/usr/bin/python3

"""Module that cointais from_json_string function"""
import json


def from_json_string(my_str):
    """Function that returns an object
    (Python data structure) represented
    by a JSON string:"""
    x = json.loads(my_str)
    return x

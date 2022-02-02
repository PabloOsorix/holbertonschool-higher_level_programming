#!/usr/bin/python3

"""Modulee that contains load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Function that creates an Object
    from a “JSON file”:"""
    with open(filename, encoding="utf-8") as file:
        json.load(file)

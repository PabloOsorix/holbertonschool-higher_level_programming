#!/usr/bin/python3
"""
Script that displays value of the variable
 in the response header.
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])

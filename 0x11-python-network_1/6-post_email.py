#!/usr/bin/python3
"""
Script that sends a value email
by a post request to given URL.
"""
from sys import argv
import requests


if __name__ == "__main__":
    data = {'email': argv[2]}
    url = argv[1]
    req = requests.post(url, data)
    print(req.text)

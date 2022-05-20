#!/usr/bin/python3
"""
Script that displays the body of the
given response
"""
from sys import argv
import requests


if __name__ == "__main__":
    if argv[1]:
        letter = {"q": argv[1]}
    else:
        letter = {"q": ""}

    req = requests.post("http://0.0.0.0:5000/search_user",
                        data=letter).json()
    try:
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except ValueError:
        raise("Not a valid JSON")
#!/usr/bin/python3
"""
Script that displays the body of the
given response
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = {"q": ""} if len(argv) == 1 else {"q": argv[1]}

    req = requests.post("http://0.0.0.0:5000/search_user",
                        data=letter)
    try:
        req = req.json()
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""
Script that send a variable email
in a POST request.
"""
import sys
import urllib.request


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlenconde(email)
    data = data.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        response = response.read().decode('utf-8')

    print(response)

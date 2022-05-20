#!/usr/bin/python3
"""
Script that send a variable email
in a POST request.
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlenconde(email).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        response = response.read().decode('utf-8')
    print(response)

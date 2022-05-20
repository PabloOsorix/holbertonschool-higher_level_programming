#!/usr/bin/python3
"""
Script that send a variable email
in a POST request.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body_r = response.read().decode('utf-8')
    print(body_r)

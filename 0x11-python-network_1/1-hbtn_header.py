#!/usr/bin/python3
"""
script that takes in a URL,
and displays the value of the
X-Request-Id variable found
in the header of the response.
"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    header = response.headers
    print(header['X-Request-Id'])

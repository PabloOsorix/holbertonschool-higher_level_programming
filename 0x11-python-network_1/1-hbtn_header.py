#!/usr/bin/python3
"""
script that obtain the
X-Request from a response
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.headers
        print(header.['X-Request-Id'])

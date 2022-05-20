#!/usr/bin/python3
"""
script that sends requests to the
given URL and display the body of
the response.
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read())
    except urllib.error.HTTPError as error:
        print("Errod code: {}".format(error.getcode()))

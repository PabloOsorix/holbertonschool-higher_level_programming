#!/usr/bin/python3
"""
Script that obtain your Git user id
through github user API with your
credentials
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    basic = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user",
                       auth=basic).json()

    print(req.get('id'))

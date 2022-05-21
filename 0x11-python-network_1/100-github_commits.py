#!/usr/bin/python3
"""
Script that list the last 10
commits of a repo with github API
"""
from sys import argv
import requests


if __name__ == "__main__":
    counter = 0
    repo = argv[1]
    owner = argv[2]
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(repo, owner)).json()

    for key in range(0, 10):
        name = req[key]['commit']['author'].get('name')
        print("{}: {}".format(req[key].get('sha'), name))

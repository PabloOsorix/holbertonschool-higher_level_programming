#!/usr/bin/python3
"""
Script that list the last 10
commits of a repo with github API
"""
from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    req = requests.get(url)
    req = req.json()
    try:
        for index in range(10):
            name = req[index].get('commit').get('author').get('name')
            print("{}: {}".format(req[index].get('sha'), name))
    except IndexError:
        pass

#!/usr/bin/python3
import hidden_4


def printNames():
    name = dir(hidden_4)
    for i in name:
        if i[0:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    printNames()
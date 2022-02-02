#!/usr/bin/python3


"""This module contan function read_file"""


def read_file(filename=""):
    """function that reads a text file (UFT-8)
    and prints it to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        lines = my_file.read()
        print(lines, end="")

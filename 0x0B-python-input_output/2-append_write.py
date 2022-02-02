#!/usr/bin/python3

"""Module that contains the append_write dunction"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added:"""
    with open(filename, mode="w",  encoding="utf-8") as file:
        file.seek(0, 2)
        return(file.write(text))

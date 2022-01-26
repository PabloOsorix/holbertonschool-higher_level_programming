#!/usr/bin/python3

"""This module contain the text_identation function"""


def text_indentation(text):
    """This function insert a new line each time that a
    ".", "," or "?" be found"""
    string = list()
    string_t = []

    if isinstance(text, str):
        if text == "":
            return
        string = list(text)
        for i in range(len(string) + 1):
            if i + 1 == len(string):
                string_t.append(string[i])
                string_t = "".join(string_t)
                print(string_t, end='')
                break
            if string[i] == " " and string[i - 1] == '.'\
                or string[i] == " " and string[i - 1] == ':'\
                    or string[i] == " " and string[i - 1] == '?':
                continue
            if string[i] == '.' or string[i] == ':' or string[i] == '?':
                string_t.append(string[i])
                string_t.append("\n\n")
            else:
                string_t.append(string[i])
    else:
        raise TypeError("text must be a string")

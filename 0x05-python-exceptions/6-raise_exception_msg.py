#!/usr/bin/python3


from email import message_from_string


def raise_exception_msg(message=""):
    try:
        print("{}".format(message))
    except NameError:
        pass

#!/usr/bin/python3

"""Module contain class object MyList"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Class that defines MyList"""
        print(sorted(self))

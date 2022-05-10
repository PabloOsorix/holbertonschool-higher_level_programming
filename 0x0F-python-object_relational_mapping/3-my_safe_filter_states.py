#!/usr/bin/python3
"""
script that takes in an argument and
displays all values in the states where
name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %(user_input)s",
                   {'user_input': argv[4]})

    for states in cursor.fetchall():
        if states[1] == argv[4]:
            print(states)
    cursor.close()
    db.close()

#!/usr/bin/python3
# script that takes in the name of a state as an
# argument and lists all cities of that state,
# using the database hbtn_0e_4_usa

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities \
        WHERE state_id= (SELECT id FROM states WHERE name= %(state_name)s) \
            ORDER BY cities.id ASC", {'state_name': argv[4]})
    obj = cursor.fetchall()
    for cities in range(len(obj)):
        if cities + 1 != len(obj):
            print(f"%s, " % (obj[cities]), end=" ")
            continue
        print(f"%s" % (obj[cities]))
    cursor.close()
    db.close()

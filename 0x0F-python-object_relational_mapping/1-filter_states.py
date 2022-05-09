#!/usr/bin/python3
# script that lists all states with a name
# starting with N (upper N) from the database hbtn_0e_0_usa
import MySQLdb
from sys import argv


db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                     passwd=argv[2], db=argv[3])
cursor = db.cursor()

cursor.execute("SELECT id, name FROM states WHERE states.name LIKE 'N%' \
               ORDER BY states.id")
for rows in cursor.fetchall():
    print(rows)
cursor.close()
db.close()

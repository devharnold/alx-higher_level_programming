#!/usr/bin/python3
"""
Write a script that lists all states with a name starting 
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", password=argv[2], user=argv[1], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows=cur.fetchall()
    for row in rows:
        print(row)
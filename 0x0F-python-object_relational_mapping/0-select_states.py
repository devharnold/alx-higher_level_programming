#!/usr/bin/python3
"""
Listing all states from the db 'hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, password=argv[2], user=argv[1], 
                           db=argv[3], charset="utf-8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print (row)


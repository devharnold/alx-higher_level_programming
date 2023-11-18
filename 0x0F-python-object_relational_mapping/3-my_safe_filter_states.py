#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, db=argv[3] ,password=argv[2], user=argv[1])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states \
                WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id ASC""",{'name': argv[4]}
                )
    
    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
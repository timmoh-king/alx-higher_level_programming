#!/usr/bin/python3

"""
    takes in arguments and displays all values in
    table states table of hbtn_0e_0_usa where name match arg
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (
            sys.argv[4], ))

    for row in cur.fetchall():
        print(row)

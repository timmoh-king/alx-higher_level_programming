#!/usr/bin/python3
import sys
import MySQLdb

"""
    takes in arguments and displays all values in
    table states table of hbtn_0e_0_usa where name match arg
"""

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            sys.argv[4]))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

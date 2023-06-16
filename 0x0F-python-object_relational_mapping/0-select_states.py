#!/usr/bin/python3
import MySQLdb

"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM `states` ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

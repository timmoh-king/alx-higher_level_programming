#!/usr/bin/python3
import MySQLdb
import sys

"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":

    db = MySQLdb.connect(user='root', passwd='@_Timmoh7', db='hbtn_0e_0_usa')
    cur = db.cursor()

    cur.execute("SELECT * FROM `states` ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

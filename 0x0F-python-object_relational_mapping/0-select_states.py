#!/usr/bin/python3
import MySQLdb

"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""

db = MySQLdb.connect(user='root', passwd='@_Timmoh7', db='hbtn_0e_0_usa')
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")
numrows = cur.fetchall()

for row in numrows:
    print(row)

cur.close()
db.close()

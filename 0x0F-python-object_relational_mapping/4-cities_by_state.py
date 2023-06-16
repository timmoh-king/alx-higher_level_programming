#!/usr/bin/python3
import sys
import MySQLdb

"""
    Write a script that lists all cities from the database hbtn_0e_4_usa
    3 arguments: mysql username, mysql password and database name
"""

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                ORDER BY cities.id ASC""")
    for row in cur.fetchall():
        print(row)

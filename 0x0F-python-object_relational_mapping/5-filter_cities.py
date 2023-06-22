#!/usr/bin/python3

"""
    a script that takes in the name of a state as an argument
    lists all cities of that state, using the database hbtn_0e_4_usa
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

    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name = '{}'
                ORDER BY cities.id""".format(sys.argv[4]))
    cities = cur.fetchall()
    if cities:
        city_list = [city[0] for city in cities]
        city_string = ", ".join(city_list)
        print(city_string)
    else:
        print()

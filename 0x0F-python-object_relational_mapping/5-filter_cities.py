#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306)
    cur = db.cursor()
    cur.execute('''SELECT cities.name FROM cities INNER JOIN states ON
                cities.states_id = states.id WHERE states.name = %s",
                 (sys.argv[4], )''')
    data = cur.fetchall()
    temp = list(row[0] for row in data)
    print(*temp, sep=", ")
    cur.close()
    db.close()

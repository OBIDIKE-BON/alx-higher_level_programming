#!/usr/bin/python3
"""
Lists all cities from the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    csr = db.cursor()
    csr.execute("SELECT * FROM `cities`")
    for city in csr.fetchall():
        print(city)

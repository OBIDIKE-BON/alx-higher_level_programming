#!/usr/bin/python3
"""
Lists all states from the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    csr = db.cursor()
    csr.execute("SELECT * FROM `states`")
    for state in csr.fetchall():
        print(state)

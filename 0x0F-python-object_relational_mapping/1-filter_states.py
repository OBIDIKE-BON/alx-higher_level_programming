#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    csr = db.cursor()
    csr.execute("SELECT * FROM `states`"+
    " WHERE name COLLATE utf8mb4_bin LIKE %s", ['N%'])
    for state in csr.fetchall():
        print(state)

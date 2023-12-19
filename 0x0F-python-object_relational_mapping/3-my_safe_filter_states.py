#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name securlly matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    csr = db.cursor()
    csr.execute("SELECT * FROM states WHERE \
    name COLLATE utf8mb4_bin = %s ORDER BY id ASC",[sys.argv[4]])
    for state in csr.fetchall():
        print(state)

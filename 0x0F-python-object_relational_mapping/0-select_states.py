#!/usr/bin/python3
"""
Lists all states from the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost:3306", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]

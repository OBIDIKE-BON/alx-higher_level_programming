#!/usr/bin/python3
"""
Lists all cities from of a state with join.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    csr = db.cursor()
    query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
            """
    csr.execute(query, [sys.argv[4]])
    first = True
    for state in csr.fetchall():
        if first:
            print(state[1], end="")
            first = False
        else:
            print(", ", (state[1]), end="")
    print()

#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name
containing the letter a from the database.
"""
import sys
from sqlalchemy import create_engine, func, collate
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    con = "mysql+mysqldb://{}:{}@localhost/{}\
".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(con, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

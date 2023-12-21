#!/bin/python3
"""
Write a script that adds the State object “Louisiana” to the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    con = "mysql+mysqldb://{}:{}@localhost/{}\
".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(con, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name = "Louisiana")
    row = session.add(new_state)
    session.commit()
    print(new_state.name)

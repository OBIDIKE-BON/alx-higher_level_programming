#!/usr/bin/python3
"""
Write a script that lists all State objects
that contain the letter a from the database
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

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print(f"{state.id}: {state.name}")

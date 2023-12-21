#!/usr/bin/python3
"""
Write a script that changes the name of a State object from the database.
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

    state_update = State(id=2, name="New Mexico")
    row = session.merge(state_update)
    session.commit()

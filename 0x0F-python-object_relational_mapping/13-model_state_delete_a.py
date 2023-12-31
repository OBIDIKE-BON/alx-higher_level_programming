#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name
containing the letter a from the database.
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

    a_states = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in a_states:
        session.delete(state)
    session.commit()

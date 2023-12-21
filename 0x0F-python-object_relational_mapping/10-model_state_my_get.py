#!/usr/bin/python3
"""
print State id from the database given itst's name.
"""
import sys
from sqlalchemy import create_engine, func, collate
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    con = "mysql+mysqldb://{}:{}@localhost/{}\
".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(con, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
            collate(State.name, 'utf8mb4_bin') == sys.argv[4]
                                        ).first()
    if state:
        print(state.id)
    else:
        print("Not found")

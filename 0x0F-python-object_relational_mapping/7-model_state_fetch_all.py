#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_0_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                )
            )

    Base.metadata.bind = engine

    dbSession = sessionmaker(bind=engine)
    session = dbSession()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()

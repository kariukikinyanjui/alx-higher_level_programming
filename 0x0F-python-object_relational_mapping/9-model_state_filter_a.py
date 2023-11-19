#!/usr/bin/python3
"""
Lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                ),
            )
    Base.metadata.bind = engine

    dbSession = sessionmaker(bind=engine)
    session = dbSession()

    states_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    for state in states_a:
        print('{}: {}'.format(state.id, state.name))

    session.close()

#!/usr/bin/python3
"""Prints the first State object from database hbtn_0e_6_usa"""
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

    state_1 = session.query(State).order_by(State.id).first()

    if state_1:
        print('{}: {}'.format(state_1.id, state_1.name))
    else:
        print('Nothing')

    session.close()

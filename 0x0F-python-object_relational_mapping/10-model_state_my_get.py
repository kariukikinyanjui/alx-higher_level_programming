#!/usr/bin/python3
"""
Prints the State objects with the name passed as argument
from the database hbtn_0_6_usa
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

    state_name = sys.argv[4]
    results = session.query(State).filter(State.name == state_name).first()

    if results:
        print(results.id)
    else:
        print('Nothing')

    session.close()

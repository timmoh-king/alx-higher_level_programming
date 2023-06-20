#!/usr/bin/python3

"""
    a script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """
        engine: instatiate the connection
        session: start the conversation with the db
    """
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(
                    sys.argv[1],
                    sys.argv[2],
                    sys.argv[3]),
                pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.id.like('2')):
        state.name = "New Mexico"
        session.commit()

    Base.metadata.create_all(engine)

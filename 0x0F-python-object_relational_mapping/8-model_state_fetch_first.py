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

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    Base.metadata.create_all(engine)

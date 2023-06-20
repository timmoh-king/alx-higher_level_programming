#!/usr/bin/python3

"""
    a script that lists all cities objects from the database hbtn_0e_6_usa
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

    for instance in session.query(State).join(Cities).order_by(Cities.id):
        print("{}: ({}) {}".format(instance.name, instance.id, instance.name))

    Base.metadata.create_all(engine)
 
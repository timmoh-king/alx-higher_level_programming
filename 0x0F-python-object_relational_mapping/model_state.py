#!/usr/bin/python3

"""
    a python file that contains the class definition of a State
    an instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
        __tablename__(str): link to the table states in the database
        id (sqlalchemy.Integer): id to the state
        name (sqlalchemy.String): represent the state name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

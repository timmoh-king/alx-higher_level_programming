#!/usr/bin/python3

"""
    a python file that contains the class definition of a State
    an instance Base = declarative_base():
"""

from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class City(Base):
    """
        __tablename__(str): link to the table states in the database
        id (sqlalchemy.Integer): id to the state
        name (sqlalchemy.String): represent the state name
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key=True)

#!/usr/bin/python3

"""Class definition of state and an instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """The class State
    Attributes:
    __tablename__: The table name of the class
    id: The id of the class
    name: The name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
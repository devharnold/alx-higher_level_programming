#!/usr/bin/python3

"""
Improve the files model_city.py and model_state.py, and
save them as relationship_city.py and relationship_state.py
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declararive import declarative_base

Base = declarative_base()

class State(Base):
    """
    Defines the Class State-> in relationship to Base
    Attributes:
    __tablename__: The table name of the class
    id: The id of the class
    name: The name of the class
    """

    __tablename__ = 'State'

    id=Column(Integer, primary_key=True)
    name=Column(String(128), nullable=False)
    cities = relationship("city", backref="state", cascades="all, delete")

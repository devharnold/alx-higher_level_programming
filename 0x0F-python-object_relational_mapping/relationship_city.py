#!/usr/bin/python3

"""
Improve the files model_city.py and model_state.py, and 
save them as relationship_city.py and relationship_state.py
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """Defines the City class Base
    Attributes:
    __tablename__: The table name of the class City
    id: The id of the class City
    name: The name of the class City
    """

    __tablename__ = 'city'
    id=Column(Integer, primary_key=True)
    name=Column(String(128), nullable=False)
    state_id=Column(Integer, ForeignKey('states.id'), nullable=False)
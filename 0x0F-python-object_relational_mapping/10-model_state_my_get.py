#!/usr/bin/python3
"""
Write a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""

from sqlalchemy import sessionmaker
from sqlalchemy.orm import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not Found')
    else:
        print('{0}'.format(instance.id))

#!/usr/bin/python3

"""
Write a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name="Califonia")
    sfr_city = City(name="San Francisco")
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
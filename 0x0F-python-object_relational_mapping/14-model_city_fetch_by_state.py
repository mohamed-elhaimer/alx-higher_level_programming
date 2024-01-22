#!/usr/bin/python3
""" script that print all City objects
 from the database hbtn_0e_14_usa
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    citys = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id)
    for city in citys:
        print(city[0] + ": " + "(" + str(city[1]) + ") "
              + city[2])

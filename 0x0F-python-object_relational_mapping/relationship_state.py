#!/usr/bin/python3
"""file that contains the class definition of
 a State and an instance Base = declarative_base()"""
from sqlalchemy import INTEGER, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """id and name attributes of each state"""
    __tablename__ = 'states'
    id = Column(INTEGER, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

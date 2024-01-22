#!/usr/bin/python3
"""
create table classe city
"""
from model_state import Base
from sqlalchemy import Integer, String, ForeignKey, column


class City(Base):
    """ id and name of cities"""
    __tablename__ = "cities"
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name = column(String(128), nullable=False)
    state_id = column(Integer, ForeignKey('states.id'), nullable=False)

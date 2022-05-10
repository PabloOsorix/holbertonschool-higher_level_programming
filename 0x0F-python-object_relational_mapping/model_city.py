#!/usr/bin/python3
"""
Module that contains and define
Class City.
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

Base = declarative_base()


class City(Base):
    """class that allow us create a table
    that contains name, id and state_id of
    cities."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'))

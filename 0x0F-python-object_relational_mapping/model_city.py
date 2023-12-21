#!/usr/bin/python3
"""
module for a model class for a table `cities`.
"""
from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """
    a model class for a table `cities`.
    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)

#!/usr/bin/python
""" holds class Service"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Service(BaseModel, Base):
    """Representation of Service """
    if models.storage_t == "db":
        __tablename__ = 'services'
        name = Column(String(128), nullable=False)
        professional = relationship("Professional",
                              backref="services",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Service"""
        super().__init__(*args, **kwargs)
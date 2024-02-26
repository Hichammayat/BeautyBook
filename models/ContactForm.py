#!/usr/bin/python
""" holds class Contactform"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Contactform(BaseModel, Base):
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'contactforms'
        professional_id = Column(String(60), ForeignKey('professionals.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        message = Column(String(1024), nullable=False)
    else:
        professional_id = ""
        user_id = ""
        message = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
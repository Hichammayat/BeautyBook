#!/usr/bin/python
""" holds class Contactform"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Contactform(BaseModel, Base):
    """Representation of Contactform """
    
    __tablename__ = 'contactforms'
    professional_id = Column(String(60), ForeignKey('professionals.id'), nullable=False)
    message = Column(String(1024), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes Contactform"""
        super().__init__(*args, **kwargs)
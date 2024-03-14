#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    
    __tablename__ = 'cities'
    name = Column(String(60), nullable=False)
    
    

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
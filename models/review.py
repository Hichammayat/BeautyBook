#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review """
    
    __tablename__ = 'reviews'
    professional_id = Column(String(60), ForeignKey('professionals.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    comments = Column(String(1024), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
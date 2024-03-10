#!/usr/bin/python3
""" holds class Professional"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from hashlib import md5

class Professional(BaseModel, Base):
    """Representation of Professional"""
    
    __tablename__ = 'professionals'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    phone_number = Column(String(128), nullable=True)
    city = Column(String(60), nullable=False)
    service_id = Column(String(60), ForeignKey('services.id'), nullable=True)
    biography = Column(String(1024), nullable=True)
    work_hours = Column(String(1024), nullable=True)
    reviews = relationship("Review", backref="professional")
    contactforms = relationship("Contactform", backref="professional")

    def __init__(self, *args, **kwargs):
        """Initializes Professional"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

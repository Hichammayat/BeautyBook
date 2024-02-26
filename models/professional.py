#!/usr/bin/python
""" holds class Professional"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Professional(BaseModel, Base):
    """Representation of Professional """
    if models.storage_t == 'db':
        __tablename__ = 'professionals'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        service_id = Column(String(60), ForeignKey('services.id'), nullable=False)
        biography = Column(String(1024), nullable=False)
        work hours = Column(String(1024), nullable=False)
        contactforms = relationship("Contactform", backref="professional")
    else:
        user_id = ""
        city_id = ""
        service_id = ""
        biography = ""
        work hours = ""

    def __init__(self, *args, **kwargs):
        """initializes Professional"""
        super().__init__(*args, **kwargs)
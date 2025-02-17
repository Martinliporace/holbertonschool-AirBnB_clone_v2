#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.place import Place
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities")

    else:
        name = ""
        state_id = ""

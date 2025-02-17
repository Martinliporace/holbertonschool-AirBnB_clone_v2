#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from os import getenv

if (models.type_storage == "db"):
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if (models.type_storage == "db"):
        city_id = Column(String(60),  ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ returns the list of Review instances with place_id
            equals to the current Place.id"""

            from models import storage

            revs = []
            new_dict = storage.all(self)
            for key, value in new_dict.items():
                if value.place_id == self.id:
                    cities.append(new_dict[key])
            return revs

        @property
        def amenities(self):
            """  returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place """

            return self.amenities

        @amenities.setter
        def amenities_setter(self, amenities=None):
            """setter of amenities"""
            if type(amenities) == Amenity:
                am_list = []
                self.am_ist.append(amenities.id)

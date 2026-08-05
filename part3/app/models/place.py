#!/usr/bin/python3
"""DPlace class."""
from app import db
from app.models.BaseEntity import BaseEntity
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity
from sqlalchemy.orm import validates
from sqlalchemy.orm import relationship


class Place(BaseEntity):
    """Represents a place that can be listed and booked.
    """

    __tablename__ = 'places'


    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Float if hasattr(db, 'Float') else db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    @property
    def title(self):
        """ The title of the place."""
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("title is required and must be a string")
        if len(value) > 100:
            raise ValueError("title must be 100 characters or fewer")
        self._title = value

    @property
    def description(self):
        """detailed description of the place """
        return self._description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("description must be a string")
        self._description = value
    '''
    @property
    def price(self):
        """The price per night for the place."""
        return self._price
    '''

    @validates('price')
    def validate_price (self, key, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("price must be a number")
        if value <= 0:
            raise ValueError("price must be a positive value")
        return value
    '''
    @property
    def latitude(self):
        """The latitude coordinate for the place location."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("latitude must be a number")
        if not -90.0 <= value <= 90.0:
            raise ValueError("latitude must be between -90.0 and 90.0")
        self._latitude = float(value)
    '''

    @validates('latitude')
    def validate_latitude(self, key, value):
        if not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        return value
    
    '''
    @property
    def longitude(self):
        """The longitude coordinate for the place location."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("longitude must be a number")
        if not -180.0 <= value <= 180.0:
            raise ValueError("longitude must be between -180.0 and 180.0")
        self._longitude = float(value)
    '''
    @validates('longitude')
    def validate_longitude(self, key, value):
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        return value

    @property
    def owner(self):
        """The User instance who owns the place."""
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("owner must be a valid User instance")
        self._owner = value
    

    def add_review(self, review):
        """Add a review to the place.
        """
        if not isinstance(review, Review):
            raise ValueError("review must be a valid Review instance")
        session = db.session.object_session(self) or db.session

        if review not in session:
            session.add(review)
            session.flush()

        with db.session.no_autoflush:
            if review not in self.reviews:
                self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place.
        """
        if not isinstance(amenity, Amenity):
            raise TypeError("Expected an Amenity object")

        session = db.session.object_session(self) or db.session

        with db.session.no_autoflush:
            if amenity not in self.amenities:
                if amenity not in session:
                    session.add(amenity)
                    session.flush()
                self.amenities.append(amenity)

    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': {
                'id': self.owner.id,
                'first_name': self.owner.first_name,
                'last_name': self.owner.last_name,
                'email': self.owner.email
            },
            'amenities': [
                {
                    'id': amenity.id,
                    'name': amenity.name
                }
                for amenity in self.amenities
            ]
        }
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id
        }

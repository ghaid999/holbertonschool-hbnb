#!/usr/bin/python3
"""Amenity class."""
from app.models.BaseEntity import BaseEntity

class Amenity(BaseEntity):
    """Represents an amenity that can be associated with a place.
    """

    def __init__(self, name):
        """Initialize a new Amenity instance.
        """
        super().__init__()
        self.name = name

    @property
    def name(self):
        """The name of the amenity."""
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("name is required and must be a string")
        if len(value) > 50:
            raise ValueError("name must be 50 characters or fewer")
        self._name = value

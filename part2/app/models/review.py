#!/usr/bin/python3
"""Defines the Review class."""
from app.models.BaseEntity import BaseEntity
from app.models.user import User


class Review(BaseEntity):
    """Represents a review left by a user for a place.
    """

    def __init__(self, text, rating, place, user):
        """Initialize a new Review instance.
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        """The content of the review."""
        return self._text

    @text.setter
    def text(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("text is required and must be a string")
        self._text = value

    @property
    def rating(self):
        """Rating given to the place."""
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError("rating must be an integer")
        if not 1 <= value <= 5:
            raise ValueError("rating must be between 1 and 5")
        self._rating = value

    @property
    def place(self):
        """The Place instance being reviewed."""
        return self._place

    @place.setter
    def place(self, value):
        from app.models.place import Place
        if not isinstance(value, Place):
            raise ValueError("place must be a valid Place instance")
        self._place = value

    @property
    def user(self):
        """The User instance who wrote the review."""
        return self._user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("user must be a valid User instance")
        self._user = value

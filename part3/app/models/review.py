#!/usr/bin/python3
"""Defines the Review class."""
from app.models.BaseEntity import BaseEntity
from app.models.user import User
from app import db
from sqlalchemy.orm import validates


class Review(BaseEntity):
    """Represents a review left by a user for a place.
    """
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id', ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    place = db.relationship("Place", back_populates="reviews")
    user = db.relationship("User", backref="reviews")


    @validates('rating')
    def validate_rating(self, key, value):
        """Vérifie que le rating est entre 1 et 5."""
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        return value

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id
        }

#!/usr/bin/python3
"""Amenity class."""

from sqlalchemy.orm import validates
from app import db
from app.models.BaseEntity import BaseEntity


class Amenity(BaseEntity):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError("name is required and must be a string")
        if len(value) > 50:
            raise ValueError("name must be 50 characters or fewer")
        return value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
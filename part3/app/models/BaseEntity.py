#!/usr/bin/env python3
"""
BaseEntity class.
"""

from app import db
import uuid
from datetime import datetime
from sqlalchemy.sql import func


class BaseEntity(db.Model):
    """Base class for all entities."""
    __abstract__ = True
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())


    def save(self):
        """Update the updated_at timestamp and commit changes to the database"""
        self.updated_at = func.now()
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
        

'''
    def __init__(self):
        """Initialize common attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the modification timestamp."""
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Update object attributes from a dictionary.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.save()
'''

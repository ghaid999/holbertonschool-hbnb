#!/usr/bin/env python3
"""
BaseEntity class.
"""

import uuid
from datetime import datetime


class BaseEntity:
    """Base class for all entities."""

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
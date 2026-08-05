#!/usr/bin/python3
"""User class."""
import re
from app.models.BaseEntity import BaseEntity
from app import bcrypt
from app import db
from sqlalchemy.orm import validates

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class User(BaseEntity):
    """Represents a user of the HBnB application.
    """
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)


    @validates('first_name', 'last_name')
    def validate_name(self, key, value):
        """Validate the first name and last name length before storing."""
        if not isinstance(value, str):
            raise TypeError(f"{key.replace('_', ' ').title()} must be a string")
        if len(value) > 50:
            raise ValueError(f"{key.replace('_', ' ').title()} must be at most 50 characters")
        return value
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    @validates('email')
    def validate_email(self, key, email):
        """Validate the email format before storing it."""
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        return email

    @validates('first_name', 'last_name')
    def validate_name(self, key, value):
        """Validate the first name and last name length before storing."""
        if not isinstance(value, str):
            raise TypeError(f"{key.replace('_', ' ').title()} must be a string")
        if len(value) > 50:
            raise ValueError(f"{key.replace('_', ' ').title()} must be at most 50 characters")
        return value

    def to_dict(self):
        """Convert the User object to a dictionary."""
        """Convert the User object to a dictionary."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
        }
    # خلصنا فالديشن





    '''
    #من هنا مب فاهمه ليه احتجنا اللي تحت؟
    @property
    def is_admin(self):
        """Whether the user has administrative privileges."""
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_admin must be a boolean")
        self.is_admin = value
    '''
    
    def add_place(self, place):
        """Add a place owned by the user."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review written by the user."""
        self.reviews.append(review)
'''  
    @property
    def first_name(self):
        """The user first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("first_name is required and must be a string")
        if len(value) > 50:
            raise ValueError("first_name must be 50 characters or fewer")
        self._first_name = value

    @property
    def last_name(self):
        """The user last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("last_name is required and must be a string")
        if len(value) > 50:
            raise ValueError("last_name must be 50 characters or fewer")
        self._last_name = value

    @property
    def email(self):
        """The user email address."""
        return self._email

    @email.setter
    def email(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("email is required and must be a string")
        if not EMAIL_REGEX.match(value):
            raise ValueError("email must be a valid email address")
        self._email = value
'''




-- ============================================================
-- HBnB Project - Database Schema (part3)
-- Target engine: SQLite (matches config.py -> sqlite:///hbnb.db)
-- Tables: User, Place, Review, Amenity, Place_Amenity
-- ============================================================
 
PRAGMA foreign_keys = ON;
 
DROP TABLE IF EXISTS Place_Amenity;
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS Place;
DROP TABLE IF EXISTS Amenity;
DROP TABLE IF EXISTS User;
 
-- ------------------------------------------------------------
-- User Table
-- Mirrors BaseEntity (id, created_at, updated_at) + User fields
-- ------------------------------------------------------------
CREATE TABLE User (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
-- ------------------------------------------------------------
-- Place Table
-- ------------------------------------------------------------
CREATE TABLE Place (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    latitude FLOAT NOT NULL CHECK (latitude BETWEEN -90.0 AND 90.0),
    longitude FLOAT NOT NULL CHECK (longitude BETWEEN -180.0 AND 180.0),
    owner_id CHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE
);
 
-- ------------------------------------------------------------
-- Review Table
-- ------------------------------------------------------------
CREATE TABLE Review (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    UNIQUE (user_id, place_id)
);
 
-- ------------------------------------------------------------
-- Amenity Table
-- ------------------------------------------------------------
CREATE TABLE Amenity (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
-- ------------------------------------------------------------
-- Place_Amenity Table (Many-to-Many, matches Place.amenities /
-- Place.add_amenity() relationship in app/models/place.py)
-- ------------------------------------------------------------
CREATE TABLE Place_Amenity (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id) ON DELETE CASCADE
);
 

-- ============================================================
-- HBnB Project - Initial Data
-- Inserts: Administrator user + base Amenities
-- ============================================================

-- ------------------------------------------------------------
-- Administrator User
-- Password 'admin1234' hashed with bcrypt (flask-bcrypt, cost 12)
-- Matches User.hash_password() in app/models/user.py
-- ------------------------------------------------------------
import sqlite3

INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$NoLeYrq9g/iYeSWHQlAxgOZxQqJCwbhc9hvkCOOcugzclcfRgydYy',
    TRUE,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- Initial Amenities
-- ------------------------------------------------------------
INSERT INTO amenities (id, name, created_at, updated_at)
VALUES ('ac433b4f-ade1-483a-8e6a-ae7ffdb719d3', 'WiFi', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO amenities (id, name, created_at, updated_at)
VALUES ('625a9f02-d49d-44f4-958c-5befd6199aa4', 'Swimming Pool', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO amenities (id, name, created_at, updated_at)
VALUES ('cd15a52a-ca28-4364-b015-26ab124fb67c', 'Air Conditioning', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ============================================================
-- HBnB Project - CRUD Test Script
-- Run AFTER 1_schema.sql and 2_initial_data.sql
-- ============================================================

-- ------------------------------------------------------------
-- 1) Verify admin user
-- ------------------------------------------------------------
SELECT id, email, is_admin FROM users WHERE email = 'admin@hbnb.io';

-- ------------------------------------------------------------
-- 2) Verify amenities
-- ------------------------------------------------------------
SELECT id, name FROM amenities;

-- ------------------------------------------------------------
-- 3) CREATE - add a regular user
-- ------------------------------------------------------------
INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at)
VALUES ('11111111-1111-1111-1111-111111111111', 'Shatha', 'Test',
        'shatha.test@example.com', '$2b$12$placeholderhash', FALSE,
        CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ------------------------------------------------------------
-- 4) CREATE - add a place owned by that user
-- ------------------------------------------------------------
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES ('22222222-2222-2222-2222-222222222222', 'Cozy Studio in Riyadh',
        'A quiet studio near the city center.', 250.00, 24.7136, 46.6753,
        '11111111-1111-1111-1111-111111111111',
        CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ------------------------------------------------------------
-- 5) CREATE - link place to an amenity (Many-to-Many)
-- ------------------------------------------------------------
INSERT INTO place_amenity (place_id, amenity_id)
VALUES ('22222222-2222-2222-2222-222222222222',
        'ac433b4f-ade1-483a-8e6a-ae7ffdb719d3');

-- ------------------------------------------------------------
-- 6) CREATE - add a review
-- ------------------------------------------------------------
INSERT INTO reviews (id, text, rating, user_id, place_id, created_at, updated_at)
VALUES ('33333333-3333-3333-3333-333333333333',
        'Great place, very clean!', 5,
        '11111111-1111-1111-1111-111111111111',
        '22222222-2222-2222-2222-222222222222',
        CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ------------------------------------------------------------
-- 7) READ - join place with its owner and amenities
-- ------------------------------------------------------------
SELECT p.title, u.first_name AS owner, a.name AS amenity
FROM places p
JOIN users u ON p.owner_id = u.id
JOIN place_amenity pa ON p.id = pa.place_id
JOIN amenities a ON pa.amenity_id = a.id;

-- ------------------------------------------------------------
-- 8) UPDATE - change the place price
-- ------------------------------------------------------------
UPDATE places
SET price = 275.00, updated_at = CURRENT_TIMESTAMP
WHERE id = '22222222-2222-2222-2222-222222222222';

-- ------------------------------------------------------------
-- 9) Attempt duplicate review (should FAIL - unique user_id/place_id)
-- ------------------------------------------------------------
-- INSERT INTO reviews (id, text, rating, user_id, place_id, created_at, updated_at)
-- VALUES ('44444444-4444-4444-4444-444444444444',
--         'Second review attempt', 4,
--         '11111111-1111-1111-1111-111111111111',
--         '22222222-2222-2222-2222-222222222222',
--         CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ------------------------------------------------------------
-- 10) DELETE - remove the test review
-- ------------------------------------------------------------
DELETE FROM reviews WHERE id = '33333333-3333-3333-3333-333333333333';

-- ------------------------------------------------------------
-- 11) Cleanup test data (place, amenity link, user)
-- ------------------------------------------------------------
DELETE FROM place_amenity WHERE place_id = '22222222-2222-2222-2222-222222222222';
DELETE FROM places WHERE id = '22222222-2222-2222-2222-222222222222';
DELETE FROM users WHERE id = '11111111-1111-1111-1111-111111111111';

#!/bin/bash

# ======================================================================
# API TESTING DOCUMENTATION (ALL CLASSES)
# Models: Users, Amenities, Places, Reviews
# ======================================================================


# ======================================================================
# PART 1: USERS API
# ======================================================================

# Test 1 — Create User (Future Owner)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com"
}'
# Expected Response:
# {"id": "b5872767-1d8d-4f97-bfbb-132dea944c1b", "first_name": "John", "last_name": "Doe", "email": "john@example.com"}
# Expected Result: 201 Created


# Test 2 — Create User (Validation Error - Missing Email)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Jane",
  "last_name": "Doe"
}'
# Expected Response:
# {"error": "Email is required"}
# Expected Result: 400 Bad Request


# Test 3 — GET all Users
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/users/
# Expected Response:
# [{"id": "b5872767-1d8d-4f97-bfbb-132dea944c1b", "first_name": "John", "last_name": "Doe", "email": "john@example.com"}]
# Expected Result: 200 OK


# Test 4 — GET User by ID
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/users/b5872767-1d8d-4f97-bfbb-132dea944c1b
# Expected Response:
# {"id": "b5872767-1d8d-4f97-bfbb-132dea944c1b", "first_name": "John", "last_name": "Doe", "email": "john@example.com"}
# Expected Result: 200 OK


# Test 5 — Update User
# ----------------------------------------------------------------------
curl -X PUT http://127.0.0.1:5000/api/v1/users/b5872767-1d8d-4f97-bfbb-132dea944c1b \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Johnny"
}'
# Expected Response:
# {"message": "User updated successfully"}
# Expected Result: 200 OK



# ======================================================================
# PART 2: AMENITIES API
# ======================================================================

# Test 6 — Create Amenity
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Wi-Fi"
}'
# Expected Response:
# {"id": "a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab", "name": "Wi-Fi"}
# Expected Result: 201 Created


# Test 7 — Create Amenity (Validation Error - Missing Name)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{}'
# Expected Response:
# {"error": "Name is required"}
# Expected Result: 400 Bad Request


# Test 8 — GET all Amenities
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/amenities/
# Expected Response:
# [{"id": "a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab", "name": "Wi-Fi"}]
# Expected Result: 200 OK


# Test 9 — GET Amenity by ID
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/amenities/a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab
# Expected Response:
# {"id": "a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab", "name": "Wi-Fi"}
# Expected Result: 200 OK


# Test 10 — Update Amenity
# ----------------------------------------------------------------------
curl -X PUT http://127.0.0.1:5000/api/v1/amenities/a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab \
-H "Content-Type: application/json" \
-d '{
  "name": "High-Speed Wi-Fi"
}'
# Expected Response:
# {"message": "Amenity updated successfully"}
# Expected Result: 200 OK



# ======================================================================
# PART 3: PLACES API
# ======================================================================

# Test 11 — Create Place
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "b5872767-1d8d-4f97-bfbb-132dea944c1b",
  "amenities": ["a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab"]
}'
# Expected Response:
# {"id": "36870767-26e6-4ee7-b956-e59df35384c2", "title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner_id": "b5872767-1d8d-4f97-bfbb-132dea944c1b"}
# Expected Result: 201 Created


# Test 12 — Create Place (Validation Error - Negative Price)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Cheap Room",
  "price": -50.0,
  "owner_id": "b5872767-1d8d-4f97-bfbb-132dea944c1b"
}'
# Expected Response:
# {"error": "Price must be a positive number"}
# Expected Result: 400 Bad Request


# Test 13 — GET all Places
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/places/
# Expected Response:
# [{"id": "36870767-26e6-4ee7-b956-e59df35384c2", "title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner_id": "b5872767-1d8d-4f97-bfbb-132dea944c1b"}]
# Expected Result: 200 OK


# Test 14 — GET Place by ID
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/places/36870767-26e6-4ee7-b956-e59df35384c2
# Expected Response:
# {"id": "36870767-26e6-4ee7-b956-e59df35384c2", "title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner": {"id": "b5872767-1d8d-4f97-bfbb-132dea944c1b", "first_name": "Johnny", "last_name": "Doe", "email": "john@example.com"}, "amenities": [{"id": "a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab", "name": "High-Speed Wi-Fi"}]}
# Expected Result: 200 OK


# Test 15 — Update Place
# ----------------------------------------------------------------------
curl -X PUT http://127.0.0.1:5000/api/v1/places/36870767-26e6-4ee7-b956-e59df35384c2 \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Apartment",
  "price": 150.0
}'
# Expected Response:
# {"message": "Place updated successfully"}
# Expected Result: 200 OK


# Test 16 — Place Not Found
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/places/fake-id
# Expected Response:
# {"error": "Place not found"}
# Expected Result: 404 Not Found



# ======================================================================
# PART 4: REVIEWS API
# ======================================================================

# Test 17 — Create Second User (Reviewer)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Jane",
  "last_name": "Smith",
  "email": "jane@example.com"
}'
# Expected Response:
# {"id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7", "first_name": "Jane", "last_name": "Smith", "email": "jane@example.com"}
# Expected Result: 201 Created


# Test 18 — Create Review (Success)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Amazing place!",
  "rating": 5,
  "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7",
  "place_id": "36870767-26e6-4ee7-b956-e59df35384c2"
}'
# Expected Response:
# {"id": "4e2daf28-2786-4818-a315-953fc5ee2120", "text": "Amazing place!", "rating": 5, "place_id": "36870767-26e6-4ee7-b956-e59df35384c2", "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7"}
# Expected Result: 201 Created


# Test 19 — Rating Below 1 (Validation Error)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Bad rating",
  "rating": 0,
  "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7",
  "place_id": "36870767-26e6-4ee7-b956-e59df35384c2"
}'
# Expected Response:
# {"error": "rating must be between 1 and 5"}
# Expected Result: 400 Bad Request


# Test 20 — Rating Above 5 (Validation Error)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Bad rating",
  "rating": 6,
  "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7",
  "place_id": "36870767-26e6-4ee7-b956-e59df35384c2"
}'
# Expected Response:
# {"error": "rating must be between 1 and 5"}
# Expected Result: 400 Bad Request


# Test 21 — User Not Found (Validation Error)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Review",
  "rating": 5,
  "user_id": "fake-user",
  "place_id": "36870767-26e6-4ee7-b956-e59df35384c2"
}'
# Expected Response:
# {"error": "'User not found'"}
# Expected Result: 400 Bad Request


# Test 22 — Place Not Found (Validation Error)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Review",
  "rating": 5,
  "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7",
  "place_id": "fake-place"
}'
# Expected Response:
# {"error": "'Place not found'"}
# Expected Result: 400 Bad Request


# Test 23 — Owner Reviews Own Place (Validation Error)
# ----------------------------------------------------------------------
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "My own place",
  "rating": 5,
  "user_id": "b5872767-1d8d-4f97-bfbb-132dea944c1b",
  "place_id": "36870767-26e6-4ee7-b956-e59df35384c2"
}'
# Expected Response:
# {"error": "User cannot review their own place"}
# Expected Result: 400 Bad Request


# Test 24 — GET all Reviews
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/reviews/
# Expected Response:
# [{"id": "4e2daf28-2786-4818-a315-953fc5ee2120", "text": "Amazing place!", "rating": 5, "place_id": "36870767-26e6-4ee7-b956-e59df35384c2", "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7"}]
# Expected Result: 200 OK


# Test 25 — GET Review by ID
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/reviews/4e2daf28-2786-4818-a315-953fc5ee2120
# Expected Response:
# {"id": "4e2daf28-2786-4818-a315-953fc5ee2120", "text": "Amazing place!", "rating": 5, "place_id": "36870767-26e6-4ee7-b956-e59df35384c2", "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7"}
# Expected Result: 200 OK


# Test 26 — GET Reviews specific to a Place
# ----------------------------------------------------------------------
curl http://127.0.0.1:5000/api/v1/places/36870767-26e6-4ee7-b956-e59df35384c2/reviews/
# Expected Response:
# [{"id": "4e2daf28-2786-4818-a315-953fc5ee2120", "text": "Amazing place!", "rating": 5, "place_id": "36870767-26e6-4ee7-b956-e59df35384c2", "user_id": "18a4fbe7-1342-4f7b-b9d1-4a580f5030f7"}]
# Expected Result: 200 OK


# Test 27 — Update Review
# ----------------------------------------------------------------------
curl -X PUT http://127.0.0.1:5000/api/v1/reviews/4e2daf28-2786-4818-a315-953fc5ee2120 \
-H "Content-Type: application/json" \
-d '{
  "text": "Updated review",
  "rating": 4
}'
# Expected Response:
# {"message": "Review updated successfully"}
# Expected Result: 200 OK


# Test 28 — Delete Review
# ----------------------------------------------------------------------
curl -X DELETE http://127.0.0.1:5000/api/v1/reviews/4e2daf28-2786-4818-a315-953fc5ee2120
# Expected Response:
# {"message": "Review deleted successfully"}
# Expected Result: 200 OK

#!/usr/bin/python3
import unittest
from app import create_app


class TestAmenityEndpoints(unittest.TestCase):
    """Test suite for Amenity endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # ============= POST /api/v1/amenities/ =============

    def test_create_amenity_success(self):
        """Create valid amenity - expects 201"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi",
            "description": "High-speed internet"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Wi-Fi")

    def test_create_amenity_empty_name(self):
        """Empty name - expects 400"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "",
            "description": "No name"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_amenity_name_too_long(self):
        """Name over 50 chars - expects 400"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "A" * 51,
            "description": "Too long"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_amenity_missing_name(self):
        """Missing name field - expects 400"""
        response = self.client.post('/api/v1/amenities/', json={
            "description": "No name provided"
        })
        self.assertEqual(response.status_code, 400)

    # ============= GET /api/v1/amenities/ =============

    def test_get_all_amenities(self):
        """Retrieve list of amenities - expects 200"""
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    # ============= GET /api/v1/amenities/<id> =============

    def test_get_amenity_by_id_success(self):
        """Get existing amenity by ID - expects 200"""
        post = self.client.post('/api/v1/amenities/', json={
            "name": "Pool",
            "description": "Outdoor pool"
        })
        amenity_id = post.get_json()["id"]
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], amenity_id)

    def test_get_amenity_not_found(self):
        """Get non-existent amenity - expects 404"""
        response = self.client.get('/api/v1/amenities/nonexistent-id')
        self.assertEqual(response.status_code, 404)

    # ============= PUT /api/v1/amenities/<id> =============

    def test_update_amenity_success(self):
        """Update existing amenity - expects 200"""
        post = self.client.post('/api/v1/amenities/', json={
            "name": "Parking",
            "description": "Free parking"
        })
        amenity_id = post.get_json()["id"]
        response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Paid Parking",
            "description": "Paid parking lot"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_amenity_not_found(self):
        """Update non-existent amenity - expects 404"""
        response = self.client.put('/api/v1/amenities/nonexistent-id', json={
            "name": "Pool"
        })
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit Tests for HBnB API Endpoints"""

import unittest
from app import create_app


class TestAmenityEndpoints(unittest.TestCase):
    """Test suite for Amenity endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity_success(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Wi-Fi")

    def test_get_all_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_amenity_by_id_success(self):
        post = self.client.post('/api/v1/amenities/', json={
            "name": "Pool"
        })
        amenity_id = post.get_json()["id"]
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], amenity_id)

    def test_update_amenity_success(self):
        post = self.client.post('/api/v1/amenities/', json={
            "name": "Parking"
        })
        amenity_id = post.get_json()["id"]
        response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Paid Parking"
        })
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

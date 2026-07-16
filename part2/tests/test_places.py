#!/usr/bin/python3
"""Unit Tests for HBnB API Endpoints"""

import unittest
import uuid
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):
    """Test suite for Place endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        unique_email = f"owner.place.{uuid.uuid4()}@example.com"
        res = self.client.post('/api/v1/users/', json={
            "first_name": "Owner",
            "last_name": "User",
            "email": unique_email
        })
        self.owner_id = res.get_json()["id"]

    def _valid_place(self, **overrides):
        data = {
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": self.owner_id,
            "amenities": []
        }
        data.update(overrides)
        return data

    def test_create_place_success(self):
        response = self.client.post('/api/v1/places/', json=self._valid_place())
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Cozy Apartment")

    def test_get_all_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_place_by_id_success(self):
        post = self.client.post('/api/v1/places/', json=self._valid_place())
        place_id = post.get_json()["id"]
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("owner", data)
        self.assertEqual(data["owner"]["id"], self.owner_id)

    def test_get_place_not_found(self):
        response = self.client.get('/api/v1/places/fake-id')
        self.assertEqual(response.status_code, 404)

    def test_update_place_success(self):
        post = self.client.post('/api/v1/places/', json=self._valid_place())
        place_id = post.get_json()["id"]
        response = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "Updated Apartment",
            "price": 150.0
        })
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

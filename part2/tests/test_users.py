#!/usr/bin/python3
"""Unit Tests for HBnB API Endpoints"""

import unittest
import uuid
from app import create_app


class TestUserEndpoints(unittest.TestCase):
    """Test suite for User endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_success(self):
        unique_email = f"john.doe.{uuid.uuid4()}@example.com"
        response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": unique_email
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["first_name"], "John")
        self.assertEqual(data["email"], unique_email)

    def test_get_all_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_user_by_id_success(self):
        unique_email = f"jane.smith.{uuid.uuid4()}@example.com"
        post = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Smith",
            "email": unique_email
        })
        user_id = post.get_json()["id"]
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], user_id)

    def test_update_user_success(self):
        unique_email = f"update.user.{uuid.uuid4()}@example.com"
        post = self.client.post('/api/v1/users/', json={
            "first_name": "Old",
            "last_name": "Name",
            "email": unique_email
        })
        user_id = post.get_json()["id"]
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Johnny"
        })
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

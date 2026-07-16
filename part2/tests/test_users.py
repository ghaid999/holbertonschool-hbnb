#!/usr/bin/python3
import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):
    """Test suite for User endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # ============= POST /api/v1/users/ =============

    def test_create_user_success(self):
        """Create a valid user - expects 201"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["first_name"], "Jane")
        self.assertEqual(data["email"], "jane.doe@example.com")
        self.assertNotIn("password", data)

    def test_create_user_empty_first_name(self):
        """Empty first_name - expects 400"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "Doe",
            "email": "test1@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_empty_last_name(self):
        """Empty last_name - expects 400"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "",
            "email": "test2@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_email(self):
        """Invalid email format - expects 400"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "invalid-email",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_duplicate_email(self):
        """Duplicate email - expects 400"""
        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "duplicate@example.com",
            "password": "password123"
        }
        self.client.post('/api/v1/users/', json=payload)
        response = self.client.post('/api/v1/users/', json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_create_user_short_password(self):
        """Password under 8 chars - expects 400"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "shortpass@example.com",
            "password": "123"
        })
        self.assertEqual(response.status_code, 400)

    # ============= GET /api/v1/users/ =============

    def test_get_all_users(self):
        """Retrieve list of users - expects 200"""
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    # ============= GET /api/v1/users/<id> =============

    def test_get_user_by_id_success(self):
        """Get existing user by ID - expects 200"""
        post = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Smith",
            "email": "john.smith@example.com",
            "password": "password123"
        })
        user_id = post.get_json()["id"]
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], user_id)

    def test_get_user_not_found(self):
        """Get non-existent user - expects 404"""
        response = self.client.get('/api/v1/users/nonexistent-id')
        self.assertEqual(response.status_code, 404)

    # ============= PUT /api/v1/users/<id> =============

    def test_update_user_success(self):
        """Update existing user - expects 200"""
        post = self.client.post('/api/v1/users/', json={
            "first_name": "Old",
            "last_name": "Name",
            "email": "update.user@example.com",
            "password": "password123"
        })
        user_id = post.get_json()["id"]
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "New",
            "last_name": "Name",
            "email": "update.user@example.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_user_not_found(self):
        """Update non-existent user - expects 404"""
        response = self.client.put('/api/v1/users/nonexistent-id', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com"
        })
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

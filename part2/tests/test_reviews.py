#!/usr/bin/python3
"""Unit Tests for HBnB API Endpoints"""

import unittest
import uuid
from app import create_app


class TestReviewEndpoints(unittest.TestCase):
    """Test suite for Review endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Create owner
        owner_email = f"owner.review.{uuid.uuid4()}@example.com"
        res = self.client.post('/api/v1/users/', json={
            "first_name": "Owner",
            "last_name": "User",
            "email": owner_email
        })
        self.owner_id = res.get_json()["id"]

        # Create reviewer
        reviewer_email = f"reviewer.test.{uuid.uuid4()}@example.com"
        res = self.client.post('/api/v1/users/', json={
            "first_name": "Reviewer",
            "last_name": "User",
            "email": reviewer_email
        })
        self.reviewer_id = res.get_json()["id"]

        # Create place
        res = self.client.post('/api/v1/places/', json={
            "title": "Test Place",
            "description": "A place for reviews",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": self.owner_id,
            "amenities": []
        })
        self.place_id = res.get_json()["id"]

    def _valid_review(self, **overrides):
        data = {
            "text": "Amazing place!",
            "rating": 5,
            "user_id": self.reviewer_id,
            "place_id": self.place_id
        }
        data.update(overrides)
        return data

    def test_create_review_success(self):
        response = self.client.post('/api/v1/reviews/', json=self._valid_review())
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["text"], "Amazing place!")

    def test_create_review_rating_below_minimum(self):
        response = self.client.post('/api/v1/reviews/', json=self._valid_review(rating=0))
        self.assertEqual(response.status_code, 400)
        self.assertIn("rating must be between 1 and 5", response.get_json().get("error", ""))

    def test_create_review_rating_above_maximum(self):
        response = self.client.post('/api/v1/reviews/', json=self._valid_review(rating=6))
        self.assertEqual(response.status_code, 400)

    def test_create_review_invalid_user(self):
        response = self.client.post('/api/v1/reviews/', json=self._valid_review(
            user_id="fake-user"
        ))
        self.assertEqual(response.status_code, 400)

    def test_create_review_invalid_place(self):
        response = self.client.post('/api/v1/reviews/', json=self._valid_review(
            place_id="fake-place"
        ))
        self.assertEqual(response.status_code, 400)

    def test_create_review_owner_reviews_own_place(self):
        response = self.client.post('/api/v1/reviews/', json=self._valid_review(
            user_id=self.owner_id
        ))
        self.assertEqual(response.status_code, 400)
        self.assertIn("User cannot review their own place", response.get_json().get("error", ""))

    def test_get_all_reviews(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_review_by_id_success(self):
        post = self.client.post('/api/v1/reviews/', json=self._valid_review())
        review_id = post.get_json()["id"]
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], review_id)

    def test_get_place_reviews(self):
        self.client.post('/api/v1/reviews/', json=self._valid_review())
        response = self.client.get(f'/api/v1/places/{self.place_id}/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_update_review_success(self):
        post = self.client.post('/api/v1/reviews/', json=self._valid_review())
        review_id = post.get_json()["id"]
        response = self.client.put(f'/api/v1/reviews/{review_id}', json={
            "text": "Updated review",
            "rating": 4
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_review_success(self):
        post = self.client.post('/api/v1/reviews/', json=self._valid_review())
        review_id = post.get_json()["id"]
        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

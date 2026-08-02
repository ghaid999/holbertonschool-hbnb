from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):

    @jwt_required()
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""

        review_data = api.payload

        current_user = get_jwt_identity()
        review_data['user_id'] = current_user

        place = facade.get_place(review_data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 400
        
        if str(place.owner.id) == current_user:
            return {
                'error': 'User cannot review their own place'
            }, 400
        
        reviews = facade.get_all_reviews()
        for review in reviews:
            if review.user.id == current_user and review.place.id == review_data['place_id']:
                return {
                    'error': 'User has already reviewed this place'
                }, 400 

        try:
            new_review = facade.create_review(review_data)
            return new_review.to_dict(), 201

        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()

        return [
            review.to_dict()
            for review in reviews
        ], 200


@api.route('/<review_id>')
class ReviewResource(Resource):

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        return review.to_dict(), 200
    
    @jwt_required()
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload

        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        current_user_claims = get_jwt()
        is_admin = current_user_claims.get('is_admin', False)
        current_user = get_jwt_identity()

        # Allow update if user is admin OR if they own the review
        if not is_admin and str(review.user.id) != current_user:
            return {
                'error': 'Unauthorized action'
            }, 403

        review_data['user_id'] = review.user.id
        review_data['place_id'] = review.place.id
        
        try:
            facade.update_review(review_id, review_data)

            return {
                'message': 'Review updated successfully'
            }, 200 

        except Exception as e:
            return {'error': str(e)}, 400

    @jwt_required()
    @api.response(403, 'Unauthorized action')
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        current_user_claims = get_jwt()
        is_admin = current_user_claims.get('is_admin', False)
        current_user = get_jwt_identity()

        # Allow deletion if user is admin OR if they own the review
        if not is_admin and str(review.user.id) != current_user:
            return {
                'error': 'Unauthorized action'
            }, 403

        try:
            facade.delete_review(review_id)

            return {
                'message': 'Review deleted successfully'
            }, 200

        except Exception as e:
            return {'error': str(e)}, 400

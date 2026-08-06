from app.persistence.repository import SQLAlchemyRepository
from app.persistence.user_repository import UserRepository
from app.persistence.place_repository import PlaceRepository
from app.persistence.amenity_repository import AmenityRepository
from app.persistence.review_repository import ReviewRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app import db



class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()
        
   # User Methods
    def create_user(self, user_data):

        if 'password' not in user_data or not user_data['password']:
            raise ValueError("Password is required")

        password = user_data.pop('password')
        
        user = User(**user_data)
        user.hash_password(password)
        #self.user_repo.add(user)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)
        return self.user_repo.get(user_id)


    # Amenity Methods

    def create_amenity(self, amenity_data):
        """Creates a new amenity."""
        name = amenity_data.get('name')
        existing_amenity = self.amenity_repo.get_amenity_by_name(name)
        if existing_amenity:
            raise ValueError("Amenity with this name already exists")

        amenity = Amenity(**amenity_data)
        #self.amenity_repo.add(amenity)
        db.session.add(amenity)
        db.session.commit()
        return amenity

    def get_amenity_by_name(self, name):
        """Retrieve an amenity by its name using the AmenityRepository."""
        amenity = self.amenity_repo.get_amenity_by_name(name)
        return amenity
    

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)

    def create_place(self, place_data):
        #user = self.user_repo.get(owner_id) if hasattr(self.user_repo, 'get') else self.user_repo.get_by_attribute('id', owner_id)
        user = self.user_repo.get(place_data['owner_id'])
        if not user:
            raise KeyError('Invalid owner ID')

        amenities = place_data.pop("amenities", [])
        for amenity_id in amenities:
            amenity = self.get_amenity(amenity_id)
            if not amenity:
                raise KeyError("Invalid amenity ID")

        place = Place(**place_data)

        #self.place_repo.add(place)
        db.session.add(place)
        db.session.commit()
        return place
    

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)
        '''
    #start of places
    def create_place(self, place_data):

        user = self.user_repo.get_by_attribute('id', place_data['owner_id'])
        if not user:
            raise KeyError('Invalid input data')
        del place_data['owner_id']
        place_data['owner'] = user
        amenities = place_data.pop("amenities", [])

        amenity_objects = []

        for amenity_id in amenities:
            amenity = self.get_amenity(amenity_id)

        if not amenity:
            raise KeyError("Invalid amenity ID")

        amenity_objects.append(amenity)

        place = Place(**place_data)

        self.place_repo.add(place)

        user.add_place(place)

        for amenity in amenity_objects:
            place.add_amenity(amenity)

        db.session.add(place)
        db.session.commit()
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)
    #end of places
    '''
    #start of review
    def create_review(self, review_data):
        user = self.user_repo.get(review_data['user_id'])

        if not user:
            raise KeyError('User not found')

        place = self.place_repo.get(review_data['place_id'])

        if not place:
            raise KeyError('Place not found')

        if place.owner.id == user.id:
            raise ValueError(
                'User cannot review their own place'
            )

       # del review_data['user_id']
        # review_data['user'] = user

        # del review_data['place_id']
       #  review_data['place'] = place

        review = Review(**review_data)

       # self.review_repo.add(review)
        db.session.add(review)
        db.session.commit()
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)
        return self.review_repo.get(review_id)
    
    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        
        if not review:
            return False
            
        self.review_repo.delete(review_id)
        return True

    def authenticate_user(self, email, password):
        """Authenticate a user by email and password."""
        user = self.get_user_by_email(email)
        if user and user.verify_password(password):
            return user
        return None

    def get_review_by_place_and_user(self, place_id, user_id):
        """Retrieve a review by place_id and user_id."""
        return Review.query.filter_by(place_id=place_id, user_id=user_id).first()
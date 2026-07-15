from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass


    #start of places
    def create_place(self, place_data):
        """Create and store a new place."""
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve a place by ID."""
        return self.place_repo.get(place_id)
    
    def get_all_places(self):
        """Retrieve all places."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update place details if the place exists."""
        place = self.place_repo.get(place_id)
        if not place:
            return None
        
        for key in ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id', 'amenities']:
            if key in place_data:
                setattr(place, key, place_data[key])
        
        self.place_repo.update(place_id, place_data)
        return place
        #end of places

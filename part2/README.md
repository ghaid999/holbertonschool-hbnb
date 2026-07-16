# HBnB

## 1. Project Title & Short Description

In this phase of the project, we implement the core functionality of the
application using Python and Flask. We build the Presentation and
Business Logic layers, along with the methods and API endpoints based
on what we designed in Part 1.

## 2. Project Structure

This is our structure:

```text
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

- `app/api/` — this is the Presentation layer. Each file defines a
  Flask-RESTx `Namespace` with its endpoints.
- `app/models/` — this is the Business Logic layer. It handles the UUID
  and the important operations that make sure each object keeps the
  right information.
- `app/services/facade.py` — this is the Facade layer. It's the
  connection between the API and the rest of the application.
- `app/persistence/repository.py` — this is the Persistence layer.
- `run.py` — this is where we run the application.
- `config.py` — contains the necessary settings.
- `requirements.txt` — flask and flask-restx.
- `README.md` — the overview of this phase.

## 3. Installation

```bash
pip install -r requirements.txt
```

## 4. Running the Application

```bash
python3 run.py
```

Once running, view the interactive API docs at
`http://127.0.0.1:5000/api/v1/`.

## 5. Business Logic Layer

**BaseEntity**: all the other classes inherit from this.
- `id`: a UUID4 string, generated automatically on creation.
- `created_at` / `updated_at`: timestamps.
- `update(data)`: updates the data.

**User**: the user class.
- `first_name`, `last_name`(string): must be a string and not empty, 50-character max.
- `email`(string): must be in the correct format.
- `is_admin` (Boolean): indicates whether the user has admin privileges.

**Place**: the place class.
- `title` (String): must be a string and not empty, 100-character max.
- `description` (String): optional.
- `price` (Float): must be a positive value.
- `latitude` and `longitude` (Float): must be numbers, not empty, and within range.
- `owner` (User): tells us who owns the place.

**Review**: the review class.
- `text` (String): must be a string and not empty.
- `rating` (Integer): the rating for the place, must be an integer, not empty, and within range.
- `place` (Place): the relationship between the review and the place.
- `user` (User): the relationship between the review and the user who wrote it.

**Amenity**: the amenity class.
- `name` (String): the name of the amenity, must be a string and not empty.

### Relationships

- A User can own many Places (one-to-many).
- A Place can have many Reviews (one-to-many).
- A Place can have many Amenities, and an Amenity can belong to many
  Places (many-to-many).

## 6. Endpoints

| Method | Endpoint                              | Description             |
|--------|----------------------------------------|--------------------------|
| POST   | `/api/v1/users/`                        | Create a user            |
| GET    | `/api/v1/users/`                        | List all users           |
| GET    | `/api/v1/users/<id>`                    | Get a user by id         |
| PUT    | `/api/v1/users/<id>`                    | Update a user            |
| POST   | `/api/v1/places/`                       | Create a place           |
| GET    | `/api/v1/places/`                       | List all places          |
| GET    | `/api/v1/places/<id>`                   | Get a place by id        |
| PUT    | `/api/v1/places/<id>`                   | Update a place           |
| POST   | `/api/v1/reviews/`                      | Create a review          |
| GET    | `/api/v1/reviews/`                      | List all reviews         |
| GET    | `/api/v1/reviews/<id>`                  | Get a review by id       |
| PUT    | `/api/v1/reviews/<id>`                  | Update a review          |
| DELETE | `/api/v1/reviews/<id>`                  | Delete a review          |
| GET    | `/api/v1/reviews/places/<place_id>/reviews` | List reviews for a place |
| POST   | `/api/v1/amenities/`                    | Create an amenity        |
| GET    | `/api/v1/amenities/`                    | List all amenities       |
| GET    | `/api/v1/amenities/<id>`                | Get an amenity by id     |
| PUT    | `/api/v1/amenities/<id>`                | Update an amenity        |

Invalid input returns a `400` status with `{"error": "<message>"}`.

## 7. Usage Examples

```python
from app.models.user import User
from app.models.place import Place

# Create a user
owner = User(first_name="Gheed", last_name="Majed",
             email="gheed.@gmail.com")

# Create a place linked to that user
place = Place(title="Tuwaiq Academy", description="A place to study",
              price=0, latitude=37.7749, longitude=-122.4194,
              owner=owner)

print(place.title, place.owner.first_name)
```

## 8. Running Tests

```bash
python3 -m unittest discover -s tests
```

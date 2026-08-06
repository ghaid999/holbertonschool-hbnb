# HBnB Evolution - Part 3

## 1. Project Title & Short Description

In this phase of the HBnB Evolution project, we extend the application by integrating a relational database using SQLAlchemy, implementing JWT-based authentication and role-based authorization, and securing the REST API endpoints. The in-memory persistence layer from the previous phase is replaced with a SQL database while preserving the layered architecture and Facade design pattern. Additionally, raw SQL scripts are created to generate the database schema, insert initial data, and verify CRUD operations independently of the ORM.

---

# 2. Project Structure

```text
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── places.py
│   │   │   ├── reviews.py
│   │   │   ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── BaseEntity.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   │   ├── place_amenity.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── repository.py
│   │   ├── amenity_repository.py
│   │   ├── place_repository.py
│   │   ├── review_repository.py
│   │   ├── user_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
├── sql_scripts/
│   ├── 1_schema.sql
│   ├── 2_initial_data.sql
│   ├── 3_rest_crud.sql
├── tests/
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_places.py
│   ├── test_reviews.py
│   ├── test_amenities.py
│   ├── testcurl.py
├── ER_Diagram.md
├── run.py
├── run_seed.py
├── hbnb.bd
├── config.py
├── requirements.txt
├── README.md
```

### Project Components

* **app/api/** — Presentation layer containing all REST API endpoints implemented with Flask-RESTx.
* **app/models/** — Business Logic layer implemented using SQLAlchemy models.
* **app/services/facade.py** — Implements the Facade pattern and connects the API with the persistence layer.
* **app/persistence/repository.py** — SQLAlchemy repository responsible for all CRUD operations.
* **app/api/v1/auth.py** — Authentication endpoints using JWT.
* **sql_scripts/** — Raw SQL scripts for schema generation, initial data insertion, and CRUD validation.
* **tests/** — API validation and testing scripts.
* **run.py** — Starts the Flask application.
* **config.py** — Application configuration.
* **requirements.txt** — Project dependencies.
* **README.md** — Project documentation.

---

# 3. Installation

Install all required packages.

```bash
pip install -r requirements.txt
```

---

# 4. Running the Application

Run the application.

```bash
python3 run.py
```

The application will start on:

```
http://127.0.0.1:5000/
```

Swagger documentation is available at:

```
http://127.0.0.1:5000/
```

---

# 5. Database Integration

Part 3 replaces the in-memory repository from Part 2 with a relational database using SQLAlchemy.

The database contains the following tables:

* Users
* Places
* Reviews
* Amenities
* Place_Amenity

Relationships implemented:

* One User owns many Places.
* One Place has many Reviews.
* One User can write many Reviews.
* Places and Amenities have a many-to-many relationship.

The SQLAlchemy repository handles all CRUD operations while preserving the Facade architecture designed in previous phases.

---

# 6. Business Logic Layer

## BaseEntity

All models inherit from **BaseEntity**.

It provides:

* UUID primary key
* created_at timestamp
* updated_at timestamp
* Common update functionality

---

## User

Represents a registered user.

Attributes:

* first_name
* last_name
* email
* password 
* is_admin

Validation:

* First and last names cannot be empty.
* Email must be unique.
* Passwords are hashed before storage.

---

## Place

Represents a property that can be listed.

Attributes:

* title
* description
* price
* latitude
* longitude
* owner

Validation:

* Title is required.
* Price must be positive.
* Latitude must be between -90 and 90.
* Longitude must be between -180 and 180.

---

## Review

Represents a review for a place.

Attributes:

* text
* rating
* user
* place

Validation:

* Rating must be between 1 and 5.
* A user can submit only one review per place.

---

## Amenity

Represents a facility available in a place.

Example:

* WiFi
* Swimming Pool
* Air Conditioning

---

## Relationships

* One User → Many Places
* One User → Many Reviews
* One Place → Many Reviews
* Many Places ↔ Many Amenities

---

# 7. Authentication and Authorization

Authentication is implemented using **JSON Web Tokens (JWT)**.

Passwords are securely stored using **Bcrypt** hashing.

Users authenticate through the login endpoint and receive an access token.

Protected endpoints require the following HTTP header:

```
Authorization: Bearer <JWT_TOKEN>
```

Role-based authorization is enforced as follows:

* Regular users can modify only their own resources.
* Administrators can perform privileged operations on any resource.

---

# 8. API Endpoints

## Authentication

| Method | Endpoint             | Description                      |
| ------ | -------------------- | -------------------------------- |
| POST   | `/api/v1/auth/login` | Authenticate user and obtain JWT |

---

## Users

| Method | Endpoint             | Description |
| ------ | -------------------- | ----------- |
| POST   | `/api/v1/users/`     | Create user |
| GET    | `/api/v1/users/`     | List users  |
| GET    | `/api/v1/users/<id>` | Get user    |
| PUT    | `/api/v1/users/<id>` | Update user |

---

## Places

| Method | Endpoint              | Description  |
| ------ | --------------------- | ------------ |
| POST   | `/api/v1/places/`     | Create place |
| GET    | `/api/v1/places/`     | List places  |
| GET    | `/api/v1/places/<id>` | Get place    |
| PUT    | `/api/v1/places/<id>` | Update place |

---

## Reviews

| Method | Endpoint                             | Description        |
| ------ | ------------------------------------ | ------------------ |
| POST   | `/api/v1/reviews/`                   | Create review      |
| GET    | `/api/v1/reviews/`                   | List reviews       |
| GET    | `/api/v1/reviews/<id>`               | Get review         |
| PUT    | `/api/v1/reviews/<id>`               | Update review      |
| DELETE | `/api/v1/reviews/<id>`               | Delete review      |
| GET    | `/api/v1/places/<place_id>/reviews/` | Reviews of a place |

---

## Amenities

| Method | Endpoint                 | Description    |
| ------ | ------------------------ | -------------- |
| POST   | `/api/v1/amenities/`     | Create amenity |
| GET    | `/api/v1/amenities/`     | List amenities |
| GET    | `/api/v1/amenities/<id>` | Get amenity    |
| PUT    | `/api/v1/amenities/<id>` | Update amenity |

---

# 9. Protected Endpoints

JWT authentication is required for protected operations.

Protected endpoints include:

* Create Place
* Update Place
* Update User
* Create Review
* Update Review
* Delete Review
* Create Amenity
* Update Amenity

Administrative privileges are required for operations restricted to administrators.

Unauthorized requests return:

```
401 Unauthorized
```

Forbidden operations return:

```
403 Forbidden
```

Invalid input returns:

```
400 Bad Request
```

Missing resources return:

```
404 Not Found
```

---

# 10. SQL Scripts

The project includes SQL scripts that recreate the database independently of SQLAlchemy.

## 1_schema.sql

Creates:

* Users
* Places
* Reviews
* Amenities
* Place_Amenity

Including:

* Primary Keys
* Foreign Keys
* Composite Keys
* Unique Constraints

---

## 2_initial_data.sql

Populates the database with:

Administrator user

```
Email:
admin@hbnb.io
```

Default amenities:

* WiFi
* Swimming Pool
* Air Conditioning

---

## 3_test_crud.sql

Validates SQL functionality through:

* CREATE
* READ
* UPDATE
* DELETE

It also verifies:

* Foreign key constraints
* Relationship integrity
* Unique review constraint
* Administrator insertion

---


# 11. Running Tests

## API Testing

The REST API was tested using Swagger.

The following scenarios were verified:

* User authentication
* JWT validation
* CRUD operations
* Input validation
* Authorization rules
* Role-based access control
* Error handling

---

## SQL Testing

The SQL scripts were tested independently using SQLite.

Verified operations include:

* Schema generation
* Table creation
* Initial data insertion
* CRUD operations
* Foreign key constraints
* Many-to-many relationships
* Unique constraints

---


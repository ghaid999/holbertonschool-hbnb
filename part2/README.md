## Project Structure
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├─ base.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── facade.py
│   └── persistence/
│       ├── __init__.py
│       └── repository.py
│   └── tests/
│   │   ├── __init__.py
│   │   ├── test_endpoints.py
│   │   └── test_curl.sh
├── run.py
├── config.py
├── requirements.txt
└── README.md

```
Overview

[Write a brief overview of the project and its main objectives.]

[Objective 1]
[Objective 2]
[Objective 3]
[Objective 4]

Team & Task Allocation (Part 2)

| Name | Tasks | Responsibilities / Deliverables |
|---|---|---|
| Geed | *Task 0, Task 2* | Project setup & package initialization (structure, Flask app scaffolding, in-memory repository, Facade placeholders). Implement *User endpoints* (POST/GET/PUT, list users), ensure *no password in responses*, correct status codes and Swagger docs. |
| Shatha | *Task 1, Task 3* | Implement core business logic classes (User, Place, Review, Amenity) with required attributes, validation, and relationships. Implement *Amenity endpoints* (POST/GET/PUT), integrate with Facade and repository, ensure consistent serialization & Swagger. |
| Dana | *Task 4, Task 5| Implement *Place endpoints* (POST/GET/PUT) with validation (price/lat/lon) and related data (owner + amenities). Implement *Review endpoints* (POST/GET/PUT/DELETE) + retrieve reviews for a place + update place to include reviews.

Repository & References
Repo: [GitHub Repository Link]
Work Path: [Project Path]
Reference Docs: [Reference Documents Location]
Task 0 Summary

[Write the Task 0 title, description, implementation details, and deliverables here.]

Task 1 Summary

[Write the Task 1 title, description, implementation details, and deliverables here.]

Task 2 Summary

[Write the Task 2 title, description, implemented endpoints, validation, and deliverables here.]

Task 3 Summary

[Write the Task 3 title, description, implemented endpoints, validation, and deliverables here.]

Task 4 Summary

[Write the Task 4 title, description, implemented endpoints, validation rules, and deliverables here.]

Task 5 Summary

[Write the Task 5 title, description, implemented endpoints, validation rules, and deliverables here.]

Task 6 Summary

[Write the Task 6 title, description, testing methods, test cases, and testing results here.]

## API Surface (v1)

- **Users:** `GET /api/v1/users/`, `POST /api/v1/users/`, `GET /api/v1/users/<id>`, `PUT /api/v1/users/<id>`
- **Amenities:** `GET /api/v1/amenities/`, `POST /api/v1/amenities/`, `GET /api/v1/amenities/<id>`, `PUT /api/v1/amenities/<id>`
- **Places:** `GET /api/v1/places/`, `POST /api/v1/places/`, `GET /api/v1/places/<id>`, `PUT /api/v1/places/<id>`, `GET /api/v1/places/<id>/reviews`
- **Reviews:** `GET /api/v1/reviews/`, `POST /api/v1/reviews/`, `GET /api/v1/reviews/<id>`, `PUT /api/v1/reviews/<id>`, `DELETE /api/v1/reviews/<id>`

Testing

[Write how to run the tests and mention the testing tools used.]

[Testing command]
Notes
[Project note]
[Project note]
[Project note]

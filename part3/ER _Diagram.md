# HBnB - Database ER Diagram (Task 10)

This diagram reflects the database schema defined in `part3/sql_scripts/`
(Task 9), keeping the two tasks consistent as required.


```mermaid
erDiagram
  USER ||--o{ PLACE : owns
  USER ||--o{ REVIEW : writes
  PLACE ||--o{ REVIEW : receives
  PLACE ||--o{ PLACE_AMENITY : has
  AMENITY ||--o{ PLACE_AMENITY : included_in

  USER {
    char36 id PK
    string first_name
    string last_name
    string email UK
    string password
    boolean is_admin
    timestamp created_at
    timestamp updated_at
  }
  PLACE {
    char36 id PK
    string title
    text description
    decimal price
    float latitude
    float longitude
    char36 owner_id FK
    timestamp created_at
    timestamp updated_at
  }
  REVIEW {
    char36 id PK
    text text
    int rating
    char36 user_id FK
    char36 place_id FK
    timestamp created_at
    timestamp updated_at
  }
  AMENITY {
    char36 id PK
    string name UK
    timestamp created_at
    timestamp updated_at
  }
  PLACE_AMENITY {
    char36 place_id PK_FK
    char36 amenity_id PK_FK
  }
```

## Relationships

| Relationship | Type | Notes |
|---|---|---|
| User → Place | One-to-many | `Place.owner_id` references `User.id`; a user can own many places |
| User → Review | One-to-many | `Review.user_id` references `User.id`; a user can write many reviews |
| Place → Review | One-to-many | `Review.place_id` references `Place.id`; a place can receive many reviews |
| Place ↔ Amenity | Many-to-many | Resolved through the `Place_Amenity` join table, whose composite primary key is `(place_id, amenity_id)` |

## Bonus - extending the model (optional exploration)

The task suggests exploring how a new `Reservation` entity might fit in.
A reservation links a `User` (who books) to a `Place` (what's booked), so it
would introduce two new one-to-many relationships without changing anything
already in the schema above:

```mermaid
erDiagram
  USER ||--o{ RESERVATION : books
  PLACE ||--o{ RESERVATION : is_booked_in

  RESERVATION {
    char36 id PK
    date start_date
    date end_date
    char36 user_id FK
    char36 place_id FK
    timestamp created_at
    timestamp updated_at
  }
```

This is exploratory only - it is not part of the Task 9 SQL schema and is not
implemented in the current database.

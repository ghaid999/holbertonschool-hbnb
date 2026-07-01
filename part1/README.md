# HBnB Evolution - Technical Documentation

## Table of Contents

1. Introduction
2. High-Level Architecture
3. Business Logic Layer
4. API Interaction Flow
5. Conclusion

---

# 1. Introduction

## Purpose

> Write a brief explanation of the purpose of this document.

## Project Overview

> Briefly describe the HBnB Evolution application and its objectives.

## Scope

> Explain what this document covers.

---

# 2. High-Level Architecture

## Overview

> Explain the layered architecture used in the project.

### Package Diagram

*(Insert the Package Diagram here.)*

### Presentation Layer

> Explain its responsibilities.

### Business Logic Layer

> Explain its responsibilities.

### Persistence Layer

> Explain its responsibilities.

### Facade Pattern

> Explain why the Facade pattern is used and how it connects the layers.

---

# 3. Business Logic Layer

## Overview

> The foolweng digram that explan the whol system inside the Business Logic Layer

### Class Diagram

*(Insert the Class Diagram here.)*

---

## BaseEntity

### Role

> The BaseEntity is the class that contain the atributs that is commen in all other class,so all the class inheret from BaseEntity. 

### Attributes

- id
- created_at
- updated_at

---

## User

### Role

> The user class is themain class , in this class the user can register, update , and delete .

### Attributes

- first_name
- last_name
- email
- password
- is_admin

### Methods

- register(first_name, last_name, email, password) : void
- update_profile(id, data) : void
- delete(id) : void

---

## Place

### Role

> in class place we have the information about the plece.

### Attributes

- title
- description
- price
- latitude
- longitude

### Methods

- create(title, description, price, latitude, longitude, owner_id) : void
- update(id, data) : void
- delete(id) : void
- list_all() : List<Place>
- add_amenity(amenity_id) : void
- remove_amenity(amenity_id) : void

---

## Review

### Role

> in class Review , a user can write a review , and a place have a reviews about the place.

### Attributes

- rating
- comment

### Methods

- create(place_id, user_id, rating, comment) : void
- update(id, data) : void
- delete(id) : void
- list_by_place(place_id) : List<Review>

---

## Amenity

### Role

> class Amenity , is the class that contain the Amenity about the place.

### Attributes

- name
- description

### Methods

- create(name, description) : void
- update(id, data) : void
- delete(id) : void
- list_all() : List<Amenity>

---

## Relationships

### BaseEntity → Entities

> The atruputs that share in all the Entities.

### User → Place

> A user can have multible places.

### User → Review

> A user can write multible Reviews about the places.

### Place → Review

> A place can have multible review that writen by the user.

### Place ↔ Amenity

> A place can have multible Amenity.

---

# 4. API Interaction Flow

## Overview

> Briefly explain what the sequence diagrams represent.

---

## User Registration

*(Insert Sequence Diagram)*

### Description

> Explain the flow.

---

## Place Creation

*(Insert Sequence Diagram)*

### Description

> Explain the flow.

---

## Review Submission

*(Insert Sequence Diagram)*

### Description

> Explain the flow.

---

## Fetch Places

*(Insert Sequence Diagram)*

### Description

> Explain the flow.

---


# 5. Conclusion

> Summarize the overall architecture and explain how this document will support the implementation of the HBnB application.


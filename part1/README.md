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

> Introduce the business entities and their purpose.

### Class Diagram

*(Insert the Class Diagram here.)*

---

## BaseEntity

### Role

> Explain the purpose of the class.

### Attributes

- id
- created_at
- updated_at

### Methods

> Describe the methods (if any).

---

## User

### Role

> Explain what a user represents.

### Attributes

- first_name
- last_name
- email
- password
- is_admin

### Methods

- register()
- update_profile()
- delete()

---

## Place

### Role

> Explain what a place represents.

### Attributes

- title
- description
- price
- latitude
- longitude

### Methods

- create()
- update()
- delete()
- list_all()
- add_amenity()
- remove_amenity()

---

## Review

### Role

> Explain what a review represents.

### Attributes

- rating
- comment

### Methods

- create()
- update()
- delete()
- list_by_place()

---

## Amenity

### Role

> Explain what an amenity represents.

### Attributes

- name
- description

### Methods

- create()
- update()
- delete()
- list_all()

---

## Relationships

### BaseEntity → Entities

> Explain the inheritance.

### User → Place

> Explain the ownership relationship.

### User → Review

> Explain the review relationship.

### Place → Review

> Explain the place-review relationship.

### Place ↔ Amenity

> Explain the many-to-many relationship.

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


# 6. Conclusion

> Summarize the overall architecture and explain how this document will support the implementation of the HBnB application.


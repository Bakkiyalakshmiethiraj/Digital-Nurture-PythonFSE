# Handson-5: Implementing CRUD Operations using Django REST Framework

## Objective

The objective of this hands-on is to implement CRUD (Create, Read, Update, Delete) operations for the Course Management System using Django REST Framework Generic Views.

---

## Technologies Used

- Python 3.13.7
- Django 6.0.6
- Django REST Framework
- SQLite
- Swagger UI

---

## CRUD Operations

### 1. Create a Course

**Method**

```
POST /api/courses/
```

**Sample Request**

```json
{
    "title": "Machine Learning",
    "code": "19AI501",
    "credits": 4,
    "department": 3
}
```

**Response**

```json
{
    "id": 6,
    "title": "Machine Learning",
    "code": "19AI501",
    "credits": 4,
    "department": 3
}
```

---

### 2. Retrieve All Courses

**Method**

```
GET /api/courses/
```

**Response**

```json
[
    {
        "id": 1,
        "title": "Python",
        "code": "19CS31",
        "credits": 3,
        "department": 2
    }
]
```

---

### 3. Update a Course

**Method**

```
PUT /api/courses/1/
```

**Sample Request**

```json
{
    "title": "Advanced Python",
    "code": "19CS31",
    "credits": 4,
    "department": 2
}
```

**Response**

```json
{
    "id": 1,
    "title": "Advanced Python",
    "code": "19CS31",
    "credits": 4,
    "department": 2
}
```

---

### 4. Delete a Course

**Method**

```
DELETE /api/courses/1/
```

**Response**

```
HTTP 204 No Content
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/courses/ | Retrieve all courses |
| POST | /api/courses/ | Create a course |
| GET | /api/courses/{id}/ | Retrieve a course |
| PUT | /api/courses/{id}/ | Update a course |
| DELETE | /api/courses/{id}/ | Delete a course |

---

## Learning Outcome

- Implemented CRUD APIs.
- Used GenericAPIView classes.
- Tested APIs using Swagger/Postman.
- Successfully performed Create, Read, Update and Delete operations.
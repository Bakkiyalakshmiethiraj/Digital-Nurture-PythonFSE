# Handson-10: Department Statistics API

## Objective

The objective of this hands-on is to create a Department Statistics API to retrieve department-wise information.

---

## Statistics API

```
GET /api/departments/<id>/statistics/
```

Example

```
GET /api/departments/1/statistics/
```

---

## Sample Response

```json
{
    "department": "Computer Science",
    "total_courses": 2,
    "total_students": 15,
    "total_enrollments": 20
}
```

---

## Features

- Department Name
- Total Courses
- Total Students
- Total Enrollments

---

## Technologies Used

- Django ORM
- REST Framework
- JSON Response

---

## Learning Outcome

- Created a custom Statistics API.
- Performed aggregate calculations.
- Retrieved department-wise analytics.
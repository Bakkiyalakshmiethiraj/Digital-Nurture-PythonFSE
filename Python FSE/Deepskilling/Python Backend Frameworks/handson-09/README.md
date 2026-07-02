# Handson-9: Dashboard API

## Objective

The objective of this hands-on is to create a Dashboard API that provides an overview of the Course Management System.

---

## Dashboard API

```
GET /api/dashboard/
```

---

## Sample Response

```json
{
    "departments": 5,
    "courses": 5,
    "students": 10,
    "enrollments": 15
}
```

---

## Features

- Total Departments
- Total Courses
- Total Students
- Total Enrollments

---

## Learning Outcome

- Created a custom API endpoint.
- Returned aggregated data.
- Used Django ORM count() function.
# 🚀 Enterprise Course Management System - Backend Hands-On

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0.6-green)
![Django REST Framework](https://img.shields.io/badge/DRF-3.17.1-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![License](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📖 Project Overview

The **Enterprise Course Management System** is a RESTful backend application developed using **Django** and **Django REST Framework (DRF)** as part of a structured backend development training program.

This project demonstrates the implementation of secure REST APIs, JWT authentication, CRUD operations, filtering, searching, pagination, API documentation, dashboard APIs, and Django Admin customization.

---

## 🎯 Objectives

- Learn Django project structure
- Develop RESTful APIs using Django REST Framework
- Implement JWT Authentication
- Perform CRUD operations
- Implement Search, Filter, Ordering and Pagination
- Generate API Documentation using Swagger & ReDoc
- Customize Django Admin Panel
- Build Dashboard APIs
- Follow professional backend development practices

---

# 🛠️ Technology Stack

| Technology | Version |
|------------|----------|
| Python | 3.13 |
| Django | 6.0.6 |
| Django REST Framework | 3.17.1 |
| SQLite | Default Database |
| JWT Authentication | Simple JWT |
| Swagger | drf-yasg |
| Postman | API Testing |

---

# 📂 Repository Structure

```
Enterprise-Course-Management-System/
│
├── Handson-1/
├── Handson-2/
├── Handson-3/
├── Handson-4/
├── Handson-5/
├── Handson-6/
├── Handson-7/
├── Handson-8/
├── Handson-9/
├── Handson-10/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📚 Hands-On Summary

| Hands-On | Topic |
|----------|------------------------------|
| Handson-1 | Django Project Setup |
| Handson-2 | Database Models |
| Handson-3 | Serializers |
| Handson-4 | CRUD REST APIs |
| Handson-5 | JWT Authentication |
| Handson-6 | Search, Filter, Ordering & Pagination |
| Handson-7 | Swagger & ReDoc Documentation |
| Handson-8 | Django Admin Customization |
| Handson-9 | Dashboard APIs & Statistics |
| Handson-10 | Validation, Testing & Final Enhancements |

---

# ✨ Features

- RESTful API Development
- JWT Authentication
- Department Management
- Course Management
- Student Management
- Enrollment Management
- Dashboard API
- Department Statistics API
- CRUD Operations
- Search
- Filter
- Ordering
- Pagination
- Swagger Documentation
- ReDoc Documentation
- Django Admin Panel
- Input Validation
- Professional API Responses

---

# 🔑 Authentication

The application uses **JSON Web Token (JWT)** authentication.

### Generate Token

```
POST /api/token/
```

### Refresh Token

```
POST /api/token/refresh/
```

Protected APIs require the following HTTP Header:

```
Authorization: Bearer <Access_Token>
```

---

# 📌 API Endpoints

## Department APIs

```
GET     /api/departments/
POST    /api/departments/
GET     /api/departments/{id}/
PUT     /api/departments/{id}/
DELETE  /api/departments/{id}/
```

---

## Course APIs

```
GET     /api/courses/
POST    /api/courses/
GET     /api/courses/{id}/
PUT     /api/courses/{id}/
DELETE  /api/courses/{id}/
```

Supports:

- Search
- Filter
- Ordering
- Pagination

---

## Student APIs

```
GET
POST
PUT
DELETE
```

---

## Enrollment APIs

```
GET
POST
PUT
DELETE
```

---

## Dashboard API

```
GET /api/dashboard/
```

Returns:

- Total Departments
- Total Courses
- Total Students
- Total Enrollments

---

## Department Statistics API

```
GET /api/departments/{id}/statistics/
```

Returns department-related statistics.

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/swagger/
```

ReDoc

```
http://127.0.0.1:8000/redoc/
```

---

# 🧪 Testing

The APIs were tested using:

- Django REST Framework Browsable API
- Swagger UI
- Postman

---

# 📷 Outputs

Each Hands-On folder contains:

- Source Code
- Output Screenshots
- README

---

# ▶️ How to Run the Project

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows

```bash
env\Scripts\activate
```

Linux / Mac

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---

# 📈 Learning Outcomes

Through this project, I gained practical experience in:

- Django Framework
- Django REST Framework
- REST API Design
- Authentication using JWT
- Database Modeling
- API Testing
- API Documentation
- Backend Best Practices
- Version Control using Git & GitHub

---

# 👩‍💻 Author

**Bakkiyalakshmi**

Engineering Student

Backend Developer Trainee

---

⭐ If you found this project useful, feel free to explore the repository.
# Handson-7: Filtering, Searching and Ordering in Django REST Framework

## Objective

The objective of this hands-on is to implement filtering, searching, and ordering functionalities for REST APIs using Django REST Framework.

---

## Technologies Used

- Python 3.13.7
- Django 6.0.6
- Django REST Framework
- django-filter
- SQLite

---

## Step 1: Install django-filter

**Command**

```bash
pip install django-filter
```

---

## Step 2: Configure Django

Add `django_filters` to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'django_filters',
]
```

---

## Step 3: Configure Filter Backend

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
```

```python
filter_backends = [
    DjangoFilterBackend,
    SearchFilter,
    OrderingFilter,
]

filterset_fields = ['department']
search_fields = ['title', 'code']
ordering_fields = ['credits', 'title']
```

---

## API Examples

### Filter Courses

```
GET /api/courses/?department=2
```

### Search Courses

```
GET /api/courses/?search=Python
```

### Order Courses

```
GET /api/courses/?ordering=credits
```

```
GET /api/courses/?ordering=-credits
```

---

## Learning Outcome

- Implemented Filtering.
- Implemented Searching.
- Implemented Ordering.
- Improved API usability.
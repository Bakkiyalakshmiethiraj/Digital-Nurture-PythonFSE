# Handson-4: Building REST APIs using Django REST Framework

## Objective

The objective of this hands-on is to develop REST APIs using Django REST Framework by creating serializers, API views, and URL routing for the Course Management System.

---

## Software Requirements

- Python 3.13.7
- Django 6.0.6
- Django REST Framework

---

## Step 1: Install Django REST Framework

**Command**

```bash
pip install djangorestframework
```

**Output**

```text
Successfully installed djangorestframework
```

---

## Step 2: Register REST Framework

Add the following in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## Step 3: Create Serializers

Created serializers for:

- Department
- Course
- Student
- Enrollment

Example:

```python
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
```

---

## Step 4: Create API Views

Implemented CRUD API views using Django REST Framework Generic Views.

Example:

```python
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
```

---

## Step 5: Configure URL Routing

Added API endpoints in `urls.py`.

Example:

```python
path("api/courses/", CourseListCreateAPIView.as_view()),
```

---

## Step 6: Test the API

Run the server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/api/courses/
```

Example Response:

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

## Learning Outcome

- Installed Django REST Framework.
- Created Model Serializers.
- Implemented Generic API Views.
- Configured API URL routing.
- Successfully tested REST APIs.
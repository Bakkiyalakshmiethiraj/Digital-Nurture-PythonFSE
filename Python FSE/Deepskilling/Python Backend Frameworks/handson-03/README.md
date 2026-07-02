# Handson-3: Creating Models and Database Migration

## Objective

The objective of this hands-on is to create database models using Django ORM and generate the corresponding database tables using migrations.

---

## Models Created

The following models were created:

- Department
- Course
- Student
- Enrollment

### Relationship

- One Department can have many Courses.
- One Department can have many Students.
- A Student can enroll in many Courses through the Enrollment model.

---

## Step 1: Create Models

The models were defined in `courses/models.py`.

Example:

```python
class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
```

---

## Step 2: Create Migration

**Command**

```bash
python manage.py makemigrations
```

**Output**

```text
Migrations for 'courses':
courses/migrations/0001_initial.py
```

---

## Step 3: Apply Migration

**Command**

```bash
python manage.py migrate
```

**Output**

```text
Applying courses.0001_initial... OK
```

---

## Database Tables Created

- Department
- Course
- Student
- Enrollment

---

## Learning Outcome

- Created Django models.
- Used Django ORM relationships.
- Generated migration files.
- Applied migrations successfully.
- Created database tables in SQLite.
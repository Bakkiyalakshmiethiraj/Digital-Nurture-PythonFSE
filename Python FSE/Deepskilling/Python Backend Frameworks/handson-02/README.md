# Handson-2: Creating a Django Application

## Objective

To create a Django application, register it in the project, and understand the basic project structure.

## Software Requirements

- Python 3.13.7
- Django 6.0.6
- Visual Studio Code

## Commands and Outputs

### 1. Create a Django App

**Command**

```bash
python manage.py startapp courses
```

**Output**

```text
Application 'courses' created successfully.
```

---

### 2. Register the App

Open **backend/settings.py** and add the app name to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'courses',
]
```

**Output**

```text
App registered successfully.
```

---

### 3. Django Project Structure

After creating the app, the project structure becomes:

```text
CourseManagementSystem/
│
├── backend/
├── courses/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── __init__.py
│
├── manage.py
└── env/
```

---

### 4. Run the Server

**Command**

```bash
python manage.py runserver
```

**Output**

```text
Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## Learning Outcome

- Created a Django application named **courses**.
- Registered the application in **settings.py**.
- Understood the Django project structure.
- Successfully executed the Django server.
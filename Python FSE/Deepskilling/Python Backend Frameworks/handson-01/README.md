# Handson-1: Django Installation and Project Setup

## Objective
To install Django, create a virtual environment, create a Django project, and run the development server.
## Software Requirements
- Python 3.13.7
- Django 6.0.6
- Visual Studio Code
## Commands and Outputs
### 1. Check Python Version
**Command**
```bash
python --version
```
**Output**
```text
Python 3.13.7
```
---
### 2. Create Virtual Environment
**Command**
```bash
python -m venv env
```
**Output**
```text
Virtual environment created successfully.
```
---
### 3. Activate Virtual Environment
**Command**
```bash
env\Scripts\activate
```
**Output**
```text
(env) C:\Users\Username\CourseManagementSystem>
```
---
### 4. Install Django
**Command**
```bash
pip install django
```
**Output**
```text
Successfully installed Django-6.0.6
```
---
### 5. Verify Django Version
**Command**
```bash
python -m django --version
```
**Output**
```text
6.0.6
```
---
### 6. Create Django Project
**Command**
```bash
django-admin startproject backend
```
**Output**
```text
Project created successfully.
```
---
### 7. Run Development Server
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
- Installed Django successfully.
- Created and activated a virtual environment.
- Created a Django project.
- Started the Django development server.
## SQL Program
models.py
```
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

engine = create_engine("sqlite:///college_db_orm.db", echo=True)


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)
    hod_name = Column(String(100))
    budget = Column(Numeric(12,2))

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(150))
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    prof_name = Column(String(100))
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(Numeric(10,2))

    department = relationship("Department", back_populates="professors")


Base.metadata.create_all(engine)

print("Tables Created Successfully")
```
crud.py
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from datetime import date

from models import Department, Student, Course, Enrollment

engine = create_engine("sqlite:///college_db_orm.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# INSERT Departments
# -------------------------------

d1 = Department(dept_name="Computer Science", hod_name="Dr Ramesh", budget=800000)

d2 = Department(dept_name="Electronics", hod_name="Dr Priya", budget=600000)

d3 = Department(dept_name="Mechanical", hod_name="Dr Suresh", budget=500000)

session.add_all([d1,d2,d3])
session.commit()

# -------------------------------
# INSERT Students
# -------------------------------

s1 = Student(first_name="Arjun",last_name="Mehta",
email="arjun@gmail.com",department=d1,enrollment_year=2022)

s2 = Student(first_name="Priya",last_name="Suresh",
email="priya@gmail.com",department=d1,enrollment_year=2022)

s3 = Student(first_name="Rohan",last_name="Verma",
email="rohan@gmail.com",department=d2,enrollment_year=2021)

s4 = Student(first_name="Sneha",last_name="Patel",
email="sneha@gmail.com",department=d3,enrollment_year=2023)

s5 = Student(first_name="Vikram",last_name="Das",
email="vikram@gmail.com",department=d1,enrollment_year=2022)

session.add_all([s1,s2,s3,s4,s5])
session.commit()

# -------------------------------
# INSERT Courses
# -------------------------------

c1 = Course(course_name="Data Structures",
course_code="CS101",
credits=4,
department=d1)

c2 = Course(course_name="DBMS",
course_code="CS102",
credits=3,
department=d1)

c3 = Course(course_name="Circuit Theory",
course_code="EC101",
credits=3,
department=d2)

session.add_all([c1,c2,c3])
session.commit()

# -------------------------------
# INSERT Enrollments
# -------------------------------

e1 = Enrollment(student=s1,course=c1,enrollment_date=date.today(),grade="A")

e2 = Enrollment(student=s2,course=c1,enrollment_date=date.today(),grade="B")

e3 = Enrollment(student=s3,course=c3,enrollment_date=date.today(),grade="A")

e4 = Enrollment(student=s5,course=c2,enrollment_date=date.today(),grade="A")

session.add_all([e1,e2,e3,e4])
session.commit()

print("\nStudents Inserted")

# -------------------------------
# READ
# -------------------------------

print("\nComputer Science Students")

students = session.query(Student).join(Department).filter(
Department.dept_name=="Computer Science").all()

for i in students:
    print(i.first_name,i.last_name)

# -------------------------------
# READ Enrollments
# -------------------------------

print("\nEnrollment Details")

records = session.query(Enrollment).all()

for r in records:
    print(r.student.first_name,"->",r.course.course_name)

# -------------------------------
# UPDATE
# -------------------------------

student = session.query(Student).filter_by(
email="vikram@gmail.com").first()

student.enrollment_year = 2024

session.commit()

print("\nUpdated Successfully")

# -------------------------------
# DELETE
# -------------------------------

enroll = session.query(Enrollment).first()

session.delete(enroll)

session.commit()

print("\nDeleted Successfully")

# -------------------------------
# joinedload (Fix N+1)
# -------------------------------

print("\nUsing joinedload")

records = session.query(Enrollment).options(
joinedload(Enrollment.student),
joinedload(Enrollment.course)
).all()

for r in records:
    print(r.student.first_name,"->",r.course.course_name)
```
## Output
<img width="752" height="851" alt="Screenshot 2026-07-03 110133" src="https://github.com/user-attachments/assets/e0196d98-45c4-4727-b48f-d6fc6920689a" />


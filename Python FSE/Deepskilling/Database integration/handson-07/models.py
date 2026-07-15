from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric, Boolean
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import declarative_base, relationship

# -------------------------------
# Database Connection
# -------------------------------

engine = create_engine(
    "mysql+mysqlconnector://root:bakki%40111@localhost/college_db_orm",
    echo=True
)

Base = declarative_base()

# -------------------------------
# Department Table
# -------------------------------

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False)
    hod_name = Column(String(100))
    budget = Column(Numeric(12,2))

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")


# -------------------------------
# Student Table
# -------------------------------

class Student(Base):
    __tablename__ = "students"
    

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)
    is_active = Column(Boolean, default=True)
    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# -------------------------------
# Course Table
# -------------------------------

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150), nullable=False)
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


# -------------------------------
# Enrollment Table
# -------------------------------

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


# -------------------------------
# Professor Table
# -------------------------------

class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(Numeric(10,2))

    department = relationship("Department", back_populates="professors")


# -------------------------------
# Create Tables
# -------------------------------

Base.metadata.create_all(engine)

print("\n===================================")
print(" All Tables Created Successfully ")
print("===================================")

print("\nTables Created:")
print("1. departments")
print("2. students")
print("3. courses")
print("4. enrollments")
print("5. professors")
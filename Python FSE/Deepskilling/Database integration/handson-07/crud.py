from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from datetime import date
from tabulate import tabulate

from models import Department, Student, Course, Enrollment, Professor

engine = create_engine(
    "mysql+mysqlconnector://root:bakki%40111@localhost/college_db_orm",
    echo=False
)

Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# INSERT DEPARTMENTS
# -------------------------------

if session.query(Department).count() == 0:

    cs = Department(
        dept_name="Computer Science",
        hod_name="Dr. Ramesh",
        budget=800000
    )

    ec = Department(
        dept_name="Electronics",
        hod_name="Dr. Priya",
        budget=600000
    )

    me = Department(
        dept_name="Mechanical",
        hod_name="Dr. Suresh",
        budget=500000
    )

    session.add_all([cs, ec, me])
    session.commit()

else:
    cs = session.query(Department).filter_by(dept_name="Computer Science").first()
    ec = session.query(Department).filter_by(dept_name="Electronics").first()
    me = session.query(Department).filter_by(dept_name="Mechanical").first()

# -------------------------------
# INSERT STUDENTS
# -------------------------------

if session.query(Student).count() == 0:

    students = [

        Student(
            first_name="Arjun",
            last_name="Mehta",
            email="arjun@gmail.com",
            department=cs,
            enrollment_year=2022
        ),

        Student(
            first_name="Priya",
            last_name="Suresh",
            email="priya@gmail.com",
            department=cs,
            enrollment_year=2022
        ),

        Student(
            first_name="Rohan",
            last_name="Verma",
            email="rohan@gmail.com",
            department=ec,
            enrollment_year=2021
        ),

        Student(
            first_name="Sneha",
            last_name="Patel",
            email="sneha@gmail.com",
            department=me,
            enrollment_year=2023
        ),

        Student(
            first_name="Vikram",
            last_name="Das",
            email="vikram@gmail.com",
            department=cs,
            enrollment_year=2022
        )

    ]

    session.add_all(students)
    session.commit()

# -------------------------------
# INSERT COURSES
# -------------------------------

if session.query(Course).count() == 0:

    c1 = Course(
        course_name="Data Structures",
        course_code="CS101",
        credits=4,
        department=cs
    )

    c2 = Course(
        course_name="DBMS",
        course_code="CS102",
        credits=3,
        department=cs
    )

    c3 = Course(
        course_name="Circuit Theory",
        course_code="EC101",
        credits=3,
        department=ec
    )

    session.add_all([c1, c2, c3])
    session.commit()

# -------------------------------
# INSERT PROFESSORS
# -------------------------------

if session.query(Professor).count() == 0:

    p1 = Professor(
        prof_name="Dr. Kumar",
        email="kumar@gmail.com",
        department=cs,
        salary=90000
    )

    p2 = Professor(
        prof_name="Dr. Priya",
        email="priyaprof@gmail.com",
        department=ec,
        salary=85000
    )

    session.add_all([p1, p2])
    session.commit()

# -------------------------------
# INSERT ENROLLMENTS
# -------------------------------

if session.query(Enrollment).count() == 0:

    s1 = session.query(Student).filter_by(email="arjun@gmail.com").first()
    s2 = session.query(Student).filter_by(email="priya@gmail.com").first()
    s3 = session.query(Student).filter_by(email="rohan@gmail.com").first()

    c1 = session.query(Course).filter_by(course_code="CS101").first()
    c2 = session.query(Course).filter_by(course_code="CS102").first()
    c3 = session.query(Course).filter_by(course_code="EC101").first()

    session.add_all([

        Enrollment(
            student=s1,
            course=c1,
            enrollment_date=date.today(),
            grade="A"
        ),

        Enrollment(
            student=s2,
            course=c2,
            enrollment_date=date.today(),
            grade="B"
        ),

        Enrollment(
            student=s3,
            course=c3,
            enrollment_date=date.today(),
            grade="A"
        )

    ])

    session.commit()

print("\nDATA INSERTED SUCCESSFULLY\n")

# -------------------------------
# READ
# -------------------------------

students = session.query(Student).join(Department).filter(
    Department.dept_name == "Computer Science"
).all()

table = []

for s in students:
    table.append([
        s.student_id,
        s.first_name,
        s.last_name,
        s.email,
        s.enrollment_year
    ])

print("COMPUTER SCIENCE STUDENTS")
print(tabulate(
    table,
    headers=["ID","First Name","Last Name","Email","Year"],
    tablefmt="grid"
))

# -------------------------------
# UPDATE
# -------------------------------

student = session.query(Student).filter_by(
    email="vikram@gmail.com"
).first()

if student:
    student.enrollment_year = 2024
    session.commit()

print("\nUPDATE SUCCESSFUL\n")

# -------------------------------
# DELETE
# -------------------------------

record = session.query(Enrollment).first()

if record:
    session.delete(record)
    session.commit()

print("DELETE SUCCESSFUL\n")

# -------------------------------
# JOINEDLOAD
# -------------------------------

records = session.query(Enrollment).options(
    joinedload(Enrollment.student),
    joinedload(Enrollment.course)
).all()

table = []

for r in records:

    table.append([
        r.enrollment_id,
        r.student.first_name,
        r.course.course_name,
        r.grade
    ])

print("ENROLLMENT DETAILS")
print(tabulate(
    table,
    headers=["Enroll ID","Student","Course","Grade"],
    tablefmt="grid"
))

print("\nHands-On 6 Completed Successfully.")
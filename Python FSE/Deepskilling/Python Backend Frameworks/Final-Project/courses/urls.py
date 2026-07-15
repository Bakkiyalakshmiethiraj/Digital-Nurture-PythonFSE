from django.urls import path
from .views import *

urlpatterns = [

    path("", home),

    # Department
    path("api/departments/", DepartmentListCreateAPIView.as_view()),
    path("api/departments/<int:pk>/", DepartmentDetailAPIView.as_view()),

    # Course
    path("api/courses/", CourseListCreateAPIView.as_view()),
    path("api/courses/<int:pk>/", CourseDetailAPIView.as_view()),

    # Student
    path("api/students/", StudentListCreateAPIView.as_view()),
    path("api/students/<int:pk>/", StudentDetailAPIView.as_view()),

    # Enrollment
    path("api/enrollments/", EnrollmentListCreateAPIView.as_view()),
    path("api/enrollments/<int:pk>/", EnrollmentDetailAPIView.as_view()),

    path("api/dashboard/", dashboard),
    
    path(
    "api/departments/<int:pk>/statistics/",
    department_statistics
),
]
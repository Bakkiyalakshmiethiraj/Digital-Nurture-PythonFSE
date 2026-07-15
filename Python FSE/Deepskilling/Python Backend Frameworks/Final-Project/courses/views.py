from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Department, Course, Student, Enrollment
from .serializers import (
    DepartmentSerializer,
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer,
)


def home(request):
    return JsonResponse({
        "message": "Welcome to Enterprise Course Management System API",
        "status": "Running Successfully"
    })

from django.http import JsonResponse
from .models import Department, Course, Student, Enrollment

def dashboard(request):
    data = {
        "total_departments": Department.objects.count(),
        "total_courses": Course.objects.count(),
        "total_students": Student.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
    }
    return JsonResponse(data)

from django.shortcuts import get_object_or_404

def department_statistics(request, pk):
    department = get_object_or_404(Department, pk=pk)

    data = {
        "department": department.name,
        "hod": department.hod,
        "budget": department.budget,
        "total_courses": Course.objects.filter(department=department).count(),
        "total_students": Student.objects.filter(department=department).count(),
    }

    return JsonResponse(data)

# -------------------- Department --------------------

class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


# -------------------- Course --------------------

from rest_framework import status
from rest_framework.response import Response

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ['department']
    search_fields = ['title', 'code']
    ordering_fields = ['credits', 'title']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Course created successfully.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# -------------------- Student --------------------

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


# -------------------- Enrollment --------------------

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]


class EnrollmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

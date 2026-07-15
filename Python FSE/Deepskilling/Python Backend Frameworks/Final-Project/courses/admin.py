from django.contrib import admin
from .models import Department, Course, Student, Enrollment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hod", "budget")
    search_fields = ("name", "hod")
    ordering = ("id",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "code", "credits", "department")
    search_fields = ("title", "code")
    list_filter = ("department",)
    ordering = ("id",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "department")
    search_fields = ("name", "email")
    list_filter = ("department",)
    ordering = ("id",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "grade")
    search_fields = ("student__name", "course__title")
    list_filter = ("grade",)
    ordering = ("id",)
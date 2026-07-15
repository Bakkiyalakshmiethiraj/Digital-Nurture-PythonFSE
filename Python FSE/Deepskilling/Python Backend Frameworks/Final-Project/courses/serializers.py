from rest_framework import serializers
from .models import Department, Course, Student, Enrollment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

    def validate_budget(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Budget must be greater than zero."
            )
        return value


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def validate_credits(self, value):
        if value < 1 or value > 6:
            raise serializers.ValidationError(
                "Credits must be between 1 and 6."
            )
        return value

    def validate_code(self, value):
        queryset = Course.objects.filter(code=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Course code already exists."
            )

        return value


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_email(self, value):
        queryset = Student.objects.filter(email=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
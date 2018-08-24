from students.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer converts to JSON and validates data parsed
    """

    class Meta:
        model   = Student
        fields = [
            'first_name',
            'last_name',
            'gender'
        ]
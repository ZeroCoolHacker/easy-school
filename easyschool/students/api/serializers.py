from students.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer converts to JSON and validates data parsed
    """

    class Meta:
        model   = Student
        # fields = [
        #     'first_name',
        #     'last_name',
        #     'gender'
        # ]
        fields = '__all__'
        read_only_fields = ['gender']

    #as we have a clean_<field_name> method to clean form data
    # we have validate_<field_name> method to validate the serializer data
    
    def validate_first_name(self, value):
        qs = Student.objects.filter(first_name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The first name has already been used")
        else:
            return value
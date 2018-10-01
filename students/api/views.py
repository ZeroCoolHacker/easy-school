from django.shortcuts import render
from rest_framework import generics
from students.api.serializers import StudentSerializer
from students.models import Student

# Create your views here.
class StudentListView(generics.ListAPIView):
    """
    Api end point that allows the students to be created
    """
    
    lookup_field      = 'pk'
    serializer_class        = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()







class StudentCreateView(generics.CreateAPIView):
    """
    Api end point that allows the students to be created
    """
    
    lookup_field      = 'pk'
    serializer_class        = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


    def perform_create(self, serializer):
        serializer.save(gender='M')






class StudentRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Api end point that allows the students to be viewed or edited or deleted
    """
    
    lookup_field      = 'pk'
    serializer_class        = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()




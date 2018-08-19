from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'father_name',
         'date_of_birth', 'fathers_phone_no'
        )

    search_fields = (
        'first_name', 'last_name', 'admission_no'
        )
    
    ordering = ('first_name',)
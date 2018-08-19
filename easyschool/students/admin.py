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

    fieldsets = (
        ("School Record", {
            'fields' : ('admission_no',)
        }),
        ("Personal Information", {
            'fields' : ('first_name', 'last_name', 'date_of_birth', 'address')
        }),
        ("Guardian Information", {
            'fields' : ('father_name', 'father_cnic', 'fathers_phone_no', 'fathers_proffesion')
        })
    )
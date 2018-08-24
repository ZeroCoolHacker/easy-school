from django.contrib import admin
from .models import Student, StudentFee
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """ Display Class of Student Model in Admin Panel"""


    def upper_case_name(self):
        return ("%s %s" % (self.first_name, self.last_name)).capitalize()
    upper_case_name.short_description = 'Name'

    empty_value_display = '--Empty--'


    list_display = (
        upper_case_name,
         'father_name',
         'date_of_birth',
         'fathers_phone_no',
         'is_studying', 'gender'
        )


    list_filter = (
        'is_studying',
        'current_class',
        'gender'
    )


    search_fields = (
        'first_name', 'last_name', 'admission_no'
        )


    ordering = ('first_name',)


    fieldsets = (
        ("School Record", {
            'fields' : ('admission_no', 'date_of_admission', 'is_studying', 'current_class')
        }),
        ("Personal Information", {
            'fields' : ('first_name', 'last_name', 'date_of_birth', 'gender', 'address')
        }),
        ("Guardian Information", {
            'fields' : ('father_name', 'father_cnic', 'fathers_phone_no', 'fathers_proffesion')
        })
    )


    def get_readonly_fields(self, request, obj=None):
        """ Make admission_no and date_of_admission uneditable if
        opened the admin change form but editable if opened
        the create form
        """
        
        if obj:# if the object exists then make them readonly
            return ['admission_no', 'date_of_admission']
        else:
            return []
    


@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    """ Admin display class for the model StudentFee """
    pass


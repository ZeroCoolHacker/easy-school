from django.contrib import admin
from .models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin Display Options to display the Course data in admin panel"""


    list_display = (
        'course_name',
        'course_description'
    )


    search_fields = (
        'course_name',
    )
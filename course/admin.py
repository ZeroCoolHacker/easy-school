from django.contrib import admin

from .models import Course
from easyschool.utils import ExportCsvMixin


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin, ExportCsvMixin):
    """Admin Display Options to display the Course data in admin panel"""

    list_display = (
        'course_name',
        'course_description'
    )

    search_fields = (
        'course_name',
    )

    actions = [
        'export_as_csv',
    ]

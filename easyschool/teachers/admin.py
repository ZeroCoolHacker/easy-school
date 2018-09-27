from django.contrib import admin
from .models import Teacher
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for Teacher'''

    list_display = (
        'full_name',
        'gender',
        'is_teaching',
        )

    list_filter = (
        'gender',
        'is_teaching',
        )

    list_select_related = True
    raw_id_fields = ('user',)

    search_fields = (
        'user__first_name',
        'user__last_name',
        )

    ordering = ('-date_of_joining',)
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Teacher, TeacherSalary
from easyschool.utils import ExportCsvMixin


# Change User Creation Form
class UserCreationFormExtended(UserCreationForm):
    """
    Overiding UserCreationForm to include fields
    which are not included by default
    """

    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)


UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin, ExportCsvMixin):
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

    actions = [
        'export_as_csv',
    ]


@admin.register(TeacherSalary)
class TeacherSalaryAdmin(admin.ModelAdmin, ExportCsvMixin):
    """ Admin display class for the model StudentFee """

    # Delete Delete Action from admin
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    raw_id_fields = ('teacher',)
    # Filtering
    list_filter = ('valid_until', 'total_amount')

    # searching
    search_fields = [
        'techer__full_name',
    ]

    list_display = (
        'teacher',
        'valid_until',
        'total_amount',
        'paid_on',
    )

    actions = [
        'export_as_csv',
    ]

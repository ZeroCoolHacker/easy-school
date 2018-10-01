from django.contrib import admin
from .models import Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _

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
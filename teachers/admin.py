import json

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from django.db.models.functions import Trunc

from .models import Teacher, TeacherSalary, FinanceSummary
from easyschool.utils import ExportCsvMixin
from students.models import StudentFee

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

@admin.register(FinanceSummary)
class FinanceSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        monthly_salaries = TeacherSalary.objects.annotate(
            month=Trunc('paid_on', 'month')).values('month').annotate(total=Sum('total_amount'))
        monthly_fees = StudentFee.objects.annotate(
            month=Trunc('date_submitted', 'month')).values('month').annotate(total=Sum('total_amount'))

        data = {}
        for salary in monthly_salaries:
            month_year = "{}-{}".format(salary['month'].month, salary['month'].year)
            data[month_year] = {
                "salaries": salary['total'],
                "fees": 0,
                "profit": salary['total']
            }

        for fee in monthly_fees:
            month_year = "{}-{}".format(fee['month'].month, fee['month'].year)
            if month_year in data:
                data[month_year]['fees'] = fee['total']
                data[month_year]['profit'] = data[month_year]['salaries'] - fee['total']
            else:
                data[month_year]['salaries'] = 0
                data[month_year]['fees'] = fee['total']
                data[month_year]['profit'] = 0 - fee['total']

        # Prepare data to graph format
        labels, salaries, fees = ([] for i in range(3))
        for key, value in data.items():
            labels.append(key)
            salaries.append(value['salaries'])
            fees.append(value['fees'])


        # Scructure of graph_data is defined by Graph.js
        graph_data = {
            'labels': labels,
            'datasets': [{
                'label': "Teacher",
                'backgroundColor': "#F5DD5D",
                'data': salaries
            }, {
                'label': "Student",
                'backgroundColor': "#44B78B",
                'data': fees
            }]
        }

        response.context_data['data'] = data
        response.context_data['graph_data'] = json.dumps(graph_data)
        return response

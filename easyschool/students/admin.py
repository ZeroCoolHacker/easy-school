from django.contrib import admin
from .models import Student, StudentFee
from django.utils.html import format_html
from django.utils.html import mark_safe
import calendar
from datetime import date
from .forms import StudentFeeAdd
# Register your models here.



admin.site.site_header  = "My School Admin"
admin.site.site_title   = "My School Admin Portal"
admin.site.index_title  = "Welcome to My School Portal"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """ Display Class of Student Model in Admin Panel"""

    #remove delete actions
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    #Custom Actions
    def expel_from_school(self, request, queryset):
        rows_updated = queryset.update(is_studying=False)
        if rows_updated == 1:
            message_bit = "1 student was"
        else:
            message_bit = "%s students were" % rows_updated
        self.message_user(request, "%s successfully marked as expelled" % message_bit)
    expel_from_school.short_description = 'Expel From School'
    expel_from_school.allowed_permissions = ('change',)


    def last_fee_submitted(self):
        paid_color  = 'green'
        unpaid_color = 'red'

        if self.is_studying:
            obj = self.studentfee_set.last()
            if obj is not None:# if a record exists
                if int(obj.month) >= date.today().month and obj.year >= date.today().year: # if paid this month
                    return format_html(
                        '<span style="color: {};">{}</span>',
                        paid_color,
                        calendar.month_name[int(obj.month)]+','+str(obj.year)
                    )
                else: # if not paid this month 
                    return format_html(
                    '<span style="color: {};">{}</span>',
                    unpaid_color,
                    calendar.month_name[int(obj.month)]+','+str(obj.year)
                )
            else: # if record does not exists
                return format_html(
                    '<span style="color: {};">{}</span>',
                    unpaid_color,
                    "No Fee Paid"
                )
        else:
            return "Left School"
    last_fee_submitted.short_description = 'Last Fee Submitted'

    def profile_image_display(self, obj):
        return mark_safe(
            '<a href={url} target="_blank"><img src="{url}" width="{width}" \
            height={height} style={style} /></a>'.format(
            url = obj.profile_image.url,
            width=200,
            height=200,
            style='',
            )
        )
    profile_image_display.short_description = "Student Image"

    empty_value_display = '--Empty--'


    list_display = (
         'full_name',
         'father_name',
         'is_studying',
         'gender',
         last_fee_submitted,
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
            'fields' : (
                'admission_no', 
                'date_of_admission',
                'is_studying',
                'current_class',
                'profile_image',
                'profile_image_display',#callable function,
                )
        }),
        ("Personal Information", {
            'fields' : ('first_name', 'last_name', 'date_of_birth', 'gender', 'address')
        }),
        ("Guardian Information", {
            'fields' : ('father_name', 'father_cnic', 'fathers_phone_no', 'fathers_proffesion')
        })
    )

    actions = ['expel_from_school',]


    def get_readonly_fields(self, request, obj=None):
        """ Make admission_no and date_of_admission uneditable if
        opened the admin change form but editable if opened
        the create form
        """
        
        if obj:# if the object exists then make them readonly
            return ['admission_no', 'date_of_admission', 'profile_image_display']
        else:
            return ['profile_image_display',]
    


@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    """ Admin display class for the model StudentFee """
    
    # Delete Delete Action from admin
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        """  The form to give django admin"""
        if obj is None:
            return StudentFeeAdd
        else:
            super(StudentFeeAdmin, self).get_form(request, obj, **kwargs)

    # Filtering
    list_filter = (
        'month',
    )
    
    #searching
    search_fields = [
        'student__admission_no',
        'student__first_name',
        'student__last_name',
    ]

    list_display = (
        'month',
        'amount',
        'date_submitted',
    )

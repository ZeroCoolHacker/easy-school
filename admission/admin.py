from django.contrib import admin
from admission.models import *
# Register your models here.

admin.site.register(PersonalInformation)
admin.site.register(EducationalBackground)
admin.site.register(EmergencyContact)
admin.site.register(Guardian)
admin.site.register(AdmissionForm)


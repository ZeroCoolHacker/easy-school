from django import forms

from admission.models import *



class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = '__all__'
    
class EducationalBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = '__all__'


class ParentGuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ("name","relationship","phone_number","email",)


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class AdmissionFormForm(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        fields = ("course","additional_information","signature_applicant",'signature_parent_guardian',)

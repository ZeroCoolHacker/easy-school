from django import forms

from admission.models import *



class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = StudentPersonalInformation
        fields = '__all__'
    
class EducationalBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = ("current_school_name","current_school_address","current_school_city",'current_school_state_province',"current_school_postal_code",'current_school_country',"grade_level","dates_attended",)


class ParentGuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ("name","relationship","phone_number","email",)


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ("name", "relationship", "phone_number",)


class AdmissionFormForm(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        fields = ("course","additional_information","signature_applicant",'signature_parent_guardian',)

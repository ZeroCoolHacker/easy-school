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
        model = ParentGuardian
        fields = '__all__'


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class AdmissionFormForm(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        fields = '__all__'

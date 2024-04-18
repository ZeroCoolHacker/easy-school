from django.contrib.auth.forms import UserCreationForm
from teachers.models import Teacher
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from easyschool.utils import GENDER_CHOICES
from django.core.exceptions import ValidationError
from datetime import datetime
class TeacherSignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        strip= False,
    )

    password2 = forms.CharField(
        label = 'Password confirmation',
        strip = False
    )
    username = forms.CharField(max_length=11, help_text="Enter your username, this will be used to login",
                               label="Username",
                               required=True)

    next_year=datetime.now().year +1
    date_of_joining = forms.DateField(widget=forms.SelectDateWidget(years=range(1960,next_year)))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1960,next_year )))
    gender = forms.ChoiceField(choices= GENDER_CHOICES)
    cnic = forms.CharField(max_length=20)
    phone_no = forms.CharField(max_length=12)
    is_teaching = forms.BooleanField(label= 'Presently teaching in this school',required=False)
    address = forms.CharField(max_length=150, required=True)
    profile_image = forms.ImageField(required=False, label='Profile Picture')
     

    def clean_email(self):
        email = self.cleaned_data['email']
        if email is None:
            raise forms.ValidationError('Please enter  email address')
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for  field in self.Meta.required:
            self.fields[field].required = True


    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name','password1','password2' ,'email']
        required = (
            'last_name',
            'email',
        )




from django.db import models
from course.models import Course
# Create your models here.

from easyschool.utils import GENDER_CHOICES
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.admission_no, filename)

class PersonalInformation(models.Model):
    admission_no = models.IntegerField(auto_created=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=150, default="Not Set")
    city = models.CharField(max_length=100, default="Not Set")
    state = models.CharField(max_length=100)
    post_code = models.BigIntegerField()
    phone_number = models.IntegerField(max_length=11)
    email = models.EmailField()
    date_of_admissionapplication  = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True)
    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).capitalize()
    



    

class EducationalBackground(models.Model):
    current_school_name = models.CharField(max_length=100)
    current_school_address = models.CharField(max_length=200)
    current_school_city = models.CharField(max_length=100)
    current_school_state_province = models.CharField(max_length=100)
    current_school_postal_code = models.CharField(max_length=20)
    current_school_country = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=50)
    dates_attended = models.CharField(max_length=100)

    def __str__(self):
        return self.current_school_name
    


class ParentGuardian(models.Model):
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AdmissionForm(models.Model):
    course =models.ForeignKey(Course, on_delete=models.CASCADE)
    personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    educational_background = models.OneToOneField(EducationalBackground, on_delete=models.CASCADE)
    guardian1 = models.OneToOneField(ParentGuardian, on_delete=models.CASCADE, related_name='guardian1')
    guardian2 = models.OneToOneField(ParentGuardian, on_delete=models.CASCADE, related_name='guardian2')
    emergency_contact = models.OneToOneField(EmergencyContact, on_delete=models.CASCADE)
    additional_information = models.TextField()

    signature_applicant = models.CharField(max_length=100)
    date_signed = models.DateField()
    signature_parent_guardian = models.CharField(max_length=100)
    date_parent_guardian_signed = models.DateField()

    def __str__(self):
        return self.personal_information.full_name
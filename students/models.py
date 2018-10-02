import calendar
from datetime import date, datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from course.models import Course
from easyschool.utils import GENDER_CHOICES, MONTHS_CHOICE


# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.admission_no, filename)


class Student(models.Model):
    admission_no = models.IntegerField(unique=True)
    date_of_admission = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    # TODO: Create a parent/guardian model and reference that, mothers could be important too you know...
    father_name = models.CharField(max_length=50)
    father_cnic = models.CharField(max_length=13)
    fathers_phone_no = models.CharField(max_length=11, default="0000000")
    fathers_proffesion = models.CharField(max_length=50, default="Not Set")
    address = models.CharField(max_length=150, default="Not Set")
    is_studying = models.BooleanField(default=True)
    current_class = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).capitalize()

    full_name.admin_order_field = 'first_name'

    @property
    def detail(self):
        return '{} Class - {}'.format(self.current_class, self.full_name)

    def __str__(self):
        return self.full_name()


# Fee Models

class FeeType(models.Model):
    name        = models.CharField('Name', max_length=, blank=False)
    display_name= models.CharField('Displayed Name', max_length=50, blank=False)
    amount      = models.PositiveIntegerField()


class StudentFee(models.Model):
    """ Datatabase Model for student fees"""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    amount = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    @property
    def month_name(self):
        return calendar.month_name[date.month]

    def __str__(self):
        return 'Fee : ' + self.student.first_name + ' ' + self.student.last_name + ' : ' + str(self.date)

    def __repr__(self):
        return self.__str__()


# class FeeSummary(StudentFee):
#     """
#     https://medium.com/@hakibenita/how-to-turn-django-admin-into-a-lightweight-dashboard-a0e0bbf609ad
#     """

#     class Meta:
#         proxy = True
#         verbose_name = 'Fee Summary'
#         verbose_name_plural = 'Fee Summary'

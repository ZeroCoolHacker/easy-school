import calendar
from datetime import date, datetime, timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from course.models import Course
from easyschool.utils import GENDER_CHOICES, MONTHS_CHOICE, next_month


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

    address = models.CharField(max_length=150, default="Not Set")
    is_studying = models.BooleanField(default=True)
    current_class = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).capitalize()

    full_name.admin_order_field = 'first_name'

    @property
    def detail(self):
        return '{} Class - {}'.format(self.current_class, self.full_name)


class StudentFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    valid_until = models.DateField(verbose_name='Valid Until', default=next_month())
    total_amount = models.PositiveIntegerField(default=0)
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Student Fee'

    def __str__(self):
        return f'Fee : {self.student.full_name()} {str(self.date_submitted)}'

    @property
    def month_name(self):
        return calendar.month_name[valid_until.month]


class Guardian(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    relation_to_student = models.ForeignKey(Student, on_delete=models.PROTECT)
    social_security_number = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, default="0000000")
    profession = models.CharField(max_length=50, default="Not Set")

    def __str__(self):
        return f'{self.name}'

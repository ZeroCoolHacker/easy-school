from django.contrib.auth.models import User
from django.db import models

from easyschool.utils import GENDER_CHOICES, next_month


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'teacher_{0}/{1}'.format(instance.cnic, filename)


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    social_security_number = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=11, default="0000000")
    address = models.CharField(max_length=150, default="Not Set")
    is_teaching = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        """Returns full name of teacher"""
        return self.user.get_full_name()


class TeacherSalary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    valid_until = models.DateField(verbose_name='Valid Until', default=next_month())
    total_amount = models.PositiveIntegerField(default=0)
    paid_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Teacher Salaries'

    def __str__(self):
        return f'Fee : {self.student.full_name()} {str(self.date_submitted)}'

    @property
    def month_name(self):
        return calendar.month_name[valid_until.month]
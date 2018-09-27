from django.db import models
from django.contrib.auth.models import User
from easyschool.utils import GENDER_CHOICES, MONTHS_CHOICE

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'teacher_{0}/{1}'.format(instance.cnic, filename)

# Create your models here.
class Teacher(models.Model):
    """
    Teacher profile model
    Linked to django default user model
    so teacher can log in
    """

    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    gender          = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth   = models.DateField()
    cnic            = models.CharField(max_length=13)
    phone_no        = models.CharField(max_length=11, default="0000000")
    address         = models.CharField(max_length=150, default="Not Set")
    is_teaching    = models.BooleanField(default=True)
    profile_image   = models.ImageField(upload_to=user_directory_path, blank=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return '{} {}'.format(self.user.first_name, self.user.last_name)
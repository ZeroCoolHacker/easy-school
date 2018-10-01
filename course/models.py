from django.db import models


# Create your models here.
class Course(models.Model):
    """ Database Model for Course/Classes held in school"""

    course_name = models.CharField(blank=False, max_length=50)
    course_description = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return self.course_name

    def __repr__(self):
        return 'Course : ' + self.course_name

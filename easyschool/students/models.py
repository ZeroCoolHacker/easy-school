from django.db import models
from course.models import Course
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Student(models.Model):
    admission_no    = models.IntegerField(unique=True)
    date_of_admission= models.DateField()
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    gender          = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth   = models.DateField()
    father_name     = models.CharField(max_length=50)
    father_cnic     = models.CharField(max_length=13)
    fathers_phone_no= models.CharField(max_length=11, default="0000000")
    fathers_proffesion= models.CharField(max_length=50, default="Not Set")
    address         = models.CharField(max_length=150, default="Not Set")
    is_studying     = models.BooleanField(default=True)
    current_class   = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+' '+self.last_name
    



class StudentFee(models.Model):
    """ Datatabase Model for student fees"""

    student     =   models.ForeignKey(Student, on_delete=models.CASCADE)
    month       =   models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year        =   models.IntegerField(validators=[MinValueValidator(date.today().year-1),
                                        MaxValueValidator(date.today().year)],
                                        default=date.today().year)
    amount      =   models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return 'Fee : '+ self.student.first_name+' '+self.student.last_name+' : '+str(self.month)
    
    def __repr__(self):
        return self.__str__()
    

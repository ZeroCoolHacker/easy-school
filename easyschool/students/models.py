from django.db import models
from course.models import Course
# Create your models here.
class Student(models.Model):
    admission_no    = models.IntegerField(unique=True)
    date_of_admission= models.DateField()
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    gender          = models.CharField(max_length=1)
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
    
    def __repr__(self):
        return 'Student(Adm:'+self.admission_no+', name:'+self.__str__()


class StudentFee(models.Model):
    """ Datatabase Model for student fees"""

    student     =   models.ForeignKey(Student, on_delete=models.CASCADE)
    month       =   models.CharField(blank=False, max_length=10)
    amount      =   models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return 'Fee : '+ self.student.first_name+' '+self.student.last_name+' : '+self.month
    
    def __repr__(self):
        return self.__str__()
    

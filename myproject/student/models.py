from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=25,verbose_name="İsim")
    surname=models.CharField(max_length=25,verbose_name="Soyisim")
    schoolId=models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    classId=models.CharField(max_length=20)

from django.db import models

# Create your models here.
class SchoolManager(models.Model):
    name=models.CharField(max_length=25,verbose_name="İsim")
    surname=models.CharField(max_length=25,verbose_name="Soyisim")
    schoolId=models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    def __str__(self):
        return self.name
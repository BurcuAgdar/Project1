from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=50 , verbose_name="Okul Adı")
    adress=models.CharField(max_length=25 , verbose_name="Adres")
    def __str__(self):
        return self.name
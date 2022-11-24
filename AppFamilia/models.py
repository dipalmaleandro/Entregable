from django.db import models

# Create your models here.
class Integrantes1(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=30)
    documento=models.IntegerField()
    ocupacion=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre+" " + self.apellido+" "+ self.documento+" "+self.ocupacion
class Integrantes2(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=30)
    documento=models.IntegerField()
    ocupacion=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre+" " + self.apellido+" "+ self.documento+" "+self.ocupacion
class Integrantes3(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=30)
    documento=models.IntegerField()
    ocupacion=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre+" " + self.apellido+" "+ self.documento+" "+self.ocupacion

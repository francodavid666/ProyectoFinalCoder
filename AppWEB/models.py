from django.db import models

# Create your models here.

class Auto (models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    año = models.IntegerField()
    
    
    
class Juegos (models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    desarrolladora = models.CharField(max_length=50)
    año_salida = models.CharField(max_length=50)
    

class Gatss (models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    color = models.IntegerField()
   
class Persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
   
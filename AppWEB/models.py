from django.db import models

# Create your models here.

class Auto (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    region = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    
    def __str__(self)-> str:
        return self.marca +" "+self.modelo
        
    
    
    
    
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
    
    def __str__ (self) -> str:
        return self.apellido+" "+self.nombre
   
class Persona_2 (models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     edad = models.IntegerField()
     profesion =  models.CharField(max_length=50)
     comision =  models.IntegerField()
       

from django.db import models

# Create your models here.

    
class USUARIO (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    

       
# se van a agregar modelos para los apartados que esta en el body de la pagina
    
    
    
       
from collections import UserList
from datetime import datetime
from distutils.command.upload import upload
from email import generator
from email.policy import default
from multiprocessing import current_process
from unittest.util import _MAX_LENGTH


from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#para el avatar

from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null =True, blank = True)
    owner = models.IntegerField('Dueño datos',blank = True, default= 1)
    pais = models.CharField(max_length=200,null =True, blank = True)
    localidad = models.CharField(max_length=200,null =True, blank = True)
    codigo_postal = models.IntegerField(null =True, blank = True)
    
    descripcion = models.CharField(max_length=200,null =True, blank = True)
    link = models.CharField(max_length=200,null =True, blank = True)
    fecha_nac = models.DateTimeField(null =True, blank = True)
   
   

   
    def __str__(self):
     return f'usuario: {self.id}'

class PostModel (models.Model):
    
    autor = models.ForeignKey(User,on_delete=models.CASCADE, null =True, blank = True)
    owner = models.IntegerField('Dueño Post',blank = True, default= 1)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    contenido = RichTextField(blank=True , null=True)
    orden= models.CharField(max_length=50)
    imagen = RichTextUploadingField(blank=True , null=True)
    
    
    
    def __str__(self):
        return f'titulo{self.titulo}'


class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank =True, default=models.URLField('DAVID_AESTETIC.png'))
        
   

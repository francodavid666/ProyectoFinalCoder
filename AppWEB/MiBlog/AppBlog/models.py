from datetime import datetime
from email import generator
from email.policy import default
from multiprocessing import current_process


from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#para el avatar

from django.contrib.auth.models import User

# Create your models here.

    
class USUARIO (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    '''
    nacionalidad= models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fecha_nacimiento = datetime ()
    edad = models.IntegerField()
    email  = models.CharField(max_length=50)'''

        
'''class USUARIO_ACADEMICO (models.Model):
    tiene_estudio= models.CharField(max_length=255, default = "")
    que_estudia = models.CharField(max_length=50)
    coding = 
   ''' 
    
class PostModel (models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = RichTextField(blank=True , null=True)
    contenido = models.TextField(max_length=500)
    orden= models.CharField(max_length=50)
    imagen = RichTextUploadingField(blank=True , null=True)
    
    def __str__(self):
        return f'titulo{self.titulo}'


class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank =True)
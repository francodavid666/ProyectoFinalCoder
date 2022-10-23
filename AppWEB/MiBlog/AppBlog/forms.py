
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CKEDITOR
from django.forms import ModelForm

class formulario_modelo (ModelForm):
    class  Meta:
        model = PostModel
        fields = ('titulo','descripcion','orden','contenido','imagen')
    

class Usuario_formulario (ModelForm):
    class  Meta:
        model = Usuario
        fields = ('pais','localidad','codigo_postal','descripcion','link', 'fecha_nac')
  
    
'''class Usuario_formulario (forms.Form):
    pais = forms.CharField(label = 'Pais')
    localidad = forms.CharField(label = 'Localidad')
    codigo_postal = forms.CharField(label = 'Codigo Postal')
  '''
 

class formulario_registro(UserCreationForm):
    username = forms.CharField(label = "Nombre de usuario")
    first_name= forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    email = forms.EmailField(label = "E-Mail")
    password1= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput)
    
    
    
    
       
    class Meta: #es una clase adentro de mi register forms para modificar detalles
         model = User
         fields = ['username', 'first_name','last_name','email','password1', 'password2']
         #help_texts = {k:"fran" for k in fields}
        
 
 
class UserEditForm (UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput)
    first_name=forms.CharField(label = 'Modificar Nombre')
    last_name=forms.CharField(label = 'Modificar Apellido')
   
    
   
    class Meta: 
        model = User
        fields = ['username', 'first_name','last_name','email','password1', 'password2']
        help_texts = {k:"fran" for k in fields}
        
        
class Avatar_formulario(forms.Form):
    
    imagen = forms.ImageField(label="Imagen")
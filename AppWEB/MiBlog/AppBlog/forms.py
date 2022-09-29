
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CKEDITOR
from django.forms import ModelForm

class formulario_modelo (ModelForm):
    class  Meta:
        model = PostModel
        fields = '__all__'
    


class Usuario_formulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    apodo = forms.CharField(max_length=50)
    codigo_postal = forms.CharField(max_length=50)
    
 
class Usuario_formulario_2 (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    apodo = forms.CharField(max_length=50)
    codigo_postal = forms.CharField(max_length=50)
    
       
    

    


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = "Nombre de usuario")
    email = forms.EmailField(label = "E-Mail")
    password1= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput)
        
    '''def clean_password2(self):
    
        password1 = self.cleaned_data.get ['password1']
        password2 = self.cleaned_data.get ['password2']
        
         '''
       
       
    class Meta: #es una clase adentro de mi register forms para modificar detalles
         model = User
         fields = ['username', 'email','password1', 'password2']
         help_texts = {k:"fran" for k in fields}
        
 
 
class UserEditForm (UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput)
    
    first_name=forms.CharField(label = 'Modificar Nombre')
    last_name=forms.CharField(label = 'Modificar Apellido')
    
    class Meta: 
        model = User
        fields = ['email','password1', 'password2', 'first_name','last_name']
        help_texts = {k:"fran" for k in fields}
        
        
class Avatar_formulario(forms.Form):
    imagen = forms.ImageField(label="Imagen")
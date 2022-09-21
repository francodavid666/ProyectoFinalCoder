from pyexpat import model
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Usuario_formulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    contraseña= forms.IntegerField()



class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(label = "Modificar E-Mail")
    password1= forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput)
    
    
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
        
from socket import fromshare
from django import forms


class Formulario (forms.Form):
    
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    
from django import forms
from .models import Auto


class Formulario (forms.Form):
    
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
 
class Formulario_2 (forms.Form):
    
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    profesion =  forms.CharField(max_length=50)
    comision =  forms.IntegerField()
       
       
class Formulario_de_autos (forms.Form):
    '''
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    anio = forms.IntegerField()
    region =  forms.CharField(max_length=50)
    color =  forms.CharField(max_length=50)
     '''  
    class Meta:
        model = Auto
        fields ='__all__' 
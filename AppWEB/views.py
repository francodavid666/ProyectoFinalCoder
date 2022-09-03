from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto, Gatss, Juegos,Persona
from AppWEB.forms import Formulario
# Create your views here.


def inicio (request):
    return render (request,"AppWEB/padre.html")

def autos (request):
    return render (request,"AppWEB/autos.html")

def juegos (request):
    return render (request,"AppWEB/juegos.html")

def juegos (request):
    return render (request,"AppWEB/gatos.html")

def formulario (request):
    return render (request, "AppWEB/formulario.html")



def fformulario (request):
    
 if request.method == "POST":
    miFormulario = Formulario (request.POST)
    print(miFormulario)
    
    if miFormulario.is_valid():
          informacion = miFormulario.cleaned_data
          print(informacion)
          nombre = informacion.get("nombre")
          apellido = informacion.get("apellido")
          edad = informacion.get("años")
          
          persona_1 = Persona( nombre=nombre, apellido=apellido , edad=edad)
          persona_1.save()
          return render (request, "AppWEB/padre.html")
    else:
        return render (request, "AppWEB/padre.html")
    
 else:
      miFormulario = Formulario()
 return render (request, "AppWEB/formulario.html", {"fformulario": Formulario})
              
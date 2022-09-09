
from django.urls import reverse
from typing import ValuesView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto, Gatss, Juegos,Persona, Persona_2
from AppWEB.forms import Formulario, Formulario_2, Formulario_de_autos
from django.views.generic import UpdateView,ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def inicio (request):
    return render (request,"AppWEB/inicio.html")

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
          edad = informacion.get("edad")
          
          persona_1 = Persona( nombre=nombre, apellido=apellido , edad=edad)
          persona_1.save()
          return render (request, "AppWEB/padre.html")
    else:
        return render (request, "AppWEB/padre.html")
    
 else:
      miFormulario = Formulario()
 return render (request, "AppWEB/formulario.html", {"fformulario": Formulario})
               

#FORMULARIO AUTOS

def autos_formulario(request):
    
    if request.method == "POST":
        formulario_auto = Formulario_de_autos(request.POST)
        print(formulario_auto)
        
        if formulario_auto.is_valid():
            informacion = formulario_auto.cleaned_data
            print(informacion)
            marca = informacion.get("marca")
            modelo = informacion.get("modelo")
            anio = informacion.get("anio")
            region = informacion.get("region")
            color = informacion.get("color")
            
            auto_1 = Auto( marca=marca , modelo=modelo , anio=anio , region=region , color=color )
            auto_1.save()
            return render(request,"AppWEB/padre.html") 
        else:
            return render (request,"AppWEB/padre.html")
    else:
        formulario_auto = Formulario_de_autos()
    return render (request, "AppWEB/formulario_auto.html", {"formularioauto": Formulario_de_autos})   
            
            
        

           
              
def busquedaPersona (request):
    return render (request, "AppWEB/busquedaPersona.html")

def buscar (request):
 if request.GET.get("edadd"): 
    edad1 = request.GET.get ("edadd")
    apellidos = Persona.objects.filter(edad = edad1)
    if len(apellidos)!=0:
     return render (request , "AppWEB/resultadoBusqueda.html", {"apellido": apellidos})
    else:
        return render (request, "AppWEB/resultadoBusqueda.html", {"mensaje": "no hay apellidos"})
 else:
     return render (request, "AppWEB/busquedaPersona.html", {"mensaje": "no enviaste datos"})
    


class List_auto(ListView):
    model = Auto
    template_name= 'AppWEB/autos.html'
    queryset = Auto.objects.all()

class Detail_auto(DetailView):
    model = Auto
    template_name= 'DetailAuto.html'

class Create_auto(LoginRequiredMixin, CreateView):
    model = Auto
    template_name = 'AppWEB/CreateAuto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('AppWEB/DetailAuto', kwargs={'pk':self.object.pk})

class Delete_auto(DeleteView):
    model = Auto
    template_name = 'AppWEB/DeleteAuto.html'

    def get_success_url(self):
        return reverse('list_products')

class Update_auto(UpdateView):
    model = Auto
    template_name = 'AppWEB/UpdateAuto.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('AppWEB/DetailAuto', kwargs = {'pk':self.object.pk})

def Search_auto(request):
    auto = Auto.objects.all()
    if auto.exists():
        context = {'auto':auto}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'AppWEB/search-auto.html', context = context)
    
        
    

    
        
    






'''
def LeerAutos(request):
    automoviles = Auto.objects.all()
    print(automoviles)
    return render (request, "AppWEB/LeerAutos.html",{"autos":automoviles})



def Eliminar_auto (request, id):
    auto=Auto.objects.filter(id=id)
    auto.delete()
    autos=Auto.objects.all()
    return render (request, "AppWEB/LeerAutos.html",{"autos": autos})
'''




'''
def Editar_auto (request, id):
    #trae el profesor 
    auto = Auto.objects.get(id=id)
    if request.method == "POST":
        #el form viene lleno, con los datos a cambiar
        form =  Formulario_de_autos(request.POST)
        if form.is_valid():
            #cambio los datos
            info=form.cleaned_data
            auto.marca=info["marca"]
            auto.modelo=info["modelo"]
            auto.anio=info["anio"]
            auto.region=info["region"]
            auto.color=info["color"]
            #guardo el auto
            auto.save()
            #vuelvo a la vista del listado para el cambio
            autos= Auto.objects.all()
            return render (request, "AppWEB/LeerAutos.html", {"autos":autos})
    else:
        form = Formulario_de_autos(initial={"marca":auto.marca,"modelo":auto.modelo,"anio": auto.anio, "region":auto.region,"color":auto.color})
        return render (request,"AppWEB/editar_auto.html",{"formulario":form, "modelo_auto": auto.modelo,"marca_auto": auto.marca, "id":auto.id})    

            


def busquedaAuto(request):
    return render (request, "AppWEB/BusquedAauto.html")

def buscarAUTO(request):
    if request.GET.get("anio"):
        anio1 = request.GET.get("anio")
'''
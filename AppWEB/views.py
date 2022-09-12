
from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto
from AppWEB.forms import Formulario_de_autos

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


#FORMULARIO AUTOS

def CreateAuto(request):
    
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
            return render(request,"AppWEB/AUTOS/auto_creado.html") 
        else:
            return render (request,"AppWEB/inicio.html")
    else:
        formulario_auto = Formulario_de_autos()
    return render (request, "AppWEB/CreateAuto.html", {"formularioauto": Formulario_de_autos})   
            
            
        
def ViewAutos(request):
    automoviles = Auto.objects.all()
    print(automoviles)
    return render (request, "AppWEB/autos.html",{"autos":automoviles})
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
def buscar (request):
 if request.GET.get("edadd"): 
    edad1 = request.GET.get ("edadd")
    apellidos = Persona.objects.filter(edad = edad1)
    if len(apellidos)!=0:
     return render (request , "AppWEB/resultadoBusqueda.html", {"apellido": apellidos})
    else:
        return render (request, "AppWEB/resultadoBusqueda.html", {"mensaje": "no hay apellidos"})
 else:
     return render (request, "AppWEB/AUTOS/BuscarAuto.html", {"mensaje": "no enviaste datos"})
    






def Eliminar_auto (request, id):
    auto=Auto.objects.filter(id=id)
    auto.delete()
    autos=Auto.objects.all()
    return render (request, "AppWEB/LeerAutos.html",{"autos": autos})
'''




'''
def Editar_auto (request, id):
    #trae el auto
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
            return render (request, "AppWEB/ViewAuto.html", {"autos":autos})
    else:
        form = Formulario_de_autos(initial={"marca":auto.marca,"modelo":auto.modelo,"anio": auto.anio, "region":auto.region,"color":auto.color})
        return render (request,"AppWEB/editar_auto.html",{"formulario":form, "modelo_auto": auto.modelo,"marca_auto": auto.marca, "id":auto.id})    

            


def busquedaAuto(request):
    return render (request, "AppWEB/BusquedAauto.html")

def BUSCAR_AUTO(request):
    if request.GET.get("anio"):
        anio1 = request.GET.get("anio")


from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppBlog.forms import *
from .forms import * 

#imports de clases
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy



# imports para login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# Create your views here.

def inicio (request):
    return render(request, "AppBlog\inicio.html")

def resultado_busqueda (request):
 return render(request, "AppBlog\resultado_busqueda.html")
 
def formulario_creado(request):
    return render (request, "AppBlog/formulario_creado.html")

def creado (request):
    return render (request,"AppBlog/creado.html")


from django.views.generic import ListView




def formulario_usuario(request):
    if request.method == "POST":
        form = Usuario_formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            apodo = info.get("apodo")
            codigo_postal = info.get("codigo_postal")
            
            usuario_1= USUARIO(nombre=nombre,apellido=apellido,apodo=apodo,codigo_postal=codigo_postal)
            usuario_1.save()
            return render(request,"AppBlog/formulario_creado.html",{"mensaje": "Se creo el formulario"})
        else:
            return render(request,"AppBlog/error_formulario",{"mensaje":f"error en crear formulario"})
    else:
        formulario = Usuario_formulario()
    return render (request,"AppBlog/formulario.html",{"formulario": formulario})

def lista_usuarios(request):
    usuarios = USUARIO.objects.all()
    return render (request,"AppBlog/ListaUsuarios.html",{"usuarios": usuarios})


def buscar ( request ):
     return render (request,"AppBlog/buscar.html")  
 
def resultado_busqueda (request):
     nom = request.GET.get("nombre")
     usuarios = USUARIO.objects.filter(nombre=nom)
     return render (request,"AppBlog/resultado_busqueda.html", {'usuarios': usuarios}) 


def editar_perfil (request):
    usuario = request.user
    if request.method =="POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
        
            usuario.first_name = form.cleaned_data["first_name"]
            usuario.last_name = form.cleaned_data["last_name"]
            usuario.email = form.cleaned_data["email"]
            
            usuario.save()
            return render (request, "AppBlog/Bienvenido.html", {'mensaje': f"perfil de {usuario} editado"})
        
    else:
        form = UserEditForm(instance=usuario)
    return render(request,"AppBlog/editar_perfil.html", {"form": form, 'usuario':usuario})
     
            
 




def Login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu= request.POST["username"]
            clave =request.POST["password"]
            
            usuario=authenticate(username=usu, password=clave)
             
            if usuario is not  None:
                 login(request, usuario) 
                 return render (request, "AppBlog/bievenido.html",{'mensaje': f"Bienvenido {usuario}"})
            else:
                return render (request, 'AppCoder/login.html', {'mensaje': 'Usuarios o contraseña incorrectos'}) 
        else: 
            
            return render (request, "AppBlog/formulario_invalido.html",{'mensaje':'FORMULARIO INVALIDO'})
    else:
        form = AuthenticationForm()
    return render (request, "AppBlog/login.html", {'form': form})
                    

def registro_request (request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            # podriamos fijarnos que no exitsta un user en la bd con ese nombre
            
            form.save()
            return render (request, 'AppBlog/creado.html',{'mensaje':f"Usuario {username} creado"})
        else:
            return render (request, 'appBlog/algomal.html', {'mensaje':f'algo anda mal'})
            
    else:
        form = UserRegisterForm()
        return render (request, 'AppBlog/registro.html',{'form':form})
        
        
 


     
    
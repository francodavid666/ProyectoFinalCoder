
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppBlog.forms import *
from .forms import * 
from django.urls import reverse_lazy



# imports para login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# Create your views here.

def inicio (request):
    return render(request, "AppBlog\padre.html")

def ingresar (request):
    return render (request, "AppBlog/ingresar.html")

def usuario_creado(request):
    return render (request, "AppBlog/usuario_creado.html")

def creado (request):
    return render (request,"AppBlog/creado.html")





def crear_usuario(request):
    
    if request.method == 'POST':
        formulario = Usuario_formulario(request.POST)
        
        if formulario.is_valid():
            cleaned_info = formulario.cleaned_data
        
            nombre = cleaned_info.get("nombre")
            apellido = cleaned_info.get("apellido")
            email = cleaned_info.get("email")
            contraseña = cleaned_info.get("contraseña")
        
            usuario_1 = Usuario(nombre=nombre, apellido=apellido, email=email, contraseña=contraseña)
            usuario_1.save()
            return render(request, "AppBlog/usuario_creado.html")
        else: 
            return render (request, "AppBlog/inicio.html")
    else:
        formulario = Usuario_formulario()    
    return render (request,"AppBlog/ingresar.html",{"formulario": Usuario_formulario})
    
    

def Login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu= request.POST["username"]
            clave =request.POST["password"]
            
            usuario=authenticate(username=usu, password=clave)
             
            if usuario is not  None:
                 login(request, usuario) 
                 return render (request, "AppBlog/padre.html",{'mensaje': f"Bienvenido {usuario}"})
            else:
                return render (request, 'AppCoder/login.html', {'mensaje': 'Usuarios o contraseña incorrectos'})
            
        else:
            return render (request, "AppBlog/login.html",{'mensaje':'FORMULARIO INVALIDO'})
    
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
        form = UserRegisterForm()
        return render (request, 'AppBlog/registro.html',{'form':form})
        
        
 
@login_required
def editar_perfil (request):
    usuario = request.user
    if request.method =="POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
        
            usuario.first_name = form.cleaned_data["first_name"]
            usuario.last_name = form.cleaned_data["last_name"]
            usuario.email = form.cleaned_data["email"]
            
            usuario.save()
            return render (request, "AppBlog/padre.html", {'mensaje': f"perfil de {usuario} editado"})
        
    else:
        form = UserEditForm(instance=usuario)
    return render(request,"AppBlog/editar_perfil.html", {"form": form, 'usuario':usuario})
            
 
        
        
        
        
        
        
    
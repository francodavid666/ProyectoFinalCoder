
from nturl2path import url2pathname
from winreg import REG_QWORD
from django.shortcuts import render, redirect
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

#Para buscar con imagen
from django.db.models import Q


# Create your views here.

#CKEDITOR
#-----------------------------------
def index (request):
    articulo = PostModel.objects.all()
    return render (request, 'AppBlog/posteos/articulos.html', {'articulos': articulo})



def detalle (request):
    articulo = PostModel.objects.get(pk=1)
    
    if request.method == 'POST':
        form = formulario_modelo(request.POST, instance = articulo)
        
        if form.is_valid():
            form.save()
            
            return redirect('detalle')
    else:
     form = formulario_modelo(instance=articulo)
    return render (request, 'AppBlog/posteos/detalle.html', {'articulos': articulo, 'form':form})


def crear_post(request):
    if request.method =='POST':
        form = formulario_modelo(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info["titulo"]
            descripcion = info["descripcion"]
            contenido = info["contenido"]
            orden = info["orden"]
            imagen = info["imagen"]
            
            post_1 = PostModel(titulo=titulo,descripcion=descripcion,contenido=contenido,orden=orden,imagen=imagen)
            post_1.save()
            
            return render (request, 'AppBlog/posteos/posteo_creado.html')
        else:
            return render (request, 'AppBlog/posteos/posteo_rechazado.html') 
    else:
        form= formulario_modelo()
    return render (request, 'AppBlog/posteos/crear_posteo.html',{'form':form,'imagen': obtener_avatar(request)})   
    
    
    

def lista_post(request):
    posteos = PostModel.objects.all()
    return render (request,'AppBlog/posteos/lista_post.html',{'posteos':posteos ,'imagen': obtener_avatar(request)})

def eliminar_post_individual(request,id):
    lista =PostModel.objects.filter(id=id)
    if len(lista)!=0:
        posteos=lista[0]
        posteos.delete()
        
    return render (request,"AppBlog/posteos/post_eliminado.html",{'mensaje':"¡Se elimino el posteo correctamente!"})



def eliminar_post(request):
    post = PostModel.objects.all()
    post.delete()
    return render (request,"AppBlog/posteos/eliminar_post.html",{'post':post})


def buscar_posteo ( request ):
     return render (request,"AppBlog/posteos/buscar_posteo.html")  
 
def resultado_busqueda_posteo (request):
     titu = request.GET.get("titulo")
     posteos = PostModel.objects.filter(titulo=titu)
     return render (request,"AppBlog/posteos/resultado_busqueda_posteo.html", {'posteos': posteos}) 

'''def resultado_busqueda_posteo (request):
     titu = request.GET.get("titulo")
     posteos = PostModel.objects.filter(titulo=titu)
     return render (request,"AppBlog/posteos/resultado_busqueda_posteo.html", {'posteos': posteos}) 
'''
 
def ver_posteo (request,titulox):
   # posteo =  PostModel.objects.get(slug = slug ) print (posteo)
    posteo = PostModel.objects.filter(titulo=titulox)
    return render (request,"AppBlog/posteos/ver_posteo.html", {'posteo': posteo, 'imagen':obtener_avatar(request)})


def posteo_editado(request):
    return render (request,'AppBlog/posteos/posteo_editado.html')

def editar_posteo(request, id):
    post = PostModel.objects.get(id = id)
    if request.method == 'POST':
        
        form =formulario_modelo(request.POST)
        if form.is_valid():
            
           
            
            post.titulo = form.cleaned_data["titulo"]
            post.descripcion = form.cleaned_data["descripcion"]
            post.contenido = form.cleaned_data["contenido"]
            post.orden = form.cleaned_data["orden"]
            post.imagen = form.cleaned_data["imagen"]
            
            
            post.save()
            posteos = PostModel.objects.all()
            return render (request,"AppBlog/posteos/posteo_editado.html",{'posteos':posteos})
    else:
        form = formulario_modelo (initial={'titulo':post.titulo,'descripcion':post.descripcion, 'contenido':post.contenido,'orden':post.orden,'imagen':post.imagen})
    return render (request,'AppBlog/posteos/editar_posteo.html',{"form": form, "id": post.id})




#-----------------------------------
def obtener_avatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
            imagen=lista[0].imagen.url
    else:
        imagen="HOLA"
    return imagen   




def articulo (request):
    queryset = request.GET.get()
    articulo = PostModel.objects.all()
    return render (request, 'AppBlog/posteos/articulo.html', {'articulo': articulo})

def inicio (request):
    return render(request, "AppBlog\inicio.html",{'imagen':obtener_avatar(request)})

def resultado_busqueda (request):
 return render(request, "AppBlog/resultado_busqueda.html")

def creado (request):
    return render (request,"AppBlog/creado.html")


from django.views.generic import ListView

#FORMULARIO DE DATOS
 
def formulario_creado(request):
    return render (request, "AppBlog/formulario_creado.html")


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



def editar_formulario(request,id):
    usuario = USUARIO.objects.get (id = id)
    if request.method =="POST":
        
        form = Usuario_formulario(request.POST)
        if form.is_valid():
            
            info = form.cleaned_data
            usuario.nombre = info ["nombre"]    
            usuario.apellido = info ["apellido"]    
            usuario.apodo = info ["apodo"] 
            usuario.codigo_postal = info ["codigo_postal"] 
            
            usuario.save()
            
            usuarios = USUARIO.objects.all()
            return render (request,"AppBlog/ListaUsuarios.html",{"usuarios": usuarios})   
    else:
        form =Usuario_formulario(initial = {"nombre":usuario.nombre, "apellido":usuario.apellido, "apodo": usuario.apodo,"codigo_postal":usuario.codigo_postal})
        return render (request,"AppBlog/editar_formulario.html",{"form": form, "nombre_usuario":usuario.nombre, "id": usuario.id})
     
def eliminar_formulario(request):
    post = USUARIO.objects.all()
    post.delete()
    return render (request,"AppBlog/eliminar_formulario.html",{'post':post})
    

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
            return render (request, "AppBlog/perfil_editado.html", {'mensaje': f"perfil de {usuario} editado"})
        
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
        return render (request, 'AppBlog/registro.html',{'form':form,})
        
        
 
  
    
    

def agregar_avatar(request):
    if request.method =='POST':
        formulario = Avatar_formulario (request.POST, request.FILES)
        if formulario.is_valid():
            avatar_viejo = Avatar.objects.get(user=request.user)
            if (avatar_viejo.imagen):
                avatar_viejo.delete()
                avatar_1 =Avatar(user=request.user, imagen =formulario.cleaned_data['imagen'])
                avatar_1.save()
            return render (request,'AppBlog/inicio.html',{'usuario': request.user,'mensaje': 'AVATAR AGREGADO EXITOSAMENTE'})       
    else:
        formulario = Avatar_formulario()
        return render (request, 'AppBlog/agregar_avatar.html',{'form':formulario,'usuario':request.user,'imagen': obtener_avatar(request)})     
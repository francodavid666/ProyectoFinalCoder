
from dataclasses import fields
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from AppBlog.forms import *
from .forms import * 

#imports de clases
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy

#para buscar
from django.db.models import Q

# imports para login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#mensajes de errores
from django.contrib import messages

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
 if request.user.is_authenticated:
    if request.method =='POST':
        form = formulario_modelo(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            
            
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
    busqueda =  request.GET.get("buscar")
    posteos = PostModel.objects.all()
    
    if busqueda: 
        posteos = PostModel.objects.filter(
            Q(titulo__icontains = busqueda)
        ).distinct()
    return render (request,'AppBlog/posteos/buscar_posteo.html',{'posteos': posteos})
 
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
        form = formulario_modelo (initial={'autor': post.autor,'titulo':post.titulo,'descripcion':post.descripcion, 'contenido':post.contenido,'orden':post.orden,'imagen':post.imagen})
    return render (request,'AppBlog/posteos/editar_posteo.html',{"form": form, "id": post.id})







def articulo (request):
    queryset = request.GET.get()
    articulo = PostModel.objects.all()
    return render (request, 'AppBlog/posteos/articulo.html', {'articulo': articulo})

@login_required(login_url='login')
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
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            
            return render(request,"AppBlog/inicio.html",{"mensaje": "Se creo el formulario"})
        else:
            return render(request,"AppBlog/inicio.html",{"mensaje":f"error en crear formulario"})
    else:
        formulario = Usuario_formulario()
    return render (request,"AppBlog/formulario.html",{"formulario": formulario})



def editar_formulario(request,id):
    usuario = Usuario.objects.get (id = id)
    if request.method =="POST":
        
        form = Usuario_formulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
              
            usuario.pais = info ["pais"] 
            usuario.localidad = info ["localidad"]    
            usuario.codigo_postal = info ["codigo_postal"] 
            
            usuario.save()
            
            usuarios = Usuario.objects.all()
            return render (request,"AppBlog/ListaUsuarios.html",{"usuarios": usuarios})   
    else:
       
        form =Usuario_formulario(initial = {"pais":usuario.pais, "localidad":usuario.localidad,"codigo_postal":usuario.codigo_postal})
        return render (request,"AppBlog/editar_formulario.html",{"form": form,"id": usuario.id})
     
def eliminar_formulario(request):
    post = Usuario.objects.all()
    post.delete()
    return render (request,"AppBlog/eliminar_formulario.html",{'post':post})
    




def buscar ( request ):
     return render (request,"AppBlog/buscar.html")  
 
def resultado_busqueda (request):
     nom = request.GET.get("nombre")
     usuarios = Usuario.objects.filter(nombre=nom)
     return render (request,"AppBlog/resultado_busqueda.html", {'usuarios': usuarios}) 


def editar_perfil (request):
    usuario = request.user
    if request.method =="POST":
        form =UserEditForm(request.POST)
        if form.is_valid():
        
            usuario.username = form.cleaned_data["username"]
            usuario.first_name = form.cleaned_data["first_name"]
            usuario.last_name = form.cleaned_data["last_name"]
            usuario.email = form.cleaned_data["email"]
            
            usuario.save()
            return render (request, "AppBlog/perfil_editado.html", {'mensaje': f"perfil de {usuario} editado"})
        
    else:
        form = UserEditForm(instance=usuario)
        formulario = Usuario_formulario()
    return render(request,"AppBlog/editar_perfil.html", {'formulario':formulario,"form": form, 'usuario':usuario,'imagen':obtener_avatar(request)})
     

'''class lista_usuarios(ListView):
    
    model = Usuario
    template_name = "AppBlog/ListaUsuarios.html"   
    
'''
def lista_usuarios(request):
    usuarios = User.objects.all()
    datos = Usuario.objects.all()
    return render (request,"AppBlog/ListaUsuarios.html",{"usuarios": usuarios,'datos':datos,'imagen':obtener_avatar(request)})         



def edit_datos_personales (request):
   # usuario = request.user
    if request.method =="POST":
        formulario = Usuario_formulario(request.POST)
        if formulario.is_valid():
        
            formulario.save()
            return render (request, "AppBlog/login.html", {'mensaje': f"tus dats  fueron editados"})
        
    else:
        formulario = Usuario_formulario()
    return render(request,"AppBlog/edit_datos_personales.html", {"formulario": formulario,'imagen':obtener_avatar(request)})
     
   


#LOGIN


def Login_request(request):
    if request.user.is_authenticated:
     return redirect("inicio")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                usu= request.POST["username"]
                clave =request.POST["password"]
                
                usuario=authenticate(username=usu, password=clave)
                
                if usuario is not  None:
                    login(request, usuario) 
                    return render (request, "AppBlog/inicio.html",{'mensaje': f"Bienvenido {usuario}"})
            else:
                messages.info(request,'usuario o contraseña incorrectos')
                #return render (request, 'AppCoder/login.html', {'mensaje': 'Usuarios o contraseña incorrectos'}) 

        else:
            form = AuthenticationForm()
        return render (request, "AppBlog/login.html", {'form': form})

                    
#REGISTER

def register (request):
    if request.user.is_authenticated:
     return redirect("inicio")
    else:
        if request.method == 'POST':
            form = formulario_registro(request.POST)
            if form.is_valid():
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(request, 'tu cuenta fue creada' + user)
                return redirect ('login')
            else: 
                return render (request,'AppBlog/registro.html',{'form':form})      
        else: 
            form= formulario_registro()
            return render (request,'AppBlog/registro.html',{'form':form})
            
    
 #---LOGOUT--- 
 
def logout_user (request):
    logout(request)
    messages.success(request,("usted se aca de deslogear"))
    return redirect ("inicio")
         
    
#---AVATAR---  




def agregar_avatar(request):
    if request.method =='POST':
        formulario = Avatar_formulario (request.POST, request.FILES)
        if formulario.is_valid():
            avatar_viejo = Avatar.objects.filter(user=request.user)
            if (len(avatar_viejo)>0):
                avatar_viejo.delete()
            avatar_1 =Avatar(user=request.user, imagen =formulario.cleaned_data['imagen'])
            avatar_1.save()
            return render (request,'AppBlog/inicio.html',{'usuario': request.user,'mensaje': 'AVATAR AGREGADO EXITOSAMENTE','imagen': obtener_avatar(request)})       
    else:
        formulario = Avatar_formulario()
        return render (request, 'AppBlog/agregar_avatar.html',{'form':formulario,'usuario':request.user,'imagen': obtener_avatar(request)})  
    
   
    #-----------------------------------
def obtener_avatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
            imagen=lista[0].imagen.url
    else:
        imagen="HOLA"
    return imagen   

'''def tus_posteos(request):
    lista = PostModel.objects.filter(user=request.user)
    if len(lista)!=0:
        posteo=lista[0].imagen.url
    else:
        posteo= ""
    return render (request,'AppBlog/posteos/lista_post.html',{'posteo':posteo ,'imagen': obtener_avatar(request)})
  '''
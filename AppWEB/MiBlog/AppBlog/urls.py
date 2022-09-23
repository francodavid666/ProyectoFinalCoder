from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ("", Login_request, name = 'login'),
    path ('inicio/', inicio, name= 'inicio'),
    
   
    path ('llenar_formulario/', formulario_usuario, name= 'llenar_formulario'),
    path ("formulario_creado/", formulario_creado, name = 'formulario_creado'),
    
    path ("lista_usuarios/", lista_usuarios, name = "lista_usuarios"),
    path ("buscar/",buscar, name = "buscar"),
    path ("resultado_busqueda/",resultado_busqueda, name = "resultado_busqueda"),
    
    
    path ("registro/", registro_request, name = 'registro'),
    path ("creado/", creado, name = 'creado'),
    path ("logout/", LogoutView.as_view(template_name = "AppBlog/logout.html"), name = 'logout'),
    path ("editar_perfil/",editar_perfil, name = 'editar_perfil'),
    
   
    
    
]


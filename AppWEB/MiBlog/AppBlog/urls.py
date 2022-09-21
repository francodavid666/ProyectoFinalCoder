from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ('', inicio, name= 'inicio'),
    path ('ingresar/', ingresar, name= 'ingresar'),
    path ('crear_usuario/', crear_usuario, name= 'crear_usuario'),
    path ("usuario_creado/", usuario_creado, name = 'usuario_creado'),
    path ("login/", Login_request, name = 'login'),
    path ("registro/", registro_request, name = 'registro'),
    path ("creado/", creado, name = 'creado'),
    path ("logout/", LogoutView.as_view(template_name = "AppBlog/logout.html"), name = 'logout'),
    path ("editar_perfil/",editar_perfil, name = 'editar_perfil'),
]


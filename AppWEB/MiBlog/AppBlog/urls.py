from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

# para el ckeditor
from django.conf import settings
from django.conf.urls.static import static
#Views de autenticacion
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ("", Login_request, name = 'login'),
    path ('inicio', inicio, name= 'inicio'),
    path ('articulo/',articulo, name= 'articulo'),
    
   
    path ('llenar_formulario/', formulario_usuario, name= 'llenar_formulario'),
    path ("formulario_creado/", formulario_creado, name = 'formulario_creado'),
    path ("editar_formulario/<id>", editar_formulario, name = 'editar_formulario'),
    path ("eliminar_formulario/", eliminar_formulario, name ='eliminar_formulario'),
    path ("lista_usuarios/", lista_usuarios, name = "lista_usuarios"),
    path ("buscar/",buscar, name = "buscar"),
    path ("resultado_busqueda/",resultado_busqueda, name = "resultado_busqueda"),
    
    
    path ("registro/", registro_request, name = 'registro'),
    path ("creado/", creado, name = 'creado'),
    path ("logout/", LogoutView.as_view(template_name = "AppBlog/logout.html"), name = 'logout'),
    path ("editar_perfil/",editar_perfil, name = 'editar_perfil'),
 #PKEDITOR   
    path('detalle/', detalle, name='detalle'),
    path('ckeditor/', include ('ckeditor_uploader.urls')),
    
    path ('eliminar_post/', eliminar_post, name = 'eliminar_post'),
    path ('lista_post/', lista_post, name = 'lista_post'),
    
    
    path ('crear_post/', crear_post, name ='crear_post'),
    
    path ('buscar_posteo/', buscar_posteo, name='buscar_posteo'),
    path ('resultado_busqueda_posteo/', resultado_busqueda_posteo, name='resultado_busqueda_posteo'),
   
    path ('eliminar_post_individual/<id>', eliminar_post_individual, name='eliminar_post_individual'),  
    path ('ver_posteo/<str:titulox>/', ver_posteo, name='ver_posteo'),  
    path ('editar_posteo/<id>', editar_posteo, name='editar_posteo'),  
    path ('posteo_editado/', posteo_editado , name='posteo_editado'),  
    
    
    #agregar avatar
    path ('agregar_avatar/', agregar_avatar, name = 'agregar_avatar'),
    
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)


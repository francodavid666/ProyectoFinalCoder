from urllib.parse import urlparse
from django.urls import path
from .views import*


urlpatterns = [
 path ('', inicio,name = 'inicio'),  
 path ("autos/", autos, name = 'autoss'),
 path ("juegos/", juegos, name = 'juegoss'),
 path ("gatos/", juegos, name = 'gatoss'),
 path ("formulario/", fformulario, name = 'formularioss'),
 ]
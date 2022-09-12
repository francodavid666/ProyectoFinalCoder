from urllib.parse import urlparse
from django.urls import path
from .views import*


urlpatterns = [
 path ('', inicio,name = 'inicio'),  
 path ("autos/", autos, name = 'autoss'),
 path ("create_auto/",  CreateAuto,name = 'CreateAuto'),
 path ("buscar_auto/", buscar, name = 'buscar'),
 path('view-auto/', ViewAutos, name = 'ViewAuto'),
 path('editar-auto/', Editar_auto, name = 'editar_auto'),
 ]
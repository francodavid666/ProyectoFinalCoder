from urllib.parse import urlparse
from django.urls import path
from .views import*


urlpatterns = [
 path ('', inicio,name = 'inicio'),  
 path ("autos/", autos, name = 'autoss'),
 path ("juegos/", juegos, name = 'juegoss'),
 path ("gatos/", juegos, name = 'gatoss'),
 path ("formulario/", fformulario, name = 'formularioss'),
 path ("auto_form/",  autos_formulario,name = 'pagina_auto'),
 path ("busquedaPersona/", busquedaPersona, name = 'busqueda_persona'),
 path ("buscar/", buscar, name = 'buscar'),
 #
path('create-auto/', Create_auto.as_view(), name = 'create_auto'),
path('search-auto/', Search_auto, name = 'search_auto'),
path('detail-auto/<int:pk>/', Detail_auto.as_view(), name = 'detail_auto'),
path('delete-auto/<int:pk>/', Delete_auto.as_view(), name = 'delete_auto'),
path('update-auto/<int:pk>/', Update_auto.as_view(), name = 'update_auto'),
path('list-auto/', List_auto.as_view(), name = 'ListAuto'),
 ]
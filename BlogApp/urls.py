from django.urls import path
from BlogApp.views import action_buscar_articulo, buscar_articulos, crear_articulo, crear_blogger, crear_interface, crear_profesion, inicio, articulos, administracion

urlpatterns = [
    path('', inicio, name="inicio"),
    path('articulos', articulos , name="articulos"),
    path('administracion', administracion, name="administracion"),
    path('crear-datos', crear_interface, name="crear-datos"),
    path('crear-profesion', crear_profesion, name="crear-profesion"),
    path('crear-blogger', crear_blogger, name="crear-blogger"),
    path('crear-articulo', crear_articulo, name="crear-articulo"),
    path('buscar-articulos', buscar_articulos, name="buscar-articulos"),
    path('action-buscar-articulo', action_buscar_articulo, name="action-buscar-articulo"),

] 

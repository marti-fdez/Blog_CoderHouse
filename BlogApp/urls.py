from django.urls import path
from BlogApp.views import action_eliminar_profesion, action_buscar_articulo, buscar_articulos, crear_articulo, crear_blogger, crear_datos, crear_profesion, inicio, articulos, administracion, eliminar_datos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('articulos', articulos , name="articulos"),
    path('administracion', administracion, name="administracion"),

    #CREATE
    path('crear-datos', crear_datos, name="crear-datos"),
    path('crear-profesion', crear_profesion, name="crear-profesion"),
    path('crear-blogger', crear_blogger, name="crear-blogger"),
    path('crear-articulo', crear_articulo, name="crear-articulo"),

    #UPDATE


    #DELETE
    path('eliminar-datos', eliminar_datos, name="eliminar-datos"),
    path('action-eliminar-profesion/<int:id>/', action_eliminar_profesion, name="action-eliminar-profesion"),
    

    #BÚSQUEDA
    path('buscar-articulos', buscar_articulos, name="buscar-articulos"),
    path('action-buscar-articulo', action_buscar_articulo, name="action-buscar-articulo"),
] 
from django.urls import path
from BlogApp.views import action_buscar_articulo, buscar_posts, crear_articulo, crear_blogger, crear_interface, crear_profesion, inicio, posts

urlpatterns = [
    path('', inicio, name="inicio"),
    path('posts', posts, name="posts"),
    path('crear-interface', crear_interface, name="crear-interface"),
    path('crear-profesion', crear_profesion, name="crear-profesion"),
    path('crear-blogger', crear_blogger, name="crear-blogger"),
    path('crear-articulo', crear_articulo, name="crear-articulo"),
    path('buscar-posts', buscar_posts, name="buscar-posts"),
    path('action-buscar-articulo', action_buscar_articulo, name="action-buscar-articulo"),

] 

from django.urls import path
from BlogApp.views import ArticuloDeleteView, ArticuloDetailView, ArticuloListView, ArticuloUpdateView, about, action_buscar_articulo, buscar_articulos, crear_articulo, inicio, articulos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('crear-articulo', crear_articulo, name="crear-articulo"),
    path('buscar-articulos', buscar_articulos, name="buscar-articulos"),
    path('action-buscar-articulo', action_buscar_articulo, name="action-buscar-articulo"),  # type: ignore
    path('editar-articulo/<int:pk>/', ArticuloUpdateView.as_view(), name="editar-articulo"),
    path('listar-articulos', ArticuloListView.as_view(), name="listar-articulos"),
    path('detalle-articulo/<int:pk>/', ArticuloDetailView.as_view(), name="detalle-articulo"),
    path('eliminar-articulo/<int:pk>/', ArticuloDeleteView.as_view(), name="eliminar-articulo"),
] 


from django.shortcuts import render
from django.urls import reverse

from BlogApp.forms import BuscarArticulo, CrearArticulo, CrearBlogger, CrearProfesion
from BlogApp.models import Articulo, Profesion, Blogger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "BlogApp/index.html")

def articulos(request):
    return render(request, "BlogApp/articulos.html")

@login_required
def administracion(request):
    return render(request, "BlogApp/administracion.html")

@login_required
def crear_datos(request):
    formulario_profesion = CrearProfesion()
    formulario_blogger = CrearBlogger()
    formulario_articulo = CrearArticulo()
    return render(request, "BlogApp/crear_datos.html", {'formulario_profesion': formulario_profesion, 'formulario_blogger': formulario_blogger, 'formulario_articulo': formulario_articulo})

@login_required
def crear_profesion(request):
    formulario = CrearProfesion(request.POST)
    if formulario.is_valid():
        data = formulario.cleaned_data
        profesion = Profesion(nombre=data['nombre'],sueldo=data['sueldo'])
        profesion.save()
        mensaje = "¡Profesión creada con éxito!"
        return render(request, 'BlogApp/administracion.html', {'mensaje': mensaje})
    else:   
        mensaje = "¡Ha ocurrido un error creando la Profesión!"
        return render(request, 'BlogApp/administracion.html', {'mensaje': mensaje})
        
@login_required
def crear_blogger(request):
    formulario = CrearBlogger(request.POST)
    if formulario.is_valid():
        data = formulario.cleaned_data
        try:
            profesion_elegida = Profesion.objects.get(nombre=data['profesion'])
        except Profesion.DoesNotExist: 
            mensaje = "¡NO existe esa Profesión!"
            formulario_profesion = CrearProfesion()
            formulario_blogger = CrearBlogger()
            formulario_articulo = CrearArticulo()
            return render(request, 'BlogApp/crear_datos.html', {'mensaje': mensaje, 'formulario_profesion': formulario_profesion, 'formulario_blogger': formulario_blogger, 'formulario_articulo': formulario_articulo})
        else:
            blogger = Blogger(nombre=data['nombre'],apellido=data['apellido'], profesion=profesion_elegida, telefono=data['telefono'], email=data['email'])
            blogger.save()
            mensaje = "¡Blogger creado con éxito!"
            return render(request, 'BlogApp/administracion.html', {'mensaje': mensaje})
    else:   
        mensaje = "¡Ha ocurrido un error creando el Blogger!"
        return render(request, 'BlogApp/administracion.html', {'mensaje': mensaje})
        
@login_required
def crear_articulo(request):
    formulario = CrearArticulo(request.POST)
    if formulario.is_valid():
        data = formulario.cleaned_data
        try:
            autor_elegido = Blogger.objects.get(nombre=data['autor'])
        except Blogger.DoesNotExist:
            mensaje = "¡NO existe ese Autor!"
            formulario_profesion = CrearProfesion()
            formulario_blogger = CrearBlogger()
            formulario_articulo = CrearArticulo()
            return render(request, 'BlogApp/crear_datos.html', {'mensaje': mensaje, 'formulario_profesion': formulario_profesion, 'formulario_blogger': formulario_blogger, 'formulario_articulo': formulario_articulo})
        else:    
            articulo = Articulo(autor=autor_elegido,nombre = data["nombre"],fecha_publicacion=data['fecha_publicacion'], tematica=data['tematica'], cantidad_paginas=data['cantidad_paginas'])
            articulo.save()
            mensaje = "¡Artículo creado con éxito!"
            return render(request, 'BlogApp/administracion.html', {'mensaje': mensaje})
    else:   
        mensaje = "¡Ha ocurrido un error creando el Artículo!"
        return render(request, 'BlogApp/administracion.html', {'mensaje': mensaje})

def buscar_articulos(request):
    formulario_buscar = BuscarArticulo()
    return render(request, 'BlogApp/buscar_articulos.html', {'formulario_buscar': formulario_buscar, "articulo_buscado": False})

def action_buscar_articulo(request):
    articulo_buscado = {}  
    formulario = BuscarArticulo(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        articulo_buscado = Articulo.objects.filter(tematica__icontains=data['tematica'])
        if articulo_buscado.exists():
            formulario_buscar = BuscarArticulo()
            return render(request, 'BlogApp/buscar_articulos.html', {'formulario_buscar': formulario_buscar, "articulo_buscado": articulo_buscado, "articulo_encontrado": True})
        else:    
            formulario_buscar = BuscarArticulo()
            return render(request, 'BlogApp/buscar_articulos.html', {'formulario_buscar': formulario_buscar,"articulo_buscado": True, "articulo_encontrado": False,"data":data['tematica']})
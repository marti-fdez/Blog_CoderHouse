
from django.shortcuts import render
from django.urls import reverse

from BlogApp.forms import BuscarArticulo, CrearArticulo
from BlogApp.models import Articulo

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.urls import reverse, reverse_lazy

# Create your views here.

def inicio(request):
    ultimo_articulo = Articulo.objects.latest('id')
    return render(request, "BlogApp/index.html", {'ultimo_articulo':ultimo_articulo})

def articulos(request):
    return render(request, "BlogApp/articulos.html")

def about(request):
    return render(request, "BlogApp/about.html")
        
@login_required
def crear_articulo(request):
    if request.method == 'POST':
        formulario = CrearArticulo(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            autor_elegido = request.user
            articulo = Articulo(autor=autor_elegido,titulo = data["titulo"],subtitulo=data["subtitulo"],cuerpo=data["cuerpo"],fecha_publicacion=data['fecha_publicacion'], imagen=data["imagen"], tematica=data['tematica'])
            articulo.save()
            mensaje = "¡Artículo creado con éxito!"
            return render(request, 'BlogApp/success.html', {'mensaje': mensaje})
        else:   
            mensaje = "¡Ha ocurrido un error creando el Artículo!"
            return render(request, 'BlogApp/articulos.html', {'mensaje': mensaje})
    form = CrearArticulo()
    return render(request, "BlogApp/crear_datos.html", {'form': form})

def buscar_articulos(request):
    formulario_buscar = BuscarArticulo()
    return render(request, 'BlogApp/buscar_articulos.html', {'formulario_buscar': formulario_buscar, "articulo_buscado": False})

from django.db.models import Q

def action_buscar_articulo(request):
    articulo_buscado = {}  
    formulario = BuscarArticulo(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        articulo_buscado = Articulo.objects.filter(Q(titulo__icontains=data['busqueda']) | Q(subtitulo__icontains=data['busqueda']) | Q(cuerpo__icontains=data['busqueda'])).distinct().order_by("autor") 
        if articulo_buscado.exists():
            formulario_buscar = BuscarArticulo()
            return render(request, 'BlogApp/buscar_articulos.html', {'formulario_buscar': formulario_buscar, "articulo_buscado": articulo_buscado, "articulo_encontrado": True})
        else:    
            formulario_buscar = BuscarArticulo()
            return render(request, 'BlogApp/buscar_articulos.html', {'formulario_buscar': formulario_buscar,"articulo_buscado": True, "articulo_encontrado": False,"data":data['busqueda']})

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ['titulo', 'subtitulo', 'cuerpo', 'fecha_publicacion', 'imagen', 'tematica']
    success_url = reverse_lazy('listar-articulos')
    template_name= "BlogApp/crear_datos.html"

class ArticuloListView(ListView):
    model = Articulo
    template_name = "BlogApp/articulos.html"

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "BlogApp/articulo.html"

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name= "BlogApp/eliminar.html"
    success_url= reverse_lazy('listar-articulos')
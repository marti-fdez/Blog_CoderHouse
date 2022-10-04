
from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    cuerpo = RichTextField()
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    tematica = models.CharField(max_length=250)
    def __str__(self):
        return f"Articulo de {self.titulo}"

from django.db import models
from django.contrib.auth.models import User
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    cuerpo = models.CharField(max_length=700)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    tematica = models.CharField(max_length=250)
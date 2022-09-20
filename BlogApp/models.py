
from django.db import models


# Create your models here.
class Profesion(models.Model):
    nombre = models.CharField(max_length=100)
    sueldo = models.IntegerField()

class Blogger(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.ForeignKey('Profesion', on_delete = models.SET_NULL, null=True)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()


class Articulo(models.Model):
    autor = models.ForeignKey('Blogger', on_delete = models.CASCADE)
    nombre = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    tematica = models.CharField(max_length=250)
    cantidad_paginas = models.IntegerField()
import email
from django import forms

class CrearProfesion(forms.Form):
    nombre = forms.CharField(max_length=100)
    sueldo = forms.IntegerField()


class CrearBlogger(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    profesion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=100)
    email = forms.EmailField()

class CrearArticulo(forms.Form):
    autor = forms.CharField(max_length=100)
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))
    tematica = forms.CharField(max_length=100)
    cantidad_paginas = forms.IntegerField()

class BuscarArticulo(forms.Form):
    tematica=forms.CharField(max_length=100)
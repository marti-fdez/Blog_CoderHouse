
from django import forms

from ckeditor.fields import RichTextFormField

class CrearArticulo(forms.Form):
    titulo = forms.CharField(max_length=250)
    subtitulo = forms.CharField(max_length=250)
    cuerpo = RichTextFormField()
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))
    imagen = forms.ImageField()
    tematica = forms.CharField(max_length=100)

class BuscarArticulo(forms.Form):
    busqueda=forms.CharField(max_length=100)

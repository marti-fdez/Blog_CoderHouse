
from django import forms

class CrearArticulo(forms.Form):
    titulo = forms.CharField(max_length=250)
    subtitulo = forms.CharField(max_length=250)
    cuerpo = forms.CharField(max_length=700)
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))
    imagen = forms.ImageField()
    tematica = forms.CharField(max_length=100)

class BuscarArticulo(forms.Form):
    busqueda=forms.CharField(max_length=100)

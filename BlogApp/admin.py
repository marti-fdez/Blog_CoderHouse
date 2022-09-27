from atexit import register
from django.contrib import admin
from BlogApp.models import Articulo
# Register your models here.
admin.site.register(Articulo)

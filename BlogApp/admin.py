from atexit import register
from django.contrib import admin
from BlogApp.models import Articulo, Profesion, Blogger
# Register your models here.
admin.site.register(Articulo)
admin.site.register(Profesion)
admin.site.register(Blogger)

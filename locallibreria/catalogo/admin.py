from django.contrib import admin

# Register your models here.
from . models import Producto, Marca,Compra

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Compra)
from django.contrib import admin
from .models import *

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'description', 'precio', 'stock']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(Categoria)
admin.site.register(Producto, ProductosAdmin)
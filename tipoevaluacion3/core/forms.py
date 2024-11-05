from django import forms
from django.forms import ModelForm
from .models import *

# Crear un template para poder usarlo en el html
class ProductoForm(ModelForm):
    
    precio = forms.IntegerField(min_value=1)
    
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'description', 'precio', 'fecha_venc', 'imagen', 'stock', 'stars']
        
        widgets = {
            'fecha_venc': forms.SelectDateWidget(years=range(2024, 2050))
        }